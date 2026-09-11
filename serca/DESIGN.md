---
name: SERCA
description: SMART-EarthRanger Conservation Alliance (SERCA) identity — booth, event, partner, and Alliance-member materials
version: 0.0.1

assets:
  # Stacked is the primary lockup; horizontal is for wide, short spaces.
  logo: assets/SERCA-logo.svg
  logo-horizontal: assets/SERCA-logo-H.svg
  logo-white: assets/SERCA-logo-white.svg
  logo-white-horizontal: assets/SERCA-logo-white-H.svg
  # Icons only (cat | shield) — small sizes, favicons, watermarks.
  logo-icon: assets/SERCA-logo-icon.svg
  logo-icon-white: assets/SERCA-logo-icon-white.svg
  # "A part of" lockup — for Alliance members showing their affiliation.
  logo-part-of: assets/SERCA-logo-part-of.svg
  logo-part-of-horizontal: assets/SERCA-logo-part-of-H.svg
  logo-part-of-white: assets/SERCA-logo-part-of-white.svg
  logo-part-of-white-horizontal: assets/SERCA-logo-part-of-white-H.svg
  # 1:1 social avatar — icons on Greyscale/Off-white.
  logo-social-profile: assets/SERCA-social-profile.svg
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
  # Dark-mode surfaces form one continuous teal ladder — Primary (darkest)
  # → Elevated → Secondary (lightest) — rather than mixing in grey.
  "UI/Background/Primary Background": { light: "#ffffff", dark: "#032629" }
  "UI/Background/Secondary Background": { light: "#faf2e9", dark: "#0a3235" }
  "UI/Background/Tertiary Background": { light: "#e7eeee", dark: "#0a3235" }
  "UI/Background/Elevated Component": { light: "#ffffff", dark: "#032629" }

  # Text
  "UI/Text/Primary Text": { light: "#0a3235", dark: "#ffffff" }
  "UI/Text/Primary Text Reversed": { light: "#ffffff", dark: "#0a3235" }
  "UI/Text/Secondary Text": { light: "#105257", dark: "#faf2e9" }
  "UI/Text/Secondary Text Reversed": { light: "#faf2e9", dark: "#105257" }
  "UI/Text/Form Labels": { light: "#105257", dark: "#ffffff" }
  "UI/Text/Tabs": { light: "#105257", dark: "#ffffff" }
  "UI/Text/Disabled": { light: "#767676", dark: "#888b8d" }

  # UI Chrome
  "UI/Icons": { light: "#767676", dark: "#888b8d" }
  "UI/Field Outline": { light: "#b1b3b3", dark: "#333333" }
  "UI/Divider Lines": { light: "#dddddd", dark: "#63666a" }

  # Actions
  "UI/CTA Primary": { light: "#0f865d", dark: "#0fcb8c" }
  "UI/CTA Secondary Blue": { light: "#cfdcdd", dark: "#27545f" }

  # Status
  "UI/Status/Error-Destructive": { light: "#d0031b", dark: "#f06374" }
  "UI/Status/Success": { light: "#0f865d", dark: "#53aa71" }
  "UI/Status/Running": { light: "#0056c7", dark: "#76b0ff" }
  "UI/Status/Warning": { light: "#e76826", dark: "#fd9964" }
  "UI/Status/Disabled": { light: "#767676", dark: "#888b8d" }
  "UI/Status/Ready": { light: "#ffb700", dark: "#ffb700" }

  # Status Backgrounds
  "UI/Status Bg/Synced Bg": { light: "#f5f7f3", dark: "#53693a" }
  "UI/Status Bg/Pending Sync Bg": { light: "#f3f3f3", dark: "#63666a" }
  "UI/Status Bg/Error Bg": { light: "#fdf2f4", dark: "#3e2125" }
  "UI/Status Bg/Draft Bg": { light: "#dde8f8", dark: "#2a394d" }
  "UI/Status Bg/Active Bg": { light: "#f5f5fa", dark: "#57528c" }
  "UI/Status Bg/Warning Bg": { light: "#fef7f4", dark: "#362922" }

  # Event Priority
  "UI/Event Priority/Green": { light: "#006842", dark: "#83af52" }
  "UI/Event Priority/Red": { light: "#d0031b", dark: "#f06374" }
  "UI/Event Priority/Amber": { light: "#e76826", dark: "#fd9964" }
  "UI/Event Priority/Grey": { light: "#888b8d", dark: "#888b8d" }

  # Patrol Status
  "UI/Patrol Status/Active": { light: "#3e35a3", dark: "#867ede" }
  "UI/Patrol Status/Overdue": { light: "#b62879", dark: "#e76eb3" }
  "UI/Patrol Status/Scheduled": { light: "#107283", dark: "#62bfd0" }
  "UI/Patrol Status/Track Line (Mobile)": { light: "#e76826", dark: "#e76826" }
  "UI/Patrol Status/Done (Mobile)": { light: "#767676", dark: "#888b8d" }

  # Data Visualization — Categorical
  "UI/Data/Categorical/Category 1": "#3e35a3"
  "UI/Data/Categorical/Category 2": "#488a00"
  "UI/Data/Categorical/Category 3": "#00958f"
  "UI/Data/Categorical/Category 4": "#b62879"
  "UI/Data/Categorical/Category 5": "#c6880c"
  "UI/Data/Categorical/Category 6": "#00d0c8"
  "UI/Data/Categorical/Category 7": "#78d811"
  "UI/Data/Categorical/Category 8": "#5c4fe7"
  "UI/Data/Categorical/Category 9": "#f4db20"
  "UI/Data/Categorical/Category 10": "#ed3ea2"

  # Data Visualization — Tracks
  "UI/Data/Tracks/Track 1": "#3e35a3"
  "UI/Data/Tracks/Track 2": "#b62879"
  "UI/Data/Tracks/Track 3": "#ff803e"
  "UI/Data/Tracks/Track 4": "#ed3ea2"
  "UI/Data/Tracks/Track 5": "#3089ff"
  "UI/Data/Tracks/Track 6": "#8c1700"
  "UI/Data/Tracks/Track 7": "#a100cb"
  "UI/Data/Tracks/Track 8": "#004e26"
  "UI/Data/Tracks/Track 9": "#002960"
  "UI/Data/Tracks/Track 10": "#f23b0e"

  # Data Visualization — Sequential
  "UI/Data/Sequential/Sequential 1": "#f4db20"
  "UI/Data/Sequential/Sequential 2": "#ffb700"
  "UI/Data/Sequential/Sequential 3": "#ed3ea2"
  "UI/Data/Sequential/Sequential 4": "#a100cb"
  "UI/Data/Sequential/Sequential 5": "#5c4fe7"
  "UI/Data/Sequential/Sequential 6": "#0056c7"
  "UI/Data/Sequential/Sequential 7": "#00882e"
  "UI/Data/Sequential/Sequential 8": "#78d811"

  # Brand
  "Brand/Acorn Logo": { light: "#008586", dark: "#008586" }
  "Brand/Accent Green": { light: "#0f865d", dark: "#0fcb8c" }

  # ── Primitive Palette ─────────────────────────────────────────────
  # Use only when no semantic token fits. Single mode (HEX) — not used
  # directly in designs; referenced by tokens above.

  # Greyscale (0 = black, 11 = near-white; Off-white is warm/cream)
  "Greyscale/0": "#000000"
  "Greyscale/1": "#111111"
  "Greyscale/2": "#222222"
  "Greyscale/3": "#333333"
  "Greyscale/4": "#444444"
  "Greyscale/5": "#63666a"
  "Greyscale/6": "#767676"
  "Greyscale/7": "#888b8d"
  "Greyscale/8": "#b1b3b3"
  "Greyscale/9": "#dddddd"
  "Greyscale/10": "#f3f3f3"
  "Greyscale/11": "#f9f9f9"
  "Greyscale/Off-white": "#faf2e9"
  "Greyscale/White": "#ffffff"

  # Blue
  "Blue/1": "#0056c7"
  "Blue/2": "#dde8f8"
  "Blue/3": "#76b0ff"
  "Blue/4": "#f4f7fd"
  "Blue/5": "#2a394d"
  "Blue/6": "#002960"
  "Blue/7": "#3089ff"

  # Indigo
  "Indigo/1": "#331878"
  "Indigo/2": "#3e35a3"
  "Indigo/3": "#5c4fe7"
  "Indigo/4": "#57528c"
  "Indigo/5": "#867ede"
  "Indigo/6": "#f5f5fa"

  # Green
  "Green/1": "#006842"
  "Green/2": "#83af52"
  "Green/3": "#00882e"
  "Green/4": "#53aa71"
  "Green/5": "#004e26"
  "Green/6": "#f5f7f3"
  "Green/7": "#0fcb8c"
  "Green/8": "#53693a"
  "Green/9": "#488a00"
  "Green/10": "#78d811"
  "Green/11": "#a1e458"
  "Green/12": "#0f865d"

  # Teal
  "Teal/1": "#107283"
  "Teal/2": "#62bfd0"
  "Teal/3": "#008586"
  "Teal/4": "#00958f"
  "Teal/5": "#00d0c8"
  "Teal/Ai2 Dark Teal": "#0a3235"
  "Teal/Ai2 Extra Dark Teal": "#032629"
  "Teal/T100": "#105257"
  "Teal/T90": "#27545f"
  "Teal/T80": "#407579"
  "Teal/T70": "#588689"
  "Teal/T60": "#70979a"
  "Teal/T50": "#87a8ab"
  "Teal/T40": "#9fbabc"
  "Teal/T30": "#b7cbcd"
  "Teal/T20": "#cfdcdd"
  "Teal/T10": "#e7eeee"

  # Red
  "Red/1": "#3e2125"
  "Red/2": "#8c1700"
  "Red/3": "#d0031b"
  "Red/4": "#f23b0e"
  "Red/5": "#f06374"
  "Red/6": "#fdf2f4"

  # Amber
  "Amber/1": "#362922"
  "Amber/2": "#b83f00"
  "Amber/3": "#e76826"
  "Amber/4": "#ff803e"
  "Amber/5": "#fd9964"
  "Amber/6": "#fef7f4"

  # Yellow
  "Yellow/1": "#9d6900"
  "Yellow/2": "#c6880c"
  "Yellow/3": "#ffb700"
  "Yellow/4": "#f4db20"

  # Magenta
  "Magenta/1": "#8b0f56"
  "Magenta/2": "#b62879"
  "Magenta/3": "#ed3ea2"
  "Magenta/4": "#e76eb3"

  # Purple
  "Purple/1": "#71038e"
  "Purple/2": "#a100cb"
  "Purple/3": "#cc74e6"

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

