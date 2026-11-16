"""Check that an ER-family change stayed inside EarthRanger, ER Legacy, SERCA and the spec sheet.

Two checks, both against a base ref (default origin/main):

1. Files: every changed file (committed on this branch, staged, unstaged or
   untracked) must be under earthranger/, er-legacy/ or serca/, or be
   spec-sheet.html, or be package.json with only its "version" line changed.
2. Other tabs: spec-sheet.html is shared with every system, so render each
   non-ER tab (both colour-mode toggles) from the base and from the working
   tree and compare. This only reads those tabs. Any difference means an edit
   leaked outside EarthRanger, ER Legacy and SERCA: report it to the user and
   undo the ER-family edit that caused it. Never edit another system's rules to
   make the check pass.

Run from the design repo root:
    uv run --no-project --with playwright --with pillow python \
        .claude/skills/er-design-change/scripts/check_scope.py [--base origin/main] [--out DIR]

Exits 0 when both checks pass, 1 when something is out of scope, 2 on a setup error.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ER_DIRS = ("earthranger/", "er-legacy/", "serca/")
ALLOWED_FILES = {"spec-sheet.html", "package.json"}
OTHER_SYSTEMS = ("strata", "asta", "olmo-earth", "skylight")
MODES = ("light", "dark")


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def changed_files(base: str) -> list[str]:
    tracked = git("diff", "--name-only", base).split()
    untracked = git("ls-files", "--others", "--exclude-standard").split()
    return sorted(set(tracked) | set(untracked))


def package_json_problems(base: str) -> list[str]:
    diff = git("diff", "-U0", base, "--", "package.json")
    lines = [l for l in diff.splitlines()
             if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    return [l for l in lines if '"version"' not in l]


def check_files(base: str) -> list[str]:
    problems = []
    for f in changed_files(base):
        if f.startswith(".claude/"):
            continue  # skill and tooling edits are reviewed separately
        if f.startswith(ER_DIRS) or f in ALLOWED_FILES:
            continue
        problems.append(f"{f}: outside EarthRanger, ER Legacy, SERCA and the spec sheet")
    if "package.json" in changed_files(base):
        for l in package_json_problems(base):
            problems.append(f"package.json: a line other than \"version\" changed: {l.strip()}")
    return problems


def shoot(page, html: Path, system: str, mode: str, dest: Path) -> None:
    page.goto(html.as_uri())
    page.wait_for_load_state("networkidle")
    # Only affects this screenshot: stops the tab switcher being caught mid-transition.
    page.add_style_tag(content="*, *::before, *::after { transition: none !important; animation: none !important; caret-color: transparent !important; }")
    # The mode toggle is hidden outside the ER family, so click through the DOM.
    page.evaluate("([s, m]) => { document.querySelector(`button[data-system=\"${s}\"]`).click();"
                  " document.querySelector(`button[data-er-mode=\"${m}\"]`).click(); }", [system, mode])
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    page.screenshot(path=str(dest), full_page=True, animations="disabled")


def check_pixels(base: str, out: Path) -> list[str]:
    from PIL import Image, ImageChops
    from playwright.sync_api import sync_playwright

    if "spec-sheet.html" not in changed_files(base):
        return []
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        wt = Path(tmp) / "base"
        git("worktree", "add", "--detach", str(wt), base)
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(viewport={"width": 1280, "height": 900})
                for system in OTHER_SYSTEMS:
                    for mode in MODES:
                        before = out / f"{system}-{mode}-before.png"
                        after = out / f"{system}-{mode}-after.png"
                        shoot(page, wt / "spec-sheet.html", system, mode, before)
                        shoot(page, Path.cwd() / "spec-sheet.html", system, mode, after)
                        a, b = Image.open(before).convert("RGB"), Image.open(after).convert("RGB")
                        if a.size != b.size:
                            problems.append(f"{system} ({mode} toggle): page height changed {a.size} -> {b.size}")
                            continue
                        box = ImageChops.difference(a, b).getbbox()
                        if box:
                            diff = out / f"{system}-{mode}-diff.png"
                            ImageChops.difference(a, b).save(diff)
                            problems.append(f"{system} ({mode} toggle): pixels differ in {box}; see {diff}")
                browser.close()
        finally:
            git("worktree", "remove", "--force", str(wt))
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--out", type=Path, help="where to keep screenshots; default a temp dir")
    args = ap.parse_args()
    if not Path("spec-sheet.html").exists():
        print("Run this from the design repo root.", file=sys.stderr)
        return 2
    out = args.out or Path(tempfile.mkdtemp(prefix="er-scope-"))
    out.mkdir(parents=True, exist_ok=True)

    problems = check_files(args.base)
    try:
        problems += check_pixels(args.base, out)
    except Exception as e:  # setup trouble, e.g. no browser installed
        print(f"Pixel check could not run: {e}", file=sys.stderr)
        print("Try: uv run --no-project --with playwright python -m playwright install chromium-headless-shell",
              file=sys.stderr)
        return 2

    files = changed_files(args.base)
    print(f"Changed files vs {args.base}: {', '.join(files) or 'none'}")
    if problems:
        print("OUT OF SCOPE:")
        for p in problems:
            print(f"  - {p}")
        return 1
    checked = ", ".join(OTHER_SYSTEMS)
    print(f"In scope. Other systems on the spec sheet ({checked}) render identically. Screenshots: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
