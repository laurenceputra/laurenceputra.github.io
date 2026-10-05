---
title: "How I Use OpenClaw Now, and What Changed Underneath"
description: "How I use OpenClaw for investment reviews, forms, and upcoming commitments, and how the architecture has changed since June."
date: 2026-10-04
tags: ["AI", "OpenClaw", "architecture", "agents"]
---

When I first started using OpenClaw, it was a way for me to explore using AI and understand how to use it in non-coding scenarios. Over time, it has started taking on more responsibilities in my personal life, from scheduling and managing my investment research to helping me with mundane form-filling work. Also, since [the June post](/ideas/how-openclaw-is-architected/), my OpenClaw has changed a fair bit, both in how I use it and what runs underneath it.

## Getting the investment workflow to work

I wanted an agentic investment workflow from the outset. OpenClaw would research an investment, maintain the records, review what had changed, and bring decisions back to me. In my experience building this with GPT-5.5 and GPT-5.6 Sol, it repeatedly drifted towards more code despite that direction being specified at the start. Several rebuilds left me with brittle workflows that failed more than they worked. Too often, maintaining the system displaced reviewing the investment.

With GPT-6 and GPT-6.1 Sol, I have been able to get closer to the workflow I intended, faster and more accurately. The current setup is better at helping me manage my investments, although I would not say I understand exactly how everything works or that I have finished rebuilding it.

The daily price-risk workflow helps me monitor changes in my portfolios. When a holding makes a significant price move, OpenClaw researches what might be behind it and assesses whether the evidence changes the investment thesis or calls for action in each affected portfolio. A price move can change the weight of a position, while a change in the business can affect whether I still want that exposure.

Monthly and quarterly reviews answer different questions. The monthly review looks at every holding within one portfolio: does it still fit the mandate, and should I hold, add, trim, exit, or investigate? It considers valuation, concentration, cash, and new evidence, and compares thesis-aligned alternatives when there is a reason to do so.

The quarterly review goes deeper into the portfolio’s strategy and structure: do the mechanisms behind its thesis still hold, what evidence would invalidate them, and does the portfolio still justify the capital and effort compared with a simpler alternative? It reuses relevant monthly evidence and focuses further research on holdings that matter to those questions.

After a substantial climb in NTRA, the position had become a concentration issue. OpenClaw flagged it and recommended a reduction, which I made. I still check the analysis and whether the work actually completed, decide whether a recommendation makes sense, and execute the transaction. In that sense, I’m OpenClaw’s MCP.

## Organising concurrent work in Discord

I now use Discord’s domain channels and threads to organise concurrent work. A portfolio review can continue in its own thread while I ask another question about the same portfolio elsewhere in the channel. When the result comes back, I can return to that conversation. Branding, travel, and family logistics work the same way.

With Discord’s [Hide After Inactivity](https://support.discord.com/hc/en-us/articles/4403205878423-Threads-FAQ), inactive threads disappear from the sidebar but remain accessible through the channel. That keeps the sidebar manageable as tasks accumulate.

## Forms and upcoming commitments

Away from the portfolios, I use OpenClaw for tasks that are easy to leave sitting on a list. The childcare excursion PDF is one example: it filled the document for me to inspect and submit. Other random forms follow much the same pattern.

For commitments, it builds a local agenda from invitations received through Gmail. It uses emailed calendar invitations, including updates, cancellations, and recurring events, to put together the briefing. An invitation in that agenda is not necessarily one I have accepted. For an upcoming event, OpenClaw has the ticket stored and is due to surface it two hours beforehand.

## What changed underneath

These uses need records that stay current, results that come back for review, and concurrent tasks that can proceed without losing their place. The architecture has to support that work without becoming another job to maintain.

The June setup used Telegram topics, a custom capabilities registry, a context-loading layer, and separate analyst, execution, writing, and coding lanes. In [July's post](/ideas/delete-yesterdays-ai-scaffolding/), I described removing duplicated instructions while retaining routing and context-loading helpers. As the models improved, I found those helpers less useful. That was a large part of why I retired them, along with the custom capabilities directory. Native discovery and retrieval now handle finding the relevant tools and context, with skills loaded selectively for the task.

| Area | June setup | Current setup |
| --- | --- | --- |
| Conversations | Telegram topics | Discord domain channels and task threads |
| Context and workflows | Custom capabilities registry and context loader | Native discovery and retrieval, selectively loaded skills |
| Delegation | Analyst, execution, writing, and coding lanes | Main, general-lite, general, and general-high with scoped tasks |
| Background work | Runtime schedules with custom workflow coordination | Native schedules, sessions, completion delivery, history, and messaging |

Main remains the agent I interact with. It coordinates the request, chooses whether to delegate, checks the result, and replies. General-lite handles bounded, straightforward execution. General takes substantial research and production work. General-high handles consequential judgment or independent review. Each child receives a scoped task and returns its result to main; a stronger reasoning lane does not get broader permission to act.

Background work also uses the native runtime now. OpenClaw schedules start the work, sessions hold the execution, and completion delivery and messaging return the result. Session history lets me inspect what happened. I no longer use a separate repository-based dispatcher for this.

The local workspace still supplies the rules and records that OpenClaw cannot infer for me. There is an owner for how work is handled and approved, a map of domains to workspaces and channels, and domain files containing current state. For investments, that includes the portfolio records and theses. The local rules also require outputs to be checked and permission obtained before consequential actions.

## Getting value from AI

I started with OpenClaw to explore what AI could do outside coding. It now helps with investment decisions and everyday tasks, but getting here has involved rebuilding systems that often failed. Adding more machinery did not necessarily bring me closer to the work I wanted done.

What started as an experiment is now helping me manage work I actually need to do. That is what I expect from AI: useful work that justifies the effort of running it. Building an elaborate system is not enough. It has to earn its place.
