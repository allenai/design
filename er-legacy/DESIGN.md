---
name: ER Legacy
description: EarthRanger product interfaces in the design system carried forward from the 2021 app
version: 0.0.1

assets:
  logo: assets/EarthRanger-logo.svg
  logo-horizontal: assets/EarthRanger-logo-H.svg
  logo-white: assets/EarthRanger-logo-white.svg
  logo-white-horizontal: assets/EarthRanger-logo-White-H.svg
  logo-icon: assets/EarthRanger-Logo-icon.svg
  logo-icon-white: assets/EarthRanger-Logo-icon-white.svg
  # The 2026 by-Ai2 lockups. The -short variants scale the by-Ai2 mark up
  # relative to the EarthRanger wordmark, so the attribution stays legible
  # when the logo is small: use them below 56px of rendered logo height.
  logo-ai2: assets/EarthRanger-Logo-2026_Ai2.svg
  logo-ai2-horizontal: assets/EarthRanger-Logo-2026_Ai2-H.svg
  logo-ai2-horizontal-short: assets/EarthRanger-Logo-2026_Ai2-H-short.svg
  logo-ai2-white: assets/EarthRanger-Logo-2026_Ai2-white.svg
  logo-ai2-white-horizontal: assets/EarthRanger-Logo-2026_Ai2-white-H.svg
  logo-ai2-white-horizontal-short: assets/EarthRanger-Logo-2026_Ai2-white-H-short.svg

