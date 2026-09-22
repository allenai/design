---
name: OlmoEarth
description: Ai2 design system — OlmoEarth product interface
version: 0.0.1

assets:
  # ── Assets that align with the design system ──────────────────────
  logo: assets/logo.svg
  wordmark: assets/wordmark.svg

colors:
  # ── Primitive palette ─────────────────────────────────────────────
  # Full-opacity base colors. Opacity variants are derived from these
  # in component and semantic contexts.
  extra-dark-teal: "#032629"
  dark-teal: "#0a3235"
  cream: "#faf2e9"
  teal: "#105257"
  teal-20: "#cbd2cc"
  teal-40: "#9cb2af"
  teal-60: "#6e9291"
  teal-80: "#3f7274"
  pink: "#f0529c"
  pink-20: "#f8d2da"
  pink-40: "#f6b2ca"
  pink-60: "#f492bb"
  pink-80: "#f272ab"
  green: "#0fcb8c"
  green-20: "#cbead6"
  green-40: "#9ce2c4"
  green-60: "#6ddbb1"
  green-80: "#3ed39f"
  gray: "#343434"
  gray-20: "#d6d6d6"
  gray-40: "#aeaeae"
  gray-60: "#858585"
  gray-80: "#5d5d5d"
  white: "#ffffff"
  info-blue: "#2a88ef"
  error-red: "#fd4645"
  error-red-dark: "#d02f2e"
  success-green: "#549c35"
  warning-orange: "#ffa31c"

  # ── Opacity primitives ────────────────────────────────────────────
  # True alpha-channel variants of extra-dark-teal and cream. Distinct
  # from the tint primitives above (teal-20, pink-40, etc.), which are
  # solid blends with cream. These use the alpha channel so the resulting
  # color adapts to whatever surface the element is placed on — page,
  # card, panel, or another translucent layer.
  extra-dark-teal-10: "#0326291a"
  extra-dark-teal-20: "#03262933"
  extra-dark-teal-30: "#0326294d"
  extra-dark-teal-40: "#03262966"
  extra-dark-teal-50: "#03262980"
  extra-dark-teal-60: "#03262999"
  extra-dark-teal-70: "#032629b3"
  extra-dark-teal-80: "#032629cc"
  extra-dark-teal-90: "#032629e6"
  cream-10: "#faf2e91a"
  cream-20: "#faf2e933"
  cream-30: "#faf2e94d"
  cream-40: "#faf2e966"
  cream-50: "#faf2e980"
  cream-60: "#faf2e999"
  cream-70: "#faf2e9b3"
  cream-80: "#faf2e9cc"
  cream-90: "#faf2e9e6"

  # ── Semantic aliases ──────────────────────────────────────────────
  # Maps intent to primitive.
  background: "{colors.cream}"
  background-reversed: "{colors.extra-dark-teal}"
  text: "{colors.dark-teal}"
  text-reversed: "{colors.cream}"
  text-disabled: "{colors.gray}"
  text-error: "{colors.error-red}"
  interactive-default: "{colors.teal}"
  interactive-default-hover: "{colors.teal-80}"
  interactive-primary: "{colors.dark-teal}"
  interactive-primary-hover: "#084245"
  interactive-secondary: "{colors.green}"
  interactive-secondary-hover: "{colors.green-60}"
  link: "{colors.teal}"
  link-reversed: "{colors.interactive-secondary}"

  # ── Subtle surfaces ───────────────────────────────────────────────
  # Translucent overlays that take their tone from the inverse of the
  # page surface. On a light page: extra-dark-teal alpha. On a dark
  # page: cream alpha.
  subtle: "{colors.extra-dark-teal-50}"
  extra-subtle: "{colors.extra-dark-teal-10}"
  on-subtle: "{colors.text-reversed}"
  # `extra-subtle` sits so close to the page surface that the inverse
  # foreground used by `subtle` loses contrast. Pair it with the
  # standard page text instead.
  on-extra-subtle: "{colors.text}"

  # A surface one step lighter than gray-20, for panel and preview backgrounds.
  # The inherited scale goes straight from white to gray-20, so Studio invented
  # this five times over before it was named.
  gray-10: "#f5f5f5"

  # Task and model state. Distinct from the semantic colors above: these read as
  # neutral progress rather than success or warning, and they predate the spec.
  status-neutral: "#9e9e9e"
  status-warning: "#ff9800"
  status-success: "#4caf50"

  # Map draw and layer styling. Provisional — these are MapLibre and
  # mapbox-gl-draw defaults that Studio adopted rather than colors anyone chose.
  map-draw: "#fbb03b"
  map-selection: "#3bb2d0"
  map-boundary: "#6d8196"

  # Charts. Also provisional, and currently two unrelated palettes: four fixed
  # series colors from Recharts, and twelve categorical colors from matplotlib's
  # tab10/tab20 assigned by hashing a label. Consolidating them needs a decision
  # about how many distinguishable hues Studio's charts actually need.
  chart-series-1: "#0088fe"
  chart-series-2: "#00c49f"
  chart-series-3: "#ffbb28"
  chart-series-4: "#ff8042"
  chart-categorical-1: "#1f77b4"
  chart-categorical-2: "#ff7f0e"
  chart-categorical-3: "#2ca02c"
  chart-categorical-4: "#d62728"
  chart-categorical-5: "#9467bd"
  chart-categorical-6: "#8c564b"
  chart-categorical-7: "#e377c2"
  chart-categorical-8: "#7f7f7f"
  chart-categorical-9: "#bcbd22"
  chart-categorical-10: "#17becf"
  chart-categorical-11: "#ff9896"
  chart-categorical-12: "#aec7e8"

