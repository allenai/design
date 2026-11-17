#!/usr/bin/env python3
"""Load Microsoft's Accessibility Considerations Toolkit at a reviewed, pinned commit.

Follows the toolkit's own guidance for downstream consumers: pin a reviewed
immutable commit (never a branch), verify an exact distribution hash, and
review every update before it is used.

  toolkit.py fetch          Download (or reuse) the pinned toolkit; print where it is.
  toolkit.py bump [--sha S] [--summary FILE]
                            Move the pin in toolkit.lock to S (default: the newest
                            upstream commit touching the toolkit). Exit 3 if already
                            there. Used by the a11y-toolkit-pin workflow, which opens
                            a PR for review; never merge a bump unread.

The pin lives in toolkit.lock next to this skill. A copy of the skill outside
allenai/design (e.g. ~/.claude/skills/a11y) reads the pin from allenai/design's
main branch instead, so it follows reviewed bumps without being re-copied.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

UPSTREAM = "microsoft/Microsoft-Accessibility"
UPSTREAM_GIT = f"https://github.com/{UPSTREAM}.git"
TK = "Accessibility-Considerations-Toolkit"
# The parts the skill reads. Generated YAML, tests and tooling are not needed.
PARTS = ["considerations", "heuristics", "methodology", "standards", "provenance.json", "LICENSE.txt"]
DESIGN_LOCK_URL = "https://raw.githubusercontent.com/allenai/design/main/.claude/skills/a11y/toolkit.lock"

SKILL_DIR = Path(__file__).resolve().parent.parent
LOCK = SKILL_DIR / "toolkit.lock"
CACHE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "a11y-act"


def git(*args, cwd=None, capture=False):
    r = subprocess.run(["git", *args], cwd=cwd, check=True, text=True,
                       stdout=subprocess.PIPE if capture else subprocess.DEVNULL,
                       stderr=subprocess.PIPE)
    return r.stdout.strip() if capture else None


def parse_lock(text):
    lock = dict(re.findall(r"^([a-z0-9_]+)=(\S+)\s*$", text, re.M))
    if not re.fullmatch(r"[0-9a-f]{40}", lock.get("commit", "")) or \
       not re.fullmatch(r"[0-9a-f]{64}", lock.get("distribution_sha256", "")):
        raise SystemExit("toolkit.lock is missing a valid commit or distribution_sha256")
    return lock


def in_design_repo():
    try:
        url = git("config", "--get", "remote.origin.url", cwd=SKILL_DIR, capture=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return "allenai/design" in url


def read_pin():
    """The repo copy uses its own lock (so a branch can test a bump); any other copy
    uses the lock on allenai/design main, falling back to its bundled one offline."""
    if in_design_repo():
        return parse_lock(LOCK.read_text()), "allenai/design checkout"
    try:
        with urllib.request.urlopen(DESIGN_LOCK_URL, timeout=10) as r:
            return parse_lock(r.read().decode()), "allenai/design main"
    except Exception as e:  # offline, or the repo moved
        print(f"note: couldn't read the pin from allenai/design main ({e}); using the bundled lock",
              file=sys.stderr)
        return parse_lock(LOCK.read_text()), "bundled toolkit.lock"


def distribution_hash(root):
    """sha256 over every vendored file's path and content, in a fixed order."""
    lines = []
    for part in PARTS:
        p = root / part
        files = [p] if p.is_file() else sorted(f for f in p.rglob("*") if f.is_file())
        for f in files:
            rel = f.relative_to(root).as_posix()
            lines.append(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {rel}\n")
    return hashlib.sha256("".join(lines).encode()).hexdigest()


def download(commit, dest):
    """Sparse, shallow checkout of just PARTS at one commit into dest/<TK>."""
    dest.mkdir(parents=True)
    git("init", "-q", cwd=dest)
    git("remote", "add", "origin", UPSTREAM_GIT, cwd=dest)
    git("sparse-checkout", "set", "--no-cone", *[f"/{TK}/{p}" for p in PARTS], cwd=dest)
    git("fetch", "-q", "--depth", "1", "origin", commit, cwd=dest)
    git("checkout", "-q", "FETCH_HEAD", cwd=dest)
    got = git("rev-parse", "HEAD", cwd=dest, capture=True)
    if got != commit:
        raise SystemExit(f"asked for {commit}, got {got}")
    missing = [p for p in PARTS if not (dest / TK / p).exists()]
    if missing:
        raise SystemExit(f"upstream {commit[:7]} has no {', '.join(missing)}: the toolkit layout changed")
    shutil.rmtree(dest / ".git")
    return dest / TK


def cmd_fetch(_):
    lock, source = read_pin()
    commit, want = lock["commit"], lock["distribution_sha256"]
    root = CACHE / commit / TK
    if not root.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        tmp = Path(tempfile.mkdtemp(prefix=".tmp-", dir=CACHE))
        try:
            download(commit, tmp / "x")
            (CACHE / commit).parent.mkdir(parents=True, exist_ok=True)
            if not (CACHE / commit).exists():
                (tmp / "x").rename(CACHE / commit)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    got = distribution_hash(root)
    if got != want:
        shutil.rmtree(CACHE / commit, ignore_errors=True)
        raise SystemExit(f"distribution hash mismatch for {commit[:7]}: expected {want}, got {got}. "
                         "Not using it.")
    os.utime(CACHE / commit)
    # Keep the three most recently used commits.
    olds = sorted((d for d in CACHE.iterdir() if d.is_dir() and not d.name.startswith(".")),
                  key=lambda d: d.stat().st_mtime, reverse=True)[3:]
    for d in olds:
        shutil.rmtree(d, ignore_errors=True)
    print(f"ACT_DIR={root}")
    print(f"ACT_COMMIT={commit}")
    print(f"PIN_SOURCE={source}")


def latest_upstream_commit():
    req = urllib.request.Request(f"https://api.github.com/repos/{UPSTREAM}/commits?path={TK}&per_page=1")
    if os.environ.get("GH_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GH_TOKEN']}")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)[0]["sha"]


