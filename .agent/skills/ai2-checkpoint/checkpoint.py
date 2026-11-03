#!/usr/bin/env python3
"""
checkpoint — local, branch-scoped snapshots of the working tree you can list,
diff and restore, without committing.

Each checkpoint is a git commit object stored under refs/checkpoints/<branch>,
built from a temporary index. HEAD, the branch, the real index and the remote
are never touched (the same trick `git stash` uses). Untracked files are
included; ignored files are not. Checkpoints never show in `git log`,
`git status`, or a push.

  checkpoint save [-m LABEL]             snapshot the tree (no-op if nothing changed)
  checkpoint list                        the checkpoints on this branch
  checkpoint diff A [B] [-p] [-- PATHS]  compare two points (B defaults to `now`)
  checkpoint show ID [PATH]              a checkpoint's summary, or a file as it was then
  checkpoint restore ID [PATHS...]       make the tree match a checkpoint (saves one first)
  checkpoint clear [--all]               drop this branch's checkpoints (or every branch's)

IDs: cp3 or 3 (ordinal, oldest first), last, now (the current tree), or any
git revision (HEAD, main, a sha).
"""

import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

NS = "refs/checkpoints"


class Fail(Exception):
    pass


def git(args, *, cwd=None, env=None, input=None, binary=False, ok=(0,)):
    r = subprocess.run(
        ["git", *args],
        cwd=cwd,
        env=env,
        input=input,
        capture_output=True,
        text=not binary,
    )
    if r.returncode not in ok:
        err = r.stderr if isinstance(r.stderr, str) else r.stderr.decode(errors="replace")
        raise Fail(f"git {' '.join(args)} failed:\n{err.strip()}")
    if binary:
        return r.stdout
    return r.stdout.rstrip("\n")


def try_git(args, cwd=None):
    """A revision lookup that may legitimately fail: returns the sha or None."""
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


class Repo:
    def __init__(self):
        root = try_git(["rev-parse", "--show-toplevel"])
        if not root:
            raise Fail("not inside a git repository")
        self.root = root
        self.git_dir = git(["rev-parse", "--absolute-git-dir"], cwd=root)
        branch = try_git(["symbolic-ref", "--short", "-q", "HEAD"], cwd=root)
        if not branch:
            head = self.head()
            branch = f"detached-{head[:7]}" if head else "detached"
        self.branch = branch
        self.ref = f"{NS}/{branch}"

    # -- revisions -----------------------------------------------------------

    def head(self):
        return try_git(["rev-parse", "-q", "--verify", "HEAD"], cwd=self.root)

    def tip(self):
        return try_git(["rev-parse", "-q", "--verify", self.ref], cwd=self.root)

    def count(self):
        return int(git(["rev-list", "--count", self.ref], cwd=self.root)) if self.tip() else 0

    def tree_of(self, rev):
        return git(["rev-parse", f"{rev}^{{tree}}"], cwd=self.root)

    def snapshot_tree(self):
        """Write the working tree (tracked + untracked, minus ignored) as a tree
        object, through a throwaway copy of the index."""
        with tempfile.TemporaryDirectory() as d:
            idx = os.path.join(d, "index")
            real = os.path.join(self.git_dir, "index")
            if os.path.exists(real):
                shutil.copyfile(real, idx)
            env = {**os.environ, "GIT_INDEX_FILE": idx}
            git(["add", "-A", "--", "."], cwd=self.root, env=env)
            return git(["write-tree"], cwd=self.root, env=env)

    def entries(self):
        """Every checkpoint on this branch, oldest first."""
        if not self.tip():
            return []
        out = git(
            ["log", "--reverse", "--format=%H%x00%ct%x00%s%x00%b%x1e", self.ref],
            cwd=self.root,
        )
        items = []
        for i, rec in enumerate(filter(None, out.split("\x1e")), 1):
            sha, ct, subject, body = rec.lstrip("\n").split("\x00", 3)
            m = re.search(r"^Base: (\S+)", body, re.M)
            items.append(
                dict(n=i, sha=sha, time=int(ct), label=subject, base=m.group(1) if m else None)
            )
        return items

    def resolve(self, idstr):
        """A checkpoint id, `now`, or any git revision → (display name, object sha)."""
        if idstr == "now":
            return "now", self.snapshot_tree()
        m = re.fullmatch(r"(?:cp)?(\d+)", idstr)
        if m:
            n, total = int(m.group(1)), self.count()
            if not 1 <= n <= total:
                raise Fail(f"no checkpoint cp{n} on {self.branch} ({total} saved)")
            return f"cp{n}", git(["rev-parse", f"{self.ref}~{total - n}"], cwd=self.root)
        if idstr in ("last", "latest"):
            total = self.count()
            if not total:
                raise Fail(f"no checkpoints on {self.branch} yet")
            return f"cp{total}", self.tip()
        sha = try_git(["rev-parse", "-q", "--verify", f"{idstr}^{{object}}"], cwd=self.root)
        if not sha:
            raise Fail(f"'{idstr}' is neither a checkpoint id nor a git revision")
        return idstr, sha

    def relpath(self, p):
        rel = os.path.relpath(os.path.abspath(p), self.root)
        return p if rel.startswith("..") else rel

    def stat(self, a, b):
        """'7 files, +120 −3' between two tree-ish objects."""
        out = git(["diff-tree", "-r", "--shortstat", a, b], cwd=self.root)
        if not out.strip():
            return "no changes"
        files = re.search(r"(\d+) files? changed", out)
        ins = re.search(r"(\d+) insertion", out)
        dels = re.search(r"(\d+) deletion", out)
        parts = [f"{files.group(1)} file{'s' if files.group(1) != '1' else ''}"]
        parts.append(f"+{ins.group(1) if ins else 0} −{dels.group(1) if dels else 0}")
        return ", ".join(parts)


