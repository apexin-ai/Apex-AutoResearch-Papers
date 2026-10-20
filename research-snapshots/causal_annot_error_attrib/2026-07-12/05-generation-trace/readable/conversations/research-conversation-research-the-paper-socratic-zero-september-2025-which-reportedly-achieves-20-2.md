# Research conversation: Research the paper "Socratic-Zero" (September 2025) which reportedly achieves +20.2pp improvement and implements Teacher

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a67b76442fb946591.jsonl`
- **Structured JSON:** [`1c614c70ae7bf60830b9.json`](../../sessions/1c/1c614c70ae7bf60830b9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-28T05:28:43.936Z_

Research the paper "Socratic-Zero" (September 2025) which reportedly achieves +20.2pp improvement and implements Teacher-Solver-Generator co-evolution where the Teacher adaptively targets solver weaknesses. 

Search for it using multiple queries:
1. "Socratic-Zero" reasoning LLM
2. "Teacher-Solver-Generator" co-evolution
3. Socratic-Zero arxiv 2025

For each result, try to fetch the actual paper or abstract using WebFetch. I need:
- Full title and authors
- Arxiv ID
- Exact results/numbers claimed
- How the Teacher targets weaknesses (is it error-type-level? concept-level? scalar difficulty?)
- The co-evolution mechanism
- Key limitations compared to a PRM-based error taxonomy approach
- Whether it uses a PRM or verifier

Be thorough - read the actual paper if possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "e5dc1790-3889-4fad-9c3a-5135304a3d01",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T05:28:43.940Z_

```json
{
  "parentUuid": "e5dc1790-3889-4fad-9c3a-5135304a3d01",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "cdb5c690-9c57-46d5-9739-9b0ac77b8b40",
  "timestamp": "2026-05-28T05:28:43.940Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T05:28:43.942Z_

```json
{
  "parentUuid": "cdb5c690-9c57-46d5-9739-9b0ac77b8b40",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "29419420-ce44-4ce4-a438-fc5a0a5f4e27",
  "timestamp": "2026-05-28T05:28:43.942Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T05:28:46.636Z_



I'll research this paper thoroughly. Let me start by loading the necessary tools and then searching for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29419420-ce44-4ce4-a438-fc5a0a5f4e27",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR2hG6RKUAKUqQVMhWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72e521ce-1037-49a7-8e7f-603e8f134c08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERaxKn99sqMXKgWMLkdofU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8929,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-28T05:28:47.116Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BKNoQ18HiABwehyBXQjYNv`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72e521ce-1037-49a7-8e7f-603e8f134c08",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR2hG6RKUAKUqQVMhWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50010214-c534-4893-9702-b7b8c321ee37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERaxKn99sqMXKgWMLkdofU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 0,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8929
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8929,
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

_source line 6 · 2026-05-28T05:28:47.120Z_

<details><summary>↩ Tool result · `toolu_01BKNoQ18HiABwehyBXQjYNv`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50010214-c534-4893-9702-b7b8c321ee37",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "6e04c395-0ad9-4857-a8a1-bf2df8ad897f",
  "sourceToolAssistantUUID": "50010214-c534-4893-9702-b7b8c321ee37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T05:28:49.780Z_



Now let me run all three search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e04c395-0ad9-4857-a8a1-bf2df8ad897f",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR2w7Y3ZUYDYdZ7JyJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4520e540-3f4f-4af6-87b8-66e3731d2643",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wi2WtLfGffnRuVPrMRtjes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 8 · 2026-05-28T05:28:50.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PcAWDDLFFtgmbrk7tp73K`</summary>

```json
{
  "query": "\"Socratic-Zero\" reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4520e540-3f4f-4af6-87b8-66e3731d2643",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR2w7Y3ZUYDYdZ7JyJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58925e4e-5304-4faf-b808-3a4c35d16364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wi2WtLfGffnRuVPrMRtjes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 9 · 2026-05-28T05:28:50.800Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TtzwgKCEJmCot9P9aKtZX8`</summary>

```json
{
  "query": "\"Teacher-Solver-Generator\" co-evolution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58925e4e-5304-4faf-b808-3a4c35d16364",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR2w7Y3ZUYDYdZ7JyJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50f466b6-5ea0-4923-be52-53a09338a729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wi2WtLfGffnRuVPrMRtjes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 10 · 2026-05-28T05:28:50.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MEFzzPh7B8PG82FSrzNxDh`</summary>

```json
{
  "query": "Socratic-Zero arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50f466b6-5ea0-4923-be52-53a09338a729",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR2w7Y3ZUYDYdZ7JyJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f465d0b6-c281-4d63-9eb7-38fc484a34e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wi2WtLfGffnRuVPrMRtjes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 11 · 2026-05-28T05:28:58.011Z_

<details><summary>↩ Tool result · `toolu_01MEFzzPh7B8PG82FSrzNxDh`</summary>

```text
Web search results for query: "Socratic-Zero arxiv 2025"

Links: [{"title":"Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution [Quick Review]","url":"https://liner.com/review/socraticzero-bootstrapping-reasoning-via-datafree-agent-coevolution"},{"title":"[Literature Review] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://www.themoonlight.io/en/review/socratic-zero-bootstrapping-reasoning-via-data-free-agent-co-evolution"},{"title":"[2509.24726] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/abs/2509.24726"},{"title":"[PDF] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Socratic-Zero-:-Bootstrapping-Reasoning-via-Agent-Wang-Jiao/08d60a8f1169eb65c120b67a1b6b8a8c448f9913"},{"title":"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/html/2509.24726"},{"title":"Paper page - Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://huggingface.co/papers/2509.24726"},{"title":"Preprint. Under Review. SOCRATIC-ZERO: BOOTSTRAPPING REASONING VIA","url":"https://arxiv.org/pdf/2509.24726"},{"title":"Socratic-Geo: Synthetic Data Generation and Geometric ...","url":"https://www.arxiv.org/pdf/2602.03414"}]

Based on the search results, here's what I found about Socratic-Zero:

## Overview

Socratic-Zero is a fully autonomous framework that generates high-quality training data from minimal seed examples through the co-evolution of three agents: the Teacher, the Solver, and the Generator.

## Problem It Addresses

Recent breakthroughs in large language models (LLMs) on reasoning tasks rely heavily on massive, high-quality datasets typically human-annotated and difficult to scale. Existing data synthesis or distillation methods struggle with inconsistent data quality and an inability to dynamically adapt to the evolving capabilities of the model, leading to suboptimal training signals.

## Key Innovation

Socratic-Zero is a fully autonomous, co-evolutionary framework designed to bootstrap mathematical reasoning from a minimal set of seed problems, entirely without relying on external human-annotated data. The architecture translates the philosophical dialogue of the Socratic method into a concrete, co-evolutionary computational framework. Unlike conventional pipelines that decouple data generation from model training, Socratic-Zero unifies them within a continuous co-evolutionary loop.

## Performance

Socratic achieves 56.1% average accuracy, outperforming Static Augmentation by +15.4 points and LLM2LLM by +15.2 points.

The paper was submitted on September 29, 2025, with arxiv ID 2509.24726.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f465d0b6-c281-4d63-9eb7-38fc484a34e3",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "c353bada-4820-4262-b9f7-6f2a5e88afa6",
  "sourceToolAssistantUUID": "f465d0b6-c281-4d63-9eb7-38fc484a34e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T05:28:58.949Z_

<details><summary>↩ Tool result · `toolu_013PcAWDDLFFtgmbrk7tp73K`</summary>

```text
Web search results for query: ""Socratic-Zero" reasoning LLM"

Links: [{"title":"[Literature Review] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://www.themoonlight.io/en/review/socratic-zero-bootstrapping-reasoning-via-data-free-agent-co-evolution"},{"title":"[2509.24726] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/abs/2509.24726"},{"title":"Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/pdf/2509.24726"},{"title":"Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution | OpenReview","url":"https://openreview.net/forum?id=I1garriWB7"},{"title":"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/html/2509.24726"},{"title":"(PDF) Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://www.researchgate.net/publication/395968931_Socratic-Zero_Bootstrapping_Reasoning_via_Data-Free_Agent_Co-evolution"},{"title":"Paper page - Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://huggingface.co/papers/2509.24726"},{"title":"(PDF) The Art of SOCRATIC QUESTIONING: Zero-shot Multimodal Reasoning with Recursive Thinking and Self-Questioning","url":"https://www.researchgate.net/publication/371009345_The_Art_of_SOCRATIC_QUESTIONING_Zero-shot_Multimodal_Reasoning_with_Recursive_Thinking_and_Self-Questioning"}]

Here are the search results for "Socratic-Zero" reasoning LLM:

## Overview

Socratic-Zero is a fully autonomous, data-free framework designed to bootstrap mathematical reasoning capabilities in large language models (LLMs) from a minimal set of seed examples. It employs a multi-agent co-evolutionary system comprising a Solver, a Teacher, and a Generator.

## How It Works

The closed-loop system continuously refines a curriculum and the agents' capabilities without relying on external human-annotated data. The Solver improves by generating solutions and refining them through the Teacher's feedback, while the Generator evolves by strategically distilling the Teacher's behavior to produce an increasingly suitable curriculum for the Solver.

## Performance Results

The framework shows impressive empirical results:

- Starting with only 100 seed questions, Socratic-Zero demonstrates superior empirical performance across seven mathematical reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva, GSM8K).

- Socratic-Solver-8B achieved an average gain of +20.2 percentage points over prior data synthesis methods, reaching 56.1% average accuracy, with significant gains on competitive problems like AIME-24 (+19.1) and AIME-25 (+16.5).

- Synthetic data from Socratic-Generator-32B enables student LLMs to achieve superior performance compared to other state-of-the-art commercial LLMs on these benchmarks, including Qwen3-235B-A22B, DeepSeek-V3.1-671B, GPT-5, Gemini-2.5-Pro, Grok-4, and Claude-4.1-Opus.

The paper was published on arXiv in September 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58925e4e-5304-4faf-b808-3a4c35d16364",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "b6c4a320-49ee-4dac-9645-49fc5e073f91",
  "sourceToolAssistantUUID": "58925e4e-5304-4faf-b808-3a4c35d16364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T05:28:59.367Z_

<details><summary>↩ Tool result · `toolu_01TtzwgKCEJmCot9P9aKtZX8`</summary>

```text
Web search results for query: ""Teacher-Solver-Generator" co-evolution"

Links: [{"title":"Preprint. Under Review. SOCRATIC-ZERO: BOOTSTRAPPING REASONING VIA","url":"https://arxiv.org/pdf/2509.24726"},{"title":"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/html/2509.24726"},{"title":"Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery","url":"https://arxiv.org/pdf/2601.22896"},{"title":"Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution","url":"https://arxiv.org/pdf/2604.03472"},{"title":"EALG: Evolutionary Adversarial Generation of Language Model-Guided Generators for Combinatorial Optimization","url":"https://arxiv.org/pdf/2506.02594"},{"title":"TTCS: Test-Time Curriculum Synthesis for Self-Evolving","url":"https://arxiv.org/pdf/2601.22628"},{"title":"Sci-CoE: Co-evolving Scientific Reasoning LLMs via Geometric Consensus with Sparse Supervision","url":"https://arxiv.org/pdf/2602.12164"}]

Based on the search results, here's what I found about "Teacher-Solver-Generator" co-evolution:

The Teacher-Solver-Generator framework is a fully autonomous system that generates high-quality training data from minimal seed examples through the co-evolution of three agents: the Teacher, the Solver, and the Generator.

## How It Works

A powerful LLM acts as the Teacher, guiding the co-evolution of two agents. The Solver improves by generating solutions and refining them through the Teacher's feedback, while the Generator evolves by strategically distilling the Teacher's behavior to produce an increasingly suitable curriculum for the Solver.

More specifically, the Solver continuously refines its reasoning by learning from preference feedback on both successful and failed trajectories; the Teacher adaptively crafts increasingly challenging questions based on the Solver's weaknesses; and the Generator distills the Teacher's question-design strategy to enable scalable, high-fidelity curriculum.

## Application: Socratic-Zero

This framework was implemented in a system called Socratic-Zero. Starting from only 100 seed questions, Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods across seven mathematical reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva, and GSM8K).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50f466b6-5ea0-4923-be52-53a09338a729",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "c293dafe-f97a-4f73-bbc4-cf5ad3ea90da",
  "sourceToolAssistantUUID": "50f466b6-5ea0-4923-be52-53a09338a729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T05:29:02.580Z_

The paper exists and is on arxiv at ID 2509.24726. Now let me fetch the actual paper content to get detailed information. I'll fetch the abstract page, the HTML version, and look for the OpenReview page in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c293dafe-f97a-4f73-bbc4-cf5ad3ea90da",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR3qBcwSTs3YwA7YLCK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99a83294-2171-4769-bc2f-f7127853fbdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJgSGn2cjT48wqHmW3CEZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 1762,
      "cache_read_input_tokens": 10054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1762,
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

_source line 15 · 2026-05-28T05:29:04.024Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01576zJdeLBn6fi6xAcnFP6D`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.24726",
  "prompt": "Extract the complete paper information: full title, all authors with affiliations, arxiv ID, submission date, abstract in full. List everything precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99a83294-2171-4769-bc2f-f7127853fbdd",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR3qBcwSTs3YwA7YLCK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f0a3d80-69a6-45ec-aa2e-405f80af728d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJgSGn2cjT48wqHmW3CEZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 1762,
      "cache_read_input_tokens": 10054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1762,
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

_source line 16 · 2026-05-28T05:29:07.347Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TWMdXAR7Wp7osxhsvzqY2F`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.24726",
  "prompt": "Extract the full paper content. I need: 1) The complete methodology section - how does the Teacher target solver weaknesses? Is it error-type-level, concept-level, or scalar difficulty? 2) The co-evolution mechanism in detail - how do Solver, Teacher, and Generator interact? 3) All experimental results with exact numbers. 4) Does it use a PRM (Process Reward Model) or verifier? 5) All limitations discussed. 6) The exact +20.2pp claim and what it's compared against. Be thorough and extract as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f0a3d80-69a6-45ec-aa2e-405f80af728d",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR3qBcwSTs3YwA7YLCK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67aaccb8-0ab4-4fca-b0dc-d2fac020cba0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJgSGn2cjT48wqHmW3CEZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 1762,
      "cache_read_input_tokens": 10054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1762,
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

_source line 17 · 2026-05-28T05:29:08.720Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J3v6h3a5wC4pQ7n2K8rCG7`</summary>

```json
{
  "url": "https://openreview.net/forum?id=I1garriWB7",
  "prompt": "Extract all reviewer comments, scores, and criticisms of the paper. What limitations did reviewers identify? Any concerns about the Teacher mechanism or comparison to PRM-based approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67aaccb8-0ab4-4fca-b0dc-d2fac020cba0",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR3qBcwSTs3YwA7YLCK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf324b22-e457-4719-a0d8-7c3a1e3600de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJgSGn2cjT48wqHmW3CEZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 1762,
      "cache_read_input_tokens": 10054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1762,
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

### Tool result

_source line 18 · 2026-05-28T05:29:09.174Z_

<details><summary>↩ Tool result · `toolu_01576zJdeLBn6fi6xAcnFP6D`</summary>

```text
# Paper Information

**Full Title:** Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution

**Authors:**
1. Shaobo Wang
2. Zhengbo Jiao
3. Zifan Zhang
4. Yilang Peng
5. Xu Ze
6. Boyu Yang
7. Wei Wang
8. Hu Wei
9. Linfeng Zhang

*Note: Author affiliations are not provided in the webpage content.*

**arXiv ID:** 2509.24726

**Submission Date:** September 29, 2025

**Abstract:**

The paper presents a framework designed to generate training data autonomously through three collaborative agents. The approach addresses limitations in existing synthetic data methods by creating a self-improving system requiring "no pre-existing tasks or labels." Starting from merely 100 seed questions, their Socratic-Solver-8B model achieved "an average gain of +20.2 percentage points over prior data synthesis methods across seven mathematical reasoning benchmarks." The synthetic data from their larger generator model reportedly enables smaller student models to "achieve superior performance compared to other state-of-the-art (SOTA) commercial LLMs on these benchmarks," including significantly larger proprietary systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f0a3d80-69a6-45ec-aa2e-405f80af728d",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "a786508d-fb84-4708-924b-f3c79295ec43",
  "sourceToolAssistantUUID": "6f0a3d80-69a6-45ec-aa2e-405f80af728d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T05:29:11.934Z_

<details><summary>↩ Tool result · `toolu_01J3v6h3a5wC4pQ7n2K8rCG7`</summary>

```text
I cannot extract reviewer comments, scores, and criticisms from the provided web page content, as none of that information is present in the text supplied.

The page shows only the paper's title, authors, abstract, and basic metadata for "Socratic-Zero" on OpenReview. It does not include reviewer feedback, assessment scores, identified limitations, concerns about mechanisms, or comparisons to other approaches that reviewers may have raised.

To access such information, you would need to:
- Visit the full OpenReview page and check if reviews have been posted
- Look for a "Reviews" or "Comments" section on the actual submission page
- Check if the paper includes a response to reviewers or revision history

The abstract alone describes the work's claimed contributions but does not reflect independent critical evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf324b22-e457-4719-a0d8-7c3a1e3600de",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "a63a493d-b3d7-42f6-a9ec-a77ba151608b",
  "sourceToolAssistantUUID": "cf324b22-e457-4719-a0d8-7c3a1e3600de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T05:29:34.631Z_

<details><summary>↩ Tool result · `toolu_01TWMdXAR7Wp7osxhsvzqY2F`</summary>

```text
# Socratic-Zero: Comprehensive Analysis

## 1. METHODOLOGY SECTION

### Teacher's Weakness Targeting Approach

The Teacher employs **error-instance-level** targeting rather than abstract concept-level approaches. According to the paper:

The Teacher uses two functions:
- **Verification function** V(q,y)→{0,1}: judges solution correctness
- **Problem refinement function** G(q,y_fail)→(q',y'_ref): "creates a new problem-solution pair by revising an original problem based on a failed solution"

The targeting mechanism is explicitly described as: "the Teacher is prompted with a specific failed solution attempt, y_fail. The new problem (q',y'_ref)=G(q,y_fail) is designed to target the specific reasoning error exhibited in y_fail, thereby helping the Solver overcome its weaknesses."

This is **scalar difficulty-aware** through zone-adaptive generation: problems are categorized into Mastered, Learning, and Too Difficult zones based on success rates s_q = (1/k)∑V(q,y_S^(i)).

## 2. CO-EVOLUTION MECHANISM

The three-agent system operates in a closed loop:

**Phase 1 - Solver Evolution (Online Preference Learning):**
- Solver generates k=8 solution attempts per problem
- Teacher verifies each attempt
- Attempts partitioned into winning set 𝒴_w(q) and losing set 𝒴_l(q)
- Solver trained via Direct Preference Optimization (DPO) loss (Equation 5): "maximizes the likelihood of preferred solutions over rejected ones"

**Phase 2 - Generator Evolution (Offline Value-Weighted Distillation):**
- Generator learns to mimic Teacher's refinement strategy
- Training uses utility function U(q'|π_θ_S)=exp(-(s_q'-μ)²/2σ²) with μ=0.5, σ=0.2
- Generator trained via weighted supervised fine-tuning to maximize utility-weighted log-likelihood
- Generator transforms (q,y_fail) inputs to new problems q'

**Phase 3 - Curriculum Expansion:**
- Failed attempts collected: ℱ_t = {(q,y_S)|(q,y_ref)∈𝒟_t, V(q,y_S)=0}
- Teacher generates 𝒟_new from failures
- Curriculum updated: 𝒟_{t+1} = 𝒟_t ∪ 𝒟_new

## 3. EXPERIMENTAL RESULTS - EXACT NUMBERS

### Solver Performance (Table 1)
Qwen3-8B-base training results across seven benchmarks:

| Benchmark | Base+SFT | Static Aug | LLM2LLM S3 | Socratic S3 | Gain |
|-----------|----------|-----------|------------|------------|------|
| AMC | 39.1 | 45.8 | 44.9 | 63.7 | +17.9pp |
| Minerva | 37.8 | 41.9 | 42.1 | 52.4 | +10.5pp |
| MATH-500 | 56.9 | 62.7 | 66.8 | 81.2 | +18.5pp |
| GSM8K | 68.2 | 74.6 | 79.4 | 87.3 | +12.7pp |
| Olympiad | 31.7 | 35.9 | 34.6 | 55.1 | +19.2pp |
| AIME-25 | 8.1 | 11.4 | 7.9 | 24.6 | +13.2pp |
| AIME-24 | 9.3 | 12.3 | 10.4 | 28.4 | +16.1pp |
| **Average** | 35.9 | 40.7 | 40.9 | **56.1** | **+15.4pp** |

### Cross-Architecture Results (Table 2)
- **GLM4-9B**: 52.3% average (+9.5pp from SFT)
- **Qwen3-14B**: 60.3% average (+8.5pp from SFT)

### Generator Quality (Table 4)
- Socratic-Generator-32B validity rate: **95.6%**
- vs Qwen3-32B base: 89.1%
- vs Claude-4.1-Opus: 96.9%

### Downstream Effectiveness (Table 5)
DeepSeek-R1-Distill-Llama-8B trained on synthetic data:
- Socratic-Generator-32B: **37.72% average accuracy**
- Qwen3-235B-A22B: 37.13%
- Claude-4.1-Opus: 37.63%
- Gemini-2.5-Pro: 37.20%
- DeepSeek-v3.1: 36.62%
- GPT-5: 36.62%
- Grok-4: 37.01%

### General Reasoning Transfer (Table 3)
- BBEH: +1.86pp
- MMLU-Pro: +10.89pp
- SuperGPQA: +5.32pp
- **Average: +6.02pp**

## 4. VERIFIER ARCHITECTURE

The system uses a **dual-verification approach** rather than a Process Reward Model:

**Verification Method:**
- **MathRule**: "rule-based tool designed to extract and standardize final numerical answers" using pattern matching for answer indicators and mathematical expression parsing
- **LLM Judge**: Teacher model (Qwen3-235B-A22B) performs semantic validation with "temperature 0.1 sampling for consistent evaluations"

The dual approach achieves high agreement, and MathRule provides "objective, rule-based verification independent of LLM judgment."

## 5. LIMITATIONS DISCUSSED

### Explicit Limitations
1. **Lack of formal convergence analysis**: "While the complex agent dynamics currently lack a formal convergence analysis, future work will aim to establish this theoretical foundation"

2. **Domain restriction**: Framework currently restricted to mathematical reasoning; "domain transfer would require careful adaptation of the Teacher's evaluation capabilities and problem generation templates"

3. **Computational requirements**: Requires 8×NVIDIA H20 GPUs (768GB total memory) for Solver training plus 16×AMD MI308X GPUs for Teacher inference

4. **Teacher dependency**: System relies on a fixed, powerful Teacher model (Qwen3-235B-A22B); scalability to resource-constrained settings unclear

5. **Seed data requirement**: Despite "data-free" framing, requires 100 carefully curated seed problems with "difficulty alignment" between 10-70% success rate

6. **Initial SFT necessity**: Ablation study (Table 6a) shows system requires "initial supervised fine-tuning" - without it, only +2.34pp improvement versus +18.38pp with SFT

### Implicit Limitations
- Generator trained on mathematical problems; generalization to other domains "requires careful adaptation"
- Problem quality control relies on Teacher self-verification, which could propagate systematic errors
- MathRule answer extraction has limitations on problems requiring open-ended or complex responses

## 6. THE +20.2 PERCENTAGE POINT CLAIM

### Claim Specification
The abstract states: "Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods"

### Source of Comparison
From the methodology: comparing against "Static Augmentation" baseline (traditional MetaMath/WizardMath approaches) and "LLM2LLM" (iterative self-training without adaptive curriculum).

### Exact Baseline Comparison
- Static Augmentation average: 40.7%
- Socratic Stage 3 average: 56.1%
- **Difference: 15.4pp** (not 20.2pp as claimed in abstract)

### Reconciliation
The 20.2pp figure likely references **aggregate improvements across all individual benchmark comparisons** rather than average accuracy difference. Examining benchmark-by-benchmark gains (Table 1): the maximum single-benchmark improvement is +19.2pp (Olympiad), suggesting the 20.2pp may represent a weighted or selective reporting of results.

The paper's most conservative and defensible claim is the **+15.4 percentage point** improvement on the seven-benchmark average over Static Augmentation.

## KEY ARCHITECTURAL INSIGHTS

- **Reward function design**: Gaussian U(q'|π_θ_S)=exp(-(s_q'-μ)²/2σ²) with μ=0.5 empirically optimal (Table 6b shows alternative functions underperform by 0.20-0.40pp)
- **Curriculum zones**: Three-zone categorization (Mastered/Learning/Too Difficult) prevents pathological difficulty scaling
- **Generator stability**: Maintains 50%±1.3% target success rate across training stages despite evolving Solver
- **Preference pairs guarantee**: System ensures valid (y_w, y_l) pairs always exist by using reference solution when Solver produces no correct attempts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67aaccb8-0ab4-4fca-b0dc-d2fac020cba0",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "98295adb-4034-4d14-ac9b-e4d318ad6c38",
  "sourceToolAssistantUUID": "67aaccb8-0ab4-4fca-b0dc-d2fac020cba0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-28T05:29:39.469Z_

Excellent, I got very detailed information from the HTML version. Let me now try to get the OpenReview reviews and also fetch the Semantic Scholar page for additional details like author affiliations and citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98295adb-4034-4d14-ac9b-e4d318ad6c38",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR6S4QgNW6R3mAPbUfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "039ee0e7-ec94-42a5-9bf1-a277cf8082bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pXyaVBeH3x19RfSrVE5it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 199,
      "cache_creation_input_tokens": 3855,
      "cache_read_input_tokens": 11816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3855,
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

_source line 22 · 2026-05-28T05:29:41.366Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X1o3mFLsVgV67xXDsi3dbS`</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/Socratic-Zero-:-Bootstrapping-Reasoning-via-Agent-Wang-Jiao/08d60a8f1169eb65c120b67a1b6b8a8c448f9913",
  "prompt": "Extract all available information: author affiliations, citation count, full abstract, venue, and any related papers or references mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "039ee0e7-ec94-42a5-9bf1-a277cf8082bc",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR6S4QgNW6R3mAPbUfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "545a19a0-2983-45b2-865b-f7d27b91c0be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pXyaVBeH3x19RfSrVE5it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 199,
      "cache_creation_input_tokens": 3855,
      "cache_read_input_tokens": 11816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3855,
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

_source line 23 · 2026-05-28T05:29:41.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BC3ByBmyx7rnWdR5ZemvDc`</summary>

```json
{
  "query": "Socratic-Zero paper limitations PRM process reward model comparison review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "545a19a0-2983-45b2-865b-f7d27b91c0be",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR6S4QgNW6R3mAPbUfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbb8a5ef-2459-476e-92bd-128fa60c8c2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pXyaVBeH3x19RfSrVE5it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 199,
      "cache_creation_input_tokens": 3855,
      "cache_read_input_tokens": 11816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3855,
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

_source line 24 · 2026-05-28T05:29:43.443Z_

<details><summary>↩ Tool result · `toolu_01X1o3mFLsVgV67xXDsi3dbS`</summary>

```text
I'd be happy to help extract information from a web page, but I notice the content section appears to be empty in your message. 

Could you please provide the actual web page content you'd like me to analyze? Once you share it, I'll extract:

- Author affiliations
- Citation count
- Full abstract
- Venue
- Related papers or references

I'll follow all your guidelines, including the 125-character limit for quotes and proper attribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "545a19a0-2983-45b2-865b-f7d27b91c0be",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "5ce64fbe-c199-4714-8c24-e8d752423677",
  "sourceToolAssistantUUID": "545a19a0-2983-45b2-865b-f7d27b91c0be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T05:29:43.926Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NnHCf23nuapj54AGnhU4as`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/socratic-zero-bootstrapping-reasoning-via-data-free-agent-co-evolution",
  "prompt": "Extract the full literature review content. I need: all criticisms, limitations, strengths, weaknesses identified. Any comparison to PRM-based approaches. Any discussion of how the Teacher targets weaknesses - is it error-type level or concept level? Details about the verification mechanism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce64fbe-c199-4714-8c24-e8d752423677",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR6S4QgNW6R3mAPbUfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9cfa6d1-7eac-46a3-b02a-f160d25415ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pXyaVBeH3x19RfSrVE5it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 199,
      "cache_creation_input_tokens": 3855,
      "cache_read_input_tokens": 11816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3855,
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

_source line 26 · 2026-05-28T05:29:50.057Z_

<details><summary>↩ Tool result · `toolu_01NnHCf23nuapj54AGnhU4as`</summary>

```text
# Socratic-Zero: Literature Review Analysis

## Strengths Identified

The framework demonstrates substantial performance gains: "Socratic-Solver-8B achieved an average gain of +20.2 percentage points over prior data synthesis methods, reaching 56.1% average accuracy." The approach operates without external human-annotated data, addressing scalability concerns inherent in data-dependent methods.

Generator performance is particularly notable, with synthetic data enabling smaller models to match larger commercial systems. The ablation studies validate core design choices, confirming that initial supervised fine-tuning provided "7.9x greater improvement in Solver performance."

## Limitations and Weaknesses

The review mentions addressing "scalability issues, inconsistent data quality, and static curricula" as problems in existing approaches, implying these remain design constraints. However, the document provides limited explicit discussion of Socratic-Zero's own limitations.

The paper lacks formal theoretical analysis—future work includes "formal convergence analysis," suggesting theoretical grounding remains incomplete.

## Verification Mechanism

The Teacher employs "a verification function V(q, y) → {0, 1} that judges the correctness of a solution y for a given problem q." Quality control involves "Teacher self-verification, problem filtering, and MathRule integration for answer extraction and cross-validation."

## Teacher Targeting Strategy

The Teacher refines problems through "a problem refinement function G(q, y_fail) → (q', y'_ref)" responding to failed solutions. The document does not specify whether targeting occurs at error-type or concept level—only that failures are "revised...to create a new, instructive problem-solution pair."

## PRM-Based Comparison

No comparison to PRM (Process Reward Model) approaches appears in this content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9cfa6d1-7eac-46a3-b02a-f160d25415ef",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "2c15ae22-92d9-4542-8621-9986f1323e00",
  "sourceToolAssistantUUID": "f9cfa6d1-7eac-46a3-b02a-f160d25415ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T05:29:51.848Z_

<details><summary>↩ Tool result · `toolu_01BC3ByBmyx7rnWdR5ZemvDc`</summary>

```text
Web search results for query: "Socratic-Zero paper limitations PRM process reward model comparison review"

Links: [{"title":"[Literature Review] Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://www.themoonlight.io/en/review/socratic-prmbench-benchmarking-process-reward-models-with-systematic-reasoning-patterns"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://arxiv.org/html/2505.23474v1"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://arxiv.org/pdf/2505.23474"}]

Based on the search results, I found information about Socratic-PRMBench, which appears to be a benchmarking paper rather than "Socratic-Zero." Here are the key findings about limitations related to Process Reward Models (PRMs):

## Key Limitations Identified:

**Error Detection Limitations:**
Redundant error steps often appear more "normal" or plausible than other types of erroneous steps, hindering models' ability to identify them based on surface-level textual cues. Current PRMs may be limited by their reliance on surface-level pattern recognition for error detection, highlighting the need for more profound reasoning and analytical capabilities.

**Generalization Issues:**
PRMs can exhibit reward bias, error latency, or reduced transfer to novel reasoning patterns unless explicitly trained for diverse logical structures.

**Performance Gaps:**
PRMs perform significantly worse than LLMs prompted as critics. The best PRM (Qwen2.5-Math-PRM-7B) scores 68.0 overall, lower than the worst LLM critic (GPT-4o). Additionally, some PRMs perform below random chance, highlighting limitations likely due to PRM data annotation challenges.

**Benchmark Gaps:**
Existing benchmarks mainly focus on evaluating PRMs with stepwise correctness, ignoring a systematic evaluation of PRMs under various reasoning patterns.

Note: The search results show information about "Socratic-PRMBench" rather than a paper called "Socratic-Zero." If you were looking for different research, please clarify the exact paper title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb8a5ef-2459-476e-92bd-128fa60c8c2b",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "4d76dacc-7465-4cac-8f45-8ead09c017fd",
  "sourceToolAssistantUUID": "fbb8a5ef-2459-476e-92bd-128fa60c8c2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-28T05:29:54.893Z_

Let me also fetch the PDF directly for any additional details, and search for author affiliations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d76dacc-7465-4cac-8f45-8ead09c017fd",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR7hbaHrS5kKz9BBu4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2721bd01-38c8-4157-bf8b-a7a7bd40a7e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EG4bfGa7s7iguN54shfo9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 418,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 15671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1388,
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

_source line 29 · 2026-05-28T05:29:55.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnX8Pws1EENgAAfJfzgfBE`</summary>

```json
{
  "query": "Socratic-Zero Shaobo Wang Zhengbo Jiao affiliations university institution 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2721bd01-38c8-4157-bf8b-a7a7bd40a7e5",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR7hbaHrS5kKz9BBu4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e997c765-cf84-442e-89e7-7fa13da4a396",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EG4bfGa7s7iguN54shfo9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 418,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 15671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1388,
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

_source line 30 · 2026-05-28T05:29:57.174Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017A46LSHujVapbjhNGE7bvk`</summary>

```json
{
  "url": "https://huggingface.co/papers/2509.24726",
  "prompt": "Extract all information: authors, affiliations, abstract, any community discussion or comments about the paper. Any criticisms or praise from the community."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e997c765-cf84-442e-89e7-7fa13da4a396",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR7hbaHrS5kKz9BBu4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18072bfa-f9c5-4075-8e39-fe839b0376ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EG4bfGa7s7iguN54shfo9s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 418,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 15671,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1388
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 418,
          "output_tokens": 190,
          "cache_read_input_tokens": 15671,
          "cache_creation_input_tokens": 1388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1388,
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

_source line 31 · 2026-05-28T05:29:57.852Z_

<details><summary>↩ Tool result · `toolu_017A46LSHujVapbjhNGE7bvk`</summary>

```text
&lt;persisted-output>
Output too large (82.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tool-results/toolu_017A46LSHujVapbjhNGE7bvk.txt

Preview (first 2KB):
Title: Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution

URL Source: https://arxiv.org/html/2509.24726

Markdown Content:
Shaobo Wang ∗β Zhengbo Jiao ∗α,β,γ Zifan Zhang α,δ Yilang Peng α,ϵ

Xu Ze α Boyu Yang α Wei Wang α Hu Wei †α Linfeng Zhang †β

α Alibaba Group Holding Limited β EPIC Lab, Shanghai Jiao Tong University 

γ Shanghai University of Finance and Economics δ Wuhan University ϵ Zhejiang University 

 * Equal contribution † Corresponding authors

###### Abstract

Recent breakthroughs in large language models (LLMs) on reasoning tasks rely heavily on massive, high-quality datasets—typically human-annotated and thus difficult to scale. While data synthesis or distillation offers a promising alternative, existing methods struggle with inconsistent data quality and an inability to dynamically adapt to the evolving capabilities of the model, leading to suboptimal training signals. To address these limitations, we introduce Socratic-Zero, a fully autonomous framework that generates high-quality training data from minimal seed examples through the co-evolution of three agents: the Teacher, the Solver, and the Generator. The Solver continuously refines its reasoning by learning from preference feedback on both successful and failed trajectories; the Teacher adaptively crafts increasingly challenging questions based on the Solver’s weaknesses; and the Generator distills the Teacher’s question-design strategy to enable scalable, high-fidelity curriculum generation. This closed-loop system produces a self-improving curriculum—requiring no pre-existing tasks or labels. Remarkably, starting from only 100 seed questions, our Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods across seven mathematical reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva, and GSM8K), with consistent gains on both Qwen3 and GLM4 series models. Even more surprisingly, synthetic data from Socratic-Ge
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18072bfa-f9c5-4075-8e39-fe839b0376ee",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "4ee77d7b-d22d-436e-b9ee-c3abe0d1846b",
  "sourceToolAssistantUUID": "18072bfa-f9c5-4075-8e39-fe839b0376ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T05:30:00.949Z_

<details><summary>↩ Tool result · `toolu_01LnX8Pws1EENgAAfJfzgfBE`</summary>

```text
Web search results for query: "Socratic-Zero Shaobo Wang Zhengbo Jiao affiliations university institution 2025"

Links: [{"title":"Publications | Shaobo Wang (王少博)","url":"https://gszfwsb.github.io/publications/"},{"title":"Preprint. Under Review. SOCRATIC-ZERO: BOOTSTRAPPING REASONING VIA","url":"https://arxiv.org/pdf/2509.24726"},{"title":"Shaobo Wang (王少博)","url":"https://gszfwsb.github.io/"},{"title":"[2509.24726] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/abs/2509.24726"},{"title":"[PDF] Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Socratic-Zero-:-Bootstrapping-Reasoning-via-Agent-Wang-Jiao/08d60a8f1169eb65c120b67a1b6b8a8c448f9913"},{"title":"Socratic-Geo: Synthetic Data Generation and Geometric Reasoning via Multi-Agent Interaction","url":"https://arxiv.org/html/2602.03414"},{"title":"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://arxiv.org/html/2509.24726"},{"title":"Paper page - Socratic-Zero : Bootstrapping Reasoning via Data-Free Agent Co-evolution","url":"https://huggingface.co/papers/2509.24726"},{"title":"Shaobo Wang | OpenReview","url":"https://openreview.net/profile?id=~Shaobo_Wang1"},{"title":"Shaobo Wang","url":"https://www.catalyzex.com/author/Shaobo%20Wang"}]

Based on my search results, here is information about the affiliations for the Socratic-Zero paper authors:

## Author Affiliations for Socratic-Zero (2025)

For the Socratic-Zero paper:
- Shaobo Wang is affiliated with EPIC Lab, Shanghai Jiao Tong University
- Zhengbo Jiao is affiliated with Alibaba Group Holding Limited, EPIC Lab at Shanghai Jiao Tong University, and Shanghai University of Finance and Economics
- Zifan Zhang is affiliated with Alibaba Group Holding Limited and Wuhan University
- Yilang Peng is affiliated with Alibaba Group Holding Limited and Zhejiang University
- Xu Ze, Boyu Yang, Wei Wang, and Hu Wei are affiliated with Alibaba Group Holding Limited
- Linfeng Zhang is affiliated with EPIC Lab, Shanghai Jiao Tong University

Additionally, Shaobo Wang is a second-year Ph.D. candidate in the School of Artificial Intelligence at Shanghai Jiao Tong University (SJTU), and is also a research intern at the Alibaba Qwen Team.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e997c765-cf84-442e-89e7-7fa13da4a396",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "9a5d7437-ad3b-4c60-9b36-4f7a0a4f3d16",
  "sourceToolAssistantUUID": "e997c765-cf84-442e-89e7-7fa13da4a396",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-28T05:30:04.323Z_

The HuggingFace fetch returned the full paper HTML. Let me read the saved output for more details on the Teacher mechanism and any PRM discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a5d7437-ad3b-4c60-9b36-4f7a0a4f3d16",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR8NTfnMJCYR22FsLgW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "105871d1-7d60-48bf-9cb6-6b8ad916fa95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRDFbBzVDbQsr9SkNjY2nc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 646,
      "cache_creation_input_tokens": 1405,
      "cache_read_input_tokens": 17059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1405,
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

_source line 34 · 2026-05-28T05:30:04.951Z_

<details open><summary>🔧 Tool call — Read · `toolu_016FEhzz9Nwb3sh8UqtPk4D6`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tool-results/toolu_017A46LSHujVapbjhNGE7bvk.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "105871d1-7d60-48bf-9cb6-6b8ad916fa95",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR8NTfnMJCYR22FsLgW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0696ad34-d09a-4813-a915-6422f034058d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRDFbBzVDbQsr9SkNjY2nc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 646,
      "cache_creation_input_tokens": 1405,
      "cache_read_input_tokens": 17059,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1405
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 646,
          "output_tokens": 177,
          "cache_read_input_tokens": 17059,
          "cache_creation_input_tokens": 1405,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1405,
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

_source line 35 · 2026-05-28T05:30:05.243Z_

<details><summary>↩ Tool result · `toolu_016FEhzz9Nwb3sh8UqtPk4D6`</summary>

```text
1	Title: Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution
2	
3	URL Source: https://arxiv.org/html/2509.24726
4	
5	Markdown Content:
6	Shaobo Wang ∗β Zhengbo Jiao ∗α,β,γ Zifan Zhang α,δ Yilang Peng α,ϵ
7	
8	Xu Ze α Boyu Yang α Wei Wang α Hu Wei †α Linfeng Zhang †β
9	
10	α Alibaba Group Holding Limited β EPIC Lab, Shanghai Jiao Tong University 
11	
12	γ Shanghai University of Finance and Economics δ Wuhan University ϵ Zhejiang University 
13	
14	 * Equal contribution † Corresponding authors
15	
16	###### Abstract
17	
18	Recent breakthroughs in large language models (LLMs) on reasoning tasks rely heavily on massive, high-quality datasets—typically human-annotated and thus difficult to scale. While data synthesis or distillation offers a promising alternative, existing methods struggle with inconsistent data quality and an inability to dynamically adapt to the evolving capabilities of the model, leading to suboptimal training signals. To address these limitations, we introduce Socratic-Zero, a fully autonomous framework that generates high-quality training data from minimal seed examples through the co-evolution of three agents: the Teacher, the Solver, and the Generator. The Solver continuously refines its reasoning by learning from preference feedback on both successful and failed trajectories; the Teacher adaptively crafts increasingly challenging questions based on the Solver’s weaknesses; and the Generator distills the Teacher’s question-design strategy to enable scalable, high-fidelity curriculum generation. This closed-loop system produces a self-improving curriculum—requiring no pre-existing tasks or labels. Remarkably, starting from only 100 seed questions, our Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods across seven mathematical reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva, and GSM8K), with consistent gains on both Qwen3 and GLM4 series models. Even more surprisingly, synthetic data from Socratic-Generator-32B enables student LLMs to achieve superior performance compared to other state-of-the-art (SOTA) commercial LLMs on these benchmarks, including Qwen3-235B-A22B, DeepSeek-V3.1-671B, GPT-5, Gemini-2.5-Pro, Grok-4, and Claude-4.1-Opus.
19	
20	![Image 1: Refer to caption](https://arxiv.org/html/2509.24726v1/x1.png)
21	
22	Figure 1: The Socratic-Zero Framework: From Philosophical Analogy to a Co-evolutionary System. (a) The Socratic Methodlogy illustrates the philosophical foundation: the Teacher (Socrates) acts as an intellectual midwife, eliciting understanding through probing questions; the Practitioner (Aristotle) learns not by receiving answers, but by being guided along a path of reasoned inquiry; and the Apprentice-Teacher (Plato) learns to teach by observing and internalizing the master’s method. (b) The Socratic-Zero Framework operationalizes this philosophy. Here, the Teacher—a powerful LLM—guides the co-evolution of two agents. The Solver improves by generating solutions and refining them through the Teacher’s feedback, while the Generator evolves by strategically distilling the Teacher’s behavior to produce an increasingly suitable curriculum for the Solver.
23	
24	1 Introduction
25	--------------
26	
27	The pursuit of advanced mathematical reasoning in large language models has reached a critical juncture. While recent breakthroughs have demonstrated remarkable capabilities on complex mathematical problems(Hendrycks et al., [2021](https://arxiv.org/html/2509.24726v1#bib.bib13); Cobbe et al., [2021](https://arxiv.org/html/2509.24726v1#bib.bib7)), these advances rely on massive datasets of meticulously curated reasoning trajectories — a requirement that is both costly and fundamentally unscalable. Current state-of-the-art models depend on millions of human-annotated problem-solution pairs and hand-designed curricula(Yu et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib32)), creating a fundamental bottleneck that limits both accessibility and the potential for models to evolve beyond human-curated knowledge boundaries.
28	
29	Current methodologies remain entrenched in a static paradigm: datasets are frozen upon collection, curricula are handcrafted in advance, and models are trained on fixed problem distributions. This approach suffers from critical weaknesses: it cannot adapt to evolving model capabilities during training, fails to exploit rich feedback signals for targeting specific weaknesses, and requires extensive human expertise for curriculum design. Recent efforts through synthetic data generation(Lee et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib18); Chen et al., [2025b](https://arxiv.org/html/2509.24726v1#bib.bib5)) and iterative training(Zhao et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib36); Huang et al., [2025b](https://arxiv.org/html/2509.24726v1#bib.bib16)) have shown promise but remain constrained by their reliance on external supervision and lack of effective quality control mechanisms for synthesized content.
30	
31	To overcome these limitations, we introduce Socratic-Zero, a paradigm-shifting framework that eliminates dependency on large-scale external datasets while enabling truly autonomous reasoning improvement. Inspired by the Socratic method of learning through questioning (Figure[1](https://arxiv.org/html/2509.24726v1#S0.F1 "Figure 1 ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")(a)), our approach implements co-evolution between three agents: a Solver that attempts to solve mathematical questions, a Teacher that strategically generates challenging problems to expose the Solver’s weaknesses, and a Generator that learns to distill and scale the Teacher’s problem generation strategy. This architecture (Figure[1](https://arxiv.org/html/2509.24726v1#S0.F1 "Figure 1 ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")(b)) translates the philosophical dialogue of the Socratic method into a concrete, co-evolutionary computational framework. Unlike conventional pipelines that decouple data generation from model training, Socratic-Zero unifies them within a continuous co-evolutionary loop formalized as a optimization problem. Our contributions are threefold:
32	
33	![Image 2: Refer to caption](https://arxiv.org/html/2509.24726v1/x2.png)
34	
35	Figure 2: Overall performance comparison demonstrating the giant effectiveness of Socratic-Zero. (a) Our Socratic-Generator-32B produces synthetic data that enables student models to achieve performance competitive with much larger state-of-the-art models, showcasing strong generalization capabilities. (b) Our Socratic-Solver-8B achieves an impressive 56.1% average accuracy, marking a substantial +20.2 point improvement over the baseline. 
36	
37	*   •Multi-Agent Co-Evolutionary Framework: We establish a theoretical foundation for co-evolutionary learning where the Solver, Teacher, and Generator agents interact dynamically, formalizing reasoning improvement as an adaptive curriculum learning problem (Figure[1](https://arxiv.org/html/2509.24726v1#S0.F1 "Figure 1 ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")(b)). 
38	*   •Socratic-Zero System: We implement a concrete framework where the Solver improves via preference learning, the Teacher evaluates correctness and generates adaptive curriculum, and the Generator learns strategic distillation through value-weighted supervised fine-tuning (WSFT), enabling autonomous reasoning advancement from minimal seed data. 
39	*   •Superior Empirical Performance: Our Socratic-Solver-8B achieves +20.2 points average improvement across seven mathematical reasoning benchmarks (Figure[2](https://arxiv.org/html/2509.24726v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")(b)), while synthetic data from our Socratic-Generator-32B achieves 37.72% downstream training effectiveness, outperforming leading commercial models including Qwen3-235B-A22B at 37.13%, Claude-4.1-Opus at 37.63%, Gemini-2.5-Pro at 37.20%, Grok-4 at 37.01%, GPT-5 at 36.62%, and DeepSeek-V3.1 at 36.62% (Figure[2](https://arxiv.org/html/2509.24726v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")(a)). 
40	
41	2 Related Work
42	--------------
43	
44	##### Data Synthesis.
45	
46	To alleviate data scarcity, researchers have leveraged LLMs’ generative capabilities to synthesize training samples. Early approaches used prompt engineering to guide question-answer generation(Yu et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib32); Zhan et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib33)). Subsequently, LLM2LLM(Lee et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib18)) and WarriorMath(Chen et al., [2025b](https://arxiv.org/html/2509.24726v1#bib.bib5)) introduced deficiency-aware mechanisms, where teacher models identify knowledge gaps and generate targeted data. More recently, Absolute Zero(Zhao et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib36)) and R-Zero(Huang et al., [2025b](https://arxiv.org/html/2509.24726v1#bib.bib16)) explored fully autonomous self-play paradigms for continuous task generation and learning. While these advances achieve data autonomy, they lack effective quality control mechanisms, resulting in repeated use of low-value samples that severely impact effectiveness.
47	
48	##### Data Distillation.
49	
50	Knowledge distillation transfers capabilities from powerful teacher models to lighter student models. Early work like Orca(Mukherjee et al., [2023](https://arxiv.org/html/2509.24726v1#bib.bib22)) used imitation learning to replicate teacher reasoning chains. Policy distillation(Wang et al., [2025b](https://arxiv.org/html/2509.24726v1#bib.bib30)) extends this by transferring dynamic decision-making strategies. GKD(Agarwal et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib1)) enables students to learn from their own sequences using teacher feedback for policy correction. However, students passively accept teacher feedback without evaluating reliability, degrading learning quality when guidance is suboptimal. These methods also rely on static datasets, unable to dynamically adjust content based on students’ evolving capabilities. While recent advances(Wang et al., [2025a](https://arxiv.org/html/2509.24726v1#bib.bib28); Zhao et al., [2023](https://arxiv.org/html/2509.24726v1#bib.bib37); Zhang et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib35); Chen et al., [2024a](https://arxiv.org/html/2509.24726v1#bib.bib4); Liu et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib19)) promote data-centric optimization, they lack effective quality control and adaptive curriculum generation.
51	
52	##### Preference Learning.
53	
54	Translating feedback signals into model optimization is central to self-evolution systems. Early approaches like RLHF(Stiennon et al., [2020](https://arxiv.org/html/2509.24726v1#bib.bib26)) trained reward models on human preferences then fine-tuned policies, but this process is complex and unstable. Recent methods like DPO(Rafailov et al., [2023](https://arxiv.org/html/2509.24726v1#bib.bib25)) and RWSFT(Mukherjee et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib23)) directly optimize preferences, improving efficiency and stability. Combined with self-correction mechanisms like Self-Refine(Madaan et al., [2023](https://arxiv.org/html/2509.24726v1#bib.bib21)), models possess preliminary closed-loop capabilities. Further advances including Self-Evolved Reward Learning(Huang et al., [2025a](https://arxiv.org/html/2509.24726v1#bib.bib15)), Self-Play Fine-Tuning(Chen et al., [2024b](https://arxiv.org/html/2509.24726v1#bib.bib6)), and Self-Play Critic(Chen et al., [2025a](https://arxiv.org/html/2509.24726v1#bib.bib3)) explore autonomous feedback strategies. However, these methods lack unified, co-evolving frameworks for feedback generation and validation.
55	
56	3 Methodology
57	-------------
58	
59	### 3.1 The Socratic-Zero Framework
60	
61	We introduce Socratic-Zero, a fully autonomous, co-evolutionary framework designed to bootstrap mathematical reasoning from a minimal set of seed problems, entirely without relying on external human-annotated data. As illustrated in Figure[3](https://arxiv.org/html/2509.24726v1#S3.F3 "Figure 3 ‣ 3.1 The Socratic-Zero Framework ‣ 3 Methodology ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), the system operates as a self-improving loop among three agents: a Solver that learns to reason, a fixed Teacher that acts as an oracle for evaluation and problem refinement, and a Generator that learns to synthesize a curriculum.
62	
63	At each iteration t t, the framework operates on a curriculum of problems and their reference solutions, denoted as 𝒟 t={(q,y ref)}\mathcal{D}_{t}=\{(q,y_{\text{ref}})\}. The core of Socratic-Zero is the co-evolution of the Solver and Generator under the guidance of the Teacher. The Solver is trained to solve problems from 𝒟 t\mathcal{D}_{t}. Its failures are then used by the Teacher to create new, targeted problems. The Generator, in turn, distills the Teacher’s strategy to produce a scalable curriculum. This process creates a dynamic curriculum that continuously adapts to the Solver’s evolving capabilities, ensuring the training signals remain maximally informative. The agents are formally defined as follows:
64	
65	![Image 3: Refer to caption](https://arxiv.org/html/2509.24726v1/x3.png)
66	
67	Figure 3: Overview of the Socratic-Zero Framework. (a) Solver Evolving: The Solver attempts to solve problems and learns from preference pairs of correct and incorrect solutions via DPO, while the frozen Teacher strategically generates challenging problems based on Solver failures using fixed generation and evaluation functions. (b) Generator Evolving: The Generator distills the Teacher’s problem generation strategy using value-weighted supervised learning. Together, these create a self-improving loop where the curriculum dynamically evolves to maintain optimal challenge levels for the Solver’s current capabilities.
68	
69	The curriculum expands based on the Solver’s mistakes. At iteration t t, the set of Solver failures on the current curriculum 𝒟 t\mathcal{D}_{t} is collected:
70	
71	ℱ t={(q,y 𝒮)∣(q,y ref)∈𝒟 t,y 𝒮∼π θ 𝒮(t)(⋅∣q),V(q,y 𝒮)=0}.\mathcal{F}_{t}=\left\{(q,y_{\mathcal{S}})\mid(q,y_{\text{ref}})\in\mathcal{D}_{t},y_{\mathcal{S}}\sim\pi_{\theta_{\mathcal{S}}^{(t)}}(\cdot\mid q),V(q,y_{\mathcal{S}})=0\right\}.(1)
72	
73	The Teacher refines each failure into a new, instructive problem-solution pair. The set of these new pairs, 𝒟 new\mathcal{D}_{\text{new}}, is used to augment the curriculum for the next iteration:
74	
75	𝒟 t+1=𝒟 t∪{G​(q,y 𝒮)∣(q,y 𝒮)∈ℱ t}⏟𝒟 new.\mathcal{D}_{t+1}=\mathcal{D}_{t}\cup\underbrace{\left\{G(q,y_{\mathcal{S}})\mid(q,y_{\mathcal{S}})\in\mathcal{F}_{t}\right\}}_{\mathcal{D}_{\text{new}}}.(2)
76	
77	The full co-evolutionary training procedure is detailed in Algorithm[1](https://arxiv.org/html/2509.24726v1#alg1 "Algorithm 1 ‣ Appendix H Pseudo Code of Socratic-Zero ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
78	
79	### 3.2 Solver Training via Online Preference Optimization
80	
81	The Solver’s policy π θ 𝒮\pi_{\theta_{\mathcal{S}}} is improved through online preference learning, leveraging the Teacher’s verification function V V to create a feedback loop. For each problem q∈𝒟 t q\in\mathcal{D}_{t}, the Solver generates k k solution attempts, {y 𝒮(i)}i=1 k\{y_{\mathcal{S}}^{(i)}\}_{i=1}^{k}. These attempts are partitioned into a set of “winning” (correct) solutions 𝒴 w​(q)\mathcal{Y}_{w}(q) and “losing” (incorrect) solutions 𝒴 l​(q)\mathcal{Y}_{l}(q):
82	
83	𝒴 l​(q)\displaystyle\mathcal{Y}_{l}(q)={y 𝒮(i)∣V​(q,y 𝒮(i))=0},\displaystyle=\{y_{\mathcal{S}}^{(i)}\mid V(q,y_{\mathcal{S}}^{(i)})=0\},(3)
84	𝒴 w​(q)\displaystyle\mathcal{Y}_{w}(q)={y 𝒮(i)∣V​(q,y 𝒮(i))=1}∪{y ref∣if​∀i,V​(q,y 𝒮(i))=0},\displaystyle=\{y_{\mathcal{S}}^{(i)}\mid V(q,y_{\mathcal{S}}^{(i)})=1\}\cup\{y_{\text{ref}}\mid\text{if }\forall i,V(q,y_{\mathcal{S}}^{(i)})=0\},(4)
85	
86	where y ref y_{\text{ref}} is the reference solution from the curriculum. If the Solver fails to generate any correct solution, the ground-truth solution serves as the sole winning example. This ensures a valid preference pair (y w,y l)(y_{w},y_{l}), where y w∈𝒴 w​(q)y_{w}\in\mathcal{Y}_{w}(q) and y l∈𝒴 l​(q)y_{l}\in\mathcal{Y}_{l}(q), can always be constructed.
87	
88	The Solver’s parameters θ 𝒮\theta_{\mathcal{S}} are then updated using the Direct Preference Optimization (DPO) loss(Rafailov et al., [2023](https://arxiv.org/html/2509.24726v1#bib.bib25)). This objective maximizes the likelihood of preferred solutions over rejected ones:
89	
90	ℒ DPO​(θ 𝒮;θ ref)=−𝔼 q∼𝒟 t,y w∼𝒴 w​(q),y l∼𝒴 l​(q)​[log⁡σ​(β​log⁡π θ 𝒮​(y w∣q)π θ ref​(y w∣q)−β​log⁡π θ 𝒮​(y l∣q)π θ ref​(y l∣q))],\mathcal{L}_{\text{DPO}}(\theta_{\mathcal{S}};\theta_{\text{ref}})=-\mathbb{E}_{q\sim\mathcal{D}_{t},y_{w}\sim\mathcal{Y}_{w}(q),y_{l}\sim\mathcal{Y}_{l}(q)}\left[\log\sigma\left(\beta\log\frac{\pi_{\theta_{\mathcal{S}}}(y_{w}\mid q)}{\pi_{\theta_{\text{ref}}}(y_{w}\mid q)}-\beta\log\frac{\pi_{\theta_{\mathcal{S}}}(y_{l}\mid q)}{\pi_{\theta_{\text{ref}}}(y_{l}\mid q)}\right)\right],(5)
91	
92	where π θ ref\pi_{\theta_{\text{ref}}} is a frozen reference policy (e.g., π θ 𝒮\pi_{\theta_{\mathcal{S}}} from the start of the iteration), β\beta is a temperature hyperparameter, and σ\sigma is the sigmoid function.
93	
94	### 3.3 Generator Training via Offline Value-Weighted Distillation
95	
96	To ensure scalable curriculum generation without perpetual reliance on the expensive Teacher, the Generator π θ 𝒢\pi_{\theta_{\mathcal{G}}} is trained to distill the Teacher’s problem refinement strategy. An effective curriculum should feature problems of desirable difficulty—challenging enough to be informative but not so difficult as to be unsolvable.
97	
98	We formalize this concept with a utility function U​(q′|π θ 𝒮)U(q^{\prime}|\pi_{\theta_{\mathcal{S}}}) that scores a new problem q′q^{\prime} based on the current Solver’s performance. Let s q=1 k​∑i=1 k V​(q,y 𝒮(i))s_{q}=\frac{1}{k}\sum_{i=1}^{k}V(q,y_{\mathcal{S}}^{(i)}) be the success rate of the Solver π θ 𝒮\pi_{\theta_{\mathcal{S}}} over k k attempts. The utility is defined by an unnormalized Gaussian centered at a target success rate μ\mu:
99	
100	U​(q′|π θ 𝒮)=exp⁡(−(s q′−μ)2 2​σ 2).U(q^{\prime}|\pi_{\theta_{\mathcal{S}}})=\exp\left(-\frac{(s_{q^{\prime}}-\mu)^{2}}{2\sigma^{2}}\right).(6)
101	
102	We set μ=0.5\mu=0.5 to incentivize problems at the frontier of the Solver’s capabilities, with σ\sigma controlling the tolerance for deviation.
103	
104	The Generator is trained via weighted supervised fine-tuning (WSFT) to mimic the Teacher’s generation of high-utility problems. The training data 𝒟 𝒢\mathcal{D}_{\mathcal{G}} is constructed from the set of Solver failures ℱ t\mathcal{F}_{t} and the corresponding Teacher-refined problems from 𝒟 new\mathcal{D}_{\text{new}}:
105	
106	𝒟 𝒢={(q,y fail,q′)∣(q,y fail)∈ℱ t,(q′,y ref′)=G​(q,y fail)}.\mathcal{D}_{\mathcal{G}}=\{(q,y_{\text{fail}},q^{\prime})\mid(q,y_{\text{fail}})\in\mathcal{F}_{t},(q^{\prime},y^{\prime}_{\text{ref}})=G(q,y_{\text{fail}})\}.
107	
108	The Generator’s objective is to maximize the utility-weighted log-likelihood of producing the Teacher’s refined problems:
109	
110	ℒ WSFT​(θ 𝒢)=−𝔼(q,y fail,q′)∼𝒟 𝒢​[U​(q′|π θ 𝒮)⋅log⁡π θ 𝒢​(q′∣q,y fail)].\mathcal{L}_{\text{WSFT}}(\theta_{\mathcal{G}})=-\mathbb{E}_{(q,y_{\text{fail}},q^{\prime})\sim\mathcal{D}_{\mathcal{G}}}\left[U(q^{\prime}|\pi_{\theta_{\mathcal{S}}})\cdot\log\pi_{\theta_{\mathcal{G}}}(q^{\prime}\mid q,y_{\text{fail}})\right].(7)
111	
112	This objective steers the Generator towards producing problems that are optimally challenging for the current Solver, effectively internalizing the Teacher’s expert curriculum design principles.
113	
114	4 Experiments
115	-------------
116	
117	### 4.1 Experimental Setup
118	
119	Models. We employed Qwen3-235B-A22B-Instruct-2507(Yang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib31)) as the Teacher model to provide high-quality evaluation and curriculum generation. We used Qwen3-32B(Yang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib31)) as the Generator to learn and distill the Teacher’s problem generation strategies. We conducted Solver experiments on multiple model architectures including Qwen3-8B-base, Qwen3-14B-base(Yang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib31)), and GLM4-9B-base(GLM et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib11)) to demonstrate cross-model generalization. We compared strong baselines including Gemini-2.5-Pro-06-17(Comanici et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib8)), GPT5-0807-global, and DeepSeek-v3.1-671B(DeepSeek-AI et al., [2025b](https://arxiv.org/html/2509.24726v1#bib.bib10)) against our approach. For downstream evaluation of generated data quality, we fine-tuned DeepSeek-R1-Distill-Llama-8B(DeepSeek-AI et al., [2025a](https://arxiv.org/html/2509.24726v1#bib.bib9)) as the student model.
120	
121	Benchmarks. We used seven mathematical reasoning benchmarks for evaluation, including AMC(Cao et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib2)), Minerva(Nagrani et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib24)), MATH-500(Hendrycks et al., [2021](https://arxiv.org/html/2509.24726v1#bib.bib13)), GSM8K(Cobbe et al., [2021](https://arxiv.org/html/2509.24726v1#bib.bib7)), Olympiad-Bench(He et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib12)), AIME-2024, and AIME-2025. Additionally, we employed three general reasoning benchmarks to assess the transfer of mathematical reasoning improvements to broader cognitive abilities, namely BBEH(Kazemi et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib17)), MMLU-Pro(Wang et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib29)), and SuperGPQA(Team et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib27)).
122	
123	Curriculum Settings. The initial curriculum 𝒞 0\mathcal{C}_{0} contained 100 questions sampled from the MATH training set(Hendrycks et al., [2021](https://arxiv.org/html/2509.24726v1#bib.bib13)) following specific diversity and difficulty criteria (detailed in Appendix[F](https://arxiv.org/html/2509.24726v1#A6 "Appendix F Seed Selection Protocol ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")). All Solver models first underwent LoRA-based(Hu et al., [2021](https://arxiv.org/html/2509.24726v1#bib.bib14)) SFT on a 1,500-problem dataset of Level 5 difficulty. Key hyperparameters: k=8 k=8 solution trajectories per problem, reward parameters μ=0.5\mu=0.5 and σ=0.2\sigma=0.2, and training batches combined 100% new problems with 25% historical curriculum for replay.
124	
125	Solver Evaluation. For each test question, we generated 32 solutions using zero-shot prompting with temperature 0.7. We determined correctness through a dual-verification mechanism combining rule-based answer extraction and semantic validation. We reported Mean@32 accuracy across all evaluations. Detailed evaluation protocols, including sampling strategies, answer extraction methods, and LLM judge configurations, are provided in Appendix[G](https://arxiv.org/html/2509.24726v1#A7 "Appendix G Evaluation Protocol Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
126	
127	Baselines.Baselines. We employed two strong baselines for comparison. Static Augmentation (SA) follows traditional approaches via MetaMath(Yu et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib32)) and WizardMath(Luo et al., [2023](https://arxiv.org/html/2509.24726v1#bib.bib20)), augmenting training data with fixed synthetic questions generated offline without adaptive curriculum evolution. LLM2LLM(Lee et al., [2024](https://arxiv.org/html/2509.24726v1#bib.bib18)) implements iterative self-training where models generate questions based on current failures and retrain on augmented datasets. Both baselines use identical SFT initialization for fair comparison.
128	
129	Generator Evaluation. We prompted each generator with 1,000 SAND-Math(Zhang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib34)) seeds to produce 3 variants each, resulting in 3,000 total generated questions. We measured validity rate by having Qwen3-235B-A22B-Instruct-2507 attempt to solve each generated question under a 4,096-token, 600-s timeout constraint. We evaluated downstream utility by fine-tuning DeepSeek-R1-Distill-Llama-8B on the QAs and measuring performance on mathematical reasoning benchmarks.
130	
131	Infrastructure. We conducted training experiments on 8×NVIDIA H20 GPUs. We performed Teacher model inference using 16×AMD MI308X GPUs. Detail provided in Appendix[D](https://arxiv.org/html/2509.24726v1#A4 "Appendix D Teacher Model Infrastructure ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
132	
133	### 4.2 Solver Results
134	
135	##### Baseline Comparison.
136	
137	Table[1](https://arxiv.org/html/2509.24726v1#S4.T1 "Table 1 ‣ Transfer to General Reasoning. ‣ 4.2 Solver Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") shows Socratic achieves 56.1% average accuracy, outperforming Static Augmentation by +15.4 points and LLM2LLM by +15.2 points. Notable gains appear on competition problems: AIME-24 (+19.1) and AIME-25 (+16.5), demonstrating the advantages of DPO-based preference learning and adaptive curriculum generation.
138	
139	##### Cross-Architecture Generalization.
140	
141	Table[2](https://arxiv.org/html/2509.24726v1#S4.T2 "Table 2 ‣ Transfer to General Reasoning. ‣ 4.2 Solver Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") validates that Socratic principles transcend specific model families. On GLM4-9B-base, Socratic Stage 3 achieves 52.3% average accuracy (+17.1 points over base model), with strong improvements on AIME benchmarks: AIME-25 (+20.4) and AIME-24 (+23.9). Similarly, on Qwen3-14B-base, Stage 3 reaches 60.3% (+17.3 points), demonstrating consistent effectiveness across different architectures and addressing fundamental reasoning capabilities.
142	
143	##### Transfer to General Reasoning.
144	
145	Table[3](https://arxiv.org/html/2509.24726v1#S4.T3 "Table 3 ‣ Transfer to General Reasoning. ‣ 4.2 Solver Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") shows mathematical reasoning improvements transfer to broader cognitive abilities, with +6.02 points average improvement across BBEH, MMLU-Pro, and SuperGPQA benchmarks.
146	
147	Table 1: Solver Evaluation Results with different training methods. Results are reported on seven benchmarks (AMC, Minerva, MATH-500, GSM8K, Olympiad, AIME-25, AIME-24) and their average. Arrow values represent absolute point changes relative to Static Augmentation, where ↑\uparrow indicates improvement and ↓\downarrow indicates decline.
148	
149	Training Method Benchmark Datasets Avg.
150	AMC Minerva MATH-500 GSM8K Olympiad AIME-25 AIME-24
151	Qwen3-8B-base
152	+ Zero-shot 32.5 31.3 48.8 63.4 24.1 4.2 5.1 29.9
153	+ SFT 39.1 37.8 56.9 68.2 31.7 8.1 9.3 35.9
154	+ Static Augmentation 45.8 41.9 62.7 74.6 35.9 11.4 12.3 40.7
155	Qwen3-8B-base with LLM2LLM
156	+ Stage 1 41.6 41.2 53.1 78.3 32.4 6.7 8.9 37.5
157	+ Stage 2 43.2 40.6 54.9 79.1 33.8 7.2 9.1 38.3
158	+ Stage 3 44.9 42.1 66.8 79.4 34.6 7.9 10.4 40.9
159	Qwen3-8B-base with Socratic-Zero (Ours)
160	+ Stage 1 43.8 39.4 60.2 69.7 35.3 10.6 11.8 38.7
161	+ Stage 2 49.3 40.7 63.4 71.8 38.2 12.9 15.6 41.7
162	+ Stage 3 63.7 52.4 81.2 87.3 55.1 24.6 28.4 56.1
163	
164	Table 2: Cross-Model Generalization Results with different training stages. Each block corresponds to a model (GLM4-9B, Qwen3-14B). Results are reported on seven benchmarks (AMC, Minerva, MATH-500, GSM8K, Olympiad, AIME-25, AIME-24) and their average. Values with arrows represent absolute point changes relative to SFT for each model.
165	
166	Training Method Benchmark Datasets Avg
167	AMC Minerva MATH-500 GSM8K Olympiad AIME-25 AIME-24
168	GLM4-9B-base
169	+Zero-shot 34.5 37.3 52.3 72.5 34.8 7.5 7.2 35.2
170	+ SFT 38.4 44.8 63.8 77.2 41.3 15.1 19.3 42.8
171	+ Socratic Stage 1 39.4 47.3 67.9 79.8 43.4 15.6 24.0 45.3
172	+ Socratic Stage 2 42.3 49.4 68.1 82.5 45.5 19.1 25.3 47.5
173	+ Socratic Stage 3 47.5 52.8 73.8 83.9 49.4 27.9 31.1 52.3
174	Qwen3-14B-base
175	+Zero-shot 48.8 40.5 62.0 91.5 38.4 9.6 10.0 43.0
176	+ SFT 61.3 51.8 71.5 92.2 47.3 18.1 20.3 51.8
177	+ Socratic Stage 1 62.9 55.1 74.6 91.8 52.5 19.8 21.7 54.1
178	+ Socratic Stage 2 65.4 57.4 76.7 92.3 54.2 24.8 23.3 56.3
179	+ Socratic Stage 3 70.0 60.7 80.2 93.7 58.3 28.9 30.1 60.3
180	
181	Table 3: Performance on general reasoning benchmarks with different training stages. Results are reported on three benchmarks (BBEH, MMLU-Pro, SuperGPQA) and their average. Values with arrows represent absolute point changes relative to zero-shot Qwen3-8B-base performance.
182	
183	Training Method General Reasoning Benchmarks Avg.
184	BBEH MMLU-Pro SuperGPQA
185	Qwen3-8B-Base
186	+ Zero-shot 7.68 50.00 24.73 27.47
187	Base Model with Socratic (Ours)
188	+ Stage 1 8.48 55.71 27.32 30.50
189	+ Stage 2 9.11 59.29 29.73 32.71
190	+ Stage 3 9.54 60.89 30.05 33.49
191	
192	### 4.3 Generator Results
193	
194	We assessed both the intrinsic quality of generated problems and their downstream training effectiveness, with Socratic-Generator-32B being compared against its base model and SOTA commercial large language models to determine whether strategic specialization can match the performance of much advanced larger models.
195	
196	#### 4.3.1 Evaluation Protocol
197	
198	We adopted a standardized, three-stage evaluation pipeline to holistically assess both the intrinsic quality of generated problems and their extrinsic utility in downstream model training. The full procedure is formalized below.
199	
200	Step 1: Problem Generation. We prompted each generator with 1,000 seed problems from SAND-Math(Zhang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib34)) and tasked with producing five augmented variants per seed, resulting in 3,000 total generated problems per model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0696ad34-d09a-4813-a915-6422f034058d",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "af30e996-37e8-4b97-a4bb-c77fd4051726",
  "sourceToolAssistantUUID": "0696ad34-d09a-4813-a915-6422f034058d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-28T05:30:15.181Z_

<details open><summary>🔧 Tool call — Read · `toolu_013XaQGmpd4anhH4e4SFXbF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tool-results/toolu_017A46LSHujVapbjhNGE7bvk.txt",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af30e996-37e8-4b97-a4bb-c77fd4051726",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR8grCw5S6UQNioNhoP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0ce6121-4e06-41c2-a642-8a06d8ee017e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFU8Ddn95ELvM1LkC6d53E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11524,
      "cache_read_input_tokens": 18464,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11524
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 18464,
          "cache_creation_input_tokens": 11524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11524,
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

_source line 37 · 2026-05-28T05:30:15.516Z_

<details><summary>↩ Tool result · `toolu_013XaQGmpd4anhH4e4SFXbF5`</summary>

```text
200	Step 1: Problem Generation. We prompted each generator with 1,000 seed problems from SAND-Math(Zhang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib34)) and tasked with producing five augmented variants per seed, resulting in 3,000 total generated problems per model.
201	
202	Step 2: Quality Assessment. We measured problem validity by prompting Qwen3-235B(Yang et al., [2025](https://arxiv.org/html/2509.24726v1#bib.bib31)) — selected for its state-of-the-art mathematical reasoning capability and its role as the teacher model in the distillation framework — to solve each generated problem under strict constraints: a 4,096-token limit and a 600-second timeout. The Validity Rate was defined as the percentage of problems successfully solved within these bounds.
203	
204	Step 3: Student Evaluation. We used all valid question-answer (QA) pairs to fine-tune the student model, DeepSeek-R1-Distill-Llama-8B(DeepSeek-AI et al., [2025a](https://arxiv.org/html/2509.24726v1#bib.bib9)). We evaluated Downstream Utility as the mean accuracy — average accuracy over 16 independent decoding runs per problem — across seven diverse mathematical reasoning benchmarks.
205	
206	#### 4.3.2 Problem Quality Assessment
207	
208	Table 4: Generator validity rates.
209	
210	Generator Model Validity Rate (%)
211	Qwen3-32B 89.1
212	Qwen3-235B-A22B 95.1
213	Gemini-2.5-Pro 94.2
214	GPT5-global 95.8
215	DeepSeek-v3.1-671B 96.5
216	Grok4 95.7
217	Claude-4.1-opus 96.9
218	Socratic-Generator-32B 95.6
219	
220	To evaluate the quality of the generated problems, we measure their Validity Rate — the percentage of problems solvable by a powerful model (Qwen3-235B-A22B-Instruct-2507). As shown in Table[4](https://arxiv.org/html/2509.24726v1#S4.T4 "Table 4 ‣ 4.3.2 Problem Quality Assessment ‣ 4.3 Generator Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), our specialized Socratic-Generator-32B generator achieves a remarkable 95.6% validity rate. This not only represents a substantial improvement over its base model Qwen3-32B but also rivals the performance of significantly larger models, including proprietary models like GPT5-0807-global, Gemini-2.5-Pro-06-17. This demonstrates our co-evolutionary strategy effectively.
221	
222	#### 4.3.3 Downstream Effectiveness
223	
224	Table[5](https://arxiv.org/html/2509.24726v1#S4.T5 "Table 5 ‣ 4.3.3 Downstream Effectiveness ‣ 4.3 Generator Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") reports the downstream utility of each generator, measured by the performance of the fine- student model. The output from our Socratic-Generator-32B leads to a final student accuracy of 37.72%. Notably, this performance not only rivals that achieved using data from significantly larger models but also marginally surpasses (+0.59 points) the result from its own Teacher (Qwen3-235B), despite being over 20x smaller.
225	
226	Table 5: Downstream Training Effectiveness with different generator models. Results are reported on seven benchmarks (AIME-24, AIME-25, AMC-23, GSM8K, MATH-500, Minerva, Olympiad) and their average. Values with arrows represent absolute point changes relative to Qwen3-32B baseline.
227	
228	Benchmark Datasets Avg.
229	AIME-24 AIME-25 AMC-23 GSM8K MATH-500 Minerva Olympiad
230	DeepSeek-R1-Distill-Llama-8B
231	+ Zero-shot 5.8 8.3 42.5 72.2 52.4 15.3 23.0 32.75
232	Open-Sourced Generators
233	Qwen3-32B 9.2 10.0 44.4 75.7 55.7 15.1 24.5 34.97
234	Qwen3-235B-A22B-Instruct-2507 12.5 12.5 47.5 76.1 57.8 16.4 23.6 37.13
235	DeepSeek-v3.1-671B 12.5 11.7 46.2 76.4 56.4 16.5 23.9 36.62
236	Advanced commercial Generators
237	Gemini-2.5-Pro-06-17 10.0 15.0 46.9 78.1 57.2 16.0 25.4 37.20
238	GPT5-0807-global 12.5 13.3 45.0 76.8 56.6 15.5 25.9 36.62
239	Grok-4 11.7 12.5 45.8 76.3 56.9 15.9 24.9 37.01
240	Claude-4.1-Opus 13.3 13.8 46.5 77.3 57.5 16.7 24.3 37.63
241	Socratic-Generator-32B 12.5 13.3 48.1 77.6 57.8 18.4 24.6 37.72
242	
243	### 4.4 Ablation Studies
244	
245	We conducted two key ablation studies to validate our framework’s design choices, with results summarized in Table[6](https://arxiv.org/html/2509.24726v1#S4.T6 "Table 6 ‣ 4.4 Ablation Studies ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"). The first study examines the necessity of initial supervised fine-tuning (SFT), while the second investigates different reward function formulations during reinforcement learning.
246	
247	Table 6: Ablation studies on the necessity of initial SFT and different strategies of reward functions. (a) Values with arrows represent absolute point changes relative to the previous stage within the same method. (b) Values with arrows represent absolute point changes relative to the Gaussian baseline. ρ\rho represents solver success rate, μ\mu represents target success rate, σ\sigma represents standard deviation in Gaussian reward function 𝒩​(μ,σ)\mathcal{N}(\mu,\sigma), Ψ ρ​(a,b)\Psi_{\rho}(a,b) represents linear function Ψ ρ​(a,b)=a​ρ+b\Psi_{\rho}(a,b)=a\rho+b.
248	
249	(a) Ablation Study on Initial SFT (AIME-24)
250	
251	Method Score (%)Δ\Delta (%)
252	Qwen3-8B-Base 9.64-
253	Socratic-Zero (w/o SFT)
254	+ Stage 1 11.67
255	+ Stage 2 11.15
256	+ Stage 3 11.98
257	Socratic-Zero (w/ SFT)
258	+ Stage 1 13.44
259	+ Stage 2 14.48
260	+ Stage 3 28.02
261	
262	(b) Ablation of Reward Functions (Benchmark Avg.)
263	
264	Reward Function Valid (%)Avg (%)Δ\Delta (%)
265	𝒩​(μ=0.5,σ=0.2)\mathcal{N}(\mu=0.5,\sigma=0.2) (Ours)89.9 35.72-
266	Ψ ρ​(a=0,b=1)\Psi_{\rho}(a=0,b=1)89.4 35.52
267	Ψ ρ​(a=1,b=0)\Psi_{\rho}(a=1,b=0)89.8 35.47
268	Ψ ρ​(a=−1,b=1)\Psi_{\rho}(a=-1,b=1)88.9 35.42
269	𝒩​(μ=0.3,σ=0.2)\mathcal{N}(\mu=0.3,\sigma=0.2)89.5 35.32
270	𝒩​(μ=0.4,σ=0.2)\mathcal{N}(\mu=0.4,\sigma=0.2)89.7 35.37
271	𝒩​(μ=0.6,σ=0.2)\mathcal{N}(\mu=0.6,\sigma=0.2)89.7 35.50
272	𝒩​(μ=0.7,σ=0.2)\mathcal{N}(\mu=0.7,\sigma=0.2)89.8 35.43
273	
274	##### Ablation on Initial SFT
275	
276	Table[6(a)](https://arxiv.org/html/2509.24726v1#S4.T6.st1 "In Table 6 ‣ 4.4 Ablation Studies ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") demonstrates the critical importance of initial supervised fine-tuning. Starting from the Qwen3-8B-Base model (9.64%), the version without SFT shows minimal improvements across all three training stages, reaching only 11.98% by Stage 3—a marginal gain of 2.34 percentage points. In stark contrast, the SFT-initialized model achieves substantial performance improvements, culminating in a remarkable 28.02% score at Stage 3, representing an 18.38 percentage point improvement over the base model. This 7.9× greater improvement highlights how SFT provides essential foundational capabilities that enable subsequent reinforcement learning stages to be dramatically more effective. The SFT phase likely equips the model with basic reasoning patterns and solution structures that serve as building blocks for more sophisticated reasoning developed during RL training.
277	
278	##### Ablation on Reward Functions
279	
280	Table[6(b)](https://arxiv.org/html/2509.24726v1#S4.T6.st2 "In Table 6 ‣ 4.4 Ablation Studies ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") compares various reward function formulations using benchmark average scores. Our Gaussian reward 𝒩​(μ=0.5,σ=0.2)\mathcal{N}(\mu=0.5,\sigma=0.2) achieves the best performance (35.72%) while maintaining high validity (89.9%). We evaluated linear functions Ψ ρ​(a,b)=a​ρ+b\Psi_{\rho}(a,b)=a\rho+b with different parameterizations, all of which underperformed our Gaussian approach by 0.20-0.30 percentage points. Similarly, varying the Gaussian mean parameter μ\mu from 0.3 to 0.7 consistently yielded inferior results, with the largest performance drop (0.40 points) occurring at μ=0.3\mu=0.3. This suggests that the Gaussian formulation with μ=0.5\mu=0.5 provides an optimal balance between exploration and exploitation during policy optimization, while the moderate variance (σ=0.2\sigma=0.2) allows sufficient reward signal differentiation without excessive noise that could destabilize training.
281	
282	5 Conclusion and Future Work
283	----------------------------
284	
285	In this paper, we introduced Socratic-Zero, a multi-agent co-evolutionary framework where Solver, Teacher, and Generator agents bootstrap autonomous mathematical reasoning from minimal seed data. Our implementation demonstrates that a carefully designed learning mechanism can achieve remarkable performance without relying on massive external datasets, offering a viable path for developing powerful reasoning systems in resource-constrained scenarios. Extensive experiments show that our framework not only achieves state-of-the-art results on mathematical benchmarks but also exhibits strong generalization capabilities across diverse problem types and difficulty levels. While the complex agent dynamics currently lack a formal convergence analysis, future work will aim to establish this theoretical foundation and extend the framework’s applicability to broader domains including scientific discovery, real-world decision making, and complex system modeling.
286	
287	References
288	----------
289	
290	*   Agarwal et al. (2024) Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos, Matthieu Geist, and Olivier Bachem. On-policy distillation of language models: Learning from self-generated mistakes. In _International Conference on Learning Representations_, 2024. 
291	*   Cao et al. (2025) Lang Cao, Chao Peng, Renhong Chen, Wu Ning, Yingtian Zou, and Yitong Li. Step guided reasoning: Improving mathematical reasoning using guidance generation and step reasoning, 2025. 
292	*   Chen et al. (2025a) Jiaqi Chen, Ruotian Ma, Bang Zhang, Peisong Wang, Zhaopeng Tu, Xiaolong Li, Kwan-Yee K. Wong, and Xiaodan Liang. Spc: Evolving self-play critic via adversarial games for llm reasoning, 2025a. 
293	*   Chen et al. (2024a) Yiming Chen, Zhenhua Liu, Xiang Yue, and Wenpeng Yin. Distillm: Towards streamlined distillation for large language models, 2024a. 
294	*   Chen et al. (2025b) Yue Chen, Minghua He, Fangkai Yang, Pu Zhao, Lu Wang, Yu Kang, Yifei Dong, Yuefeng Zhan, Hao Sun, Qingwei Lin, Saravan Rajmohan, and Dongmei Zhang. Warriormath: Enhancing the mathematical ability of large language models with a defect-aware framework, 2025b. 
295	*   Chen et al. (2024b) Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, and Quanquan Gu. Self-play fine-tuning converts weak language models to strong language models, 2024b. 
296	*   Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems, 2021. 
297	*   Comanici et al. (2025) Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities, 2025. 
298	*   DeepSeek-AI et al. (2025a) DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025a. 
299	*   DeepSeek-AI et al. (2025b) DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, et al. Deepseek-v3 technical report, 2025b. 
300	*   GLM et al. (2024) Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Dan Zhang, Diego Rojas, Guanyu Feng, Hanlin Zhao, et al. Chatglm: A family of large language models from glm-130b to glm-4 all tools, 2024. 
301	*   He et al. (2024) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024. 
302	*   Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset, 2021. 
303	*   Hu et al. (2021) Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models, 2021. 
304	*   Huang et al. (2025a) Chenghua Huang, Zhizhen Fan, Lu Wang, Fangkai Yang, Pu Zhao, Zeqi Lin, Qingwei Lin, Dongmei Zhang, Saravan Rajmohan, and Qi Zhang. Self-evolved reward learning for llms, 2025a. 
305	*   Huang et al. (2025b) Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, and Dong Yu. R-zero: Self-evolving reasoning llm from zero data, 2025b. 
306	*   Kazemi et al. (2025) Mehran Kazemi, Bahare Fatemi, Hritik Bansal, John Palowitch, Chrysovalantis Anastasiou, Sanket Vaibhav Mehta, Lalit K. Jain, Virginia Aglietti, Disha Jindal, Peter Chen, et al. Big-bench extra hard, 2025. 
307	*   Lee et al. (2024) Nicholas Lee, Thanakul Wattanawong, Sehoon Kim, Karttikeya Mangalam, Sheng Shen, Gopala Anumanchipalli, Michael W. Mahoney, Kurt Keutzer, and Amir Gholami. Llm2llm: Boosting llms with novel iterative data enhancement, 2024. 
308	*   Liu et al. (2025) Xuyang Liu, Zichen Wen, Shaobo Wang, Junjie Chen, Zhishan Tao, Yubo Wang, Xiangqi Jin, Chang Zou, Yiyu Wang, Chenfei Liao, Xu Zheng, Honggang Chen, Weijia Li, Xuming Hu, Conghui He, and Linfeng Zhang. Shifting ai efficiency from model-centric to data-centric compression, 2025. 
309	*   Luo et al. (2023) Haipeng Luo, Qingfeng Sun, Can Xu, Pu Zhao, Jianguang Lou, Chongyang Tao, Xiubo Geng, Qingwei Lin, Shifeng Chen, and Dongmei Zhang. Wizardmath: Empowering mathematical reasoning for large language models via reinforced evol-instruct. _arXiv preprint arXiv:2308.09583_, 2023. 
310	*   Madaan et al. (2023) Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-refine: Iterative refinement with self-feedback, 2023. 
311	*   Mukherjee et al. (2023) Subhabrata Mukherjee, Arindam Mitra, Ganesh Jawahar, Sahaj Agarwal, Hamid Palangi, and Ahmed Awadallah. Orca: Progressive learning from complex explanation traces of gpt-4, 2023. 
312	*   Mukherjee et al. (2025) Subhojyoti Mukherjee, Viet Dac Lai, Raghavendra Addanki, Ryan Rossi, Seunghyun Yoon, Trung Bui, Anup Rao, Jayakumar Subramanian, and Branislav Kveton. Learning to clarify by reinforcement learning through reward-weighted fine-tuning, 2025. 
313	*   Nagrani et al. (2025) Arsha Nagrani, Sachit Menon, Ahmet Iscen, Shyamal Buch, Ramin Mehran, Nilpa Jha, Anja Hauth, Yukun Zhu, Carl Vondrick, Mikhail Sirotenko, et al. Minerva: Evaluating complex video reasoning, 2025. 
314	*   Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model, 2023. 
315	*   Stiennon et al. (2020) Markus Stiennon, Long Ouyang, Jeff Wu, Rewon Child, David Amodei, Dario Amodei, David F.M. Brown, Benjamin Mann, Paul Christiano, Peter Chen, and John Schulman. Learning to follow instructions with human feedback, 2020. 
316	*   Team et al. (2025) P Team, Xinrun Du, Yifan Yao, Kaijing Ma, Bingli Wang, Tianyu Zheng, King Zhu, Minghao Liu, Yiming Liang, Xiaolong Jin, et al. Supergpqa: Scaling llm evaluation across 285 graduate disciplines, 2025. 
317	*   Wang et al. (2025a) Shaobo Wang, Yicun Yang, Zhiyuan Liu, Chenghao Sun, Xuming Hu, Conghui He, and Linfeng Zhang. Dataset distillation with neural characteristic function: A minmax perspective. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, pp. 25570–25580, June 2025a. 
318	*   Wang et al. (2024) Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark, 2024. 
319	*   Wang et al. (2025b) Zhiyuan Wang, Yuxiao Chen, Chao Yu, Yifan Zhang, and Jun Wang. A survey of reinforcement learning-driven knowledge distillation, 2025b. 
320	*   Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report, 2025. 
321	*   Yu et al. (2024) Longhui Yu, Weisen Jiang, Han Shi, Jincheng Yu, Zhengying Liu, Yu Zhang, James T. Kwok, Zhenguo Li, Adrian Weller, and Weiyang Liu. Metamath: Bootstrap your own mathematical questions for large language models, 2024. 
322	*   Zhan et al. (2025) Shaoxiong Zhan, Yanlin Lai, Ziyu Lu, Dahua Lin, Ziqing Yang, and Fei Tan. Mathsmith: Towards extremely hard mathematical reasoning by forging synthetic problems with a reinforced policy, 2025. 
323	*   Zhang et al. (2025) Yifan Zhang, Yifan Luo, Yang Yuan, and Andrew Chi-Chih Yao. Sand-math: Using llms to generate novel, difficult and useful mathematics questions and answers, 2025. 
324	*   Zhang et al. (2024) Yue Zhang, Tianxiang Sun, Xiangyang Liu, Hang Yan, and Xipeng Qiu. Dilm: Distilling dataset into language model for text-level dataset distillation, 2024. 
325	*   Zhao et al. (2025) Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, and Gao Huang. Absolute zero: Reinforced self-play reasoning with zero data, 2025. 
326	*   Zhao et al. (2023) Liang Zhao, Yuhui Shi, Zhiyong Feng, and Shuo Wang. Data distillation: A survey, 2023. 
327	
328	Appendix A Prompts
329	------------------
330	
331	### A.1 Solver Reasoning Prompt
332	
333	### A.2 Teacher Evaluation Prompt
334	
335	### A.3 Teacher Generation Prompt
336	
337	### A.4 Static Augmentation Baseline Prompts
338	
339	Appendix B Implementation Details
340	---------------------------------
341	
342	We conducted training experiments on 8×NVIDIA H20 GPUs with the following configuration: - GPU Memory: 96GB HBM3 per GPU - Total Training Memory: 768GB - Interconnect: NVLink 4.0 - Storage: High-speed NVMe SSD arrays for dataset caching - Network: InfiniBand for distributed training coordination
343	
344	The training infrastructure utilized mixed-precision training (FP16) with gradient checkpointing to optimize memory usage. We employed distributed training using PyTorch’s DistributedDataParallel with NCCL backend for efficient gradient synchronization across GPUs.
345	
346	### B.1 Training Hyperparameters
347	
348	We provide the complete hyperparameter settings for all components of the Socratic-Zero framework in Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
349	
350	Table 7: Hyperparameters used in Socratic-Zero framework.
351	
352	Component Parameter Value
353	Solver SFT Training Learning rate 5e-5
354	Per-device batch size 2
355	Gradient accumulation steps 4
356	Maximum sequence length 2048
357	LoRA rank (r r)64
358	LoRA alpha (α\alpha)128
359	LoRA dropout 0.1
360	Number of epochs 1
361	Solver DPO Training Learning rate 1e-6 – 5e-6
362	Per-device batch size 2
363	Gradient accumulation steps 4 – 16
364	Maximum sequence length 2048
365	Maximum training steps 10 – 200
366	DPO regularization (β\beta)0.05 – 0.2
367	Warmup steps 2 – 20
368	Optimizer AdaFactor
369	Weight decay 0.01
370	Maximum gradient norm 1.0
371	Generator Training Learning rate 1e-5
372	Per-device batch size 1
373	Gradient accumulation steps 8
374	Maximum sequence length 2048
375	LoRA rank (r r)64
376	LoRA alpha (α\alpha)128
377	Number of epochs 2
378	Curriculum Parameters Solutions per problem (k k)8
379	reward mean (μ\mu)0.5
380	reward std (σ\sigma)0.2
381	Historical replay ratio 25%
382	Evaluation Settings Sampling temperature 0.7
383	Number of samples 32
384	Token limit for validity check 4096
385	
386	Appendix C Curriculum Evolution Details
387	---------------------------------------
388	
389	This appendix provides a detailed description of the mechanisms for curriculum evolution, including the problem categorization and adaptive generation strategies that guide the learning process.
390	
391	### C.1 Problem Categorization by Solver Performance
392	
393	To effectively manage curriculum difficulty, we dynamically categorize each problem q∈𝒟 t q\in\mathcal{D}_{t} based on the current Solver’s performance. The Solver π θ 𝒮\pi_{\theta_{\mathcal{S}}} makes k k attempts {y 𝒮(i)}i=1 k\{y_{\mathcal{S}}^{(i)}\}_{i=1}^{k} on each problem. We then calculate the Solver’s success rate:
394	
395	s q≜1 k​∑i=1 k V​(q,y 𝒮(i)),s_{q}\triangleq\frac{1}{k}\sum_{i=1}^{k}V(q,y_{\mathcal{S}}^{(i)}),(8)
396	
397	where V V is the Teacher’s verification function. This metric allows us to partition the curriculum 𝒟 t\mathcal{D}_{t} into three distinct zones:
398	
399	1.   1.Mastered Zone (𝒟 mastered={q∣s q=1}\mathcal{D}_{\text{mastered}}=\{q\mid s_{q}=1\}): Problems the Solver consistently solves correctly. These problems form a solid foundation and are used as a basis for generating more challenging variants. 
400	2.   2.Learning Zone (𝒟 learning={q∣0<s q<1}\mathcal{D}_{\text{learning}}=\{q\mid 0<s_{q}<1\}): Problems the Solver can solve intermittently. This zone represents the optimal frontier for learning, where the Solver has emerging competence but requires further practice to achieve mastery. 
401	3.   3.Too Difficult Zone (𝒟 difficult={q∣s q=0}\mathcal{D}_{\text{difficult}}=\{q\mid s_{q}=0\}): Problems the Solver consistently fails to solve. These problems are temporarily set aside from the generation process to avoid creating tasks far beyond the Solver’s current capabilities. 
402	
403	### C.2 Zone-Adaptive Problem Generation
404	
405	New problems are strategically generated by the Teacher’s refinement function, G G, using problems from the Mastered and Learning zones. This ensures that curriculum expansion remains within the Solver’s zone of proximal development. The generation strategy is adapted to the source category:
406	
407	*   •From the Learning Zone: For a problem q∈𝒟 learning q\in\mathcal{D}_{\text{learning}}, the Teacher is prompted with a specific failed solution attempt, y fail y_{\text{fail}}. The new problem (q′,y ref′)=G​(q,y fail)(q^{\prime},y^{\prime}_{\text{ref}})=G(q,y_{\text{fail}}) is designed to target the specific reasoning error exhibited in y fail y_{\text{fail}}, thereby helping the Solver overcome its weaknesses. 
408	*   •From the Mastered Zone: For a problem q∈𝒟 mastered q\in\mathcal{D}_{\text{mastered}}, the Teacher is prompted with a successful solution, y succ y_{\text{succ}}. The new problem (q′,y ref′)=G​(q,y succ)(q^{\prime},y^{\prime}_{\text{ref}})=G(q,y_{\text{succ}}) is a more complex variant, designed to push the boundaries of the Solver’s established competence. 
409	
410	The set of newly generated problems 𝒟 new\mathcal{D}_{\text{new}} is thus composed of variants from both zones, creating a balanced and targeted curriculum expansion. Problems from 𝒟 difficult\mathcal{D}_{\text{difficult}} are explicitly excluded from this generation process to prevent counterproductive increases in difficulty.
411	
412	### C.3 Dynamic Recategorization of Problems
413	
414	As the Solver’s policy π θ 𝒮\pi_{\theta_{\mathcal{S}}} is updated at each iteration, its performance on existing problems changes. Consequently, all problems in the curriculum are periodically re-evaluated and recategorized. This dynamic process ensures the curriculum remains perfectly attuned to the Solver’s evolving skill set. The typical transitions between zones are:
415	
416	𝒟 difficult(t)\displaystyle\mathcal{D}_{\text{difficult}}^{(t)}→𝒟 learning(t+1)(as capability improves)\displaystyle\rightarrow\mathcal{D}_{\text{learning}}^{(t+1)}\quad\text{(as capability improves)}(9)
417	𝒟 learning(t)\displaystyle\mathcal{D}_{\text{learning}}^{(t)}→𝒟 mastered(t+1)(as skills are consolidated)\displaystyle\rightarrow\mathcal{D}_{\text{mastered}}^{(t+1)}\quad\text{(as skills are consolidated)}(10)
418	
419	This recategorization mechanism allows problems that were once too difficult to re-enter the active learning and generation pool once the Solver is ready, ensuring a continuous and adaptive learning trajectory.
420	
421	Appendix D Teacher Model Infrastructure
422	---------------------------------------
423	
424	The Teacher model (Qwen3-235B-A22B-Instruct-2507) requires substantial computational resources for curriculum generation and solution evaluation. We deployed the model using a distributed inference architecture to meet the throughput demands of the co-evolutionary training process.
425	
426	We distributed the Teacher model across 16 AMD MI308X GPUs, each equipped with 192GB HBM3 memory, providing a total of 3,072GB aggregate memory. This configuration enables concurrent processing of curriculum generation requests while maintaining inference consistency across the framework.
427	
428	To ensure system reliability and scalability, we implemented a multi-endpoint architecture with automatic load balancing and failover mechanisms. We configured the inference service with connection pooling (50 concurrent connections per endpoint) and exponential backoff retry policies to handle high request volumes during training.
429	
430	We optimized key performance parameters for the mathematical reasoning domain: request timeouts of 600 seconds accommodate complex problem generation, while a 4,096-token limit ensures efficient solution evaluation. Batch processing utilizes 32 concurrent workers to maximize throughput during curriculum evolution phases.
431	
432	Appendix E Teacher-Generated Problem Enhancement
433	------------------------------------------------
434	
435	We provide examples of how the Teacher model enhances problems based on Solver failures. The following demonstrates the progression from original problems to ly-targeted enhanced versions.
436	
437	### E.1 Example 1: Rational Inequality Enhancement
438	
439	Original Problem: 
440	
441	 Find all real numbers x x satisfying 2​x−5 x+3≥2\frac{2x-5}{x+3}\geq 2. (Give your answer in interval notation.)
442	
443	Enhanced Problem (Round 3): 
444	
445	 Find all real numbers x x satisfying 2​x−5 x 2−9+1 x+3≤4​x+1(x−3)2\frac{2x-5}{x^{2}-9}+\frac{1}{x+3}\leq\frac{4x+1}{(x-3)^{2}}. (Give your answer in interval notation.)
446	
447	Enhancement Analysis: The enhancement introduces multiple complexity factors: (1) factored denominators requiring domain analysis, (2) multiple rational terms requiring common denominators, (3) squared terms in denominators, and (4) more complex algebraic manipulation. The enhanced problem targets common student errors in rational inequality solving while maintaining the core mathematical concepts.
448	
449	### E.2 Example 2: Number Theory Enhancement
450	
451	Original Problem: 
452	
453	 Find the greatest common divisor of 10!+6 10!+6 and 11!+14 11!+14.
454	
455	Enhanced Problem: 
456	
457	 Find the greatest common divisor of 12!+8 12!+8 and 13!+26 13!+26, where the second number can be written as 13⋅12!+26 13\cdot 12!+26.
458	
459	Enhancement Analysis: The enhancement maintains the GCD structure while increasing numerical complexity and requiring students to recognize the relationship between consecutive factorials, targeting errors in modular arithmetic applications.
460	
461	Appendix F Seed Selection Protocol
462	----------------------------------
463	
464	The selection of initial seed problems is critical for establishing an effective curriculum foundation. We employed a systematic approach to ensure the seed set provides appropriate difficulty, comprehensive coverage, and sufficient diversity for subsequent curriculum evolution.
465	
466	##### Difficulty Alignment
467	
468	We selected seed problems to match the base model’s capability range to ensure productive learning dynamics. We drew problems from MATH dataset Levels 2-4, which empirically provide optimal challenge levels for our base models. Specifically, we excluded Level 1 problems (too easy, leading to trivial curriculum generation) and Level 5 problems (too difficult, resulting in universal failure and poor learning signals). Pre-filtering involved evaluating candidate problems with the base model using 8 solution attempts; we retained problems with success rates between 10-70% to ensure neither complete failure nor trivial success.
469	
470	##### Domain Coverage
471	
472	To ensure comprehensive mathematical reasoning development, we sampled seed problems across all seven MATH subject areas with balanced representation as shown in Table[8](https://arxiv.org/html/2509.24726v1#A6.T8 "Table 8 ‣ Domain Coverage ‣ Appendix F Seed Selection Protocol ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"):
473	
474	Table 8: Seed Problem Distribution Across Mathematical Domains
475	
476	Subject Area Count Representative Topics
477	Algebra 15 Linear/quadratic equations, inequalities, functions
478	Number Theory 15 Divisibility, modular arithmetic, prime factorization
479	Geometry 15 Coordinate geometry, trigonometry, area/volume calculations
480	Combinatorics 15 Counting principles, permutations, probability
481	Precalculus 15 Complex numbers, sequences, polynomial analysis
482	Intermediate Algebra 15 Advanced algebraic manipulation, systems
483	Prealgebra 10 Foundational arithmetic and basic algebraic concepts
484	Total 100 Comprehensive mathematical reasoning coverage
485	
486	This distribution ensures that curriculum evolution can target weaknesses across diverse mathematical domains rather than overfitting to specific problem types.
487	
488	##### Diversity Assurance
489	
490	Within each subject area, we selected problems to maximize methodological diversity. We employed clustering based on solution approach similarity (using embedding representations of problem statements) and selected problems from different clusters to ensure varied reasoning patterns. Additionally, we explicitly included problems requiring different mathematical tools to promote comprehensive skill development.
491	
492	##### Quality Control
493	
494	We subjected all candidate problems to rigorous quality verification through a multi-stage process:
495	
496	This systematic selection process ensures that the initial curriculum 𝒞 0\mathcal{C}_{0} provides a robust foundation for the co-evolutionary training dynamics while maintaining the diversity necessary for effective curriculum expansion.
497	
498	Appendix G Evaluation Protocol Details
499	--------------------------------------
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0ce6121-4e06-41c2-a642-8a06d8ee017e",
  "isSidechain": true,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "14eadb1b-738a-487b-a94c-998460f64610",
  "sourceToolAssistantUUID": "f0ce6121-4e06-41c2-a642-8a06d8ee017e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T05:30:21.368Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EU4GGKKKBn937KCJQNPLYh`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tool-results/toolu_017A46LSHujVapbjhNGE7bvk.txt",
  "offset": 499,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14eadb1b-738a-487b-a94c-998460f64610",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR9Sn9eFYr78Y7zAnmJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ffb94c7-b42e-494b-874e-c5772bf880ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTzx6MYjAc9p5R9G8efg5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10624,
      "cache_read_input_tokens": 29988,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 29988,
          "cache_creation_input_tokens": 10624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10624,
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

_source line 39 · 2026-05-28T05:30:21.383Z_

<details><summary>↩ Tool result · `toolu_01EU4GGKKKBn937KCJQNPLYh`</summary>

```text
499	--------------------------------------
500	
501	##### Mean@32 Sampling Strategy
502	
503	The Mean@32 evaluation metric represents the average accuracy across 32 independent solution attempts per problem. For each test problem, we generated 32 distinct solutions using temperature-based sampling (T=0.7) with top-p nucleus sampling (p=0.9) as specified in Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"). This approach provides robust performance estimates by capturing the model’s consistency and reliability across multiple attempts.
504	
505	We employed the sampling process using zero-shot prompting without few-shot examples to ensure unbiased evaluation. We generated each of the 32 solutions independently with different random seeds, preventing potential correlation effects. The final accuracy is computed as the proportion of correct solutions among the 32 attempts, providing a more stable performance measure than single-shot evaluation.
506	
507	##### MathRule Answer Extraction
508	
509	MathRule is a rule-based tool designed to extract and standardize final numerical answers from mathematical solution text. The tool employs pattern matching to identify answer indicators such as “Therefore,” “Thus,” “The answer is,” and LaTeX boxed expressions like \boxed​{}\backslash\text{boxed}\{\}.
510	
511	The extraction process involves: (1) Locating answer indicators within the solution text, (2) Parsing mathematical expressions using regex patterns for common formats (fractions, decimals, integers, algebraic expressions), (3) Standardizing representations (e.g., converting 1 2\frac{1}{2} to 0.5 when appropriate), (4) Handling multiple answer formats and selecting the most confident extraction based on contextual cues.
512	
513	MathRule achieves high precision in answer extraction while maintaining robustness to variations in solution formatting and mathematical notation styles.
514	
515	##### LLM Judge Configuration
516	
517	The Teacher model (Qwen3-235B-A22B-Instruct-2507) serves as an LLM judge for semantic validation when rule-based extraction is insufficient or ambiguous. The judge evaluates both numerical correctness and reasoning validity using structured prompts.
518	
519	We instructed the evaluation prompt to: (1) Verify the final numerical answer against the expected result, (2) Assess the logical coherence of the reasoning steps, (3) Identify any mathematical errors or invalid assumptions, (4) Provide binary correctness judgments with brief justification.
520	
521	We ensured judge reliability through temperature 0.1 sampling for consistent evaluations and validation against human expert annotations on a subset of problems. The dual-verification approach (MathRule + LLM judge) provides reliable automated assessment for large-scale evaluation.
522	
523	Appendix H Pseudo Code of Socratic-Zero
524	---------------------------------------
525	
526	The pseudo code of Socratic-Zero is provided in Algorithm[1](https://arxiv.org/html/2509.24726v1#alg1 "Algorithm 1 ‣ Appendix H Pseudo Code of Socratic-Zero ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
527	
528	Algorithm 1 Socratic-Zero Co-evolutionary Learning
529	
530	1:Require: Initial curriculum
531	
532	𝒟 0\mathcal{D}_{0}
533	, initial Solver parameters
534	
535	θ 𝒮(0)\theta_{\mathcal{S}}^{(0)}
536	, initial Generator parameters
537	
538	θ 𝒢(0)\theta_{\mathcal{G}}^{(0)}
539	, fixed Teacher
540	
541	𝒯​(V,G)\mathcal{T}(V,G)
542	, total iterations
543	
544	T T
545	, attempts per problem
546	
547	k k
548	.
549	
550	2:Initialize Solver
551	
552	π θ 𝒮←π θ 𝒮(0)\pi_{\theta_{\mathcal{S}}}\leftarrow\pi_{\theta_{\mathcal{S}}^{(0)}}
553	and Generator
554	
555	π θ 𝒢←π θ 𝒢(0)\pi_{\theta_{\mathcal{G}}}\leftarrow\pi_{\theta_{\mathcal{G}}^{(0)}}
556	.
557	
558	3:for
559	
560	t=0 t=0
561	to
562	
563	T−1 T-1
564	do
565	
566	4:
567	
568	⊳\triangleright
569	Phase 1: Online Solver Evolution
570	
571	5: Set reference policy
572	
573	π θ ref←π θ 𝒮(t)\pi_{\theta_{\text{ref}}}\leftarrow\pi_{\theta_{\mathcal{S}}^{(t)}}
574	.
575	
576	6: Initialize preference data
577	
578	𝒫 t←∅\mathcal{P}_{t}\leftarrow\emptyset
579	and failure set
580	
581	ℱ t←∅\mathcal{F}_{t}\leftarrow\emptyset
582	.
583	
584	7:for each problem
585	
586	q q
587	in curriculum
588	
589	𝒟 t\mathcal{D}_{t}
590	do
591	
592	8: Generate
593	
594	k k
595	solution attempts
596	
597	{y 𝒮(i)}i=1 k∼π θ 𝒮(t)(⋅∣q)\{y_{\mathcal{S}}^{(i)}\}_{i=1}^{k}\sim\pi_{\theta_{\mathcal{S}}^{(t)}}(\cdot\mid q)
598	.
599	
600	9: Construct winning set
601	
602	𝒴 w​(q)\mathcal{Y}_{w}(q)
603	and losing set
604	
605	𝒴 l​(q)\mathcal{Y}_{l}(q)
606	using Teacher verifier
607	
608	V V
609	.
610	
611	10: Collect preference pairs:
612	
613	𝒫 t←𝒫 t∪{(y w,y l)∣y w∈𝒴 w​(q),y l∈𝒴 l​(q)}\mathcal{P}_{t}\leftarrow\mathcal{P}_{t}\cup\{(y_{w},y_{l})\mid y_{w}\in\mathcal{Y}_{w}(q),y_{l}\in\mathcal{Y}_{l}(q)\}
614	.
615	
616	11: Collect failures:
617	
618	ℱ t←ℱ t∪{(q,y l)∣y l∈𝒴 l​(q)}\mathcal{F}_{t}\leftarrow\mathcal{F}_{t}\cup\{(q,y_{l})\mid y_{l}\in\mathcal{Y}_{l}(q)\}
619	.
620	
621	12:end for
622	
623	13: Update Solver parameters
624	
625	θ 𝒮(t+1)←Adam​(∇θ 𝒮 ℒ DPO​(θ 𝒮(t);𝒫 t,θ ref))\theta_{\mathcal{S}}^{(t+1)}\leftarrow\text{Adam}(\nabla_{\theta_{\mathcal{S}}}\mathcal{L}_{\text{DPO}}(\theta_{\mathcal{S}}^{(t)};\mathcal{P}_{t},\theta_{\text{ref}}))
626	.
627	
628	14:
629	
630	⊳\triangleright
631	Phase 2: Offline Generator Evolution & Curriculum Expansion
632	
633	15: Generate new problem-solution pairs with the Teacher:
634	
635	𝒟 new←{G​(q,y fail)∣(q,y fail)∈ℱ t}\mathcal{D}_{\text{new}}\leftarrow\{G(q,y_{\text{fail}})\mid(q,y_{\text{fail}})\in\mathcal{F}_{t}\}
636	.
637	
638	16: Construct Generator training data
639	
640	𝒟 𝒢←∅\mathcal{D}_{\mathcal{G}}\leftarrow\emptyset
641	.
642	
643	17:for each new problem
644	
645	(q′,y ref′)(q^{\prime},y^{\prime}_{\text{ref}})
646	generated from
647	
648	(q,y fail)(q,y_{\text{fail}})
649	do
650	
651	18: Estimate utility
652	
653	U​(q′|π θ 𝒮(t+1))U(q^{\prime}|\pi_{\theta_{\mathcal{S}}^{(t+1)}})
654	via rollouts with the updated Solver.
655	
656	19: Add weighted training example to dataset:
657	
658	𝒟 𝒢←𝒟 𝒢∪{(q,y fail,q′,U​(q′))}\mathcal{D}_{\mathcal{G}}\leftarrow\mathcal{D}_{\mathcal{G}}\cup\{(q,y_{\text{fail}},q^{\prime},U(q^{\prime}))\}
659	.
660	
661	20:end for
662	
663	21: Update Generator parameters
664	
665	θ 𝒢(t+1)←Adam​(∇θ 𝒢 ℒ WSFT​(θ 𝒢(t);𝒟 𝒢))\theta_{\mathcal{G}}^{(t+1)}\leftarrow\text{Adam}(\nabla_{\theta_{\mathcal{G}}}\mathcal{L}_{\text{WSFT}}(\theta_{\mathcal{G}}^{(t)};\mathcal{D}_{\mathcal{G}}))
666	.
667	
668	22:
669	
670	⊳\triangleright
671	Phase 3: Curriculum Update
672	
673	23: Augment the curriculum for the next iteration:
674	
675	𝒟 t+1←𝒟 t∪{(q′,y ref′)∣(q′,y ref′)∈𝒟 new}\mathcal{D}_{t+1}\leftarrow\mathcal{D}_{t}\cup\{(q^{\prime},y^{\prime}_{\text{ref}})\mid(q^{\prime},y^{\prime}_{\text{ref}})\in\mathcal{D}_{\text{new}}\}
676	.
677	
678	24:end for
679	
680	25:Output: Trained Solver policy
681	
682	π θ 𝒮(T)\pi_{\theta_{\mathcal{S}}^{(T)}}
683	and Generator policy
684	
685	π θ 𝒢(T)\pi_{\theta_{\mathcal{G}}^{(T)}}
686	.
687	
688	Appendix I Problem Quality Control Mechanism
689	--------------------------------------------
690	
691	To ensure curriculum integrity and prevent the propagation of erroneous problems, we implemented a comprehensive quality control mechanism that monitors problem validity through Solver performance feedback and automated verification.
692	
693	##### Teacher Self-Verification Protocol
694	
695	When the Teacher model evaluates Solver attempts and finds that all k=8 k=8 solutions for a given problem are incorrect (success rate j p=0 j_{p}=0), this triggers an automatic quality verification process. The system recognizes that universal failure may indicate either: (1) the problem exceeds current Solver capability (expected behavior), or (2) the problem itself or its reference solution contains errors (quality issue).
696	
697	The Teacher model performs self-verification by re-examining both the problem statement and its originally provided reference solution. This involves: (1) Re-solving the problem independently with temperature 0.1 for consistency, (2) Cross-validating the reference solution against the new solution attempt, (3) Checking for mathematical consistency, ambiguous problem statements, or computational errors, (4) Verifying that the problem has a unique, well-defined solution.
698	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ffb94c7-b42e-494b-874e-c5772bf880ed",
  "isSidechain": true,
  "promptId": "f32fafd0-7f3e-4a0c-9e02-af4d1d6593ae",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "90b30542-f77f-43b6-bffb-ec4e4748728d",
  "sourceToolAssistantUUID": "1ffb94c7-b42e-494b-874e-c5772bf880ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T05:30:24.759Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B68fybTgX1cm16TSYVWBYF`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tool-results/toolu_017A46LSHujVapbjhNGE7bvk.txt",
  "offset": 698,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90b30542-f77f-43b6-bffb-ec4e4748728d",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbUR9tG5qVUEp9wvMfT3r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "233daf23-bc86-43df-a018-7a07b0551ca2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122rfyFWPR3Z3F9PckioZ7P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3457,
      "cache_read_input_tokens": 40612,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 40612,
          "cache_creation_input_tokens": 3457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3457,
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

_source line 41 · 2026-05-28T05:30:24.764Z_

<details><summary>↩ Tool result · `toolu_01B68fybTgX1cm16TSYVWBYF`</summary>

```text
698	
699	##### Problem Filtering and Exclusion
700	
701	We immediately flagged and excluded problems that fail the self-verification process from further curriculum evolution. Specifically, we discarded problems if: (1) The Teacher cannot reproduce its own reference solution, (2) Multiple valid interpretations of the problem statement exist, (3) Computational errors are detected in the reference solution, (4) The problem lacks sufficient information for a unique solution.
702	
703	We removed discarded problems from the active curriculum 𝒞 t\mathcal{C}_{t} and they do not contribute to subsequent Solver training or Generator learning. This prevents the accumulation of low-quality problems that could degrade training effectiveness or introduce systematic biases.
704	
705	##### MathRule Integration for Contamination Minimization
706	
707	The integration of MathRule answer extraction serves as an additional quality control layer by providing objective, rule-based verification independent of LLM judgment. When MathRule successfully extracts a clear numerical answer from the Solver’s solution, this extraction is compared against the reference answer using standardized formats.
708	
709	This dual-verification approach (MathRule + Teacher evaluation) minimizes contamination from: (1) LLM judge inconsistencies or biases, (2) Format-related misinterpretations, (3) Numerical precision issues, (4) Ambiguous answer representations.
710	
711	Problems where MathRule and Teacher evaluations consistently disagree trigger additional quality review, as such disagreements often indicate underlying issues with problem clarity or reference solution accuracy.
712	
713	##### Feedback-Driven Quality Monitoring
714	
715	The system continuously monitors curriculum quality through Solver performance patterns. We flagged problems that consistently produce anomalous results—such as sudden performance drops across multiple Solver variants or inconsistent difficulty ratings—for manual review or automatic exclusion.
716	
717	This feedback-driven approach ensures that quality control adapts to emerging issues and maintains curriculum integrity throughout the co-evolutionary training process, preventing the accumulation of problematic content that could compromise learning effectiveness.
718	
719	Appendix J Curriculum Stability and Diversity Analysis
720	------------------------------------------------------
721	
722	We analyzed the curriculum evolution dynamics across two dimensions: difficulty progression and problem diversity preservation.
723	
724	##### Solver Performance Evolution
725	
726	Table[9](https://arxiv.org/html/2509.24726v1#A10.T9 "Table 9 ‣ Solver Performance Evolution ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") tracks the Solver’s mean reward (correctness rate) across training rounds, revealing adaptive curriculum difficulty.
727	
728	##### Solver Performance Evolution
729	
730	Table[9](https://arxiv.org/html/2509.24726v1#A10.T9 "Table 9 ‣ Solver Performance Evolution ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") tracks the Solver’s mean reward (correctness rate) across training stages, revealing adaptive curriculum difficulty.
731	
732	Table 9: Solver Mean Reward Evolution Across Training Stages
733	
734	Stage S1 S2 S3 Trend
735	Mean Reward (%)52.1 48.7 50.1↓\downarrow then ↑\uparrow
736	
737	The Solver exhibits characteristic performance decline from Stage 1 (52.1%) to Stage 2 (48.7%) followed by recovery in Stage 3 (50.1%) as shown in Table[9](https://arxiv.org/html/2509.24726v1#A10.T9 "Table 9 ‣ Solver Performance Evolution ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"). This pattern reflects adaptive curriculum generation where the Teacher progressively increases difficulty faster than Solver capability initially improves, then the Solver begins adapting to enhanced curriculum complexity.
738	
739	##### Generator Stability
740	
741	Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") examines reward distribution in Generator training.
742	
743	Table 10: Generator Reward Distribution Analysis
744	
745	Stage S1 S2 S3 Stability
746	High Reward Problems (%)50.7 49.4 50.2 Stable
747	Target Range (45-55%)✓✓✓Maintained
748	
749	As demonstrated in Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), the Generator maintains remarkable stability with high-reward problems consistently around 50%, fluctuating within only 1.3% range. This indicates successful learning of the optimal difficulty zone defined by the Gaussian reward function with parameters μ=0.5\mu=0.5 and σ=0.2\sigma=0.2 as specified in Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
750	
751	##### Generator Stability
752	
753	Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") examines reward distribution in Generator training.
754	
755	As demonstrated in Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), the Generator maintains remarkable stability with high-reward problems consistently around 50%, fluctuating within only 1.3% range. This indicates successful learning of the optimal difficulty zone defined by the Gaussian reward function with parameters μ=0.5\mu=0.5 and σ=0.2\sigma=0.2 as specified in Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
756	
757	##### Problem Diversity
758	
759	Three key mechanisms ensure curriculum diversity throughout training:
760	
761	Multi-domain initialization: The 100 seed problems span all 7 MATH subjects (Algebra, Number Theory, Geometry, etc.) across difficulty levels 2-4 as detailed in Table[8](https://arxiv.org/html/2509.24726v1#A6.T8 "Table 8 ‣ Domain Coverage ‣ Appendix F Seed Selection Protocol ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), providing diverse starting points for curriculum evolution.
762	
763	High-temperature sampling: We employed temperature 0.8-0.9 sampling at three critical stages: (1) Solver trajectory generation during curriculum advancement, (2) Teacher error analysis for varied failure interpretation, and (3) Teacher problem generation for diverse enhancement strategies.
764	
765	Compounding diversity effects: Multi-domain seeds combined with stochastic sampling create diverse failure patterns, while high-temperature generation ensures varied problem formulations even from similar error patterns.
766	
767	Appendix K Generalizability of Problem Generation Capabilities
768	--------------------------------------------------------------
769	
770	A key question emerging from our work is whether the Generator’s learned problem creation abilities can transfer to domains beyond mathematical reasoning. The value function and curriculum evolution mechanisms developed in Socratic-Zero are domain-agnostic in principle, suggesting potential for broader applicability.
771	
772	The Generator learns fundamental skills in difficulty calibration, error pattern recognition, and targeting that may generalize across reasoning domains. For instance, the ability to identify when a problem is “appropriately challenging” (around 50% success rate as shown in Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")) represents a meta-cognitive skill applicable to logical reasoning, scientific problem-solving, or even creative tasks. The Gaussian reward function with μ=0.5\mu=0.5 and σ=0.2\sigma=0.2 (Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")) creates a transferable framework for difficulty calibration that could adapt to other domains by adjusting the target success rate parameter.
773	
774	Our Generator’s superior performance compared to much larger models, achieving 37.72% downstream utility versus 37.13% from Qwen3-235B-A22B (Table[5](https://arxiv.org/html/2509.24726v1#S4.T5 "Table 5 ‣ 4.3.3 Downstream Effectiveness ‣ 4.3 Generator Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")), demonstrates that strategic specialization can outperform raw parameter scaling. This suggests that domain-specific Generator training could be effective across various reasoning domains without requiring massive computational resources.
775	
776	However, domain transfer would require careful adaptation of the Teacher’s evaluation capabilities and problem generation templates. Mathematical reasoning benefits from relatively objective correctness criteria with our dual-verification approach (MathRule + LLM judge) achieving 94.2% agreement with human experts, while other domains may require more nuanced evaluation frameworks. The seed selection protocol detailed in Table[8](https://arxiv.org/html/2509.24726v1#A6.T8 "Table 8 ‣ Domain Coverage ‣ Appendix F Seed Selection Protocol ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), which ensures balanced coverage across seven mathematical domains, provides a template for systematic domain expansion that could be adapted to physics, computer science, or other reasoning areas.
777	
778	Future work should investigate whether a Generator trained on mathematical problems can effectively create challenging problems in adjacent domains like physics or computer science, potentially through few-shot adaptation or domain-specific fine-tuning leveraging the value learning mechanisms demonstrated in our framework.
779	
780	Appendix L Framework Scalability and Extensibility
781	--------------------------------------------------
782	
783	The modular architecture of Socratic-Zero demonstrates strong potential for scalability and extension across multiple dimensions. The clear separation between Solver, Teacher, and Generator roles enables independent scaling and optimization of each component, as evidenced by our successful deployment across different computational configurations detailed in Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution").
784	
785	The framework’s extensibility is particularly evident in its ability to accommodate different model architectures and scales. Our cross-model validation demonstrates consistent performance improvements: Qwen3-8B achieves 56.1% average accuracy (+20.2 points), while similar gains are observed on GLM4-9B and Qwen3-14B architectures (Table[1](https://arxiv.org/html/2509.24726v1#S4.T1 "Table 1 ‣ Transfer to General Reasoning. ‣ 4.2 Solver Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")). This cross-architecture consistency suggests the co-evolutionary principles transcend specific model families and could readily incorporate emerging architectures or specialized reasoning models.
786	
787	The curriculum evolution mechanism shows robust scalability properties. Starting from just 100 seed problems (Table[8](https://arxiv.org/html/2509.24726v1#A6.T8 "Table 8 ‣ Domain Coverage ‣ Appendix F Seed Selection Protocol ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")), the system generates thousands of ly valuable problems while maintaining quality, with our Generator achieving 95.6% validity rate compared to 89.1% from the base Qwen3-32B model (Table[4](https://arxiv.org/html/2509.24726v1#S4.T4 "Table 4 ‣ 4.3.2 Problem Quality Assessment ‣ 4.3 Generator Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")). This demonstrates that the framework can scale curriculum generation without proportional increases in seed data requirements.
788	
789	Multi-domain extension represents another promising direction supported by our balanced seed distribution across seven mathematical domains. The current mathematical focus could expand to encompass multiple reasoning domains simultaneously, with domain-specific Teachers providing specialized curriculum generation while sharing the underlying co-evolutionary dynamics. The reward distribution analysis (Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")) shows stable performance across training rounds, indicating the framework’s robustness to curriculum expansion.
790	
791	The framework also supports hierarchical scaling, where multiple Solver-Generator pairs could operate at different difficulty levels or specialization areas, coordinated by higher-level meta-learning mechanisms. The oscillatory convergence patterns observed in Table[9](https://arxiv.org/html/2509.24726v1#A10.T9 "Table 9 ‣ Solver Performance Evolution ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") suggest natural synchronization points where multiple agents could coordinate their learning phases.
792	
793	Appendix M Convergence and Theoretical Foundations
794	--------------------------------------------------
795	
796	The theoretical understanding of multi-agent co-evolutionary learning remains an open challenge with significant implications for system reliability and predictability. Our empirical observations provide crucial insights into the convergence behavior of such systems.
797	
798	The oscillatory convergence patterns documented in Table[9](https://arxiv.org/html/2509.24726v1#A10.T9 "Table 9 ‣ Solver Performance Evolution ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution") reveal characteristic dynamics: Solver performance declines from R1 (60.12%) to R4 (48.7%) followed by recovery in R5 (50.1%). This pattern reflects adaptive curriculum generation where the Teacher progressively increases difficulty faster than Solver capability initially improves, then the Solver adapts to enhanced curriculum complexity. These bounded oscillations suggest the system reaches dynamic equilibria rather than static optima.
799	
800	Complementing this, the Generator maintains remarkable stability with high-reward problems consistently around 50%, fluctuating within only 1.3% range across training rounds (Table[10](https://arxiv.org/html/2509.24726v1#A10.T10 "Table 10 ‣ Generator Stability ‣ Appendix J Curriculum Stability and Diversity Analysis ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")). This stability indicates successful learning of the optimal difficulty zone defined by the Gaussian reward function with μ=0.5\mu=0.5 and σ=0.2\sigma=0.2 (Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")), providing empirical evidence for convergence to ly meaningful equilibria.
801	
802	The cross-architecture consistency observed in Table[1](https://arxiv.org/html/2509.24726v1#S4.T1 "Table 1 ‣ Transfer to General Reasoning. ‣ 4.2 Solver Results ‣ 4 Experiments ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"), where similar improvement patterns emerge across Qwen3-8B, GLM4-9B, and Qwen3-14B models, suggests robust system-level properties that transcend specific model architectures. This consistency provides evidence that the convergence behavior represents fundamental properties of the co-evolutionary dynamics rather than architecture-specific artifacts.
803	
804	Future theoretical work should investigate conditions under which the system exhibits stable convergence versus chaotic dynamics. Key questions include: What curriculum evolution rates ensure stable learning? How do different value functions affect convergence properties? Can we establish bounds on the oscillation amplitude around target performance levels observed in our empirical data?
805	
806	The intersection of curriculum learning, preference optimization, and multi-agent dynamics presents rich opportunities for theoretical development. The DPO training parameters (Table[7](https://arxiv.org/html/2509.24726v1#A2.T7 "Table 7 ‣ B.1 Training Hyperparameters ‣ Appendix B Implementation Details ‣ Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution")) and their interaction with curriculum evolution rates could inform theoretical models of multi-agent preference learning. Establishing convergence guarantees would enable more principled hyperparameter selection and provide confidence bounds for practical deployment.
807	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "233daf23-bc86-43df-a018-7a07b0551ca2",
  "isSidechain": true,
  "promptId": "f32fafd0-7f3e-4a0c-9e02-af4d1d6593ae",
  "agentId": "a67b76442fb946591",
  "type": "user",
  "uuid": "24b1a20e-a4a5-4240-ba6d-38abe0b81d82",
  "sourceToolAssistantUUID": "233daf23-bc86-43df-a018-7a07b0551ca2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-28T05:31:35.442Z_

I now have the complete paper content. Let me compile the comprehensive research report.

---

Here is the thorough analysis of the Socratic-Zero paper:

## Full Title and Authors

**Title:** Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution

**Arxiv ID:** 2509.24726 (submitted September 29, 2025; preprint, under review)

**Authors (with affiliations):**
- Shaobo Wang* (EPIC Lab, Shanghai Jiao Tong University) -- 2nd-year PhD candidate, also research intern at Alibaba Qwen Team
- Zhengbo Jiao* (Alibaba Group, EPIC Lab SJTU, Shanghai Univ. of Finance and Economics) -- *equal contribution
- Zifan Zhang (Alibaba Group, Wuhan University)
- Yilang Peng (Alibaba Group, Zhejiang University)
- Xu Ze (Alibaba Group)
- Boyu Yang (Alibaba Group)
- Wei Wang (Alibaba Group)
- Hu Wei (Alibaba Group) -- corresponding author
- Linfeng Zhang (EPIC Lab, Shanghai Jiao Tong University) -- corresponding author

---

## Exact Results/Numbers Claimed

**The +20.2pp claim:** The abstract states "Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods." However, looking at Table 1 closely, the actual average accuracy comparison is:

| Method | Avg Accuracy |
|---|---|
| Qwen3-8B + Zero-shot | 29.9% |
| + SFT | 35.9% |
| + Static Augmentation | 40.7% |
| + LLM2LLM Stage 3 | 40.9% |
| **+ Socratic Stage 3** | **56.1%** |

The gap from Static Augmentation is +15.4pp, and from LLM2LLM is +15.2pp. The +20.2pp figure appears to come from comparing against the SFT baseline (56.1 - 35.9 = 20.2), which is framed as improvement "over prior data synthesis methods" but is actually measured against the pre-augmentation SFT checkpoint, not the augmentation baselines themselves. This is a somewhat misleading framing -- the most defensible improvement over the strongest comparable baseline is **+15.2pp to +15.4pp**.

**Individual benchmark gains (Stage 3 vs Static Augmentation):**
- AMC: 63.7 vs 45.8 (+17.9)
- Minerva: 52.4 vs 41.9 (+10.5)
- MATH-500: 81.2 vs 62.7 (+18.5)
- GSM8K: 87.3 vs 74.6 (+12.7)
- Olympiad: 55.1 vs 35.9 (+19.2)
- AIME-25: 24.6 vs 11.4 (+13.2)
- AIME-24: 28.4 vs 12.3 (+16.1)

**Cross-architecture:** GLM4-9B reaches 52.3% avg; Qwen3-14B reaches 60.3% avg.

**Generator results:** Socratic-Generator-32B (a 32B model) achieves 37.72% downstream training effectiveness, marginally outperforming data from Claude-4.1-Opus (37.63%), Qwen3-235B (37.13%), GPT-5 (36.62%), Gemini-2.5-Pro (37.20%), Grok-4 (37.01%), DeepSeek-V3.1 (36.62%).

**General reasoning transfer:** +6.02pp average across BBEH, MMLU-Pro, SuperGPQA.

---

## How the Teacher Targets Weaknesses

The Teacher operates at the **error-instance level**, not at an error-type taxonomy level or concept level. Specifically:

1. **Verification function** `V(q, y) -> {0,1}`: Binary correctness judgment on each solution attempt.

2. **Problem refinement function** `G(q, y_fail) -> (q', y'_ref)`: The Teacher is prompted with a *specific failed solution attempt* and creates a new problem designed to target the *specific reasoning error exhibited in that failed attempt*.

3. **Zone-adaptive generation** based on scalar difficulty (success rate `s_q`):
   - **Mastered Zone** (s_q = 1): All attempts correct. Teacher generates harder variants from successful solutions.
   - **Learning Zone** (0 < s_q < 1): Partial success. Teacher is prompted with specific failed solutions and generates problems targeting those specific errors.
   - **Too Difficult Zone** (s_q = 0): All attempts fail. These problems are **excluded** from generation to prevent counterproductive difficulty escalation.

**Critically, the targeting is NOT:**
- Error-type-level (no taxonomy of error categories like "algebraic manipulation errors" vs "logic errors")
- Concept-level (no explicit identification of which mathematical concepts are weak)
- It IS instance-level: each failed solution is individually used as input to generate a new problem that targets that specific failure

The difficulty calibration uses a Gaussian utility function `U(q') = exp(-(s_q' - 0.5)^2 / (2 * 0.2^2))` centered at 50% success rate, which provides a scalar difficulty signal but not a structured error taxonomy.

---

## The Co-Evolution Mechanism

Three phases per iteration:

**Phase 1 -- Solver Evolution (Online Preference Learning):**
- Solver generates k=8 solution attempts per problem
- Teacher verifies each (binary correct/incorrect)
- Solutions partitioned into winning set and losing set
- If Solver produces zero correct solutions, the reference solution serves as the winning example
- Solver trained via **DPO (Direct Preference Optimization)** loss on preference pairs

**Phase 2 -- Generator Evolution (Offline Value-Weighted Distillation):**
- Failed solution attempts collected
- Teacher generates new problems from failures via `G(q, y_fail)`
- Each new problem scored by utility function (Gaussian centered at 50% Solver success rate)
- Generator trained via **weighted SFT (WSFT)** to mimic Teacher's problem refinement, weighted by utility scores
- This teaches the Generator to produce problems at the optimal difficulty frontier

**Phase 3 -- Curriculum Expansion:**
- New Teacher-generated problems added to curriculum
- All existing problems recategorized (Mastered/Learning/Too Difficult) based on updated Solver
- Problems dynamically transition between zones as Solver improves

The system runs for 3 stages total. Initial SFT on 1,500 Level-5 MATH problems is required before the co-evolution loop begins (ablation shows only +2.34pp without SFT vs +18.38pp with SFT).

---

## Whether It Uses a PRM or Verifier

**No PRM (Process Reward Model) is used.** The system uses:

1. **MathRule** -- a rule-based tool that extracts and standardizes final numerical answers using pattern matching (looking for "Therefore," "The answer is," boxed expressions, etc.)

2. **LLM Judge** -- the Teacher model (Qwen3-235B-A22B) performs semantic validation at temperature 0.1

This is a **dual outcome-level verification** approach (binary correct/incorrect on final answers), not step-level process supervision. There is no process reward model evaluating intermediate reasoning steps. The verification function is `V(q, y) -> {0, 1}` -- purely binary outcome.

---

## Key Limitations Compared to a PRM-Based Error Taxonomy Approach

**Limitations explicitly stated in the paper:**

1. **No formal convergence analysis** -- the authors acknowledge this gap and defer it to future work

2. **Domain restriction** -- currently only mathematical reasoning; adaptation to other domains would "require careful adaptation of the Teacher's evaluation capabilities and problem generation templates"

3. **Heavy computational requirements** -- 8x NVIDIA H20 GPUs for Solver + 16x AMD MI308X GPUs (3,072GB total) for Teacher inference

4. **Fixed Teacher dependency** -- relies on Qwen3-235B-A22B as a static oracle; no mechanism for the Teacher itself to improve

5. **Not truly "data-free"** -- requires 100 curated seed problems with 10-70% success rate + 1,500 problems for initial SFT

6. **Critical SFT dependency** -- without initial SFT, the system barely works (+2.34pp vs +18.38pp)

**Implicit limitations particularly relevant vs a PRM-based error taxonomy approach:**

7. **No structured error diagnosis** -- The Teacher generates new problems from individual failed solutions but never builds a taxonomy of error types. A PRM-based approach could identify *classes* of errors (e.g., "sign errors in algebraic manipulation," "incorrect application of modular arithmetic") and systematically target each category. Socratic-Zero's instance-level targeting may miss systematic error patterns.

8. **No step-level feedback** -- With only binary outcome verification, the system cannot pinpoint *where* in a reasoning chain the error occurs. A PRM provides step-level reward signals that identify the exact step where reasoning goes wrong. This means Socratic-Zero's DPO training treats entire solutions as good/bad without localizing errors.

9. **No error pattern aggregation** -- Because there is no taxonomy, the system cannot measure whether the Solver has systematic weaknesses in specific reasoning skills. It relies on the Teacher's implicit (prompt-based) analysis of individual failures rather than explicit statistical tracking of error categories.

10. **Quality control relies on Teacher self-verification** -- this creates a closed loop where systematic Teacher errors could propagate. A PRM trained on diverse annotations would provide an independent quality signal.

11. **Difficulty is scalar, not multidimensional** -- The Gaussian utility function targets a single number (50% success rate). It cannot distinguish between a problem that is hard because of novel concepts vs one that is hard because of computational complexity. A PRM-based taxonomy could target specific skill dimensions independently.

12. **Generator distills Teacher behavior, not error structure** -- The Generator learns to mimic *how* the Teacher creates problems from failures but does not learn a structured representation of error types that could enable more principled curriculum design.

---

Sources:
- [Socratic-Zero on arXiv (abstract)](https://arxiv.org/abs/2509.24726)
- [Socratic-Zero full HTML paper](https://arxiv.org/html/2509.24726)
- [Socratic-Zero PDF](https://arxiv.org/pdf/2509.24726)
- [Socratic-Zero on OpenReview](https://openreview.net/forum?id=I1garriWB7)
- [Socratic-Zero on HuggingFace Papers](https://huggingface.co/papers/2509.24726)
- [Socratic-Zero Literature Review (Moonlight)](https://www.themoonlight.io/en/review/socratic-zero-bootstrapping-reasoning-via-data-free-agent-co-evolution)
- [Shaobo Wang's homepage](https://gszfwsb.github.io/)
- [Semantic Scholar entry](https://www.semanticscholar.org/paper/Socratic-Zero-:-Bootstrapping-Reasoning-via-Agent-Wang-Jiao/08d60a8f1169eb65c120b67a1b6b8a8c448f9913)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24b1a20e-a4a5-4240-ba6d-38abe0b81d82",
  "isSidechain": true,
  "agentId": "a67b76442fb946591",
  "requestId": "req_011CbURA8d2SLRob6nQ9Fn71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19e9e7a6-31f8-4483-94ea-d26b6fc3c271",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5UmyhXUuanuo7eyeU1TBQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4803,
      "cache_read_input_tokens": 44069,
      "output_tokens": 2801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2801,
          "cache_read_input_tokens": 44069,
          "cache_creation_input_tokens": 4803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4803,
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
