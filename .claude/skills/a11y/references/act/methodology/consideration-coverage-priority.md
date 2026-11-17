# Consideration Coverage Prioritization

When full evaluation is not practical, prioritize access considerations by the interface and task,
not by ranking disability communities or comparing people with a default user.

## Prioritization dimensions

### 1. Task-contextual interaction differences

Compare the input and output methods relevant to the interface. A change in access strategy may
expose a different dependency, such as a drag-only action without keyboard operation or a visual
chart without programmatic information.

Shared strategies are reusable reference material, not a default person's capabilities. An excluded
shared strategy marks a document's evaluation scope, not a person's limitations.

### 2. Likely barriers for the UI type

Use documented patterns to select checks, then verify the actual interface:

- Custom widgets: keyboard operation, focus order, and programmatic names, roles, and states.
- Dense layouts: magnification, reflow, contrast, and spatial context.
- Charts and status indicators: alternatives to colour cues and nonvisual information.
- Dynamic content: focus management, live regions, and status messages.
- Media and conferencing: captions, sign language options, audio clarity, and communication
  alternatives, according to the task and expressed access needs.
- Multi-step flows: memory and attention demands, language comprehension, numeracy, time limits, and
  error recovery.

These are prompts for investigation, not proof that a particular interface contains a barrier.

### 3. Coverage breadth

Cover a range of input methods, output channels, devices, AT configurations, and task demands.
Several documents may overlap, and one person may use strategies from multiple documents. Do not
equate checking one document with representing an entire community.

## How to apply

1. List the access topics relevant to the interface and evaluation scope.
2. Identify dependencies that change when input, output, or task conditions change.
3. Prioritize core-task blockers and high-risk interaction patterns.
4. Use breadth across access strategies as a tiebreaker when risks are comparable.
5. Record evaluated and omitted topics, the reason for prioritization, and uncertainty.

## Examples

| Interface          | Candidate priorities                                                                               | Why                                                                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Complex form       | Keyboard interaction, voice control, visual adaptation, alternatives to colour cues                | Verify focus and activation, visible-label/accessible-name matching, reflow and error proximity, and non-colour validation feedback.                         |
| Data dashboard     | Alternatives to colour cues, nonvisual access, visual adaptation, pointer and keyboard interaction | Examine series differentiation, programmatic data alternatives, contrast/reflow, and alternatives to hover and dragging.                                     |
| Video conferencing | Audio alternatives, audio adaptation, keyboard interaction, voice control, visual adaptation       | Examine communication without hearing, audio clarity and supplementary cues, reachable controls, label-based activation, and visibility under magnification. |

These are starting points, not fixed priority rankings. Include cognition, language, numeracy, or
other considerations when the task demands them. Findings should identify interface requirements and
possible barriers; co-design and testing with people with disabilities remain necessary.