typography:
  display:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
  heading-xl:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.2
  heading-lg:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 2rem
    fontWeight: 700
    lineHeight: 1.2
  heading-md:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.3
  heading-sm:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 1.25rem
    fontWeight: 600
    lineHeight: 1.4
  body-lg:
    fontFamily: Manrope, Arial, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: Manrope, Arial, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Manrope, Arial, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  body-xs:
    fontFamily: Manrope, Arial, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
  mono:
    fontFamily: Roboto Mono, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6

  # The small emphasised label above a value, or naming a section. Studio uses it
  # in 72 places. These are the values it renders today, which are MUI's defaults
  # — see the note below about the weight.
  subtitle-md:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.75
  subtitle-sm:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: 0.875rem
    fontWeight: 500
    lineHeight: 1.57

spacing:
  2xs: 8px
  xs: 12px
  sm: 14px
  md: 16px
  lg: 18px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 36px
  5xl: 40px
  6xl: 48px
  3xs: 4px
  4xs: 2px

rounded:
  3xs: 4px
  2xs: 8px
  xs: 12px
  sm: 14px
  md: 16px
  lg: 18px
  xl: 20px
  2xl: 24px
  3xl: 32px

components:
  # ── Buttons ───────────────────────────────────────────────────────
  # Filled variants
  button-default:
    backgroundColor: "{colors.interactive-default}"
    textColor: "{colors.cream}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-default-hover:
    backgroundColor: "{colors.interactive-default-hover}"
    textColor: "{colors.cream}"
  button-reversed:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.extra-dark-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-reversed-hover:
    backgroundColor: "{colors.white}"
    textColor: "{colors.extra-dark-teal}"
  button-primary:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.cream}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-primary-hover:
    backgroundColor: "{colors.interactive-primary-hover}"
    textColor: "{colors.cream}"
  button-secondary:
    backgroundColor: "{colors.interactive-secondary}"
    textColor: "{colors.extra-dark-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-secondary-hover:
    backgroundColor: "{colors.interactive-secondary-hover}"
    textColor: "{colors.extra-dark-teal}"

  # Outlined variants
  button-default-outlined:
    backgroundColor: transparent
    textColor: "{colors.interactive-default}"
    borderColor: "{colors.interactive-default}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-default-outlined-hover:
    backgroundColor: "{colors.teal-20}"
    textColor: "{colors.interactive-default}"
    borderColor: "{colors.interactive-default}"
  button-reversed-outlined:
    backgroundColor: transparent
    textColor: "{colors.cream}"
    borderColor: "{colors.cream}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-reversed-outlined-hover:
    backgroundColor: "{colors.white}"
    textColor: "{colors.extra-dark-teal}"
    borderColor: "{colors.white}"
  button-primary-outlined:
    backgroundColor: transparent
    textColor: "{colors.interactive-primary}"
    borderColor: "{colors.interactive-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-primary-outlined-hover:
    backgroundColor: "{colors.pink-20}"
    textColor: "{colors.extra-dark-teal}"
    borderColor: "{colors.interactive-primary}"
  button-secondary-outlined:
    backgroundColor: transparent
    textColor: "{colors.interactive-secondary}"
    borderColor: "{colors.interactive-secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-secondary-outlined-hover:
    backgroundColor: "{colors.green-20}"
    textColor: "{colors.extra-dark-teal}"
    borderColor: "{colors.interactive-secondary}"

  # Disabled state
  button-disabled:
    backgroundColor: "{colors.gray-80}"
    textColor: "{colors.cream}"
    rounded: "{rounded.3xs}"

  # Sizes
  button-size-sm:
    height: 32px
    padding: "{spacing.2xs}"
    typography: "{typography.body-sm}"
  button-size-md:
    height: 36px
    padding: "{spacing.xs}"
    typography: "{typography.body-sm}"
  button-size-lg:
    height: 48px
    padding: "{spacing.md}"
    typography: "{typography.body-sm}"

  # ── Inputs ────────────────────────────────────────────────────────
  input-default:
    backgroundColor: "rgba(0, 0, 0, 0)"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: 4px
    padding: 14px
    borderColor: "rgba(0, 0, 0, 0.23)"
  input-error:
    backgroundColor: "{colors.white}"
    textColor: "{colors.error-red-dark}"
    rounded: "{rounded.3xs}"
  input-disabled:
    backgroundColor: "rgba(0, 0, 0, 0)"
    textColor: "rgba(0, 0, 0, 0.38)"
    rounded: 4px
    borderColor: "rgba(0, 0, 0, 0.26)"
  input-size-sm:
    height: 40px
    padding: 8.5px
    typography: "{typography.body-sm}"
  input-size-md:
    height: 56px
    padding: 16.5px
    typography: "{typography.body-md}"
  input-size-lg:
    height: 48px
    padding: "{spacing.md}"
    typography: "{typography.body-md}"

  # ── Form controls ─────────────────────────────────────────────────
  # Checkbox
  checkbox-default:
    backgroundColor: "{colors.white}"
    borderColor: "{colors.teal}"
    width: 24px
    height: 24px
    rounded: 2px
  checkbox-checked:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.cream}"

  # Radio
  radio-default:
    backgroundColor: "{colors.white}"
    borderColor: "{colors.teal}"
    width: 24px
    height: 24px
  radio-checked:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.cream}"

  # Switch
  switch-default:
    backgroundColor: "#000000"
    borderColor: "{colors.teal-80}"
    width: 58px
    height: 38px
  switch-checked:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.cream}"

  # Slider
  slider-track:
    backgroundColor: "{colors.teal-20}"
    height: 8px
  slider-track-filled:
    backgroundColor: "{colors.interactive-default}"

  # ── Chips ─────────────────────────────────────────────────────────
  chip-default:
    backgroundColor: "rgba(0, 0, 0, 0.08)"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: 16px
    padding: "{spacing.xs}"
    height: 32px
  chip-primary:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.cream}"
    rounded: "{rounded.3xs}"
  chip-secondary:
    backgroundColor: "{colors.interactive-secondary}"
    textColor: "{colors.extra-dark-teal}"
    rounded: "{rounded.3xs}"
  chip-subtle:
    backgroundColor: "{colors.subtle}"
    textColor: "{colors.on-subtle}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  chip-extra-subtle:
    backgroundColor: "{colors.extra-subtle}"
    textColor: "{colors.on-extra-subtle}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"

  # Sizes
  chip-size-sm:
    height: 24px
    padding: "{spacing.2xs}"
    typography: "{typography.body-sm}"
  chip-size-md:
    height: 32px
    padding: "{spacing.xs}"
    typography: "{typography.body-sm}"
  chip-size-lg:
    height: 48px
    padding: "{spacing.md}"
    typography: "{typography.body-md}"

  # ── Avatars ───────────────────────────────────────────────────────
  avatar-default:
    backgroundColor: "{colors.extra-dark-teal}"
    textColor: "{colors.cream}"
    rounded: "{rounded.3xs}"
  avatar-primary:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.extra-dark-teal}"
    rounded: "{rounded.3xs}"
  avatar-secondary:
    backgroundColor: "{colors.interactive-secondary}"
    textColor: "{colors.extra-dark-teal}"
    rounded: "{rounded.3xs}"
  avatar-subtle:
    backgroundColor: "{colors.subtle}"
    textColor: "{colors.on-subtle}"
    rounded: "{rounded.3xs}"
  avatar-extra-subtle:
    backgroundColor: "{colors.extra-subtle}"
    textColor: "{colors.on-extra-subtle}"
    rounded: "{rounded.3xs}"

  # Sizes
  avatar-size-xs:
    width: 24px
    height: 24px
    typography: "{typography.body-xs}"
  avatar-size-sm:
    width: 32px
    height: 32px
    typography: "{typography.body-sm}"
  avatar-size-md:
    width: 36px
    height: 36px
    typography: "{typography.body-md}"
  chip-outlined:
    backgroundColor: "rgba(0, 0, 0, 0)"
    textColor: "{colors.text}"
    borderColor: "#bdbdbd"
    rounded: 16px
    height: 32px

  # The confusion matrix's diagonal, as green at even opacities over white. Stated
  # as rgba so the steps land on exactly 10% through 50%.
  confusion-diagonal-1:
    backgroundColor: "rgba(15, 203, 140, 0.1)"
  confusion-diagonal-2:
    backgroundColor: "rgba(15, 203, 140, 0.2)"
  confusion-diagonal-3:
    backgroundColor: "rgba(15, 203, 140, 0.3)"
  confusion-diagonal-4:
    backgroundColor: "rgba(15, 203, 140, 0.4)"
  confusion-diagonal-5:
    backgroundColor: "rgba(15, 203, 140, 0.5)"
