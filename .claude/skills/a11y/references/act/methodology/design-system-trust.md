# Design System Trust

When a design system or component library is named (e.g., Fluent UI, Material UI, Chakra UI), trust
that standard components implement their documented accessibility semantics correctly.

## Principle

Standard components from established design systems have been tested for accessibility. **Do NOT
flag standard component behavior as findings.** Only flag design decisions where the component is
configured incorrectly, used for the wrong purpose, or composed in a way that breaks its built-in
accessibility.

## What standard components handle automatically

- Semantic roles, states, and properties documented for that component
- Keyboard interaction patterns (Tab, arrow keys, Enter, Escape, Space)
- Focus management (focus trapping in dialogs, focus return after dismissal, roving tabindex in
  composite widgets)
- Value programmatic access for AT
- Label association when the component's label prop is used
- State programmatic access for AT

## What TO flag

- **Design decisions** that the component library cannot solve automatically: missing labels (no
  label prop specified), wrong component choice for the interaction, non-standard compositions,
  custom interactions built outside the library
- **Content-level concerns**: vague link text, missing alt text decisions (decorative vs.
  meaningful), heading hierarchy, landmark structure, reading order
- **Application-workflow issues**: focus not managed across multi-step workflows, missing status
  announcements for asynchronous operations
- **Deviations from the library's standard patterns**: a component used in a non-standard way that
  would override its built-in accessibility

## Design System Documentation URLs

When a design system is referenced, the following documentation URLs may be used as authoritative
sources for component behavior:

| Design System     | Documentation URL                                |
| ----------------- | ------------------------------------------------ |
| Fluent UI         | https://developer.microsoft.com/en-us/fluentui#/ |
| Material UI / MUI | https://mui.com/                                 |
| Chakra UI         | https://chakra-ui.com/                           |
| Radix             | https://www.radix-ui.com/                        |
| Headless UI       | https://headlessui.com/                          |
| React Aria        | https://react-spectrum.adobe.com/react-aria/     |
| Carbon            | https://carbondesignsystem.com/                  |
| Ant Design        | https://ant.design/                              |

## When uncertain

When uncertain whether something is standard component behavior, note it briefly as a low-priority
manual check — do not assert it as a finding.
