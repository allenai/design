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
  # Dark-mode surfaces form one continuous teal ladder — Secondary/Tertiary
  # (darkest) → Primary/Elevated → Selected (lightest) — rather than mixing
  # in grey.
  "UI/Background/Primary Background": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-2}" }
  "UI/Background/Secondary Background": { light: "{colors.greyscale-11}", dark: "{colors.greyscale-1}" }
  "UI/Background/Tertiary Background": { light: "{colors.greyscale-11}", dark: "{colors.greyscale-1}" }   # the same as Secondary Background: ER Legacy has no third surface tone
  "UI/Background/Elevated Component": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-3}" }
  "UI/Background/Selected Background": { light: "{colors.blue-4}", dark: "{colors.blue-5}" }   # dark is proposed: the legacy frame has no selected background

  # Text
  "UI/Text/Primary Text": { light: "{colors.greyscale-0}", dark: "{colors.greyscale-white}" }
  "UI/Text/Primary Text Reversed": { light: "{colors.greyscale-white}", dark: "{colors.teal-ai2-dark-teal}" }
  "UI/Text/Secondary Text": { light: "{colors.greyscale-5}", dark: "{colors.greyscale-8}" }
  "UI/Text/Secondary Text Reversed": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-2}" }   # sits on the opposite surface, so it takes the other mode's background
  "UI/Text/Form Labels": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Text/Tabs": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }
  "UI/Text/Disabled": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }

  # UI Chrome
  "UI/Icons": { light: "{colors.greyscale-5}", dark: "{colors.greyscale-7}" }   # deviates from the Figma legacy frame, which has Greyscale/6
  "UI/Field Outline": { light: "{colors.greyscale-8}", dark: "{colors.greyscale-3}" }
  "UI/Divider Lines": { light: "{colors.greyscale-9}", dark: "{colors.greyscale-5}" }

  # Actions
  "UI/CTA Primary": { light: "{colors.blue-1}", dark: "{colors.blue-3}" }
  "UI/CTA Secondary Blue": { light: "{colors.blue-2}", dark: "{colors.blue-5}" }

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
  "UI/Data/Categorical/Category 1": { light: "{colors.indigo-2}", dark: "{colors.indigo-2}" }   # the legacy frame draws this scale once, not per mode
  "UI/Data/Categorical/Category 2": { light: "{colors.green-9}", dark: "{colors.green-9}" }   # the legacy frame draws this scale once, not per mode
  "UI/Data/Categorical/Category 3": { light: "{colors.teal-4}", dark: "{colors.teal-4}" }   # the legacy frame draws this scale once, not per mode
  "UI/Data/Categorical/Category 4": { light: "{colors.magenta-2}", dark: "{colors.magenta-3}" }
  "UI/Data/Categorical/Category 5": { light: "{colors.yellow-2}", dark: "{colors.yellow-4}" }
  "UI/Data/Categorical/Category 6": { light: "{colors.teal-5}", dark: "{colors.teal-4}" }
  "UI/Data/Categorical/Category 7": { light: "{colors.green-10}", dark: "{colors.green-10}" }   # the legacy frame draws this scale once, not per mode
  "UI/Data/Categorical/Category 8": { light: "{colors.indigo-3}", dark: "{colors.indigo-3}" }   # the legacy frame draws this scale once, not per mode
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

  # Brand
  "Brand/Acorn Logo": { light: "{colors.teal-3}", dark: "{colors.teal-3}" }
  "Brand/Accent Green": { light: "{colors.green-7}", dark: "{colors.green-7}" }
  "Brand/Background/Primary Background": { light: "{colors.greyscale-off-white}", dark: "{colors.teal-ai2-dark-teal}" }
  "Brand/Background/Secondary Background": { light: "{colors.greyscale-white}", dark: "{colors.teal-t100}" }
  "Brand/Text/Primary Text": { light: "{colors.teal-ai2-dark-teal}", dark: "{colors.greyscale-white}" }
  "Brand/Text/Secondary Text": { light: "{colors.teal-t100}", dark: "{colors.greyscale-off-white}" }

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
      web-fonts: PP Telegraf
      windows: Arial
      ios: SF Pro
      android: Roboto

  # ── Strata Text Styles ────────────────────────────────────────────
  # Shared scale (0 letter-spacing, no text-transform on any style).
  # Display & Headings: PP Telegraf Bold. Body: Roboto Regular.
  display:
    fontFamily: PP Telegraf
    fontStyle: Bold
    fontSize: 48px
    lineHeight: 52.8px

  heading-xl:
    fontFamily: PP Telegraf
    fontStyle: Bold
    fontSize: 40px
    lineHeight: 48px

  heading-lg:
    fontFamily: PP Telegraf
    fontStyle: Bold
    fontSize: 32px
    lineHeight: 38.4px

  heading-md:
    fontFamily: PP Telegraf
    fontStyle: Bold
    fontSize: 24px
    lineHeight: 31.2px

  heading-sm:
    fontFamily: PP Telegraf
    fontStyle: Bold
    fontSize: 20px
    lineHeight: 28px

  # UI headings: Roboto Medium, for headings inside product UI. No
  # line-height set (Figma uses auto) — the layout decides.
  heading-ui-lg:
    fontFamily: Roboto
    fontWeight: 500
    fontSize: 32px

  heading-ui-md:
    fontFamily: Roboto
    fontWeight: 500
    fontSize: 24px

  # Button labels: Roboto SemiBold. No line-height set (Figma uses auto).
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
    lineHeight: 28.8px

  body-md:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 16px
    lineHeight: 25.6px

  body-sm:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 14px
    lineHeight: 21px

  body-xs:
    fontFamily: Roboto
    fontStyle: Regular
    fontSize: 12px
    lineHeight: 18px

  # ── Monospace ─────────────────────────────────────────────────────
  mono:
    fontFamily: Roboto Mono
    fontStyle: Regular
    fontSize: 14px
    lineHeight: 22.4px

  # ── External Communications (NOT for product UI) ──────────────────
  # Manrope, body text only. Scope: slide decks, EarthRanger.com, email
  # newsletters, printed materials. Headings in these contexts still use
  # PP Telegraf (see Strata Text Styles above) — only body text changes.
  external-comms-body-lg:
    fontFamily: Manrope
    fontStyle: Regular
    fontSize: 18px
    lineHeight: 28.8px

  external-comms-body-md:
    fontFamily: Manrope
    fontStyle: Regular
    fontSize: 16px
    lineHeight: 25.6px

  external-comms-body-sm:
    fontFamily: Manrope
    fontStyle: Regular
    fontSize: 14px
    lineHeight: 21px

  external-comms-body-xs:
    fontFamily: Manrope
    fontStyle: Regular
    fontSize: 12px
    lineHeight: 18px
