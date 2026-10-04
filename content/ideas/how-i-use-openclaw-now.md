---
title: "How I Use OpenClaw Now, and What Changed Underneath"
description: "How I use OpenClaw for investment reviews, forms, and upcoming commitments, and how the architecture has changed since June."
date: 2026-10-04
tags: ["AI", "OpenClaw", "architecture", "agents"]
---

I use OpenClaw to monitor my portfolios, maintain investment theses and records, and review allocations. It also handles smaller jobs: filling forms, putting together an agenda from emailed invitations, and keeping things I will need for an upcoming event. The investment work has taken several rebuilds to get into its current shape.

Since [my June architecture post](/ideas/how-openclaw-is-architected/), both the way I organise the work and the machinery underneath have changed. I now use Discord rather than Telegram, and more of the coordination runs through native OpenClaw features. The current setup is better at managing my investments, although I would not say I understand exactly how everything works or that I have finished rebuilding it.

## Getting the investment workflow to work

I wanted an agentic investment workflow from the outset. OpenClaw would research an investment, maintain the records, review what had changed, and bring decisions back to me. In my experience building this with GPT-5.6 Sol, it repeatedly drifted towards more code despite that direction being specified at the start. Several rebuilds left me with brittle workflows that failed more than they worked. Too often, I was dealing with the system rather than reviewing the investment.

There are steps where code makes sense, especially when something needs to be repeatable and precise. But the versions I built were not working reliably enough. I have been able to work around the limitations I encountered, with substantial rebuilding and continued checking of both the investment analysis and what actually completed.

The daily price-risk monitor helps me keep track of my portfolios. Alongside that monitoring, OpenClaw helps identify changes in the investment case for each holding and review allocations. These parts of the work belong together: a price move can change the weight of a position, while a change in the business can affect whether I still want that exposure. Keeping the thesis and portfolio records current gives the review something to work from beyond the latest price.

NTRA was a concrete example. After a massive climb, the position had become a concentration issue. OpenClaw flagged it and recommended a reduction, which I made. That is the kind of decision I want the workflow to bring to my attention. It connects a change in the portfolio to an action I can consider, rather than leaving me with another report to read.

I still decide whether a recommendation makes sense and execute the transaction. Tongue in cheek, I act as the MCP for OpenClaw to make transactions. MCP means Model Context Protocol, a way to connect AI systems to tools and data; here, the connection is me.

## What changed underneath

The June setup used Telegram topics, a custom capabilities registry, a context-loading layer, and separate analyst, execution, writing, and coding lanes. In [July's post](/ideas/delete-yesterdays-ai-scaffolding/), I described removing duplicated instructions while retaining routing and context-loading helpers. Those helpers have since been retired, along with the custom capabilities directory. Native discovery and retrieval now handle finding the relevant tools and context, with skills loaded selectively for the task.

| Area | June setup | Current setup |
| --- | --- | --- |
| Conversations | Telegram topics | Discord domain channels and task threads |
| Context and workflows | Custom capabilities registry and context loader | Native discovery and retrieval, selectively loaded skills |
| Delegation | Analyst, execution, writing, and coding lanes | Main, general-lite, general, and general-high with scoped tasks |
| Background work | Runtime schedules with custom workflow coordination | Native schedules, sessions, completion delivery, history, and messaging |

Main remains the agent I interact with. It coordinates the request, chooses whether to delegate, checks the result, and replies. General-lite handles bounded, straightforward execution. General takes substantial research and production work. General-high handles consequential judgment or independent review. Each child receives a scoped task and returns its result to main; a stronger reasoning lane does not get broader permission to act.

Background work also uses the native runtime now. OpenClaw schedules start the work, sessions hold the execution, and completion delivery and messaging return the result. Session history lets me inspect what happened. I no longer use a separate repository-based dispatcher for this.

The local workspace still supplies the rules and records that OpenClaw cannot infer for me. There is an owner for how work is handled and approved, a map of domains to workspaces and channels, and domain files containing current state. For investments, that includes the portfolio records and theses. Approvals and verification remain local requirements. Moving coordination into the runtime does not remove the need to check an output or get permission before a consequential action.

This is a different division of work from June. Less of the workspace is concerned with telling OpenClaw how to find and coordinate work, while the facts, decisions, and authority boundaries still need explicit owners.

## Organising concurrent work in Discord

Discord is now the front door because it supports threads within each domain channel. I can run several tasks about the same portfolio without putting them all into one continuous conversation. A review can have its own thread, while another question about that portfolio continues elsewhere in the channel. Branding, travel, and family logistics work the same way.

That fits the way I use an agent that can keep working on one request while I start another. The domain channel tells me where the work belongs; the thread gives that particular task somewhere to continue. When a result comes back, I can return to its conversation without untangling the other work in the domain.

Inactive threads disappear from the sidebar but remain accessible through the channel. Discord calls this [Hide After Inactivity](https://support.discord.com/hc/en-us/articles/4403205878423-Threads-FAQ). They are hidden from that working view, not deleted, so the sidebar can stay manageable without losing the conversations.

## Forms and upcoming commitments

Away from the portfolios, I use OpenClaw for tasks that are easy to leave sitting on a list. The childcare excursion PDF is one example: it filled the document for me to inspect and submit. Other random forms follow much the same pattern.

For commitments, it builds a local agenda from invitations received through Gmail. It processes emailed calendar files, including updates, cancellations, and recurring events, and a native schedule is configured to produce a briefing. An invitation in that agenda is not necessarily one I have accepted. Direct Google Calendar integration is still planned; the current workflow reads invitations from email rather than using the Calendar API.

I also have a ticket for a future event stored to be surfaced two hours beforehand. That reminder is still to come. It is a small job, but having the ticket at hand when I need it is exactly the sort of thing I want an assistant to handle.

The current setup gives me portfolio changes to review, documents I can submit, and a way to keep upcoming commitments in view. It has taken several attempts to get here, and I still need to check the work. When I change the architecture again, those are the things I want to keep working, rather than finding myself spending more time repairing the workflow than using it.
