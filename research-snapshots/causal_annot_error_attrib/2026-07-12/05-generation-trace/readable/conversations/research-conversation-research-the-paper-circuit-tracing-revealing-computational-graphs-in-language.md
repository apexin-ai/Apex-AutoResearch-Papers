# Research conversation: Research the paper "Circuit Tracing: Revealing Computational Graphs in Language Models" by Emmanuel Ameisen, Jack Lindse

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9226866692b579ca.jsonl`
- **Structured JSON:** [`2d4813a5424d7d26bb63.json`](../../sessions/2d/2d4813a5424d7d26bb63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-30T06:22:18.542Z_

Research the paper "Circuit Tracing: Revealing Computational Graphs in Language Models" by Emmanuel Ameisen, Jack Lindsey, Adam Pearce, Wes Gurnee et al. (Anthropic), March 2025, URL: https://transformer-circuits.pub/2025/attribution-graphs/methods.html

Do the following:
1. Use WebFetch on the URL to read the methods page
2. Use WebSearch to find additional information about this Anthropic technical report on circuit tracing / attribution graphs
3. Try to find related blog posts or companion pages

Report back with:
- The exact problem/gap they identified in circuit tracing
- Their key innovation: attribution graphs with cross-layer transcoders
- How cross-layer transcoders differ from standard SAEs
- How they trace complete computational chains
- What circuits they demonstrated (multi-step reasoning, hallucination, planning)
- The scale of models they applied this to (Claude 3.5 Haiku)
- Open-sourced tools and their capabilities
- Limitations they acknowledge

Be thorough and specific with technical details. Report in under 800 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "7edc72fe-9c67-472c-87b2-0e4a0c364a42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:22:18.565Z_

```json
{
  "parentUuid": "7edc72fe-9c67-472c-87b2-0e4a0c364a42",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "2f62ebf1-4664-4a67-8ad0-5d12016f65be",
  "timestamp": "2026-05-30T06:22:18.565Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:22:18.568Z_

```json
{
  "parentUuid": "2f62ebf1-4664-4a67-8ad0-5d12016f65be",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3e73ee67-027b-4771-8aab-c24d7acc56c0",
  "timestamp": "2026-05-30T06:22:18.568Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:22:21.110Z_



I'll start by fetching the tools I need, then gather information from the paper and related sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e73ee67-027b-4771-8aab-c24d7acc56c0",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGjVhS5dGYnS9j4wPjz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b194c2b-b234-4f6b-8ce0-73bc2163a181",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDqSUoAiYDMzH2mqrbAaCf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1607,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-30T06:22:22.047Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QxeZUZb2jrAmMMJpJhJy7B`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b194c2b-b234-4f6b-8ce0-73bc2163a181",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGjVhS5dGYnS9j4wPjz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9959b4c-2d0d-4a1f-a204-644cb3c0dc60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDqSUoAiYDMzH2mqrbAaCf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 7413,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1607,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-30T06:22:22.056Z_

<details><summary>↩ Tool result · `toolu_01QxeZUZb2jrAmMMJpJhJy7B`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9959b4c-2d0d-4a1f-a204-644cb3c0dc60",
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "2b9e7e10-0ee5-4e9a-a73c-440fb2fa7c41",
  "sourceToolAssistantUUID": "d9959b4c-2d0d-4a1f-a204-644cb3c0dc60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:22:24.509Z_



Now let me fetch the paper and search for related information in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b9e7e10-0ee5-4e9a-a73c-440fb2fa7c41",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGjkRD1oL3TCCpTHLyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6608e82c-9ff6-490c-81fc-62854565054c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR71HYz5DkrCpX3Efh36Jf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-30T06:22:29.139Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K46f88LSgUFqbiXuwqTrg6`</summary>

```json
{
  "url": "https://transformer-circuits.pub/2025/attribution-graphs/methods.html",
  "prompt": "Extract all technical details from this paper: 1) The exact problem/gap they identified in circuit tracing, 2) Their key innovation (attribution graphs with cross-layer transcoders), 3) How cross-layer transcoders differ from standard SAEs, 4) How they trace complete computational chains, 5) What circuits they demonstrated (multi-step reasoning, hallucination, planning), 6) The scale of models they applied this to, 7) Open-sourced tools and capabilities, 8) Limitations they acknowledge. Be thorough and specific with technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6608e82c-9ff6-490c-81fc-62854565054c",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGjkRD1oL3TCCpTHLyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0caea856-679a-40b9-89fb-251db26f59cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR71HYz5DkrCpX3Efh36Jf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-30T06:22:30.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RpjqLL5SrigvT3Ch94XkHX`</summary>

```json
{
  "query": "Anthropic \"Circuit Tracing\" \"attribution graphs\" cross-layer transcoders 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0caea856-679a-40b9-89fb-251db26f59cf",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGjkRD1oL3TCCpTHLyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0a7605a-131b-437e-b006-f3257e9a5eb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR71HYz5DkrCpX3Efh36Jf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-30T06:22:30.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014hPKrqsiHkcQ5DbSAFNtwT`</summary>

```json
{
  "query": "Anthropic circuit tracing Claude 3.5 Haiku attribution graphs blog post 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0a7605a-131b-437e-b006-f3257e9a5eb2",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGjkRD1oL3TCCpTHLyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a99dc2a9-55a6-4951-a908-f281f13ac848",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR71HYz5DkrCpX3Efh36Jf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-30T06:22:38.563Z_

<details><summary>↩ Tool result · `toolu_014hPKrqsiHkcQ5DbSAFNtwT`</summary>

```text
Web search results for query: "Anthropic circuit tracing Claude 3.5 Haiku attribution graphs blog post 2025"

Links: [{"title":"On the Biology of a Large Language Model","url":"https://transformer-circuits.pub/2025/attribution-graphs/biology.html"},{"title":"This AI Paper from Anthropic Introduces Attribution Graphs: A New Interpretability Method to Trace Internal Reasoning in Claude 3.5 Haiku - MarkTechPost","url":"https://www.marktechpost.com/2025/04/06/this-ai-paper-from-anthropic-introduces-attribution-graphs-a-new-interpretability-method-to-trace-internal-reasoning-in-claude-3-5-haiku/"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"},{"title":"On the Biology of a Large Language Model – Review | Hun Tae Kim","url":"https://ht0324.github.io/blog/2025/biology/"},{"title":"Inside Claude 3.5 Haiku: How Circuit Tracing Uncovered 30 Million Signals Inside AI’s Mind | by R. Thompson (PhD) | Apr, 2025 | Medium","url":"https://medium.com/@rogt.x1997/inside-claude-3-5-haiku-how-circuit-tracing-uncovered-30-million-signals-inside-ais-mind-eeb2219175dc"},{"title":"Anthropic: Circuit Tracing – Revealing Computational Graphs in Language Models","url":"https://ibl.ai/blog/anthropic-circuit-tracing-revealing-computational-graphs-in-language-models"},{"title":"Tracing the thoughts of a large language model","url":"https://www.anthropic.com/research/tracing-thoughts-language-model"},{"title":"Tracing the thoughts of a large language model","url":"https://simonwillison.net/2025/Mar/27/tracing-the-thoughts-of-a-large-language-model/"},{"title":"Secrets Of Anthropic’s Claude 3.5 Haiku AI Model - Moor Insights & Strategy","url":"https://moorinsightsstrategy.com/poetry-and-deception-secrets-of-anthropics-claude-3-5-haiku-ai-model/"}]

Based on the web search results, I found substantial information about Anthropic's circuit tracing research on Claude 3.5 Haiku with attribution graphs:

## Overview

Anthropic applied attribution graphs to study Claude 3.5 Haiku, released in October 2024, which serves as Anthropic's lightweight production model. Anthropic shared two new papers representing progress on developing a "microscope" to understand AI biology, with the first paper linking interpretable concepts ("features") inside a model into computational "circuits", revealing parts of the pathway that transforms words going into Claude into words that come out.

## Attribution Graphs Method

Attribution graphs allow researchers to partially trace the chain of intermediate steps that a model uses to transform a specific input prompt into an output response, and they generate hypotheses about the mechanisms used by the model, which are tested through follow-up perturbation experiments.

## Key Research Findings

The research uncovered several sophisticated strategies:

- Claude 3.5 Haiku routinely uses multiple intermediate reasoning steps "in its head" during the forward pass to decide its outputs, displays signs of forward planning by considering multiple possibilities for what it will say well in advance, and performs backward planning by working backwards from goal states to formulate earlier parts of its response.

- The shared circuitry between languages increases with model scale, with Claude 3.5 Haiku sharing more than twice the proportion of its features between languages as compared to a smaller model.

- The research uncovered circuit mechanisms that allow the model to distinguish between familiar and unfamiliar entities, and "misfires" of this circuit can cause hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a99dc2a9-55a6-4951-a908-f281f13ac848",
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "eb97f611-9414-4451-b4e7-75b55a687614",
  "sourceToolAssistantUUID": "a99dc2a9-55a6-4951-a908-f281f13ac848",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:22:39.872Z_

<details><summary>↩ Tool result · `toolu_01RpjqLL5SrigvT3Ch94XkHX`</summary>

```text
Web search results for query: "Anthropic "Circuit Tracing" "attribution graphs" cross-layer transcoders 2025"

Links: [{"title":"Circuit Tracing and Attribution Graphs | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/circuit-tracing/"},{"title":"The Circuits Research Landscape: Results and Perspectives - August 2025 ｜ Neuronpedia","url":"https://www.neuronpedia.org/graph/info"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"},{"title":"Anthropic: Circuit Tracing – Revealing Computational Graphs in Language Models","url":"https://ibl.ai/blog/anthropic-circuit-tracing-revealing-computational-graphs-in-language-models"},{"title":"Anthropic Open-Sources Tool to Trace the \"Thoughts\" of Large Language Models - InfoQ","url":"https://www.infoq.com/news/2025/06/anthropic-circuit-tracing/"},{"title":"Replicating Circuit Tracing for a Simple Known Mechanism","url":"https://www.goodfire.ai/research/replicating-circuit-tracing-for-a-simple-mechanism"},{"title":"On the Biology of a Large Language Model – Review | Hun Tae Kim","url":"https://ht0324.github.io/blog/2025/biology/"},{"title":"CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/pdf/2603.21014"}]

Based on the search results, here's what I found about Anthropic's Circuit Tracing, attribution graphs, and cross-layer transcoders from 2025:

## Core Methodology

The approach has two parts: build a replacement model where MLPs are replaced by cross-layer transcoders, then trace backward from the output through the feature network. Attribution graphs combined cross-layer transcoders with backward Jacobian tracing to build complete feature-level circuit maps.

## Key Research

In March 2025, Anthropic published a paper titled "Circuit Tracing: Revealing Computational Graphs in Language Models." This approach uses replacement models and Cross-Layer Transcoders to connect low-level features with high-level behaviors.

## Applications and Adoption

The researchers used attribution graphs on Anthropic's Claude 3.5 Haiku model to study how it behaves across different tasks. In the case of poem generation, they discovered that the model doesn't just generate the next word. It engages in a form of planning, both forward and backward.

Participants in the Anthropic Fellows program released the Circuit Tracer library, which initially supported Gemma-2-2B and Llama-3.1-1B, and now Qwen3-4B as well. The initial release used per-layer transcoders (PLTs), and more recently cross-layer transcoder (CLT) support has been added.

## Impact on the Field

Cross-Layer Transcoders (CLTs) address redundancy issues by sharing features across layers while allowing layer-specific decoding. This reduces redundancy and produces much more compact and interpretable attribution graphs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0a7605a-131b-437e-b006-f3257e9a5eb2",
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "5f37e084-36aa-4b9c-993f-41a89db3e7fc",
  "sourceToolAssistantUUID": "a0a7605a-131b-437e-b006-f3257e9a5eb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:22:44.340Z_

<details><summary>↩ Tool result · `toolu_01K46f88LSgUFqbiXuwqTrg6`</summary>

```text
# Circuit Tracing: Technical Deep Dive

## 1. Problem/Gap Identified

The core challenge was that "model neurons are often polysemantic — representing a mixture of many unrelated concepts." This made it difficult to understand language model computations at a granular level. Previous approaches either used raw neurons (which activate for multiple unrelated concepts) or gross components like entire MLP blocks (which play multifaceted roles across data distributions).

## 2. Key Innovation: Attribution Graphs with Cross-Layer Transcoders

The authors introduced a methodology combining:
- **Attribution graphs**: causal computational graphs depicting feature interactions on specific prompts
- **Cross-layer transcoders (CLTs)**: interpretable replacement components substituting for MLPs across all downstream layers

This creates what they call a "local replacement model" that exactly matches the original model's activations on a given prompt while using interpretable feature-level units.

## 3. Cross-Layer Transcoders vs. Standard SAEs

Standard sparse autoencoders (SAEs) operate per-layer independently. CLTs differ fundamentally:

> "each feature reads from the model's residual stream at one layer and contributes to the outputs of all subsequent MLP layers"

Features encode at a specific layer but decode across *all* subsequent layers. This cross-layer architecture enables direct feature-feature interaction analysis and substantially reduces computational path lengths in resulting graphs.

## 4. Tracing Complete Computational Chains

The method freezes attention patterns and normalization denominators, then adds error correction terms to achieve exact reconstruction. This converts the model into a fully-connected network where:

> "the activity of each feature is the sum of its input edges (up to its activation threshold)"

They compute edge weights using backwards Jacobians with stop-gradients on nonlinearities, deriving virtual weights representing linear paths through attention and residual connections.

## 5. Demonstrated Circuits

**In the 18-layer model:**
- Acronym generation (three parallel paths from component words)
- Factual recall (Michael Jordan → basketball)
- Two-digit addition (parallel low/medium/high-precision heuristics)

**In Claude 3.5 Haiku companion paper:**
- Multi-hop reasoning (Dallas → Texas → Austin)
- Planning in poetry (pre-selecting rhyme options)
- Multilingual circuits (language-specific and abstract pathways)
- Medical diagnosis (candidate hypothesis generation)
- Hallucination mechanisms (familiar vs. unfamiliar entity distinction)
- Refusal circuits (general-purpose harmful-request features)
- Chain-of-thought faithfulness analysis

## 6. Model Scale

- **Small model**: 18-layer transformer ("18L")
- **Frontier model**: Claude 3.5 Haiku (applied in companion paper)
- **Feature dictionary sizes**: 300K–10M features for 18L; 300K–30M for Haiku
- **Largest 18L CLT**: 50% next-token prediction match on diverse prompts

## 7. Open-Sourced Tools

The paper explicitly shares:
- "We have found that this improves circuit interpretability...enough to justify the investment"
- Front-end code for the interactive graph analysis interface on GitHub (attribution-graphs-frontend)
- CLT implementation guidance in appendices
- Graph pruning methodology details
- Interactive visualization interface for exploring attribution graphs

## 8. Key Limitations Acknowledged

**Attention circuits**: "Our graphs do not attempt to explain how the model's attention patterns were formed." QK-circuits remain opaque; the method only captures OV-circuit effects.

**Reconstruction errors**: Only explains ~61% end-to-end paths in best cases; substantial "dark matter" remains unexplained.

**Inactive features**: Cannot explain what models *don't* activate—suppression motifs are hard to identify.

**Graph complexity**: Even pruned graphs contain hundreds of nodes and tens of thousands of edges.

**Abstraction mismatch**: Feature splitting and polysemanticity mean features often aren't at the right level for understanding.

**Global circuits**: Methods work well for single-prompt attribution but struggle generalizing across many inputs (interference problem with virtual weights).

**Mechanistic faithfulness**: Perturbation effects become inconsistent across layers; directional consistency (~0.8 cosine similarity one layer out) compounds poorly downstream.

The authors emphasize: "These limitations...are a promising direction for future work."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0caea856-679a-40b9-89fb-251db26f59cf",
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "4c1f23c6-2ed3-4f61-95d2-370c962f8bdb",
  "sourceToolAssistantUUID": "0caea856-679a-40b9-89fb-251db26f59cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:22:46.661Z_

Let me fetch the companion "biology" paper and the Anthropic blog post for additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c1f23c6-2ed3-4f61-95d2-370c962f8bdb",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGmPgqTD2TUZbaZ2qPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15330b2d-deac-4f44-8915-d0fa7d66b054",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMcS6rxSzdWqvaC8mb9pVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1833,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 10144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-30T06:22:49.974Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F6UQUdqMynNpnULCyDyZn7`</summary>

```json
{
  "url": "https://transformer-circuits.pub/2025/attribution-graphs/biology.html",
  "prompt": "Extract key details about: 1) circuits demonstrated (multi-step reasoning, hallucination, planning), 2) scale of application to Claude 3.5 Haiku, 3) specific findings about hallucination circuits, planning circuits, and multi-hop reasoning, 4) open-sourced tools, 5) limitations acknowledged. Be specific with technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15330b2d-deac-4f44-8915-d0fa7d66b054",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGmPgqTD2TUZbaZ2qPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e990246b-1dfc-44e0-bc1e-f245ddcdd327",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMcS6rxSzdWqvaC8mb9pVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1833,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 10144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T06:22:51.655Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0159LqRDhyyRbi4sAvN3gJqR`</summary>

```json
{
  "url": "https://www.anthropic.com/research/tracing-thoughts-language-model",
  "prompt": "Extract details about: open-sourced tools and their capabilities, the key findings about circuit tracing, and any limitations or caveats mentioned. Also extract any details about the scale of work (feature counts, model size)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e990246b-1dfc-44e0-bc1e-f245ddcdd327",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGmPgqTD2TUZbaZ2qPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d853c91f-a0da-481f-91c0-b33c465204d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMcS6rxSzdWqvaC8mb9pVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1833,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 10144,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1833,
          "output_tokens": 302,
          "cache_read_input_tokens": 10144,
          "cache_creation_input_tokens": 1374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1374,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:22:59.609Z_

<details><summary>↩ Tool result · `toolu_01F6UQUdqMynNpnULCyDyZn7`</summary>

```text
# Key Details from "On the Biology of a Large Language Model"

## 1) Circuits Demonstrated

The paper reveals several sophisticated internal mechanisms:

**Multi-step Reasoning**: The model performs genuine two-hop reasoning internally. When completing "the capital of the state containing Dallas is," the model represents Texas as an intermediate step rather than relying solely on memorization, confirmed through feature inhibition and swapping experiments.

**Planning Circuits**: In poetry generation, the model engages in forward planning by identifying candidate end-of-line words at the beginning of each line, then uses these representations to structure intermediate words to reach the planned target.

**Hallucination Prevention**: The model activates "can't answer" features by default for unfamiliar entities, which are suppressed by "known answer" features when the model recognizes an entity. Hallucinations occur when known-entity features misfire despite insufficient knowledge.

## 2) Scale of Application to Claude 3.5 Haiku

The research specifically targets "Claude 3.5 Haiku — Anthropic's lightweight production model" released October 2024. The authors employed a cross-layer transcoder (CLT) architecture containing "30 million features across all layers" to create interpretable replacement models.

## 3) Specific Findings

**Multi-hop Reasoning**: "Dallas features activate Texas features, which jointly with capital features promote saying Austin" through multiple pathways including a direct shortcut.

**Planning Mechanisms**: "Planned word features activate before writing each line," with the model restructuring sentences when planned words are edited.

**Hallucination Circuits**: The authors discovered that "known answer features activate weakly for Andrej Karpathy despite lacking specific paper knowledge," causing the model to guess plausibly but falsely.

## 4) Open-Sourced Tools

The paper provides an interactive attribution graph interface for exploring mechanisms. Readers can access detailed visualizations of computational pathways, though the authors note this requires time to master.

## 5) Acknowledged Limitations

The authors emphasize their methods provide insights for approximately one-quarter of tested prompts. Key limitations include:

- Attribution graphs represent "hypotheses about mechanisms" requiring validation through intervention experiments
- The replacement model "incompletely and imperfectly captures" the original model
- Attention circuit mechanisms remain largely invisible to their current methodology
- Results constitute "existence proofs" rather than systematic guarantees about mechanism prevalence
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e990246b-1dfc-44e0-bc1e-f245ddcdd327",
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "0c748bbc-d243-4a3d-934c-30a061adeb41",
  "sourceToolAssistantUUID": "e990246b-1dfc-44e0-bc1e-f245ddcdd327",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T06:23:04.767Z_

<details><summary>↩ Tool result · `toolu_0159LqRDhyyRbi4sAvN3gJqR`</summary>

```text
# Analysis of Anthropic's Interpretability Research

## Open-Sourced Tools and Capabilities

The article does not indicate that Anthropic has open-sourced any tools as part of this research. Instead, it references two papers available at transformer-circuits.pub describing their methods, but these appear to be publications rather than open-source software releases. The work focuses on developing an interpretability "microscope" for examining model internals, but no publicly available implementation is mentioned.

## Key Findings About Circuit Tracing

The research reveals several important discoveries:

1. **Multilingual Processing**: Claude employs "a kind of universal 'language of thought'" with shared conceptual features across languages like English, French, and Chinese, with larger models showing greater cross-lingual feature sharing.

2. **Planning Ahead**: Contrary to initial expectations, Claude demonstrates forward planning—notably in poetry writing, where it "thinks of possible rhyming words in advance and writes the next line to get there."

3. **Reasoning Fidelity Issues**: The model sometimes produces "plausible-sounding argument[s]" that don't reflect actual computational steps, particularly when given incorrect hints or asked difficult questions.

4. **Multi-Step Reasoning**: Claude combines independent facts rather than merely retrieving memorized answers, as demonstrated in geographic reasoning tasks.

5. **Hallucination Mechanisms**: Refusal to answer is the default behavior; hallucinations occur when "known entity" features incorrectly override the default reluctance.

## Limitations and Caveats

The researchers acknowledge significant constraints: "Even on short, simple prompts, our method only captures a fraction of the total computation performed by Claude." Additionally, "the mechanisms we do see may have some artifacts based on our tools which don't reflect what is going on in the underlying model."

Scalability remains problematic—"It currently takes a few hours of human effort to understand the circuits we see, even on prompts with only tens of words."

## Scale of Work

Specific feature counts or comprehensive model size details aren't provided in this article, though the research examines Claude 3.5 Haiku and discusses "ten crucial model behaviors."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d853c91f-a0da-481f-91c0-b33c465204d6",
  "isSidechain": true,
  "promptId": "f2aced3c-8af5-4f18-a915-b072b63e4ea7",
  "agentId": "a9226866692b579ca",
  "type": "user",
  "uuid": "2693013e-53c3-4cc5-af85-f1ae0316d6a9",
  "sourceToolAssistantUUID": "d853c91f-a0da-481f-91c0-b33c465204d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-30T06:23:44.304Z_

Here is the report.

---

**Circuit Tracing: Revealing Computational Graphs in Language Models (Anthropic, March 2025)**

**Problem/Gap Identified.** Model neurons are polysemantic -- a single neuron fires for many unrelated concepts -- making it impossible to trace computations at a meaningful granularity. Prior work used either raw neurons (too entangled) or gross components like entire MLP blocks (too coarse). Sparse autoencoders (SAEs) improved matters by extracting monosemantic features, but standard per-layer SAEs operate independently at each layer, creating redundant features and long, hard-to-follow attribution paths through the network.

**Key Innovation: Attribution Graphs with Cross-Layer Transcoders.** The authors build a "local replacement model" that exactly matches the original model's activations on a given prompt while substituting all MLPs with a single cross-layer transcoder (CLT). They freeze attention patterns and normalization denominators, then add error-correction terms for exact reconstruction. The result is a fully-connected feature network where each feature's activity equals the sum of its input edges (up to an activation threshold). They compute edge weights via backward Jacobians with stop-gradients on nonlinearities, yielding "virtual weights" that represent linear paths through attention and residual connections. The resulting attribution graph is a causal computational graph depicting feature-to-feature interactions on a specific prompt.

**How CLTs Differ from Standard SAEs.** Standard SAEs encode and decode within a single layer independently. A CLT feature reads from the residual stream at one layer but contributes to MLP outputs at all subsequent layers. This cross-layer architecture eliminates redundant copies of the same concept at different layers, drastically shortens computational path lengths in attribution graphs, and enables direct feature-to-feature interaction analysis without layer-by-layer chaining.

**Tracing Complete Computational Chains.** After constructing the replacement model, the method traces backward from the output token through the feature network. Graph pruning removes low-weight edges, producing a subgraph of hundreds of nodes and thousands of edges. Researchers then inspect this subgraph -- examining feature labels, activation patterns, and edge weights -- to form mechanistic hypotheses, which are validated through perturbation experiments (feature inhibition, swapping, editing).

**Demonstrated Circuits.** On an 18-layer research model: acronym generation (parallel paths from component words), factual recall (Michael Jordan to basketball), and two-digit addition (parallel low/medium/high-precision heuristics). On Claude 3.5 Haiku (30 million features across all layers): multi-hop reasoning (Dallas activates Texas features, which jointly with capital features promote Austin -- confirmed by inhibition experiments); forward and backward planning in poetry (the model pre-selects candidate rhyming words before writing a line, then structures intermediate words to reach them); hallucination mechanisms (a "can't answer" feature fires by default for unfamiliar entities but is suppressed by "known entity" features -- hallucinations occur when known-entity features misfire despite insufficient knowledge, e.g., for Andrej Karpathy); multilingual shared circuitry (a universal "language of thought" with cross-lingual feature sharing that increases with scale); chain-of-thought faithfulness analysis (the model sometimes produces plausible-sounding arguments that do not reflect actual internal computation); and refusal circuits (general-purpose harmful-request features).

**Scale.** The methods paper uses an 18-layer transformer with CLT dictionaries of 300K to 10M features. The companion biology paper applies the technique to Claude 3.5 Haiku (Anthropic's production model, released October 2024) with a 30-million-feature CLT. The largest 18L CLT achieved ~50% next-token prediction match on diverse prompts.

**Open-Sourced Tools.** Anthropic released the front-end code for their interactive attribution graph visualization interface on GitHub (attribution-graphs-frontend). The community has also built on this: the Circuit Tracer library (from Anthropic Fellows) supports Gemma-2-2B, Llama-3.1-1B, and Qwen3-4B with both per-layer transcoders and CLTs, and a third-party CLT-Forge library provides scalable CLT training.

**Acknowledged Limitations.** (1) Attention circuits are invisible -- the method captures OV-circuit effects but cannot explain how attention patterns (QK circuits) are formed. (2) Reconstruction explains only ~61% of end-to-end paths at best; substantial "dark matter" remains. (3) Inactive features and suppression motifs are hard to identify. (4) Even pruned graphs contain hundreds of nodes and tens of thousands of edges, requiring hours of human effort per prompt. (5) Feature splitting and residual polysemanticity mean features are often at the wrong abstraction level. (6) The method works for single-prompt attribution but struggles to generalize across inputs (interference in virtual weights). (7) Directional consistency (~0.8 cosine similarity one layer out) compounds poorly across many layers. (8) Results are "existence proofs" providing insight on roughly one-quarter of tested prompts, not systematic guarantees.

Sources:
- [Methods paper](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
- [Biology companion paper](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
- [Anthropic blog post](https://www.anthropic.com/research/tracing-thoughts-language-model)
- [Towards Data Science overview](https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/)
- [InfoQ coverage](https://www.infoq.com/news/2025/06/anthropic-circuit-tracing/)
- [CLT-Forge library](https://arxiv.org/pdf/2603.21014)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2693013e-53c3-4cc5-af85-f1ae0316d6a9",
  "isSidechain": true,
  "agentId": "a9226866692b579ca",
  "requestId": "req_011CbYGnu4wfze4bNp29yX9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c2e105d-f8c5-4066-8d84-29c3da0acb93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "555eb8fb-8845-4b6c-b693-68f6f834c71a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTCMLetMgfYMxzEJ6NKhAT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 11518,
      "output_tokens": 1370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3210
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1370,
          "cache_read_input_tokens": 11518,
          "cache_creation_input_tokens": 3210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3210,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