# -- helpers --------------------------------------------------------------------


def when(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    today = datetime.date.today()
    delta = time.time() - ts
    if delta < 60:
        rel = "just now"
    elif delta < 3600:
        rel = f"{int(delta // 60)}m ago"
    elif dt.date() == today:
        rel = f"{int(delta // 3600)}h ago"
    elif dt.date() == today - datetime.timedelta(days=1):
        rel = "yesterday"
    else:
        rel = f"{int(delta // 86400)}d ago"
    clock = dt.strftime("%H:%M") if dt.date() == today else dt.strftime("%b %d %H:%M")
    return f"{rel}, {clock}"


def table(rows, headers):
    widths = [max(len(str(r[i])) for r in [headers, *rows]) for i in range(len(headers))]
    fmt = "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers).rstrip())
    for r in rows:
        print(fmt.format(*[str(c) for c in r]).rstrip())


def save(repo, label, *, quiet):
    """Save a checkpoint; returns its ordinal, or None when nothing changed."""
    tree = repo.snapshot_tree()
    tip = repo.tip()
    if tip and repo.tree_of(tip) == tree:
        if not quiet:
            print(f"Nothing changed since cp{repo.count()} — no checkpoint saved.")
        return None
    head = repo.head()
    msg = f"{label}\n\nBranch: {repo.branch}\nBase: {head or 'none'}\n"
    parents = ["-p", tip] if tip else []
    commit = git(["commit-tree", tree, *parents], cwd=repo.root, input=msg)
    git(["update-ref", repo.ref, commit, tip or ""], cwd=repo.root)
    n = repo.count()
    prev = tip or head
    change = f"{repo.stat(prev, commit)}{'' if tip else f' vs commit {head[:7]}'}" if prev else "first snapshot"
    print(f"Saved cp{n} — {label}  ({change})")
    return n


# -- commands -------------------------------------------------------------------


def cmd_save(repo, args):
    label = args.message or ("auto" if args.auto else "checkpoint")
    save(repo, label, quiet=args.auto)


def cmd_list(repo, args):
    items = repo.entries()
    head = repo.head()
    if not items:
        print(f"No checkpoints on {repo.branch} yet. Save one: checkpoint save -m \"label\"")
        return
    print(f"Checkpoints on {repo.branch}  (HEAD {head[:9] if head else 'none'})\n")
    rows = []
    for e in items:
        prev = items[e["n"] - 2]["sha"] if e["n"] > 1 else e["base"]
        if prev and prev != "none":
            change = repo.stat(prev, e["sha"]) + (f" vs commit {prev[:7]}" if e["n"] == 1 else "")
        else:
            change = "first snapshot"
        rows.append((f"cp{e['n']}", when(e["time"]), e["label"], change))
    table(rows, ("id", "when", "label", "change from previous"))
    now = repo.snapshot_tree()
    last = items[-1]
    drift = repo.stat(last["sha"], now)
    print()
    if drift == "no changes":
        print(f"The working tree matches cp{last['n']}.")
    else:
        print(f"The working tree has moved on from cp{last['n']}: {drift}  (checkpoint diff last)")


def cmd_diff(repo, args):
    rest = list(args.rest)
    ids, i = [], 0
    while i < len(rest) and len(ids) < 2 and not rest[i].startswith("-"):
        ids.append(rest[i])
        i += 1
    if not ids:
        raise Fail("usage: checkpoint diff A [B] [git diff options] [-- paths]")
    extra = rest[i:]
    if "--" in extra:
        k = extra.index("--")
        opts, paths = extra[:k], extra[k + 1 :]
    else:
        opts = [x for x in extra if x.startswith("-")]
        paths = [x for x in extra if not x.startswith("-")]
    if not opts:
        opts = ["--stat=120,90"]
    (la, sa) = repo.resolve(ids[0])
    (lb, sb) = repo.resolve(ids[1] if len(ids) > 1 else "now")
    paths = [repo.relpath(p) for p in paths]
    print(f"{la} → {lb}" + (f"  ({', '.join(paths)})" if paths else ""))
    out = git(["diff", *opts, sa, sb, "--", *paths], cwd=repo.root)
    print(out if out.strip() else "(no differences)")


def cmd_show(repo, args):
    label, sha = repo.resolve(args.id)
    if args.path:
        rel = repo.relpath(args.path)
        exists = try_git(["rev-parse", "-q", "--verify", f"{sha}:{rel}"], cwd=repo.root)
        if not exists:
            raise Fail(f"{rel} does not exist at {label}")
        sys.stdout.buffer.write(git(["cat-file", "blob", f"{sha}:{rel}"], cwd=repo.root, binary=True))
        return
    kind = git(["cat-file", "-t", sha], cwd=repo.root)
    if kind != "commit":
        print(f"{label}: {kind} {sha}")
        return
    subject, date, body = git(["log", "-1", "--format=%s%x00%ci%x00%b", sha], cwd=repo.root).split("\x00", 2)
    print(f"{label} — {subject}\n{date}\n{body.strip()}\n")
    print(git(["diff-tree", "-r", "--root", "--no-commit-id", "--stat=120,90", sha], cwd=repo.root))


def cmd_restore(repo, args):
    label, sha = repo.resolve(args.id)
    target = repo.tree_of(sha) if git(["cat-file", "-t", sha], cwd=repo.root) == "commit" else sha
    paths = [repo.relpath(p) for p in args.paths]
    saved = save(repo, f"before restore to {label}", quiet=True)
    now = repo.snapshot_tree()
    raw = git(
        ["diff-tree", "-r", "--no-renames", "--raw", "-z", target, now, "--", *paths],
        cwd=repo.root,
        binary=True,
    ).decode()
    toks = raw.split("\0")
    pairs = [(toks[j], toks[j + 1]) for j in range(0, len(toks) - 1, 2) if toks[j]]
    if not pairs:
        scope = f" for {', '.join(paths)}" if paths else ""
        print(f"The working tree already matches {label}{scope}.")
        return
    wrote = removed = skipped = 0
    for meta, path in pairs:
        srcmode, _dstmode, srcsha, _dstsha, status = meta.lstrip(":").split()
        full = os.path.join(repo.root, path)
        if status == "A":  # present now, absent at the checkpoint
            if os.path.lexists(full):
                os.remove(full)
            removed += 1
            parent = os.path.dirname(full)
            while parent != repo.root and os.path.isdir(parent) and not os.listdir(parent):
                os.rmdir(parent)
                parent = os.path.dirname(parent)
            continue
        if srcmode == "160000":  # submodule pointer; not ours to move
            skipped += 1
            continue
        os.makedirs(os.path.dirname(full), exist_ok=True)
        blob = git(["cat-file", "blob", srcsha], cwd=repo.root, binary=True)
        if os.path.lexists(full):
            os.remove(full)
        if srcmode == "120000":
            os.symlink(blob.decode(), full)
        else:
            with open(full, "wb") as f:
                f.write(blob)
            mode = os.stat(full).st_mode
            os.chmod(full, (mode | 0o111) if srcmode == "100755" else (mode & ~0o111))
        wrote += 1
    note = f", {skipped} submodule{'s' if skipped != 1 else ''} left alone" if skipped else ""
    print(f"Restored {label}: {wrote} file{'s' if wrote != 1 else ''} written, {removed} removed{note}.")
    if saved:
        print(f"Saved cp{saved} first — `checkpoint restore cp{saved}` undoes this.")


def cmd_clear(repo, args):
    if args.all:
        refs = git(["for-each-ref", "--format=%(refname)", NS], cwd=repo.root).split()
        for r in refs:
            git(["update-ref", "-d", r], cwd=repo.root)
        print(f"Dropped the checkpoints of {len(refs)} branch{'es' if len(refs) != 1 else ''}.")
        return
    n = repo.count()
    if not n:
        print(f"No checkpoints on {repo.branch}.")
        return
    git(["update-ref", "-d", repo.ref], cwd=repo.root)
    print(f"Dropped {n} checkpoint{'s' if n != 1 else ''} on {repo.branch}.")


def main(argv):
    p = argparse.ArgumentParser(prog="checkpoint", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("save", help="snapshot the working tree")
    s.add_argument("-m", "--message", help="a short label for this checkpoint")
    s.add_argument("--auto", action="store_true", help="quiet when nothing changed; never fails (for hooks)")
    sub.add_parser("list", aliases=["ls"], help="list this branch's checkpoints")
    d = sub.add_parser("diff", help="compare two points; B defaults to `now`")
    d.add_argument("rest", nargs=argparse.REMAINDER)
    sh = sub.add_parser("show", help="a checkpoint's summary, or a file as it was then")
    sh.add_argument("id")
    sh.add_argument("path", nargs="?")
    r = sub.add_parser("restore", help="make the working tree match a checkpoint (saves one first)")
    r.add_argument("id")
    r.add_argument("paths", nargs="*")
    c = sub.add_parser("clear", help="drop this branch's checkpoints")
    c.add_argument("--all", action="store_true", help="every branch's")
    args = p.parse_args(argv)
    auto = args.cmd == "save" and args.auto
    try:
        repo = Repo()
        {
            "save": cmd_save,
            "list": cmd_list,
            "ls": cmd_list,
            "diff": cmd_diff,
            "show": cmd_show,
            "restore": cmd_restore,
            "clear": cmd_clear,
        }[args.cmd](repo, args)
    except Fail as e:
        if auto:
            return 0
        print(f"checkpoint: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
