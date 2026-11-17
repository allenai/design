# Usability Heuristics with Accessibility Lenses

This file is the entry point for the usability heuristic frameworks used in accessibility
evaluation. Each heuristic includes an accessibility lens to apply where relevant to the task.
Per-consideration lens overrides are defined in each consideration file's "Heuristic Lens Overrides"
section, keeping considerations self-contained.

Read the supplementary concerns below, then load only the heuristic file(s) relevant to the
evaluation cell you are working on. Listed filenames are relative to this file.

## Supplementary Concerns

These concerns are not mapped to a specific heuristic but should be evaluated across all heuristics:

### Privacy / Discreet

_Incorporates EN 301 549 FPS 4.2.11 (Privacy): "Where ICT provides features that are provided for
accessibility, the ICT maintains the privacy of users of these features at the same level as other
users."_

Interfaces should support use in social contexts without embarrassment or unwanted disclosure. This
applies across all considerations and all heuristics. Evaluate whether the interface inadvertently
exposes information the user would expect to remain private, including:

- **AT output exposure**: Content spoken aloud by a screen reader in earshot of others, enlarged
  text visible to bystanders when using screen magnification, and private data exposed through
  assistive technology output that the user would otherwise expect to remain discreet.
- **Accessibility-preference exposure**: A separate version, visible mode toggle, or AT-usage
  collection may expose preferences or invite unwanted inference. Using an accessibility feature is
  not evidence of disability; avoid unnecessary disclosure and classification.
- **Accessible version parity**: A separate version or mode must provide equivalent content and
  functionality. Distinct styling may expose a selected mode or preference; it does not establish a
  person's disability. Evaluate parity and privacy without making that inference.
- **Volume and audio privacy**: Users who compensate for hearing loss by increasing volume may
  expose private content to others nearby. Interfaces should support caption alternatives and
  headphone-compatible audio to mitigate this.
- **Input method privacy**: Voice control users who speak commands aloud ("click My Medical
  Records") disclose their interaction targets to others in the environment. Screen reader users in
  public spaces face similar exposure. Interfaces that require interacting with sensitive labels by
  voice or that announce sensitive content via screen reader without user-controlled verbosity
  options create privacy risks.

### Bad Prediction

Incorrect autocomplete, smart suggestions, or predictive text can add recovery effort, especially
when suggestions must be navigated sequentially through AT. Evaluate dismissal, workflow
interference, and efficient rejection or override for the access strategies in scope.

## Nielsen's 10 Usability Heuristics — Menu

| #   | Name                                                    | File                     |
| --- | ------------------------------------------------------- | ------------------------ |
| 1   | Visibility of System Status                             | `h1-visibility.md`       |
| 2   | Match Between System and Real World                     | `h2-match.md`            |
| 3   | User Control and Freedom                                | `h3-control.md`          |
| 4   | Consistency and Standards                               | `h4-consistency.md`      |
| 5   | Error Prevention                                        | `h5-error-prevention.md` |
| 6   | Recognition Rather than Recall                          | `h6-recognition.md`      |
| 7   | Flexibility and Efficiency of Use                       | `h7-flexibility.md`      |
| 8   | Aesthetic and Minimalist Design                         | `h8-minimalist.md`       |
| 9   | Help Users Recognize, Diagnose, and Recover from Errors | `h9-errors.md`           |
| 10  | Help and Documentation                                  | `h10-help.md`            |
