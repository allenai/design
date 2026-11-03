---
name: ai2-checkpoint
description: "Save, list, compare and restore local checkpoints of the working tree — snapshots the user can look back at to see how things changed, kept apart from git commits. Use when the user asks for a checkpoint, snapshot or save point; asks what changed since earlier, to compare with before, or how a file looked before; or wants to go back to an earlier state. Also use it unprompted: save a checkpoint before and after any big change — a multi-file refactor, an agent fan-out, a revert, a formatting pass, each stage of a page build — so there is always a 'before' to compare against."
version: 1.0.0
keywords: [checkpoint, snapshot, undo, diff, restore, git]
---

# Checkpoint

People want to see how things changed when the work moves in big steps, and to go back when a step was wrong. A checkpoint is a snapshot of the whole working tree — tracked edits and new files alike, minus what `.gitignore` excludes — that can be listed, diffed and restored later.

It is **not a commit.** Saving one never stages, commits or pushes anything, so any rules the user has about committing still hold. Checkpoints live under `refs/checkpoints/<branch>` (the mechanism `git stash` uses), never appear in `git log`, `git status` or a push, and go away with `clear`.

The tool, run from anywhere inside the repo (the script lives next to this file — substitute this skill's base directory):

```
python3 <skill dir>/checkpoint.py <command>
```

| Command                | Does                                                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `save -m "label"`      | Snapshot now. A no-op when nothing changed since the last one.                                                                                              |
| `list`                 | This branch's checkpoints — id, when, label, what changed from the previous one — and whether the tree has moved on since the last.                          |
| `diff A [B]`           | What changed between two points, as a file list with +/− counts. `B` defaults to `now`. Add `-p` for the full patch, `-- path` to narrow it.                |
| `show ID [path]`       | A checkpoint's summary, or one file exactly as it was then.                                                                                                 |
| `restore ID [paths]`   | Make the tree (or just those paths) match a checkpoint. Saves a checkpoint first, so it is always undoable.                                                 |
| `clear [--all]`        | Drop this branch's checkpoints (or every branch's).                                                                                                         |

Ids: `cp3` or `3` (oldest first), `last`, `now`, or any git revision (`HEAD`, `main`, a sha).

## When to save

Save unprompted — that is what makes the history exist when the user wants to look back:

- **Before and after a big change.** Big means: touching more than a few files, a refactor or rename, a formatting pass, a revert, an agent fan-out (save before launching, again when the results are in), anything you'd describe with "rewrote" or "restructured".
- **At stage boundaries** of a long build — after the scaffold, after each section or chapter lands, before the audit.
- **When the user asks**, with their words as the label.

A label is a few words naming the state, in the user's terms: `"theorizer: empty shell"`, `"header bar in"`, `"before agent fan-out (t2–t5)"`. Not "wip", not a timestamp. Report a save in one line — `Saved cp4 — header bar in` — not a paragraph.

Don't save after every small edit. `list` should read like a table of contents, not a keystroke log.

## When the user asks what changed

1. `diff A B` for the shape; `diff A B -p` (narrowed with `-- path` when the list is long) to read the changes yourself. `B` defaults to `now`: "since cp3" usually means "compared with what's on disk".
2. Say in plain words what moved — which files, what they do now that they didn't — before showing any diff. Point at the few hunks that matter; don't paste the whole patch unless asked.
3. Offer the next step: `show ID path` to see a file as it was, `restore ID path` to take one file back.

## Restoring

- A full `restore` rewrites the tree: confirm first unless the user asked for exactly that ("go back to cp2", "undo all of that"). Restoring one or two files they named needs no confirmation.
- Say what it did (`n files written, m removed`) and that the pre-restore checkpoint undoes it.
- Afterwards, reload whatever is watching the files (the browser pane, a dev server) so the user is looking at the restored state.
- Never `clear` without being asked. It is the user's undo history.

## Optional: a checkpoint every turn

For checkpoints nobody has to remember, agents that support lifecycle hooks (e.g. Claude Code's `Stop` hook in `settings.json`) can save one at the end of every turn in which files changed — `--auto` is silent when nothing changed and never fails:

```json
{
    "hooks": {
        "Stop": [
            {
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 <skill dir>/checkpoint.py save --auto -m \"end of turn\""
                    }
                ]
            }
        ]
    }
}
```

Only install it when the user says so; it is a global change to how every session behaves.
