---
title: "Building Is Getting Cheaper. Here Are Two Plugins I Needed."
description: "Custom search and fetch providers for OpenClaw, and what cheaper software changes about the value of building."
date: 2026-10-08
draft: true
tags: ["AI", "engineering", "OpenClaw", "Codex"]
---

Over the past two days, I built two OpenClaw plugins because search and fetching pages were getting in the way of using my agents.

In my setup, Codex hosted search was using Astra and burning through usage on searches. Separately, web fetch was returning 403 on a number of sites. These were ordinary operations that an agent needed to do, rather than the work I wanted it to spend its attention on.

The plugins are `custom-codex-search` and `custom-codex-fetch`. They are independent, so you can use one without the other. Both are experimental. I intend to release them on npm when I get access to my computer, but they are not published yet.

The practical change is that I can choose how these tools run without replacing the agent harness. What struck me more was how much easier it has become to turn a specific annoyance into a piece of software.

## Keep Pi. Change the tool provider.

This is for OpenClaw users running Codex-backed agents through the Pi harness. Pi continues to run the agent. These plugins register providers for OpenClaw's ordinary `web_search` and `web_fetch` tools.

When a native operation is needed, the plugin starts a separate Codex app-server worker. That worker handles the search or extraction, then returns the result to the tool call. It does not become the harness for the parent agent.

Both workers default to `gpt-6-sol` with `low` reasoning effort. Those are explicit plugin settings, not settings inherited from the model running your conversation. I can choose the model for a search separately from the model doing the work that needs it. I have not measured the usage savings yet.

## Trying search locally

Start with the [repository README](https://github.com/laurenceputra/openclaw-codex-plugins) and the [search README](https://github.com/laurenceputra/openclaw-codex-plugins/blob/main/packages/custom-codex-search/README.md). The current compatibility target is narrow: Node 24 or newer, OpenClaw 2026.9.8 and native Codex 0.158.0. Other host versions are not supported by this release candidate.

If you have access to a checkout, the documented local packaging route is:

~~~sh
cd packages/custom-codex-search
npm test
npm pack --ignore-scripts
openclaw plugins install ./custom-codex-search-0.2.0.tgz --no-enable
~~~

Install the individual package, not the repository root. This installs an archive without enabling it; review and activation are separate operator steps. There is no npm registry install recipe to use yet.

The provider needs your existing subscription authentication profile and a trusted native Codex binary. Merge the following into the existing search plugin configuration, replacing the placeholders with your own authorized values:

~~~js
plugins.entries["custom-codex-search"].config = {
  agentDir: "/absolute/auth-owning-agent-directory",
  profileId: "openai:existing-subscription-profile",
  binaryPath: "/absolute/operator-selected/codex",
  model: "gpt-6-sol",
  effort: "low"
}
~~~

This is configuration notation, not a shell command. After review and activation, select `tools.web.search.provider = "custom-codex-search"`. Your agent can then use its normal `web_search` tool. You do not need to teach it a second search tool.

The model and effort must actually be supported by the authenticated native catalog. An unsupported selection fails rather than silently switching models. Authentication goes through the host SDK; there is no API-key billing fallback or reason to copy credential files into the repository.

Search returns bounded results and labels its evidence limitations. Snippets are not proof that a page was fetched. Generated summaries still need source-checking, especially when the answer matters. Requesting five results limits retained sources, not the number of native operations or your usage.

## Fetch is still HTTP-first

The fetch plugin is a fallback, not a promise to get through every 403.

OpenClaw first tries ordinary HTTP retrieval. With readability enabled, successful HTML extraction can finish without invoking Codex. Empty extraction or HTTP failures can reach the selected native fallback. Readability does not execute JavaScript, so it is not a browser replacement either.

The [fetch README](https://github.com/laurenceputra/openclaw-codex-plugins/blob/main/packages/custom-codex-fetch/README.md) documents the recommended route and its separate installation steps. It uses its own `plugins.entries["custom-codex-fetch"].config` for authentication and binary settings. The HTTP-first route is:

~~~json
{
  "tools": {
    "web": {
      "fetch": {
        "provider": "custom-codex-fetch",
        "readability": true,
        "cacheTtlMinutes": 0
      }
    }
  }
}
~~~

Disabling the local fetch cache makes it easier to distinguish fresh retrieval from a cached answer. It does not disable upstream caches or change search caching.

The native path remains best-effort extraction, not a verified complete response from the origin. Its status of zero means the origin HTTP status is unknown. Its returned URL does not verify redirects. Some exact URLs still fail on the hosted native path, and the cause remains unresolved. A successful readability result establishes that the HTTP route worked, not that native fetching was repaired.

Read the package security guidance before installing either plugin. They use an experimental private SDK integration, and local archives do not acquire official-plugin trust. Do not relax trust checks to make installation work. For consequential use, independently check retrieved text.

## Building is no longer what sets you apart

Two days of building does not make these plugins production-proven. Compatibility needs maintenance, and failure behavior matters as much as a successful example.

But the cost of building software has decreased significantly. A tool that once might have stayed on a list of small frustrations can now become something you can try in your own workflow.

That changes where I think the value sits. Building alone is no longer what sets you apart. Choosing a useful problem, deciding what behavior is acceptable, and maintaining that behavior are still real work. Cheaper implementation makes those decisions more important because producing another implementation is easier.

The standard I care about is whether the software removes the constraint it was built for, with limits I can understand and failures I can live with. The fact that I can build it is increasingly the starting point.