colors:
  # ── Semantic UI Tokens ────────────────────────────────────────────
  # Use these first. Semantic tokens carry intent and adapt if the
  # design system is updated. Three-layer architecture: Primitives →
  # Tokens → Platform. Tokens below list both Light and Dark values —
  # dark mode inverts (not just darkens): backgrounds swap from white and
  # Grey/11 to black and Grey/1, text flips accordingly, and status tokens
  # shift to lighter/more-saturated primitive steps for contrast.

  # Background
  # Listed from the quietest surface to the most forward: the page sits on
  # Tertiary or Secondary, Elevated Component 0 is the banded sub-surface
  # inside a panel (a table header, a row label) and the fill behind a
  # default button, and Elevated and Primary are the panel itself. In dark
  # the quiet surfaces sit on black and the panel on Grey/1, so a panel
  # reads as lifted while the page recedes.
  "UI/Background/Tertiary Background": { light: "{colors.greyscale-11}", dark: "{colors.greyscale-0}" }   # quiet surfaces: filter chips, map controls, read-only fields
  "UI/Background/Secondary Background": { light: "{colors.greyscale-11}", dark: "{colors.greyscale-0}" }
  "UI/Background/Elevated Component 0": { light: "{colors.greyscale-10}", dark: "{colors.greyscale-2}" }   # banded sub-surface inside a panel (table header, row label); also the default button fill
  "UI/Background/Elevated Component": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-1}" }
  "UI/Background/Primary Background": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-1}" }
  "UI/Background/Selected Background": { light: "{colors.blue-4}", dark: "{colors.blue-5}" }   # selection, and the hover fill behind an outlined button
  "UI/Background/Hover Background": { light: "{colors.blue-2}", dark: "{colors.blue-5}" }   # the fill a surface or control takes on hover

  # Text
  "UI/Text/Primary Text": { light: "{colors.greyscale-0}", dark: "{colors.greyscale-white}" }
  "UI/Text/Primary Text Reversed": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-1}" }
  "UI/Text/Secondary Text": { light: "{colors.greyscale-5}", dark: "{colors.greyscale-8}" }
  "UI/Text/Secondary Text Reversed": { light: "{colors.blue-1}", dark: "{colors.blue-3}" }
  "UI/Text/Form Labels": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Text/Tabs": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Text/Disabled": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }

  # UI Chrome
  "UI/Icons": { light: "{colors.greyscale-4}", dark: "{colors.greyscale-9}" }
  "UI/Field Outline": { light: "{colors.greyscale-8}", dark: "{colors.greyscale-4}" }
  "UI/Divider Lines": { light: "{colors.greyscale-9}", dark: "{colors.greyscale-3}" }

  # Actions
  "UI/CTA Primary": { light: "{colors.blue-1}", dark: "{colors.blue-3}" }
  "UI/CTA Secondary": { light: "{colors.blue-2}", dark: "{colors.blue-5}" }
  "UI/CTA Text": { light: "{colors.blue-1}", dark: "{colors.blue-3}" }   # text and marks on a CTA Secondary fill

  # Status
  "UI/Status/Error-Destructive": { light: "{colors.red-3}", dark: "{colors.red-5}" }
  "UI/Status/Success": { light: "{colors.green-3}", dark: "{colors.green-4}" }
  "UI/Status/Running": { light: "{colors.blue-1}", dark: "{colors.blue-3}" }
  "UI/Status/Warning": { light: "{colors.amber-3}", dark: "{colors.amber-5}" }
  "UI/Status/Disabled": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Status/Ready": { light: "{colors.yellow-3}", dark: "{colors.yellow-3}" }

  # Status Backgrounds
  "UI/Status Bg/Synced Bg": { light: "{colors.green-6}", dark: "{colors.green-8}" }
  "UI/Status Bg/Pending Sync Bg": { light: "{colors.greyscale-10}", dark: "{colors.greyscale-5}" }
  "UI/Status Bg/Error Bg": { light: "{colors.red-6}", dark: "{colors.red-1}" }
  "UI/Status Bg/Draft Bg": { light: "{colors.blue-2}", dark: "{colors.blue-5}" }
  "UI/Status Bg/Active Bg": { light: "{colors.indigo-6}", dark: "{colors.indigo-4}" }
  "UI/Status Bg/Warning Bg": { light: "{colors.amber-6}", dark: "{colors.amber-1}" }

  # Event Priority
  "UI/Event Priority/Green": { light: "{colors.green-1}", dark: "{colors.green-2}" }
  "UI/Event Priority/Red": { light: "{colors.red-3}", dark: "{colors.red-5}" }
  "UI/Event Priority/Amber": { light: "{colors.amber-3}", dark: "{colors.amber-5}" }
  "UI/Event Priority/Grey": { light: "{colors.greyscale-7}", dark: "{colors.greyscale-7}" }

  # Patrol Status
  "UI/Patrol Status/Active": { light: "{colors.indigo-2}", dark: "{colors.indigo-5}" }
  "UI/Patrol Status/Paused": { light: "{colors.yellow-2}", dark: "{colors.yellow-3}" }
  "UI/Patrol Status/Overdue": { light: "{colors.magenta-2}", dark: "{colors.magenta-4}" }
  "UI/Patrol Status/Scheduled": { light: "{colors.teal-1}", dark: "{colors.teal-2}" }
  "UI/Patrol Status/Track Line (Mobile)": { light: "{colors.amber-3}", dark: "{colors.amber-3}" }
  "UI/Patrol Status/Done (Mobile)": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }

  # Data Visualization — Categorical (mode-specific: dark values are the
  # brighter/darker counterparts; slots 6–10 swap the light/dark steps)
  "UI/Data/Categorical/Category 1": { light: "{colors.teal-4}", dark: "{colors.teal-5}" }
  "UI/Data/Categorical/Category 2": { light: "{colors.indigo-2}", dark: "{colors.indigo-3}" }
  "UI/Data/Categorical/Category 3": { light: "{colors.green-9}", dark: "{colors.green-10}" }
  "UI/Data/Categorical/Category 4": { light: "{colors.magenta-2}", dark: "{colors.magenta-3}" }
  "UI/Data/Categorical/Category 5": { light: "{colors.yellow-2}", dark: "{colors.yellow-4}" }
  "UI/Data/Categorical/Category 6": { light: "{colors.teal-5}", dark: "{colors.teal-4}" }
  "UI/Data/Categorical/Category 7": { light: "{colors.indigo-3}", dark: "{colors.indigo-2}" }
  "UI/Data/Categorical/Category 8": { light: "{colors.green-10}", dark: "{colors.green-9}" }
  "UI/Data/Categorical/Category 9": { light: "{colors.yellow-4}", dark: "{colors.yellow-2}" }
  "UI/Data/Categorical/Category 10": { light: "{colors.magenta-3}", dark: "{colors.magenta-2}" }

  # Data Visualization — Tracks
  "UI/Data/Tracks/Track 1": "{colors.indigo-2}"
  "UI/Data/Tracks/Track 2": "{colors.magenta-2}"
  "UI/Data/Tracks/Track 3": "{colors.amber-4}"
  "UI/Data/Tracks/Track 4": "{colors.magenta-3}"
  "UI/Data/Tracks/Track 5": "{colors.blue-7}"
  "UI/Data/Tracks/Track 6": "{colors.red-2}"
  "UI/Data/Tracks/Track 7": "{colors.purple-2}"
  "UI/Data/Tracks/Track 8": "{colors.green-5}"
  "UI/Data/Tracks/Track 9": "{colors.blue-6}"
  "UI/Data/Tracks/Track 10": "{colors.red-4}"

  # Data Visualization — Sequential
  "UI/Data/Sequential/Sequential 1": "{colors.yellow-4}"
  "UI/Data/Sequential/Sequential 2": "{colors.yellow-3}"
  "UI/Data/Sequential/Sequential 3": "{colors.magenta-3}"
  "UI/Data/Sequential/Sequential 4": "{colors.purple-2}"
  "UI/Data/Sequential/Sequential 5": "{colors.indigo-3}"
  "UI/Data/Sequential/Sequential 6": "{colors.blue-1}"
  "UI/Data/Sequential/Sequential 7": "{colors.green-3}"
  "UI/Data/Sequential/Sequential 8": "{colors.green-10}"


  # ── Primitive Palette ─────────────────────────────────────────────
  # Use only when no semantic token fits. Single mode (HEX) — not used
  # directly in designs; referenced by tokens above.

  # Greyscale (0 = black, 11 = near-white; Off-white is warm/cream)
  greyscale-0: "#000000"
  greyscale-1: "#111111"
  greyscale-2: "#222222"
  greyscale-3: "#333333"
  greyscale-4: "#444444"
  greyscale-5: "#63666a"
  greyscale-6: "#767676"
  greyscale-7: "#888b8d"
  greyscale-8: "#b1b3b3"
  greyscale-9: "#dddddd"
  greyscale-10: "#f3f3f3"
  greyscale-11: "#f9f9f9"
  greyscale-off-white: "#faf2e9"
  greyscale-off-white-50: "#fdf9f4"
  greyscale-white: "#ffffff"

  # Blue
  blue-1: "#0056c7"
  blue-2: "#dde8f8"
  blue-3: "#76b0ff"
  blue-4: "#f4f7fd"
  blue-5: "#2a394d"
  blue-6: "#002960"
  blue-7: "#3089ff"

  # Indigo
  indigo-1: "#331878"
  indigo-2: "#3e35a3"
  indigo-3: "#5c4fe7"
  indigo-4: "#57528c"
  indigo-5: "#867ede"
  indigo-6: "#f5f5fa"

  # Green
  green-1: "#006842"
  green-2: "#83af52"
  green-3: "#00882e"
  green-4: "#53aa71"
  green-5: "#004e26"
  green-6: "#f5f7f3"
  green-7: "#0fcb8c"
  green-8: "#53693a"
  green-9: "#488a00"
  green-10: "#78d811"
  green-11: "#a1e458"
  green-12: "#0f865d"

  # Teal
  teal-1: "#107283"
  teal-2: "#62bfd0"
  teal-3: "#008586"
  teal-4: "#00958f"
  teal-5: "#00d0c8"
  teal-ai2-dark-teal: "#0a3235"
  teal-ai2-extra-dark-teal: "#032629"
  teal-darkest: "#02191b"
  teal-dark-90: "#1c3c3e"
  teal-dark-80: "#355154"
  teal-t100: "#105257"
  teal-t90: "#27545f"
  teal-t80: "#407579"
  teal-t70: "#588689"
  teal-t60: "#70979a"
  teal-t50: "#87a8ab"
  teal-t40: "#9fbabc"
  teal-t30: "#b7cbcd"
  teal-t20: "#cfdcdd"
  teal-t10: "#e7eeee"
  teal-3-05: "#f2f9f9"

  # Red
  red-1: "#3e2125"
  red-2: "#8c1700"
  red-3: "#d0031b"
  red-4: "#f23b0e"
  red-5: "#f06374"
  red-6: "#fdf2f4"

  # Amber
  amber-1: "#362922"
  amber-2: "#b83f00"
  amber-3: "#e76826"
  amber-4: "#ff803e"
  amber-5: "#fd9964"
  amber-6: "#fef7f4"

  # Yellow
  yellow-1: "#9d6900"
  yellow-2: "#c6880c"
  yellow-3: "#ffb700"
  yellow-4: "#f4db20"

  # Magenta
  magenta-1: "#8b0f56"
  magenta-2: "#b62879"
  magenta-3: "#ed3ea2"
  magenta-4: "#e76eb3"

  # Purple
  purple-1: "#71038e"
  purple-2: "#a100cb"
  purple-3: "#cc74e6"

