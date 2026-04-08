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

## Index

- [Delegate](#delegate)
- [Escalate](#escalate)
- [Signal-first analysis](#signal-first-analysis)
- [Analysis core](#analysis-core)
- [Multi-model comparison](#multi-model-comparison)
- [Deep research](#deep-research)
- [Research core](#research-core)
- [Travel research](#travel-research)
- [Portfolio research](#portfolio-research)
- [Portfolio construction](#portfolio-construction)
- [Blog writing](#blog-writing)
- [Analytical writing core](#analytical-writing-core)

## The control layer

I use a small set of skills as explicit control surfaces. To make that concrete, I am including the safe framework files below as verbatim markdown, with sensitive files omitted.

### Delegate

Source: `skills/delegate/SKILL.md`


````markdown
---
name: delegate
description: Delegate clear, bounded, execution-heavy work to a subagent. Use when the task is straightforward, well-scoped, and mostly about doing rather than deciding, such as file cleanup, formatting, straightforward config edits, conversion, summarization of provided or already-known material, or repetitive but bounded implementation work. Do not use when the task is unclear, risky, research-heavy, reasoning-heavy, or high-stakes. In those cases, use escalate instead.
---

# Delegate

Use this skill for thin, practical handoff.

## Delegate when

- the request is clear enough to pass through with minimal reframing
- the scope is bounded
- the work is mostly execution, not analysis
- mistakes are easy to detect and recover from

Examples:

- clean up or reorganize files
- apply formatting or mechanical edits
- make straightforward config changes
- convert data or file formats
- summarize material that is already provided or already known
- complete repetitive but bounded implementation work

## Do not delegate with this skill when

- the request is ambiguous or underspecified
- the work needs real judgment, deep analysis, or research
- the task is high-stakes, risky, or hard to reverse
- the main job is deciding what to do, not doing it

Use `skills/escalate/SKILL.md` for those cases.

## Workflow

1. Send a brief acknowledgment.
2. Spawn a subagent with:

```text
model: openrouter/xiaomi/mimo-v2-flash
reasoning: true
timeoutSeconds: 3600
```

3. Pass the request with minimal reframing. Preserve the user's wording unless a tiny amount of structure is needed to make the execution target explicit.
4. Yield. Let the subagent return only when the work is complete or clearly blocked.

## Rules

- Keep the handoff short.
- Do not add broad analysis frameworks or extra planning.
- Do not silently upgrade ambiguous or risky work into this path. Use escalate instead.
- Prefer direct execution in the current session when delegation adds no real benefit.
````


### Escalate

Source: `skills/escalate/SKILL.md`


````markdown
---
name: escalate
description: Delegate unclear, risky, reasoning-heavy, research-heavy, or high-stakes work to a stronger subagent. Use when the task needs real judgment, deep analysis, research, coding design, or substantial multi-step reasoning. Do not use for clear, bounded, mostly executional work that fits the delegate skill.
---

# Escalate

Use this path for heavier judgment work.

## Escalate when

- the request is unclear, underspecified, or easy to mis-scope
- the work needs real reasoning, analysis, or research
- the task is high-stakes, risky, or hard to reverse
- the main challenge is deciding what to do, not just doing it

Use `skills/delegate/SKILL.md` instead when the task is clear, bounded, and mostly executional.

## Workflow

1. Send a brief acknowledgment.
2. Spawn a subagent with:

```text
model: openai-codex/gpt-5.4
thinking: high
timeoutSeconds: 172800
```

3. Pass the user request with minimal reframing, and include explicit instruction: "Do not make any changes to files or skills. Only output your proposed framework/options."
4. Yield. Let the subagent return when the work is complete.

## Model Notes

- **github-copilot/gpt-5.4**: Produces thorough, structured analysis with high quality output. Best for deep analysis requiring maximum depth.
- **openrouter/xiaomi/mimo-v2-pro**: Faster alternative, reliable output quality. Use when speed matters.
- **Avoid:** openai-codex/gpt-5.4 (observed reliability issues)

## Rules

- Do not try to do the heavy reasoning yourself first.
- Keep the handoff short.
- If the task is ambiguous or risky, prefer this path over `delegate`.
- Handle only acknowledgments, simple confirmations, greetings, status checks, and simple config commands directly.

## Change approval protocol

When escalating for analysis or design work:

1. **Explicit instruction to subagents**: Include "Do not make any changes to files or skills. Only output your proposed framework/options."
2. **If a subagent proposes a file change**: It must output the proposed content and wait for explicit approval.
3. **Approval required**: The main agent will only execute changes after the user gives explicit go-ahead.
4. **Unapproved changes**: If a subagent makes unapproved changes, the main agent should revert them unless the user approves retroactively.

This ensures that escalations for analysis remain safe and that changes are deliberate.
````


### Signal-first analysis

Source: `skills/signal-first-analysis/SKILL.md`


````markdown
---
name: signal-first-analysis
description: Analyze material by prioritizing evidentiary signal over topical salience. Use when the task is to triage noisy inputs, summarize dense material, classify items against a rubric, compare source quality, separate facts from inferences and unknowns, or support a decision with explicit uncertainty.
---

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
5. Surface contradictions, edge cases, and decision-relevant unknowns early.
6. Deliver the answer in the lightest format that preserves the signal.

## Execution modes

### Triage

- Rank items by evidentiary leverage, not by novelty or how much discussion they generated.
- Lead with the top signals first.
- Cut or collapse low-leverage duplicates.

### Summarization

- Compress repeated points into distinct signals.
- Separate what is established from what is inferred.
- Keep caveats only when they change the takeaway.

### Classification

- State the rubric before classifying.
- Mark borderline cases separately from clean fits.
- Cite the evidence that drove each label.

### Source analysis

- Distinguish primary evidence, authoritative secondary analysis, and commentary.
- Compare scope, freshness, definitions, and failure modes.
- Explain what each source can establish and what it cannot.

### Decision support

- Give the current answer first.
- Name the main alternative and why it lost.
- State the uncertainty that still matters and what would change the answer.

## Notes

- Keep the framework in `methodologies/analysis-core.md`. Do not duplicate it here.
- If the task becomes current, source-heavy, or broad enough to require full research, load `skills/deep-research/SKILL.md` or escalate as appropriate.
- Prefer a simple working table over prose when it makes the distinctions clearer.
````


### Analysis core

Source: `methodologies/analysis-core.md`


````markdown
# Analysis Core

Reusable framework for general analysis: triage, summarization, classification, source analysis, and decision support.

This file owns the analytical structure. Keep task execution patterns in the relevant skills.

---

## 1. Define the analytical question

Write the job in one line:

```text
Question:
Decision or output needed:
Scope:
Hard constraints:
What would change the answer:
```

If the task is not a decision, define the judgment being made anyway. Examples:
- which items matter most
- what this evidence is enough to support
- which category something belongs in
- what the shortest accurate summary is

---

## 2. Optimize for signal, not salience

Rank evidence by **evidentiary leverage**: how much it should change the answer if true.

Prefer:
- direct measurements or primary documents
- falsifying facts and hard constraints
- base-rate setters and bottlenecks
- evidence that changes ranking, scope, or recommendation

Downweight:
- vivid anecdotes
- recent chatter with weak grounding
- repeated paraphrases of the same point
- identity, status, or consensus cues without underlying evidence
- side issues that are interesting but non-decisive

Quick test:

```text
If this item disappeared, would the conclusion materially change?
If this item were false, what would I have to revise?
```

Lead with the few signals that most constrain the answer.

---

## 3. Separate facts, inferences, and unknowns

Use explicit buckets:
- **Facts**: grounded observations or sourced claims
- **Inferences**: what those facts suggest
- **Unknowns**: decision-relevant gaps or unresolved conflicts

Rules:
- Do not mix a fact and an inference in the same bullet or sentence.
- Tie each inference to the specific facts it depends on.
- Promote an unknown only when it could change the answer or next action.

---

## 4. Rank by leverage before expanding

For each item, assess informally:
- relevance to the question
- reliability of the source
- uniqueness versus duplication
- directionality: does it support, weaken, or split the current answer?
- decision impact: would it change the ranking or recommendation?

Then:
- keep the highest-leverage items explicit
- compress corroboration unless independent evidence changes confidence
- cut low-leverage color

---

## 5. Handle contradiction and edge cases

When evidence conflicts, do not average it away. Check whether the conflict comes from:
- scope mismatch
- time mismatch
- definition mismatch
- source-quality asymmetry
- selection effects or base-rate distortion
- a genuine exception that breaks the rule

Edge-case rule:
- If an edge case would change the recommendation for a meaningful subset, elevate it.
- If it is rare and non-decisive, label it and move on.

---

## 6. Compress redundancy

Summaries should expose distinct signals, not repeat the same point from multiple angles.

Compression rules:
- merge duplicate claims into one representative statement
- keep the strongest source or clearest example
- count corroboration separately from novelty
- prefer a short ranked list over a long thematic inventory when the job is prioritization

---

## 7. Make uncertainty operational

Do not stop at "uncertain." Specify:

```text
Unknown:
Why it matters:
Current leaning if forced to act:
What would verify it:
What would change if verified:
```

Default behavior under uncertainty:
- decide now if the remaining uncertainty is low-impact or one-directional
- defer only when the unknown is high-impact and waiting is cheap
- run the cheapest next check when the uncertainty is decision-relevant and reducible

---

## 8. Default output shape

When no other format is required, use:
1. current answer or ranking
2. highest-leverage facts
3. inferences drawn from those facts
4. unknowns and edge cases
5. what would change the answer
6. recommended next action, if any

---

## Revision log
- 2026-04-05: Created to separate reusable analysis structure from execution-oriented analysis skills.
````


### Multi-model comparison

Source: `methodologies/multi-model-comparison.md`


````markdown
# Multi-Model Comparison

Reusable workflow for comparison tasks that use multiple sibling subagents or models.

This file owns the orchestration rule. Keep the task-specific analysis in the relevant methodology or skill.

---

## 1. Define the comparison job

Write the job in one line:

```text
Question:
Models or agents:
Comparison target:
Must-compare dimensions:
Output shape:
```

Be explicit about whether the user wants:
- a synchronized side-by-side comparison
- a merged recommendation after all runs finish
- a baseline plus deltas

---

## 2. Run the requested set

- Spawn the requested subagents or models.
- Wait for the full requested set to complete.
- If one result arrives early and is already usable, treat it as the working baseline.
- Do not wait for perfect symmetry unless the user explicitly asked for it.

---

## 3. Merge immediately once the set is complete

When the requested set has returned:
- compare agreement and disagreement
- isolate the main divergences, not every wording difference
- keep the comparison decision-useful
- deliver one merged result in the same turn

A subagent completion event is a reply trigger. If any complete sibling result is already usable, do not keep saying the task is still waiting. If the user explicitly asked for synchronized comparison, wait for the full requested set and then synthesize immediately when the last sibling completes.

If a sibling result adds only minor detail, fold it in as a delta. Do not restart the comparison loop.

---

## 4. Sort differences by consequence

Prioritize differences that affect:
- the final answer
- confidence level
- what should be imported or changed
- what should stay out

Deprioritize differences that are only stylistic or cosmetic.

---

## 5. Handle partial or missing outputs

If a sibling is missing or blocked:
- use the completed outputs as the baseline
- state the gap clearly
- do not make the user wait for a redundant rerun unless the missing output is likely to change the conclusion

---

## 6. Output shape

When no other format is required, use:
1. consensus
2. key differences
3. practical recommendation
4. any workflow fix or follow-up action

---

## Revision log
- 2026-04-05: Created to encode the multi-subagent comparison workflow and the baseline-first rule.
````


### Deep research

Source: `skills/deep-research/SKILL.md`


````markdown
---
name: deep-research
description: Plan and execute structured, source-grounded deep research on complex topics. Use when the user asks for a deep dive, comprehensive research, multi-facet analysis, or a decision memo that needs current evidence, clear segmentation, and explicit tradeoffs.
---

# Deep Research

Use this skill as a thin entrypoint into the shared research methodology.

## Workflow

1. Capture the minimum decision context:
   - subject
   - scope
   - goal
   - constraints
   - priority signals
   - audience
   - output shape
   
   *For classification and required elements, see `research-core.md` step 1. Classification drives depth; required elements prevent omissions.*
2. Load `methodologies/research-core.md` for the reusable research framework.
3. If the domain has a more specific methodology, load that too.
4. Break the work into coherent segments before going deep.
5. Gather current evidence with grounded sources.
6. If search is rate-limited or times out due to rate limiting, retry with exponential backoff (max N attempts). If retries still fail, stop, document the gap, and use the configured search fallback path.
7. Compare serious options, expose tradeoffs, and name uncertainties.
8. Run the contradiction and completion checks from the methodology before finalizing.

## Domain extensions

Load a domain-specific methodology only when it clearly fits the job.

- Travel work: `methodologies/travel-research.md`
- Portfolio research: `methodologies/portfolio-research.md`
- AI portfolio research: `methodologies/portfolio-research-ai.md` (extends portfolio-research)
- Portfolio construction: `methodologies/portfolio-construction.md` (extends portfolio-research)
- AI portfolio construction: `methodologies/portfolio-construction-ai.md` (extends portfolio-construction)

## Model Configuration

For consistency, reference the escalate skill's configuration as the single source of truth. When spawning a subagent for deep research, use the model and parameters defined in `skills/escalate/SKILL.md` (currently `github-copilot/gpt-5.4` with thinking high).

## Notes

- Do not duplicate the full framework in this skill. The methodology files own the structure.
- Keep execution details local to the relevant domain skill or workspace instructions.
- For heavier research tasks in this workspace, follow the escalation path in `skills/escalate/SKILL.md` when delegation is appropriate.
````


### Research core

Source: `methodologies/research-core.md`

````markdown
# Research Core

Reusable framework for structured, source-grounded research across domains.

This file defines the thinking framework. Keep domain-specific execution details, tool commands, provider-switching steps, and platform URL patterns in the relevant skills.

---

## 1. Define the research job

Capture the minimum decision context before collecting data.

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

### Classification
Classify the work so depth matches the job:
- Exploratory
- Comparative
- Decision-driven
- Comprehensive mapping

### Required elements
List anything that must appear even if it does not emerge naturally.

Rules:
- Treat required elements as constraints, not afterthoughts.
- Spread them across the structure when distribution improves variety or coverage.
- If a required element cannot be satisfied, say so explicitly and explain why.

---

## 2. Segment the space

Break the topic into coherent segments that reduce overlap and make comparison easier.

Possible segmentation axes:
- Geography
- Theme
- Category
- Time period
- Workflow stage
- User type
- Architecture layer

### Segmenting rules
- Pick the axis that best matches the user's actual decision.
- Prefer segments with clear boundaries and low overlap.
- Use enough segments to create choice, but do not force artificial ones.
- If the natural structure is thinner than the target, document target vs actual and explain the limitation.

### Per-segment definition
```text
Segment:
  - Scope:
  - Boundaries:
  - Why it matters:
  - Representative anchors:
```

---

## 3. Collect evidence inside each segment

For each segment, gather:

### A. Segment context
- What the segment covers
- Adjacent or competing segments
- Why it matters to the goal

### B. Anchor items
Research 2 to 4 anchor items when the domain supports it.

For each anchor item, capture:
- Name
- Why it matters
- Key attributes relevant to the decision
- Constraints, caveats, or risks
- Source URLs

### C. Supporting items
Add enough supporting items to create fallback options and comparison depth.

For each supporting item, capture:
- Name
- Key attributes
- Why it is included
- Source URLs

### D. Domain-specific fields
Add only the fields needed for the decision. Examples:
- Travel: distance, access, hours, stroller fit, price
- Product: specs, compatibility, pricing, support
- Academic: thesis, methodology, citation context, limitations
- Technical: architecture, benchmarks, maintenance cost, ecosystem

Do not bloat the framework with domain fields that belong in a specialization.

---

## 4. Compare and narrow

At each decision point:
- Present 2 to 3 serious options when possible
- Show why each option could win
- Show the main tradeoff
- Mark likely keep / maybe / skip paths

### Decision filters
Apply these in order:
1. Priority signals
2. Hard constraints
3. Source quality and freshness
4. Unique value versus overlap
5. Operational practicality

### Iteration loop
1. Present findings
2. Capture feedback
3. Refine without reopening settled questions
4. Keep an audit trail of rejected options and why they lost

---

## 5. Ground every claim

Use a simple source hierarchy:
- Tier 1: official or primary
- Tier 2: authoritative secondary
- Tier 3: community or user signal
- Tier 4: search or aggregator fallback

### Grounding rules
- Prefer direct item URLs over generic search-result URLs.
- Mark weaker grounding clearly.
- If rate-limited, stop, document the gap, and use temporary fallback grounding only where necessary.
- Do not hide uncertainty behind confident prose.

Implementation details for source gathering belong in the skill, not here.

---

## 6. Produce a layered output

### Layer 1: Executive summary
- Subject and scope
- Key findings
- Primary recommendation or takeaway
- Biggest caveat

### Layer 2: Structured detail
- Segment-by-segment findings
- Anchor and supporting items
- Rationale and tradeoffs
- Sources

### Layer 3: Quick reference
- Compact list of key items with links
- Portable enough to use without rereading the full report

---

## 7. Run quality control

### Contradiction check
Before finalizing, test for:
- Conflicting constraints and recommendations
- Number conflicts between targets and requirements
- Scope creep from local rules being stated as universal rules
- Internal inconsistencies in dates, prices, ratings, or terminology

### Assumptions and gaps
Document:
```text
Assumption:
Basis:
Risk if wrong:
How to verify:
```

```text
Gap:
Reason:
Impact:
Mitigation:
```

### Completion check
- The research answers the stated goal
- Priority signals are reflected in the output
- Source quality is visible
- Open uncertainties are named
- The structure matches the user's decision

---

## 8. Specialize cleanly

Use this file as the base layer. Add domain extensions only where they add real decision value.

Examples:
- `methodologies/travel-research.md` extends this with trip definition, geographic clustering, itinerary shaping, and accessibility checks.
- Skills own execution-heavy details such as search tooling, provider switching, exact platform URL formats, and app-specific verification steps.

---

## Revision log
- 2026-04-04: Normalized from the earlier general research methodology into a cleaner reusable core framework.
````

### Travel research

Source: `methodologies/travel-research.md`


````markdown
# Travel Research

Reusable framework for destination research and itinerary design.

This file extends `methodologies/research-core.md` with travel-specific structure. Keep platform mechanics, search-provider changes, and exact URL-format instructions in the relevant active skills or workspace docs, not in this methodology file.

---

## 1. Trip definition

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

### Trip-specific notes
Capture local trip rules here, not in the reusable framework. Examples:
- one child's nap window
- one family's food preferences
- one destination's special cuisine requirement
- one hotel's evening-radius constraint

If a rule only applies to a single trip, store it in that trip's planning files.

---

## 2. Build travel clusters

Travel research usually works best when clustered by geography first.

### Clustering method
1. Start from the lodging base or main anchor point.
2. Map natural activity zones by proximity, theme, or transit pattern.
3. Target slightly more clusters than final day-slots when the destination supports it.
4. Do not force clusters when the geography is compact.
5. Name each cluster clearly enough that someone can navigate by it.

### Per-cluster definition
```text
Cluster:
  - Geography / boundaries:
  - Typical travel time from base:
  - Best for:
  - Anchor attractions:
  - Food and rest options:
```

### Validation
Check:
- Does this reduce transit waste?
- Are the clusters distinct enough to plan around?
- Do they cover the trip's main interests?
- Is the target cluster count being treated as a guideline, not a fake requirement?

---

## 3. Research each cluster

For each cluster, gather:

### Geography and access
- What area the cluster actually covers
- Main entry points
- Transit options
- Walking burden
- Whether it works for the travel group

### Anchor attractions
Research 2 to 4 anchor attractions when the area supports it.

Capture:
- Name
- Why it matters
- Opening pattern
- Cost or booking friction
- Accessibility notes
- Best visit window
- Source URLs

### Food and recovery options
Research enough dining and fallback options to support real planning.

Capture:
- Name
- Cuisine or meal role
- Price band
- Distance from the cluster flow
- Family / stroller / elderly fit when relevant
- Source URLs

### Operational notes
Include only what changes the plan:
- weather sensitivity
- nap compatibility
- indoor backup value
- queue or crowd risk
- terrain difficulty

---

## 4. Cover required experiences deliberately

Travel plans often have must-cover items such as cuisines, attractions, or activity types.

Rules:
- Distribute required experiences across the trip when that improves variety and pacing.
- Do not stack all mandatory items into one exhausted day unless geography forces it.
- If a required item can only be satisfied in one cluster, say so clearly.
- Destination-specific cuisine rules belong in the trip file, not here.

---

## 5. Convert research into day shapes

### Day template
```text
Day / half-day:
  - Primary cluster:
  - Main activity:
  - Meal plan:
  - Backup option:
  - Skip-first item if energy or weather drops:
```

### Good travel outputs should show
- a brief trip summary
- cluster overview
- day-by-day recommendation or option set
- quick-reference list of places and links
- explicit notes for timing, weather, and accessibility

Keep the methodology focused on planning logic. Output formatting details can be adapted to the user's requested format.

---

## 6. Quality control for travel work

Before finalizing, check for:
- impossible transit assumptions
- activities that conflict with the group's pacing
- restaurant choices that break stated food rules
- day plans overloaded with too many anchor items
- late-day activities that conflict with bedtime or return constraints
- destination claims presented as general travel rules

### Assumptions and gaps
Document any item that still needs confirmation:
- hours
- booking status
- seasonal closures
- exact transport practicality
- exact listing URLs when only search-level grounding is available

---

## 7. Ownership boundaries

### Methodology owns
- how to define the trip
- how to cluster the destination
- how to compare areas and day shapes
- how to check pacing, accessibility, and tradeoffs

### Skill owns
- search workflow
- app and platform usage
- provider switching
- exact URL patterns
- verification mechanics

### Trip file owns
- destination-specific rules
- hotel-specific constraints
- family-specific preferences
- one-off cuisine requirements
- final itinerary choices

---

## Revision log
- 2026-04-04: Normalized from the earlier travel research methodology. Removed Foshan-specific cuisine rules, evening strategy, and platform implementation detail from the reusable framework.
````


### Portfolio research

Source: `methodologies/portfolio-research.md`


````markdown
# Portfolio Research Methodology

**Extends:** `methodologies/research-core.md`

---

## Research Job Template

Before starting a portfolio research job, define:

```text
Subject: [Sector/Thesis] portfolio research
Thesis: [Growth/Value/Turnaround/Sector theme]
Thesis Label: [THESIS] (e.g., "AI", "Healthcare", "Renewables")
Scope: [N candidates, time horizon]
Constraints: [Minimum position size, sector limits, etc.]
```

**Example for AI:**
- Thesis Label: `AI`
- This makes `[THESIS]` fields become `AI Revenue`, `AI Exposure %`, etc.

---

## Domain-Specific Fields for Each Anchor Item

### Thesis Exposure Analysis
| Field | Description |
|-------|-------------|
| **Total Revenue** | TTM or FY company revenue |
| **[THESIS] Revenue** | Reported or estimated revenue from thesis theme |
| **[THESIS] Exposure %** | Thesis Revenue ÷ Total Revenue |
| **[THESIS] Revenue Growth YoY** | Year-over-year thesis growth rate |
| **Implied Total Co Growth** | Thesis Revenue × Growth ÷ Total Revenue |

*Example (AI Thesis):*
- Total Revenue: $100B
- AI Revenue: $30B
- AI Exposure %: 30%
- Implied Total Co Growth: 30% × growth rate

### Valuation Context
| Field | Description |
|-------|-------------|
| **Current Price** | Latest trading price |
| **P/E (TTM)** | Trailing twelve months |
| **P/E (Forward)** | Forward earnings multiple |
| **EV/EBITDA** | Enterprise value / EBITDA |
| **Margin Profile** | Gross/operating margin trends |
| **12-mo Price Target** | Analyst consensus target |
| **Upside/Downside** | % change from current price |
| **Intrinsic Value** | Fair value estimate if available |

### Key Metrics
| Field | Description |
|-------|-------------|
| **Backlog/Orders** | Record-breaking orders, book-to-bill |
| **[THESIS] Market Share** | Position in thesis segment |
| **Competitive Moat** | Sustained competitive advantage |
| **Supply Chain Position** | Where company sits in chain |

### Risk Factors
| Field | Description |
|-------|-------------|
| **Concentration Risk** | Revenue dependency on thesis |
| **Regulatory Risk** | Policy, compliance, permitting |
| **Customer Concentration** | Over-reliance on few customers |
| **Cyclicality Exposure** | Commodity or cyclical business drag |
| **Competitive Threats** | New entrants, disruption risk |
| **Execution Risk** | Delivery, scale-up challenges |

---

## Segmentation Axes (Pick 2-3 Per Job)

### 1. Thesis Exposure Level
- **High (70%+)** — Thesis is dominant business driver
- **Medium (30-70%)** — Thesis is significant but not sole focus
- **Low (under 30%)** — Thesis is one growth area among many

### 2. Supply Chain Position (4-Layer Model)
| Layer | Description | Examples by Sector |
|-------|-------------|-------------------|
| **Bottleneck** | Critical IP, scarce resource, high moat | AI: Compute/Memory; Pharma: Patents; Energy: Drilling rights |
| **Infrastructure Enabler** | Physical layers, manufacturing capacity | AI: Cooling/Power; Pharma: Manufacturing; Energy: Pipelines |
| **Platform/Integration** | Systems, distribution networks | AI: Networking; Pharma: Distribution; Energy: Refining |
| **Application/End User** | End-market players, direct exposure | AI: Software/Services; Pharma: Hospitals; Energy: Retail |

### 3. Growth Phase
- **Early** — Nascent market, high uncertainty, large TAM
- **Adoption** — Growing demand, scaling capacity, improving margins
- **Mature** — Stable demand, competitive pressure, margin focus

### 4. Valuation Profile
- **Premium** — High multiple, growth justified
- **Fair** — In-line with sector/peers
- **Contrarian** — Low multiple, thesis reversal potential

---

## Pre-Screening Checks (All Must Pass)

1. **Thesis Exposure Check** — Is thesis revenue exposure meaningful (>20%)?
2. **Scalability Check** — Can thesis growth translate to total company growth?
3. **Cyclicality Check** — Is the non-thesis business stable or a drag?
4. **Valuation Sanity Check** — Does valuation make sense relative to growth?
5. **Backlog/Orders Check** — Do we have forward visibility (>1 year)?

---

## Scoring Adjustments

| Adjustment | Threshold | Effect |
|------------|-----------|--------|
| High Thesis Exposure | Exposure >70% | +10% to score |
| Low Thesis Exposure | Exposure <30% | -5% to score (unless clear expansion path) |
| Strong Backlog | >2 years visibility | +5% to score |
| High Cyclicality | Non-thesis business is cyclical | -5% to score |
| Margin Expansion | Improving margins | +5% to score |
| Regulatory Headwinds | Known regulatory risks | -5% to score |

---

## Portfolio-Level Summary

Include when presenting research:

1. **Thesis Exposure Distribution**
   - Breakdown by exposure level (High/Medium/Low)
   - % of portfolio in each bucket

2. **Supply Chain Coverage**
   - Which layers are represented in the portfolio
   - Gaps or over-concentration

3. **Concentration Checks**
   - Single-stock caps respected?
   - Thesis-level concentration within limits?

4. **Phase Mix**
   - Early vs. Adoption vs. Mature breakdown
   - Alignment with thesis stage

---

## Extension Pattern

To specialize for a specific thesis (e.g., AI, Healthcare, Renewables):

1. Copy `portfolio-research.md` to `portfolio-research-[thesis].md`
2. Replace `[THESIS]` placeholder with the actual label
3. Populate supply chain table with real examples
4. Set thesis-specific thresholds in scoring adjustments
5. Add thesis-specific risk factors if needed

**Example: `portfolio-research-ai.md`**
- Replace `[THESIS]` with `AI`
- Supply chain examples: NVDA, AVGO, VRT, DELL
- High exposure threshold: 70% (vs. 50% for other sectors)
- Add AI-specific risks: supply chain constraints, export controls
````

## Why this works

OpenClaw is useful to me because it makes the invisible work visible.

I can see when I am delegating, when I am escalating, when I am researching, and when I am trying to force a conclusion before the evidence is ready. That gives me leverage. It also gives me a way to improve the system without rewriting everything from scratch.

The model is still important. But the harness decides whether the model is operating inside a clean workflow or a mess.

That is why I care about the structure more than the leaderboard.

And that is why I would rather have a system I can inspect, modify, and leave than a model I can only admire.

### Portfolio construction

Source: `methodologies/portfolio-construction.md`


````markdown
# Portfolio Construction Methodology

**Purpose:** Transform ranked candidates from `portfolio-research.md` into an optimized, risk-managed portfolio

**Extends:** `methodologies/portfolio-research.md`

---

## 1. Position Sizing Framework

### 1.1 Conviction-Tier Sizing

Tie position weight to research score and thesis conviction:

| Tier | Score Range | Position Size | Criteria |
|------|-------------|---------------|----------|
| **Tier 1 (Core)** | 85-100 | 15-20% | Top decile conviction, strong catalyst, clear edge, low idiosyncratic risk |
| **Tier 2 (Strong)** | 70-84 | 8-14% | Solid thesis, acceptable valuation, medium catalyst clarity |
| **Tier 3 (Satellite)** | 60-69 | 3-7% | Promising but unproven, higher uncertainty, exploratory |
| **Watchlist** | <60 | 0% | Do not enter until thesis improves |

### 1.2 Position Sizing Formula

```
Base Size = Tier minimum + (Score - Tier Threshold) × 0.2%
Example: Tier 2 base 8% + (75-70) × 0.2% = 8% + 1% = 9% target
```

### 1.3 Minimum and Maximum Constraints
- **Minimum viable position:** 3% (below this is sub-scale, administrative drag)
- **Maximum position:** 20% (hard cap, requires explicit justification)
- **Single-stock cap:** 20% of NAV
- **Subtheme/cluster cap:** 30% of NAV

### 1.4 Volatility-Adjusted Overlay

Normalize position size by volatility to ensure equal risk contribution:

```
Adjusted Size = Target Size ÷ (Volatility ÷ Portfolio Average Volatility)
```

**Example:** If a position has 2x portfolio volatility, halve its target weight.

### 1.5 Correlation-Aware Sizing

Build correlation matrix for all positions:
- If average pairwise correlation > 0.6, reduce position sizes by 10%
- Cap cluster exposure (e.g., AI hardware layer) at 40% of NAV
- Favor negative/low correlation for diversification benefit

---

## 2. Entry Strategy

### 2.1 Catalyst Requirement

Every entry must have:
- **Near-term catalyst:** Within 0-60 days (earnings, guidance, product launch, regulatory decision)
- **Medium-term catalyst:** Within 3-12 months (capex cycle, market expansion, competitive shift)

**Entry invalidation:** If catalyst timeline extends or disappears, do not enter.

### 2.2 Staggered Entry Protocol

| Tranche | Timing | Trigger |
|---------|--------|---------|
| **Initial (50%)** | Upon entry decision | Price action confirmation or early catalyst signal |
| **Confirmation (25%)** | Upon near-term catalyst hit | Thesis working as expected, price reacting positively |
| **Full position (25%)** | Upon medium-term catalyst or thesis validation | Sustained thesis working, fundamentals improving |

**Alternative:** Full position at entry if thesis is time-sensitive (e.g., pre-catalyst event window).

### 2.3 Entry Invalidation Rules

Do NOT enter if:
- Price-to-fair-value exceeds 1.25x without new information
- Catalyst window closes without entry
- New negative information emerges (competitive threat, regulatory shift)
- Thesis score drops below entry threshold (60)

### 2.4 Technical Entry Filters (Optional Overlay)

- Avoid buying into resistance levels
- Prefer entries near support or on volume confirmation
- Consider macro regime (risk-on vs. risk-off)

---

## 3. Exit Strategy

### 3.1 Tranche Exit for Winners

When position reaches 1.5-2x expected return:
- **Sell 25-33%** to recoup cost basis (free ride)
- **Let remainder run** with trailing stop or new thesis-based target
- **Re-evaluate** if stock rises without fundamental change

### 3.2 Scale-Out Triggers

| Trigger | Action |
|---------|--------|
| **Price target reached** | Trim 25% (consensus + premium) |
| **Thesis invalidated** | Exit 100% (growth/moat/capital returns broken on 2 of 3 dimensions) |
| **Valuation stretched** | Trim 25-50% (P/E > 2σ above historical mean) |
| **Better opportunity exists** | Replace using Total Market charter replacement framework |
| **Catalyst passed** | Re-evaluate; exit if thesis no longer holds |

### 3.3 Thesis Break Rule

**Exit if 2 of 3 thesis dimensions are broken:**
1. Revenue growth decelerating or negative
2. Competitive moat eroding (new entrants, pricing pressure)
3. Capital returns declining (cuts, suspension, misallocation)

### 3.4 Time-Based Review

**Exit review triggers:**
- Quarterly mandatory review regardless of performance
- Monthly if position is Tier 1 (core holding)
- Event-driven on any major catalyst or negative news

---

## 4. Drawdown Management

### 4.1 Per-Position Drawdown Rules

| Drawdown | Action |
|----------|--------|
| **-15% from entry** | Mandatory thesis review within 5 trading days |
| **-20% from entry** | Automatic 50% reduction (must reaffirm thesis within 5 days or full exit) |
| **-30% from entry** | Full exit (thesis likely broken) |

### 4.2 Portfolio-Level Circuit Breakers

| Drawdown from Peak | Action |
|--------------------|--------|
| **-10%** | Halve all new buying, audit all thesis scores, review portfolio concentration |
| **-15%** | Reduce aggregate exposure to 70%, keep only Tier 1 positions at full weight |
| **-20%** | Reduce to 50% cash, pause all buying until trend confirms reversal |

### 4.3 Thesis-Wide Drawdown Protocol

If **all positions in a single supply chain layer** (e.g., Buildout Enablers) drop >15% simultaneously:
- Thesis may be under attack, not just individual names
- Trigger full thesis review
- Consider exiting entire layer

---

## 5. Rebalancing Triggers

### 5.1 Threshold-Based Rebalancing

**Rebalance when:**
- Any position drifts >5% from target weight (absolute, not relative)
- Portfolio drifts >3% from intended allocation

**Action:** Rebalance to target weights, but only if thesis is still intact.

### 5.2 Score-Degradation Rebalancing

When a position's research score drops:
- **Below 70:** Initiate exit review within 48 hours
- **Below 60:** Exit position within 5 trading days

### 5.3 Event-Driven Rebalancing

Immediate re-score and position review on:
- Earnings misses or guidance cuts
- Competitive announcements
- Regulatory decisions
- Major market dislocations

### 5.4 Winner/Loser Management

**Winners:**
- No mechanical rebalancing that sells winners
- Only trim if thesis no longer justifies size (valuation, concentration)
- Let winners run, but enforce concentration caps

**Losers:**
- Do not average down unless thesis is intact AND valuation is below fair value AND no new negative information
- Cut losers decisively when thesis is broken

---

## 6. Portfolio-Level Analysis

### 6.1 Correlation Analysis

**Before finalizing portfolio:**
1. Build pairwise correlation matrix (trailing 1-year returns)
2. Calculate average pairwise correlation
3. Flag if average > 0.6 (reconsider diversification)
4. Identify and cap correlated clusters

### 6.2 Scenario Analysis

For each position, estimate:
| Scenario | Assumptions | Probability | Expected Return |
|----------|-------------|-------------|-----------------|
| **Bull** | Thesis fully plays out, multiple expansion, market grows faster | 20-25% | [Calculate] |
| **Base** | Thesis partially plays out, current multiple, market as expected | 50-60% | [Calculate] |
| **Bear** | Thesis stalls, multiple compression, market disappoints | 15-25% | [Calculate] |

**Portfolio-level stress test:** What happens if all bear cases hit simultaneously? If portfolio drops >30-40%, concentration is too high.

### 6.3 Concentration Scoring

Calculate **effective positions**:
```
Effective Positions = 1 ÷ Σ(Weight²)
```

**Interpretation:**
- 5-7 effective positions = moderately concentrated
- 3-4 effective positions = highly concentrated
- <3 effective positions = extremely concentrated (justify explicitly)

### 6.4 Diversification Benefit Check

For each new position added, ask:
- Does it reduce portfolio volatility?
- Does it provide uncorrelated returns?
- Does it hedge existing exposures?

If no to all three, reconsider the addition.

---

## 7. Portfolio Construction Workflow

### Step-by-Step Process

1. **Research candidates** using `portfolio-research.md`
2. **Rank by risk-adjusted expected return** (not just raw score)
3. **Assign to conviction tiers** based on score
4. **Size positions** using tier sizing + volatility adjustment
5. **Check portfolio-level constraints** (correlation, concentration, liquidity)
6. **Run scenario analysis** (bull/base/bear for each position)
7. **Set exit criteria** for each position before entering
8. **Define rebalancing triggers** (thresholds, events, score changes)
9. **Document portfolio thesis** in one paragraph:
   - What we own
   - Why we own it
   - What would make us sell
10. **Execute staggered entry** per the protocol

---

## 8. Feedback Loop & Post-Mortem

### 8.1 Entry Documentation

At time of purchase, document:
- One-paragraph thesis
- 3 things that would invalidate it
- Expected catalysts and timeline
- Exit criteria (price-based, time-based, thesis-based)

### 8.2 Quarterly Thesis Review

Re-score each position against original thesis:
- Has anything changed?
- Is thesis still valid?
- Does position size still make sense?

### 8.3 Exit Post-Mortem

After every exit (win or lose):
- What worked?
- What didn't?
- What should change in the methodology?

### 8.4 Portfolio Performance Attribution

Analyze monthly:
- Alpha source: stock selection, sector allocation, timing, or luck?
- Track record by conviction tier
- Adjust sizing rules based on results

---

## Appendix: Quick Reference Checklist

### Before Entry
- [ ] Score ≥ 60
- [ ] Near-term catalyst within 60 days
- [ ] Medium-term catalyst within 12 months
- [ ] Position size fits tier constraints
- [ ] Portfolio correlation/cluster check passed
- [ ] Valuation sanity check passed

### At Entry
- [ ] Staggered entry plan defined
- [ ] Exit criteria documented
- [ ] Position assigned to tier and sized accordingly

### Ongoing (Monthly/Quarterly)
- [ ] Thesis review
- [ ] Score check
- [ ] Drawdown check
- [ ] Correlation check
- [ ] Rebalancing check

### Exit Triggers
- [ ] Thesis broken (2 of 3 dimensions)
- [ ] Price target reached
- [ ] Valuation stretched
- [ ] Better opportunity exists
- [ ] Drawdown limits hit
- [ ] Time-based review triggers exit
````


### Blog writing

Source: `skills/blog-writing/SKILL.md`


````markdown
---
name: blog-writing
description: Write, outline, or revise long-form blog posts and articles. Use when the user asks to write a blog post, article, essay for publication, Substack post, or long-form piece. Triggers on phrases like "blog post," "write an article," "help me write," "draft a post."
---

# Blog Writing Skill

## Workflow

### Step 1: Intake

Ask the intake questions from `references/intake-questions.md`. Ask the first 6 by default. Use 7-9 only if needed. Use fallback probes if answers are thin.

Do not proceed to drafting until you have at minimum:
- A one-sentence core claim
- The hidden variable or real mechanism
- At least one personal encounter or real example
- The stakes (why the reader cares)

### Step 2: Load the methodology

Load `methodologies/analytical-writing-core.md` for the analytical framework (hidden variable framing, evidence template, layering staircase, philosophy rules, guardrails).

### Step 3: Load the blog layer

Load `references/blog-post-rules.md` for blog-specific delivery rules (opening reversal, cadence, hammer sentences, compressed ending, final inversion).

### Step 4: Draft the outline first

If the user is still at "rough hunch" or "partial outline" stage, draft an outline before writing full prose. Use the skeleton from `assets/outline-template.md`.

Confirm the outline with the user before proceeding to full draft.

### Step 5: Draft

Write the full post following both the core methodology and the blog layer rules.

### Step 6: Revision

Before delivering the final draft, run through `references/revision-checklist.md`. Fix any issues found.

## Notes

- The core methodology (`analytical-writing-core.md`) works for any analytical format. It is always loaded for blog posts because almost all useful blog posts are analytical.
- The blog layer adds delivery format rules on top. Do not skip it.
- If the user asks for a non-analytical blog post (e.g., a listicle, a how-to guide, a personal narrative), you may skip the core methodology and use only the blog layer. But default to loading both.
- Philosophy is optional. Only include it if the intake reveals a conceptual frame that genuinely clarifies the mechanism.
````


### Analytical writing core

Source: `methodologies/analytical-writing-core.md`


````markdown
# Analytical Writing Core

Reusable framework for long-form analytical writing: essays, memos, reports, explainers, speeches, and analytical blog posts.

This file is loaded by specific writing skills (e.g., blog-writing). Do not duplicate its rules in skill files.

---

## 1. Core Argument Shape

Build the piece around **one central claim**.

State or imply the **common interpretation**, then replace it with a more precise explanation.

Name the **hidden variable** early — the real mechanism, distinction, or factor that actually explains the issue. Reuse the same label throughout the piece. Make it the organizing spine. Do not introduce competing framings unless they serve the same spine.

## 2. Evidence Through Personal Encounter

After naming the mechanism, include one concrete personal encounter, experiment, or observation that validates it.

Structure that section in this order:

1. **Starting assumption** — what I believed before
2. **Setup** — what I tried or observed
3. **Surprising result** — what happened that didn't match expectation
4. **Revised belief** — what I had to change my mind about
5. **Broader lesson** — what this reveals beyond the specific case

Use first person only where it adds leverage:
- Proof (this actually happened)
- Stakes (this matters to me)
- Changed belief (this shifted my thinking)

Do not use personal detail as filler or scene-setting unless it changes the argument.

If you lack a personal experiment, ask for a real example or switch to a case-study mode. Do not invent one.

## 3. Layered Expansion

Expand the argument in a staircase, one layer at a time:

1. **Technical** — what is happening mechanically
2. **User/behavioral** — what that changes for the people affected
3. **Strategic/economic/social** — what that changes at scale

Move outward one layer at a time. Before each transition, make the previous layer legible.

Use hinge phrases that clearly mark expansion:
- "At the technical level..."
- "For users, this means..."
- "Strategically, the consequence is..."
- "There is also an economic dimension..."
- "And this is where the lesson stops being theoretical."

Each layer must answer: **So what changed?**

## 4. Philosophy and Conceptual Framing

Use a philosophical or conceptual reference only if it makes the mechanism clearer. Not as decoration.

Rules:
- Introduce it **only after** the core mechanism is already understandable
- Translate it immediately into plain operational language
- Limit to **one or two references max**
- Apply the **deletion test**: if removing the reference does not weaken the argument, cut it

## 5. Claim Calibration

Make strong claims, but calibrate them honestly. Use calibration phrases when the evidence warrants hedging:
- "my current guess"
- "I think the real shift is"
- "this seems to suggest"
- "the signal I'm tracking is"

This is not mushy hedging. It's honest confidence signaling. The reader should know what you're certain about and what you're still testing.

## 6. Guardrails

- Do not manufacture a contrarian angle if the real argument is additive rather than oppositional
- Do not invent a personal experiment. If you lack one, use a real case study
- Do not use philosophy as decoration
- Do not widen to higher-order consequences until the underlying mechanism is clear
- Cut any paragraph that does not advance one of these jobs:
  - reverse or refine the obvious takeaway
  - define the real variable
  - validate it
  - widen the implications
  - end with a distilled warning or choice
````
