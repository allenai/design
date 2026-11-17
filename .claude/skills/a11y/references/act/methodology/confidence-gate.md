# Confidence Gate

If you are uncertain about a component's purpose or behavior (e.g., whether an element is
interactive or informational, whether it is a selector or a data display, what charting library it
uses, or how it responds to keyboard input), do NOT assert a finding based on your assumption.

Instead:

- Report the uncertainty as a question, note, or manual check with a clear description of what needs
  verification.
- NEVER build a finding on top of an unverified assumption about component behavior. If the finding
  would collapse if the assumption were wrong, it does not belong in confirmed findings.

The appropriate way to record an uncertain item depends on the evaluation context the consumer
defines — for example, a deferred verification step, a question back to a stakeholder, or a manual
check. Whatever the mechanism, the uncertain item must be kept clearly separate from confirmed
findings until it is resolved.

High-confidence findings should survive scrutiny; uncertain observations should be explicitly
labeled as such.