---

## Overview

_To be populated with product-specific design rationale._

## Colors

Studio's primary action is **dark teal**, not the pink Strata specifies. Pink remains
in the palette as an accent; `interactive-primary` points at dark teal, so buttons,
chips and avatars all follow without being overridden one at a time. The primary
hover goes *darker* (`#084245`) where Strata's goes lighter.

`gray-10` fills a gap rather than adding a shade: the inherited neutral scale steps
from white straight to `gray-20`, and a panel background needs something in between.

Three groups here are **provisional**, recorded so they stop being invisible:

- **Status colors** for task and model state. They overlap the semantic colors
  without matching them, and whether they collapse into `success-green` and
  friends is undecided.
- **Map colors** are MapLibre and mapbox-gl-draw defaults Studio adopted rather
  than chose. Whether map styling belongs in a design system at all is open.
- **Chart colors** are currently two unrelated palettes — four fixed series colors
  from Recharts, twelve categorical ones from matplotlib assigned by hashing a
  label. The Analytics page draws a pie chart from one and a bar chart from the
  other, on the same screen.

## Typography

Every heading renders in **Manrope**. PP Telegraf is named upstream as the heading
face but has never been loaded here, and adopting it would need a license.

**The subtitle weight is an open question.** `subtitle-md` and `subtitle-sm` record
what Studio renders, which is MUI's default — but of the 72 call sites, **24
override the weight**: 17 to `600`, 5 to `bold`, 2 to `700`. A third of the callers
disagreeing with the value, and agreeing with each other, is the codebase asking
for `600` — which is also the weight `heading-md` and `heading-sm` already use.