typography:
  # ── Platform font-family ──────────────────────────────────────────
  # Controls font-family per platform. All text styles below share
  # this — reference a platform, don't hardcode a family.
  platform:
    body:
      web-fonts: Roboto
      windows: Arial
      ios: SF Pro
      android: Roboto
    heading:
      web-fonts: Roboto
      windows: Arial
      ios: SF Pro
      android: Roboto

  # ── Text Styles ───────────────────────────────────────────────────
  # One Roboto scale. Headings and body share a family and differ only by
  # weight and size.
  # No style sets a line height: the layout decides. 0 letter-spacing and
  # no text-transform throughout.
  display:
    fontFamily: Roboto
    fontStyle: Bold
    fontSize: 48px

  heading-xl:
    fontFamily: Roboto
    fontStyle: Bold
    fontSize: 40px

  heading-lg:
    fontFamily: Roboto
    fontStyle: Bold
    fontSize: 32px

  heading-md:
    fontFamily: Roboto
    fontStyle: Bold
    fontSize: 24px

  heading-sm:
    fontFamily: Roboto
    fontStyle: Bold
    fontSize: 20px

  # UI headings: Roboto Medium, for headings inside product UI, matching
  # EarthRanger's own. No line height set — the layout decides.
  heading-ui-lg:
    fontFamily: Roboto
    fontWeight: 500
    fontSize: 32px

  heading-ui-md:
    fontFamily: Roboto
    fontWeight: 500
    fontSize: 24px

  # Button labels: Roboto SemiBold.
  button-sm:
    fontFamily: Roboto
    fontWeight: 600
    fontSize: 18px

  button-xs:
    fontFamily: Roboto
    fontWeight: 600
    fontSize: 16px

  body-lg:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 18px

  body-md:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 16px

  body-sm:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 14px

  body-xs:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 12px

  # ── Monospace ─────────────────────────────────────────────────────
  mono:
    fontFamily: Roboto Mono
    fontStyle: Regular
    fontSize: 14px

