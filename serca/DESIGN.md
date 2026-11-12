---
name: SERCA
description: SMART-EarthRanger Conservation Alliance (SERCA) identity — booth, event, partner, and Alliance-member materials
version: 0.0.1

assets:
  # The pixel-bear mark. Vertical is the primary lockup; horizontal is for
  # wide, short spaces. Teal, teal-green, and black are for light grounds;
  # white, cream-green (and the cream icon) are for dark grounds.
  logo: assets/SERCA_vertical-teal.svg
  logo-horizontal: assets/SERCA_horiz-teal.svg
  logo-teal-green: assets/SERCA_vertical-teal-green.svg
  logo-teal-green-horizontal: assets/SERCA_horiz-teal-green.svg
  logo-black: assets/SERCA_vertical-black.svg
  logo-black-horizontal: assets/SERCA_horiz-black.svg
  logo-white: assets/SERCA_vertical-white.svg
  logo-white-horizontal: assets/SERCA_horiz-white.svg
  logo-cream-green: assets/SERCA_vertical-cream-green.svg
  logo-cream-green-horizontal: assets/SERCA_horiz-cream-green.svg
  # Icon only (bear + pixel) — small sizes, favicons, avatars, watermarks.
  logo-icon: assets/SERCA_icon-teal.svg
  logo-icon-teal-green: assets/SERCA_icon-teal-green.svg
  logo-icon-black: assets/SERCA_icon-black.svg
  logo-icon-white: assets/SERCA_icon-white.svg
  logo-icon-cream: assets/SERCA_icon-cream.svg
  # Alliance member logos — secondary, never top billing (see Overview).
  # Their own brand colors; "-white" files are the members' reverse versions
  # for dark grounds. PNG where that is what the member supplied.
  member-ai2: assets/members/ai2.svg
  member-fzs: assets/members/fzs.png
  member-nc-zoo: assets/members/nc-zoo.svg
  member-nc-zoo-white: assets/members/nc-zoo-white.svg
  member-panthera: assets/members/panthera.png
  member-panthera-white: assets/members/panthera-white.png
  member-rewild: assets/members/rewild.png
  member-rewild-white: assets/members/rewild-white.png
  member-wcs: assets/members/wcs.png
  member-wps: assets/members/wps.png
  member-wps-white: assets/members/wps-white.png
  member-wwf: assets/members/wwf.png
  member-zsl: assets/members/zsl.png