The SMART-EarthRanger Conservation Alliance (SERCA) is a global collaboration that unites SMART and EarthRanger — the world's most widely used conservation management platforms — with proven field experience and training resources into a single, free support system for the people safeguarding protected and conserved areas. The Alliance is governed by nine member organizations; no single organization leads it. SMART and EarthRanger remain the platforms practitioners use today.

This file is the **Alliance identity, not a product interface**. Use it for booth and event materials, partner decks and one-pagers, social profiles, and the "A part of" lockup an Alliance member uses to show its affiliation. It is not a primary product mark — SMART and EarthRanger keep their own marks on their own product surfaces.

SERCA's colors and typography are EarthRanger's, token for token: every color value, text style, size, and weight below is identical, so Alliance materials sit naturally beside EarthRanger materials. What SERCA adds is the mark and the rules for applying it.

SERCA materials reach practitioners, protected-area managers, Alliance member organizations, funders, and press. Speak of **practitioners** and **conservation teams**, never users or customers, and capitalize **Alliance** when it refers to SERCA. SERCA is a unified platform, not a suite; it is free; and while SMART and EarthRanger are available today, SERCA Web and Mobile follow a milestone-based roadmap rather than dates.

### The mark

Two silhouettes separated by a hairline divider — a walking big cat on the left and the striped shield on the right, one from each founding platform's lineage — with the wordmark set as "SMART-EarthRanger" over "Conservation Alliance". The whole mark is a single color: `Teal/Ai2 Dark Teal` (`#0a3235`) on light grounds, white on dark grounds. There is no multi-color version.

