---
title: "Delete Yesterday's AI Scaffolding"
description: "As models improve, the next productivity gain may come from removing yesterday's prompts and orchestration without removing the controls that protect judgment."
date: 2026-07-23
draft: true
tags: ["AI", "architecture", "agents", "systems", "judgment"]
aliases: ["/blog/delete-yesterdays-ai-scaffolding/"]
---

<!--
Working outline, not a finished post.
The Reddit example is based on a screenshot supplied by Laurence. Treat the figures as source-reported observations, not as an independently verified benchmark.
-->

## Core claim

As models improve, the next AI productivity gain may come from deleting yesterday's scaffolding rather than adding more prompts. Good AI architecture is adaptive: keep the controls that preserve safety, approval, provenance, and verification, while removing instructions, plugins, and orchestration that no longer earn their token cost.

## The opening reversal

The obvious takeaway from a new model release is that we should add more capability around it: more prompts, more routing, more memory, more agents, more automation.

The reversal: a stronger model can make an old AI system worse if the system still carries scaffolding built for a weaker model. The added instructions may now be redundant, consume context, compete for attention, and increase token use without improving the result.

The first question after a model upgrade should not be, "What else can we add?" It should be, "What can we safely remove?"

## The hidden variable: architectural half-life

AI architecture has a half-life.

Every layer of prompting, routing, retrieval, memory, and orchestration was designed around an assumption about what the model could not do reliably. When a new generation makes part of that layer native, the layer changes from leverage into overhead.

The hard part is distinguishing:

- **Native capability:** work the model can now perform reliably without bespoke scaffolding.
- **Explicit control:** safety, approval, provenance, permissions, current-information checks, and verification that should remain visible even when models improve.
- **Legacy overhead:** duplicated instructions, stale routing logic, unnecessary replay, and orchestration that survives only because nobody re-tested the assumption underneath it.

This is the real system-design problem. The architecture must evolve with the model without allowing the model to erase judgment.

## The personal encounter

### The triggering case: when the plugin is the bottleneck

A Reddit user posted a much cleaner example than a model comparison.

They reported that a routine Push/Deploy task was consuming about 4% of their weekly limit. Over the next six hours, they used more than 80% of that weekly limit. Other users pointed to the `Superpowers` plugin as the source of the burn.

The user deleted the plugin. About six hours later, they reported having consumed barely 3% of the limit. The workload, model, and reasoning setting had not changed.

That is source-reported evidence, not a controlled benchmark. It does not prove that `Superpowers` will have the same effect in every setup. It does show the mechanism clearly enough to challenge the default diagnosis: sometimes the expensive part is not the model or the work. It is the layer we added to make the model more capable.

The plugin was supposed to be leverage. In that configuration, it had become overhead.

### Starting assumption

In the GPT-5.4 and GPT-5.5 era, we built substantial instruction, routing, memory, retrieval, and orchestration scaffolding to make the system reliable enough for real work.

That was rational at the time. The scaffolding solved real problems.

### The signal

In the GPT-5.6 era, many capabilities appeared to be more native. The same broad workflows did not require the same amount of explicit instruction and coordination.

Yet the system was still carrying yesterday's assumptions. Token use rose even though the workflow had not changed much.

The symptom was not simply that the model was expensive. The architecture was asking the model to process work that the model, or the surrounding runtime, no longer needed to be told in the same way.

### The intervention

We simplified the system by:

- reducing group conversation replay to 20 messages;
- removing duplicated bootstrap instructions from `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and `WORKSPACE-MAP.md`;
- making `route-work` the canonical owner of routed-work completion mechanics;
- narrowing `review-router` to review-method selection;
- removing obsolete `llama.cpp` runtime and configuration surface;
- adding lightweight date-based retention for disposable generated artifacts.

We preserved the gates that still carry independent value:

- safety and privacy;
- approval for external or consequential actions;
- current-information checks;
- context-loader discipline;
- provenance and source attribution;
- verification before claiming completion.

### The surprising result

Rough user-assessed impact, not a controlled benchmark:

- a small task had previously consumed about 3% of weekly quota;
- full research and underwriting of one stock had previously consumed about 6% to 8%;
- after simplification, the same kind of stock research could be done in about 1% of weekly quota.

The evidence does not establish that GPT-5.6 alone caused the improvement. The change combined a newer model with a leaner instruction and runtime architecture.

That qualification is part of the lesson. If the system changes several variables at once, the honest conclusion is that the new combination was more efficient, not that one model release explains everything.

## Technical consequence

A model upgrade changes the economics of the surrounding system.

Redundant instructions consume tokens. Long conversation replay increases input cost and context competition. Duplicated ownership rules create conflicts the model has to resolve. Obsolete runtime configuration expands the surface area the system must understand. Extra orchestration adds latency and failure points when native capability has made the orchestration unnecessary.

The architecture therefore needs a re-test loop after every meaningful model generation:

1. Identify the assumptions the current system was built around.
2. Test which assumptions are still true.
3. Remove redundant scaffolding in a reversible branch.
4. Preserve controls whose purpose is independent of model capability.
5. Compare cost, latency, quality, and failure modes before and after.

This is closer to refactoring than to prompt engineering.

## User consequence

Using AI is not only operating the interface. It is understanding enough of the system to notice when the interface is hiding a changed mechanism.

A user who cannot inspect the architecture will tend to respond to model change by piling on more instructions. That can produce the opposite of the intended result: more tokens, more latency, more ambiguity, and less attention available for the actual task.

The practical skill is model literacy. Know what the model is doing, what the runtime is doing, and what your own scaffolding is doing. Then adapt when the boundary moves.

That does not mean every user needs to become a systems engineer. It means serious users need enough judgment to tell the difference between a missing control and an obsolete one.

## Strategic consequence

The advantage will not belong only to people who adopt each new model quickly. It will belong to people who can re-underwrite their AI architecture quickly.

Every generation creates a new question:

- Which assumptions just became false?
- Which controls are still necessary?
- Which costs are now self-inflicted?
- Which parts of the workflow should remain deliberately human?

This creates a new form of technical debt. AI systems can become less efficient not only because they are old, but because they preserve instructions designed for an earlier model frontier.

The durable capability is therefore adaptive architecture: the ability to change the system while keeping judgment, accountability, and control intact.

## What a smart skeptic will say

A smart skeptic will say that removing scaffolding is risky. Some instructions look redundant until the model fails in an edge case. A leaner system can also make behavior less predictable if simplification is driven by token cost alone.

That objection is correct.

The answer is not to delete blindly. It is to delete experimentally, preserve rollback, and verify the behaviors that matter. Efficiency is not the only objective. A cheaper system that loses provenance or approval discipline is a regression.

The correct optimization target is useful work per unit of cost while preserving the controls that make the work trustworthy.

## Distilled warning

Do not confuse more visible architecture with more capable architecture.

Do not keep a control merely because it once solved a real problem.

Do not remove a control merely because a stronger model appears to understand it.

Re-test the boundary. Keep judgment explicit.

## Closing commands

- Re-underwrite the assumptions behind your AI stack.
- Delete duplicated instructions before adding new ones.
- Preserve safety, approval, provenance, and verification.
- Measure the system after the change, even if the first measurement is rough.
- Keep your judgment outside the model.

## Final inversion

The danger is not only that AI will become too powerful for us to control. It is that we will keep controlling yesterday's model so tightly that we waste the capabilities of today's one, then mistake our own scaffolding for the limits of intelligence.

## Source discipline for the eventual draft

- **Source-reported Reddit observation:** a user reported that a routine Push/Deploy task consumed about 4% of weekly limit, followed by more than 80% consumption in six hours. After deleting the `Superpowers` plugin, they reported barely 3% consumption over the next six hours, with no change to workload, model, or reasoning.
- **Supplied context:** Laurence observed higher token use for broadly similar workflows, then simplified the architecture and saw lower rough quota consumption.
- **Rough user estimates:** approximately 3% of weekly quota for a small task before; approximately 6% to 8% for full stock research before; approximately 1% after simplification. These are not controlled benchmarks.
- **Inference:** newer model capabilities can make some older scaffolding less necessary and therefore more expensive relative to its benefit. The Reddit example also suggests this can happen without a model change at all.
- **Unknown:** how much of Laurence's improvement came from the model generation, how much came from the architecture changes, and how much came from workflow variation.

## Triggering reference

Reddit thread supplied by Laurence: [r/OpenaiCodex discussion](https://www.reddit.com/r/OpenaiCodex/s/1k0wvMu2Gv)
