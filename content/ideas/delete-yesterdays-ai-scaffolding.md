---
title: "Delete Yesterday's AI Scaffolding"
description: "As models improve, the next AI productivity gain may come from removing yesterday's prompts, plugins, and orchestration while keeping the controls that protect judgment."
date: 2026-07-23
tags: ["AI", "architecture", "agents", "systems", "judgment"]
aliases: ["/blog/delete-yesterdays-ai-scaffolding/"]
---

When an AI workflow becomes more expensive, my first instinct is usually to ask whether the work has become harder. Recently, that explanation stopped fitting what I was seeing. I was using more tokens for broadly similar work even though the underlying tasks had not changed much. The model had improved, and the system around it had accumulated more instructions, routing decisions, memory, retrieval, and coordination. The cost was increasingly coming from the way I had organised the work.

Most of that scaffolding had been added for good reasons. During the GPT-5.4 and GPT-5.5 era, I needed explicit mechanisms to compensate for behaviours the models did not handle reliably enough on their own. Prompts clarified constraints, routing logic selected specialised workflows, memory layers preserved continuity, and orchestration created repeatable checks. Each addition solved a real problem at the time, so carrying the whole system forward felt safer than questioning it. The difficulty was that the assumptions behind those additions were becoming less visible as the system grew.

My experience with GPT-5.6 made me reconsider those assumptions. Some work that had previously required bespoke guidance appeared to be handled more reliably by the newer combination of model and runtime. The older layers were still consuming context and shaping the model's attention, even when their original purpose had weakened. I began to see model upgrades as an architectural review point: each generation changes the boundary between what the model can do natively, what the runtime should enforce, and what the user still needs to specify.

## How a plugin can become the bottleneck

A Reddit discussion helped me see one possible mechanism more clearly. The original poster reported that a routine Push/Deploy task consumed about 4% of their weekly limit and that more than 80% of the limit had been used within six hours. In the discussion, other users attributed the unexpected consumption to the `Superpowers` plugin. According to the original poster, they deleted the plugin and then used barely 3% over roughly the next six hours, while the workload, model, and reasoning setting remained unchanged.

Those figures and conditions come from the poster's own account. They are source-reported observations from that discussion, and they do not measure my system. The commenters' attribution of the consumption to the plugin remains an explanation offered in the discussion. The example does not isolate every variable or establish causation with confidence. I found it useful because it illustrated a failure mode that matched what I had begun to suspect in my own setup: a layer introduced to improve an AI workflow can eventually account for a significant share of its cost. A plugin can remain useful in principle while its particular implementation, configuration, or interaction with a newer model creates more work than value.

That is why I am increasingly interested in the architecture around the model. When token consumption rises, the model is the most visible component, so it is easy to blame model pricing, model reasoning, or the complexity of the task. The Reddit example points to a wider diagnostic process. Before changing the model or reducing the quality of the work, inspect the prompts, plugins, replay rules, and orchestration that cause the model to process the request in the first place.

## Every layer encodes an assumption

I now look at every layer in an AI system as an assumption about what the model, runtime, or user cannot yet do reliably. A prompt may exist because an earlier model repeatedly missed a constraint. A routing rule may have been necessary because workflow selection was inconsistent. Retrieval may be required because the task depends on current information that the model cannot know from its training data. A plugin may implement a planning or verification loop that the base system otherwise lacks. Each layer represents a judgement about where the system needs support.

Those assumptions have a half-life. When the model or runtime changes, the surrounding layers deserve to be tested again. Some will continue to earn their place because they provide capabilities the model still lacks. Others may duplicate behaviour that has become sufficiently reliable elsewhere in the system. Leaving all of them in place can increase input cost, create competing instructions, add latency, and make failures harder to diagnose. The architecture becomes a record of historical problems, even after some of those problems have been solved.

For practical purposes, I divide the architecture into three groups:

- **Native capability:** work that the current model and runtime can perform reliably enough without bespoke scaffolding.
- **Explicit control:** safety, privacy, approval, permissions, provenance, current-information checks, context-loader discipline, and verification mechanisms that remain important regardless of model quality.
- **Legacy overhead:** duplicated instructions, stale routing logic, unnecessary context replay, and orchestration whose original assumptions no longer hold.

The boundaries between these groups move as the system changes. I treat the classification as a working view that needs regular revision. A prompt that was essential six months ago may now be redundant. A control that looks like overhead may still be the only visible protection against an external action, a stale fact, or an unverified claim.

## What I changed in my own setup

My setup had grown around earlier model behaviour. It included a large instruction surface, broad replay of past conversation, overlapping ownership rules, and runtime configuration that I had continued carrying forward because each component was individually defensible. Looking at the system as a whole made the accumulated cost easier to see. I was asking the model to navigate the history of my operating system before it could spend its attention on the task in front of it.