Changing it here would make all 72 consistent and let Studio delete those 24 local
overrides. Left as it renders for now so the change is a decision rather than a
side effect of writing the role down.

## Layout

An 8px base unit underlies layout. The spacing scale is a linear progression from
8px to 48px, and layout decisions should snap to it.

- Use `2xs` (8px) and `xs` (12px) for tight intra-component spacing (icon-to-label
  gaps, list item padding) and component internal padding.
- Use `md` (16px) through `xl` (20px) for inter-component gaps and section gutters.
- Use `2xl` (24px) and above for section-level separation.

Studio extends the scale downward with `3xs` (4px) and `4xs` (2px). Much of the
product is chrome floating over a map — legends, layer panels, annotation cards —
where padding is taken directly from the thing the user opened the page to see. The
8px floor is the right floor for a page and too coarse for a row that repeats
fifteen times inside a 360px panel.

These are a **dense tier, not a smaller default**, and two rules keep them from
leaking into general layout:

- Reach for them only inside a component's repeating content — legend rows,
  label/value pairs, the gap between a swatch and its text. Card padding, panel
  gutters and the space between components stay on `2xs` and up.
- When a row goes tighter than `2xs`, set its `line-height` explicitly. Below 8px
  the padding is no longer what separates one row from the next — the text box is.
  A dense row that inherits a 1.5 line-height hasn't actually been made denser, and
  one that inherits 1.0 collides with its neighbour.

