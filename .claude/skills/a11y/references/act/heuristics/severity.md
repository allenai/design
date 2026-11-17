# Severity Scale

## Severity Levels

| Level | Label       | Description                                                                                                        |
| ----- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 0     | Critical    | Blocks task completion entirely, causes data loss, or causes physical pain. The user cannot accomplish their goal. |
| 1     | Significant | Major barrier that substantially impedes the user. High-priority fix. Workaround may exist but is costly.          |
| 2     | Moderate    | Noticeable friction that slows the user down or causes confusion. Medium priority.                                 |
| 3     | Low         | Minor polish issue. The user notices it but can work around it easily.                                             |
| 4     | Trivial     | Usability smoothing with negligible impact. Edge case or cosmetic issue.                                           |

## Severity Assessment Model

Severity should be assessed through three dimensions:

### Frequency

How often does this barrier occur when using the access strategy under evaluation?

- **Every task** — encountered on every use of the primary workflow
- **Sometimes** — encountered on secondary tasks or specific paths
- **Rarely** — encountered only in edge cases or unusual workflows

### Impact

What task impact is supported by the evidence for this access strategy?

- **Blocked** — cannot complete the task at all
- **Significantly impeded** — can eventually complete but with major difficulty
- **Friction** — noticeable slowdown or confusion but can proceed
- **Cosmetic** — aware of the issue but unaffected functionally

### Persistence

Is a workaround available and usable through the access strategy under evaluation?

- **No workaround** — the barrier cannot be bypassed
- **Workaround with cost** — a workaround exists but requires significant extra effort, time, or a
  different approach
- **Easy workaround** — simple alternative path available

### Learnability

Does the cost persist across encounters, or can discoverable guidance reduce it with learning? Do
not assume that everyone will learn or use the same workaround.

- **Persists** — the barrier has the same cost every time it is encountered, regardless of
  experience (e.g., a keyboard trap, excessive tab stops that cannot be bypassed)
- **Reduces with learning** — initial friction is significant but decreases as the user builds a
  mental model (e.g., a non-obvious shortcut that, once learned, becomes routine)
- **First-time only** — the issue affects first encounters but has zero cost once learned (e.g.,
  discovering that F6 cycles between panes in a desktop application)

Learnability does NOT override impact for barriers that impose physical or cognitive cost on every
encounter. A keyboard user who must press Tab 30 times to reach the primary action faces that cost
every time — learning does not reduce the keystroke count. But a keyboard user who must discover
that F6 navigates between panes faces a one-time discovery cost that disappears once learned.

## Mapping to Severity Levels

| Frequency  | Impact                | Persistence          | Learnability          | Severity              |
| ---------- | --------------------- | -------------------- | --------------------- | --------------------- |
| Every task | Blocked               | No workaround        | Persists              | 0 — Critical          |
| Every task | Significantly impeded | Workaround with cost | Persists              | 1 — Significant       |
| Sometimes  | Friction              | Workaround available | Persists              | 2 — Moderate          |
| Every task | Friction              | Easy workaround      | Reduces with learning | 2–3 — Moderate to Low |
| Every task | Friction              | No workaround        | First-time only       | 3 — Low               |
| Rarely     | Friction              | Easy workaround      | Persists              | 3 — Low               |
| Edge case  | Cosmetic              | N/A                  | Any                   | 4 — Trivial           |

This table provides representative mappings. In practice, severity assessment requires judgment — a
rarely-encountered issue that blocks the user entirely may still be Critical if the task is
essential.

When learnability is "First-time only" or "Reduces with learning", consider whether the interface
provides adequate learning paths (documentation, keyboard shortcuts dialogs, tooltips on focus) that
make the pattern discoverable. An issue that reduces with learning but has no discovery path is more
severe than one with clear in-app guidance.

## Mitigation-Aware Severity

When the same evaluation identifies both a barrier and a working mitigation for that barrier, the
severity must account for the mitigation. A finding that documents "53 Tab stops to reach the
target" is less severe if the same report also confirms "search field reduces this to 4 Tab stops."

### Applying mitigations to severity

For each finding, check whether the evaluation has confirmed a mitigation — an alternative path,
workaround, or feature that reduces the barrier's impact:

1. **Discoverable and effective mitigation** — the mitigation is easy to find (visible in the
   interface, reachable without extensive navigation) and substantially reduces the barrier. Lower
   the severity by one level and document the mitigation in the finding. The finding's Persistence
   dimension shifts from "No workaround" to "Easy workaround."

2. **Existing but hard-to-discover mitigation** — the mitigation works but requires the user to
   discover it first (e.g., a search field that only appears after scrolling past many sections).
   Note the mitigation in the finding but do not lower severity — the discovery cost itself is a
   barrier, especially for first-time users.

3. **Partial mitigation** — the mitigation reduces but does not eliminate the barrier (e.g.,
   filtering reduces Tab count but phantom tab stops still exist within filtered results). Note the
   mitigation and use judgment on severity adjustment — partial mitigations may warrant a half-step
   reduction or no change.

Always document confirmed mitigations in the finding regardless of whether they affect the severity
rating. This provides a complete picture: the barrier exists, but the user has a path through it.

### Self-consistency check

Before finalising severity ratings, review all findings and dismissed items together. If a finding's
barrier is substantially addressed by a feature documented elsewhere in the report (in dismissed
items, in another finding's evidence, or in the consideration impact narrative), the finding's
severity should reflect that. Do not rate a barrier as if no mitigation exists when the same report
confirms one does.

## Per-Consideration Severity

The same finding can have different severity for different considerations. For example:

- Focus lost after an action may block keyboard or screen-reader navigation if no recovery path
  exists, or disrupt orientation under magnification. Determine severity from actual focus behavior
  and recovery options; do not assign it from a disability label.

When evaluating across multiple considerations, produce a severity per consideration per finding.
