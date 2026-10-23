---
name: Asta
description: Ai2 design system — AI research assistant interface, dark mode
version: 0.0.1

assets:
  # ── Assets that align with the design system ──────────────────────
  logo: assets/logos/logo.svg
  wordmark: assets/logos/wordmark.svg
  slide-background-1: assets/slide backgrounds/1.png
  slide-background-2: assets/slide backgrounds/2.png
  slide-background-3: assets/slide backgrounds/3.png

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
  background: "{colors.extra-dark-teal}"
  background-reversed: "{colors.cream}"
  text: "{colors.cream}"
  text-reversed: "{colors.dark-teal}"
  text-disabled: "{colors.gray}"
  text-error: "{colors.error-red}"
  interactive-default: "{colors.teal}"
  interactive-default-hover: "{colors.teal-80}"
  interactive-primary: "{colors.green}"
  interactive-primary-hover: "{colors.green-60}"
  interactive-secondary: "{colors.green}"
  interactive-secondary-hover: "{colors.green-60}"
  link: "{colors.green}"
  link-reversed: "{colors.pink}"

  # ── Subtle surfaces ───────────────────────────────────────────────
  # Translucent overlays that take their tone from the inverse of the
  # page surface. On a light page: extra-dark-teal alpha. On a dark
  # page: cream alpha.
  subtle: "{colors.cream-50}"
  extra-subtle: "{colors.cream-10}"
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
    backgroundColor: "{colors.extra-dark-teal}"
    textColor: "{colors.cream}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-reversed-hover:
    backgroundColor: "{colors.dark-teal}"
    textColor: "{colors.cream}"
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
    textColor: "{colors.teal-40}"
    borderColor: "{colors.teal-40}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-default-outlined-hover:
    backgroundColor: "{colors.teal-80}"
    textColor: "{colors.cream}"
    borderColor: "{colors.teal-40}"
  button-reversed-outlined:
    backgroundColor: transparent
    textColor: "{colors.extra-dark-teal}"
    borderColor: "{colors.extra-dark-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-reversed-outlined-hover:
    backgroundColor: "{colors.extra-dark-teal}"
    textColor: "{colors.cream}"
    borderColor: "{colors.extra-dark-teal}"
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
    backgroundColor: "{colors.dark-teal}"
    textColor: "{colors.cream}"
    typography: "{typography.body-md}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  input-error:
    backgroundColor: "{colors.white}"
    textColor: "{colors.error-red-dark}"
    rounded: "{rounded.3xs}"
  input-disabled:
    backgroundColor: "{colors.extra-dark-teal}"
    textColor: "{colors.gray-40}"
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

This is the Ai2 design system for an AI-powered research assistant. The interface is dark by default and optimized for information-dense research workflows. The page surface is `extra-dark-teal` and the primary text color is `cream`.

Green is the primary brand accent — used for links, active states, and key interactive highlights.

The design language is measured and precise: generous line heights for long-form reading, compact interactive elements that don't interrupt the reading flow, and restrained use of color to keep attention on the content.

## Colors

Semantic color aliases:

- **Background:** `extra-dark-teal` (#032629) — the primary page surface.
- **Text:** `cream` (#faf2e9) — all body copy, headings, and labels.
- **Interactive-primary:** `green` (#0fcb8c) — links, active states, and key interactive highlights.
- **Interactive-default:** `teal` (#105257) — form controls and secondary interactive elements.

For surfaces and containers, use the `extra-dark-teal` opacity scale to layer depth without introducing new colors: 4% for subtle panel differentiation, 20% for borders and dividers.

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

## Shapes

Border radii follow the same numeric scale as spacing (`3xs` through `3xl`). The scale is intentionally wide to support the full range from sharp (`3xs: 4px`) to pill-shaped (`3xl: 32px`).

- **Buttons, inputs, chips, and avatars:** All use `rounded.3xs` (4px) — sharp and structured throughout the system.
- **Pill shapes:** Use `rounded.3xl` (32px) or a full-radius value for badge or tag variants that require a pill silhouette.
- **Avoid mixing radii** within a single component group — pick one scale level and apply it consistently.

## Components

### Buttons

Use small (`sm`, 32px) and medium (`md`, 36px) buttons only. Large buttons (`lg`, 48px) are not used — they interrupt the compact, information-dense layout. Default to `sm` for all actions within panels, toolbars, and inline controls.

The `button-default` (teal) is the default interactive button. The `button-primary` (green) is reserved for the single most prominent call to action per view.

The `button-default-outlined` uses `teal-40` for text and border so it reads against the dark page surface. The `button-reversed` family renders dark-on-cream — `extra-dark-teal` text and borders on a cream inverse surface.

### Typography

`body-md` (16px) is the default reading size for research output and document content. Use generous line heights — the interface surfaces long-form academic text, and whitespace aids comprehension.

## Do's and Don'ts

- **Do** use dark surfaces consistently — never mix light and dark surfaces within a single view.
- **Do** use `green` for all interactive highlights and primary actions.
- **Don't** use `button-size-lg` — it breaks the compact layout rhythm.
- **Don't** use high-saturation colors for decorative purposes — keep the palette restrained to let content breathe.
