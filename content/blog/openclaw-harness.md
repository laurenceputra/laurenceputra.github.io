---
title: "How I Use OpenClaw"
description: "A technical overview of the harness layer I actually rely on for analysis, writing, and research."
date: 2026-04-08
slug: openclaw-harness
tags: ["OpenClaw", "AI", "harness", "workflow", "research"]
noindex: true
sitemap:
  disable: true
---

OpenClaw is not a chatbot to me. It is the workflow spec for how I want an AI system to behave when the work matters.

The model answers. The harness decides what the model sees, how work gets split, when I stop, and what I trust.

That difference is the whole point.

## The control layer

I use a small set of skills as explicit control surfaces. They keep the system from collapsing into one giant prompt.

### Delegate
When the work is bounded, I do not need a grand theory. I need a clean handoff.

```text
---
name: delegate
description: Delegate clear, bounded, execution-heavy work to a subagent. Use when the task is straightforward, well-scoped, and mostly about doing rather than deciding, such as file cleanup, formatting, straightforward config edits, conversion, summarization of provided or already-known material, or repetitive but bounded implementation work. Do not use when the task is unclear, risky, research-heavy, reasoning-heavy, or high-stakes. In those cases, use escalate instead.
---

# Delegate

Use this skill for thin, practical handoff.
```

That is the right tool when the problem is execution, not judgment.

### Escalate
When the work gets ambiguous, risky, or genuinely reasoning-heavy, I switch to the stronger path.

```text
---
name: escalate
description: Delegate unclear, risky, reasoning-heavy, research-heavy, or high-stakes work to a stronger subagent. Use when the task needs real judgment, deep analysis, research, coding design, or substantial multi-step reasoning. Do not use for clear, bounded, mostly executional work that fits the delegate skill.
---

# Escalate

Use this path for heavier judgment work.
```

That keeps uncertain work from being forced through a thin execution slot.

### Signal-first analysis
Before I expand an answer, I want to know what actually matters.

```text
# Signal-First Analysis

Use this skill as the execution layer for general analysis tasks. Load `methodologies/analysis-core.md` for the reusable framework.

## Workflow

1. Capture the job in one line:
   - question or decision
   - scope
   - output shape
   - hard constraints
2. Load `methodologies/analysis-core.md`.
3. Pick the execution mode that matches the task.
4. Build only the minimum working structure needed: a ranked list, a facts / inferences / unknowns table, a rubric, or a source comparison.
```

That is how I keep analysis from turning into topic drift.

### Multi-model comparison
When the question is comparative, I want the comparison framed before anyone starts improvising.

```text
Question:
Models or agents:
Comparison target:
Must-compare dimensions:
Output shape:
```

That keeps model choice from becoming a vibe contest.

## The analytical spine

The deeper structure lives in the reusable analysis and research files. These are the documents that keep me from reinventing the same thinking loop every time.

### Analysis core

```text
Question:
Decision or output needed:
Scope:
Hard constraints:
What would change the answer:
```

```text
Use explicit buckets:
- Facts: grounded observations or sourced claims
- Inferences: what those facts suggest
- Unknowns: decision-relevant gaps or unresolved conflicts
```

That is the basic discipline. Separate what is known from what is inferred.

### Research core

```text
Subject:
Scope:
Goal:
Constraints:
Priority signals:
  - Always include:
  - Always avoid:
Audience:
Output shape:
```

```text
## 7. Run quality control

### Contradiction check
Before finalizing, test for:
- Conflicting constraints and recommendations
- Number conflicts between targets and requirements
- Scope creep from local rules being stated as universal rules
- Internal inconsistencies in dates, prices, ratings, or terminology
```

That is the research version of the same habit. Define the job, segment the space, then check for contradictions before I trust the result.

### Deep research
The deep research skill is a thin entrypoint. The real work lives in the research framework.

