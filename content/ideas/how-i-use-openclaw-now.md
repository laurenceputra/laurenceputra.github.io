---
title: "How I Use OpenClaw Now, and What Changed Underneath"
description: "Portfolio reviews, forms, and upcoming commitments are useful today. Getting here has involved several rebuilds, and the architecture has changed since June."
date: 2026-10-04
tags: ["AI", "OpenClaw", "architecture", "agents"]
---

OpenClaw is doing useful work for me now. It monitors my portfolios, keeps investment theses and records updated, helps me review allocations, and handles small administrative tasks that otherwise remain on my list. It filled a childcare excursion PDF for me to submit. It has filled other random forms too.

That does not mean the system has been straightforward to build. I have rebuilt the investment setup several times. Some earlier versions were overly brittle and failed more than they worked. The current version is in better shape, but I would not claim that I know exactly how everything works now, or that the rebuilding is over.

I have been able to work around the limitations I have encountered so far. That has involved substantial rebuilding, and it does not remove the need to check the work.

## Why I moved to Discord

Discord is now where I interact with OpenClaw. The main reason for switching was threads within channels.

Each domain has a channel, and I can have several pieces of work running in separate threads within it. A portfolio review does not have to share one continuous conversation with a different question about the same portfolio. The same applies to branding, travel, and family logistics. I can come back to the particular piece of work without untangling everything else that happened in that domain.

Inactive threads disappear from the sidebar, which keeps the working surface manageable. They are still discoverable through the channel. Discord calls this [Hide After Inactivity](https://support.discord.com/hc/en-us/articles/4403205878423-Threads-FAQ). Disappearing from the sidebar does not mean the thread has been deleted.

This is a fairly mundane interface choice. It matters because concurrent work is easier to follow when each conversation has somewhere to live.

## The investment system took several attempts

I wanted an agentic investment workflow from the outset: a system that could do research, maintain the records, review what had changed, and bring a decision back to me.

In my experience building it with GPT-5.6 Sol, the work kept drifting towards more code even though I had specified that direction. Several rounds of rebuilding produced a system that was too brittle. Too often, I was dealing with a failed workflow rather than reviewing an investment.

This is an observation about my setup and those attempts. Code is not inherently the problem, and I cannot turn this into a general diagnosis of the model. Scripts can be useful when a step needs to be repeatable and precise. The problem was the system I ended up with. It failed more than it worked.

The current setup is more useful for managing my investments. That is a narrower claim than saying the architecture is solved. I still need to check the substance of the work and what actually completed.

## What changed underneath

In [June's architecture post](/ideas/how-openclaw-is-architected/), I described Telegram topics, a custom capabilities registry, a context-loading layer, and separate analyst, execution, writing, and coding lanes.

By [July](/ideas/delete-yesterdays-ai-scaffolding/), I was removing duplicated instructions, but I still retained `route-work`, `review-router`, and `context-loader`. The current setup has moved further from that design.

| Area | June setup | Current setup |
| --- | --- | --- |
| Conversations | Telegram topics | Discord domain channels with threads for individual work |
| Work selection | Custom capabilities registry and context loader | Native tool discovery and selectively loaded skills |
| Delegation | Analyst, execution, writing, and coding lanes | Main coordinates; general-lite, general, and general-high take scoped work |

The owner files remain important. `AGENTS.md` defines how work is handled and where approval is needed. `WORKSPACE-MAP.md` maps domains to their workspaces and channels. Domain files hold the actual records and current state.

The main agent coordinates the request, selects the appropriate lane, checks what comes back, and replies. A child agent gets a bounded task and returns its result to main. The lighter lane handles straightforward execution, the general lane handles substantial research and production work, and the higher-judgment lane handles consequential assessment or independent review. More thinking effort does not grant more authority to act.

The ordinary flow is now simple enough to describe without drawing every tool:

```text
Discord domain channel / task thread
                  ↓
       Main coordinates the request
                  ↓
    Scoped child work, when needed
                  ↓
       Result returns to main
                  ↓
  Check the output and reply in context
                  ↓
 Human approval and execution where required
```

Native OpenClaw schedules, sessions, completion delivery, session history, and messaging now handle asynchronous work. A repository-based Trello dispatcher was an intervening experiment, not a feature of the June design, and it is no longer the execution path. The custom capabilities directory from June is also no longer part of the active setup.

There is still local policy and domain-specific work. I have not replaced the entire workspace with a blank prompt. What changed is which parts of coordination belong to the runtime and which facts and decisions still need a local owner.

## What a useful portfolio review looks like

The useful work spans several portfolios: monitoring changes, updating theses, maintaining records, and reviewing allocations. Daily price-risk reviews help me keep track of how the portfolios are changing.

One concrete example was NTRA. After a massive climb, it had become a concentration issue. OpenClaw caught that and recommended reducing the position. I made the reduction.

That is a useful outcome I can point to. It does not establish that OpenClaw improved my returns or timed the market well. It brought a portfolio change to my attention and gave me a recommendation I could evaluate and act on.

The workflow I care about is fairly practical: look at what changed, relate it to the thesis and allocation, keep the record current, and bring me the decision that needs attention. I still decide whether the recommendation makes sense and execute the transaction.

Tongue in cheek, I act as the MCP for OpenClaw to make transactions. MCP means Model Context Protocol, a way for AI systems to connect to tools and data. In this case, the joke is that the connection to the transaction is me. I am not describing an autonomous brokerage integration.

## Forms and upcoming commitments

The less interesting tasks are useful too. A completed excursion form is a concrete artifact I can inspect and submit. It does not need a sophisticated story about agent orchestration to be worth doing.

For upcoming commitments, the current calendar-related setup builds a local agenda from invitations received through Gmail. It processes emailed calendar files, including updates, cancellations, and recurring events, and a native schedule is configured for a briefing. An invitation appearing in that agenda does not mean I have accepted it.

This is not direct Google Calendar access. Reading email with a Gmail app password did not give OpenClaw Calendar OAuth access. Direct Google Calendar integration is still planned, rather than completed.

I also have a ticket stored so it can be surfaced two hours before a future event. That is an upcoming reminder, not a successful delivery I can already claim. Keeping that distinction matters: storing something and scheduling its return are useful steps, but the test is whether it reaches me when I need it.

## Build around outcomes, not orchestration

The current setup is doing work I find useful, after several attempts that were much less useful. I do not want to turn that into a tidy story where the last rebuild fixed everything.

For the next change, I want to start with the thing I need to receive. Is the form ready for me to submit? Does the portfolio review identify a change that needs my attention? Does the reminder arrive before the event? If a workflow fails, can I tell what completed and what still needs doing?

Those are usable tests. A completed run, an extra agent, or a more elaborate diagram does not answer them on its own. I want to build around those outcomes and judge the architecture by whether it delivers them.
