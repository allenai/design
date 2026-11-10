---
name: ER Legacy
description: EarthRanger product interfaces in the palette used before the design-system adoption
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
  # dark mode inverts (not just darkens): backgrounds swap from warm
  # whites/off-whites to deep teal, text flips accordingly, and status
  # tokens shift to lighter/more-saturated primitive steps for contrast.

  # Background
  # Dark-mode surfaces climb a neutral grey ladder — Secondary (black) →
  # Primary/Elevated → Tertiary → Selected (lightest). Elevated shares a step
  # with Primary, so a raised surface reads by its stroke, not its tone.
  "UI/Background/Primary Background": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-1}" }
  "UI/Background/Secondary Background": { light: "{colors.greyscale-11}", dark: "{colors.greyscale-0}" }
  "UI/Background/Tertiary Background": { light: "{colors.greyscale-10}", dark: "{colors.greyscale-3}" }   # quiet surfaces: filter chips, map controls, read-only fields
  "UI/Background/Elevated Component": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-1}" }
  "UI/Background/Selected Background": { light: "{colors.blue-4}", dark: "{colors.blue-5}" }

  # Text
  "UI/Text/Primary Text": { light: "{colors.greyscale-0}", dark: "{colors.greyscale-white}" }
  "UI/Text/Primary Text Reversed": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-1}" }
  "UI/Text/Secondary Text": { light: "{colors.greyscale-5}", dark: "{colors.greyscale-8}" }
  "UI/Text/Secondary Text Reversed": { light: "{colors.blue-1}", dark: "{colors.blue-3}" }
  "UI/Text/Form Labels": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Text/Tabs": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Text/Disabled": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }

  # UI Chrome
  "UI/Icons": { light: "{colors.greyscale-5}", dark: "{colors.greyscale-7}" }
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

EarthRanger is a real-time platform for conservation: field reports, sensor telemetry and partner data on one map, used by protected-area managers, rangers, analysts and operations staff. Interfaces serve both field teams making time-sensitive decisions and analysts working through dense data at a desk, so the design language prioritizes **usability and data security above all else** — reliable and built for serious work, without being intimidating.

**ER Legacy is a bridge, not a fork.** EarthRanger Web adopted the design tokens and was repainted in the new palette in one step — blue calls to action became green, grey neutrals teal, blue selection teal. The architecture was the win; the whole palette change at the same moment was more than the product was ready for.

ER Legacy separates those. A product takes the token architecture now and the new colors when it suits, keeping the palette its users know in the meantime. **The second step is the point:** because both palettes share every token name, moving to EarthRanger is a change of token file — no redlines change, no component is touched. `UI/CTA Primary` is still `UI/CTA Primary`; it resolves to blue here and green there. A product adopts ER Legacy to make that move cheap, not to avoid it.

So a product picks one and stays on it until it switches. There is no blending the two. Use ER Legacy where a palette change would land alongside other disruption, or where users navigate by color; new surfaces should use EarthRanger. Anything that improves here should usually improve in EarthRanger too — this is a staging post, not a design direction.

## Colors

Always use **semantic tokens** (`UI/Text/Primary Text`) rather than raw primitives. They carry intent, give a Light and a Dark value, and adapt if the system changes.

**No new color values are introduced.** Every token resolves to a primitive EarthRanger already publishes; what differs is which primitive each points at. Seventeen tokens differ — the rest are identical, and are repeated so the spec stands alone.

The primary interactive color is `UI/CTA Primary` (`#0056c7` light / `#76b0ff` dark, Blue/1 and Blue/3), for calls to action, links and active states. **That is the defining difference from EarthRanger, whose CTA is green.** Note that `UI/Status/Running` shares the CTA's value here, so interactive and informational blue are the same color — rely on placement and component, not hue, to tell them apart. Status colors are otherwise strictly functional: use them to communicate meaning, never decoratively.

**Neutrals are grey, not teal.** Secondary text and icons are `Greyscale/5`, dividers `Greyscale/9`, field outlines `Greyscale/8`, the secondary background `Greyscale/11`, and the tertiary background `Greyscale/10` — the quiet surface filter chips, map controls and read-only fields sit on. Selection is blue-tinted (`Blue/4`), not teal. Icons share their value with secondary text, so an icon and its label read as one tier.