Density is bought with type and rules as much as with space. Stepping the size down
(16px → 14px → 12px) and letting a 1px divider do the work that 16px of padding was
doing buys more than tightening padding alone, and stays legible where padding
alone stops being. A tighter row that still reads at a glance is the goal; one that
saves 4px and costs a second look is not.

## Elevation & Depth

Heavy shadows are not used. Depth is expressed through tonal layering — surfaces stack by shifting between `background` opacity levels. The `extra-dark-teal` opacity scale (4%, 10%, 20%) creates subtle container definitions without hard borders.

- `opacity-4` (4%): Subtle differentiation, barely perceptible — used for overlay headers and footers.
- `opacity-10` (10%): Light container backgrounds, hover states on text buttons.
- `opacity-20` (20%): Stroke/border level — input field borders, dividers.

## Shapes

Border radii follow the same numeric scale as spacing (`3xs` through `3xl`). The scale is intentionally wide to support the full range from sharp (`3xs: 4px`) to pill-shaped (`3xl: 32px`).

- **Buttons, inputs, chips, and avatars:** All use `rounded.3xs` (4px) — sharp and structured throughout the system.
- **Pill shapes:** Use `rounded.3xl` (32px) or a full-radius value for badge or tag variants that require a pill silhouette.
- **Avoid mixing radii** within a single component group — pick one scale level and apply it consistently.

## Components

The default chip takes the 10% tonal layer rather than a teal fill: Studio's chips
are mostly metadata tags, and a teal fill reads as an emphasis they don't carry.
Contrast against the dark-teal text stays above 10:1 on both cream and white.

Chip, input and switch dimensions are stated as MUI renders them. That is a
description, not a decision — those numbers came from the framework, and if the
system wants its own density scale these are the values it would be replacing.

Two things the format can't express, so they live here as prose: the checkbox's 2px
corner radius and its border color, which MUI draws as an SVG path rather than a
styled box.

## Do's and Don'ts

- **Do** reach for the tonal layers (`extra-subtle`, `subtle`) for chips, hovers
  and empty states, rather than a filled brand color.
- **Do** put text on white inside a form. Inputs sit on white against the cream
  page, which is what makes a field read as somewhere to type.
- **Don't** use `interactive-primary` for more than the single most important
  action on a screen. It's dark teal here, which is quiet enough to overuse.
- **Don't** use the chart or map colors for interface chrome — they're chosen for
  distinguishability against imagery, not for hierarchy.
