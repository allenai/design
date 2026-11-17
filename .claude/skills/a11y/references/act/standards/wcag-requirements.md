# WCAG 2.2 Success Criteria Reference

> **Supporting reference only.** This file includes WCAG 2.2 material under the W3C Document License
> and is not the authoritative specification. Preserve
> [`wcag-requirements.LICENSE.md`](wcag-requirements.LICENSE.md) when copying or distributing this
> file. For conformance decisions, use the canonical
> [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/).

Web Content Accessibility Guidelines (WCAG) 2.2 Success Criteria — verbatim normative text from the
[W3C Recommendation of 12 December 2024](https://www.w3.org/TR/WCAG22/). Organized by applicability
category for efficient matching against evaluation findings.

**Total Success Criteria: 87 (86 active + 1 obsolete: 4.1.1 Parsing)**

**Conformance levels:** A, AA, AAA

> Verbatim text from WCAG 2.2; see [`wcag-requirements.LICENSE.md`](wcag-requirements.LICENSE.md)
> for W3C copyright, status, derivative-work notice, and the disclaimers required by the
> [W3C Document License — 2023 version](https://www.w3.org/copyright/document-license-2023/).

## Categories

- [Compatible with platform 3rd Party AT](#compatible-with-platform-3rd-party-at) (12)
- [Visuals, Animations, Audio, Video](#visuals-animations-audio-video) (25)
- [Keyboarding / Focus](#keyboarding--focus) (14)
- [Gen. Design Guidelines](#gen.-design-guidelines) (20)
- [Login, Time-Bound Interaction & Error Management](#login-time-bound-interaction--error-management)
  (16)

## Compatible with platform 3rd Party AT

### 1.1.1 — Non-text Content

**Level:** A **Guideline:** 1.1 Text Alternatives

All non-text content that is presented to the user has a text alternative that serves the equivalent
purpose, except for the situations listed below.

- **Controls, Input** If non-text content is a control or accepts user input, then it has a name
  that describes its purpose. (Refer to Success Criterion 4.1.2 for additional requirements for
  controls and content that accepts user input.)
- **Time-Based Media** If non-text content is time-based media, then text alternatives at least
  provide descriptive identification of the non-text content. (Refer to Guideline 1.2 for additional
  requirements for media.)
- **Test** If non-text content is a test or exercise that would be invalid if presented in text,
  then text alternatives at least provide descriptive identification of the non-text content.
- **Sensory** If non-text content is primarily intended to create a specific sensory experience,
  then text alternatives at least provide descriptive identification of the non-text content.
- **CAPTCHA** If the purpose of non-text content is to confirm that content is being accessed by a
  person rather than a computer, then text alternatives that identify and describe the purpose of
  the non-text content are provided, and alternative forms of CAPTCHA using output modes for
  different types of sensory perception are provided to accommodate different disabilities.
- **Decoration, Formatting, Invisible** If non-text content is pure decoration, is used only for
  visual formatting, or is not presented to users, then it is implemented in a way that it can be
  ignored by assistive technology.

[Understanding Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)

### 1.3.1 — Info and Relationships

**Level:** A **Guideline:** 1.3 Adaptable

Information, structure, and relationships conveyed through presentation can be programmatically
determined or are available in text.

[Understanding Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)

### 1.3.5 — Identify Input Purpose

**Level:** AA **Guideline:** 1.3 Adaptable

The purpose of each input field collecting information about the user can be programmatically
determined when:

- The input field serves a purpose identified in the Input Purposes for user interface components
  section; and
- The content is implemented using technologies with support for identifying the expected meaning
  for form input data.

[Understanding Identify Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)

### 1.3.6 — Identify Purpose

**Level:** AAA **Guideline:** 1.3 Adaptable

In content implemented using markup languages, the purpose of user interface components, icons, and
regions can be programmatically determined.

[Understanding Identify Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-purpose.html)

### 2.4.2 — Page Titled

**Level:** A **Guideline:** 2.4 Navigable

Web pages have titles that describe topic or purpose.

[Understanding Page Titled](https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html)

### 2.4.4 — Link Purpose (In Context)

**Level:** A **Guideline:** 2.4 Navigable

The purpose of each link can be determined from the link text alone or from the link text together
with its programmatically determined link context, except where the purpose of the link would be
ambiguous to users in general.

[Understanding Link Purpose (In Context)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)

### 2.4.9 — Link Purpose (Link Only)

**Level:** AAA **Guideline:** 2.4 Navigable

A mechanism is available to allow the purpose of each link to be identified from link text alone,
except where the purpose of the link would be ambiguous to users in general.

[Understanding Link Purpose (Link Only)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-link-only.html)

### 3.1.1 — Language of Page

**Level:** A **Guideline:** 3.1 Readable

The default human language of each web page can be programmatically determined.

[Understanding Language of Page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html)

### 3.1.2 — Language of Parts

**Level:** AA **Guideline:** 3.1 Readable

The human language of each passage or phrase in the content can be programmatically determined
except for proper names, technical terms, words of indeterminate language, and words or phrases that
have become part of the vernacular of the immediately surrounding text.

[Understanding Language of Parts](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html)

### 4.1.1 — Parsing (Obsolete and removed)

**Level:** Obsolete and removed **Guideline:** 4.1 Compatible

This criterion was originally adopted to address problems that assistive technology had directly
parsing HTML. Assistive technology no longer has any need to directly parse HTML. Consequently,
these problems either no longer exist or are addressed by other criteria. This criterion no longer
has utility and is removed.

**Annotation note:** Do not map findings to WCAG 4.1.1 in WCAG 2.2 evaluations. Retained here for
completeness because authors reporting WCAG 2.0 or 2.1 conformance may still need to reference it.

[Understanding Parsing (Obsolete and removed)](https://www.w3.org/WAI/WCAG22/Understanding/parsing.html)

### 4.1.2 — Name, Role, Value

**Level:** A **Guideline:** 4.1 Compatible

For all user interface components (including but not limited to: form elements, links and components
generated by scripts), the name and role can be programmatically determined; states, properties, and
values that can be set by the user can be programmatically set; and notification of changes to these
items is available to user agents, including assistive technologies.

[Understanding Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)

### 4.1.3 — Status Messages

**Level:** AA **Guideline:** 4.1 Compatible

In content implemented using markup languages, status messages can be programmatically determined
through role or properties such that they can be presented to the user by assistive technologies
without receiving focus.

[Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

## Visuals, Animations, Audio, Video

### 1.2.1 — Audio-only and Video-only (Prerecorded)

**Level:** A **Guideline:** 1.2 Time-based Media

For prerecorded audio-only and prerecorded video-only media, the following are true, except when the
audio or video is a media alternative for text and is clearly labeled as such:

- **Prerecorded Audio-only** An alternative for time-based media is provided that presents
  equivalent information for prerecorded audio-only content.
- **Prerecorded Video-only** Either an alternative for time-based media or an audio track is
  provided that presents equivalent information for prerecorded video-only content.

[Understanding Audio-only and Video-only (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html)

### 1.2.2 — Captions (Prerecorded)

**Level:** A **Guideline:** 1.2 Time-based Media

Captions are provided for all prerecorded audio content in synchronized media, except when the media
is a media alternative for text and is clearly labeled as such.

[Understanding Captions (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html)

### 1.2.3 — Audio Description or Media Alternative (Prerecorded)

**Level:** A **Guideline:** 1.2 Time-based Media

An alternative for time-based media or audio description of the prerecorded video content is
provided for synchronized media, except when the media is a media alternative for text and is
clearly labeled as such.

[Understanding Audio Description or Media Alternative (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html)

### 1.2.4 — Captions (Live)

**Level:** AA **Guideline:** 1.2 Time-based Media

Captions are provided for all live audio content in synchronized media.

[Understanding Captions (Live)](https://www.w3.org/WAI/WCAG22/Understanding/captions-live.html)

### 1.2.5 — Audio Description (Prerecorded)

**Level:** AA **Guideline:** 1.2 Time-based Media

Audio description is provided for all prerecorded video content in synchronized media.

[Understanding Audio Description (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)

### 1.2.6 — Sign Language (Prerecorded)

**Level:** AAA **Guideline:** 1.2 Time-based Media

Sign language interpretation is provided for all prerecorded audio content in synchronized media.

[Understanding Sign Language (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/sign-language-prerecorded.html)

### 1.2.7 — Extended Audio Description (Prerecorded)

**Level:** AAA **Guideline:** 1.2 Time-based Media

Where pauses in foreground audio are insufficient to allow audio descriptions to convey the sense of
the video, extended audio description is provided for all prerecorded video content in synchronized
media.

[Understanding Extended Audio Description (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/extended-audio-description-prerecorded.html)

### 1.2.8 — Media Alternative (Prerecorded)

**Level:** AAA **Guideline:** 1.2 Time-based Media

An alternative for time-based media is provided for all prerecorded synchronized media and for all
prerecorded video-only media.

[Understanding Media Alternative (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/media-alternative-prerecorded.html)

### 1.2.9 — Audio-only (Live)

**Level:** AAA **Guideline:** 1.2 Time-based Media

An alternative for time-based media that presents equivalent information for live audio-only content
is provided.

[Understanding Audio-only (Live)](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-live.html)

### 1.3.3 — Sensory Characteristics

**Level:** A **Guideline:** 1.3 Adaptable

Instructions provided for understanding and operating content do not rely solely on sensory
characteristics of components such as shape, color, size, visual location, orientation, or sound.

[Understanding Sensory Characteristics](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html)

### 1.3.4 — Orientation

**Level:** AA **Guideline:** 1.3 Adaptable

Content does not restrict its view and operation to a single display orientation, such as portrait
or landscape, unless a specific display orientation is essential.

[Understanding Orientation](https://www.w3.org/WAI/WCAG22/Understanding/orientation.html)

### 1.4.1 — Use of Color

**Level:** A **Guideline:** 1.4 Distinguishable

Color is not used as the only visual means of conveying information, indicating an action, prompting
a response, or distinguishing a visual element.

[Understanding Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)

### 1.4.3 — Contrast (Minimum)

**Level:** AA **Guideline:** 1.4 Distinguishable

The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except
for the following:

- **Large Text** Large-scale text and images of large-scale text have a contrast ratio of at least
  3:1;
- **Incidental** Text or images of text that are part of an inactive user interface component, that
  are pure decoration, that are not visible to anyone, or that are part of a picture that contains
  significant other visual content, have no contrast requirement.
- **Logotypes** Text that is part of a logo or brand name has no contrast requirement.

[Understanding Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

### 1.4.4 — Resize Text

**Level:** AA **Guideline:** 1.4 Distinguishable

Except for captions and images of text, text can be resized without assistive technology up to 200
percent without loss of content or functionality.

[Understanding Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)

### 1.4.5 — Images of Text

**Level:** AA **Guideline:** 1.4 Distinguishable

If the technologies being used can achieve the visual presentation, text is used to convey
information rather than images of text except for the following:

- **Customizable** The image of text can be visually customized to the user's requirements;
- **Essential** A particular presentation of text is essential to the information being conveyed.

[Understanding Images of Text](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html)

### 1.4.6 — Contrast (Enhanced)

**Level:** AAA **Guideline:** 1.4 Distinguishable

The visual presentation of text and images of text has a contrast ratio of at least 7:1, except for
the following:

- **Large Text** Large-scale text and images of large-scale text have a contrast ratio of at least
  4.5:1;
- **Incidental** Text or images of text that are part of an inactive user interface component, that
  are pure decoration, that are not visible to anyone, or that are part of a picture that contains
  significant other visual content, have no contrast requirement.
- **Logotypes** Text that is part of a logo or brand name has no contrast requirement.

[Understanding Contrast (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html)

### 1.4.7 — Low or No Background Audio

**Level:** AAA **Guideline:** 1.4 Distinguishable

For prerecorded audio-only content that (1) contains primarily speech in the foreground, (2) is not
an audio CAPTCHA or audio logo, and (3) is not vocalization intended to be primarily musical
expression such as singing or rapping, at least one of the following is true:

- **No Background** The audio does not contain background sounds.
- **Turn Off** The background sounds can be turned off.
- **20 dB** The background sounds are at least 20 decibels lower than the foreground speech content,
  with the exception of occasional sounds that last for only one or two seconds.

[Understanding Low or No Background Audio](https://www.w3.org/WAI/WCAG22/Understanding/low-or-no-background-audio.html)

### 1.4.8 — Visual Presentation

**Level:** AAA **Guideline:** 1.4 Distinguishable

For the visual presentation of blocks of text, a mechanism is available to achieve the following:

- Foreground and background colors can be selected by the user.
- Width is no more than 80 characters or glyphs (40 if CJK).
- Text is not justified (aligned to both the left and the right margins).
- Line spacing (leading) is at least space-and-a-half within paragraphs, and paragraph spacing is at
  least 1.5 times larger than the line spacing.
- Text can be resized without assistive technology up to 200 percent in a way that does not require
  the user to scroll horizontally to read a line of text on a full-screen window.

[Understanding Visual Presentation](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html)

### 1.4.9 — Images of Text (No Exception)

**Level:** AAA **Guideline:** 1.4 Distinguishable

Images of text are only used for pure decoration or where a particular presentation of text is
essential to the information being conveyed.

[Understanding Images of Text (No Exception)](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text-no-exception.html)

### 1.4.10 — Reflow

**Level:** AA **Guideline:** 1.4 Distinguishable

Content can be presented without loss of information or functionality, and without requiring
scrolling in two dimensions for:

- Vertical scrolling content at a width equivalent to 320 CSS pixels;
- Horizontal scrolling content at a height equivalent to 256 CSS pixels.

Except for parts of the content which require two-dimensional layout for usage or meaning.

[Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

### 1.4.11 — Non-text Contrast

**Level:** AA **Guideline:** 1.4 Distinguishable

The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent
color(s):

- **User Interface Components** Visual information required to identify user interface components
  and states, except for inactive components or where the appearance of the component is determined
  by the user agent and not modified by the author;
- **Graphical Objects** Parts of graphics required to understand the content, except when a
  particular presentation of graphics is essential to the information being conveyed.

[Understanding Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)

### 1.4.12 — Text Spacing

**Level:** AA **Guideline:** 1.4 Distinguishable

In content implemented using markup languages that support the following text style properties, no
loss of content or functionality occurs by setting all of the following and by changing no other
style property:

- Line height (line spacing) to at least 1.5 times the font size;
- Spacing following paragraphs to at least 2 times the font size;
- Letter spacing (tracking) to at least 0.12 times the font size;
- Word spacing to at least 0.16 times the font size.

Exception: Human languages and scripts that do not make use of one or more of these text style
properties in written text can conform using only the properties that exist for that combination of
language and script.

[Understanding Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)

### 2.3.1 — Three Flashes or Below Threshold

**Level:** A **Guideline:** 2.3 Seizures and Physical Reactions

Web pages do not contain anything that flashes more than three times in any one second period, or
the flash is below the general flash and red flash thresholds.

[Understanding Three Flashes or Below Threshold](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)

### 2.3.2 — Three Flashes

**Level:** AAA **Guideline:** 2.3 Seizures and Physical Reactions

Web pages do not contain anything that flashes more than three times in any one second period.

[Understanding Three Flashes](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes.html)

### 2.3.3 — Animation from Interactions

**Level:** AAA **Guideline:** 2.3 Seizures and Physical Reactions

Motion animation triggered by interaction can be disabled, unless the animation is essential to the
functionality or the information being conveyed.

[Understanding Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)

## Keyboarding / Focus

### 1.4.13 — Content on Hover or Focus

**Level:** AA **Guideline:** 1.4 Distinguishable

Where receiving and then removing pointer hover or keyboard focus triggers additional content to
become visible and then hidden, the following are true:

- **Dismissible** A mechanism is available to dismiss the additional content without moving pointer
  hover or keyboard focus, unless the additional content communicates an input error or does not
  obscure or replace other content;
- **Hoverable** If pointer hover can trigger the additional content, then the pointer can be moved
  over the additional content without the additional content disappearing;
- **Persistent** The additional content remains visible until the hover or focus trigger is removed,
  the user dismisses it, or its information is no longer valid.

Exception: The visual presentation of the additional content is controlled by the user agent and is
not modified by the author.

[Understanding Content on Hover or Focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html)

### 2.1.1 — Keyboard

**Level:** A **Guideline:** 2.1 Keyboard Accessible

All functionality of the content is operable through a keyboard interface without requiring specific
timings for individual keystrokes, except where the underlying function requires input that depends
on the path of the user's movement and not just the endpoints.

[Understanding Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)

### 2.1.2 — No Keyboard Trap

**Level:** A **Guideline:** 2.1 Keyboard Accessible

If keyboard focus can be moved to a component of the page using a keyboard interface, then focus can
be moved away from that component using only a keyboard interface, and, if it requires more than
unmodified arrow or tab keys or other standard exit methods, the user is advised of the method for
moving focus away.

[Understanding No Keyboard Trap](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html)

### 2.1.3 — Keyboard (No Exception)

**Level:** AAA **Guideline:** 2.1 Keyboard Accessible

All functionality of the content is operable through a keyboard interface without requiring specific
timings for individual keystrokes.

[Understanding Keyboard (No Exception)](https://www.w3.org/WAI/WCAG22/Understanding/keyboard-no-exception.html)

### 2.1.4 — Character Key Shortcuts

**Level:** A **Guideline:** 2.1 Keyboard Accessible

If a keyboard shortcut is implemented in content using only letter (including upper- and lower-case
letters), punctuation, number, or symbol characters, then at least one of the following is true:

- **Turn off** A mechanism is available to turn the shortcut off;
- **Remap** A mechanism is available to remap the shortcut to include one or more non-printable
  keyboard keys (e.g., Ctrl, Alt);
- **Active only on focus** The keyboard shortcut for a user interface component is only active when
  that component has focus.

[Understanding Character Key Shortcuts](https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html)

### 2.4.1 — Bypass Blocks

**Level:** A **Guideline:** 2.4 Navigable

A mechanism is available to bypass blocks of content that are repeated on multiple web pages.

[Understanding Bypass Blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html)

### 2.4.3 — Focus Order

**Level:** A **Guideline:** 2.4 Navigable

If a web page can be navigated sequentially and the navigation sequences affect meaning or
operation, focusable components receive focus in an order that preserves meaning and operability.

[Understanding Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)

### 2.4.6 — Headings and Labels

**Level:** AA **Guideline:** 2.4 Navigable

Headings and labels describe topic or purpose.

[Understanding Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)

### 2.4.7 — Focus Visible

**Level:** AA **Guideline:** 2.4 Navigable

Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is
visible.

[Understanding Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)

### 2.4.11 — Focus Not Obscured (Minimum)

**Level:** AA **Guideline:** 2.4 Navigable

When a user interface component receives keyboard focus, the component is not entirely hidden due to
author-created content.

[Understanding Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

### 2.4.12 — Focus Not Obscured (Enhanced)

**Level:** AAA **Guideline:** 2.4 Navigable

When a user interface component receives keyboard focus, no part of the component is hidden by
author-created content.

[Understanding Focus Not Obscured (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-enhanced.html)

### 2.4.13 — Focus Appearance

**Level:** AAA **Guideline:** 2.4 Navigable

When the keyboard focus indicator is visible, an area of the focus indicator meets all the
following:

- is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component or
  sub-component, and
- has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states.

Exceptions:

- The focus indicator is determined by the user agent and cannot be adjusted by the author, or
- The focus indicator and the indicator's background color are not modified by the author.

[Understanding Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

### 3.2.1 — On Focus

**Level:** A **Guideline:** 3.2 Predictable

When any user interface component receives focus, it does not initiate a change of context.

[Understanding On Focus](https://www.w3.org/WAI/WCAG22/Understanding/on-focus.html)

### 3.2.2 — On Input

**Level:** A **Guideline:** 3.2 Predictable

Changing the setting of any user interface component does not automatically cause a change of
context unless the user has been advised of the behavior before using the component.

[Understanding On Input](https://www.w3.org/WAI/WCAG22/Understanding/on-input.html)

## Gen. Design Guidelines

### 1.3.2 — Meaningful Sequence

**Level:** A **Guideline:** 1.3 Adaptable

When the sequence in which content is presented affects its meaning, a correct reading sequence can
be programmatically determined.

[Understanding Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)

### 2.4.5 — Multiple Ways

**Level:** AA **Guideline:** 2.4 Navigable

More than one way is available to locate a web page within a set of web pages except where the web
page is the result of, or a step in, a process.

[Understanding Multiple Ways](https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways.html)

### 2.4.8 — Location

**Level:** AAA **Guideline:** 2.4 Navigable

Information about the user's location within a set of web pages is available.

[Understanding Location](https://www.w3.org/WAI/WCAG22/Understanding/location.html)

### 2.4.10 — Section Headings

**Level:** AAA **Guideline:** 2.4 Navigable

Section headings are used to organize the content.

[Understanding Section Headings](https://www.w3.org/WAI/WCAG22/Understanding/section-headings.html)

### 2.5.1 — Pointer Gestures

**Level:** A **Guideline:** 2.5 Input Modalities

All functionality that uses multipoint or path-based gestures for operation can be operated with a
single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential.

[Understanding Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html)

### 2.5.2 — Pointer Cancellation

**Level:** A **Guideline:** 2.5 Input Modalities

For functionality that can be operated using a single pointer, at least one of the following is
true:

- **No Down-Event** The down-event of the pointer is not used to execute any part of the function;
- **Abort or Undo** Completion of the function is on the up-event, and a mechanism is available to
  abort the function before completion or to undo the function after completion;
- **Up Reversal** The up-event reverses any outcome of the preceding down-event;
- **Essential** Completing the function on the down-event is essential.

[Understanding Pointer Cancellation](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html)

### 2.5.3 — Label in Name

**Level:** A **Guideline:** 2.5 Input Modalities

For user interface components with labels that include text or images of text, the name contains the
text that is presented visually.

[Understanding Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)

### 2.5.4 — Motion Actuation

**Level:** A **Guideline:** 2.5 Input Modalities

Functionality that can be operated by device motion or user motion can also be operated by user
interface components and responding to the motion can be disabled to prevent accidental actuation,
except when:

- **Supported Interface** The motion is used to operate functionality through an accessibility
  supported interface;
- **Essential** The motion is essential for the function and doing so would invalidate the activity.

[Understanding Motion Actuation](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html)

### 2.5.5 — Target Size (Enhanced)

**Level:** AAA **Guideline:** 2.5 Input Modalities

The size of the target for pointer inputs is at least 44 by 44 CSS pixels except when:

- **Equivalent** The target is available through an equivalent link or control on the same page that
  is at least 44 by 44 CSS pixels;
- **Inline** The target is in a sentence or block of text;
- **User Agent Control** The size of the target is determined by the user agent and is not modified
  by the author;
- **Essential** A particular presentation of the target is essential to the information being
  conveyed.

[Understanding Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)

### 2.5.6 — Concurrent Input Mechanisms

**Level:** AAA **Guideline:** 2.5 Input Modalities

Web content does not restrict use of input modalities available on a platform except where the
restriction is essential, required to ensure the security of the content, or required to respect
user settings.

[Understanding Concurrent Input Mechanisms](https://www.w3.org/WAI/WCAG22/Understanding/concurrent-input-mechanisms.html)

### 2.5.7 — Dragging Movements

**Level:** AA **Guideline:** 2.5 Input Modalities

All functionality that uses a dragging movement for operation can be achieved by a single pointer
without dragging, unless dragging is essential or the functionality is determined by the user agent
and not modified by the author.

[Understanding Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)

### 2.5.8 — Target Size (Minimum)

**Level:** AA **Guideline:** 2.5 Input Modalities

The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when:

- **Spacing** Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a
  24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect
  another target or the circle for another undersized target;
- **Equivalent** The function can be achieved through a different control on the same page that
  meets this criterion;
- **Inline** The target is in a sentence or its size is otherwise constrained by the line-height of
  non-target text;
- **User Agent Control** The size of the target is determined by the user agent and is not modified
  by the author;
- **Essential** A particular presentation of the target is essential or is legally required for the
  information being conveyed.

[Understanding Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

### 3.1.3 — Unusual Words

**Level:** AAA **Guideline:** 3.1 Readable

A mechanism is available for identifying specific definitions of words or phrases used in an unusual
or restricted way, including idioms and jargon.

[Understanding Unusual Words](https://www.w3.org/WAI/WCAG22/Understanding/unusual-words.html)

### 3.1.4 — Abbreviations

**Level:** AAA **Guideline:** 3.1 Readable

A mechanism for identifying the expanded form or meaning of abbreviations is available.

[Understanding Abbreviations](https://www.w3.org/WAI/WCAG22/Understanding/abbreviations.html)

### 3.1.5 — Reading Level

**Level:** AAA **Guideline:** 3.1 Readable

When text requires reading ability more advanced than the lower secondary education level after
removal of proper names and titles, supplemental content, or a version that does not require reading
ability more advanced than the lower secondary education level, is available.

[Understanding Reading Level](https://www.w3.org/WAI/WCAG22/Understanding/reading-level.html)

### 3.1.6 — Pronunciation

**Level:** AAA **Guideline:** 3.1 Readable

A mechanism is available for identifying specific pronunciation of words where meaning of the words,
in context, is ambiguous without knowing the pronunciation.

[Understanding Pronunciation](https://www.w3.org/WAI/WCAG22/Understanding/pronunciation.html)

### 3.2.3 — Consistent Navigation

**Level:** AA **Guideline:** 3.2 Predictable

Navigational mechanisms that are repeated on multiple web pages within a set of web pages occur in
the same relative order each time they are repeated, unless a change is initiated by the user.

[Understanding Consistent Navigation](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html)

### 3.2.4 — Consistent Identification

**Level:** AA **Guideline:** 3.2 Predictable

Components that have the same functionality within a set of web pages are identified consistently.

[Understanding Consistent Identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html)

### 3.2.5 — Change on Request

**Level:** AAA **Guideline:** 3.2 Predictable

Changes of context are initiated only by user request or a mechanism is available to turn off such
changes.

[Understanding Change on Request](https://www.w3.org/WAI/WCAG22/Understanding/change-on-request.html)

### 3.2.6 — Consistent Help

**Level:** A **Guideline:** 3.2 Predictable

If a web page contains any of the following help mechanisms, and those mechanisms are repeated on
multiple web pages within a set of web pages, they occur in the same order relative to other page
content, unless a change is initiated by the user:

- Human contact details;
- Human contact mechanism;
- Self-help option;
- A fully automated contact mechanism.

[Understanding Consistent Help](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html)

## Login, Time-Bound Interaction & Error Management

### 1.4.2 — Audio Control

**Level:** A **Guideline:** 1.4 Distinguishable

If any audio on a web page plays automatically for more than 3 seconds, either a mechanism is
available to pause or stop the audio, or a mechanism is available to control audio volume
independently from the overall system volume level.

[Understanding Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html)

### 2.2.1 — Timing Adjustable

**Level:** A **Guideline:** 2.2 Enough Time

For each time limit that is set by the content, at least one of the following is true:

- **Turn off** The user is allowed to turn off the time limit before encountering it; or
- **Adjust** The user is allowed to adjust the time limit before encountering it over a wide range
  that is at least ten times the length of the default setting; or
- **Extend** The user is warned before time expires and given at least 20 seconds to extend the time
  limit with a simple action (for example, "press the space bar"), and the user is allowed to extend
  the time limit at least ten times; or
- **Real-time Exception** The time limit is a required part of a real-time event (for example, an
  auction), and no alternative to the time limit is possible; or
- **Essential Exception** The time limit is essential and extending it would invalidate the
  activity; or
- **20 Hour Exception** The time limit is longer than 20 hours.

[Understanding Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html)

### 2.2.2 — Pause, Stop, Hide

**Level:** A **Guideline:** 2.2 Enough Time

For moving, blinking, scrolling, or auto-updating information, all of the following are true:

- **Moving, blinking, scrolling** For any moving, blinking or scrolling information that (1) starts
  automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other
  content, there is a mechanism for the user to pause, stop, or hide it unless the movement,
  blinking, or scrolling is part of an activity where it is essential; and
- **Auto-updating** For any auto-updating information that (1) starts automatically and (2) is
  presented in parallel with other content, there is a mechanism for the user to pause, stop, or
  hide it or to control the frequency of the update unless the auto-updating is part of an activity
  where it is essential.

[Understanding Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)

### 2.2.3 — No Timing

**Level:** AAA **Guideline:** 2.2 Enough Time

Timing is not an essential part of the event or activity presented by the content, except for
non-interactive synchronized media and real-time events.

[Understanding No Timing](https://www.w3.org/WAI/WCAG22/Understanding/no-timing.html)

### 2.2.4 — Interruptions

**Level:** AAA **Guideline:** 2.2 Enough Time

Interruptions can be postponed or suppressed by the user, except interruptions involving an
emergency.

[Understanding Interruptions](https://www.w3.org/WAI/WCAG22/Understanding/interruptions.html)

### 2.2.5 — Re-authenticating

**Level:** AAA **Guideline:** 2.2 Enough Time

When an authenticated session expires, the user can continue the activity without loss of data after
re-authenticating.

[Understanding Re-authenticating](https://www.w3.org/WAI/WCAG22/Understanding/re-authenticating.html)

### 2.2.6 — Timeouts

**Level:** AAA **Guideline:** 2.2 Enough Time

Users are warned of the duration of any user inactivity that could cause data loss, unless the data
is preserved for more than 20 hours when the user does not take any actions.

[Understanding Timeouts](https://www.w3.org/WAI/WCAG22/Understanding/timeouts.html)

### 3.3.1 — Error Identification

**Level:** A **Guideline:** 3.3 Input Assistance

If an input error is automatically detected, the item that is in error is identified and the error
is described to the user in text.

[Understanding Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)

### 3.3.2 — Labels or Instructions

**Level:** A **Guideline:** 3.3 Input Assistance

Labels or instructions are provided when content requires user input.

[Understanding Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)

### 3.3.3 — Error Suggestion

**Level:** AA **Guideline:** 3.3 Input Assistance

If an input error is automatically detected and suggestions for correction are known, then the
suggestions are provided to the user, unless it would jeopardize the security or purpose of the
content.

[Understanding Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html)

### 3.3.4 — Error Prevention (Legal, Financial, Data)

**Level:** AA **Guideline:** 3.3 Input Assistance

For web pages that cause legal commitments or financial transactions for the user to occur, that
modify or delete user-controllable data in data storage systems, or that submit user test responses,
at least one of the following is true:

- **Reversible** Submissions are reversible.
- **Checked** Data entered by the user is checked for input errors and the user is provided an
  opportunity to correct them.
- **Confirmed** A mechanism is available for reviewing, confirming, and correcting information
  before finalizing the submission.

[Understanding Error Prevention (Legal, Financial, Data)](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html)

### 3.3.5 — Help

**Level:** AAA **Guideline:** 3.3 Input Assistance

Context-sensitive help is available.

[Understanding Help](https://www.w3.org/WAI/WCAG22/Understanding/help.html)

### 3.3.6 — Error Prevention (All)

**Level:** AAA **Guideline:** 3.3 Input Assistance

For web pages that require the user to submit information, at least one of the following is true:

- **Reversible** Submissions are reversible.
- **Checked** Data entered by the user is checked for input errors and the user is provided an
  opportunity to correct them.
- **Confirmed** A mechanism is available for reviewing, confirming, and correcting information
  before finalizing the submission.

[Understanding Error Prevention (All)](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-all.html)

### 3.3.7 — Redundant Entry

**Level:** A **Guideline:** 3.3 Input Assistance

Information previously entered by or provided to the user that is required to be entered again in
the same process is either:

- auto-populated, or
- available for the user to select.

Except when:

- re-entering the information is essential,
- the information is required to ensure the security of the content, or
- previously entered information is no longer valid.

[Understanding Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html)

### 3.3.8 — Accessible Authentication (Minimum)

**Level:** AA **Guideline:** 3.3 Input Assistance

A cognitive function test (such as remembering a password or solving a puzzle) is not required for
any step in an authentication process unless that step provides at least one of the following:

- **Alternative** Another authentication method that does not rely on a cognitive function test.
- **Mechanism** A mechanism is available to assist the user in completing the cognitive function
  test.
- **Object Recognition** The cognitive function test is to recognize objects.
- **Considerationl Content** The cognitive function test is to identify non-text content the user
  provided to the website.

[Understanding Accessible Authentication (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)

### 3.3.9 — Accessible Authentication (Enhanced)

**Level:** AAA **Guideline:** 3.3 Input Assistance

A cognitive function test (such as remembering a password or solving a puzzle) is not required for
any step in an authentication process unless that step provides at least one of the following:

- **Alternative** Another authentication method that does not rely on a cognitive function test.
- **Mechanism** A mechanism is available to assist the user in completing the cognitive function
  test.

[Understanding Accessible Authentication (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-enhanced.html)
