#!/usr/bin/env bash
# Refresh references/act/ from Microsoft's Accessibility Considerations Toolkit.
#
#   update_toolkit.sh [SHA]
#
# With no SHA, uses the newest upstream commit that touched the toolkit. Rewrites
# references/act/ and the pin in references/SOURCE.md, then checks that every
# file SKILL.md names still exists. Run it from anywhere; it works on the skill
# directory it lives in. The a11y-toolkit-sync workflow runs it weekly and opens
# a PR; you can also run it by hand.
#
# Exit codes: 0 updated, 3 already at that commit, 1 error.
# Writes a summary to $SUMMARY_FILE when set (the workflow uses it as the PR body).
set -euo pipefail

REPO=microsoft/Microsoft-Accessibility
TK=Accessibility-Considerations-Toolkit
# What we vendor. Anything else upstream (generated YAML, tests, tooling) stays out.
PARTS=(considerations heuristics methodology standards provenance.json LICENSE.txt)

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ACT="$SKILL_DIR/references/act"
SOURCE="$SKILL_DIR/references/SOURCE.md"

current=$(sed -n 's/^- Pinned commit: `\([0-9a-f]\{40\}\)`.*/\1/p' "$SOURCE")
[ -n "$current" ] || { echo "Can't find the pinned commit in $SOURCE" >&2; exit 1; }

target=${1:-}
if [ -z "$target" ]; then
  target=$(curl -fsSL ${GH_TOKEN:+-H "Authorization: Bearer $GH_TOKEN"} \
    "https://api.github.com/repos/$REPO/commits?path=$TK&per_page=1" |
    python3 -c 'import json,sys; print(json.load(sys.stdin)[0]["sha"])')
fi
if [ "$target" = "$current" ]; then
  echo "Already at $current."
  exit 3
fi

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
git -C "$work" init -q
git -C "$work" remote add origin "https://github.com/$REPO.git"
git -C "$work" sparse-checkout set --no-cone $(printf "/$TK/%s " "${PARTS[@]}")
git -C "$work" fetch -q --depth 1 origin "$target"
git -C "$work" checkout -q FETCH_HEAD
target=$(git -C "$work" rev-parse HEAD)
date=$(git -C "$work" log -1 --format=%cs)
subject=$(git -C "$work" log -1 --format=%s | tr -d '`"')

# Upstream says paths and aliases may be renamed. Stop rather than vendor half a toolkit.
for p in "${PARTS[@]}"; do
  [ -e "$work/$TK/$p" ] || { echo "Upstream $target has no $TK/$p; the layout changed. Update PARTS and SKILL.md by hand." >&2; exit 1; }
done

rm -rf "$ACT"
mkdir -p "$ACT"
for p in "${PARTS[@]}"; do cp -R "$work/$TK/$p" "$ACT/"; done
find "$ACT" -name .DS_Store -delete

python3 - "$SOURCE" "$target" "$date" "$subject" <<'PY'
import re, sys, datetime
path, sha, date, subject = sys.argv[1:]
text = open(path).read()
pin = f'- Pinned commit: `{sha}` ({date}, "{subject}")\n'
text = re.sub(r'- Pinned commit: `[0-9a-f]{40}`.*?\n(?=- )', pin, text, count=1, flags=re.S)
text = re.sub(r'- Copied on \d{4}-\d{2}-\d{2}:', f'- Copied on {datetime.date.today()}:', text, count=1)
open(path, 'w').write(text)
PY

# SKILL.md names consideration and methodology files; a rename upstream breaks it silently.
missing=()
while read -r ref; do
  [ -e "$SKILL_DIR/$ref" ] || [ -e "$ACT/considerations/$ref" ] || [ -e "$ACT/$ref" ] || missing+=("$ref")
done < <(grep -oE '(references/act/[A-Za-z0-9/._-]+\.md|4\.2\.[0-9]+-[a-z-]+\.md|(methodology|heuristics|standards)/[A-Za-z0-9._-]+\.md)' "$SKILL_DIR/SKILL.md" | sort -u | grep -v '<N>')

git -C "$SKILL_DIR" add -N -- "$ACT" 2>/dev/null || true

# Things a reviewer should look at by eye: these files are loaded into model context.
flags=$(git -C "$SKILL_DIR" diff -U0 -- "$ACT" 2>/dev/null |
  grep -E '^\+' | grep -iE 'ignore (all|previous|the above)|system prompt|api[_ -]?key|password|secret|curl |wget |https?://' |
  grep -vE '^\+\+\+' | head -20 || true)

{
  echo "Updates the vendored Accessibility Considerations Toolkit used by \`/a11y\`."
  echo
  echo "- From: \`${current:0:7}\`  To: \`${target:0:7}\` ($date, \"$subject\")"
  echo "- Upstream diff: https://github.com/$REPO/compare/$current...$target"
  echo
  echo "### Changed files"
  echo '```'
  git -C "$SKILL_DIR" diff --stat -- "$ACT" 2>/dev/null | tail -40 || true
  echo '```'
  if [ ${#missing[@]} -gt 0 ]; then
    echo
    echo "### ⚠️ SKILL.md names files that no longer exist"
    printf -- '- `%s`\n' "${missing[@]}"
    echo
    echo "Update the topic table and file list in \`SKILL.md\` before merging."
  fi
  echo
  echo "### Review before merging"
  echo "These files are loaded into Claude's context when \`/a11y\` runs, so read the diff, not just the stat."
  if [ -n "$flags" ]; then
    echo "Added lines worth a closer look (URLs, credentials, instruction-like text):"
    echo '```'
    echo "$flags"
    echo '```'
  fi
} > "${SUMMARY_FILE:-/dev/stdout}"

echo "Updated references/act/ to $target." >&2
[ ${#missing[@]} -eq 0 ] || echo "Warning: SKILL.md references missing files: ${missing[*]}" >&2
exit 0