```text
1. Capture the minimum decision context:
   - subject
   - scope
   - goal
   - constraints
   - priority signals
   - audience
   - output shape
2. Load `methodologies/research-core.md` for the reusable research framework.
3. If the domain has a more specific methodology, load that too.
4. Break the work into coherent segments before going deep.
5. Gather current evidence with grounded sources.
```

That is the line between asking and researching.

## The writing spine

I use the same harness logic for writing. Good writing is not just prose. It is a controlled sequence of constraints.

### Abstracted writing system

```text
Every persuasive piece follows this four-phase arc. The phases are structural; the execution varies.

Phase 1: Concede
Phase 2: Reclassify
Phase 3: Compress
Phase 4: Moralize
```

That is the skeleton for most of my longer argument pieces.

### Analytical writing core

```text
Build the piece around one central claim.

State or imply the common interpretation, then replace it with a more precise explanation.

Use first person only where it adds leverage:
- Proof (this actually happened)
- Stakes (this matters to me)
- Changed belief (this shifted my thinking)
```

That keeps the writing honest. No filler. No fake narrative.

### Blog writing

```text
### Step 1: Intake

Ask the intake questions from `references/intake-questions.md`. Ask the first 6 by default. Use 7-9 only if needed. Use fallback probes if answers are thin.
```

```text
### Step 4: Draft the outline first

If the user is still at "rough hunch" or "partial outline" stage, draft an outline before writing full prose. Use the skeleton from `assets/outline-template.md`.

Confirm the outline with the user before proceeding to full draft.
```

That is the same idea again. Do not draft until the structure is real.

## The domain modules

The same pattern extends to travel and portfolio work. I do not treat those as special cases. They are just different decision spaces.

### Travel research

```text
Destination:
Dates:
Base(s):
Travelers:
Transport model:
Budget guardrails:
Pacing:
Accessibility needs:
Priority signals:
  - Always include:
  - Avoid:
Required experiences or cuisine types:
```

That keeps trip planning grounded in real constraints instead of wishful itineraries.

### Portfolio research

```text
Subject: [Sector/Thesis] portfolio research
Thesis: [Growth/Value/Turnaround/Sector theme]
Thesis Label: [THESIS] (e.g., "AI", "Healthcare", "Renewables")
Scope: [N candidates, time horizon]
Constraints: [Minimum position size, sector limits, etc.]
```

That is enough structure to research a thesis without drowning in noise.

### Portfolio construction

```text
Purpose: Transform ranked candidates from `portfolio-research.md` into an optimized, risk-managed portfolio

Extends: `methodologies/portfolio-research.md`
```

```text
| Tier | Score Range | Position Size | Criteria |
|------|-------------|---------------|----------|
| Tier 1 (Core) | 85-100 | 15-20% | Top decile conviction, strong catalyst, clear edge, low idiosyncratic risk |
| Tier 2 (Strong) | 70-84 | 8-14% | Solid thesis, acceptable valuation, medium catalyst clarity |
| Tier 3 (Satellite) | 60-69 | 3-7% | Promising but unproven, higher uncertainty, exploratory |
| Watchlist | <60 | 0% | Do not enter until thesis improves |
```

That is the part people miss. The research does not end with an opinion. It ends with a position size.

## What I keep private

I keep the following out of the public layer:

- credentials and tokens
- account IDs and private URLs
- live portfolio state
- deployment wiring
- private group or channel details
- anything that would let someone reconstruct current execution instead of the framework

That line matters. The point of sharing the harness is to share the method, not the keys.

## Why this works

OpenClaw is useful to me because it makes the invisible work visible.

I can see when I am delegating, when I am escalating, when I am researching, and when I am trying to force a conclusion before the evidence is ready. That gives me leverage. It also gives me a way to improve the system without rewriting everything from scratch.

The model is still important. But the harness decides whether the model is operating inside a clean workflow or a mess.

That is why I care about the structure more than the leaderboard.

And that is why I would rather have a system I can inspect, modify, and leave than a model I can only admire.
