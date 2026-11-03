---
name: Strata
description: Ai2 base design system — shared foundation for all Ai2 product interfaces
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
  interactive-primary: "{colors.pink}"
  interactive-primary-hover: "{colors.pink-60}"
  interactive-secondary: "{colors.green}"
  interactive-secondary-hover: "{colors.green-60}"
  link: "{colors.interactive-primary}"
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

typography:
  display:
    fontFamily: PP Telegraf, Manrope, Arial, sans-serif
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
  heading-xl:
    fontFamily: PP Telegraf, Manrope, Arial, sans-serif
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.2
  heading-lg:
    fontFamily: PP Telegraf, Manrope, Arial, sans-serif
    fontSize: 2rem
    fontWeight: 700
    lineHeight: 1.2
  heading-md:
    fontFamily: PP Telegraf, Manrope, Arial, sans-serif
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.3
  heading-sm:
    fontFamily: PP Telegraf, Manrope, Arial, sans-serif
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
    textColor: "{colors.extra-dark-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-primary-hover:
    backgroundColor: "{colors.interactive-primary-hover}"
    textColor: "{colors.extra-dark-teal}"
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
    backgroundColor: "{colors.white}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  input-error:
    backgroundColor: "{colors.white}"
    textColor: "{colors.error-red-dark}"
    rounded: "{rounded.3xs}"
  input-disabled:
    backgroundColor: "{colors.gray-20}"
    textColor: "{colors.text}"
    rounded: "{rounded.3xs}"
  input-size-sm:
    height: 32px
    padding: "{spacing.2xs}"
    typography: "{typography.body-sm}"
  input-size-md:
    height: 36px
    padding: "{spacing.xs}"
    typography: "{typography.body-md}"
  input-size-lg:
    height: 48px
    padding: "{spacing.md}"
    typography: "{typography.body-md}"

  # ── Dropdowns ─────────────────────────────────────────────────────
  # The closed trigger is an input: it reuses input-default, input-error,
  # input-disabled and the input-size-* scale, plus a caret.
  dropdown-panel:
    backgroundColor: "{colors.white}"
    textColor: "{colors.text}"
    rounded: "{rounded.3xs}"
    padding: 4px
  dropdown-item:
    backgroundColor: "{colors.white}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.2xs}"
  dropdown-item-highlighted:
    backgroundColor: "{colors.teal-20}"
  dropdown-item-check:
    textColor: "{colors.interactive-default}"
  dropdown-group-label:
    textColor: "{colors.extra-dark-teal-70}"
    typography: "{typography.body-xs}"
    padding: "{spacing.xs}"
  dropdown-search:
    backgroundColor: "{colors.white}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs}"

  # ── Info tips ─────────────────────────────────────────────────────
  info-tip-trigger:
    textColor: "{colors.extra-dark-teal-70}"
    typography: "{typography.body-xs}"
    rounded: "{rounded.3xl}"
    size: 18px
  info-tip-trigger-hover:
    textColor: "{colors.interactive-default}"
  info-tip-panel:
    backgroundColor: "{colors.white}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
    width: 320px

  # ── Form controls ─────────────────────────────────────────────────
  # Checkbox
  checkbox-default:
    backgroundColor: "{colors.white}"
    borderColor: "{colors.teal-80}"
    width: 18px
    height: 18px
    rounded: 2px
  checkbox-checked:
    backgroundColor: "{colors.interactive-default}"
    textColor: "{colors.cream}"

  # Radio
  radio-default:
    backgroundColor: "{colors.white}"
    borderColor: "{colors.teal-80}"
    width: 18px
    height: 18px
  radio-checked:
    backgroundColor: "{colors.interactive-default}"
    textColor: "{colors.cream}"

  # Switch
  switch-default:
    backgroundColor: "{colors.white}"
    borderColor: "{colors.teal-80}"
    width: 34px
    height: 18px
  switch-checked:
    backgroundColor: "{colors.interactive-default}"
    textColor: "{colors.cream}"

  # Slider
  slider-track:
    backgroundColor: "{colors.teal-20}"
    height: 8px
  slider-track-filled:
    backgroundColor: "{colors.interactive-default}"

  # ── Chips ─────────────────────────────────────────────────────────
  chip-default:
    backgroundColor: "{colors.interactive-default}"
    textColor: "{colors.cream}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  chip-primary:
    backgroundColor: "{colors.interactive-primary}"
    textColor: "{colors.extra-dark-teal}"
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
    height: 32px
    padding: "{spacing.2xs}"
    typography: "{typography.body-sm}"
  chip-size-md:
    height: 36px
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
---

## Overview

This is the Ai2 foundation design system — the shared visual language (color, typography, spacing, shape, and core components) for Ai2 product interfaces.

