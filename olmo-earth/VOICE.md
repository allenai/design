---
name: Voice and Tone
description: Communication conventions used across user-facing skills.
---

# Voice and Tone

OlmoEarth is the open foundation for planetary intelligence: frontier models and an end-to-end platform that turn raw satellite data into decision-ready insights, and insights into measurable, real-world impact. Built by Ai2, the nonprofit AI institute.

**Tone philosophy: impact is the north star.** Every claim ladders up to a real-world outcome, and every number carries a receipt. Everything below serves that.

## Audience

Voice, audience, and channel are separate dials. Establish the audience before drafting; if it isn't clear, ask. Writing for researchers in an operations register is the most common failure, and it stays invisible until a reader bounces.

| Audience | Who | Cares about | Register |
|---|---|---|---|
| Technical practitioners | ML and Earth-observation researchers, data teams, university labs | Benchmarks, architecture, reproducibility, whether they can build on it | Mechanism-forward. Name the actual cause. They will check anything checkable. |
| Mission organizations | Conservation, climate, and humanitarian orgs | Accuracy, cost, time-to-truth | Operational. What it costs, how often it refreshes, what it replaces. |
| Governments and institutions | Ministries, research institutes, development agencies | Reliable national-scale intelligence on realistic budgets | Institutional. Defensibility and provenance over novelty. |
| Ecosystem and funders | Integration partners, public-good funders, donors | Integration paths, public-good impact, a credible roadmap | Systems-level. Where our layer ends and theirs begins. |

Inside these audiences are two people to keep in mind:

- **The ML expert.** Wants every knob and a direct comparison to alternatives. Point at a working example, not documentation, and be explicit about deployment.
- **The data scientist at a small NGO.** Medium-high GIS, low ML. Lead with what they will see, not how it works. Define every term. Never assume a code path.

Data quality gates are harder than ML fluency. Pitch accordingly.

Copy aimed at people who build on OlmoEarth with no relationship to us should assume no contact ever happens: everything they need must be in the public materials.

## Voice

Technically fluent, confidently open. These traits do not change across contexts.

1. **Lead with specifics.** Numbers over adjectives: benchmarks, accuracy, hectares, days-to-map. If a claim has a figure behind it, use the figure.
2. **Flex the full platform.** Not just models: the end-to-end system from raw satellite data to decision-ready insights, refreshed as conditions change. The platform is the differentiator; the models are one layer.
3. **Frontier, without hype.** State-of-the-art is a measured claim. Every "best" points to the benchmark or technical report that proves it.
4. **Open by default.** Open weights, open training data, nonprofit mission. Invite inspection.

### Don't say / Do say

| Do say | Don't say | Why |
|---|---|---|
| "OlmoEarth leads every model we benchmarked against — see the technical report." | "OlmoEarth is revolutionary AI for the planet." | Claims carry receipts. |
| "An end-to-end platform: from data acquisition through fine-tuning to production deployment." | "A satellite imagery model." | The platform is the differentiator. |
| "Fully open: weights, training data, and code you can inspect and adapt." | "Free to use." | "Free" undersells what open enables. |
| "Global Mangrove Watch is seeing ~97% accuracy with processing time cut in half." | "Partners love OlmoEarth." | Named partners with numbers do the persuading. |
| "Frontier performance at every size." | "Smaller than GPT-scale models." | Define the frontier on Earth-data terms, not LLM terms. |

### The three-beat item

Build each item on three beats:

1. **Capability.** First line, present tense, product as subject, number in the first clause.
2. **Mechanism.** One sentence naming the actual cause. Don't simplify it into vagueness.
3. **Impact.** Who it changes something for: the place, the partner, the result.

Weak: "We're excited to announce enhanced vectorization capabilities! Predictions can now be converted into vector formats."

Strong: "**Raster predictions can now come out as polygons.** Simplify tolerance is set in pixels rather than map units, so one config behaves the same at the equator and at 60° north. A deforestation briefing needs a boundary, a concession, a parcel, a road corridor, not a grid of pixels."

When space is short, keep capability plus impact for a tweet or newsletter item; keep capability plus mechanism for a deep dive. Impact is the first beat cut under length pressure, so decide deliberately. When a release ships as a thread, blog, and changelog, write the mechanism sentence once and reuse it verbatim, then confirm impact appears somewhere in the bundle.

Work that can't honestly reach a named outcome (a queue migration, an autoscaling change) belongs in the engineering blog, not in impact-framed copy. Don't stretch it.

## Plain language

- Sentence case for titles and subheads.
- Oxford comma, always.
- pretrain, post-train, fine-tune.
- multimodal, datasets, codebase: one word each.
- open source, not open-source.
- Use platform terms consistently. "Temporal context window" is the agreed platform-wide term. When a term is still unsettled, define it in place rather than assuming it.
- Don't concede the frame that embeddings do it all, and don't dismiss it either. Embeddings are half the story; fine-tuning is where quality lives for precision work.
- Defer to the Ai2 style guide where it is settled.

## Honesty & confidence

- **Never invent, estimate, or round a figure.** Check every number and partner outcome against its source. If a needed number isn't available, leave a marked placeholder.
- **Hedge the magnitude, never the evidence.** "A modest improvement, consistent across all four sizes on our kNN and linear-probe evaluations, with per-size numbers in the technical report." A small number is still a number; an adjective is not.
- **Attribute demand.** "Partners asked for it" is the same failure as "partners love OlmoEarth." Name one, or name what was breaking for them.
- **No hype adjectives standing in for evidence.** "Best," "leading," and "state-of-the-art" each point at a named benchmark or the technical report.
- **No competitor comparisons** that aren't in a published document.
- **Don't credit new work with old results.** Never imply a newly shipped capability produced a partner's past result.
- **Don't promise access the reader doesn't have.** Studio is no-cost but partner-only; the open path is weights, the public repos, and the Viewer.
- **Internal-only claims stay internal**, whatever the framing.

The final test: would this survive a skeptical ML researcher's read? If a claim would send that reader looking for the source, the source is already in the copy.
