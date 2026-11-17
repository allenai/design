# Source of references/act/

Vendored from Microsoft's Accessibility Considerations Toolkit:

- Repo: https://github.com/microsoft/Microsoft-Accessibility
- Path: `Accessibility-Considerations-Toolkit/`
- Pinned commit: `6d4e52d588eaf2bc79297b3898aa4641d61e574d` (2026-11-11, "Import Accessibility Considerations Toolkit into the monorepo (#9)")
- Copied on 2026-11-16: `considerations/`, `heuristics/`, `methodology/`, `standards/`,
  `provenance.json`, `LICENSE.txt`. Omitted: `schemas/` (generated YAML), `tests/`, `scripts/`, and
  tooling config.

The toolkit has no release tags yet, so this pins a commit.

## Keeping it current

`.github/workflows/a11y-toolkit-sync.yml` checks upstream every Monday. When the toolkit has moved,
it runs `scripts/update_toolkit.sh` and opens a PR with the new content, an upstream compare link,
and a warning if `SKILL.md` names files that no longer exist. It never merges on its own. These
files are loaded into model context, so read the diff before merging. Run the workflow by hand
(optionally with a specific commit) from the Actions tab.

To update locally instead: `bash .claude/skills/a11y/scripts/update_toolkit.sh [SHA]`.