The palette is anchored in deep teal and warm cream, with pink as the primary brand accent. The result is an interface aesthetic that feels credible, focused, and human — appropriate for tools used by experts and general audiences alike.

## Colors

The palette is organized in two layers: primitives and semantic aliases.

**Primitive colors** are the raw values — named by their visual character, not their role. They should rarely be used directly in product UI; prefer semantic aliases instead.

**Semantic aliases** map intent to primitive. They answer "what color should I use for a primary action?" rather than requiring the designer or agent to know that the answer is `pink`.

- **Background / background-reversed:** The default page surface is `cream` — warm, off-white, easy on the eye. The reversed (dark mode) surface is `extra-dark-teal`, a near-black that anchors the deep end of the palette.
- **Text / text-reversed:** Default body text is `dark-teal` for high contrast on cream. On dark backgrounds, text flips to `cream`.
- **Interactive-default (`teal`):** Default interactive state for non-CTA elements — checkboxes, sliders, toggles, focused inputs. Distinct from primary pink to avoid visual competition.
- **Interactive-primary (`pink`):** The main brand accent and CTA color. Used for primary buttons, links, and key interactive highlights. Use with restraint — its intensity should signal importance.
- **Interactive-secondary (`green`):** Supporting interactive color. Used for secondary actions, success states in interactive contexts, and as a visual counterpoint to pink.
- **Semantic status:** `info-blue`, `error-red`, `success-green`, and `warning-orange` are reserved for system feedback. Never use them for decorative purposes.

## Typography

