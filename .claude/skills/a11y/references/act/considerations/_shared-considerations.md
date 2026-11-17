---
type: shared
title: Shared exploration strategies, interaction contexts, and learning considerations
description: >
  Reusable guidance for several access strategies and task contexts. Include only entries
  relevant to the evaluation; these do not describe a default person or capabilities
  shared by everyone. This file is supporting content, not a standalone evaluation lens.
---

# Shared Accessibility Considerations

This file collects reusable exploration strategies, interaction contexts, and learning
considerations. No strategy applies to everyone. Each elaborated consideration document includes
applicable entries inline and excludes strategies outside its evaluation scope. The entries describe
interface support for possible ways of interacting, not a default user.

> Use considerations to evaluate interface barriers, not to classify real people. Do not infer
> disability, diagnosis, capability, or accommodation from behavior, zoom level, preferences, or
> assistive-technology use. See
> [`methodology/responsible-consideration-use.md`](../methodology/responsible-consideration-use.md).

## Exploration Strategies

### Visual scanning and layout comprehension

When visual scanning is available and preferred, page regions such as the header, navigation, main
content, sidebar, and footer can help establish layout. Visible control affordances and hierarchy
through headings, spacing, colour, and size may help locate actions. Do not assume that visual
scanning is available or that these cues work alone.

**AT Mechanisms**: Visual perception **Device context**: All

**UI Requirements**: Clear visual hierarchy through headings, spacing, and grouping. Interactive
elements must look interactive (visible borders, underlines, or other affordances). Primary actions
should be visually prominent.

### Mouse / pointer interaction

Mouse, trackpad, or touch-pointer interaction may involve clicking, selecting text, dragging,
hovering for tooltips, or opening context menus. Evaluate the actions supported by the chosen input
method; hover and sustained dragging are not available in every pointer context.

**AT Mechanisms**: Mouse, Trackpad, Touchscreen **Device context**: Desktop

**UI Requirements**: Interactive elements are easy to activate with the intended pointer action and
are far enough apart that users do not accidentally activate adjacent controls. Hover states should
indicate interactivity. Drag-and-drop should have clear affordances.

### Reading and scrolling

Visual reading may proceed sequentially or through heading scans, with scrolling to reach content
beyond the viewport. Evaluate logical flow appropriate to the writing system, such as top-to-bottom
and left-to-right in LTR content. Do not assume one reading direction or scrolling method across
languages and input configurations.

**AT Mechanisms**: Visual reading, Mouse wheel / scroll gesture **Device context**: All

**UI Requirements**: Text must be readable: sufficient contrast, reasonable font size, adequate line
spacing. Content should not require horizontal scrolling at standard viewport widths. Long pages
should provide navigation aids (table of contents, back-to-top).

### Form interaction

Form tasks may involve reaching fields, typing, selecting options, checking boxes, and submitting
through different input methods. Evaluate clear labels, placeholder text that does not replace
labels, and actionable error feedback without assuming pointer access.

**AT Mechanisms**: Keyboard (typing), Mouse (clicking fields), Visual reading (labels) **Device
context**: All

**UI Requirements**: Every form field must have a visible label. Required fields must be clearly
indicated. Error messages must be specific, adjacent to the field, and visible without scrolling.
Successful submission must be clearly confirmed.

### Navigation and wayfinding

Menus, breadcrumbs, links, and browser back/forward can support navigation between pages and views.
Evaluate whether the current location, available destinations, and return paths are understandable
through the access strategies in scope.

**AT Mechanisms**: Visual scanning, Mouse clicking, Browser controls **Device context**: All

**UI Requirements**: Consistent navigation across pages. Current location clearly indicated (active
nav item, breadcrumbs). Important actions reachable from any page. Browser back button should work
predictably.

### Touch / pointer interaction

Touch interaction may include taps, swipes, pinch-zoom, or long presses, depending on the device and
access method. Direct touch has no hover preview; evaluate discoverable controls, target size, and
alternatives to complex gestures. Do not require every touch interaction pattern to be available to
the same person.

**AT Mechanisms**: Touchscreen tap, Swipe gestures, Pinch-zoom **Device context**: Mobile

**UI Requirements**: Touch targets are easy to activate without accidentally activating adjacent
controls — small or tightly packed targets force users to retry or hit the wrong control. No
reliance on hover for essential information. Custom gestures must have single-pointer alternatives.
Drag-and-drop must have tap-based alternatives. No accidental activation from scroll gestures.

## Interaction Contexts

### New / infrequent user

First-time or infrequent interaction may require rediscovering controls and workflows. Labels,
accessible affordances, and progressive disclosure can support learning without requiring prior
knowledge of shortcuts or hidden features.

**Primary AT**: None **Device context**: All **Preferred navigation**: Visual scanning and layout
comprehension, Navigation and wayfinding, Form interaction

**Expectations**:

- Interface is learnable without documentation
- Primary actions are visually obvious
- Error messages guide toward resolution
- Navigation structure is understandable

### Expert / frequent user

Frequent interaction may build familiarity with layouts, shortcuts, and workflows. Consistency and
efficient paths can support established strategies; changes may require relearning. Expertise in a
task does not establish expertise with every assistive technology.

**Primary AT**: None **Device context**: All **Preferred navigation**: Mouse / pointer interaction,
Navigation and wayfinding

**Expectations**:

- Keyboard shortcuts for common tasks
- Consistent layout across sessions and pages
- Efficient paths to frequently used features
- Changes to familiar workflows are clearly communicated

## Learning Considerations

- **First visit**: Familiar web, desktop, and mobile conventions may support learning, but
  recognition of hamburger menus, search icons, tabs, or modals is not guaranteed. Explain
  unfamiliar patterns and expose their purpose through accessible labels and feedback.

- **Mental models**: Early interactions may establish expectations. Inconsistent behavior, such as a
  button that sometimes navigates and sometimes submits, can undermine confidence and require
  additional checking.

- **Error recovery**: Support recovery from mistakes through undo, appropriate confirmation dialogs,
  and clear error messages. Make the consequences of irreversible actions clear rather than assuming
  every mistake can be avoided.

- **Cognitive load**: Clutter, excessive options, and unclear hierarchy can increase attention and
  memory demands. Evaluate those demands in the task context without inferring a person's cognitive
  capabilities.

## Shared Exclusions by Consideration

When a consideration includes shared content, its exclusions define evaluation scope, not a person's
capabilities. Other strategies may still be useful outside that scope:

| Consideration                        | Excluded Shared Strategies                                                 |
| ------------------------------------ | -------------------------------------------------------------------------- |
| 4.2.1 (Nonvisual access)             | Visual scanning and layout comprehension, Mouse / pointer interaction      |
| 4.2.7 (Keyboard interaction)         | Mouse / pointer interaction, Touch / pointer interaction                   |
| 4.2.7 (Voice control)                | Mouse / pointer interaction, Touch / pointer interaction, Form interaction |
| 4.2.8 (Pointer interaction)          | _(no exclusions; include only task-relevant entries)_                      |
| 4.2.3 (Alternatives to colour cues)  | _(no exclusions; include only task-relevant entries)_                      |
| 4.2.2 (Visual adaptation)            | _(no exclusions; include only task-relevant entries)_                      |
| 4.2.6 (Alternatives to speech input) | _(no exclusions; include only task-relevant entries)_                      |