I removed duplicated bootstrap instructions from `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and `WORKSPACE-MAP.md`. I made `route-work` the canonical owner of routed-work completion mechanics, narrowed `review-router` to selecting the review method, and introduced lightweight date-based retention for disposable generated artifacts. These were targeted changes to places where I could identify duplication or an expired assumption. I did not try to redesign the entire system, because a broad rewrite would have made it harder to know which change produced which result.

I deliberately retained controls whose purpose extends beyond compensating for model weakness. Safety and privacy rules still define what the system may do. Approval remains necessary for external, consequential, destructive, or privacy-sensitive actions. Provenance and source attribution still show where important claims came from. Current-information checks remain necessary when facts may have changed, and context-loader discipline still helps retrieve the appropriate bounded context before broader investigation. Verification remains essential before the system claims that work is complete.

This is the one distinction I want to preserve clearly: I am removing redundant scaffolding, not delegating judgment and accountability to the model. The system should become easier to operate as models improve, with the parts that make its actions inspectable and governable remaining visible.

## What my rough quota estimates suggest

My own numbers are rough user-assessed observations from weekly quota usage, with no controlled benchmark behind them. A full research and underwriting pass on GPT-5.6-Sol at medium reasoning consumed roughly 6% to 8% of my weekly quota. A similar pass on GPT-5.5 at medium reasoning took around 1% to 2%. After I improved the instruction set, my last two runs took 1% each.

I consider that improvement meaningful enough to investigate. The figures cannot support a precise causal claim. The model generation and surrounding architecture changed together, individual research tasks vary, and the quota observations were collected during ordinary work rather than a controlled experiment. I therefore cannot determine how much of the improvement came from GPT-5.6, how much came from removing redundant system layers, or how much came from workflow variation.

The narrower inference is that the newer combination of model, runtime, and simplified architecture appears more efficient for my workflows. I also think the architecture changes probably contributed because they reduced repeated context and coordination, although the available observations do not let me quantify that contribution. Keeping the observation, the inference, and the remaining uncertainty separate matters because a plausible explanation can quickly harden into an unsupported story about causation.

## Why model upgrades change system economics

A model upgrade changes more than output quality. It changes the economics of every mechanism wrapped around the model. Repeated instructions consume input tokens on every relevant turn. Long conversation replay adds cost and gives the model more material to weigh when deciding what matters. Duplicated ownership rules create conflicts the model has to resolve. Obsolete runtime configuration expands the surface area the system must understand. Additional orchestration adds latency and failure points when the underlying capability has moved elsewhere.

This is why token use can rise even when the user's work stays broadly the same. The system may be processing more of its own scaffolding, replaying more history, or invoking more intermediate steps than the task requires. The resulting inefficiency is easy to miss because the visible output can still look good. A capable model may absorb a great deal of unnecessary context and return a reasonable answer, while the quota, latency, and reliability costs accumulate out of sight.

The review process I want after each meaningful model generation is therefore fairly practical. I would identify the assumptions the current system was built around, test which ones are still true, remove redundant scaffolding in a reversible branch, preserve controls whose purpose is independent of model capability, and compare cost, latency, quality, and failure modes before and after. That makes model maintenance closer to refactoring than to prompt engineering. The work is a combination of observation, controlled simplification, and verification.

## What this asks of the user

Using AI now requires more than operating the interface. It requires enough model literacy to notice when the mechanism underneath the interface has changed. A user who cannot inspect the system will usually respond to a problem by adding instructions, because instructions are the most accessible form of intervention. That response can increase token use, latency, ambiguity, and the amount of attention spent on the workflow itself.

Serious users do not need to become systems engineers. They do need to understand what the model is doing, what the runtime is doing, and what their own scaffolding is doing. That understanding makes it possible to ask better questions when a workflow becomes slow or expensive. Is the task genuinely harder? Is the model failing to follow a constraint? Is the context too large? Is a plugin repeating work the model can already perform? Is the system spending tokens proving to itself that it is following instructions?

The habit I want is simple to describe, even though it takes discipline to maintain: after a new model arrives, revisit the assumptions that shaped the old workflow. Treat the model as one changing component in a larger system. Pay attention to the relationship between capability, context, coordination, cost, and control.

## The strategic consequence

The advantage will belong to people who can re-underwrite their AI architecture quickly. Adopting a new model is increasingly easy. Understanding which parts of an existing workflow should change with it is harder, because that requires an account of how the system produces its result and where the cost is coming from.

Every generation creates a maintenance question. Which assumptions have become false? Which controls are still necessary? Which costs are now self-inflicted? Which parts of the workflow should remain deliberately human? These questions are relevant to individual users, teams building internal tools, and companies embedding AI into products. They determine how quickly an organisation can take advantage of a new model without carrying forward an architecture designed for an earlier frontier.

This creates a new form of technical debt. AI systems become inefficient when they preserve instructions, plugins, and workflows designed for an earlier model's limitations. The debt is difficult to see because each individual component may still appear reasonable. It becomes visible when the total system consumes more, takes longer, and requires more explanation for the same useful work.

## Keeping judgment explicit

The appeal of a stronger model is that more of the workflow can become automatic. That is useful, and it changes where human attention should go. I want the model to handle more of the repetitive work. The system should still make clear who approved an action, where an important fact came from, whether the information is current, and what was actually verified.

Those controls serve accountability as much as they serve model performance. They help me understand why a result should be trusted, where it may be weak, and what needs to be checked before an action leaves the private workspace. A leaner architecture should make those boundaries easier to inspect. It should reduce duplication and historical baggage while preserving the points where responsibility, permission, and judgement enter the process.

## The operating habit

AI architecture changes every week, even when the configuration file does not. A new model can make an old prompt redundant. A plugin can quietly turn into a token multiplier. A routing rule can survive after the workflow it served has changed. A memory layer can preserve context that no longer helps. These changes are easy to miss when the system is treated as a fixed collection of instructions, even though it is an evolving set of assumptions.

The maintenance habit is to review the system with the same seriousness used to review code. Re-test the assumptions, inspect the token and latency costs, delete duplicated instructions, preserve safety and approval boundaries, check provenance and currentness, and verify the result before declaring the change an improvement. The aim is a system that can absorb new model capabilities while remaining inspectable and economical by default.

Use the new model, inspect the system around it, and adapt before the old scaffolding becomes the bottleneck. The deeper risk is that we keep managing today's models with yesterday's scaffolding, then call the resulting waste a limitation of AI.

_Source example: [a Reddit discussion in r/OpenaiCodex](https://www.reddit.com/r/OpenaiCodex/s/1k0wvMu2Gv)._
