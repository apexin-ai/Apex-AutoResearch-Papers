# Research conversation: You are a senior ML researcher. Research the paper "Circuit Tracing: Revealing Computational Graphs in Language Models" 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8229769393fca3c5.jsonl`
- **Structured JSON:** [`cd4160dd90ef8986921a.json`](../../sessions/cd/cd4160dd90ef8986921a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-30T06:19:33.094Z_

You are a senior ML researcher. Research the paper "Circuit Tracing: Revealing Computational Graphs in Language Models" by Emmanuel Ameisen, Jack Lindsey, Adam Pearce et al. (Anthropic), March 2025, published at https://transformer-circuits.pub/2025/attribution-graphs/methods.html

Use WebSearch and WebFetch to:
1. Read the paper/technical report content from transformer-circuits.pub
2. Search for commentary, blog posts, or discussions about this work
3. Find details about cross-layer transcoders (CLTs) and attribution graphs

For each search/fetch, extract:
- The exact problem gap they identified and HOW they identified it
- The key insight that others missed (particularly re: cross-layer transcoders vs standard SAEs)
- How they formulated the problem differently from prior circuit discovery work
- What existing techniques they adapted/combined (transcoders, attribution, sparse autoencoders)
- Technical method details: What are cross-layer transcoders? How do attribution graphs work? How do they trace circuits end-to-end? What scale do they operate at?
- Limitations and open questions
- Building blocks (reusable methods/tools/datasets)

Report all findings in detail. Be thorough but focus on HOW they innovate, not just WHAT they did.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "b3bcfa54-5ad3-4073-bf62-361dd5e52df8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:19:33.097Z_

```json
{
  "parentUuid": "b3bcfa54-5ad3-4073-bf62-361dd5e52df8",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
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
  "uuid": "3da7868b-e1f6-4add-b972-dd47e198d8c4",
  "timestamp": "2026-05-30T06:19:33.097Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:19:33.098Z_

```json
{
  "parentUuid": "3da7868b-e1f6-4add-b972-dd47e198d8c4",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "383a8a62-60b1-4f65-a996-d31844d65331",
  "timestamp": "2026-05-30T06:19:33.098Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:19:35.742Z_



I'll research this paper thoroughly using web search and fetch. Let me start by fetching the paper directly and searching for commentary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "383a8a62-60b1-4f65-a996-d31844d65331",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGXHvgEmjrzGPvwuzsa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e347bd9-fac7-42e6-bdb1-072c5d839df4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nk4khu3JQA3Pth5ps1vC3s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1646,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1646,
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

_source line 5 · 2026-05-30T06:19:36.135Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01H3euU4t6Nipwjm3VcAxeHP`</summary>

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
  "parentUuid": "8e347bd9-fac7-42e6-bdb1-072c5d839df4",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGXHvgEmjrzGPvwuzsa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40f5ba64-3e5c-429d-bae7-b2c813f062c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nk4khu3JQA3Pth5ps1vC3s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1646,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1646,
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

_source line 6 · 2026-05-30T06:19:36.138Z_

<details><summary>↩ Tool result · `toolu_01H3euU4t6Nipwjm3VcAxeHP`</summary>

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
  "parentUuid": "40f5ba64-3e5c-429d-bae7-b2c813f062c2",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "1923bb53-f096-4948-8928-0249fe9c910f",
  "sourceToolAssistantUUID": "40f5ba64-3e5c-429d-bae7-b2c813f062c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:19:38.293Z_



Now let me fetch the paper directly and search for commentary in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1923bb53-f096-4948-8928-0249fe9c910f",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGXXUzzBuxsCaFtbrwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42f3612d-1845-4f80-8c99-e5d3e56d738c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKoGXEZpXh6Fb6v1iziFw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 8 · 2026-05-30T06:19:44.639Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LWSzaRZUczeqFkZMaM4zL1`</summary>

```json
{
  "url": "https://transformer-circuits.pub/2025/attribution-graphs/methods.html",
  "prompt": "Extract the full technical content of this paper. I need:\n1. The exact problem statement and motivation - what gap did they identify?\n2. What are cross-layer transcoders (CLTs)? How do they differ from standard SAEs and transcoders?\n3. How do attribution graphs work? What is the mathematical formulation?\n4. How do they trace circuits end-to-end?\n5. What scale do they operate at (model size, number of features)?\n6. What existing techniques did they adapt or combine?\n7. Key technical details about the attribution method\n8. Limitations and open questions they discuss\n9. Any novel contributions vs prior work on circuit discovery\n10. Building blocks and reusable methods\n\nBe as detailed and technical as possible. Include equations, architecture details, and algorithmic steps."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42f3612d-1845-4f80-8c99-e5d3e56d738c",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGXXUzzBuxsCaFtbrwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79c87f32-d9b8-4ed4-8b9d-e9c24b116f44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKoGXEZpXh6Fb6v1iziFw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 9 · 2026-05-30T06:19:45.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014XNuDfHqSdSXy3FsecEp6f`</summary>

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
  "parentUuid": "79c87f32-d9b8-4ed4-8b9d-e9c24b116f44",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGXXUzzBuxsCaFtbrwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f9d7bad-416e-4430-b45e-b28b033f33b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKoGXEZpXh6Fb6v1iziFw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 10 · 2026-05-30T06:19:45.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0192uUUuNk2Gkph267ZK6tkR`</summary>

```json
{
  "query": "\"cross-layer transcoders\" CLT sparse autoencoders language models interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f9d7bad-416e-4430-b45e-b28b033f33b8",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGXXUzzBuxsCaFtbrwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9517a1c7-9fac-453b-9f2d-6687ca4dfefd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKoGXEZpXh6Fb6v1iziFw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9059,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 9059,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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

_source line 11 · 2026-05-30T06:19:52.932Z_

<details><summary>↩ Tool result · `toolu_014XNuDfHqSdSXy3FsecEp6f`</summary>

```text
Web search results for query: "Anthropic "Circuit Tracing" "attribution graphs" cross-layer transcoders 2025"

Links: [{"title":"Circuit Tracing and Attribution Graphs | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/circuit-tracing/"},{"title":"The Circuits Research Landscape: Results and Perspectives - August 2025 ｜ Neuronpedia","url":"https://www.neuronpedia.org/graph/info"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"},{"title":"Tracing Attention Computation Through Feature Interactions","url":"https://transformer-circuits.pub/2025/attention-qk/index.html"},{"title":"Anthropic Open-Sources Tool to Trace the \"Thoughts\" of Large Language Models - InfoQ","url":"https://www.infoq.com/news/2025/06/anthropic-circuit-tracing/"},{"title":"Replicating Circuit Tracing for a Simple Known Mechanism","url":"https://www.goodfire.ai/research/replicating-circuit-tracing-for-a-simple-mechanism"},{"title":"CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/pdf/2603.21014"},{"title":"On the Biology of a Large Language Model","url":"https://transformer-circuits.pub/2025/attribution-graphs/biology.html"}]

Based on the search results, here's what I found about Anthropic's Circuit Tracing, Attribution Graphs, and Cross-Layer Transcoders from 2025:

## Overview

Attribution graphs combine cross-layer transcoders with backward Jacobian tracing to build complete feature-level circuit maps. The approach has two parts: build a replacement model where MLPs are replaced by cross-layer transcoders, then trace backward from the output through the feature network.

## Cross-Layer Transcoders (CLTs)

Cross-Layer Transcoders address redundancy by sharing features across layers while allowing layer-specific decoding, which reduces redundancy and produces more compact and interpretable attribution graphs.

## Applications and Implementation

Researchers used attribution graphs on Anthropic's Claude 3.5 Haiku model to study how it behaves across different tasks, discovering that in poem generation, the model engages in planning both forward and backward.

Participants in the Anthropic Fellows program released the Circuit Tracer library, which initially supported Gemma-2-2B and Llama-3.1-1B, and now Qwen3-4B as well, initially using per-layer transcoders and more recently adding cross-layer transcoder support.

## Related Work

EleutherAI released a separate attribution graph library (Attribute) which supports CLTs, and Goodfire also implemented CLT-based attribution graphs internally.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f9d7bad-416e-4430-b45e-b28b033f33b8",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "b9830fe9-8e1c-4977-ab47-950cf04074a2",
  "sourceToolAssistantUUID": "5f9d7bad-416e-4430-b45e-b28b033f33b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:19:53.756Z_

<details><summary>↩ Tool result · `toolu_0192uUUuNk2Gkph267ZK6tkR`</summary>

```text
Web search results for query: ""cross-layer transcoders" CLT sparse autoencoders language models interpretability"

Links: [{"title":"CLT-Forge: Scalable Cross-Layer Transcoder Library","url":"https://www.emergentmind.com/papers/2603.21014"},{"title":"Cross-Layer Transcoders and Sparse Autoencoders","url":"https://www.jonvet.com/blog/llm-transcoder-and-saes"},{"title":"Cross-Layer Transcoders are incentivized to learn ...","url":"https://www.lesswrong.com/posts/6CS2NDmoLCFcEJMor/cross-layer-transcoders-are-incentivized-to-learn-unfaithful"},{"title":"CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/pdf/2603.21014"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"[2603.21014] CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/abs/2603.21014"},{"title":"CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/html/2603.21014v1"},{"title":"Cross Layer Transcoders for the Qwen3 LLM Family","url":"https://www.lesswrong.com/posts/cW9AdDm2DZtbXBnvt/cross-layer-transcoders-for-the-qwen3-llm-family"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"Cross Layer Transcoders for the Qwen3 LLM Family — BluelightAI","url":"https://bluelightai.com/blog/clts-for-qwen3"}]

Based on the search results, here's what I found about cross-layer transcoders, sparse autoencoders, and their role in language model interpretability:

## Overview

Transcoders approximate the computation of MLP layers by replacing their dense nonlinear transformations with sparse, linear combinations of interpretable features computed from the same inputs. Cross-Layer Transcoders (CLTs) aim to decompose the MLP within a transformer layer into sparse features and are a sparse approximation of the MLP computation itself.

## Relationship to Sparse Autoencoders

Sparse autoencoders (SAE) are autoencoders trained with sparsity constraints to discover interpretable features in model activations. CLTs are an evolution of Sparse Autoencoders (SAEs), which tried to decompose just the MLP activations.

## How CLTs Work for Interpretability

Cross-layer transcoders base analysis on features that read from the residual stream at one layer and contribute to the outputs of all subsequent MLP layers of the original model, which greatly simplifies the resulting circuits. Computation can be represented as a feature attribution graph, where nodes correspond to features and edges capture causal influence through linear pathways.

## Practical Applications

Cross-Layer Transcoders address redundancy issues by sharing features across layers while preserving layer-specific decoding, yielding more compact representations. Recent implementations like CLT-Forge provide scalable distributed training with model sharding and compressed activation caching, a unified automated interpretability pipeline for feature analysis and explanation, and attribution graph computation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9517a1c7-9fac-453b-9f2d-6687ca4dfefd",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "129c3c42-b712-4d2c-a778-efa0a17af229",
  "sourceToolAssistantUUID": "9517a1c7-9fac-453b-9f2d-6687ca4dfefd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:20:22.429Z_

<details><summary>↩ Tool result · `toolu_01LWSzaRZUczeqFkZMaM4zL1`</summary>

````text
# Circuit Tracing: Technical Summary

## 1. Problem Statement and Motivation

The researchers identified a fundamental challenge in mechanistic interpretability: individual neurons in language models exhibit **polysemanticity** (representing multiple unrelated concepts) and operate in **superposition** (models represent more concepts than they have neurons). This creates a mismatch between basic computational units and meaningful concepts.

Prior approaches using raw neurons proved insufficient for understanding circuits. The gap was that "large components play a multitude of unrelated roles across the data distribution, so [they sought] a more granular decomposition."

## 2. Cross-Layer Transcoders (CLTs)

### Architecture
CLTs consist of sparsely-active features organized into L layers (matching the underlying model):

- **Feature computation at layer ℓ**: 
  ```
  a^ℓ = JumpReLU(W_enc^ℓ · x^ℓ)
  ```
  where x^ℓ is the residual stream and W_enc^ℓ is the encoder matrix.

- **Multi-layer reconstruction**:
  ```
  ŷ^ℓ = Σ(ℓ'=1 to ℓ) W_dec^(ℓ'→ℓ) · a^ℓ'
  ```
  Features from all previous layers (ℓ' ≤ ℓ) contribute to reconstructing MLP outputs at layer ℓ.

### Key Differences from Standard Approaches

| Aspect | Standard SAE | Per-Layer Transcoders | CLTs |
|--------|-------------|---------------------|------|
| **Scope** | Single layer | Individual layers | Cross-layer connectivity |
| **Feature Output** | Limited to same layer | Layer-specific | All downstream layers |
| **Circuit Paths** | Long chains | Extended paths | Collapsed paths |

CLTs achieve ~50% token prediction accuracy on diverse prompts while per-layer transcoders and thresholded neurons show worse Pareto frontiers. This enables studying "direct feature-feature interactions" that would otherwise require tracing through multiple layers.

### Training Objective
```
L_total = L_MSE + λ·L_sparsity

where L_MSE = Σ_ℓ ||ŷ^ℓ - y^ℓ||²
and L_sparsity = λ Σ_ℓ Σ_i tanh(c·||W_dec,i^ℓ|| · a_i^ℓ)
```

**Scale**: Trained on 18-layer and Haiku models with 300K–30M total features across layers.

## 3. Attribution Graphs: Mathematical Formulation

### Node Types
1. **Output nodes** – candidate tokens (up to 95% probability mass)
2. **Intermediate nodes** – active transcoder features at prompt positions
3. **Input nodes** – token embeddings
4. **Error nodes** – unexplained MLP reconstruction residuals

### Edge Weight Computation

For a source feature s at layer ℓ_s and position c_s to target feature t at layer ℓ_t and position c_t:

```
A_(s→t) = a_s · w_(s→t)

where w_(s→t) = Σ(ℓ_s ≤ ℓ < ℓ_t) (W_dec,s^(ℓ_s→ℓ))^T · 
                J^(c_s,ℓ_s→c_t,ℓ_t) · W_enc,t^ℓ_t
```

The Jacobian J uses stop-gradients on all nonlinearities: "the preactivation h_t of any feature node t is simply the sum of its incoming edges."

This ensures **linearity**: all feature preactivations decompose additively into attributed sources.

### Local Replacement Model

For a specific prompt p:
- Substitute CLT for MLP layers
- Freeze attention patterns and normalization denominators from original forward pass
- Add error correction: Δ = true_MLP_output - CLT_reconstruction

Result: A fully connected network spanning tokens where:
- Inputs are one-hot token vectors
- Neurons are active CLT features at each position
- Weights are "virtual weights" through attention and residual paths
- Outputs exactly match underlying model on prompt p

## 4. End-to-End Circuit Tracing Pipeline

**Step 1: Feature Identification**
- Compute CLT feature activations across all prompt positions and layers
- Identify "active" features (those with non-zero post-activation)

**Step 2: Attribution Computation**
- Calculate Jacobians from residual stream positions
- Compute virtual weights between feature pairs
- Compute embeddings-to-features and features-to-logits pathways

**Step 3: Graph Construction**
- Create nodes for embeddings, active features, error terms, logits
- Add edges with weights A_(s→t) = a_s · w_(s→t)
- Include multi-hop paths via feature-to-feature chains

**Step 4: Graph Pruning**
- Use "indirect influence matrix": B = (I - A)^(-1) - I
- Keep nodes/edges contributing >threshold influence to target logit
- Achieve ~10x node reduction while retaining 80% completeness

**Step 5: Validation via Perturbations**
- **Constrained patching**: Modify feature activation in layer range [ℓ-1, ℓ]
- **Iterative patching**: Allow second-order effects across layers
- Measure downstream effects on other features and logits
- Compare to graph predictions using Spearman correlation (0.72 for feature-pairs)

## 5. Scale and Experimental Setup

**Models Studied:**
- 18-layer Transformer ("18L"): 17 MLP layers
- Claude 3.5 Haiku (frontier model)

**Dictionary Sizes:**
- 18L: 300K–10M features (largest: 88 average active features per token)
- Haiku: 300K–30M features (largest: 235 average active per token)

**Datasets:**
- Pretraining-style prompts from open sources
- Common Corpus, The Pile (books removed), LMSYS Chat 1M
- 10,000 two-digit addition problems for arithmetic analysis

## 6. Existing Techniques Adapted

1. **Sparse autoencoders** – Inspiration for feature extraction via sparsity
2. **Transcoders/Crosscoders** – Multi-layer feature architecture
3. **Virtual weights framework** – Decomposing paths through attention
4. **Attribution through Jacobians** – Stop-gradient approach from prior work
5. **Feature visualization** – Examples + logit effects (from Scaling Monosemanticity paper)
6. **Perturbation validation** – Steering features multiplicatively or via sign reversal

Novel integration: CLTs + local replacement models + graph pruning + mechanistic faithfulness evaluation.

## 7. Key Technical Details

### Pruning Algorithm
Normalized unsigned adjacency matrix A where input edges sum to 1. Compute influence via Neumann series: B = A + A² + A³ + ...

Two completion metrics:
- **Completeness**: Fraction of target node inputs from features vs. errors
- **Replacement**: Fraction of full paths from embeddings to logits via features

### Mechanistic Faithfulness Evaluation
- Node-to-logit: Influence score vs. ablation effect (cosine similarity on one-layer effects)
- Feature-pairs: Graph influence vs. downstream activation change (ρ_Spearman = 0.72)
- Full model: Perturbation responses—~0.8 cosine similarity at one layer, degrading over depth

### Feature Interpretation
Three categories:
1. **Input features** – Activate on specific tokens/token categories
2. **Functional features** – Perform operations (e.g., "add 9")
3. **Output features** – Promote specific tokens; labeled "say X"

LLM-based interpretability metrics:
- **Sort Eval**: Can Claude distinguish which of two features activates on novel examples?
- **Contrastive Eval**: Can Claude identify which prompt caused feature activation?

Both improve with scale; CLTs outperform per-layer transcoders and thresholded neurons.

## 8. Limitations and Open Questions

### Primary Limitations

**Missing Attention Circuits**
- "Attribution graphs are constructed...with respect to fixed attention patterns"
- Cannot explain QK-circuits; handles only OV-circuits
- Fails on induction, multiple-choice questions, and any behavior driven by attention pattern changes
- Example: "Aunt Sally" induction fails because graph only shows "Sally token → say Sally" without explaining why attention moved there

**Reconstruction Errors & Dark Matter**
- Largest 18L CLT: 11.5% normalized reconstruction error; Haiku: 21.7%
- Error nodes proliferate; "when the critical computation is missing, attribution graphs won't reveal much"
- Unknown what computation is hidden in reconstruction error

**Inactive Features & Inhibition**
- Method emphasizes active features; misses equally-important inhibitory mechanisms
- Cannot easily identify which features *should* fire but don't
- Polysemantic features complicate interpretation

**Graph Complexity**
- Even pruned graphs: hundreds of nodes, tens of thousands of edges
- Interactive interface helps but still cognitively demanding
- No automated method successfully groups similar features across all use cases

**Feature Abstraction Level**
- Features often split across layers (same concept represented multiple times)
- "Absorption" where polysemantic features overshadow monosemantic ones
- Label ambiguity and feature splitting (see Similar Features & Supernodes appendix)

**Global vs. Local Understanding**
- Method excels at single-prompt attribution graphs
- Global circuits (across many prompts) suffer from **interference**: features never co-activating have large virtual weights
- TWERA (target-weighted expected residual attribution) partially mitigates via co-activation statistics but remains imperfect

**Mechanistic Faithfulness Gap**
- Local replacement model perturbation effects: 0.8 cosine similarity at one layer
- Compounding errors across layers; magnitude effects diverge significantly
- "CLTs have different causal structure than underlying model"—example: Copenhagen feature amplification chains invisible in CLTs

## 9. Novel Contributions vs. Prior Circuit Work

**Prior Work:**
- Circuit identification in vision models (using individual neurons)
- Neuron-based circuits in language (failed due to polysemanticity)
- Per-layer sparse autoencoders
- Framework for understanding attention (A Mathematical Framework)

**Novel Here:**
1. **Cross-layer transcoders** – Consolidated architecture collapsing amplification paths; enables direct feature-feature analysis
2. **Local replacement model** – Achieves mechanistic equivalence on specific prompts via error correction
3. **Structured pruning with influence metrics** – 10x reduction with 20% completeness loss
4. **Mechanistic faithfulness metrics** – Quantitative validation via perturbations (Spearman ρ = 0.72)
5. **Interactive visualization interface** – Enables exploration of millions-edge graphs
6. **Global weights analysis** – Virtual weights + TWERA addressing interference problem
7. **Systematic evaluation framework** – LLM-based interpretability, path length, replacement/completeness scores
8. **Companion paper on frontier model** – Nine detailed behavioral case studies on Claude 3.5 Haiku

## 10. Reusable Building Blocks

**Modular Components (can be remixed):**

1. **Feature Extraction**: Any sparse coding method (SAE, per-layer transcoder, CLT)
2. **Attribution Method**: Jacobian stop-gradients + virtual weight composition
3. **Graph Construction**: Node types + edge weight formula (model-agnostic)
4. **Pruning Strategy**: Influence matrix approach (independent of feature type)
5. **Visualization**: Interactive interface (open-sourced on GitHub)
6. **Validation**: Constrained/iterative patching + downstream effect measurement

**Key Formulas for Implementation:**

```
Virtual Weight: V_st = <Σ_ℓ W_dec^s,ℓ, W_enc^t>

Indirect Influence: B = (I - A)^(-1) - I

Completeness: Σ_e B^ℓ_t,e / Σ_e B^∞_t,e (normalized)

TWERA: V^TWERA_ij = [E[a_j·a_i] / E[a_j]] · V_ij
```

---

**Cost-Benefit**: Significant upfront training cost (amortized over multiple circuit analyses) yields interpretability and parsimony improvements justifying the investment for mechanistic understanding at scale.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79c87f32-d9b8-4ed4-8b9d-e9c24b116f44",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "36bb543f-34b7-4f58-ae29-be895c1d72f2",
  "sourceToolAssistantUUID": "79c87f32-d9b8-4ed4-8b9d-e9c24b116f44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:20:26.986Z_

Excellent. Now let me fetch more detailed content -- the companion biology paper, the LessWrong criticism, and the Towards Data Science analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36bb543f-34b7-4f58-ae29-be895c1d72f2",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGavzx5VtAWhdTToCZ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e262b3a-b201-4cfb-85bc-f00811a01ab0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Syf2S2TRyMiktn85bVEihg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1695,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 10188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 15 · 2026-05-30T06:20:30.801Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0133KCg2CmR3uaY2qVPCXPzV`</summary>

```json
{
  "url": "https://transformer-circuits.pub/2025/attribution-graphs/biology.html",
  "prompt": "Extract the key findings from this companion paper \"On the Biology of a Large Language Model\". Focus on:\n1. What specific behaviors/circuits did they discover using attribution graphs on Claude 3.5 Haiku?\n2. What surprising findings emerged?\n3. What does this reveal about model internals that wasn't known before?\n4. Any examples of multi-step reasoning, planning, or emergent computation?\n5. What limitations did they encounter when applying the method?\nBe detailed and technical."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e262b3a-b201-4cfb-85bc-f00811a01ab0",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGavzx5VtAWhdTToCZ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c3f32cf-1422-4a9b-9c32-18ba41f1bd55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Syf2S2TRyMiktn85bVEihg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1695,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 10188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 16 · 2026-05-30T06:20:32.659Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013i7oKuwKKDpJePENnX265N`</summary>

```json
{
  "url": "https://www.lesswrong.com/posts/6CS2NDmoLCFcEJMor/cross-layer-transcoders-are-incentivized-to-learn-unfaithful",
  "prompt": "Extract the full argument about why cross-layer transcoders might learn unfaithful representations. What is the critique? What evidence do they provide? What are the implications for circuit tracing? Be detailed and technical."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3f32cf-1422-4a9b-9c32-18ba41f1bd55",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGavzx5VtAWhdTToCZ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09623cae-3ba4-4c7f-befb-043f0f3ec68b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Syf2S2TRyMiktn85bVEihg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1695,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 10188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 17 · 2026-05-30T06:20:35.110Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012BFYVXC3A4LRH7ENMRMmWX`</summary>

```json
{
  "url": "https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/",
  "prompt": "Extract the analysis of Anthropic's circuit tracing paper. Focus on: How does the author evaluate the contribution? What do they highlight as key innovations? What criticisms or limitations do they raise? What context do they place it in relative to other interpretability work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09623cae-3ba4-4c7f-befb-043f0f3ec68b",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGavzx5VtAWhdTToCZ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c9d4915-3a92-4cd3-af3f-b581bd5347f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Syf2S2TRyMiktn85bVEihg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1695,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 10188,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1695,
          "output_tokens": 508,
          "cache_read_input_tokens": 10188,
          "cache_creation_input_tokens": 3516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3516,
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

_source line 18 · 2026-05-30T06:20:41.412Z_

<details><summary>↩ Tool result · `toolu_012BFYVXC3A4LRH7ENMRMmWX`</summary>

```text
# Analysis of Anthropic's Circuit Tracing Paper

## Evaluation of Contribution

The author positions circuit tracing as "a major milestone on the path to true interpretability," emphasizing its importance for understanding LLM decision-making. The work is framed as addressing a fundamental gap: while LLMs produce sophisticated outputs, their internal reasoning remains opaque.

## Key Innovations Highlighted

1. **Feature-Level Analysis**: Rather than tracking neuron activations, the approach traces features—more fundamental interpretable units. The author notes that "individual neurons are often polysemantic" and composed of these more basic elements.

2. **Transcoders & Replacement Models**: The introduction of cross-layer transcoders that capture effects "across several layers" enables tracking features that span multiple transformer layers.

3. **Attribution Graphs**: The paper's core contribution is a tool visualizing computational paths backward from outputs to inputs using Jacobian analysis.

4. **Concrete Findings**: For poem generation, researchers discovered the model engages in "a form of planning, both forward and backward" rather than purely sequential generation.

## Limitations Raised

The author identifies several critical shortcomings:

- Attribution graphs work only for single inputs, lacking understanding of "global circuits"
- Uncertainty whether transcoders genuinely replicate mechanisms or merely approximate outputs
- The approach only highlights active features while "inactive or inhibitory ones can be just as important"

## Context Within Interpretability Work

Circuit tracing is positioned within mechanistic interpretability research, building on prior work like "Towards Monosemanticity" that established features as interpretable units, representing progress toward understanding LLM internals systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c9d4915-3a92-4cd3-af3f-b581bd5347f9",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "2d6c9b85-de14-4e5a-b8ac-355e618c48be",
  "sourceToolAssistantUUID": "1c9d4915-3a92-4cd3-af3f-b581bd5347f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:20:47.293Z_

<details><summary>↩ Tool result · `toolu_013i7oKuwKKDpJePENnX265N`</summary>

```text
# Cross-Layer Transcoders and Unfaithful Circuit Learning

## The Core Argument

The authors contend that Cross-Layer Transcoders (CLTs) systematically learn to compress multi-step computational pathways into shallow single-hop circuits, obscuring the actual intermediate computations that models perform. This occurs because CLTs' architecture and training objectives create perverse incentives toward depth collapse rather than faithful circuit representation.

## Why This Happens: The Mechanistic Critique

**The "Free Decoder" Problem:**
Once a feature activates in early layers, additional decoder vectors to downstream layers impose minimal sparsity costs. As the authors explain, "additional decoder vectors are almost free" because the penalty applies to concatenated decoders rather than per-layer norms, making width expansion cheaper than activating new features at later layers.

**Loss Function Misalignment:**
CLTs optimize for reconstruction accuracy and sparsity—not intermediate computational fidelity. When shallow approximations match performance with lower sparsity penalties than faithful decompositions, "the CLT is incentivized to learn the shortcut."

## Evidence Presented

**1. Toy Model (Ground Truth):**
The researchers built a 2-layer network computing "(a XOR b) AND (c XOR d)" with known ground-truth circuits. CLTs learned to skip the intermediate layer entirely, instead creating a lookup table that maps inputs directly to outputs via layer-0 features only. Critically, this achieves "perfect reconstruction" while missing actual computational steps—a smoking gun for unfaithfulness.

**2. Asymmetric L0 Across Layers:**
Training CLTs on GPT-2-small reveals layer-0 features activate 3× more frequently than later layers. Per-Layer Transcoders (PLTs) show uniform activation, indicating the asymmetry stems from CLT architecture, not inherent activation geometry.

**3. Attribution Concentration:**
On Gemma-2-2B, CLT attribution circuits show "a sharp jump at layer 1, with nearly all contributions concentrated in layers 0 and 1," whereas PLTs distribute contributions evenly across depth.

**4. Divergent Interpretations (MIT License Case):**
For verbatim memorization, CLTs suggest pure lookup-table behavior, while PLTs reveal intermediate general-purpose features (verb-tense transformation circuits) that interact with memorization mechanisms. These represent fundamentally different mechanistic stories about model computation.

## Implications for Circuit Tracing

**Three Critical Problems:**

1. **Interpretability Collapse:** CLT circuits may show "shallower" mechanisms than actually implemented, potentially missing intermediate reasoning steps that distinguish genuine computation from pattern matching.

2. **Reliability Assessment Failure:** When trying to verify whether models perform actual multi-step reasoning versus sophisticated memorization (crucial for safety evaluation), CLTs may systematically hide intermediate computation, making unfaithful collapse undetectable.

3. **Conflicting Tool Outputs:** Different transcoder architectures (CLT vs. PLT) can produce contradictory mechanistic conclusions about identical behaviors, undermining confidence in circuit-based interpretability claims.

## Core Distinction: Superposition vs. Multi-Step Circuits

The authors identify a crucial diagnostic: true cross-layer superposition occurs when multiple layers reinforce identical features in the same subspace. Multi-step circuits involve intermediate features computed in one layer and transformed by later layers into distinct feature spaces. CLTs cannot reliably distinguish these, conflating legitimate superposition with depth collapse.

## Proposed Mitigations

- **Per-layer decoder norm penalties** (most promising): Sum separate L2 norms instead of concatenated norms, eliminating geometric cost advantages of decoder proliferation
- **L0 asymmetry penalties:** Regularize against extreme activation differences across layers
- **Architectural constraints:** Limit feature span to local windows (e.g., 5 downstream layers) rather than all downstream layers
- **Auxiliary faithfulness losses:** Directly reward feature activations that correlate with actual neuron activations

The authors acknowledge limitations: the toy model may not reflect real language model complexity, Gemma-2-2B evidence remains circumstantial without ground truth, and attention layers warrant separate analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09623cae-3ba4-4c7f-befb-043f0f3ec68b",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "62fa9d0d-f67b-4562-8e85-0a4fba79ef81",
  "sourceToolAssistantUUID": "09623cae-3ba4-4c7f-befb-043f0f3ec68b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:20:47.458Z_

<details><summary>↩ Tool result · `toolu_0133KCg2CmR3uaY2qVPCXPzV`</summary>

```text
# Key Findings from "On the Biology of a Large Language Model"

## 1. Core Discoveries Using Attribution Graphs

The researchers developed **attribution graphs** to trace computational pathways in Claude 3.5 Haiku, revealing how features interact to produce outputs. Key discoveries include:

**Multi-step Reasoning**: The model performs genuine two-hop reasoning internally. When completing "the capital of the state containing Dallas is," the model activates intermediate "Texas" representations before outputting "Austin," rather than using pure memorization shortcuts.

**Forward Planning in Poetry**: The model plans ahead when writing rhyming couplets. Before composing each line, it identifies candidate end-of-line words that satisfy both rhyme scheme and semantic constraints, then structures the entire line around these predetermined targets.

**Language-Independent Circuits**: The model uses a hybrid approach with both language-specific and abstract multilingual components. Interestingly, "English appears mechanistically privileged as the default" despite genuine multilingual feature representations.

## 2. Surprising Findings

**Metacognitive Failures**: The model cannot articulate its own mechanisms. When asked how it computed 36+59=95, it provided a standard carrying algorithm explanation, but internal circuits used entirely different heuristics—"low-precision pathways feed into lookup table features."

**Hallucination as Circuit Misfire**: Hallucinations result from "known entity" features inadvertently suppressing default refusal circuitry. When asked about obscure figures, these inhibitory circuits activate despite the model lacking actual knowledge.

**Attention-Mediated Operations**: Some critical computations occur through attention pattern changes rather than MLP features, creating gaps in interpretability. The multilingual antonym circuit partially operates through "attention—corresponding to dotted lines."

## 3. Novel Insights About Model Internals

**Backward Planning**: Beyond forward planning, models work backward from goal states. In medical diagnosis, the model "identifies candidate diagnoses based on reported symptoms, and uses these to inform follow-up questions."

**Flexible Circuit Reuse**: Addition circuits generalize across vastly different contexts—astronomical measurements, financial tables, academic citations—with the same "lookup table features" serving different computational roles depending on contextual signals.

**Hierarchical Refusal Architecture**: Safety finetuning aggregates pretraining-learned specific harms into general "harmful request" features. The paper notes that "dictionaries trained with only pretraining data had very few refusal features," suggesting finetuning wires together diverse harm concepts.

**Intermediate Representation Tagging**: The model distinguishes intermediate versus final computations through "expression type" features that flag when results like 4+5=9 shouldn't become outputs but remain as intermediate steps.

## 4. Examples of Emergent Computation

**Entity Recognition Decision Tree**: Features represent familiar versus unfamiliar entities, with "unknown name features" activated by default. Known entities suppress these through inhibitory "known answer" features—a circuit that can misfire causing hallucinations.

**Jailbreak Mechanism Deconstruction**: The model doesn't recognize acronym-decoded requests until explicitly saying them: "each independently contributes to output probabilities, collectively voting for BOMB via constructive interference." Critically, harmful request features fire weakly until the model rephrases the request itself.

**Medical Diagnostic Circuits**: The model activates candidate diagnosis features (preeclampsia, cholecystitis) in parallel, then routes through features representing confirmatory symptoms—mirroring differential diagnosis logic.

## 5. Methodological Limitations Identified

**Success Rate Constraints**: "Attribution graphs provide satisfying insight for about a quarter of the prompts we've tried," limiting generalizability claims from case studies.

**Incomplete Mechanistic Capture**: Error nodes represent gaps between replacement models and actual activations. The paper emphasizes these are "hypotheses about mechanisms" requiring validation through perturbation experiments.

**Attention Blindness**: The methodology treats attention patterns as fixed, missing computations in QK circuits. The multilingual circuit "might be seen as a kind of counterexample concretely demonstrating a weakness of our present circuit analysis."

**Inactive Feature Problem**: The method cannot explain why refusal features *don't* activate appropriately. After "BOMB" appears, harmful request features fire at only 10-30% of baseline strength, but "the attribution graph suggests...there are no strong pathways along which the model considers refusing"—precisely when understanding is most important.

**Mechanistic Unfaithfulness Risk**: Multi-hop interventions can diverge from graph predictions because "graph-predicted indirect effects may not even exist within the underlying model," particularly in downstream layers past the intervention point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c3f32cf-1422-4a9b-9c32-18ba41f1bd55",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "4cbbf920-5fa0-4683-bc16-ceef54b10c83",
  "sourceToolAssistantUUID": "1c3f32cf-1422-4a9b-9c32-18ba41f1bd55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:20:54.396Z_

Let me now fetch more details -- the Goodfire replication study, the InfoQ coverage, and the CLT-Forge paper for implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cbbf920-5fa0-4683-bc16-ceef54b10c83",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGd3szdzndMvp58VM5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "163b02cb-d093-47cd-8476-6625d32c81d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TB9nHmoW3UDASxqBYmPbe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1360,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 13704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3373,
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

_source line 22 · 2026-05-30T06:20:57.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y1K5w3aBrzotWThwH9KpcL`</summary>

```json
{
  "url": "https://www.goodfire.ai/research/replicating-circuit-tracing-for-a-simple-mechanism",
  "prompt": "Extract details about Goodfire's replication of circuit tracing. What did they find when implementing CLTs and attribution graphs independently? Did they confirm or challenge Anthropic's findings? What technical details about implementation did they share? What problems did they encounter?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163b02cb-d093-47cd-8476-6625d32c81d7",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGd3szdzndMvp58VM5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63f88dee-bb91-4239-8213-f9e0693ba5a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TB9nHmoW3UDASxqBYmPbe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1360,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 13704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3373,
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

_source line 23 · 2026-05-30T06:20:59.306Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ShVr5pFC3esDENduxhu1ob`</summary>

```json
{
  "url": "https://www.infoq.com/news/2025/06/anthropic-circuit-tracing/",
  "prompt": "Extract the key points about Anthropic's circuit tracing. What does this article highlight about the significance, technical approach, and reception of the work? Any industry reactions or implications mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63f88dee-bb91-4239-8213-f9e0693ba5a7",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGd3szdzndMvp58VM5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5552346e-dde7-43ea-b5dd-1ad7eda77ae5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TB9nHmoW3UDASxqBYmPbe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1360,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 13704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3373,
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

_source line 24 · 2026-05-30T06:20:59.646Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5fD1bs4svzK7rQ9gwBHYP`</summary>

```json
{
  "query": "Anthropic circuit tracing attribution graphs limitations criticism discussion 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5552346e-dde7-43ea-b5dd-1ad7eda77ae5",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGd3szdzndMvp58VM5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dbf9e03-70a5-49ca-87c4-8157b6e09d85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TB9nHmoW3UDASxqBYmPbe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1360,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 13704,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1360,
          "output_tokens": 343,
          "cache_read_input_tokens": 13704,
          "cache_creation_input_tokens": 3373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3373,
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

_source line 25 · 2026-05-30T06:21:04.329Z_

<details><summary>↩ Tool result · `toolu_01Y1K5w3aBrzotWThwH9KpcL`</summary>

```text
# Goodfire's Circuit Tracing Replication: Key Findings

## Overview
Goodfire trained Cross-Layer Transcoders (CLTs) on GPT-2 Small and analyzed the greater-than task to evaluate CLTs' ability to recover known computational mechanisms previously documented by Hanna et al.

## Confirmations
The team successfully identified interpretable features aligned with prior work. Their attribution graphs revealed "a dense concentration of features originating from input token 11 (the final digit of '1711') and flowing toward the final token position," demonstrating CLTs capture relevant computational pathways.

## Novel Discoveries
Beyond confirmation, Goodfire found surprising structures, including abstract parity features—mechanisms that "encode a general representation of conceptual opposition or parity across diverse domains" beyond numerical reasoning. They also identified "structured number features" detecting multiples of 5 and other mathematical patterns.

## Key Divergences
Importantly, their results showed "a somewhat less clean representation space" than Hanna et al.'s original analysis. Some discovered features displayed extreme input dependence (e.g., Feature 349410 activating only for input year 11), appearing as "special-case lookups" rather than generalizable computational primitives.

## Technical Challenges
A significant limitation emerged: discrepancies between logit attribution heatmaps and max-activating examples. Feature 425104 showed strong input-date dependence in examples but weak dependence in attribution analysis, suggesting "features interact in the full model context" in ways single-feature analysis cannot capture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63f88dee-bb91-4239-8213-f9e0693ba5a7",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "0f0b504e-910c-44dd-9496-71587cb4e03d",
  "sourceToolAssistantUUID": "63f88dee-bb91-4239-8213-f9e0693ba5a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-30T06:21:05.679Z_

<details><summary>↩ Tool result · `toolu_01ShVr5pFC3esDENduxhu1ob`</summary>

```text
# Anthropic's Circuit Tracing Tool: Key Insights

## Significance
Anthropic has released an open-source tool for understanding LLM internal processes during inference—addressing a critical gap in AI safety and interpretability research.

## Technical Approach
The method replaces standard neural networks with ones using "sparsely-active features from cross-layer MLP transcoders." This generates attribution graphs by identifying which features influence specific outputs. The library computes "the direct effect that each non-zero transcoder feature...has on each other non-zero transcoder feature and output logit."

The approach builds intermediate computational steps into visual graphs, revealing how models reason through problems.

## Significance for Safety
Trenton Bricken from Anthropic emphasizes this represents a "key contribution to LLM mechanistic interpretability"—understanding core computational units within models. He frames this as essential: "we might not be in the place where we can prove from the ground up that everything is safe" currently, but establishing this goal serves as a "powerful reassuring North Star."

## Industry Reception
The work has generated interest in the research community, with availability through GitHub, Neuronpedia, and tutorial notebooks, making it accessible for broader adoption across open-weights models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5552346e-dde7-43ea-b5dd-1ad7eda77ae5",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "918ca21e-468a-4e13-8e39-655d93718e87",
  "sourceToolAssistantUUID": "5552346e-dde7-43ea-b5dd-1ad7eda77ae5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-30T06:21:08.434Z_

<details><summary>↩ Tool result · `toolu_01F5fD1bs4svzK7rQ9gwBHYP`</summary>

```text
Web search results for query: "Anthropic circuit tracing attribution graphs limitations criticism discussion 2025"

Links: [{"title":"Circuit Tracing for the Rest of Us: From Probes to Attribution Graphs and What It Means for Production Safety | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/circuit-tracing-production/"},{"title":"Anthropic Revolutionizes LLM Debugging With Open-Source Circuit Tracing: Toward Reliable, Explainable Enterprise AI","url":"https://www.thenocodeguy.com/en/blog/anthropic-revolutionizes-llm-debugging-with-open-source-circuit-tracing-toward-reliable-explainable-enterprise-ai/"},{"title":"Anthropic: Circuit Tracing – Revealing Computational Graphs in Language Models","url":"https://ibl.ai/blog/anthropic-circuit-tracing-revealing-computational-graphs-in-language-models"},{"title":"The Circuits Research Landscape: Results and Perspectives - August 2025 ｜ Neuronpedia","url":"https://www.neuronpedia.org/graph/info"},{"title":"Anthropic papers on Circuit Tracing, March 2025 - Awesome paper - Hugging Face Forums","url":"https://discuss.huggingface.co/t/anthropic-papers-on-circuit-tracing-march-2025/164361"},{"title":"ADAG: Automatically Describing Attribution Graphs","url":"https://arxiv.org/pdf/2604.07615"}]

Based on the search results, here's what I found about Anthropic's circuit tracing and attribution graphs, including limitations and criticisms discussed in 2025:

## Overview of Circuit Tracing

Anthropic's 2025 work made the breakthrough of tracing not just what features are active but how they influence each other in sequence, using computational graphs and attribution graphs as key tools.

## Key Limitations and Criticisms

**Resource and Accessibility Issues:**
Circuit tracing currently requires significant memory and compute, posing scaling challenges for production environments. Additionally, attribution graphs and feature maps demand expertise to interpret, potentially limiting accessibility for non-specialists.

**Technical Limitations with Attribution Graphs:**
Interpreting global weights is challenging due to issues like interference (spurious connections) and the lack of accounting for attention-mediated interactions. While attribution graphs provide insights on specific prompts, future work aims to enhance the understanding of global mechanisms and address current limitations.

**Limited Availability:**
Circuit tracing at this resolution isn't available for most open-weight models like Mistral, Gemma, and Qwen, as Anthropic has built these tools for their own models, though the open-source release through Neuronpedia lets you explore attribution graphs on supported Claude models.

**Production Gaps:**
If you're an enterprise team wanting to do circuit-level analysis on your production models today, you're going to hit tooling gaps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dbf9e03-70a5-49ca-87c4-8157b6e09d85",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "405b08f6-df36-400b-858c-06070cb27ec7",
  "sourceToolAssistantUUID": "8dbf9e03-70a5-49ca-87c4-8157b6e09d85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-30T06:21:12.734Z_

Let me get a few more crucial pieces -- the Neuronpedia landscape overview and the attention/QK companion paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "405b08f6-df36-400b-858c-06070cb27ec7",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGeLBYmzxYVTMV8x8Sa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01f4e51c-4bbf-4c02-9067-6e87c7dbf692",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01473HdkgLtyxTGUuaQzMA3a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 17077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3109,
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

_source line 29 · 2026-05-30T06:21:15.098Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GDUi2bTyQC1kD8uuAmAJc5`</summary>

```json
{
  "url": "https://www.neuronpedia.org/graph/info",
  "prompt": "Extract the overview of the circuits research landscape. What does this page say about the state of circuit tracing, attribution graphs, and cross-layer transcoders as of mid-2025? What tools and implementations exist? What are the open problems identified? What is the community consensus on the approach?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01f4e51c-4bbf-4c02-9067-6e87c7dbf692",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGeLBYmzxYVTMV8x8Sa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48e31a65-2093-43dc-85d2-ddceb2c8bc68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01473HdkgLtyxTGUuaQzMA3a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 17077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3109,
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

_source line 30 · 2026-05-30T06:21:16.596Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019chLCR59vHjnCsRoTTaqac`</summary>

```json
{
  "url": "https://transformer-circuits.pub/2025/attention-qk/index.html",
  "prompt": "Extract the key technical content about tracing attention computation through feature interactions. How does this companion paper extend the circuit tracing work? What problem does it solve regarding QK circuits? What methods do they introduce? What are the key findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48e31a65-2093-43dc-85d2-ddceb2c8bc68",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGeLBYmzxYVTMV8x8Sa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a9dba9d-554b-49e8-8e17-ed97dedc027d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01473HdkgLtyxTGUuaQzMA3a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 17077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3109,
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

### Tool result

_source line 31 · 2026-05-30T06:21:23.069Z_

<details><summary>↩ Tool result · `toolu_019chLCR59vHjnCsRoTTaqac`</summary>

```text
# Tracing Attention Computation Through Feature Interactions

## Overview

This companion paper to the Transformer Circuits Thread addresses a critical gap in understanding attention mechanisms. The authors develop methods to explain attention patterns by analyzing how features interact within these components.

## Problem Statement

Standard circuit analysis struggles with QK (Query-Key) circuits in attention heads. These circuits are difficult to interpret because attention patterns emerge from complex interactions between query and key projections that don't decompose neatly into linear attribution.

## Key Methods Introduced

The paper introduces techniques to trace attention computation through feature interactions rather than relying solely on direct attribution. Their approach:

- Analyzes how different feature representations contribute to attention pattern formation
- Maps feature interactions into attribution graphs for clearer visualization
- Extends existing circuit tracing methodology to handle nonlinear attention mechanics

## Main Findings

The authors demonstrate that attention patterns can be explained more effectively by examining feature interactions. This provides:

1. **Improved interpretability** of previously opaque attention head behavior
2. **Integration** of feature interaction analysis into standard attribution frameworks
3. **Better understanding** of how compositional features drive attention outcomes

This work bridges a significant gap between feature-level analysis and circuit-level understanding, enabling researchers to follow information flow more precisely through transformer attention mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a9dba9d-554b-49e8-8e17-ed97dedc027d",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "69588338-d0f3-4918-a941-cf1a12a9dd94",
  "sourceToolAssistantUUID": "8a9dba9d-554b-49e8-8e17-ed97dedc027d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T06:21:25.730Z_

<details><summary>↩ Tool result · `toolu_01GDUi2bTyQC1kD8uuAmAJc5`</summary>

```text
# The Circuits Research Landscape: Mid-2025 Overview

## State of the Field

As of August 2025, circuit tracing has matured from a theoretical framework into an applied methodology. The paper emphasizes a shift from "building microscopes" to "using our many available tools to gain practical insights about models." Attribution graphs—which map feature-to-feature interactions across transformer layers—are now the primary lens for studying LLM mechanisms.

## Available Tools and Implementations

Multiple organizations have independently replicated and extended the core methodology:

- **Circuit Tracer** (Anthropic Fellows): A library supporting per-layer transcoders (PLTs) and cross-layer transcoders (CLTs) across Gemma-2-2B, Llama-3.1-1B, and Qwen3-4B
- **Neuronpedia**: A public interface enabling interactive graph generation without infrastructure requirements; over 7,000 graphs had been generated by publication
- **Attribute** (EleutherAI): An independent attribution graph library using CLTs
- **Goodfire AI**: Internal CLT-based implementation for studying mechanisms in GPT-2

Pre-trained CLTs are publicly available via Hugging Face.

## Key Findings on Transcoders

Research identified important tradeoffs in architecture choices:

- CLTs generally outperform PLTs across relevant sparsity regimes
- JumpReLU and TopK activation functions perform similarly, with TopK offering easier hyperparameter tuning
- Skip connections reduce reconstruction error without improving replacement scores for circuit analysis
- Training-time and pruning-time sparsity work synergistically; optimal approaches "overshoot" desired post-pruning sparsity by approximately 5-10×

## Identified Limitations and Open Problems

The paper acknowledges that transcoders can "shatter" geometric structures in representation spaces, producing per-prompt execution traces rather than general algorithms. Key unresolved questions include:

- Scaling attribution graphs to long contexts (thousands of tokens)
- Automating graph analysis and hypothesis validation
- Understanding variable binding, state tracking, and planning mechanisms
- Distinguishing causal relationships in chain-of-thought reasoning

## Community Consensus

The emerging consensus treats interpretability as a natural science rather than engineering discipline, requiring complementary supervised and unsupervised methods operating at multiple abstraction levels—analogous to biology's hierarchical approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48e31a65-2093-43dc-85d2-ddceb2c8bc68",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "b7cc9085-54e8-4ef0-b9f2-a7f88124c8f9",
  "sourceToolAssistantUUID": "48e31a65-2093-43dc-85d2-ddceb2c8bc68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-30T06:21:28.449Z_

Now let me search for additional technical depth on the virtual weights formulation and the specific innovation of how CLTs differ from prior transcoder work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7cc9085-54e8-4ef0-b9f2-a7f88124c8f9",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGfbWp6GghUViZeyS9m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42139d32-7f8b-417b-9546-2f5f03e5d225",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1H1b4GsuA9jomgQAxCc4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 308,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 20186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 34 · 2026-05-30T06:21:30.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014s1opHZyHsDqobGnC7hkET`</summary>

```json
{
  "query": "transcoders interpretable LLM feature circuits Bricken Dunefsky 2024 original transcoder paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42139d32-7f8b-417b-9546-2f5f03e5d225",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGfbWp6GghUViZeyS9m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e06f2a6-a000-43d7-8d8c-5ea55459129e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1H1b4GsuA9jomgQAxCc4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 308,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 20186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 35 · 2026-05-30T06:21:31.807Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PjMAd34sv5uHH6aqVLaYQC`</summary>

```json
{
  "url": "https://www.jonvet.com/blog/llm-transcoder-and-saes",
  "prompt": "Extract the technical comparison between cross-layer transcoders and sparse autoencoders. What are the key architectural differences? How do transcoders improve on SAEs for circuit discovery? What are the tradeoffs? Include any mathematical formulations or architectural diagrams described."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e06f2a6-a000-43d7-8d8c-5ea55459129e",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGfbWp6GghUViZeyS9m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb80b0b2-674e-4ff3-a4ae-3f4b824e5c67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1H1b4GsuA9jomgQAxCc4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 308,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 20186,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 308,
          "output_tokens": 234,
          "cache_read_input_tokens": 20186,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 853,
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

_source line 36 · 2026-05-30T06:21:37.790Z_

<details><summary>↩ Tool result · `toolu_014s1opHZyHsDqobGnC7hkET`</summary>

```text
Web search results for query: "transcoders interpretable LLM feature circuits Bricken Dunefsky 2024 original transcoder paper"

Links: [{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/html/2406.11944v1"},{"title":"Transcoders Find Interpretable LLM Feature Circuits [Quick Review]","url":"https://liner.com/review/transcoders-find-interpretable-llm-feature-circuits"},{"title":"Transcoders find interpretable LLM feature circuits | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738684"},{"title":"[Paper Note] Transcoders Find Interpretable LLM Feature Circuits, Jacob Dunefsky+, arXiv'24, 2024.06 · Issue #4028 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4028"},{"title":"[2406.11944] Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/abs/2406.11944"},{"title":"Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/pdf/2406.11944"},{"title":"NeurIPS Poster Transcoders find interpretable LLM feature circuits","url":"https://neurips.cc/virtual/2024/poster/95736"},{"title":"Transcoders Find Interpretable LLM Feature Circuits Jacob Dunefsky∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2b8f4db0464cc5b6e9d5e6bea4b9f308-Paper-Conference.pdf"}]

I found the paper for you! Here's what I discovered:

## "Transcoders Find Interpretable LLM Feature Circuits"

The paper was authored by Jacob Dunefsky (Yale University), Philippe Chlenski (Columbia University), and Neel Nanda, and was posted on arXiv on June 17, 2024.

### Main Contribution

The paper introduces transcoders, which seek to faithfully approximate a densely activating MLP layer with a wider, sparsely-activating MLP layer. Transcoders are wide, sparsely-activating ReLU MLPs with one hidden layer, trained to approximate original MLP sublayers' input-output behavior.

### The Problem They Address

MLP sublayers make fine-grained circuit analysis on transformer-based language models difficult. In particular, interpretable features—such as those found by sparse autoencoders (SAEs)—are typically linear combinations of extremely many neurons, each with its own nonlinearity to account for. Circuit analysis in this setting thus either yields intractably large circuits or fails to disentangle local and global behavior.

### Results

Transcoders were successfully trained on language models with 120M, 410M, and 1.4B parameters, and found them to perform at least on par with SAEs in terms of sparsity, faithfulness, and human-interpretability. The authors applied transcoders to reverse-engineer unknown circuits in the model, and obtained novel insights regarding the "greater-than circuit" in GPT2-small.

Code is available at https://github.com/jacobdunefsky/transcoder_circuits/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e06f2a6-a000-43d7-8d8c-5ea55459129e",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "32571728-4e92-410e-8e1d-307a50b0ac19",
  "sourceToolAssistantUUID": "4e06f2a6-a000-43d7-8d8c-5ea55459129e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-30T06:21:38.526Z_

<details><summary>↩ Tool result · `toolu_01PjMAd34sv5uHH6aqVLaYQC`</summary>

```text
# Technical Comparison: Cross-Layer Transcoders vs Sparse Autoencoders

## Architectural Differences

**Sparse Autoencoders (SAEs):**
SAEs operate at a single point in the model—the post-MLP activations. They employ a two-step process: a linear encoder maps n-dimensional MLP activations into m-dimensional space with ReLU activation, then a linear decoder projects back to activation space. The loss function combines reconstruction error (MSE) with sparsity penalties weighted by λ.

**Cross-Layer Transcoders (CLTs):**
CLTs operate across two points: both pre-MLP (residual stream) and post-MLP activations. They use a similar encoder-decoder structure but with critical differences:
- The encoder applies JumpReLU instead of standard ReLU, introducing trainable threshold parameters
- The decoder incorporates outputs from all previous layers: "a weighted sum of decoder vectors" at multiple depth levels
- The loss function spans the entire model depth and uses tanh-based sparsity penalties

## Circuit Discovery Advantages

CLTs enable sparse computational graph construction that SAEs cannot match. As the article explains, SAEs only reveal "what features are important on a given input, but not why," since they don't model MLP computation itself. CLTs allow tracing features backward through layers—identifying which prior-layer features drive activation of downstream features.

## Performance Tradeoffs

The research indicates CLTs achieve "similar pareto frontier" performance to SAEs on standard metrics (interpretability and fidelity), while offering superior explanatory power for circuit analysis. No significant computational overhead disadvantages are mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb80b0b2-674e-4ff3-a4ae-3f4b824e5c67",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "3eeded36-ba09-4b7e-9b61-d7664efae869",
  "sourceToolAssistantUUID": "eb80b0b2-674e-4ff3-a4ae-3f4b824e5c67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-30T06:21:41.073Z_

Let me get one final piece -- the ADAG paper and any more detail on the mathematical formulation of virtual weights.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eeded36-ba09-4b7e-9b61-d7664efae869",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGgYCQs9bwT4isfVLzA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91ca5ecd-f3d5-4191-a086-510d219d7e92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W44ydFz8Kx5WJhUoZg7BV2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1974,
      "cache_read_input_tokens": 21039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1974,
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

_source line 39 · 2026-05-30T06:21:43.058Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Pcg4zFnrczRWXKDXuCruc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.07615",
  "prompt": "Extract the key content of ADAG (Automatically Describing Attribution Graphs). How does this follow-up work extend Anthropic's circuit tracing? What problem does it solve? What methods does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91ca5ecd-f3d5-4191-a086-510d219d7e92",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGgYCQs9bwT4isfVLzA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d6a55eb-1a95-48af-9140-4fe76280de0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W44ydFz8Kx5WJhUoZg7BV2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1974,
      "cache_read_input_tokens": 21039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1974,
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

_source line 40 · 2026-05-30T06:21:43.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VesNdorjgxjmatWALMzCn4`</summary>

```json
{
  "query": "\"virtual weights\" \"attribution graphs\" transformer circuits cross-layer transcoder mathematical formulation jacobian"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d6a55eb-1a95-48af-9140-4fe76280de0f",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGgYCQs9bwT4isfVLzA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ffe4734-7750-4a14-ad90-8cb0f467c8b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W44ydFz8Kx5WJhUoZg7BV2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1974,
      "cache_read_input_tokens": 21039,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 21039,
          "cache_creation_input_tokens": 1974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1974,
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

_source line 41 · 2026-05-30T06:21:47.757Z_

<details><summary>↩ Tool result · `toolu_011Pcg4zFnrczRWXKDXuCruc`</summary>

```text
# ADAG: Automatically Describing Attribution Graphs

## The Problem It Solves

Prior circuit tracing work relied on "ad-hoc human interpretation of the role that each feature in the circuit plays, via manual inspection of data artifacts." ADAG addresses this limitation by fully automating the process of describing and interpreting attribution graphs in language models.

## Key Methods

The system introduces several novel components:

1. **Attribution Profiles**: Quantifies a feature's functional role through its input and output gradient effects.

2. **Clustering Algorithm**: Groups features together based on their attribution profiles.

3. **LLM Explainer-Simulator Setup**: Generates natural-language explanations of feature group roles and scores them for quality.

## What It Achieves

The research demonstrates ADAG can "recover interpretable circuits" on known human-analyzed tasks while also identifying "steerable clusters which are responsible for a harmful advice jailbreak in Llama 3.1 8B Instruct."

## Extension of Prior Work

Rather than a direct Anthropic extension, ADAG builds upon the general circuit tracing methodology by removing the manual interpretation bottleneck, enabling scalable automated analysis of which internal model features drive specific outputs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d6a55eb-1a95-48af-9140-4fe76280de0f",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "7b92037c-3014-4eac-b32d-bbbb5749cd22",
  "sourceToolAssistantUUID": "0d6a55eb-1a95-48af-9140-4fe76280de0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-30T06:21:50.700Z_

<details><summary>↩ Tool result · `toolu_01VesNdorjgxjmatWALMzCn4`</summary>

```text
Web search results for query: ""virtual weights" "attribution graphs" transformer circuits cross-layer transcoder mathematical formulation jacobian"

Links: [{"title":"Circuit Tracing in Vision–Language Models: Understanding the Internal Mechanisms of Multimodal Thinking","url":"https://arxiv.org/html/2602.20330v1"},{"title":"Transcoders Find Interpretable LLM Feature Circuits Jacob Dunefsky∗","url":"https://arxiv.org/pdf/2406.11944"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf"},{"title":"Transformer Circuits Thread","url":"https://transformer-circuits.pub/"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://transformer-circuits.pub/2021/framework/index.html"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://arxiv.org/html/2511.13653v1"}]

Based on the search results, here's what I found about these interconnected concepts in transformer interpretability:

## Virtual Weights

Virtual weights are implicit connections directly linking any pair of transformer layers (even those separated by many other layers) by multiplying out their interactions through the residual stream. This concept leverages the linear, additive structure of the residual stream in transformers.

## Attribution Graphs

Attribution graphs linearly decompose how features contribute to activations in upper layers and, ultimately, to the output logits on a fixed prompt. Because each transcoder replaces the MLP with a sparse linear readout from features, and all nonlinearities are frozen at their values on the given prompt, the model becomes locally linear around that input.

## Cross-Layer Transcoders

Cross-layer transcoders work alongside attribution graphs, with quantitative evaluations showing metrics by which CLTs provide Pareto-improvements over neurons and per-layer transcoders. Recent work yields circuits on production models across a variety of behaviors by using linear attribution graphs between cross-layer transcoder features.

## Mathematical Formulation with Jacobians

The backward Jacobian tells how much a feature in the previous layer contributed to the current feature activation, and is applied recursively until reaching the input. The residual-stream Jacobian of the original transformer uses stop-gradients on all nonlinearities (LayerNorm, attention softmax, and ReLU).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ffe4734-7750-4a14-ad90-8cb0f467c8b5",
  "isSidechain": true,
  "promptId": "eee12e6f-4b22-4cb0-adff-def0ae050a12",
  "agentId": "a8229769393fca3c5",
  "type": "user",
  "uuid": "58a3e207-7c14-4cd5-891c-2e2a46988210",
  "sourceToolAssistantUUID": "6ffe4734-7750-4a14-ad90-8cb0f467c8b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T06:23:47.984Z_

I now have comprehensive information. Here is the full detailed research report.

---

## Circuit Tracing: Revealing Computational Graphs in Language Models -- Detailed Research Report

### 1. The Problem Gap They Identified and How They Identified It

The Anthropic team identified a fundamental obstacle in mechanistic interpretability: **polysemanticity and superposition**. Individual neurons in language models represent multiple unrelated concepts simultaneously, and models encode more concepts than they have neurons. This means the natural computational units (neurons) do not correspond to meaningful semantic units.

Prior circuit discovery work (dating back to Anthropic's own "A Mathematical Framework for Transformer Circuits" from 2021 and community efforts on small models) had attempted to trace circuits through raw neurons, but this repeatedly failed to yield clean, interpretable results in larger models. The circuits were either intractably large or failed to disentangle local behavior from global behavior.

The gap was identified through a progression of work:
- **Sparse autoencoders (SAEs)** from "Towards Monosemanticity" (2023) and "Scaling Monosemanticity" (2024) showed that meaningful features *could* be extracted from activations, but SAEs only reveal *what* features are important, not *why* -- they decompose activations at a single point and cannot model the computation (input-to-output transformation) of MLP layers.
- **Per-layer transcoders** (Dunefsky et al., NeurIPS 2024) improved on this by modeling MLP computation directly, but each transcoder operated on a single layer, meaning circuits had to chain through many layers, creating long attribution paths with redundant features appearing at multiple layers.

The critical gap: there was no method that could simultaneously (a) decompose model computation into interpretable features, (b) handle multi-layer effects where the same conceptual computation spans several layers, and (c) produce tractable circuit graphs at the scale of production models.

---

### 2. The Key Insight Others Missed: Cross-Layer Transcoders vs. Standard SAEs

The central innovation is the **cross-layer transcoder (CLT)** architecture, which exploits an observation that others had not leveraged: in transformers, the residual stream makes information computed at any layer available to all subsequent layers. This means a single conceptual feature often manifests across multiple MLP layers -- not because it is recomputed, but because the same information in the residual stream is read out by multiple downstream MLPs.

**What others missed:**

1. **SAEs operate on the wrong target.** SAEs decompose MLP *activations* (post-computation), not the MLP *computation itself*. They answer "what features are present?" but not "what transformation was performed?" This makes them fundamentally unsuitable for circuit tracing.

2. **Per-layer transcoders create artificial circuit length.** When you have one transcoder per layer, a feature that conceptually represents "this word is a country name" might appear as separate features at layers 5, 8, and 12 -- creating long chains in attribution graphs that are really just the same information being read from the residual stream. Per-layer transcoders cannot collapse these redundant paths.

3. **Cross-layer structure is natural, not forced.** CLTs allow a single feature to read from the residual stream at one layer and contribute decoder vectors to the MLP outputs at all subsequent layers. This "cross-layer" structure naturally collapses amplification chains (where layer N reads from the residual stream what layer N-3 wrote) into direct feature-to-feature connections. This dramatically simplifies attribution graphs without losing information.

The architectural difference:

| Aspect | SAE | Per-Layer Transcoder | CLT |
|--------|-----|---------------------|-----|
| Input | MLP output at layer L | Residual stream at layer L | Residual stream at layer L |
| Output | Reconstruction of MLP output at layer L | MLP output at layer L | MLP outputs at layers L, L+1, ..., L_max |
| What it models | Activation structure | Single-layer MLP computation | Multi-layer MLP computation |
| Circuit path length | N/A (not for circuits) | Long (one hop per layer) | Short (direct cross-layer connections) |

---

### 3. How They Formulated the Problem Differently

Prior circuit discovery work (e.g., Conmy et al.'s ACDC, Wang et al.'s IOI circuit) framed the problem as: *"Given a model behavior, identify which components (attention heads, MLP layers, neurons) are causally responsible."* This top-down, ablation-based approach requires knowing what behavior you are looking for and struggles to scale.

The Anthropic team reformulated the problem as: *"Replace the model's MLP computation with an interpretable sparse approximation, then read off circuits directly from the resulting linear structure."*

This is a fundamentally different formulation:
- **Not ablation-based but replacement-based.** Instead of removing components and measuring damage, they *substitute* components with interpretable equivalents and trace the resulting computational graph.
- **Local linearization.** On any specific prompt, once you freeze attention patterns and LayerNorm denominators, the model with CLT replacements becomes a **fully linear network** from token embeddings to output logits, with CLT features as intermediate nodes. Circuits are then just paths through this linear network.
- **Bottom-up, not top-down.** You don't need to specify the behavior first. The attribution graph for any prompt reveals *all* the computational structure, and you can then identify which parts are interesting.

The "local replacement model" concept is key: for a specific prompt p, they:
1. Run the original model to get attention patterns and LayerNorm statistics
2. Freeze these non-MLP components
3. Replace each MLP layer with its CLT approximation
4. Add error correction terms (difference between true MLP output and CLT reconstruction)
5. The result is a model that produces *exactly the same output* as the original on prompt p, but whose MLP computation is now a sparse linear network

---

### 4. Existing Techniques Adapted and Combined

The work synthesizes several threads:

1. **Sparse Autoencoders** (Bricken et al., 2023; Templeton et al., 2024): The idea of using sparse dictionaries to find interpretable features. CLTs inherit the JumpReLU activation function from this line.

2. **Transcoders** (Dunefsky, Chlenski & Nanda, 2024): The idea of modeling MLP input-to-output transformation rather than just activating structure. CLTs extend this from per-layer to cross-layer.

3. **Crosscoders** (concept referenced in the paper): Multi-layer feature sharing, which CLTs generalize.

4. **Virtual Weights** (Elhage et al., 2021 "Mathematical Framework"): The decomposition of paths through the residual stream into direct "virtual" weight matrices between any two features. This framework is what makes the linear attribution tractable.

5. **Stop-gradient Jacobians**: The attribution method uses Jacobians with stop-gradients on all nonlinearities (LayerNorm scale factors, attention softmax, ReLU/JumpReLU activations). This makes attribution locally linear and additive -- the preactivation of any feature is exactly the sum of its incoming edges.

6. **Graph pruning via influence matrices**: They compute B = (I - A)^(-1) - I, the indirect influence matrix, using the Neumann series expansion B = A + A^2 + A^3 + ..., to identify which nodes contribute the most to target outputs. This achieves ~10x node reduction.

7. **Perturbation-based validation**: Constrained patching (modifying a feature in a limited layer range) and iterative patching (allowing second-order cascade effects) to empirically validate graph predictions.

---

### 5. Technical Method Details

**Cross-Layer Transcoder Architecture:**

A CLT has L encoder layers and L^2 decoder pathways:
- Encoder at layer l: `a^l = JumpReLU(W_enc^l * x^l)` where x^l is the residual stream
- Decoder from layer l' to layer l: `y_hat^l = sum_{l'=1}^{l} W_dec^{l'->l} * a^{l'}`
- Each feature i activated at layer l' has decoder vectors for every downstream layer l >= l'

Training objective:
```
L_total = L_MSE + lambda * L_sparsity
L_MSE = sum_l ||y_hat^l - y^l||^2   (y^l = true MLP output at layer l)
L_sparsity = lambda * sum_l sum_i tanh(c * ||W_dec,i^l|| * a_i^l)
```

The tanh-based sparsity penalty (rather than L1) encourages features to either be fully off or meaningfully active, avoiding the "shrinkage" problem of L1.

**Attribution Graph Construction:**

Edge weight from source feature s (layer l_s, position c_s) to target feature t (layer l_t, position c_t):
```
A_{s->t} = a_s * w_{s->t}
w_{s->t} = sum_{l_s <= l < l_t} (W_dec,s^{l_s->l})^T * J^{c_s,l_s -> c_t,l_t} * W_enc,t^{l_t}
```
where J is the residual-stream Jacobian with stop-gradients on all nonlinearities.

The virtual weight w_{s->t} captures the total effect of source s on target t through all intermediate residual stream paths, including attention-mediated pathways (OV circuits only, not QK).

**Graph Nodes:**
- Input nodes: token embeddings
- Intermediate nodes: active CLT features at each (position, layer)
- Output nodes: candidate tokens (top tokens covering 95% probability mass)
- Error nodes: residual reconstruction error per layer

**Pruning:**
Normalize adjacency matrix so input edges sum to 1. Compute indirect influence B = (I-A)^(-1) - I. Threshold on B to retain only nodes/edges contributing above a cutoff to the target output.

**Scale:**
- 18-layer transformer: CLTs with 300K to 10M features; largest has 88 average active features per token
- Claude 3.5 Haiku: CLTs with up to 30M features; largest has 235 average active features per token
- Training data: Common Corpus, The Pile, LMSYS Chat 1M

**Validation Metrics:**
- Completeness: fraction of target node inputs from features vs. error nodes
- Replacement: fraction of full paths from embeddings to logits via features
- Node-to-logit cosine similarity: ~0.8 for one-layer effects
- Feature-pair Spearman correlation: 0.72 between predicted influence and actual activation change
- Sort Eval and Contrastive Eval: LLM-based interpretability scoring (can Claude distinguish which feature activated on novel examples?)

---

### 6. Limitations and Open Questions

**Fundamental Limitations:**

1. **Attention circuits are invisible.** The method freezes attention patterns and only traces through OV (output-value) circuits. QK (query-key) circuits -- which determine *where* the model attends -- are completely opaque. This means any behavior driven by attention pattern changes (induction heads, certain forms of in-context learning, copying) cannot be explained. A companion paper on QK-circuit tracing partially addresses this.

2. **Reconstruction error ("dark matter").** The largest 18L CLT has 11.5% normalized reconstruction error; Haiku has 21.7%. Whatever computation lives in these residuals is invisible to the method. When critical computation falls in the error, attribution graphs reveal nothing useful.

3. **CLTs may learn unfaithful circuits.** This is the most serious critique, detailed in a LessWrong post. Because additional decoder vectors to downstream layers are nearly "free" in terms of sparsity cost, CLTs are incentivized to collapse multi-step computations into single-hop shortcuts. Evidence: (a) In a toy model computing (a XOR b) AND (c XOR d), CLTs learn a lookup table skipping the intermediate XOR step entirely; (b) On GPT-2 Small, layer-0 CLT features activate 3x more than later layers, unlike per-layer transcoders which show uniform activation; (c) CLTs and per-layer transcoders produce contradictory mechanistic stories for the same behavior.

4. **Inactive features and inhibition.** The method only tracks active features. Equally important inhibitory mechanisms -- features that *should* fire but don't -- are invisible. This is critical for understanding safety-relevant behaviors like refusal.

5. **Local vs. global understanding.** Attribution graphs work well for single prompts but struggle to generalize. Global virtual weights suffer from "interference" -- features that never co-activate can have large virtual weights that are meaningless. TWERA (target-weighted expected residual attribution) partially mitigates this.

6. **Scale of graphs.** Even after pruning, graphs have hundreds of nodes and tens of thousands of edges, making interpretation cognitively demanding.

7. **Success rate.** The companion "Biology" paper candidly notes: "Attribution graphs provide satisfying insight for about a quarter of the prompts we've tried."

**Open Questions:**
- What computation hides in reconstruction error?
- Can CLT unfaithfulness be eliminated without losing cross-layer benefits?
- How to extend to QK circuits fully?
- How to automate interpretation (ADAG is an early attempt)?
- Can this scale to longer contexts (current work limited to short prompts)?
- How to identify inhibitory/absent circuits?

---

### 7. Building Blocks (Reusable Methods/Tools/Datasets)

**Reusable Methodological Components:**
1. **JumpReLU activation with trainable thresholds** -- applicable to any sparse coding method
2. **Stop-gradient Jacobian attribution** -- model-agnostic; can trace through any frozen-nonlinearity network
3. **Virtual weight computation** -- applicable wherever residual streams create skip connections
4. **Influence matrix pruning** (Neumann series) -- general graph sparsification technique
5. **Local replacement model** concept -- substituting components with interpretable equivalents while maintaining exact output
6. **TWERA** -- correcting global weights using co-activation statistics
7. **Sort Eval / Contrastive Eval** -- LLM-based interpretability metrics for any feature dictionary

**Available Tools and Implementations:**
- **Circuit Tracer** library (Anthropic Fellows): open-source, supports Gemma-2-2B, Llama-3.1-1B, Qwen3-4B
- **Attribute** (EleutherAI): independent attribution graph library
- **CLT-Forge**: scalable distributed CLT training library with model sharding
- **Neuronpedia**: interactive web interface for exploring attribution graphs (7,000+ graphs generated)
- **Pre-trained CLTs**: available on Hugging Face for multiple models
- **ADAG**: automated attribution graph description using LLM explainer-simulator

**Datasets:**
- Common Corpus, The Pile (books removed), LMSYS Chat 1M for training
- 10,000 two-digit addition problems for arithmetic circuit analysis

---

### 8. How They Innovate (Summary of the Innovation Pattern)

The core innovation pattern is **architectural reformulation enabling analytical tractability**:

1. They observed that the residual stream makes transformers "locally linear" when nonlinearities are frozen -- an insight from the 2021 Mathematical Framework paper that had not been fully exploited for circuit discovery at scale.

2. They noticed that per-layer feature decompositions create artificial complexity by splitting naturally cross-layer computations into per-layer fragments.

3. They designed CLTs specifically to exploit the residual stream's information-sharing property, collapsing multi-layer amplification chains into direct feature connections.

4. They combined this with the replacement model trick: exact output preservation via error correction, meaning the interpretable approximation doesn't sacrifice accuracy on any individual prompt.

5. The result is a system where circuits are not *discovered* through expensive search or ablation, but *read off directly* from the linear structure of the replacement model.

This is a shift from "circuit discovery as search" to "circuit discovery as architecture" -- you build the microscope into the model itself, rather than probing the model from outside.

---

Sources:
- [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)
- [Tracing Attention Computation Through Feature Interactions](https://transformer-circuits.pub/2025/attention-qk/index.html)
- [Cross-Layer Transcoders Are Incentivized to Learn Unfaithful Circuits (LessWrong)](https://www.lesswrong.com/posts/6CS2NDmoLCFcEJMor/cross-layer-transcoders-are-incentivized-to-learn-unfaithful)
- [Circuit Tracing: A Step Closer to Understanding LLMs (Towards Data Science)](https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/)
- [Replicating Circuit Tracing for a Simple Known Mechanism (Goodfire)](https://www.goodfire.ai/research/replicating-circuit-tracing-for-a-simple-mechanism)
- [Anthropic Open-Sources Tool to Trace "Thoughts" of LLMs (InfoQ)](https://www.infoq.com/news/2025/06/anthropic-circuit-tracing/)
- [The Circuits Research Landscape (Neuronpedia)](https://www.neuronpedia.org/graph/info)
- [Transcoders Find Interpretable LLM Feature Circuits (Dunefsky et al., NeurIPS 2024)](https://arxiv.org/abs/2406.11944)
- [Cross-Layer Transcoders and Sparse Autoencoders (Jon Vet)](https://www.jonvet.com/blog/llm-transcoder-and-saes)
- [CLT-Forge: A Scalable Library for Cross-Layer Transcoders](https://arxiv.org/abs/2603.21014)
- [ADAG: Automatically Describing Attribution Graphs](https://arxiv.org/abs/2604.07615)
- [Cross Layer Transcoders for Qwen3 (BluelightAI)](https://bluelightai.com/blog/clts-for-qwen3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58a3e207-7c14-4cd5-891c-2e2a46988210",
  "isSidechain": true,
  "agentId": "a8229769393fca3c5",
  "requestId": "req_011CbYGhSHjn6Fn5S7wqqprq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3278686d-8a43-46c0-aee9-b83b32292db1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "94d88260-dbbe-43d4-abc2-f8f5a7fda9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UU5eGCYPjTE5Yi3pwNnxyW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1229,
      "cache_read_input_tokens": 23013,
      "output_tokens": 4487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1229
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4487,
          "cache_read_input_tokens": 23013,
          "cache_creation_input_tokens": 1229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1229,
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