Three typeface roles are used: **PP Telegraf** (with Manrope as fallback) for headings, **Manrope** for body copy, and **Roboto Mono** for code and technical output. PP Telegraf is a licensed display typeface; Manrope is the open-source fallback and is used directly for body text at all sizes. Both Manrope and Roboto Mono are available via [Google Fonts](https://fonts.google.com).

The type scale runs from `body-xs` (12px) through `display` (48px) with consistent line height ratios. Heading weights default to bold (700) or semibold (600). Body weights default to regular (400).

- Use `display` and `heading-xl` only for hero moments — page titles, empty states, major section headers.
- `body-md` is the default reading size for prose and UI copy.
- `body-sm` is used for button labels, captions, and metadata.
- `mono` (`Roboto Mono`) is reserved for code snippets, model output, and any content where exact character spacing matters.

## Layout

An 8px base unit underlies layout. The spacing scale (`2xs` through `6xl`) is a linear progression from 8px to 48px. All layout decisions should snap to this scale.

- Use `2xs` (8px) and `xs` (12px) for tight intra-component spacing (icon-to-label gaps, list item padding) and component internal padding.
- Use `md` (16px) through `xl` (20px) for inter-component gaps and section gutters.
- Use `2xl` (24px) and above for section-level separation.

## Elevation & Depth

Heavy shadows are not used. Depth is expressed through tonal layering — surfaces stack by shifting between `background` opacity levels. The `extra-dark-teal` opacity scale (4%, 10%, 20%) creates subtle container definitions without hard borders.

- `opacity-4` (4%): Subtle differentiation, barely perceptible — used for overlay headers and footers.
- `opacity-10` (10%): Light container backgrounds, hover states on text buttons.
- `opacity-20` (20%): Stroke/border level — input field borders, dividers.

**Floating surfaces** are the one exception. Panels that open over other content — dropdown menus and info tips — use the same fill as inputs with an `extra-dark-teal-20` border and a single soft shadow, `0 4px 12px` at 8% `extra-dark-teal`, so they read as above the page rather than part of it. Nothing that sits in the page flow uses this shadow.

## Shapes

Border radii follow the same numeric scale as spacing (`3xs` through `3xl`). The scale is intentionally wide to support the full range from sharp (`3xs: 4px`) to pill-shaped (`3xl: 32px`).

- **Buttons, inputs, chips, and avatars:** All use `rounded.3xs` (4px) — sharp and structured throughout the system.
- **Pill shapes:** Use `rounded.3xl` (32px) or a full-radius value for badge or tag variants that require a pill silhouette.
- **Avoid mixing radii** within a single component group — pick one scale level and apply it consistently.

## Components

### Sizes

Buttons, inputs, and chips share a common size scale: `sm` (32px), `md` (36px), `lg` (48px). Avatars use the same pixel values but extend down to `xs` (24px). All heights are outer measurements using `box-sizing: border-box` — borders are absorbed into the declared height so components align cleanly when composed side by side.

### Buttons

Four button intents are available: `interactive-default` (teal, neutral interactive), `interactive-primary` (pink, high-emphasis), `interactive-secondary` (green, supporting action), and `reversed` (cream, for use on dark backgrounds). Each intent has a filled and outlined variant. A shared `disabled` state applies across all button types.

Filled hover states lighten to a solid tint (the base color blended at 60% on cream). Outlined hover states fill with the lightest tint (20%) and shift text to `extra-dark-teal` for contrast. All transitions should use a 150ms ease-in-out curve.

### Form Inputs

Inputs use a white fill with a low-opacity `extra-dark-teal` stroke in their default state. On focus the stroke transitions to \`interactive-default\` (teal). On error the stroke becomes `error-red-dark` and text adopts the same color. Disabled inputs use a `gray-20` fill with `dark-teal` text.

### Dropdowns

A dropdown's closed state is an input: same fill, `extra-dark-teal-20` stroke, focus, error and disabled states, and the `sm`/`md`/`lg` size scale, with a small caret at the right in `extra-dark-teal-70`. Placeholder text uses `extra-dark-teal-60`. Focus shows the teal stroke only for keyboard focus, so the trigger doesn't stay highlighted after a mouse click.

The open menu is a floating surface (see Elevation & Depth): `dropdown-panel`, at least as wide as the trigger, 4px below it, scrolling past 320px tall. Items are `body-sm` with 8px vertical padding and room on the right for a check mark. The item under the pointer or keyboard cursor takes `dropdown-item-highlighted`; the selected item is semibold with a `dropdown-item-check` mark at the right.

Use a plain dropdown for short, fixed lists (levels, categories). For long lists such as people, add a `dropdown-search` field at the top of the panel, separated from the items by an `extra-dark-teal-20` divider, that filters as you type and shows "No matches." when nothing fits. Long lists can be grouped under `dropdown-group-label` headings. An item may carry faint secondary text after its label in `extra-dark-teal-60`; it is searchable too.

Dropdowns must work from the keyboard: arrow keys move the highlight, Enter selects, Escape closes, and typing in a searchable dropdown filters.

### Info tips

An info tip keeps secondary explanation — a definition, a rule of thumb — out of the layout until someone asks for it. The trigger is a small circled "i": 18px, `info-tip-trigger` text inside an `extra-dark-teal-40` ring, turning `interactive-default` (ring and letter) on hover, on keyboard focus, and while open. Place it right after the label it explains.

Clicking the trigger opens `info-tip-panel`, a floating surface above the trigger, aligned to its start, up to 320px wide. It opens on click or tap rather than hover so it works on touch screens and from the keyboard, and closes on Escape or a click outside. Keep the content to a sentence or two of plain text; anything longer belongs on the page. Give the trigger an accessible name that says what it explains (for example "About Autonomy").

### Form Controls

Checkbox, radio, and switch all share the same color logic: unchecked state uses a white fill with a `teal-80` stroke; checked state fills with \`interactive-default\` (teal) and uses `cream` for the mark or thumb. The switch thumb is 14×14px, inset 2px from the track edge.

The slider track is 8px tall. The filled (selected) portion uses \`interactive-default\` (teal); the unfilled portion uses `teal-20`.

### Chips

Chips use the same 4px radius and size scale as buttons. Three color intents are available: `interactive-default` (teal), `interactive-primary` (pink), and `interactive-secondary` (green). Chips are filled-only — outlined chips would compete with outlined buttons for the same visual role.

Two additional **subtle** variants — `subtle` and `extra-subtle` — render as translucent overlays that take their tone from the page surface (`extra-dark-teal` at 50% / 10% on a light page; on a dark page the overlay flips to `cream`). They pair with two foreground tokens: `on-subtle` (inverse of the page text, contrasts with the mid-tone `subtle` background) and `on-extra-subtle` (the standard page text, since `extra-subtle` is too close to the page surface for an inverse to read). Use `subtle` for tags that should sit a layer back from primary content; use `extra-subtle` for the lightest-touch background — barely-there tags, ghost states, or hover surfaces.

### Avatars

Avatars display initials, icons, or images in a fixed square container with 4px radius. Three color intents: `interactive-default` (extra-dark-teal), `interactive-primary` (pink), `interactive-secondary` (green). The same **subtle** and **extra-subtle** translucent variants used by chips are also available here, primarily for placeholder or "more authors" stack tiles. Sizes run from `xs` (24px) to `md` (36px). Font weight for initials should be semibold (600) for legibility at small sizes. For specific compositions that need a circular silhouette (e.g. stacked author lists), apply `rounded.3xl` (32px) at the call site — it exceeds half of every avatar size and renders as a circle.

## Do's and Don'ts

- **Do** use semantic color aliases (`{colors.interactive-primary}`, `{colors.text}`) rather than primitives directly.
- **Do** keep primary pink reserved for the single most important action per view.
- **Don't** use status colors (`error-red`, `success-green`, etc.) for decorative or categorical purposes.
- **Don't** mix button intents within a single action group — pick one hierarchy and apply it consistently.
- **Don't** use `mono` for UI copy — reserve it for code and model output.
- **Don't** use the floating-surface shadow on anything that sits in the page flow — it's only for menus and info tips that open over content.
