# This repo

Houses Ai2's design systems as `DESIGN.md` files — a self-contained, plain-text
format (YAML token frontmatter + markdown rationale) documented in `docs/spec.md`.
`spec-sheet.html` is a living, static demo driven by these files (colors, type,
components, per-system overrides) — it is manually kept in sync with them, not
auto-generated.

## Before doing any design/token/UI work, read the relevant DESIGN.md first

| Working on | Read |
| --- | --- |
| Strata (the shared foundation) | `strata/DESIGN.md` |
| Asta | `asta/DESIGN.md` |
| OlmoEarth | `olmo-earth/DESIGN.md` (currently a stub — identical to Strata until `olmo-earth/DESIGN.src.md` is populated) |
| EarthRanger | `earthranger/DESIGN.md` |
| SERCA (Alliance identity — EarthRanger tokens + SERCA marks) | `serca/DESIGN.md` |

Treat that file's tokens as normative. If a change affects `spec-sheet.html`,
update both and keep them consistent — do not treat one as authoritative and
let the other drift.

## Scope discipline

Changes requested for one product system should not bleed into the others
unless explicitly asked. `spec-sheet.html` renders all four systems from one
file — check that a fix or token change is actually scoped to the system it's
meant for before touching shared CSS/JS.

## Useful context

- `strata/DESIGN.md` is the base every other product overlays or diverges from.
- `scripts/compose.ts` merges a product's `DESIGN.src.md` overlay onto Strata's
  base to produce that product's `DESIGN.md` (see `package.json`'s `compose:*`
  scripts) — this exists for Asta/OlmoEarth. EarthRanger's `DESIGN.md` is
  maintained directly, not composed.
- `serca/DESIGN.md` is also maintained directly. Its `colors:` and `typography:`
  frontmatter must stay byte-identical to `earthranger/DESIGN.md` — SERCA only
  changes the assets, Overview, and mark rules.
- `npm run lint` runs `@google/design.md lint` against strata/asta/olmo-earth.
