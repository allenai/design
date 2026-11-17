# Standard Conventions in Recommendations

Before recommending a novel interaction pattern or keyboard shortcut:

1. **Check whether an established convention already solves the problem.** For example: Enter to
   submit a form, Escape to close a dialog, arrow keys within a radio group, Tab to move between
   interactive elements. Familiar patterns may reduce learning demands; do not assume prior
   knowledge for everyone.

2. **Prefer platform and design system standard patterns over custom inventions.** The platform and
   design systems define expected keyboard interaction patterns for common widgets (tabs, menus,
   trees, dialogs, comboboxes, etc.). Custom keyboard patterns that diverge from these expectations
   violate user mental models.

3. **Do not recommend visual layout changes as solutions to tab order problems.** Visual rendering
   does not affect rendered order. Recommending sticky positioning or CSS changes will not fix tab
   order issues — rendered UI restructuring or tabindex management is needed.

4. **Do not recommend keyboard shortcuts that duplicate existing standard behavior** or that would
   be undiscoverable without documentation. A shortcut that does the same thing as Tab is redundant;
   a shortcut that no one knows about is useless.

## Purpose

Recommendations should move the interface toward standard, predictable behavior — not introduce
novel patterns that require additional learning. The goal is to align with what users already know.
