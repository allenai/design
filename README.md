# Ai2 Design System

This repository contains the DESIGN.md files for Ai2's design systems. These files define design tokens and rationale for use by coding agents and developer tooling.

## What is DESIGN.md?

DESIGN.md is an open format specification created by Google for describing visual design systems to coding agents. Each file combines:

- **YAML frontmatter** — machine-readable design tokens (colors, typography, spacing, etc.)
- **Markdown prose** — human-readable rationale explaining *why* values exist and *how* to apply them

This repository follows the [DESIGN.md format specification](https://github.com/google-labs-code/design.md) published by Google. We use their open-source CLI tools for validation and export. A local copy of the spec is kept in [`docs/spec.md`](docs/spec.md) for reference.

---

## How to use these files with agents

Each product has a fully resolved `DESIGN.md` file — no inheritance to follow, no build step required. Each file is self-contained and reads as a standalone document; it doesn't reference other systems or internal build details. Copy it into your project and agents will pick it up automatically, or paste the contents directly into your system prompt:

```
asta/DESIGN.md
olmo-earth/DESIGN.md
```

If your project also needs logos or wordmarks, grab the product's `assets/` folder alongside the `DESIGN.md`. Asset paths are declared in the file's `assets:` frontmatter key so agents know what's available:

```yaml
assets:
  logo: assets/logo.svg
  wordmark: assets/wordmark.svg
```

Alternatively, export the tokens to other formats for use in your build pipeline:

```bash
npx @google/design.md export --format <fmt> asta/DESIGN.md
```

| Format | Output | Use case |
|:-------|:-------|:---------|
| `json-tailwind` | JSON | Tailwind v3 `theme.extend` config |
| `css-tailwind` | CSS | Tailwind v4 `@theme { ... }` block |
| `dtcg` | JSON | W3C Design Tokens — interoperable with Figma, Style Dictionary |

---

## Structure

```
strata/             ← Base design system — source of truth
  DESIGN.md
  assets/           ← logos and wordmarks

asta/               ← Asta product system
  DESIGN.src.md     ← product overrides and additions (edit this)
  DESIGN.md         ← generated output (use this with agents)
  assets/           ← product-specific logos and wordmarks

olmo-earth/         ← OlmoEarth product system
  DESIGN.src.md     ← product overrides and additions (edit this)
  DESIGN.md         ← generated output (use this with agents)

scripts/
  compose.ts        ← merges base + overlay → DESIGN.md
```

### Strata (Base)

Strata is the Ai2 foundation layer. It defines the primitive and semantic tokens shared across all products: the full color palette, type scale, spacing system, border radii, and universally-shared components.

### Product Systems (Asta, OlmoEarth)

Each product system defines only what differs from Strata — brand accent overrides, product-specific components, and product-specific rationale. A build step merges the base and overlay into a single `DESIGN.md` that agents and developers consume.


## Editing a product design system

Edit `[product]/DESIGN.src.md` (the overlay), then rebuild:

```bash
npm run build
```

Only define what differs from Strata in the overlay — colors, tokens, or components that are specific to that product. Everything else is inherited automatically from `strata/DESIGN.md`.

## Commands

```bash
npm install       # once
npm run build     # recompose the overlay specs, rebuild asta/ and olmo-earth/tokens.json
npm run lint      # validate every product's spec
```

Rebuild or check a single product while iterating:

```bash
npm run compose:asta          # or compose:olmo-earth
npm run tokens:asta           # or tokens:olmo-earth
npx @google/design.md lint asta/DESIGN.md
```

Also from the [DESIGN.md CLI](https://github.com/google-labs-code/design.md):

```bash
# What changed between two versions of a spec
npx @google/design.md diff strata/DESIGN.md strata/DESIGN-v2.md

# Print the DESIGN.md format spec, e.g. to give an agent context for reading these files
npx @google/design.md spec
```

## Cutting a release

1. Edit `version` in [`package.json`](package.json): last number for a fix, middle
   for additions, first for anything renamed or removed.
2. Commit that to `main`.
3. **Actions → Release → Run workflow → `main`.**

If the version already has a tag, the run fails and says so — that means step 1
hasn't happened yet.

The workflow rebuilds the generated files and commits them, lints every spec,
tags the commit, and creates a GitHub release. Products pick it up from that tag.
Re-running is harmless: it skips a version that already exists.

## Using these specs in a product

```bash
npm install "github:allenai/design#semver:^0.1.0"
```

The `#semver:` range resolves against this repo's release tags, and your lockfile
records the exact commit, so builds are reproducible. Pin harder if you'd rather:
`#v0.1.0` for one release, or a commit SHA for absolute certainty.

### What you can import

```js
// The tokens, as plain JSON with every reference already resolved to a literal
import tokens from "@allenai/design-system/olmo-earth/tokens.json";
tokens.colors["dark-teal"];             // "#0a3235"
tokens.components["button-default"];    // { backgroundColor, textColor, typography, … }

// The spec itself — for docs, or to hand to an agent
const specPath = require.resolve("@allenai/design-system/olmo-earth");

// Brand assets
import logo from "@allenai/design-system/olmo-earth/assets/logo.svg";
```

TypeScript needs no extra types here: with `resolveJsonModule`, it infers exact keys and per-component shapes from the JSON, so `tokens.colors["dark-teel"]` is a compile error.

The other products' specs and assets are exported the same way — `strata`, `asta`, `earthranger`, `serca`, and `<product>/voice` where a `VOICE.md` exists. Asta and OlmoEarth have a generated `tokens.json` (`asta/tokens.json` feeds the Asta theme builder in the varnish repo); the others can have one when something needs it.

## Why it's built this way

Skip unless something here surprises you.

**`tokens.json` is [W3C Design Tokens](https://www.designtokens.org) (DTCG).** That
means Figma's token plugins, [Style Dictionary](https://styledictionary.com) and
[Terrazzo](https://terrazzo.app) can all read it, so a product can generate whatever
its stack needs instead of parsing a shape invented here.

**We generate it rather than using `@google/design.md export --format dtcg`,
which is what we'd prefer.** That exporter is currently lossy: it omits the entire
`components` section, drops `lineHeight` from every typography role, and emits
alpha colours without an `alpha` channel — so its output fails the schema it
declares ([design.md#172](https://github.com/google-labs-code/design.md/issues/172)).
`scripts/emit-tokens.ts` matches its structure deliberately, so switching is a
[three-step migration](#migrating-to-the-clis-exporter) whenever that's fixed.

**Two places the spec and DTCG don't line up**, handled rather than papered over:

- `letterSpacing` is required by DTCG's composite `typography` type and the
  DESIGN.md format has no such key, so it's emitted as `0` — what these roles
  render as today.
- A role that can't be a composite becomes a group of primitive tokens instead.
  EarthRanger writes `fontStyle: Regular` rather than a weight, and an absolute
  `lineHeight: 28.8px` where DTCG wants a multiplier. Emitting those as separate
  tokens stays valid and loses nothing, where converting 28.8px into a multiplier
  would mean inventing a number the spec never states.

**Node, not bun.** Both scripts are plain TypeScript that Node runs directly, and
the CLI is invoked with `npx`, so a second runtime and a second lockfile bought
nothing.

**Not on npm yet.** Publishing needs `@allenai` npm org membership. The release
workflow publishes as soon as an `NPM_AUTH_TOKEN` secret exists and does nothing
about it until then — installing from git works either way, and npm would add a
registry page and provenance rather than versioning.

## Migrating to the CLI's exporter

`scripts/emit-tokens.ts` exists only because `@google/design.md export --format
dtcg` is missing things we need. When that's fixed, this repo should stop
generating tokens itself.

**1. Check whether it has caught up.**

```bash
npm run tokens:upstream     # regenerate asta/ and olmo-earth/tokens.json using the CLI
git diff                    # compare against what our script produced
```

What to look for in the diff: a `components` section, a `lineHeight` on every
typography role, and an `alpha` channel on the translucent colours. If those are
present and the values match, it has caught up. [design.md#172](https://github.com/google-labs-code/design.md/issues/172)
tracks it.

**2. Point `tokens` at the CLI.** In `package.json`:

```json
"tokens": "npm run tokens:upstream"
```

**3. Delete `scripts/emit-tokens.ts`** and the `tokens:asta` / `tokens:olmo-earth` scripts.

Consumers see nothing: the file keeps its name, its path and its shape, so no
product needs a change. If the diff in step 1 isn't empty, it's worth reading
before switching — a difference there is a difference every consumer will get.