---

## Overview

EarthRanger is a platform for conservationists to collect data from the field, integrate cutting-edge technology, see wildlife and teams in real time, and develop strategies that accelerate conservation impact. The platform encompasses EarthRanger Web, EarthRanger Mobile, Ecoscope, Gundi, and the Buoy app — a suite of tools built around data-driven decision making and adaptive management.

EarthRanger is used by a broad range of conservation professionals: protected area managers, field personnel, analysts, operations coordinators, and technologists. Interfaces must serve both experts in the field making time-sensitive decisions and analysts working through complex data sets at a desk.

The design language prioritizes **usability and data security above all else**. EarthRanger is trustworthy, innovative, and approachable. Every interface decision should reinforce that the platform is reliable and built for serious work — without being intimidating or opaque.

**ER Legacy is the EarthRanger palette as it stood before the design-system adoption.** It is a color variant of EarthRanger, not a separate product: the voice, typography, iconography, logos, and layout are EarthRanger's, and only the color tokens differ. It exists so surfaces that need continuity can keep the colors their users already know while the rest of the design system moves forward.

ER Legacy and EarthRanger are two skins over the same components. **Every token has the same name in both**, so a screen specced against one works against the other without a single redline changing — `UI/CTA Primary` is still `UI/CTA Primary`, it simply resolves to blue here and green there. That is what makes moving a product between them a palette swap rather than a redesign.

