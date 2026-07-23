---
title: "Delete Yesterday's AI Scaffolding"
description: "As models improve, the next AI productivity gain may come from removing yesterday's prompts, plugins, and orchestration while keeping the controls that protect judgment."
date: 2026-07-23
draft: true
tags: ["AI", "architecture", "agents", "systems", "judgment"]
aliases: ["/blog/delete-yesterdays-ai-scaffolding/"]
---

A better model does not automatically make an AI setup cheaper.

Sometimes it reveals that the setup has become too elaborate.

I started noticing this because I was using more tokens for broadly similar workflows. The work had not changed much. The model had improved. The surrounding system had become heavier.

In the GPT-5.4 and GPT-5.5 era, we built substantial instruction, routing, memory, retrieval, and orchestration scaffolding to make AI reliable enough for real work. That was a sensible response to the models we had at the time.

In the GPT-5.6 era, more of those capabilities appeared to be native. The old layers still existed, even where they had become partly redundant. They continued to consume context, create coordination overhead, and shape the model's attention.

The first response should be an audit, not another layer.

## A plugin can become the bottleneck

A Reddit post brought the mechanism into sharper focus.

The author reported that a routine Push/Deploy task was consuming about 4% of their weekly limit. Within six hours, they had used more than 80% of that limit. Other users pointed to the `Superpowers` plugin as the source of the burn.

They deleted the plugin. About six hours later, they reported that they had barely consumed 3%. The workload, model, and reasoning setting had not changed.

This is a source-reported observation, not a controlled benchmark. It does not establish that the plugin will behave the same way in every setup. It does show how easily a layer intended to improve an AI workflow can become the most expensive part of it.

A plugin can start as leverage and become overhead.

That is the architectural problem I recognised in my own system.

## Every AI architecture has a half-life

Every layer of an AI system encodes an assumption about what the model cannot do reliably on its own.

A prompt may exist because the model used to miss a constraint. A routing layer may exist because the model needed help choosing the right workflow. A retrieval step may exist because the model could not reliably find current information. A plugin may exist because the model needed a particular planning or verification loop.

Those assumptions have a half-life.

When a new model generation handles part of the work natively, the layer around it needs to be re-tested. It may still provide value. It may also be duplicating a capability that has moved into the model, the runtime, or the user's normal workflow.

I think about the layers in three groups:

- **Native capability:** work the model can now perform reliably without bespoke scaffolding.
- **Explicit control:** safety, approval, permissions, provenance, current-information checks, and verification that should remain visible even as models improve.
- **Legacy overhead:** duplicated instructions, stale routing logic, unnecessary replay, and orchestration that survives because nobody has re-tested the assumption underneath it.

The boundary moves with every generation.

## What I changed in my own setup

I had been carrying forward a system designed around earlier model behaviour. It included a large instruction surface, broad conversation replay, overlapping ownership rules, and runtime configuration that no longer earned its place.

So I simplified it.

I reduced group conversation replay to 20 messages. I removed duplicated bootstrap instructions from `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and `WORKSPACE-MAP.md`. I made `route-work` the canonical owner of routed-work completion mechanics. I narrowed `review-router` to review-method selection. I removed obsolete `llama.cpp` runtime and configuration surface. I added lightweight date-based retention for disposable generated artifacts.

I kept the controls that have value independent of model capability: safety and privacy rules, approval for external or consequential actions, current-information checks, context-loader discipline, source attribution, and verification before claiming completion.

The goal was to reduce overhead without weakening judgment.

## The early numbers are encouraging, with an important caveat

These are rough user-assessed observations, not a controlled benchmark.

Before the simplification, a small task could consume about 3% of weekly quota. Full research and underwriting of one stock often consumed 6% to 8%. After the simplification, the same kind of stock research could be done in about 1% of weekly quota.

That is a meaningful change. It is also impossible to attribute to GPT-5.6 alone. The model generation and the architecture changed together, and workflow variation still exists. The honest conclusion is that the new combination was more efficient.

That distinction matters because model releases encourage simple stories. A new model arrives, performance improves, and we credit the model for everything. The surrounding system quietly contributes a large part of the result, including the cost when it is poorly designed.

## The technical consequence

A model upgrade changes the economics of the system around it.

Redundant instructions consume tokens. Long conversation replay increases input cost and context competition. Duplicated ownership rules create conflicts the model has to resolve. Obsolete runtime configuration expands the surface area the system must understand. Extra orchestration adds latency and failure points when a native capability has made the orchestration unnecessary.

This is why token use can rise even when the user's work stays broadly the same. The system is processing more of its own scaffolding.

The correct response is a re-test loop after every meaningful model generation:

1. Identify the assumptions the current system was built around.
2. Test which assumptions are still true.
3. Remove redundant scaffolding in a reversible branch.
4. Preserve controls whose purpose is independent of model capability.
5. Compare cost, latency, quality, and failure modes before and after.

This is closer to refactoring than to prompt engineering.

## The user consequence

Using AI now requires more than operating the interface. It requires enough model literacy to notice when the mechanism underneath the interface has changed.

A user who cannot inspect the system will usually respond to a problem by adding instructions. That can increase token use, latency, ambiguity, and the amount of attention spent on the workflow itself.

Serious users do not need to become systems engineers. They do need to understand what the model is doing, what the runtime is doing, and what their own scaffolding is doing. That is enough to recognise the difference between a missing control and an obsolete one.

The habit I want is simple: after a new model arrives, revisit the assumptions that shaped the old workflow.

## The strategic consequence

The advantage will not belong only to people who adopt each new model quickly. It will belong to people who can re-underwrite their AI architecture quickly.

Every generation creates a maintenance question:

- Which assumptions just became false?
- Which controls are still necessary?
- Which costs are now self-inflicted?
- Which parts of the workflow should remain deliberately human?

This creates a new form of technical debt. AI systems become inefficient when they preserve instructions designed for an earlier model frontier.

The durable capability is adaptive architecture: changing the system while keeping judgment, accountability, and control intact.

## Keep judgment explicit

The appeal of a stronger model is that more of the workflow can become automatic. That is useful. It also creates a temptation to let the model become the authority inside the system.

I want the model to handle more of the work. I still want the system to make clear who approved an action, where an important fact came from, whether the information is current, and what was actually verified.

Those controls should remain explicit because they serve accountability, not merely model performance.

A leaner system is valuable when it removes duplication. It becomes dangerous when it removes the ability to inspect, challenge, or stop the system.

## The operating habit

AI architecture changes every week, even when the configuration file does not.

A new model can make an old prompt redundant. A plugin can quietly turn into a token multiplier. A routing rule can survive after the workflow it served has changed. A memory layer can preserve context that no longer helps.

The answer is a regular architectural review:

- re-test the assumptions;
- delete duplicated instructions;
- measure the result;
- preserve safety, approval, provenance, and verification;
- keep human judgment at the points where responsibility matters.

Use the new model. Inspect the system around it. Adapt before the old scaffolding becomes the bottleneck.

The deeper risk is that we keep managing today's models with yesterday's scaffolding, then call the resulting waste a limitation of AI.

_Source example: [a Reddit discussion in r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex/s/1k0wvMu2Gv)._
