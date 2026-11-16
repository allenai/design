# Figma: ER Design System

File key `gQJAI5XKeENQsqkCaFBev3`. URL: `https://www.figma.com/design/gQJAI5XKeENQsqkCaFBev3/ER-Design-System`.

Load the `figma:figma-use` skill before any `use_figma` call. Load `figma:figma-generate-library` too when creating variables. Call `create_session` with the file key first, and reuse its id.

Node ids below were correct on 2026-11-16. Find things by name if an id no longer resolves.

## Where things are

| What | Where |
| --- | --- |
| Spec sheets | Page **Color** (`102:2`). Sections: `EarthRanger Spec Sheet — Color Tokens- <M/D/YY>` (visible one is current; older dated ones hidden) and `Legacy Spec Sheet — Color Tokens`. There is also a `Button translation` section there. |
| Semantic variables | Collection **Tokens** (`VariableCollectionId:2717:1095`), modes `Light`, `Dark`, `Legacy Light`, `Legacy Dark`. Groups: `UI/Background`, `UI/Text`, `UI/Icons`, `UI/Field Outline`, `UI/Divider Lines`, `UI/CTA Primary`, `UI/CTA Secondary`, `UI/CTA Text`, `UI/Status`, `UI/Status Bg`, `UI/Patrol Status`, `UI/Event Priority`, `UI/Data`, `Brand/…`. |
| Primitives | Collection **Primitives** (`VariableCollectionId:2550:971`), one mode `HEX`. Names like `Greyscale/0`…`Greyscale/11`, `Blue/1`…, `Teal/1`…, `Red/…`. Figma's names don't match DESIGN.md's (`greyscale-9` is `Greyscale/9`, but teal ramps differ). Match by hex value, not by name. |
| Platform fonts | Collection **Platform**, modes `Web Fonts`, `Windows`, `iOS`, `Android`. |
| Text styles | 38 local text styles (e.g. `Pre-rebrand/Web-H1`). No paint (colour) styles exist. |
| Disabled button reference | Buttons page, node `6632:429`. |

## Variables

1. Read first: list the group the token lives in, with each mode's value, resolved through aliases.
2. For a new semantic token:
   - create it in **Tokens** with the exact DESIGN.md name;
   - scope it to what it's for (`FRAME_FILL`, `SHAPE_FILL` for backgrounds; `TEXT_FILL` for text; `STROKE_COLOR` for outlines);
   - set each mode with `figma.variables.createVariableAlias(primitive)`, not a raw colour.
3. If the needed primitive isn't in **Primitives**, add it, following the ramp's naming, and tell the user.
4. Read back: return every mode's alias target name and hex.

## Spec sheet

1. Find the visible section for the system by name prefix. Duplicate it, then place the copy to the right of the current one, clear of other nodes.
2. Rename the copy with today's date in the same format (`- 11/16/26`). The Legacy sheet has no date in its name yet. Add one the same way, as the team agreed on 2026-11-16.
3. Add or change the row:
   - copy a sibling row (same group) so layout, fonts and labels match;
   - bind the swatch fill to the variable (`setBoundVariableForPaint`);
   - update the label text, loading its fonts first.
4. Hide the previous section (`visible = false`).
5. Screenshot the new section and show the user.

## Publishing the library

Publishing can't be done through the Plugin API. Walk the user through it one step at a time, waiting after each:

1. In the ER Design System file, open the **Assets** panel (left sidebar).
2. Click the **Libraries** (book) icon.
3. Next to this file, click **Publish…**. Figma lists the changed variables and styles.
4. Check the list contains only this change, add a short description (e.g. "Add UI/Background/Disabled"), and click **Publish**.

If the list shows changes you didn't make, someone else has unpublished edits. Stop and let the user decide before publishing them along with yours.