The flip side is that a product picks one and stays on it, the way you would not run two themes on the same screen. There is no blending the two, and no screen that is half of each.

Use it where continuity matters more than alignment — an established interface whose users navigate by color, or a release where a palette change would land alongside other disruption. New surfaces should use EarthRanger. This spec records a palette that already existed so it can be versioned, shared, and changed in one place rather than hand-maintained per application; it is not a design direction, and anything that improves here should usually improve in EarthRanger too.

## Colors

Always use **semantic tokens** (e.g. `UI/Text/Primary Text`) instead of raw primitive values wherever possible. Semantic tokens carry intent, provide both a Light and Dark value, and will automatically adapt if the design system is updated.

ER Legacy uses EarthRanger's primitives unchanged. **No new color values are introduced** — every token here resolves to a primitive EarthRanger already publishes. What differs is which primitive each semantic token points at. Twenty-three semantic tokens differ; the rest are identical and are repeated here so the spec stands on its own.

The primary interactive color is `UI/CTA Primary` (`#0056c7` light / `#76b0ff` dark, Blue/1 and Blue/3) — used for calls to action, links, and active states. **This is the defining difference from EarthRanger, whose CTA is green.** Status colors are strictly functional: use them only to communicate meaning (error, success, warning, running/informational), never decoratively. Blue also covers in-progress state and general informational messaging via `UI/Status/Running`, which shares the CTA's value here — so in ER Legacy, unlike EarthRanger, interactive and informational blues are the same color. Rely on placement and component, not hue, to tell them apart.

**Neutrals are grey, not teal.** `UI/Text/Secondary Text` and `UI/Icons` are `Greyscale/5` (`#63666a`), dividers are `Greyscale/9` (`#dddddd`), field outlines are `Greyscale/8` (`#b1b3b3`), and the tertiary and secondary backgrounds are `Greyscale/10` and `Greyscale/11`. EarthRanger tints all of these toward teal; ER Legacy does not. Selection is blue-tinted (`UI/Background/Selected Background`, `Blue/4` `#f4f7fd`) rather than teal.

`UI/Icons` shares its value with `UI/Text/Secondary Text`, so an icon and the label beside it read as one tier.

The 2026 by-Ai2 logo is drawn in this palette rather than EarthRanger's: `Greyscale/3` for the EarthRanger wordmark, `Greyscale/5` for the by-Ai2 lockup, `Teal/3` for the mark, and `Greyscale/9` for the lockup on the white variants. It needs no recoloring here.

Teal remains available as a primitive and is still used by `UI/Patrol Status/Scheduled` (`Teal/1`), but it is **not** a brand accent in ER Legacy and should not appear in navigation, headers, or chrome. Use `Greyscale/3` (`#333333`) for dark chrome instead.

Use `UI/Text/Primary Text Reversed` (`#ffffff` light) for text or icon marks that sit directly on a filled CTA or other saturated surface. Pink is not part of the EarthRanger palette. Do not introduce any pink values, even from the broader Ai2 primitive palette.

For data visualization, use the categorical, tracks, and sequential scales in order — do not skip steps or substitute brand colors. Tracks and sequential are intentionally identical in Light and Dark mode; categorical uses a separate value per mode, so always resolve it through the token rather than copying a hex. ER Legacy reorders the categorical scale relative to EarthRanger but uses the same values.

### Dark mode

ER Legacy's dark mode is a **greyscale ladder, not EarthRanger's teal one**. Backgrounds step `Greyscale/1` `#111111` (secondary) up through `Greyscale/2` `#222222` (primary) to `Greyscale/3` `#333333` (elevated). Dividers are `Greyscale/5`, field outlines `Greyscale/3`. Primary text inverts to white, secondary text to `Greyscale/8` `#b1b3b3`, and icons, form labels and tabs to `Greyscale/7` `#888b8d`.