| Variant | Use it for |
| --- | --- |
| **Stacked** — `logo`, `logo-white` | The primary lockup. Booth banners, slide title pages, one-pager headers — anywhere with room for a roughly 2.2:1 block. |
| **Horizontal** — `logo-horizontal`, `logo-white-horizontal` | Wide, short spaces: web headers and footers, email signatures, table-top banners, lanyard strips. |
| **Icons only** — `logo-icon`, `logo-icon-white` | Below about 120px wide, favicons, app-badge sizes, watermarks, and wherever the wordmark would not be legible. |
| **"A part of"** — `logo-part-of`, `logo-part-of-horizontal` and white versions | Alliance members and partners showing affiliation on their own materials. Never SERCA's own primary mark. |
| **Social profile** — `logo-social-profile` | 1:1 avatars. The icons on `Greyscale/Off-white` (`#faf2e9`) — the only variant that ships with its own ground. |

Use the teal artwork on white and off-white grounds and the white artwork on `Teal/Ai2 Dark Teal`, `Teal/Ai2 Extra Dark Teal`, and photography. Give the mark clear space on every side of at least the shield's width, and keep the ground behind it solid or quiet. The "A part of" byline in the teal lockups is set in `#055256` inside the artwork itself — that value is not a UI token and is not reused anywhere else.

