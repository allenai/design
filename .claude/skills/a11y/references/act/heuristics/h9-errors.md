# 9. Help Users Recognize, Diagnose, and Recover from Errors

**Definition**: Error messages should be expressed in plain language (no error codes), precisely
indicate the problem, and constructively suggest a solution.

**Accessibility Lens**: Error messages must be visually and semantically associated with the fields
they relate to so that assistive technology users can find which field has the error and understand
what to fix. When errors appear, the user must be made aware of them — errors that are only
indicated visually (such as a colour change or border) communicate nothing to users who cannot see
them. Dynamically appearing validation messages must be surfaced to all users, and an error summary
should help the user navigate directly to each problem. Beyond error messages, consider whether user
work is preserved during error recovery: if a form submission fails, is the user's input still
present, or must they re-enter everything? Data loss during error recovery is a compounding failure
— the original error plus the lost work. For users who invested significant effort entering data
sequentially through assistive technology, this is especially costly.