The CTA lightens from `Blue/1` to `Blue/3` (`#76b0ff`); the secondary blue moves from `Blue/2` to `Blue/5` (`#2a394d`). Status and priority colors shift to lighter, softer steps so they read on a dark surface without glowing: error to `Red/5`, warning and amber to `Amber/5`, success to `Green/4`, event-priority green to `Green/2`, patrol active to `Indigo/5`, and patrol overdue to `Magenta/4`.

Unlike EarthRanger, the categorical data scale is **mode-stable** — the legacy frame draws it once rather than once per mode, so the same values serve both.

Three tokens have no value in the legacy frame in either mode, and the values given are proposed rather than drawn: tertiary background, selected background, and reversed secondary text. Each is marked in the frontmatter.

## Typography

ER Legacy shares EarthRanger's typography exactly — the unified Strata text-style scale (Display, Heading XL/LG/MD/SM, Body LG/MD/SM/XS, and Mono) rather than separate per-platform scales. What changes per platform is only the **font-family**, via the `platform.body` and `platform.heading` tokens:

| Platform | Body | Heading |
| --- | --- | --- |
| Web Fonts | Roboto | PP Telegraf |
| Windows | Arial | Arial |
| iOS | SF Pro | SF Pro |
| Android | Roboto | Roboto |

