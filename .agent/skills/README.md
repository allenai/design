# Agent skills

Portable, agent-agnostic **skills** for this repository — reusable task
instructions that any coding agent (Claude, Cursor, Copilot, Gemini, or
homegrown tooling) can discover and follow.

Skills here are intentionally *not* stored under `.claude/`, `.cursor/`, or any
vendor-specific location, and they never name a specific agent's tools. They
follow the same philosophy as this repo's `DESIGN.md` files: self-contained,
plain-text, and readable by any tool that cares to look.

## Available skills

### Ai2 comms

A suite for **outbound Ai2 communications** — launch blogs, newsletters, social
posts, research amplification. They cross-reference each other; read whichever
matches the task, and follow the sibling references it names.

| Skill | Use it for |
| --- | --- |
| [`ai2-comms-style-source`](ai2-comms-style-source/SKILL.md) | Voice, source fidelity, claims discipline, approval gates, house style. The reference hub the others build on — start here if you read only one. |
| [`ai2-comms-launch-engagement`](ai2-comms-launch-engagement/SKILL.md) | Pre-draft release planning: arc placement, demo scope, asset staging, partner roles, audience, follow-up beat. |
| [`ai2-comms-writer`](ai2-comms-writer/SKILL.md) | Drafting and revising copy. |
| [`ai2-comms-structure-lector`](ai2-comms-structure-lector/SKILL.md) | Reviewing framing, openings, section order, redundancy. |
| [`ai2-comms-claims-lector`](ai2-comms-claims-lector/SKILL.md) | Reviewing factuality, attribution, benchmark scope, approval-sensitive claims. |
| [`ai2-comms-chart-designer`](ai2-comms-chart-designer/SKILL.md) | Benchmark charts, leaderboard tables, explanatory diagrams. Reads tokens from the product `DESIGN.md` files. |
| [`ai2-comms-channel-adapter`](ai2-comms-channel-adapter/SKILL.md) | Adapting cleared copy for X, LinkedIn, Reddit, Discord, Bluesky, Hugging Face, newsletters. |
| [`ai2-comms-pipeline`](ai2-comms-pipeline/SKILL.md) | Running a whole task end to end through the phases above. |

Typical flow: `launch-engagement` → `writer` → `structure-lector` and
`claims-lector` → `chart-designer` → `channel-adapter`. Any phase can be entered
directly.

**Comms voice is not product voice.** These skills cover what Ai2 says *about* a
product. What a product says to its own users lives in that product's
`VOICE.md` (`strata/VOICE.md`, `asta/VOICE.md`, `olmo-earth/VOICE.md`). Neither
overrides the other.

**Approval gates are categorical here.** `ai2-comms-style-source` describes the
*kinds* of claim that need clearance before publication. The current roster of
specific gated partners, deployments, and customers is maintained by the Ai2
comms team and is deliberately not recorded in this public repository.

**Worked examples are limited to published copy.** Two full examples ship —
`newsletter-example.md` and `sunset-example.md` — both drawn from copy that is
live. The remaining genres are described in `worked-shapes.md` as transferable
moves rather than reproduced, so this repository carries no unpublished Ai2
drafts.

### Working-tree checkpoints

| Skill | Use it for |
| --- | --- |
| [`ai2-checkpoint`](ai2-checkpoint/SKILL.md) | Saving, listing, comparing and restoring local snapshots of the working tree, kept apart from git commits — so there is always a "before" to diff against or roll back to around big changes. Ships the small `checkpoint.py` tool the skill drives. |

## Layout

Each skill is a directory containing a `SKILL.md`, plus any supporting files it
needs (scripts, templates, reference docs):

```
.agent/skills/
  README.md                  ← this file (the convention)
  <skill-name>/
    SKILL.md                 ← required: frontmatter + instructions
    ...                      ← optional supporting files, referenced by SKILL.md
```

- The directory name **is** the skill name: lowercase `kebab-case`, matching the
  `name` field in the frontmatter.
- One skill per directory. Keep each skill narrowly scoped to a single task.

## `SKILL.md` format

YAML frontmatter followed by markdown instructions:

```markdown
---
name: <kebab-case-name>          # required — matches the directory name
description: <one line>          # required — what the skill does + when to use it,
                                 #   written so an agent can decide relevance
version: 0.1.0                   # optional — semver
keywords: [design, tokens]       # optional — aids discovery/matching
---

# <Human-readable title>

Step-by-step instructions the agent should follow to accomplish the task.
Write for *any* agent: describe intent and outcomes, not a specific tool's API.
```

### Authoring rules

- **Agent-agnostic.** Don't reference a specific agent's tool names, slash
  commands, or config files. Describe *what* to do, not *which button to press*.
- **Self-contained.** A skill should stand alone. Inline the guidance an agent
  needs rather than assuming other context is loaded.
- **Repo-relative paths.** Reference files like `strata/DESIGN.md` or
  `spec-sheet.html` by their path from the repo root — never absolute machine
  paths.
- **Normative on tokens.** For anything touching colors, type, or components,
  point at the relevant `DESIGN.md` as the source of truth (see the root
  `CLAUDE.md` for the product → file mapping). Don't restate token values that
  belong in `DESIGN.md`.
- **Plain text.** Markdown only, no binary or vendor-proprietary formats, so the
  file is portable and diff-friendly.

## Discovery

Any agent can be pointed at this directory. Some examples of how a given tool
might surface these skills:

- Reference `.agent/skills/` from that agent's own config/instructions file
  (e.g. a `CLAUDE.md`, Cursor rule, or system prompt) so it reads the relevant
  `SKILL.md` before starting a matching task.
- Symlink or copy a skill into a vendor-specific location if a tool only scans
  its own folder.

The `name` + `description` frontmatter is what an agent reads first to decide
whether a skill applies, so keep the description concrete about *when* to use it.