def skill_refs_missing(root):
    """Files SKILL.md names that the new commit no longer has (upstream renames paths)."""
    text = (SKILL_DIR / "SKILL.md").read_text()
    refs = set(re.findall(r"\b(?:considerations|methodology|heuristics|standards)/[A-Za-z0-9._-]+\.md", text))
    refs |= {f"considerations/{m}" for m in re.findall(r"\b4\.2\.\d+-[a-z-]+\.md", text)}
    return sorted(r for r in refs if not (root / r).exists())


def cmd_bump(args):
    lock = parse_lock(LOCK.read_text())
    old = lock["commit"]
    new = args.sha or latest_upstream_commit()
    if new == old:
        print(f"Already pinned to {old}.", file=sys.stderr)
        return 3
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        root = download(new, t / "new")
        digest = distribution_hash(root)
        missing = skill_refs_missing(root)

        # Diff the two commits for review, using a shallow fetch of both.
        d = t / "diff"
        d.mkdir()
        git("init", "-q", cwd=d)
        git("remote", "add", "origin", UPSTREAM_GIT, cwd=d)
        git("fetch", "-q", "--depth", "1", "origin", old, new, cwd=d)
        paths = [f"{TK}/{p}" for p in PARTS]
        stat = git("diff", "--stat", old, new, "--", *paths, cwd=d, capture=True)
        added = git("diff", "-U0", old, new, "--", *paths, cwd=d, capture=True)
        meta = git("log", "-1", "--format=%cs%x09%s", new, cwd=d, capture=True)
    date, _, subject = meta.partition("\t")
    flags = [l for l in added.splitlines()
             if l.startswith("+") and not l.startswith("+++")
             and re.search(r"ignore (all|previous|the above)|system prompt|api[_ -]?key|password|secret|"
                           r"curl |wget |https?://", l, re.I)][:20]

    LOCK.write_text(LOCK.read_text()
                    .replace(old, new)
                    .replace(lock["distribution_sha256"], digest)
                    .replace(f"date={lock.get('date', '')}", f"date={date}"))

    body = [
        "Moves the `/a11y` skill's pin on Microsoft's Accessibility Considerations Toolkit.",
        "",
        f"- From `{old[:7]}` to `{new[:7]}` ({date}, \"{subject}\")",
        f"- Upstream diff: https://github.com/{UPSTREAM}/compare/{old}...{new}",
        "",
        "### Changed files",
        "```", stat or "(no changes in the parts /a11y reads)", "```",
    ]
    if missing:
        body += ["", "### ⚠️ SKILL.md names files this commit doesn't have",
                 *[f"- `{m}`" for m in missing], "",
                 "Update `SKILL.md` in this PR before merging."]
    body += ["", "### Review before merging",
             "This content is loaded into Claude's context whenever `/a11y` runs, so read the upstream "
             "diff, not just the stat. Microsoft asks consumers to review each update before using it."]
    if flags:
        body += ["", "Added lines worth a closer look (URLs, credentials, instruction-like text):",
                 "```", *flags, "```"]
    text = "\n".join(body) + "\n"
    if args.summary:
        Path(args.summary).write_text(text)
    else:
        print(text)
    print(f"Pinned {new}.", file=sys.stderr)
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch").set_defaults(fn=cmd_fetch)
    b = sub.add_parser("bump")
    b.add_argument("--sha")
    b.add_argument("--summary")
    b.set_defaults(fn=cmd_bump)
    args = ap.parse_args()
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    main()
