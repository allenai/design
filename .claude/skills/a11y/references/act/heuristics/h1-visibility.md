# 1. Visibility of System Status

**Definition**: The design should always keep users informed about what is going on, through
appropriate feedback within a reasonable amount of time.

**Accessibility Lens**: Users who cannot see visual feedback — colour changes, spinners, progress
bars — need their assistive technology to surface the current system state so they understand what
is happening. After a user activates a control, the interface must communicate the outcome through
whatever channel the user relies on; if nothing is communicated, this heuristic is violated. Also
consider timing: a slow or absent response leaves the user uncertain whether their action
registered. If the system is processing, the user must know — a captive wait with no feedback is
worse than a slow response with a clear progress indication. Feedback must be timely, not just
present.
