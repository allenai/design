---
name: Asta
description: Ai2 design system — AI research assistant interface, dark mode
version: 0.0.1

assets:
  logo: assets/logos/logo.svg
  wordmark: assets/logos/wordmark.svg
  slide-background-1: assets/slide backgrounds/1.png
  slide-background-2: assets/slide backgrounds/2.png
  slide-background-3: assets/slide backgrounds/3.png

colors:
  # ── Semantic aliases ──────────────────────────────────────────────
  # Dark mode. Page surface is extra-dark-teal; primary text is cream.
  background: "{colors.extra-dark-teal}"
  background-reversed: "{colors.cream}"
  text: "{colors.cream}"
  text-reversed: "{colors.dark-teal}"

  interactive-primary: "{colors.green}"
  interactive-primary-hover: "{colors.green-60}"
  link: "{colors.green}"
  link-reversed: "{colors.pink}"

  # Translucent overlays on the dark page surface use cream alpha.
  subtle: "{colors.cream-50}"
  extra-subtle: "{colors.cream-10}"

components:
  # ── Inputs ────────────────────────────────────────────────────────
  # Inputs use a dark surface. Text is cream.
  input-default:
    backgroundColor: "{colors.dark-teal}"
    textColor: "{colors.cream}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  input-disabled:
    backgroundColor: "{colors.extra-dark-teal}"
    textColor: "{colors.gray-40}"
    rounded: "{rounded.3xs}"

  # ── Buttons ───────────────────────────────────────────────────────
  # `teal` (#105257) falls below 1.5:1 on the extra-dark-teal page
  # surface. Outlined-default uses teal-40 so it reads against the page.
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

  # The "reversed" surface is cream — the inverse of the default
  # extra-dark-teal page. Reversed buttons render dark on that cream
  # inverse surface.
  button-reversed:
    backgroundColor: "{colors.extra-dark-teal}"
    textColor: "{colors.cream}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.3xs}"
    padding: "{spacing.xs}"
  button-reversed-hover:
    backgroundColor: "{colors.dark-teal}"
    textColor: "{colors.cream}"
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