Teal survives as a primitive, used by `UI/Patrol Status/Scheduled`, but it is **not** a brand accent here and should not appear in navigation, headers or chrome — use `Greyscale/3` for dark chrome. **ER Legacy defines no brand tokens at all:** logo lockups, accent green and the brand backgrounds belong to EarthRanger and SERCA, and a surface needing them is a brand surface. Pink is never used, in either palette.

Use `UI/Text/Primary Text Reversed` for text or icon marks sitting on a filled CTA or other saturated surface.

The data scales — categorical, tracks and sequential — are **EarthRanger's, unchanged**, including the separate light and dark values on categorical. Use them in order, and resolve each through its token rather than copying a hex, so a chart keeps working when a product moves to EarthRanger.

### Dark mode

A **greyscale ladder, not EarthRanger's teal one.** Backgrounds step `Greyscale/1` (secondary) → `Greyscale/2` (primary) → `Greyscale/3` (elevated and tertiary). Text inverts to white, secondary text to `Greyscale/8`, icons and labels to `Greyscale/7`, dividers to `Greyscale/5`.

The CTA lightens to `Blue/3` and the secondary blue deepens to `Blue/5`. Status and priority colors move to softer steps so they read without glowing: error `Red/5`, warning `Amber/5`, success `Green/4`, priority green `Green/2`, patrol active `Indigo/5`, overdue `Magenta/4`.

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

The scale is Display, Heading (XL/LG/MD/SM), Body (LG/MD/SM/XS), Mono, and two button labels (`button-sm` 18px, `button-xs` 16px, SemiBold). Display and Headings are Bold; Body and Mono Regular.

### Fallback stack (performance)

EarthRanger runs in low-bandwidth field conditions where a delayed web font can mean delayed information at a bad moment. Always pair the web font with a fast, native fallback, never a generic one — see Do's and Don'ts for the checklist.

### Externally-facing communications

ER Legacy covers **product UI only**. For websites, decks, newsletters and print, see SERCA.

## Icons

> **Never substitute a different icon for the one shown in the design.**

### Library 1: Material Design Icons

Figma library `x3D0XAL06JEEEi12suKcGs`. Outlined by default, 24×24px. The primary library: look here first for any standard UI icon. Color them with `UI/Icons` (`#63666a` light / `#888b8d` dark) unless the design says otherwise.

### Library 2: ER Design System Custom Icons

ER Design System Figma file `gQJAI5XKeENQsqkCaFBev3`, Icons page. Custom filled icons for EarthRanger concepts Material does not cover (Patrol, Spoor, Basemap, Fence, Wildlife Sighting, GPS, Report, Deforestation). 18×18px, or 16×16px in menu bars and inline. Some have filled/outline or state variants — match the design exactly. Anything not listed as a custom symbol comes from Material.

## Do's and Don'ts

**Don't put `UI/Text/Primary Text` on a solid `UI/CTA Primary` fill.** In light mode it measures 3.16:1, under the 4.5:1 AA minimum for normal text — use `UI/Text/Primary Text Reversed`, which is white and measures 6.65:1. In dark mode the rule flips: `Blue/3` is light enough that **dark** text is correct at 8.47:1, while white falls to 2.23:1.

**Don't mix ER Legacy and EarthRanger on one screen.** They share token names deliberately, so loading both breaks nothing visibly — one quietly wins and you get a screen that is neither palette. Pick one per product.

**Don't use emojis — use an icon library.** Emojis render inconsistently across platforms and carry none of the states (filled/outline, active/inactive) the libraries provide.

**Don't load web fonts without these safeguards.** EarthRanger runs in low-bandwidth field conditions where a delayed font means delayed information during an active patrol or incident.

- **Native OS fallback** — Windows: Arial, Android: Roboto, iOS and macOS: SF Pro
- **Subset fonts** with `glyphhanger` or `fonttools`
- **Regular and Bold only** — don't ship the full weight range
- **`font-display: optional`** so a slow font never blocks rendering or shifts layout
- **Self-host** — no third-party CDN round trip
