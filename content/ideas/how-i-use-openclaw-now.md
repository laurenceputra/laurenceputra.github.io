---
title: "How I Use OpenClaw Now, and What Changed Underneath"
description: "How I use OpenClaw for investment reviews, forms, and upcoming commitments, and how the architecture has changed since June."
date: 2026-10-04
tags: ["AI", "OpenClaw", "architecture", "agents"]
---

I want OpenClaw to help me keep up with my investments and get everyday tasks done. For the portfolios, that means keeping theses and records current, identifying changes in risk or the business, and bringing allocation recommendations to me. For smaller jobs, it means preparing a form I can submit or putting together an agenda from emailed invitations. Adopting AI does not automatically make any of that work useful. The investment workflow has taken several rebuilds to get into its current shape.

Since [my June architecture post](/ideas/how-openclaw-is-architected/), both the way I organise the work and the machinery underneath have changed. I now use Discord rather than Telegram, and more of the coordination runs through native OpenClaw features. The current setup is better at managing my investments, although I would not say I understand exactly how everything works or that I have finished rebuilding it.

## Getting the investment workflow to work

I wanted an agentic investment workflow from the outset. OpenClaw would research an investment, maintain the records, review what had changed, and bring decisions back to me. In my experience building this with GPT-5.6 Sol, it repeatedly drifted towards more code despite that direction being specified at the start. Several rebuilds left me with brittle workflows that failed more than they worked. Too often, I was dealing with the system rather than reviewing the investment.

I still check the investment analysis and whether the work actually completed.

The daily price-risk monitor runs across my portfolios. Alongside it, OpenClaw looks for developments that improve or otherwise change the investment case for a holding, keeps the thesis and portfolio records current, and recommends allocation changes. A price move can change the weight of a position, while a change in the business can affect whether I still want that exposure.

After a substantial climb in NTRA, the position had become a concentration issue. OpenClaw flagged it and recommended a reduction, which I made.

I still decide whether a recommendation makes sense and execute the transaction. In that sense, I’m OpenClaw’s MCP.

## What changed underneath

Those rebuilds have made me more careful about what the architecture is there to support. I need the research and records to stay current, the work to come back for review, and consequential actions to remain subject to permission. The coordination has to make that work reliable enough to use without becoming another job to maintain.

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

## Organising concurrent work in Discord

I now use Discord’s domain channels and threads to organise concurrent work. A portfolio review can continue in its own thread while I ask another question about the same portfolio elsewhere in the channel. When the result comes back, I can return to that conversation. Branding, travel, and family logistics work the same way.

With Discord’s [Hide After Inactivity](https://support.discord.com/hc/en-us/articles/4403205878423-Threads-FAQ), inactive threads disappear from the sidebar but remain accessible through the channel. That keeps the sidebar manageable as tasks accumulate.

## Forms and upcoming commitments

Away from the portfolios, I use OpenClaw for tasks that are easy to leave sitting on a list. The childcare excursion PDF is one example: it filled the document for me to inspect and submit. Other random forms follow much the same pattern.

For commitments, it builds a local agenda from invitations received through Gmail. It processes emailed calendar files, including updates, cancellations, and recurring events, and a native schedule is configured to produce a briefing. An invitation in that agenda is not necessarily one I have accepted. Direct Google Calendar integration is still planned.

I also have a ticket stored for an upcoming event. OpenClaw is due to surface it two hours beforehand.

After several rebuilds, I have a better investment workflow, though I still check the analysis and whether the work completed. The earlier attempts also left me with a cost to weigh: the effort of maintaining a system that often failed. More capable models have made some of my helpers less useful, and native OpenClaw features now handle more of the coordination. I judge the setup by the work it completes, the decisions it helps me make, and the effort it takes to keep running.

For the next change, I want to start with the work and what completion requires: what result I need, what needs checking, and which decisions remain mine. I will retain or add orchestration where it serves a concrete need, such as keeping concurrent tasks separate or returning a scheduled result for review. That gives me a way to decide whether an architectural change is worth making before I build it.