---

## Overview

EarthRanger is a platform for conservationists to collect data from the field, integrate cutting-edge technology, see wildlife and teams in real time, and develop strategies that accelerate conservation impact. The platform encompasses EarthRanger Web, EarthRanger Mobile, Ecoscope, Gundi, and the Buoy app — a suite of tools built around data-driven decision making and adaptive management.

EarthRanger is used by a broad range of conservation professionals: protected area managers, field personnel, analysts, operations coordinators, and technologists. Interfaces must serve both experts in the field making time-sensitive decisions and analysts working through complex data sets at a desk.

The design language prioritizes usability, accessibility, and data security above all else. EarthRanger is trustworthy, innovative, and approachable. Every interface decision should reinforce that the platform is reliable and built for serious work — without being intimidating or opaque.

EarthRanger Legacy is a design system built from what existed in the app from 2021. The system was built for utility to remain steady as the brand around EarthRanger evolved. The primary CTA color is blue; a lighter blue is the secondary accent. Pink is never used in EarthRanger interfaces. Dark mode is a first-class, fully-defined mode (not just light-mode tokens dimmed) — it inverts rather than darkens: backgrounds swap from white/light grey to black/dark grey, text flips accordingly, and status colors shift to lighter/more-saturated steps for contrast on the dark surface. Track and sequential data colors are mode-stable — the same primitives work on both light and dark backgrounds. Categorical data colors have separate light and dark values.

## Colors

Always use **semantic tokens** (e.g. `UI/Text/Primary Text`) instead of raw primitive values wherever possible. Semantic tokens carry intent, provide both a Light and Dark value, and will automatically adapt if the design system is updated.

The primary interactive color is `UI/CTA Primary` — used for calls to action, links, and active states. `UI/CTA Secondary` is the quiet companion fill behind a secondary action. Status colors are strictly functional: use them only to communicate meaning (error, success, warning, running/informational), never decoratively. Note that `UI/Status/Running` resolves to the same blue as `UI/CTA Primary`, so informational and interactive blue look alike — rely on placement and component to tell them apart, and reach for `UI/CTA Primary` for anything the user can act on.

**Neutrals are greyscale.** `UI/Text/Secondary Text`, `UI/Icons`, `UI/Field Outline` and `UI/Divider Lines` all resolve to greys, as do `UI/Background/Secondary Background` and `UI/Background/Tertiary Background` — which share one value, the quiet surface filter chips, map controls and read-only fields sit on. `UI/Background/Elevated Component 0` is the banded sub-surface inside a panel such as a table header or a row label, and the fill behind a default button — whose label is `UI/Icons`, so a button's label and the icon beside it read as one tier; the fill darkens on hover rather than inverting that label. `UI/Background/Selected Background` carries selection, and fills an outlined button on hover; `UI/Background/Hover Background` is the fill a surface or control takes on hover. `UI/Icons` sits a step darker than `UI/Text/Secondary Text` in light mode and a step brighter in dark, so icons and default button labels stay legible on the near-black panel.