**PP Telegraf font files and license:** the font files, along with the Ai2 font license README for PP Telegraf, are in this [Google Drive folder](https://drive.google.com/drive/folders/1GQnBozz9Gbsevr7vuj_BQ4WdiSY1hyzl?usp=drive_link). Read the license README before using or distributing the font.

Always reference a text-style token (e.g. `body-md`, `heading-lg`) rather than hardcoding font properties directly — the platform's font-family resolves automatically. `body-md` (16px / 25.6px line height) is the default reading size. All styles use 0 letter-spacing and no text-transform.

Two groups sit alongside the PP Telegraf Display/Heading scale: `heading-ui-lg` (32px) and `heading-ui-md` (24px) are Roboto Medium headings, and `button-sm` (18px) and `button-xs` (16px) are Roboto SemiBold styles for button labels. Unlike the other styles they don't set a line height.

### Fallback stack (performance)

EarthRanger is used in low-bandwidth field conditions where a delayed web font can mean delayed information in high-stakes moments (active patrols, incident response). Always pair the web font with a fast, native fallback — never a generic one. See Do's and Don'ts below for the full performance checklist.

### External communications (Manrope) — not for UI

Manrope is a typographic option for **externally-facing communications only**: slide decks, EarthRanger.com, email newsletters, and printed materials. It is **never** used in product UI — product interfaces always use Roboto for body text via the `platform.body` tokens above.

Scope is deliberately narrow: Manrope replaces Roboto for **body text only** (`external-comms-body-lg/md/sm/xs`, same sizes/line-heights as the UI Body scale). Headings in external communications still use PP Telegraf, exactly as in product UI — do not substitute Manrope for headings, with one exception: slide decks, which use Manrope for everything.

## Icons

> **Never substitute a different icon for the one shown in the design.** Always match exactly what is specified.

### Library 1: Material Design Icons

- **Source:** Material Design Icons Figma library (`x3D0XAL06JEEEi12suKcGs`)
- **Style:** Outlined (default); filled variants exist for some icons
- **Default size:** 24×24px
- **Usage:** Primary icon library — search for any standard UI icon here first
- **Color:** Use `UI/Icons` token (`#63666a` light / `#888b8d` dark) by default unless the design specifies otherwise

### Library 2: ER Design System Custom Icons

- **Source:** ER Design System Figma file (`gQJAI5XKeENQsqkCaFBev3`), Icons page
- **Style:** Custom filled icons specific to the EarthRanger domain
- **Default size:** 18×18px for most icons; 16×16px for menu bar and inline UI icons
- **Usage:** Use these for domain-specific concepts not covered by Material (e.g. Patrol, Spoor, Basemap, Fence, Wildlife Sighting, GPS, Report, Observation Patrol, Deforestation, etc.)
- **Variants:** Some icons have filled/outline or state variants (e.g. Cloud Online/Offline, Eye Open/Closed, Active/Inactive, Download states) — use the variant that matches the design exactly
- **Note:** The ER icon library references Material Design as its base — for any icon not listed as a custom symbol, search the Material Design library

### Library 3: ER Google Slides Template

- **Source:** [EarthRanger Slide Template](https://docs.google.com/presentation/d/1rm7CEqJaps473VlnG1n8CIznZONLk7yXBwCNGfKg0CE/edit?usp=sharing) — MAKE A COPY
- **Backup:** If you cannot access the URL above, reference the PDF export at `earthranger/assets/EarthRanger-Slide-Template.pdf` to recreate the template.
- **Usage:** Starting point for external-facing slide decks (see Typography's External Communications section — Manrope, not Roboto, for body text in this context)
- **Note:** Always duplicate the template rather than editing the source file directly. When asked to make a deck, copy the template, build from its layouts, and apply the rules below.
- **Fonts:** Manrope for everything in slide decks, headings included — decks are the exception to PP Telegraf headings
- **Layouts:** Add slides from the Layout menu so titles keep the same placement, font and size on every slide
- **Content:** About 3 bullets max per slide. Put detail in speaker notes, not on the slide

## Do's and Don'ts

**Don't place `UI/Text/Primary Text` (or the raw `Greyscale/0` primitive) on a solid `UI/CTA Primary` fill (Blue/1 in light mode).** It measures 3.16:1 — under the 4.5:1 WCAG AA minimum for normal text, only clearing the 3:1 floor for large text and UI outlines. Use `UI/Text/Primary Text Reversed` instead, which resolves to white and measures 6.65:1. In dark mode the rule flips: `Blue/3` is light enough that **dark** text is the correct pairing, at 9.42:1, while white on it falls to 2.23:1.

**Don't place white or `UI/Text/Primary Text Reversed` on `Brand/Accent Green` (Green/7).** ER Legacy's accent green is a bright mint, the inverse of EarthRanger's, so white on it measures 2.11:1 and fails outright. Use `UI/Text/Primary Text` there instead, which measures 9.94:1. This is the one place where ER Legacy's text-on-fill rule is the opposite of EarthRanger's — check the fill's lightness rather than carrying the habit across.

**Don't use the full by-Ai2 lockup below 56px of rendered logo height.** Use the `-short` variants (`logo-ai2-horizontal-short`, `logo-ai2-white-horizontal-short`), which scale the by-Ai2 mark up relative to the EarthRanger wordmark so the attribution stays legible. Above 56px, use the standard lockups.

**Don't mix ER Legacy and EarthRanger on the same screen.** They share token names on purpose, so nothing visibly breaks if a product loads both — one simply wins, quietly, and you get a screen that is neither palette. Pick one per product.

**Don't use emojis in EarthRanger interfaces — use an icon library instead.** See the Icons section above: Material Design Icons for standard UI icons, ER Design System Custom Icons for domain-specific concepts (Patrol, Spoor, Basemap, Fence, Wildlife Sighting, etc.). Emojis render inconsistently across platforms/fonts and don't carry the states (filled/outline, active/inactive, etc.) the icon libraries provide.

**Don't load web fonts without these performance safeguards.** EarthRanger is used in low-bandwidth field conditions where a delayed font can mean delayed information in high-stakes moments (active patrols, incident response).

- **Native OS fallback** if the web font hasn't loaded — Windows: Arial, Android: Roboto, iOS: SF Pro, macOS: SF Pro
- **Subset fonts** to strip unneeded characters, using `glyphhanger` or `fonttools`
- **Regular and Bold weights only** — don't ship the full weight range
- **`font-display: optional`** so a slow-loading web font never blocks rendering or shifts layout
- **Self-host fonts** — don't depend on a third-party CDN round trip