### Alliance members

Nine organizations govern SERCA equally: Ai2, Frankfurt Zoological Society (FZS), North Carolina Zoo, Panthera, Re:wild, Wildlife Conservation Society (WCS), Wildlife Protection Solutions (WPS), WWF, and Zoological Society of London (ZSL). Their logos ship under `assets/members/` as the `member-*` assets above.

Member logos never get top billing. The SERCA mark leads every Alliance piece, and member marks appear only when a member needs highlighting — a workshop or training a member hosts, a use case or field story from a member's landscape, a co-presented session, or a governance slide that lists the Alliance.

- **All nine, or only the ones involved.** When showing governance, show all nine at equal optical size in one row or a 3×3 grid, in the order above, under an "Alliance members" or "Governed by" label in `body-sm`. When highlighting one member, show only that member — don't imply the others are absent.
- **Smaller than SERCA, and separated.** A member mark is never larger than the SERCA mark on the same surface. Cap it at the height of the SERCA icons (cat and shield), and separate the two with a hairline divider (`UI/Divider Lines`) or clear space of at least the shield's width.
- **Their colors, not ours.** Reproduce member logos in their own brand colors on light grounds and use their supplied white versions on dark grounds. Never recolor a member mark, and never apply SERCA teal to it. Ai2's mark is pink — that is a member mark reproduced faithfully, not a SERCA color; the no-pink rule covers SERCA's own design.
- **Use what was supplied.** FZS, WCS, WWF, and ZSL exist in one version only (WWF's file carries its own white ground) — on a dark ground, put them on a white or `Greyscale/Off-white` panel rather than inventing a reverse. `member-nc-zoo` is a one-color `Teal/Ai2 Dark Teal` rendering, matching the Alliance kit's teal treatment, because no full-color vector was supplied; swap in the member's own artwork when it is available. PNG members should be placed at or below their pixel size.

SERCA's visual identity is grounded in Ai2's brand standards, using the same three-layer token architecture as Strata (Primitives → Tokens → Platform). The primary CTA color is green; teal is the brand/secondary accent and appears in navigation, headers, and brand moments. Pink is never used in SERCA materials. Dark mode is a first-class, fully-defined mode (not just light-mode tokens dimmed) — it inverts rather than darkens: backgrounds swap from white/off-white to deep teal, text flips accordingly, and status colors shift to lighter/more-saturated steps for contrast on the dark surface. Data colors (categorical, tracks, sequential) are mode-stable — the same primitives work on both light and dark backgrounds.

## Colors

Always use **semantic tokens** (e.g. `UI/Text/Primary Text`) instead of raw primitive values wherever possible. Semantic tokens carry intent, provide both a Light and Dark value, and will automatically adapt if the design system is updated.

The primary interactive color is `UI/CTA Primary` (`#0f865d` light / `#0fcb8c` dark, Green/12 and Green/7) — used for calls to action, links, and active states. Status colors are strictly functional: use them only to communicate system state (error, success, warning, running), never decoratively. Blue is reserved for the `Running` status only — it is not a general-purpose interactive color.

Teal (`Teal/T100`, `#105257` light / `#faf2e9` off-white text on `Teal/T100` dark surfaces) is the primary brand accent and appears in navigation, headers, form labels/tabs, and `UI/CTA Secondary Blue`. `Brand/Accent Green` (`#0f865d` light / `#0fcb8c` dark) shares its values with `UI/CTA Primary` — they're the same brand-accent green.

Use `UI/Text/Primary Text Reversed` (`#ffffff` light / `#0a3235` dark — the inverse of `UI/Text/Primary Text`) for text or icon marks that sit directly on a brand-teal surface, such as a filled default-intent button or a checked control's mark. Teal is a mid-tone in light mode but becomes a pale tint in dark mode, so a fixed light color reads fine in light mode but disappears in dark mode — this token flips with the mode so it always contrasts against the surface it's on.

Pink is not part of the SERCA palette. Do not introduce any pink values, even from the broader Ai2 primitive palette.

For data visualization, use the categorical, tracks, and sequential scales in order — do not skip steps or substitute brand colors. These scales are designed for perceptual distinctiveness and accessibility across the full range of values, and are intentionally identical in Light and Dark mode.

## Typography

SERCA shares Strata's unified text-style scale — Display, Heading (XL/LG/MD/SM), Body (LG/MD/SM/XS), and Mono — rather than maintaining separate per-platform scales. What changes per platform is only the **font-family**, via the `platform.body` and `platform.heading` tokens:

| Platform | Body | Heading |
| --- | --- | --- |
| Web Fonts | Roboto | PP Telegraf |
| Windows | Arial | Arial |
| iOS | SF Pro | SF Pro |
| Android | Roboto | Roboto |

Always reference a text-style token (e.g. `body-md`, `heading-lg`) rather than hardcoding font properties directly — the platform's font-family resolves automatically. `body-md` (16px / 25.6px line height) is the default reading size. All styles use 0 letter-spacing and no text-transform.

### Fallback stack (performance)

SERCA materials are viewed in the same low-bandwidth field conditions as EarthRanger, where a delayed web font can mean delayed information in high-stakes moments (active patrols, incident response). Always pair the web font with a fast, native fallback — never a generic one. See Do's and Don'ts below for the full performance checklist.

### External communications (Manrope) — not for UI

Manrope is a typographic option for **externally-facing communications only**: slide decks, serca.org, email newsletters, and printed materials. Most SERCA materials are external communications, so Manrope body text is the common case here. It is **never** used in product UI — product interfaces always use Roboto for body text via the `platform.body` tokens above.

Scope is deliberately narrow: Manrope replaces Roboto for **body text only** (`external-comms-body-lg/md/sm/xs`, same sizes/line-heights as the UI Body scale). Headings in external communications still use PP Telegraf, exactly as in product UI — do not substitute Manrope for headings anywhere.

## Icons

> **Never substitute a different icon for the one shown in the design.** Always match exactly what is specified.

### Library 1: Material Design Icons

- **Source:** Material Design Icons Figma library (`x3D0XAL06JEEEi12suKcGs`)
- **Style:** Outlined (default); filled variants exist for some icons
- **Default size:** 24×24px
- **Usage:** Primary icon library — search for any standard UI icon here first
- **Color:** Use `UI/Icons` token (`#767676`) by default unless the design specifies otherwise

### Library 2: ER Design System Custom Icons

- **Source:** ER Design System Figma file (`gQJAI5XKeENQsqkCaFBev3`), Icons page
- **Style:** Custom filled icons specific to the EarthRanger domain
- **Default size:** 18×18px for most icons; 16×16px for menu bar and inline UI icons
- **Usage:** Use these for domain-specific concepts not covered by Material (e.g. Patrol, Spoor, Basemap, Fence, Wildlife Sighting, GPS, Report, Observation Patrol, Deforestation, etc.)
- **Variants:** Some icons have filled/outline or state variants (e.g. Cloud Online/Offline, Eye Open/Closed, Active/Inactive, Download states) — use the variant that matches the design exactly
- **Note:** The ER icon library references Material Design as its base — for any icon not listed as a custom symbol, search the Material Design library

### Library 3: SERCA Google Slides Template

- **Source:** 2026 SERCA Slide Template (Google Slides, maintained by SERCA Communications) — MAKE A COPY
- **Usage:** Starting point for external-facing SERCA slide decks (see Typography's External Communications section — Manrope, not Roboto, for body text in this context)
- **Note:** Always duplicate the template rather than editing the source file directly

## Do's and Don'ts

**Don't place `UI/Text/Primary Text` (or the raw dark-teal/`extra-dark-teal` primitives) on a solid `UI/CTA Primary` or `Brand/Accent Green` fill (Green/12 in light mode).** It measures ~3:1 contrast — under the 4.5:1 WCAG AA minimum for normal text, only clearing the 3:1 floor for large text/UI outlines. Use `UI/Text/Primary Text Reversed` instead, which resolves to white in light mode. In dark mode this isn't an issue — Green/7 is bright enough that dark text reads fine there.

**Don't recolor, outline, or add effects to the mark.** Teal artwork (`Teal/Ai2 Dark Teal`) on light grounds, white artwork on dark grounds — nothing else. No gradients, drop shadows, strokes, or a green (`UI/CTA Primary`) mark.

**Don't separate the cat from the shield, drop the divider, or rearrange the lockup.** The icons-only files are the only approved partial mark, and the wordmark never appears without the icons.

**Don't give an Alliance member logo top billing or set it larger than the SERCA mark.** Member marks appear only where a member is being highlighted (a workshop they host, a use case from their landscape, a governance list), always after and smaller than the SERCA mark, in their own brand colors.

**Don't use the "A part of" lockup as SERCA's own mark.** It exists for Alliance members and partners to show affiliation. SERCA's own materials use `logo` or `logo-horizontal`.

**Don't place the teal mark on `Teal/Ai2 Dark Teal`, `Teal/Ai2 Extra Dark Teal`, or busy photography.** Switch to the white artwork, or put the mark on a solid white / `Greyscale/Off-white` panel.

**Don't write "suite of tools", "users", or "available now" in SERCA materials.** SERCA is a unified platform; the people it serves are practitioners and conservation teams; SMART and EarthRanger are available today, while SERCA Web and Mobile follow a milestone-based roadmap.

**Don't use emojis in SERCA materials — use an icon library instead.** See the Icons section above: Material Design Icons for standard UI icons, ER Design System Custom Icons for domain-specific concepts (Patrol, Spoor, Basemap, Fence, Wildlife Sighting, etc.). Emojis render inconsistently across platforms/fonts and don't carry the states (filled/outline, active/inactive, etc.) the icon libraries provide.

**Don't load web fonts without these performance safeguards.** SERCA materials are viewed in low-bandwidth field conditions where a delayed font can mean delayed information in high-stakes moments (active patrols, incident response).

- **Native OS fallback** if the web font hasn't loaded — Windows: Arial, Android: Roboto, iOS: SF Pro, macOS: SF Pro
- **Subset fonts** to strip unneeded characters, using `glyphhanger` or `fonttools`
- **Regular and Bold weights only** — don't ship the full weight range
- **`font-display: optional`** so a slow-loading web font never blocks rendering or shifts layout
- **Self-host fonts** — don't depend on a third-party CDN round trip