colors:
  # ── Semantic UI Tokens ────────────────────────────────────────────
  # Use these first. Semantic tokens carry intent and adapt if the
  # design system is updated. Three-layer architecture: Primitives →
  # Tokens → Platform. Tokens below list both Light and Dark values —
  # dark mode inverts (not just darkens): backgrounds swap from warm
  # whites/off-whites to deep teal, text flips accordingly, and status
  # tokens shift to lighter/more-saturated primitive steps for contrast.

  # Background
  # Listed from the quietest surface to the most forward: the page sits on
  # Tertiary or Secondary, Elevated Component 0 is the banded sub-surface
  # inside a panel (a table header, a row label), and Elevated and Primary
  # are the panel itself. Dark mode runs one continuous teal ladder rather
  # than mixing in grey.
  "UI/Background/Tertiary Background": { light: "{colors.teal-t10}", dark: "{colors.teal-darkest}" }
  "UI/Background/Secondary Background": { light: "{colors.greyscale-off-white}", dark: "{colors.teal-darkest}" }
  "UI/Background/Elevated Component 0": { light: "{colors.greyscale-11}", dark: "{colors.teal-ai2-dark-teal}" }
  "UI/Background/Elevated Component": { light: "{colors.greyscale-white}", dark: "{colors.teal-ai2-extra-dark-teal}" }
  "UI/Background/Primary Background": { light: "{colors.greyscale-white}", dark: "{colors.teal-ai2-extra-dark-teal}" }
  "UI/Background/Selected Background": { light: "{colors.teal-3-05}", dark: "{colors.teal-t100}" }
  "UI/Background/Hover Background": { light: "{colors.teal-t10}", dark: "{colors.teal-t100}" }

  # Text
  "UI/Text/Primary Text": { light: "{colors.teal-ai2-dark-teal}", dark: "{colors.greyscale-white}" }
  "UI/Text/Primary Text Reversed": { light: "{colors.greyscale-white}", dark: "{colors.teal-ai2-extra-dark-teal}" }
  "UI/Text/Secondary Text": { light: "{colors.teal-t100}", dark: "{colors.teal-t20}" }
  "UI/Text/Secondary Text Reversed": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-white}" }
  "UI/Text/Form Labels": { light: "{colors.teal-t100}", dark: "{colors.greyscale-white}" }
  "UI/Text/Tabs": { light: "{colors.teal-t100}", dark: "{colors.greyscale-white}" }
  "UI/Text/Disabled": { light: "{colors.greyscale-6}", dark: "{colors.greyscale-7}" }

  # UI Chrome
  "UI/Icons": { light: "{colors.teal-t80}", dark: "{colors.teal-t60}" }
  "UI/Field Outline": { light: "{colors.teal-t30}", dark: "{colors.teal-dark-80}" }
  "UI/Divider Lines": { light: "{colors.teal-t20}", dark: "{colors.teal-dark-90}" }

  # Actions
  "UI/CTA Primary": { light: "{colors.green-12}", dark: "{colors.green-7}" }
  "UI/CTA Secondary": { light: "{colors.teal-t100}", dark: "{colors.teal-t90}" }
  "UI/CTA Text": { light: "{colors.greyscale-white}", dark: "{colors.greyscale-off-white}" }   # text and marks on a CTA Secondary fill

  # Status
  "UI/Status/Error-Destructive": { light: "{colors.red-3}", dark: "{colors.red-5}" }
  "UI/Status/Success": { light: "{colors.green-12}", dark: "{colors.green-4}" }
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

  # Brand
  "Brand/Acorn Logo": { light: "{colors.teal-3}", dark: "{colors.teal-3}" }
  "Brand/Accent Green": { light: "{colors.green-12}", dark: "{colors.green-7}" }
  "Brand/Background/Primary Background": { light: "{colors.greyscale-white}", dark: "{colors.teal-ai2-dark-teal}" }
  "Brand/Background/Secondary Background": { light: "{colors.greyscale-off-white}", dark: "{colors.teal-t100}" }
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
      web-fonts: PP Telegraf
      windows: Arial
      ios: SF Pro
      android: Roboto
    # Slide decks (Claude Design Slides, Google Slides): Manrope for
    # both body and headings. PP Telegraf is not available in Google
    # Slides, so it is never used in decks.
    slides:
      body: Manrope
      heading: Manrope

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
  # Manrope, body text only. Scope: slide decks, SERCA.org, email
  # newsletters, printed materials. Headings in these contexts still use
  # PP Telegraf (see Strata Text Styles above) — only body text changes.
  # EXCEPTION: slide decks use Manrope for headings too (platform.slides).
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

The SMART-EarthRanger Conservation Alliance (SERCA) is a global collaboration that unites SMART and EarthRanger — the world's most widely used conservation management platforms — with proven field experience and training resources into a single, free support system for the people safeguarding protected and conserved areas. The Alliance is governed by nine member organizations; no single organization leads it. SMART and EarthRanger remain the platforms practitioners use today.

This file is the **Alliance identity, not a product interface**. Use it for booth and event materials, partner decks and one-pagers, social profiles, and Alliance members' materials showing their affiliation. It is not a primary product mark — SMART and EarthRanger keep their own marks on their own product surfaces. The SERCA platform brings together SERCA Web, SERCA Mobile, Ecoscope, and Gundi — tools built around data-driven decision making and adaptive management.

SERCA's colors and typography are EarthRanger's, token for token: every color value, text style, size, and weight below is identical, so Alliance materials sit naturally beside EarthRanger materials. What SERCA adds is the mark and the rules for applying it.

SERCA materials reach practitioners, protected-area managers, Alliance member organizations, funders, and press. Speak of **practitioners** and **conservation teams**, never users or customers, and capitalize **Alliance** when it refers to SERCA. SERCA is a unified platform, not a suite; it is free; and while SMART and EarthRanger are available today, SERCA Web and Mobile follow a milestone-based roadmap rather than dates.

### The mark

The pixel bear: a bear silhouette looking up toward a single square pixel, with the wordmark "SERCA" set below it (vertical) or beside it (horizontal). The pixel is part of the mark — it is never dropped, moved, or resized independently.

The mark ships in single-color and two-color versions:

| Colorway | Files | Ground |
| --- | --- | --- |
| **Teal** — the default | `logo`, `logo-horizontal`, `logo-icon` | White and `Greyscale/Off-white` |
| **Teal-green** — teal bear and wordmark, green pixel | `logo-teal-green`, `logo-teal-green-horizontal`, `logo-icon-teal-green` | White and `Greyscale/Off-white` |
| **Black** — one-color reproduction | `logo-black`, `logo-black-horizontal`, `logo-icon-black` | Light grounds where color printing isn't available |
| **White** | `logo-white`, `logo-white-horizontal`, `logo-icon-white` | `Teal/Ai2 Dark Teal`, `Teal/Ai2 Extra Dark Teal`, and photography |
| **Cream-green** — cream bear and wordmark, green pixel | `logo-cream-green`, `logo-cream-green-horizontal` (icon: `logo-icon-cream`, single-color cream) | `Teal/Ai2 Dark Teal`, `Teal/Ai2 Extra Dark Teal` |

| Lockup | Use it for |
| --- | --- |
| **Vertical** — `logo` and its colorways | The primary lockup. Booth banners, slide title pages, one-pager headers, and anywhere with room for a roughly square block (about 1.1:1). |
| **Horizontal** — `logo-horizontal` and its colorways | Wide, short spaces (about 2.6:1): web headers and footers, email signatures, table-top banners, lanyard strips. |
| **Icon** — `logo-icon` and its colorways | Below about 120px wide, favicons, app-badge sizes, social avatars, watermarks, and anywhere the wordmark would not be legible. |

The artwork's colors are fixed inside the files and are **not UI tokens**: teal `#005458`, green `#00f2a6`, cream `#fcf2e8`, and black `#231f20`. They sit close to `Teal/T100` (`#105257`) and `Greyscale/Off-white` (`#faf2e9`) but are not the same values. Never sample them for UI, type, or backgrounds; use the EarthRanger tokens below. Give the mark clear space on every side of at least the width of the pixel, and keep the ground behind it solid or quiet.

There is no pixel-bear "A part of" lockup yet. Until one exists, Alliance members showing affiliation use the standard mark, following the member rules below.

### Alliance members

Nine organizations govern SERCA equally: Ai2, Frankfurt Zoological Society (FZS), North Carolina Zoo, Panthera, Re:wild, Wildlife Conservation Society (WCS), Wildlife Protection Solutions (WPS), WWF, and Zoological Society of London (ZSL). Their logos ship under `assets/members/` as the `member-*` assets above.

Member logos never get top billing. The SERCA mark leads every Alliance piece, and member marks appear only when a member needs highlighting — a workshop or training a member hosts, a use case or field story from a member's landscape, a co-presented session, or a governance slide that lists the Alliance.

