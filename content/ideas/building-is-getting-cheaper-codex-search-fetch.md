---
title: "Building Is Getting Cheaper. Here Are Two Plugins I Needed."
description: "Custom search and fetch providers for OpenClaw, and what cheaper software changes about the value of building."
date: 2026-10-08
tags: ["AI", "engineering", "OpenClaw", "Codex"]
---

Over the past two days, I built two OpenClaw plugins because search and fetching pages were getting in the way of using my agents.

In my setup, Codex hosted search was using Astra and burning through usage. Separately, web fetch was returning 403 on a number of sites. If you run Codex-backed agents through OpenClaw's Pi harness, the useful change is that I can now choose the search worker's model and reasoning effort without leaving Pi. Fetch adds a best-effort fallback, although it has not solved every failed retrieval.

The plugins are `custom-codex-search` and `custom-codex-fetch`. They are independent, so you can use one without the other. Both are experimental. I intend to release them on npm when I get access to my computer, but they are not published yet.

The building work was smaller than those two problems might suggest. OpenClaw already supplied the ordinary tool-provider interfaces and the parent harness. Codex already supplied native search and extraction. The plugins connect those surfaces, choose a worker, and check what comes back. They share the same authentication adapter and closely related worker plumbing; there was no need for a new agent harness or a search engine.

AI assistance was part of planning that integration: the agent proposed native tests, reusing the search safeguards, and independent review. I still questioned the setup, including why readability had been disabled. That question matters because a successful HTTP extraction and a successful native fetch are different things. This is the part of the experience that interests me: getting to an implementation is easier, but deciding what it should do and what counts as working still needs judgment. Two elapsed days are not a productivity benchmark.

## Keep Pi. Change the tool provider.

Pi continues to run the agent. These plugins register providers for OpenClaw's ordinary `web_search` and `web_fetch` tools. When a native operation is needed, the plugin starts a separate Codex app-server worker and returns its result to the tool call.

Both workers default to `gpt-6-sol` with `low` reasoning effort. These are explicit plugin settings, not settings inherited from the model running your conversation. I can choose the model for a search separately from the model doing the work that needs it. I have not measured the usage savings yet.

## Trying search locally

The versions here are search 0.2.0 and fetch 0.1.2, with Node 24 or newer, npm, OpenClaw 2026.9.8 and native Codex 0.158.0. Other host versions are unsupported. Read the [repository README](https://github.com/laurenceputra/openclaw-codex-plugins) and each package's security guidance first. The authentication integration uses an experimental private SDK API that may break on host updates. Local archives do not acquire official-plugin trust; do not relax trust checks to install them.

Clone the public repository, then test and package search on your OpenClaw host:

~~~sh
git clone --branch main https://github.com/laurenceputra/openclaw-codex-plugins.git
cd openclaw-codex-plugins/packages/custom-codex-search
npm test
npm pack --ignore-scripts
openclaw plugins install ./custom-codex-search-0.2.0.tgz --no-enable
~~~

Install the individual package, not the repository root. These are interactive install commands: review the source and any capability prompts rather than bypassing them. `--no-enable` preserves existing enablement and policy settings; on a fresh install, configure the plugin before enabling it. The repository can change, so check the package version before using the archive name above. There is no npm registry recipe yet.

In your existing `openclaw.json`, merge this fragment into `plugins.entries["custom-codex-search"].config`. Replace the placeholders with your existing values, and keep other fields such as timeouts and output limits:

~~~json
{
  "agentDir": "/absolute/auth-owning-agent-directory",
  "profileId": "openai:existing-subscription-profile",
  "binaryPath": "/absolute/operator-selected/codex",
  "model": "gpt-6-sol",
  "effort": "low"
}
~~~

`agentDir` is the directory belonging to the OpenClaw agent that owns the existing subscription profile, not this project checkout. Use that exact profile ID and a trusted, directly executable native Codex binary whose version you have checked. Authentication goes through the host SDK; there is no API-key billing fallback or reason to copy credential files into the repository.

After reviewing the package and configuration, enable it and inspect its runtime registration:

~~~sh
openclaw plugins enable custom-codex-search
openclaw plugins inspect custom-codex-search --runtime --json
~~~

Run these against a running local Gateway so the changes can apply. Inspect should show the search provider registration, not just an installed package. Merge `"provider": "custom-codex-search"` into `tools.web.search`, preserving its other fields. Your agent can then use its normal `web_search` tool, for example to find the documentation for a library you are using. See the [search README](https://github.com/laurenceputra/openclaw-codex-plugins/blob/main/packages/custom-codex-search/README.md) for deeper configuration and troubleshooting.

The model and effort must be explicitly supported by the authenticated native catalog. Unsupported selections fail rather than silently switching models. Search results identify the provider and label their evidence limitations. Snippets are not proof that a page was fetched, and generated summaries still need source-checking. Requesting five results limits retained sources, not native operations or usage.

## Fetch is still HTTP-first

Fetch uses the same local path, independently. From the search package directory above:

~~~sh
cd ../custom-codex-fetch
npm test
npm pack --ignore-scripts
openclaw plugins install ./custom-codex-fetch-0.1.2.tgz --no-enable
~~~

Merge the same five-field configuration fragment above into `plugins.entries["custom-codex-fetch"].config`, using the existing subscription profile and trusted binary, and preserving any existing fetch plugin settings. Review it, then enable and inspect fetch:

~~~sh
openclaw plugins enable custom-codex-fetch
openclaw plugins inspect custom-codex-fetch --runtime --json
~~~

If you only want fetch, start from the repository checkout and go straight to `packages/custom-codex-fetch`; search does not need to be installed. The [fetch README](https://github.com/laurenceputra/openclaw-codex-plugins/blob/main/packages/custom-codex-fetch/README.md) explains its routing and limits.

Merge these fields into `tools.web.fetch`, keeping unrelated settings:

~~~json
{
  "provider": "custom-codex-fetch",
  "readability": true,
  "cacheTtlMinutes": 0
}
~~~

Your agent still uses ordinary `web_fetch` with a URL. OpenClaw tries HTTP first. With readability enabled, successful HTML extraction can finish without invoking Codex; empty extraction or HTTP failures can reach the selected native fallback. Readability does not execute JavaScript and can omit page content, so this is not a browser replacement or a promise to get through every 403.

Look at the result's extractor and provider to understand which route ran. A readability result means the HTTP route worked, not that native fetching was repaired. Disabling the local fetch cache helps distinguish fresh retrieval from a cached answer; it does not disable upstream caches or change search caching.

The native path returns best-effort extraction, not a verified complete origin response. Status zero means the origin HTTP status is unknown. The returned URL does not verify redirects, and completeness remains unknown. Some exact URLs still fail on the hosted native path, with no resolved cause. For consequential use, independently check the retrieved text.

## Building is no longer what sets you apart

What changed here is control over search execution and another route to try when fetching fails. That is useful, but it is not evidence of measured usage savings or a universal fix for retrieval. Compatibility and failure behavior still need maintenance.

My judgment from this experience is that implementation is getting cheaper. Existing capabilities and assistance with planning make a small frustration easier to turn into something I can try. I cannot put a defensible number on that reduction, and producing the code does not establish that the problem is solved.

That changes where I think the value sits. Building alone is no longer what sets you apart. Choosing a useful problem, deciding what behavior is acceptable, and maintaining that behavior are still real work. Easier implementation makes those decisions more important.

The standard I care about is whether the software removes the constraint it was built for, with limits I can understand and failures I can live with. The fact that I can build it is increasingly the starting point.
