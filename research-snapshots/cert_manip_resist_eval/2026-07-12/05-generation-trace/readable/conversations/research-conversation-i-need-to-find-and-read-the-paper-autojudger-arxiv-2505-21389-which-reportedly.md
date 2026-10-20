# Research conversation: I need to find and read the paper "AutoJudger" (arXiv 2505.21389) which reportedly uses IRT for adaptive multimodal benc

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7acfb706113e525c.jsonl`
- **Structured JSON:** [`7cff3862e361a2fad816.json`](../../sessions/7c/7cff3862e361a2fad816.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-27T23:54:51.294Z_

I need to find and read the paper "AutoJudger" (arXiv 2505.21389) which reportedly uses IRT for adaptive multimodal benchmark evaluation. 

1. Search for this paper using web search with queries like "AutoJudger IRT adaptive multimodal benchmark arXiv 2505.21389", "AutoJudger adaptive evaluation item response theory"
2. Fetch and read the actual paper or its abstract page to understand:
   - What exactly does AutoJudger do?
   - How does it use IRT?
   - Is it multimodal?
   - Does it generate new items or just calibrate existing ones?
   - How does it relate to adaptive testing for LLMs/VLMs?
3. Also search for any other very recent (2025-2026) papers combining IRT with multimodal evaluation that might be relevant.

Report back with detailed findings including paper title, authors, key contributions, and how it differs from (or overlaps with) a system that combines programmatic generation + IRT calibration + frontier tracking for multimodal math.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "77109c78-6734-4a81-89e6-9caa95f1ac17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T23:54:51.298Z_

```json
{
  "parentUuid": "77109c78-6734-4a81-89e6-9caa95f1ac17",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
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
  "uuid": "55bcc376-9ed1-4aa4-aa49-502d1c0d20ff",
  "timestamp": "2026-05-27T23:54:51.298Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T23:54:51.298Z_

```json
{
  "parentUuid": "55bcc376-9ed1-4aa4-aa49-502d1c0d20ff",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0225d143-5a9d-4175-802d-db0fa633b490",
  "timestamp": "2026-05-27T23:54:51.298Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T23:54:53.747Z_



I'll search for the AutoJudger paper and related work. Let me start with multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0225d143-5a9d-4175-802d-db0fa633b490",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTya16ygpQaqXFH8ox9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbb21736-99a2-4c1e-97ce-6557df20a4c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdXaGpeEBKTg71PyP42gTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8999,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8999,
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

_source line 5 · 2026-05-27T23:54:54.289Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CHDA8BdAnQfPQk1RWecc3A`</summary>

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
  "parentUuid": "cbb21736-99a2-4c1e-97ce-6557df20a4c3",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTya16ygpQaqXFH8ox9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c67847b6-27f8-4eac-8e28-b5cd6449fb37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdXaGpeEBKTg71PyP42gTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8999,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8999,
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

### Tool result

_source line 6 · 2026-05-27T23:54:54.293Z_

<details><summary>↩ Tool result · `toolu_01CHDA8BdAnQfPQk1RWecc3A`</summary>

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
  "parentUuid": "c67847b6-27f8-4eac-8e28-b5cd6449fb37",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "5aaa930b-7ded-463c-87f0-33697feb6740",
  "sourceToolAssistantUUID": "c67847b6-27f8-4eac-8e28-b5cd6449fb37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T23:54:57.456Z_



Now let me run multiple searches in parallel to find the AutoJudger paper and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aaa930b-7ded-463c-87f0-33697feb6740",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyaEgo28zEHyYQTd85w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d84d9cc7-0254-45b8-879b-6e3dbb0c5d21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnJ8KTA9Mzq7Rntt8Ga5Vf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-27T23:54:57.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012SAPYz8pkAdHhzGDP5V4CV`</summary>

```json
{
  "query": "AutoJudger IRT adaptive multimodal benchmark arXiv 2505.21389"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d84d9cc7-0254-45b8-879b-6e3dbb0c5d21",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyaEgo28zEHyYQTd85w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f605e14f-a690-471e-a34c-edae1f171a60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnJ8KTA9Mzq7Rntt8Ga5Vf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 8999,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 8999,
          "cache_creation_input_tokens": 1126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-27T23:55:04.437Z_

<details><summary>↩ Tool result · `toolu_012SAPYz8pkAdHhzGDP5V4CV`</summary>

```text
Web search results for query: "AutoJudger IRT adaptive multimodal benchmark arXiv 2505.21389"

Links: [{"title":"[2505.21389] AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs","url":"https://arxiv.org/abs/2505.21389"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs","url":"https://arxiv.org/pdf/2505.21389"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs","url":"https://paperreading.club/page?id=310496"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs {cutout}0-1.5cm0cm1","url":"https://arxiv.org/html/2505.21389v1"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs | OpenReview","url":"https://openreview.net/forum?id=ueh4YWLX4n"},{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory","url":"https://arxiv.org/pdf/2603.02663"},{"title":"AdaptMMBench: Benchmarking Adaptive Multimodal Reasoning for Mode Selection and Reasoning Process","url":"https://arxiv.org/pdf/2602.02676"}]

Based on the search results, here's what I found about the paper:

## AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs

AutoJudger is an agent-driven framework for efficient and adaptive benchmarking of MLLMs that tackles the escalating cost of evaluation.

**Key Components:**

AutoJudger employs the Item Response Theory (IRT) to estimate the question difficulty and an autonomous evaluation agent to dynamically select the most informative test questions based on the model's real-time performance.

AutoJudger incorporates two pivotal components: a semantic-aware retrieval mechanism to ensure that selected questions cover diverse and challenging scenarios across both vision and language modalities, and a dynamic memory that maintains contextual statistics of previously evaluated questions to guide coherent and globally informed question selection throughout the evaluation process.

**Performance Results:**

AutoJudger uses only 4% of the data to achieve over 90% ranking accuracy with the full benchmark evaluation on MMT-Bench.

The paper was submitted to arXiv on May 27, 2025, and the authors are from Fudan University, Shanghai, China, and the University of Southern California.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f605e14f-a690-471e-a34c-edae1f171a60",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "826490a4-8bb5-4411-8ce2-11ce378c11b5",
  "sourceToolAssistantUUID": "f605e14f-a690-471e-a34c-edae1f171a60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T23:55:06.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VuxjmR1ETnrsTnNqCquYb3`</summary>

```json
{
  "query": "AutoJudger adaptive evaluation item response theory multimodal LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "826490a4-8bb5-4411-8ce2-11ce378c11b5",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyayGP7tpysxPyaGsgB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0ba255e-adc7-4201-b278-45def7948195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvXABdxu6wL3sLuCF8popb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 10125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 11 · 2026-05-27T23:55:07.480Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0157Z5vFsHc2P4z4hMYM6zLo`</summary>

```json
{
  "query": "IRT item response theory multimodal evaluation LLM VLM benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0ba255e-adc7-4201-b278-45def7948195",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyayGP7tpysxPyaGsgB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc612427-9082-4e49-a209-cc96169818b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvXABdxu6wL3sLuCF8popb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 10125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 12 · 2026-05-27T23:55:14.375Z_

<details><summary>↩ Tool result · `toolu_01VuxjmR1ETnrsTnNqCquYb3`</summary>

```text
Web search results for query: "AutoJudger adaptive evaluation item response theory multimodal LLM 2025"

Links: [{"title":"[2505.21389] AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs","url":"https://arxiv.org/abs/2505.21389"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs | OpenReview","url":"https://openreview.net/forum?id=ueh4YWLX4n"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs","url":"https://paperreading.club/page?id=310496"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs","url":"https://arxiv.org/pdf/2505.21389"},{"title":"AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs {cutout}0-1.5cm0cm1","url":"https://arxiv.org/html/2505.21389v1"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://www.arxiv.org/pdf/2602.00521"},{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory","url":"https://arxiv.org/html/2603.02663v1"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/html/2602.00521"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"}]

Based on the search results, here's what I found about AutoJudger:

## Overview

AutoJudger is an agent-driven framework for efficient and adaptive benchmarking of MLLMs (multimodal large language models).

## Key Components

AutoJudger employs the Item Response Theory (IRT) to estimate the question difficulty and an autonomous evaluation agent to dynamically select the most informative test questions based on the model's real-time performance.

Specifically, AutoJudger incorporates two pivotal components: a semantic-aware retrieval mechanism to ensure that selected questions cover diverse and challenging scenarios across both vision and language modalities, and a dynamic memory that maintains contextual statistics of previously evaluated questions to guide coherent and globally informed question selection throughout the evaluation process.

## Performance

AutoJudger uses only 4% of the data to achieve over 90% ranking accuracy with the full benchmark evaluation on MMT-Bench. The framework was designed to address the challenge that evaluating multimodal large language models (MLLMs) is increasingly expensive, as the growing size and cross-modality complexity of benchmarks demand significant scoring efforts.

The research was recently published on May 27, 2025, with authors including Xuanwen Ding and collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0ba255e-adc7-4201-b278-45def7948195",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "abdd90eb-f666-48fa-995e-e3bedc486b24",
  "sourceToolAssistantUUID": "a0ba255e-adc7-4201-b278-45def7948195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T23:55:14.488Z_

<details><summary>↩ Tool result · `toolu_0157Z5vFsHc2P4z4hMYM6zLo`</summary>

```text
Web search results for query: "IRT item response theory multimodal evaluation LLM VLM benchmark 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/5af32a3eb819a4ead9222e437104d91a206b5e95.pdf"},{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory","url":"https://arxiv.org/html/2603.02663v1"},{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory | OpenReview","url":"https://openreview.net/forum?id=jMbyMp5DCh"},{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory","url":"https://arxiv.org/pdf/2603.02663"},{"title":"Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length","url":"https://arxiv.org/html/2512.07019v1"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"}]

Based on the search results, I found several recent papers on using Item Response Theory (IRT) for evaluating Large Language Models and Vision-Language Models:

## Key Findings:

**M3IRT Framework (2026)**: A multi-modal and multidimensional item response theory framework (M3IRT) has been introduced that extends classical IRT by decomposing both model ability and item difficulty into image-only, text-only, and cross-modal components. Current benchmarks are filled with shortcut questions, which can be solved using only single modality, and thereby yielding unreliable rankings. M3IRT prioritizes genuinely cross-modal questions over shortcuts and preserves ranking fidelity even when 50% of items are artificially generated low-quality questions, thereby reducing evaluation cost while improving reliability.

**VLM Evaluation Studies**: Recent research collected responses from 24 VLMs, including the GPT-4.1 series, Gemini-2.0 series, and Claude-3.7 series, as well as open-source models such as Qwen-2.5-vl, Llama-3.2, and Pixtral.

**General IRT Framework for LLMs**: Item Response Theory (IRT), together with Computerized Adaptive Testing (CAT), from the psychometrics literature has emerged as a promising framework for evaluating LLMs in a more principled and interpretable manner.

**Benchmark Quality Analysis (2026)**: One analysis examined 11 LLM benchmarks comprising 41,871 items, revealing significant shortcomings in their measurement quality, and demonstrated that leveraging IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc612427-9082-4e49-a209-cc96169818b7",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "d31490dd-7abd-4a94-8bc4-93c373d348b1",
  "sourceToolAssistantUUID": "dc612427-9082-4e49-a209-cc96169818b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T23:55:16.734Z_

Good, I'm finding excellent results. Now let me fetch the actual paper pages for detailed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d31490dd-7abd-4a94-8bc4-93c373d348b1",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTybiFGfxNCPVnJnCyxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c51293-2a65-4785-add1-a042d86dc82a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Gu3FNKLDWKsBvAALYXEAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 10887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1668,
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

_source line 15 · 2026-05-27T23:55:19.147Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EZ3HyTURRvVA3dbTx64hA9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21389",
  "prompt": "Extract the full abstract, all author names, the paper title, and any key details about the methodology (IRT usage, adaptive testing, multimodal aspects, item generation vs calibration). Also extract submission date and any institutional affiliations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c51293-2a65-4785-add1-a042d86dc82a",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTybiFGfxNCPVnJnCyxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29945d0f-6e4f-4153-97cc-35802f727368",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Gu3FNKLDWKsBvAALYXEAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 10887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1668,
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

_source line 16 · 2026-05-27T23:55:22.777Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AK6Ae3vqprMTC1ncYjFkvV`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.21389v1",
  "prompt": "Extract detailed information about: 1) How exactly IRT is used (which IRT model - 1PL, 2PL, 3PL? what parameters are estimated?), 2) The adaptive testing algorithm (how questions are selected), 3) Whether the system generates new items or only selects from existing ones, 4) What benchmarks it was tested on, 5) The key experimental results, 6) How it handles multimodal aspects specifically, 7) The semantic-aware retrieval mechanism, 8) The dynamic memory component. Provide as much technical detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29945d0f-6e4f-4153-97cc-35802f727368",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTybiFGfxNCPVnJnCyxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9aa316d-df1c-4ca0-82ed-fc783873ec2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Gu3FNKLDWKsBvAALYXEAV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 10887,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 347,
          "cache_read_input_tokens": 10887,
          "cache_creation_input_tokens": 1668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1668,
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

_source line 17 · 2026-05-27T23:55:24.747Z_

<details><summary>↩ Tool result · `toolu_01EZ3HyTURRvVA3dbTx64hA9`</summary>

```text
# AutoJudger: Paper Details

**Title:** AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs

**Authors:** Xuanwen Ding, Chengjun Pan, Zejun Li, Jiwen Zhang, Siyuan Wang, Zhongyu Wei

**Submission Date:** May 27, 2025

**Abstract:**
The paper addresses expensive evaluation of multimodal large language models by introducing an adaptive benchmarking system. The framework employs "Item Response Theory (IRT) to estimate the question difficulty and an autonomous evaluation agent to dynamically select the most informative test questions based on the model's real-time performance." It incorporates semantic-aware retrieval to ensure diverse coverage across vision and language modalities, plus dynamic memory tracking previously evaluated questions. Results demonstrate that the method "uses only 4% of the data to achieve over 90% ranking accuracy with the full benchmark evaluation on MMT-Bench."

**Key Methodology Components:**
- **IRT Application:** Estimates question difficulty parameters for adaptive selection
- **Adaptive Testing:** Dynamically chooses questions based on real-time model performance
- **Multimodal Coverage:** Semantic-aware retrieval ensures diversity across vision and language dimensions
- **Memory System:** Maintains contextual statistics from prior evaluations to guide coherent question selection

**Institutional Affiliation:** Not explicitly stated in the provided content
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29945d0f-6e4f-4153-97cc-35802f727368",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "4bee2d2d-ced2-4182-b94a-67713f58ca6a",
  "sourceToolAssistantUUID": "29945d0f-6e4f-4153-97cc-35802f727368",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T23:55:36.036Z_

<details><summary>↩ Tool result · `toolu_01AK6Ae3vqprMTC1ncYjFkvV`</summary>

```text
# AutoJudger: Technical Deep Dive

## 1) IRT Model Specification

AutoJudger employs the **one-parameter logistic IRT model (Rasch model)**, not 2PL or 3PL variants. The core equation is:

> "p(rij is correct) = 1/(1+exp(-(aj-di)))"

where **aj** represents model ability and **di** represents question difficulty. The framework estimates question difficulties offline using a Bayesian variational approach with maximum likelihood estimation, then keeps these fixed during evaluation while dynamically updating model ability estimates.

## 2) Adaptive Testing Algorithm

The selection process involves four sequential steps:

**Difficulty Filtering**: Questions are filtered to maintain success probability between 0.2-0.8 based on current model ability and question difficulty estimates.

**Semantic Diversity**: A max-min retrieval strategy selects the top-5 candidates with maximum Euclidean distance from previously attempted questions, ensuring semantic coverage.

**Agent-Based Selection**: An MLLM agent analyzes the 5 candidates considering memory, ability estimates, and question semantics, selecting the most appropriate question.

**Memory Update**: The system maintains a dynamic memory table tracking statistics by semantic category.

## 3) Item Generation vs. Selection

The system **exclusively selects from existing questions**—it performs no generation. It operates on fixed benchmarks and creates subsets through intelligent selection.

## 4) Benchmark Evaluation

Testing occurred on four benchmarks:
- **MMMU-Dev Val** (expert-level reasoning, 11,500 questions)
- **SEEDBench-Image** (19K+ questions across 12 dimensions)
- **MMT-Bench-Val** (31K+ questions spanning 32 meta-tasks)
- **AI2D-Test** (diagram-based reasoning, 5,000+ diagrams)

## 5) Key Experimental Results

AutoJudger achieved remarkable compression efficiency:

> "AutoJudger achieves 92% rank consistency using only 4% of the data (125 samples)" on MMT-Bench.

Performance at 5% compression ratio (Table 1):
- AI2D: 94.85% ranking accuracy
- MMMU: 87.94% accuracy
- MMT-Bench: 92.06% accuracy
- SEEDBench: 90.74% accuracy

The method demonstrated superior stability (lower variance) compared to random, stratified, and cluster-based sampling baselines.

## 6) Multimodal Handling

The framework leverages multimodal capabilities in three ways:

**Semantic Encoding**: Uses CLIP ViT-B/32 to generate embeddings from both images and text for initial clustering and diversity measurement.

**Agent Understanding**: The judging agent (Qwen2.5-VL-7B) analyzes full question-image pairs, not just text, enabling informed recommendations based on visual content.

**Visual Information Necessity**: Ablation studies showed removing visual information degraded performance, confirming multimodal understanding's importance.

## 7) Semantic-Aware Retrieval Mechanism

The retrieval module operates in two phases:

**Initialization**: K-means clustering (k=10) on semantic embeddings partitions the entire benchmark, selecting diverse questions from each cluster to construct an initial representative set.

**Iterative Retrieval**: For each iteration, questions are filtered by difficulty appropriateness, then the max-min strategy identifies the five candidates exhibiting maximum minimum distance to previously selected questions, explicitly balancing difficulty alignment with semantic novelty.

## 8) Dynamic Memory Component

The memory maintains categorical statistics organized as markdown tables:

> "For each category, the memory tracks statistics including the number of questions, max/min/average difficulty, and overall accuracy."

This enables the agent to identify underrepresented domains and balance selection across topics. Ablation studies revealed memory removal caused the system to favor questions matching current ability too closely, reducing semantic diversity from 0.86 to 0.78 average distance. Memory essentially prevents mode collapse in question selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9aa316d-df1c-4ca0-82ed-fc783873ec2e",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "8601cfa0-f2bc-46e2-baa0-d3e166289311",
  "sourceToolAssistantUUID": "a9aa316d-df1c-4ca0-82ed-fc783873ec2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-27T23:55:39.185Z_

Excellent, very detailed information on AutoJudger. Now let me fetch the related M3IRT paper and search for more recent related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8601cfa0-f2bc-46e2-baa0-d3e166289311",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTydJN9D6zWudkDq5PzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d942c700-bedc-4a54-84b8-f1297898a0dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrMBgveHgBkSeVEpddrHkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 12555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 20 · 2026-05-27T23:55:42.950Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015cA7FgmRz66hV1QbKJjeHe`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.02663v1",
  "prompt": "Extract the paper title, authors, abstract, and key methodology details. Specifically: 1) What is M3IRT? 2) How does it decompose ability and difficulty into modality-specific components? 3) How does it handle shortcut questions? 4) What benchmarks is it tested on? 5) Key results including the claim about preserving ranking fidelity with 50% low-quality items. 6) Does it generate new items or calibrate existing ones? 7) How does it differ from standard IRT approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d942c700-bedc-4a54-84b8-f1297898a0dd",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTydJN9D6zWudkDq5PzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e18c42a9-d662-4eeb-ba39-ebf5d15be775",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrMBgveHgBkSeVEpddrHkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 12555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 21 · 2026-05-27T23:55:43.366Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RxMqbwcHYXKRWsiXSGKz5R`</summary>

```json
{
  "query": "computerized adaptive testing LLM evaluation IRT programmatic item generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e18c42a9-d662-4eeb-ba39-ebf5d15be775",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTydJN9D6zWudkDq5PzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ca78a3a-3b34-441e-9977-334e642f8e73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrMBgveHgBkSeVEpddrHkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 12555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 22 · 2026-05-27T23:55:50.909Z_

<details><summary>↩ Tool result · `toolu_01RxMqbwcHYXKRWsiXSGKz5R`</summary>

```text
Web search results for query: "computerized adaptive testing LLM evaluation IRT programmatic item generation 2025 2026"

Links: [{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | OpenReview","url":"https://openreview.net/forum?id=iX39LhePyd"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"[2511.04689] Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/abs/2511.04689"},{"title":"[2603.23506] Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/abs/2603.23506"},{"title":"[2601.13885] Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/abs/2601.13885"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/pdf/2601.13885"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"ADAPTIVE TESTING FOR LLM EVALUATION: A","url":"https://arxiv.org/pdf/2511.04689"}]

Based on the search results, here's what I found regarding computerized adaptive testing (CAT), LLM evaluation, IRT, and programmatic item generation in 2025-2026:

## Recent Developments in IRT-Based Adaptive Testing for LLMs

ATLAS is an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information–guided item selection. ATLAS reduces the number of required items by up to 90% while maintaining measurement precision.

A computerized adaptive testing (CAT) framework grounded in item response theory (IRT) has been proposed for efficient assessment of standardized medical knowledge in LLMs. This approach comprises a two-phase design: a Monte Carlo simulation to identify optimal CAT configurations and an empirical evaluation of 38 LLMs using a human-calibrated medical item bank.

## Extensions to Continuous Scoring

While CAT has proven effective for multiple-choice benchmarks, modern LLM evaluation increasingly relies on generation tasks with continuous scores, with IRT-based adaptive testing extended to continuous bounded scores by replacing the Bernoulli response distribution with a heteroskedastic normal distribution. This method uses 2% of the items while improving ranking correlation by 0.12 τ over random sampling.

## Calibration and Item Banks

ATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters. The research shows that ATLAS uses a substantially larger and more diverse pool of 3,000+ LMs for calibration.

These recent developments (from late 2025 through early 2026) demonstrate an active research area in applying psychometric principles to make LLM evaluation more efficient and cost-effective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ca78a3a-3b34-441e-9977-334e642f8e73",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "4fd8ca6e-f7d9-43ef-a80b-e7d09ffff670",
  "sourceToolAssistantUUID": "1ca78a3a-3b34-441e-9977-334e642f8e73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T23:55:51.114Z_

<details><summary>↩ Tool result · `toolu_015cA7FgmRz66hV1QbKJjeHe`</summary>

```text
# Paper Summary: Evaluating Cross-Modal Reasoning with M3IRT

**Title:** "Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory"

**Authors:** Uebayashi, Masui, Atarashi, Bao, Kashima, Inoue, Otani, Takeuchi (Kyoto University, CyberAgent, The Institute of Statistical Mathematics, Tohoku University)

## What is M3IRT?

M3IRT (Multimodal Multi-dimensional Item Response Theory) extends classical IRT by explicitly modeling modality-specific and cross-modal components. The framework treats vision-language models as test subjects and benchmark questions as assessment items, enabling quantification of genuinely cross-modal reasoning demands.

## Decomposition Strategy

The approach decomposes both model ability and item difficulty into four components:

- **Base ability/difficulty:** foundational reasoning capability
- **Image-only:** visual processing capacity
- **Text-only:** linguistic comprehension capacity  
- **Cross-modal:** information integration across modalities

As the paper states: "decomposing both model ability and item difficulty into image-only, text-only, and cross-modal components" enables distinguishing truly multimodal questions from single-modality shortcuts.

## Handling Shortcut Questions

M3IRT identifies "shortcut questions" (solvable using only one modality) by estimating cross-modal difficulty parameters. The framework prioritizes items requiring both modalities, filtering out questions answerable from isolated image or text presentation.

## Benchmark Testing

Experiments span three major VLM benchmarks:
- **MMMU** (900 validation questions)
- **MathVista** (1,000 test-min questions)
- **SEED-Bench** (1,000 questions from L1/L2 sets)

Testing involved 24 vision-language models including GPT-4, Gemini, Claude, and open-source alternatives.

## Key Results

The framework "nearly reconstructs the original ranking using only a 10% subset across all datasets" while maintaining ranking fidelity even with 50% artificially introduced low-quality questions. It also reduces low-quality question proportions to "less than half that of existing methods."

## Item Generation vs. Calibration

M3IRT **calibrates existing items** rather than generating new ones. It estimates parameters from observed response patterns without requiring ground-truth labels, treating the task as a parameter estimation problem similar to tensor completion.

## Differentiation from Standard IRT

Standard IRT uses single latent ability and difficulty parameters. M3IRT's key innovation is the modality-aware decomposition enabling explicit measurement of whether model performance reflects genuine cross-modal reasoning or exploitation of single-modality shortcuts—a distinction classical IRT cannot capture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e18c42a9-d662-4eeb-ba39-ebf5d15be775",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "f54cb629-d6ca-4d8b-99ca-d49151ecb995",
  "sourceToolAssistantUUID": "e18c42a9-d662-4eeb-ba39-ebf5d15be775",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T23:56:00.445Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S1diH9z7LgCQBYDT5svHx2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.04689",
  "prompt": "Extract the paper title, authors, abstract, key methodology details about ATLAS. Specifically: 1) How does it use IRT (which model)? 2) Does it generate new items? 3) How does adaptive testing work in ATLAS? 4) What benchmarks? 5) Key results? 6) Is it multimodal?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f54cb629-d6ca-4d8b-99ca-d49151ecb995",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyeQqbghUnEPdFCWRby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a372715-23dd-4cfd-a345-9267d25674be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVzCc3FbPY57HUMqEj8KR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 829,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 14202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1052,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 25 · 2026-05-27T23:56:01.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ZrffnqJ2NDLsShvw9yH6W`</summary>

```json
{
  "query": "IRT programmatic question generation benchmark contamination multimodal math vision 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a372715-23dd-4cfd-a345-9267d25674be",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyeQqbghUnEPdFCWRby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1956d009-4e3c-43fa-ac54-362674c0af59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVzCc3FbPY57HUMqEj8KR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 829,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 14202,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1052
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 829,
          "output_tokens": 212,
          "cache_read_input_tokens": 14202,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1052,
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

_source line 26 · 2026-05-27T23:56:05.426Z_

<details><summary>↩ Tool result · `toolu_01S1diH9z7LgCQBYDT5svHx2`</summary>

```text
# ATLAS: Adaptive Testing for LLM Evaluation

**Paper Title:** "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"

**Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla

## Key Details

**IRT Implementation:**
The paper employs Item Response Theory with "Fisher information-guided item selection" to estimate model ability. The specific IRT model type is not detailed in the abstract.

**Item Generation:**
ATLAS does not generate new items. Instead, it works with "calibrated item banks" from existing benchmarks, using psychometric principles to select strategically from available test materials.

**Adaptive Testing Mechanism:**
The system dynamically selects test items based on Fisher information—a statistical measure indicating which questions provide the most discriminative power for the current ability estimate. This focuses evaluation on maximally informative items rather than administering all available questions.

**Benchmarks Evaluated:**
The paper tested on five benchmarks, with specific mention of HellaSwag (5,600 items).

**Key Results:**
ATLAS "reduces the number of required items by up to 90% while maintaining measurement precision." For example, it matched whole-bank estimates using only 41 HellaSwag items with 0.157 mean absolute error.

**Multimodal Capability:**
The abstract does not indicate multimodal functionality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a372715-23dd-4cfd-a345-9267d25674be",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "dd7226c1-a680-4479-9394-82b017babdbd",
  "sourceToolAssistantUUID": "9a372715-23dd-4cfd-a345-9267d25674be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T23:56:07.952Z_

<details><summary>↩ Tool result · `toolu_014ZrffnqJ2NDLsShvw9yH6W`</summary>

```text
Web search results for query: "IRT programmatic question generation benchmark contamination multimodal math vision 2025 2026"

Links: [{"title":"Benchmarking Multimodal Mathematical Reasoning with Explicit Visual Dependency","url":"https://arxiv.org/html/2504.18589v2"},{"title":"Measuring Multimodal Mathematical Reasoning with the MATH-Vision Dataset","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ad0edc7d5fa1a783f063646968b7315b-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"Automated Generation of Challenging Multiple-Choice Questions for Vision Language Model Evaluation","url":"https://arxiv.org/html/2501.03225v1"},{"title":"MV-MATH: Evaluating Multimodal Math Reasoning in Multi-Visual Contexts","url":"https://arxiv.org/pdf/2502.20808"},{"title":"Evaluating Visual Mathematics in Multimodal LLMs: A Multilingual Benchmark Based on the Kangaroo Tests","url":"https://arxiv.org/pdf/2506.07418"},{"title":"Reasoning Multimodal Large Language Model: Data Contamination and Dynamic Evaluation","url":"https://arxiv.org/pdf/2506.07202"},{"title":"Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM","url":"https://arxiv.org/pdf/2411.03823"}]

Based on the search results, I found several relevant research papers addressing topics related to your query:

## Key Findings:

**Data Contamination & Dynamic Evaluation:**
A recent study addresses concerns about data contamination in Multimodal Large Language Models, proposing a dynamic evaluation framework to assess MLLM generalization beyond static benchmarks. Instead of perturbing inputs, the framework perturbs the task itself, evaluating models across a family of tasks to probe diverse capabilities and reveal whether performance is robust or reliant on superficial task-specific cues.

**Multimodal Detection Framework:**
Research on MM-Detect shows that it is effective and sensitive in identifying varying degrees of contamination in multimodal benchmarks.

**Vision-Language Math Benchmarks:**
VCBench is a comprehensive benchmark for multimodal mathematical reasoning with explicit visual dependencies, comprising 1,720 question-answer pairs and 6,697 images. MathVista is the first multimodal dataset aimed at assessing MLLMs' mathematical reasoning for visual math QA tasks, while MATH-Vision targets multimodal mathematical understanding with questions from mathematics competitions.

**Recent 2025 Developments:**
A 2025 paper analyzes MLLMs for mathematical problem-solving in visually presented mathematics across multiple languages, assessing models including GPT-4o, Pixtral, Qwen-VL, and Gemini 2.0 Flash.

These results highlight ongoing research into programmatic question generation, benchmark contamination detection, and multimodal mathematical evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1956d009-4e3c-43fa-ac54-362674c0af59",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "9da9a749-5ce8-42b5-b7a4-4f81ee0149c7",
  "sourceToolAssistantUUID": "1956d009-4e3c-43fa-ac54-362674c0af59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T23:56:11.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JjXdypNjMycq2jNYhKiZit`</summary>

```json
{
  "query": "\"adaptive benchmark\" \"item generation\" \"frontier tracking\" LLM VLM IRT calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9da9a749-5ce8-42b5-b7a4-4f81ee0149c7",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyfeySAvinor85ddcBN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ce9ec3f-faca-40d1-88e1-f31517527552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsQYC6m7hP6Zd3wJdVaMvy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2172,
      "cache_read_input_tokens": 15254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 29 · 2026-05-27T23:56:12.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01767rijRabrUR25GeQK2rCz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.13885",
  "prompt": "Extract the paper title, authors, abstract, and key methodology. Does this paper generate new items or select from existing ones? Does it handle multimodal evaluation? How does it extend IRT?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce9ec3f-faca-40d1-88e1-f31517527552",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyfeySAvinor85ddcBN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f98b4c2b-c4af-46e2-9f77-b8d5b039db87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsQYC6m7hP6Zd3wJdVaMvy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2172,
      "cache_read_input_tokens": 15254,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 15254,
          "cache_creation_input_tokens": 2172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2172,
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

_source line 30 · 2026-05-27T23:56:17.293Z_

<details><summary>↩ Tool result · `toolu_01767rijRabrUR25GeQK2rCz`</summary>

```text
# Paper Analysis: Confident Rankings with Fewer Items

## Title, Authors & Abstract
**Title:** "Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores"

**Authors:** Esma Balkır, Alice Pernthaller, Marco Basaldella, José Hernández-Orallo, Nigel Collier

**Abstract Summary:** The work addresses efficient LLM evaluation by extending Computerized Adaptive Testing (CAT) to handle continuous scoring metrics. It "achieves reliable model ranking while testing as few items and as cheaply as possible," using only 2% of test items while improving ranking correlation.

## Item Selection vs. Generation
This paper **selects from existing items** rather than generating new ones. It implements an adaptive testing approach that strategically chooses which evaluation items to administer from an existing benchmark pool.

## Multimodal Evaluation
**No multimodal evaluation is addressed.** The scope covers text-based evaluation metrics: "n-gram-based, embedding-based, and LLM-as-judge metrics."

## IRT Extension
The methodology extends Item Response Theory by "replacing the Bernoulli response distribution with a heteroskedastic normal distribution" to accommodate continuous bounded scores (ROUGE, BLEU, LLM-as-Judge outputs) instead of traditional binary correct/incorrect responses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f98b4c2b-c4af-46e2-9f77-b8d5b039db87",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "ed68a7e8-cafb-45ff-a4b3-24ac576ceaae",
  "sourceToolAssistantUUID": "f98b4c2b-c4af-46e2-9f77-b8d5b039db87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T23:56:17.972Z_

<details><summary>↩ Tool result · `toolu_01JjXdypNjMycq2jNYhKiZit`</summary>

```text
Web search results for query: ""adaptive benchmark" "item generation" "frontier tracking" LLM VLM IRT calibration 2025 2026"

Links: [{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/pdf/2601.13885"},{"title":"LLM Evaluation in 2026. Frontier models now saturate the… | by Milind Nair | Mar, 2026 | Medium","url":"https://medium.com/@nairmilind3/llm-evaluation-in-2026-e631a78c67dc"},{"title":"Aligning Language Model Benchmarks with Pairwise Preferences","url":"https://arxiv.org/html/2602.02898v1"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Published as a conference paper at ICLR 2025 ME TABENCH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"Benchmarking at the Edge of Comprehension","url":"https://arxiv.org/pdf/2602.14307"}]

I found several relevant research papers and articles on adaptive benchmarking for LLMs and VLMs. Here's what the search results show:

## Key Recent Work on Adaptive Benchmarking

Hofmann et al. (2025) introduce fluid benchmarking, which combines IRT with adaptive testing to dynamically select evaluation items matched to a model's capability.

A computerized adaptive testing (CAT) framework grounded in item response theory (IRT) has been proposed for efficient assessment of standardized medical knowledge in LLMs.

ATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability, terminating when precision thresholds are reached.

## Continuous Score Approaches

A continuous extension of IRT-based adaptive testing accommodates real-valued scores while preserving the mathematical structure of binary CAT by replacing the Bernoulli response distribution with a heteroskedastic normal distribution that maintains the same logistic mean function.

## Frontier Model Saturation and Evaluation Trends

As frontier models acquire stronger reasoning capabilities, benchmarks have struggled to keep up and are often criticized for being static, ambiguous in what they measure, and ephemeral, with the fact that benchmarks quickly saturate being the most concerning.

The search results show active development in adaptive benchmarking techniques during 2025-2026, particularly focusing on IRT calibration and dynamic item selection for more efficient LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ce9ec3f-faca-40d1-88e1-f31517527552",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "418360b2-a3bc-4145-8faf-3e82e9ede5de",
  "sourceToolAssistantUUID": "7ce9ec3f-faca-40d1-88e1-f31517527552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T23:56:23.675Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RZrvcycZnMkG1L8RnNasHg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.23506",
  "prompt": "Extract the paper title, authors, abstract. Does it handle multimodal evaluation? Does it generate items or select from existing ones? Key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418360b2-a3bc-4145-8faf-3e82e9ede5de",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTygPgT9P5JLxMWVdkE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c0358c3-9222-4c48-8a4d-fb5f75408029",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKkgCGyAFUFUC5NDCtNGWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 333,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 17426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 33 · 2026-05-27T23:56:24.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Q7dDY1cfoYtJsj18Mus9S`</summary>

```json
{
  "query": "dynamic benchmark generation multimodal math IRT difficulty calibration vision language model evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c0358c3-9222-4c48-8a4d-fb5f75408029",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTygPgT9P5JLxMWVdkE6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d84e54ec-e8b7-4f3a-884c-fc25ec9e1552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKkgCGyAFUFUC5NDCtNGWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 333,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 17426,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 333,
          "output_tokens": 168,
          "cache_read_input_tokens": 17426,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 957,
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

_source line 34 · 2026-05-27T23:56:27.934Z_

<details><summary>↩ Tool result · `toolu_01RZrvcycZnMkG1L8RnNasHg`</summary>

```text
# Paper Summary

**Title:** "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking"

**Authors:** Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng

**Abstract:** The research proposes an item response theory-based computerized adaptive testing framework to efficiently assess medical knowledge in LLMs. Rather than static benchmarks, the approach dynamically selects items and terminates upon reaching reliability thresholds, reducing evaluation time from hours to minutes while preserving performance rankings.

## Key Questions Addressed

**Multimodal Evaluation:** Not addressed. The paper focuses exclusively on text-based medical knowledge assessment.

**Item Generation vs. Selection:** The framework **selects from existing items**—specifically from a "human-calibrated medical item bank." It does not generate new test items.

**Key Results:**
- Adaptive testing achieved near-perfect correlation with full assessments (r = 0.988)
- Used only 1.3% of available items
- Reduced computational cost substantially while maintaining inter-model performance rankings across 38 evaluated LLMs
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c0358c3-9222-4c48-8a4d-fb5f75408029",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "e163aea1-e500-4fa6-94c8-5d9d836e13cc",
  "sourceToolAssistantUUID": "7c0358c3-9222-4c48-8a4d-fb5f75408029",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T23:56:31.322Z_

<details><summary>↩ Tool result · `toolu_017Q7dDY1cfoYtJsj18Mus9S`</summary>

```text
Web search results for query: "dynamic benchmark generation multimodal math IRT difficulty calibration vision language model evaluation 2025 2026"

Links: [{"title":"[2410.08695] Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping","url":"https://arxiv.org/abs/2410.08695"},{"title":"Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping","url":"https://arxiv.org/pdf/2410.08695"},{"title":"DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical   Reasoning Robustness of Vision Language Models","url":"https://arxiv.org/pdf/2411.00836"},{"title":"Benchmarking Multimodal Mathematical Reasoning with Explicit Visual Dependency","url":"https://arxiv.org/pdf/2504.18589"},{"title":"KBE-DME: Dynamic Multimodal Evaluation via Knowledge Enhanced Benchmark Evolution","url":"https://arxiv.org/pdf/2510.21182"},{"title":"[2411.00836] DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models","url":"https://arxiv.org/abs/2411.00836"}]

I found several highly relevant research papers on dynamic benchmark generation for multimodal math evaluation of vision-language models. Here are the key findings:

## Dynamic Benchmark Generation for Multimodal Math Evaluation

Vision-Language Bootstrapping (VLB) dynamically generates new visual question-answering samples through multimodal bootstrapping that modifies both images and language, offering dynamic variants of existing benchmarks with diverse complexities to enable evaluation that co-evolves with LVLMs.

DynaMath is a dynamic visual math benchmark designed to fill the gap where traditional benchmarks contain only static sets of problems and cannot easily evaluate mathematical reasoning robustness of VLMs.

## Knowledge-Enhanced Dynamic Evaluation

KBE-DME (Dynamic Multimodal Evaluation via Knowledge-Enhanced Benchmark Evolution) addresses data contamination and data saturation by modeling VQA problems using a Graph formulation with multimodal knowledge triplets and identifying key triplets necessary for answering questions.

## Key Challenges Addressed

Current static benchmarks maintain fixed complexity constraints and overlap with pre-training data, resulting in data contamination issues. These approaches enable difficulty-controllable evaluation by adjusting the degree of question exploration.

The research from 2024-2025 demonstrates a clear trend toward dynamic, difficulty-calibrated evaluation methods that address data contamination concerns in multimodal math reasoning assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d84e54ec-e8b7-4f3a-884c-fc25ec9e1552",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "221d8149-7db9-4fe0-833a-68a7b676856c",
  "sourceToolAssistantUUID": "d84e54ec-e8b7-4f3a-884c-fc25ec9e1552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-27T23:56:34.708Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LyxDiJBPGg1XiSygQvBr1r`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.00836",
  "prompt": "Extract the paper title, authors, abstract. How does DynaMath generate new items? Does it use IRT? How does it handle difficulty calibration? Key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221d8149-7db9-4fe0-833a-68a7b676856c",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyhNvqd77Dsaeh1z1UM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177a4ec7-5cd4-4417-8c8f-772ec8ec6c31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3HG4PxSJCaGJgK8RQzUTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1442,
      "cache_read_input_tokens": 18383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1442,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 37 · 2026-05-27T23:56:35.648Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VxmGYEk85aWT9VZJVSwteW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.08695",
  "prompt": "Extract the paper title, authors, abstract. How does VLB generate new items? Does it use IRT? How does it handle difficulty calibration? Is it specifically for math? Key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "177a4ec7-5cd4-4417-8c8f-772ec8ec6c31",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyhNvqd77Dsaeh1z1UM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae77d92c-81e0-4fd2-95d1-0852a72edc20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3HG4PxSJCaGJgK8RQzUTg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1442,
      "cache_read_input_tokens": 18383,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 18383,
          "cache_creation_input_tokens": 1442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1442,
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

_source line 38 · 2026-05-27T23:56:39.793Z_

<details><summary>↩ Tool result · `toolu_01LyxDiJBPGg1XiSygQvBr1r`</summary>

```text
# DynaMath Paper Summary

**Title:** DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models

**Authors:** Chengke Zou, Xingang Guo, Rui Yang, Junyu Zhang, Bin Hu, Huan Zhang

**Abstract:** The paper addresses how state-of-the-art Vision-Language Models (VLMs) fail when applying solution steps to similar problems with minor variations. DynaMath is introduced as "a dynamic visual math benchmark designed for in-depth assessment of VLMs" to evaluate generalization under varying input conditions.

## Generation Method

DynaMath generates new items through a Python-based approach. The benchmark contains "501 high-quality, multi-topic seed questions, each represented as a Python program." These programs "are carefully designed and annotated to enable the automatic generation of a much larger set of concrete questions, including many different types of visual and textual variations."

## IRT and Difficulty Calibration

The provided content does not mention Item Response Theory (IRT) or discuss difficulty calibration mechanisms.

## Key Results

Evaluation of 14 state-of-the-art VLMs using 5,010 generated questions revealed a significant gap: "the worst-case model accuracy...is significantly lower than the average-case accuracy." This demonstrates that VLMs lack robustness in mathematical reasoning when facing problem variants.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177a4ec7-5cd4-4417-8c8f-772ec8ec6c31",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "56c986a7-c3e1-4ef9-87f3-014a857cbaec",
  "sourceToolAssistantUUID": "177a4ec7-5cd4-4417-8c8f-772ec8ec6c31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-27T23:56:40.642Z_

<details><summary>↩ Tool result · `toolu_01VxmGYEk85aWT9VZJVSwteW`</summary>

```text
# Paper Analysis

**Title:** "Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping"

**Authors:** Yue Yang, Shuibai Zhang, Wenqi Shao, Kaipeng Zhang, Yi Bin, Yu Wang, Ping Luo

**Abstract Summary:**
The paper addresses static evaluation benchmarks for Large Vision-Language Models (LVLMs) by introducing VLB, which "dynamically generates new visual question-answering samples through a multimodal bootstrapping module that modifies both images and language."

## Key Questions Addressed:

**How does VLB generate new items?**
VLB uses a "multimodal bootstrapping module that modifies both images and language" while maintaining consistency through a judge module that ensures newly generated samples remain aligned with originals.

**Does it use IRT?**
No mention of Item Response Theory in the provided content.

**Difficulty calibration?**
The system offers "dynamic variants of existing benchmarks with diverse complexities," though specific calibration mechanisms aren't detailed in this excerpt.

**Math-specific?**
No—the paper evaluates "visual perception and reasoning" across multimodal tasks, tested on SEEDBench, MMBench, and MME benchmarks (general multimodal evaluation suites).

**Key Results:**
VLB "significantly reduces data contamination and exposes performance limitations of LVLMs" across multiple benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae77d92c-81e0-4fd2-95d1-0852a72edc20",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "f2a99e19-51c1-4203-9d80-6769028d111f",
  "sourceToolAssistantUUID": "ae77d92c-81e0-4fd2-95d1-0852a72edc20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T23:56:44.041Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Quvy3a81erfZbf65qCUqi8`</summary>

```json
{
  "query": "\"Lost in Benchmarks\" \"item response theory\" LLM rethinking 2505.15055"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a99e19-51c1-4203-9d80-6769028d111f",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyi4hzr2t49PrPvtygG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53921658-ca38-4b35-8152-41c91693b350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGXKq8pHJRgB32kYgcqcrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 19825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 927,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 41 · 2026-05-27T23:56:44.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GdhqpLsyV8mAGPeQsmE8RY`</summary>

```json
{
  "query": "Diagnosing reliability \"LLM-as-a-Judge\" item response theory 2602.00521"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53921658-ca38-4b35-8152-41c91693b350",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyi4hzr2t49PrPvtygG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "598c6d05-4197-4a89-82ef-b021c3eac350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGXKq8pHJRgB32kYgcqcrf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 19825,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 927
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 927,
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

_source line 42 · 2026-05-27T23:56:50.261Z_

<details><summary>↩ Tool result · `toolu_01Quvy3a81erfZbf65qCUqi8`</summary>

```text
Web search results for query: ""Lost in Benchmarks" "item response theory" LLM rethinking 2505.15055"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v1"}]

Based on the search results, here's what I found about the paper (arXiv:2505.15055):

## Paper Overview

The paper addresses concerns about LLM benchmark evaluation, noting inconsistencies between different leaderboards and poor separability among top models.

## Main Contribution

The authors propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. PSN-IRT is a novel framework integrating neural networks with Item Response Theory (IRT), a psychometric framework traditionally used in educational assessments.

## Key Findings

The authors conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Additionally, LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items.

## Practical Applications

The paper demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.

The paper was submitted to arXiv on May 21, 2025, and has since been accepted to the AAAI Conference on Artificial Intelligence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53921658-ca38-4b35-8152-41c91693b350",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "a03f560d-a5bc-4f66-987c-0c9d4808cab4",
  "sourceToolAssistantUUID": "53921658-ca38-4b35-8152-41c91693b350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-27T23:56:50.422Z_

<details><summary>↩ Tool result · `toolu_01GdhqpLsyV8mAGPeQsmE8RY`</summary>

```text
Web search results for query: "Diagnosing reliability "LLM-as-a-Judge" item response theory 2602.00521"

Links: [{"title":"[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/abs/2602.00521"},{"title":"Paper page - Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://huggingface.co/papers/2602.00521"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/html/2602.00521v1"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://www.arxiv.org/pdf/2602.00521"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/pdf/2412.12509"},{"title":"Diagnosing LLM Judge Reliability: Conformal Prediction Sets and Transitivity Violations","url":"https://arxiv.org/html/2604.15302"},{"title":"Are We on the Right Way to Assessing LLM-as-a-Judge?","url":"https://arxiv.org/pdf/2512.16041"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item ...","url":"https://www.researchgate.net/publication/400369489_Diagnosing_the_Reliability_of_LLM-as-a-Judge_via_Item_Response_Theory"},{"title":"Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges","url":"https://arxiv.org/pdf/2601.20913"}]

Based on the search results, I found the paper you're looking for:

The paper introduces a two-phase diagnostic framework for assessing reliability of LLM-as-a-Judge, grounded in Item Response Theory (IRT). 

While LLM-as-a-Judge is widely used in automated evaluation, existing validation practices primarily operate at the level of observed outputs, offering limited insight into whether LLM judges themselves function as stable and reliable measurement instruments.

The framework adopts Graded Response Model (GRM) of IRT and formalizes reliability along two complementary dimensions: (1) intrinsic consistency, defined as the stability of measurement behavior under prompt variations, and (2) human alignment, capturing correspondence with human preferences.

These signals provide practical guidance for verifying reliability of LLM-as-a-Judge and identifying potential causes of unreliability.

The paper was submitted on January 31, 2026 to arXiv. You can access the full paper at https://arxiv.org/abs/2602.00521.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "598c6d05-4197-4a89-82ef-b021c3eac350",
  "isSidechain": true,
  "promptId": "c70ddd60-84e4-415e-8b5e-2a776b11fc55",
  "agentId": "a7acfb706113e525c",
  "type": "user",
  "uuid": "6297c841-5a0e-455f-9dbe-3f46c90f5241",
  "sourceToolAssistantUUID": "598c6d05-4197-4a89-82ef-b021c3eac350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-27T23:57:59.140Z_

Now I have comprehensive information. Let me compile the detailed findings.

---

## Detailed Findings

### 1. AutoJudger (arXiv 2505.21389)

**Title:** AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs

**Authors:** Xuanwen Ding, Chengjun Pan, Zejun Li, Jiwen Zhang, Siyuan Wang, Zhongyu Wei (Fudan University; University of Southern California)

**Date:** May 27, 2025

#### What AutoJudger Does
AutoJudger is an adaptive evaluation framework that dramatically reduces the cost of benchmarking Multimodal Large Language Models (MLLMs). Instead of running a model through an entire benchmark (tens of thousands of questions), it intelligently selects a tiny subset (~4-5%) of questions that are maximally informative, achieving >90% ranking accuracy compared to full evaluation.

#### How It Uses IRT
- Uses the **one-parameter logistic (Rasch/1PL) model**: `p(correct) = 1/(1 + exp(-(a_j - d_i)))` where `a_j` = model ability, `d_i` = question difficulty.
- Item difficulty parameters are estimated **offline** via Bayesian variational inference with MLE on historical response data from multiple models.
- During evaluation, item difficulties are **fixed**; only model ability is updated dynamically as the model answers questions.
- Questions are filtered to those with estimated success probability between 0.2 and 0.8 (the informative range for the current ability estimate).

#### Is It Multimodal?
Yes, explicitly multimodal:
- Uses **CLIP ViT-B/32** embeddings to encode both images and text for semantic clustering and diversity measurement.
- The selection agent (**Qwen2.5-VL-7B**) analyzes full question-image pairs, not just text.
- Ablation studies confirmed that removing visual information degraded performance.
- Tested on multimodal benchmarks: MMMU-Dev Val (11.5K questions), SEEDBench-Image (19K+), MMT-Bench-Val (31K+), AI2D-Test (5K+ diagrams).

#### Does It Generate New Items or Calibrate Existing Ones?
**Neither generates nor calibrates in a novel sense.** AutoJudger exclusively **selects from existing benchmark items**. It calibrates item difficulty parameters offline from historical data, then uses those fixed parameters to guide adaptive selection. No new questions are ever created.

#### Adaptive Testing Algorithm (4 steps per iteration)
1. **Difficulty Filtering:** Remove questions outside the 0.2-0.8 success probability window.
2. **Semantic Diversity:** Max-min retrieval selects 5 candidates with maximum Euclidean distance from previously attempted questions (in CLIP embedding space).
3. **Agent-Based Selection:** An MLLM agent examines the 5 candidates considering memory, ability estimates, and visual/textual semantics, then picks the best one.
4. **Memory Update:** A dynamic memory table tracks per-category statistics (count, max/min/avg difficulty, accuracy) to prevent mode collapse.

#### Key Results
- **MMT-Bench:** 92% rank consistency with only 4% of data (125 samples)
- At 5% compression: AI2D 94.85%, MMMU 87.94%, MMT-Bench 92.06%, SEEDBench 90.74% ranking accuracy
- Superior stability (lower variance) vs. random, stratified, and cluster-based sampling baselines.

---

### 2. How AutoJudger Differs From a System Combining Programmatic Generation + IRT Calibration + Frontier Tracking for Multimodal Math

| Dimension | AutoJudger | Programmatic Generation + IRT + Frontier Tracking |
|---|---|---|
| **Item creation** | None. Selects from fixed existing benchmarks. | Generates new items programmatically (e.g., via Python programs like DynaMath). |
| **IRT model** | 1PL (Rasch) only. Simple difficulty parameter. | Could use 2PL or 3PL with discrimination and guessing parameters for richer item characterization. |
| **IRT role** | Guides adaptive item *selection* to reduce evaluation cost. | Calibrates item parameters to understand difficulty landscape AND track model ability over time. |
| **Benchmark contamination** | Does not address contamination; items are static and known. | Programmatic generation inherently resists contamination since items are novel. |
| **Frontier tracking** | No longitudinal tracking. Evaluates one model at a time. | Explicitly tracks how the difficulty frontier evolves as new models emerge. |
| **Domain** | General multimodal (diagrams, seeds, expert knowledge, etc.). | Focused on multimodal math specifically. |
| **Difficulty control** | Selects items at appropriate difficulty; cannot create harder items when existing ones saturate. | Can generate items at arbitrary difficulty levels, solving the saturation problem. |
| **Scalability to future models** | Limited by the fixed item pool. When all items become too easy, the benchmark is saturated. | Unlimited, because new harder items can be generated on demand. |
| **Goal** | Efficiency: same evaluation quality with fewer items. | Expressiveness + longevity: always have items that discriminate at the frontier. |

The key philosophical difference: AutoJudger optimizes the *efficiency* of evaluation on static benchmarks. A programmatic generation + IRT system optimizes the *expressiveness and longevity* of evaluation by creating new items as needed, calibrating them with IRT, and tracking how the frontier of model capabilities shifts over time. AutoJudger cannot solve benchmark saturation or contamination because it is bound to existing items.

---

### 3. Other Relevant Recent Papers (2025-2026) Combining IRT with Multimodal or LLM Evaluation

**M3IRT** (arXiv 2603.02663) -- "Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory"
- Authors: Uebayashi et al. (Kyoto University, CyberAgent, Tohoku University)
- Decomposes ability and difficulty into image-only, text-only, and cross-modal components.
- Identifies "shortcut questions" solvable with a single modality.
- Preserves ranking fidelity with only 10% of items; robust to 50% injected low-quality items.
- Calibrates existing items; does not generate new ones.
- Tested on MMMU, MathVista, SEED-Bench with 24 VLMs.
- This is the most relevant paper for multimodal IRT specifically.

**ATLAS** (arXiv 2511.04689) -- "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"
- Authors: Peiyu Li et al. (Notre Dame)
- Uses 3PL IRT with Fisher information-guided item selection.
- Reduces items by up to 90%. Text-only; not multimodal.
- Calibrates from 3,000+ LMs. Does not generate items.

**PSN-IRT / "Lost in Benchmarks"** (arXiv 2505.15055, AAAI)
- Pseudo-Siamese Network for IRT; neural-enhanced item parameter estimation.
- Analyzes 11 benchmarks (41,871 items), revealing saturation and contamination.
- Constructs smaller benchmarks with stronger human-preference alignment.
- Text-only; does not generate items.

**CAT for Medical LLMs** (arXiv 2603.23506)
- IRT-based CAT for medical knowledge assessment.
- Achieves r=0.988 correlation with full assessment using 1.3% of items across 38 LLMs.
- Text-only; selects from existing human-calibrated medical item bank.

**Confident Rankings with Fewer Items** (arXiv 2601.13885)
- Extends IRT to continuous bounded scores (ROUGE, BLEU, LLM-as-judge).
- Uses heteroskedastic normal distribution instead of Bernoulli.
- 2% of items; text-only; no item generation.

**Diagnosing LLM-as-a-Judge Reliability** (arXiv 2602.00521)
- Uses Graded Response Model (GRM) of IRT to assess judge reliability.
- Measures intrinsic consistency and human alignment.
- Different focus: evaluating the evaluator, not the model.

**DynaMath** (arXiv 2411.00836)
- 501 seed questions as Python programs generating variant math problems.
- Programmatic generation approach closest to your concept, but does NOT use IRT for calibration.
- Focuses on robustness evaluation via visual/textual perturbations.

---

### 4. Key Takeaway: The Gap in the Literature

There is a clear research gap at the intersection of these approaches. The landscape breaks down as follows:

- **IRT for adaptive selection** (AutoJudger, ATLAS, CAT-Medical): Efficient but bound to static item pools. Cannot generate new items or address saturation/contamination.
- **IRT for multimodal decomposition** (M3IRT): Rich modality-aware modeling but still operates on fixed items.
- **Programmatic generation** (DynaMath, VLB): Creates new items dynamically but does NOT use IRT for difficulty calibration or ability estimation.
- **IRT for benchmark quality analysis** (PSN-IRT): Diagnoses problems but doesn't solve them.

No existing paper combines all three of: (1) programmatic item generation, (2) IRT-based calibration of generated items, and (3) frontier tracking of model capabilities over time -- particularly for multimodal math. A system doing this would be genuinely novel and would address the saturation and contamination problems that all current IRT-based approaches inherit from their reliance on static item pools.

Sources:
- [AutoJudger (arXiv 2505.21389)](https://arxiv.org/abs/2505.21389)
- [AutoJudger HTML](https://arxiv.org/html/2505.21389v1)
- [M3IRT (arXiv 2603.02663)](https://arxiv.org/html/2603.02663v1)
- [ATLAS (arXiv 2511.04689)](https://arxiv.org/abs/2511.04689)
- [Lost in Benchmarks / PSN-IRT (arXiv 2505.15055)](https://arxiv.org/abs/2505.15055)
- [CAT for Medical LLMs (arXiv 2603.23506)](https://arxiv.org/abs/2603.23506)
- [Confident Rankings with Fewer Items (arXiv 2601.13885)](https://arxiv.org/abs/2601.13885)
- [Diagnosing LLM-as-a-Judge Reliability (arXiv 2602.00521)](https://arxiv.org/abs/2602.00521)
- [DynaMath (arXiv 2411.00836)](https://arxiv.org/abs/2411.00836)
- [VLB Dynamic Multimodal Evaluation (arXiv 2410.08695)](https://arxiv.org/abs/2410.08695)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6297c841-5a0e-455f-9dbe-3f46c90f5241",
  "isSidechain": true,
  "agentId": "a7acfb706113e525c",
  "requestId": "req_011CbTyinQFFw9GAWxvygz3j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbe90fb8-eb4b-411f-b980-3f62a9592dc7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "31cc7514-0c05-4e6e-a370-ce9e9fb73fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAvrZFRtkuiTpXXmucFHB8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 20752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1878,
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