- **All nine, or only the ones involved.** When showing governance, show all nine at equal optical size in one row or a 3×3 grid, in the order above, under an "Alliance members" or "Governed by" label in `body-sm`. When highlighting one member, show only that member — don't imply the others are absent.
- **Smaller than SERCA, and separated.** A member mark is never larger than the SERCA mark on the same surface. Cap it at the height of the SERCA bear, and separate the two with a hairline divider (`UI/Divider Lines`) or clear space of at least the width of the pixel.
- **Their colors, not ours.** Reproduce member logos in their own brand colors on light grounds and use their supplied white versions on dark grounds. Never recolor a member mark, and never apply SERCA teal to it. Ai2's mark is pink — that is a member mark reproduced faithfully, not a SERCA color; the no-pink rule covers SERCA's own design.
- **Use what was supplied.** FZS, WCS, WWF, and ZSL exist in one version only (WWF's file carries its own white ground) — on a dark ground, put them on a white or `Greyscale/Off-white` panel rather than inventing a reverse. `member-nc-zoo` is a one-color `Teal/Ai2 Dark Teal` rendering, matching the Alliance kit's teal treatment, because no full-color vector was supplied; swap in the member's own artwork when it is available. PNG members should be placed at or below their pixel size.

SERCA's visual identity is grounded in Ai2's brand standards, using the same three-layer token architecture as Strata (Primitives → Tokens → Platform). The primary CTA color is green; teal is the brand/secondary accent and appears in navigation, headers, and brand moments. Pink is never used in SERCA materials. Dark mode is a first-class, fully-defined mode (not just light-mode tokens dimmed) — it inverts rather than darkens: backgrounds swap from white/off-white to deep teal, text flips accordingly, and status colors shift to lighter/more-saturated steps for contrast on the dark surface. Track and sequential data colors are mode-stable — the same primitives work on both light and dark backgrounds. Categorical data colors have separate light and dark values.

## Colors

Always use **semantic tokens** (e.g. `UI/Text/Primary Text`) instead of raw primitive values wherever possible. Semantic tokens carry intent, provide both a Light and Dark value, and will automatically adapt if the design system is updated.

The primary interactive color is `UI/CTA Primary` (`#0f865d` light / `#0fcb8c` dark, Green/12 and Green/7) — used for calls to action, links, and active states. Status colors are strictly functional: use them only to communicate meaning (error, success, warning, running/informational), never decoratively. Blue (`UI/Status/Running`) covers in-progress state and general informational messaging — notices, tips, and neutral callouts — but it is not an interactive color: use `UI/CTA Primary` for buttons, links, and active states.

Teal (`Teal/T100`, `#105257` light / `#faf2e9` off-white text on `Teal/T100` dark surfaces) is the primary brand accent and appears in navigation, headers, form labels/tabs, and `UI/CTA Secondary`. `Brand/Accent Green` (`#0f865d` light / `#0fcb8c` dark) shares its values with `UI/CTA Primary` — they're the same brand-accent green.

Use `UI/Text/Primary Text Reversed` (`#ffffff` light / `#0a3235` dark — the inverse of `UI/Text/Primary Text`) for text or icon marks that sit directly on a brand-teal surface, such as a filled default-intent button or a checked control's mark. Teal is a mid-tone in light mode but becomes a pale tint in dark mode, so a fixed light color reads fine in light mode but disappears in dark mode — this token flips with the mode so it always contrasts against the surface it's on.

Pink is not part of the SERCA palette. Do not introduce any pink values, even from the broader Ai2 primitive palette.

For data visualization, use the categorical, tracks, and sequential scales in order — do not skip steps or substitute brand colors. These scales are designed for perceptual distinctiveness and accessibility across the full range of values. Tracks and sequential are intentionally identical in Light and Dark mode; categorical uses a separate value per mode, so always resolve it through the token rather than copying a hex.

## Typography

SERCA shares Strata's unified text-style scale — Display, Heading (XL/LG/MD/SM), Body (LG/MD/SM/XS), and Mono — rather than maintaining separate per-platform scales. What changes per platform is only the **font-family**, via the `platform.body` and `platform.heading` tokens:

| Platform | Body | Heading |
| --- | --- | --- |
| Web Fonts | Roboto | PP Telegraf |
| Windows | Arial | Arial |
| iOS | SF Pro | SF Pro |
| Android | Roboto | Roboto |

Always reference a text-style token (e.g. `body-md`, `heading-lg`) rather than hardcoding font properties directly — the platform's font-family resolves automatically. `body-md` (16px / 25.6px line height) is the default reading size. All styles use 0 letter-spacing and no text-transform.

Two groups sit alongside the PP Telegraf Display/Heading scale: `heading-ui-lg` (32px) and `heading-ui-md` (24px) are Roboto Medium headings, and `button-sm` (18px) and `button-xs` (16px) are Roboto SemiBold styles for button labels. Unlike the other styles they don't set a line height.

### Fallback stack (performance)

SERCA materials are viewed in the same low-bandwidth field conditions as EarthRanger, where a delayed web font can mean delayed information in high-stakes moments (active patrols, incident response). Always pair the web font with a fast, native fallback — never a generic one. See Do's and Don'ts below for the full performance checklist.

### External communications (Manrope) — not for UI

Manrope is a typographic option for **externally-facing communications only**: slide decks, SERCA.org, email newsletters, and printed materials. Most SERCA materials are external communications, so Manrope body text is the common case here. It is **never** used in product UI — product interfaces always use Roboto for body text via the `platform.body` tokens above.

Scope is deliberately narrow: Manrope replaces Roboto for **body text only** (`external-comms-body-lg/md/sm/xs`, same sizes/line-heights as the UI Body scale). Headings in external communications still use PP Telegraf, exactly as in product UI — with one exception: slide decks.

### Slide decks (Manrope for everything)

**Manrope is the default and only font for SERCA slide decks** — body *and* headings (use Manrope Bold for Display and Heading styles, Manrope Regular for body). PP Telegraf is not available in Google Slides, so decks that specify it force a font substitution on export. Claude Design Slides and any deck built from the SERCA Google Slides template should set Manrope everywhere and never reference PP Telegraf or Roboto. This exception applies to slide decks only; SERCA.org, email, and print keep PP Telegraf headings, and product UI keeps Roboto / PP Telegraf.

## Icons

> **Never substitute a different icon for the one shown in the design.** Always match exactly what is specified.

### Library 1: Material Design Icons

- **Source:** Material Design Icons Figma library (`x3D0XAL06JEEEi12suKcGs`)
- **Style:** Outlined (default); filled variants exist for some icons
- **Default size:** 24×24px
- **Usage:** Primary icon library — search for any standard UI icon here first
- **Color:** Use `UI/Icons` token (`#407579` light / `#70979a` dark) by default unless the design specifies otherwise

### Library 2: SERCA Design Figma File

- **Source:** SERCA Design Figma file (`gQJAI5XKeENQsqkCaFBev3`), Icons page
- **Style:** SERCA icons — custom filled icons specific to the SERCA domain
- **Default size:** 18×18px for most icons; 16×16px for menu bar and inline UI icons
- **Usage:** Use these for domain-specific concepts not covered by Material (e.g. Patrol, Spoor, Basemap, Fence, Wildlife Sighting, GPS, Report, Observation Patrol, Deforestation, etc.)
- **Variants:** Some icons have filled/outline or state variants (e.g. Cloud Online/Offline, Eye Open/Closed, Active/Inactive, Download states) — use the variant that matches the design exactly
- **Note:** The SERCA icon library references Material Design as its base — for any icon not listed as a custom symbol, search the Material Design library

### Library 3: SERCA Google Slides Template

- **Source:** 2026 SERCA Slide Template (Google Slides, maintained by SERCA Communications) — MAKE A COPY
- **Usage:** Starting point for external-facing SERCA slide decks (see Typography's Slide decks section — Manrope for both body and headings in this context)
- **Note:** Always duplicate the template rather than editing the source file directly

## Do's and Don'ts

**Don't place `UI/Text/Primary Text` (or the raw dark-teal/`extra-dark-teal` primitives) on a solid `UI/CTA Primary` or `Brand/Accent Green` fill (Green/12 in light mode).** It measures ~3:1 contrast — under the 4.5:1 WCAG AA minimum for normal text, only clearing the 3:1 floor for large text/UI outlines. Use `UI/Text/Primary Text Reversed` instead, which resolves to white in light mode. In dark mode this isn't an issue — Green/7 is bright enough that dark text reads fine there.

**Don't recolor, outline, or add effects to the mark.** Use only the supplied colorways (teal, teal-green, black, white, cream-green, cream). No gradients, drop shadows, or strokes; don't swap in `UI/CTA Primary` or any other token for the artwork's own colors; and the green pixel appears only in the two-color files, never on a single-color bear you've recolored yourself.

**Don't separate the bear from the pixel, drop or move the pixel, or rearrange the lockup.** The icon files are the only approved partial mark, and the wordmark never appears without the bear.

**Don't give an Alliance member logo top billing or set it larger than the SERCA mark.** Member marks appear only where a member is being highlighted (a workshop they host, a use case from their landscape, a governance list), always after and smaller than the SERCA mark, in their own brand colors.

**Don't place the teal, teal-green, or black mark on `Teal/Ai2 Dark Teal`, `Teal/Ai2 Extra Dark Teal`, or busy photography.** Switch to the white or cream-green artwork, or put the mark on a solid white / `Greyscale/Off-white` panel.

**Don't write "suite of tools", "users", or "available now" in SERCA materials.** SERCA is a unified platform; the people it serves are practitioners and conservation teams; SMART and EarthRanger are available today, while SERCA Web and Mobile follow a milestone-based roadmap.

**Don't use emojis in SERCA materials — use an icon library instead.** See the Icons section above: Material Design Icons for standard UI icons, SERCA icons for domain-specific concepts (Patrol, Spoor, Basemap, Fence, Wildlife Sighting, etc.). Emojis render inconsistently across platforms/fonts and don't carry the states (filled/outline, active/inactive, etc.) the icon libraries provide.

**Don't load web fonts without these performance safeguards.** SERCA materials are viewed in low-bandwidth field conditions where a delayed font can mean delayed information in high-stakes moments (active patrols, incident response).

- **Native OS fallback** if the web font hasn't loaded — Windows: Arial, Android: Roboto, iOS: SF Pro, macOS: SF Pro
- **Subset fonts** to strip unneeded characters, using `glyphhanger` or `fonttools`
- **Regular and Bold weights only** — don't ship the full weight range
- **`font-display: optional`** so a slow-loading web font never blocks rendering or shifts layout
- **Self-host fonts** — don't depend on a third-party CDN round trip