Use `UI/Text/Primary Text Reversed` (the inverse of `UI/Text/Primary Text`) for text or icon marks that sit directly on a saturated surface, such as a filled CTA or a checked control's mark. The CTA is a mid-tone blue in light mode but a pale tint in dark mode, so a fixed light color reads fine in light mode and disappears in dark — this token flips with the mode so it always contrasts against the surface it's on.

Pink is not part of the palette. Do not introduce any pink values, even from the broader Ai2 primitive palette.

For data visualization, use the categorical, tracks, and sequential scales in order — do not skip steps or substitute other colors. These scales are designed for perceptual distinctiveness and accessibility across the full range of values. Tracks and sequential are intentionally identical in Light and Dark mode; categorical uses a separate value per mode, so always resolve it through the token rather than copying a hex.

## Typography

**Roboto throughout.** Headings and body share one family and differ only by weight and size; there is no separate heading face.

| Platform | Body | Heading |
| --- | --- | --- |
| Web Fonts | Roboto | Roboto |
| Windows | Arial | Arial |
| iOS | SF Pro | SF Pro |
| Android | Roboto | Roboto |

Reference a text-style token (`body-md`, `heading-lg`) rather than hardcoding font properties — the platform family resolves automatically. `body-md` (16px) is the default reading size. 0 letter-spacing, no text-transform.

**No style sets a line height.** The layout decides, so one token suits a dense table row and a roomy card alike.

The scale is Display, Heading (XL/LG/MD/SM), Body (LG/MD/SM/XS), Mono, two UI headings (`heading-ui-lg` 32px, `heading-ui-md` 24px, Medium) and two button labels (`button-sm` 18px, `button-xs` 16px, SemiBold). Display and Headings are Bold; Body and Mono Regular. The UI headings and button labels set no line height.

### Fallback stack (performance)

EarthRanger runs in low-bandwidth field conditions where a delayed web font can mean delayed information at a bad moment. Always pair the web font with a fast, native fallback, never a generic one — see Do's and Don'ts for the checklist.

### Externally-facing communications

This system covers **product UI only**. For websites, decks, newsletters and print, see **External communications** in `earthranger/DESIGN.md`.

## Icons

> **Never substitute a different icon for the one shown in the design.**

### Library 1: Material Design Icons

Figma library `x3D0XAL06JEEEi12suKcGs`. Outlined by default, 24×24px. The primary library: look here first for any standard UI icon. Color them with `UI/Icons` unless the design says otherwise.

### Library 2: ER Design System Custom Icons

ER Design System Figma file `gQJAI5XKeENQsqkCaFBev3`, Icons page. Custom filled icons for EarthRanger concepts Material does not cover (Patrol, Spoor, Basemap, Fence, Wildlife Sighting, GPS, Report, Deforestation). 18×18px, or 16×16px in menu bars and inline. Some have filled/outline or state variants — match the design exactly. Anything not listed as a custom symbol comes from Material.

## Do's and Don'ts

**Don't put `UI/Text/Primary Text` on a solid `UI/CTA Primary` fill.** In light mode it measures 3.16:1, under the 4.5:1 AA minimum for normal text — use `UI/Text/Primary Text Reversed`, which is white and measures 6.65:1. In dark mode the rule flips: `Blue/3` is light enough that **dark** text is correct at 8.47:1, while white falls to 2.23:1.

**Don't load two token files at once.** Every EarthRanger-family system emits the same token names, so a second one layered on top breaks nothing visibly — one quietly wins and you get a screen that is neither palette. A product loads one, and swaps it whole when it moves.

**Don't use emojis — use an icon library.** Emojis render inconsistently across platforms and carry none of the states (filled/outline, active/inactive) the libraries provide.

**Don't load web fonts without these safeguards.** EarthRanger runs in low-bandwidth field conditions where a delayed font means delayed information during an active patrol or incident.

- **Native OS fallback** — Windows: Arial, Android: Roboto, iOS and macOS: SF Pro
- **Subset fonts** with `glyphhanger` or `fonttools`
- **Regular and Bold only** — don't ship the full weight range
- **`font-display: optional`** so a slow font never blocks rendering or shifts layout
- **Self-host** — no third-party CDN round trip
