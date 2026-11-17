# Source of references/act/

Vendored from Microsoft's Accessibility Considerations Toolkit:

- Repo: https://github.com/microsoft/Microsoft-Accessibility
- Path: `Accessibility-Considerations-Toolkit/`
- Pinned commit: `6d4e52d588eaf2bc79297b3898aa4641d61e574d` (2026-11-11, "Import Accessibility
  Considerations Toolkit into the monorepo (#9)")
- Copied on 2026-11-16: `considerations/`, `heuristics/`, `methodology/`, `standards/`,
  `provenance.json`, `LICENSE.txt`. Omitted: `schemas/` (generated YAML), `tests/`, `scripts/`, and
  tooling config.

The toolkit has no release tags yet. To update, review the diff between this commit and the new one
before replacing files. These files are loaded into model context, so read what changed.

```sh
S=$(mktemp -d) && cd "$S" && git init -q && \
git remote add origin https://github.com/microsoft/Microsoft-Accessibility.git && \
git sparse-checkout set --no-cone /Accessibility-Considerations-Toolkit/considerations \
  /Accessibility-Considerations-Toolkit/heuristics /Accessibility-Considerations-Toolkit/methodology \
  /Accessibility-Considerations-Toolkit/standards /Accessibility-Considerations-Toolkit/provenance.json \
  /Accessibility-Considerations-Toolkit/LICENSE.txt && \
git fetch -q --depth 1 origin <NEW_SHA> && git checkout -q FETCH_HEAD
```
