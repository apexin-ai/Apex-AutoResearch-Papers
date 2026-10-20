# Research conversation: You are researching the current state-of-the-art on the ProcessBench benchmark for process reward model evaluation, as o

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 113
- **Recorded user turns:** 1
- **Tool calls:** 47
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a195100b4dfd60a19.jsonl`
- **Structured JSON:** [`c1aa01e3f1984ed467e9.json`](../../sessions/c1/c1aa01e3f1984ed467e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

113 recorded events

### User

_source line 1 · 2026-05-27T17:47:57.989Z_

You are researching the current state-of-the-art on the ProcessBench benchmark for process reward model evaluation, as of May 2026.

I need:
1. Current leaderboard/SOTA on ProcessBench - which models achieve what F1 scores?
2. Performance of key models: GenPRM (various sizes), ThinkPRM (various sizes), any other recent entries
3. What is the gap between generative vs discriminative approaches on ProcessBench?
4. Any new benchmarks beyond ProcessBench that are now standard for PRM evaluation?
5. Recent papers (2025-2026) that report ProcessBench numbers

Use WebSearch with queries like:
- "ProcessBench leaderboard state of the art 2025 2026"
- "ProcessBench F1 scores process reward model comparison"
- "process reward model benchmark comparison 2026"
- "ProcessBench best results generative verifier"
- "Papers with Code ProcessBench"

Then use WebFetch on any relevant leaderboard pages or papers. Report all specific numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "d8bc4f07-0252-4dfe-89a7-307efafc662c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T17:47:57.991Z_

```json
{
  "parentUuid": "d8bc4f07-0252-4dfe-89a7-307efafc662c",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
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
      "TaskStop",
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
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "071df556-a556-475b-b4b0-4eb53660dc66",
  "timestamp": "2026-05-27T17:47:57.991Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T17:47:57.991Z_

```json
{
  "parentUuid": "071df556-a556-475b-b4b0-4eb53660dc66",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5923a75b-45fb-4c63-bc91-9b9bffc8841f",
  "timestamp": "2026-05-27T17:47:57.991Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T17:48:00.741Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5923a75b-45fb-4c63-bc91-9b9bffc8841f",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbJkPhv5gJ2vu9Y7Uc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "903cf740-7c57-4997-b9d2-610e788d7039",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JUHNAbDigSooV51NEdE2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1576,
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

_source line 5 · 2026-05-27T17:48:00.826Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016ix792YNM1sL6z26qgrrqT`</summary>

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
  "parentUuid": "903cf740-7c57-4997-b9d2-610e788d7039",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbJkPhv5gJ2vu9Y7Uc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a4419e9-3c47-4963-a585-f2fcce545514",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JUHNAbDigSooV51NEdE2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1576,
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

_source line 6 · 2026-05-27T17:48:00.830Z_

<details><summary>↩ Tool result · `toolu_016ix792YNM1sL6z26qgrrqT`</summary>

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
  "parentUuid": "8a4419e9-3c47-4963-a585-f2fcce545514",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "756e589a-bad1-4890-b71a-2f883cc4e745",
  "sourceToolAssistantUUID": "8a4419e9-3c47-4963-a585-f2fcce545514",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T17:48:03.324Z_



Now let me run multiple searches in parallel to gather information on ProcessBench.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "756e589a-bad1-4890-b71a-2f883cc4e745",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbXAG6Z3uTKcBAFzow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b379c0d-5a39-4b9f-9f0e-e113d0907ac6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQKKC4whRdVonsRBRjWBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 8 · 2026-05-27T17:48:03.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6P1KvMs5FQX1RrwDJQXvz`</summary>

```json
{
  "query": "ProcessBench leaderboard state of the art 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b379c0d-5a39-4b9f-9f0e-e113d0907ac6",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbXAG6Z3uTKcBAFzow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e139431f-0494-4db1-a63d-f26de7678f34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQKKC4whRdVonsRBRjWBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 9 · 2026-05-27T17:48:04.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017RecZKMTtfdvojmf5TzXPs`</summary>

```json
{
  "query": "ProcessBench F1 scores process reward model comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e139431f-0494-4db1-a63d-f26de7678f34",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbXAG6Z3uTKcBAFzow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c7fbcf7-18c9-475c-bea5-fc4c2ca1b93a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQKKC4whRdVonsRBRjWBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 10 · 2026-05-27T17:48:04.833Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q4BGuhyURRCZW2jsU58etj`</summary>

```json
{
  "query": "GenPRM ThinkPRM ProcessBench results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c7fbcf7-18c9-475c-bea5-fc4c2ca1b93a",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbXAG6Z3uTKcBAFzow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3b88e42-7271-4d52-816a-6f79d0624848",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQKKC4whRdVonsRBRjWBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 11 · 2026-05-27T17:48:04.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lo5AHfEMHZh4SKu8UyqCck`</summary>

```json
{
  "query": "Papers with Code ProcessBench benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3b88e42-7271-4d52-816a-6f79d0624848",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVbXAG6Z3uTKcBAFzow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e987fdfb-e7b0-47d2-ae7f-4279e0f2dbd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQKKC4whRdVonsRBRjWBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8987,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 8987,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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

_source line 12 · 2026-05-27T17:48:10.094Z_

<details><summary>↩ Tool result · `toolu_01A6P1KvMs5FQX1RrwDJQXvz`</summary>

```text
Web search results for query: "ProcessBench leaderboard state of the art 2025 2026"

Links: [{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"AI Benchmarks 2026: Top Evaluations and Their Limits","url":"https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"ProcessTBench: An LLM Plan Generation Dataset for Process Mining","url":"https://arxiv.org/pdf/2409.09191"},{"title":"ProBench: Benchmarking GUI Agents with Accurate Process Information","url":"https://arxiv.org/pdf/2511.09157"}]

Based on the search results, I found information about ProcessBench as a benchmark for process-level reward models, though not a dedicated "ProcessBench leaderboard" in the traditional sense.

ProcessBench is a benchmark for assessing reasoning process evaluation, containing 3,400 test cases with an average of 7.1 steps. It is used to evaluate process reward models (PRMs), which help assess the correctness of reasoning steps and train large language models with appropriate rewards.

However, the search results show that ProcessBench has been compared to newer benchmarks like PRMBench, which offers more fine-grained error type detection and larger test cases (6,216 test cases with 13.4 average steps).

The broader AI benchmark landscape for 2025-2026 includes various leaderboards tracking state-of-the-art models across different tasks (coding, math, reasoning), but ProcessBench itself appears to be a specific evaluation dataset rather than a public leaderboard with ranked models. If you're looking for information about a specific ProcessBench leaderboard platform or more recent rankings, please let me know and I can search for more targeted information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e139431f-0494-4db1-a63d-f26de7678f34",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "46cc1abe-c0f9-4165-bfe3-71de68d0642c",
  "sourceToolAssistantUUID": "e139431f-0494-4db1-a63d-f26de7678f34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T17:48:11.237Z_

<details><summary>↩ Tool result · `toolu_01Lo5AHfEMHZh4SKu8UyqCck`</summary>

```text
Web search results for query: "Papers with Code ProcessBench benchmark"

Links: [{"title":"Paper page - ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://huggingface.co/papers/2412.06559"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"Code2Bench: Scaling Source and Rigor for Dynamic Benchmark Construction","url":"https://arxiv.org/pdf/2508.07180"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research","url":"https://arxiv.org/pdf/2506.17335"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=LiveCodeBench+Pro"}]

Based on the search results, here's what I found about the ProcessBench benchmark:

ProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning. 

**Key characteristics:**
- It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems, with each test case containing a step-by-step solution with error location annotated by human experts.
- Models are required to identify the earliest step that contains an error, or conclude that all steps are correct.

**Main findings:**
ProcessBench evaluates models' ability to identify errors in mathematical reasoning steps, showing that existing process reward models struggle with difficult problems and underperform compared to critic models and a fine-tuned PRM. The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini.

The benchmark was introduced in December 2024 and is designed to foster research in reasoning process assessment and scalable oversight of language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e987fdfb-e7b0-47d2-ae7f-4279e0f2dbd7",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "e7ac5cb3-c868-4b14-b189-789a54307450",
  "sourceToolAssistantUUID": "e987fdfb-e7b0-47d2-ae7f-4279e0f2dbd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T17:48:11.398Z_

<details><summary>↩ Tool result · `toolu_01Q4BGuhyURRCZW2jsU58etj`</summary>

```text
Web search results for query: "GenPRM ThinkPRM ProcessBench results"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2?locale=en"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"THINKPRM: generative Process Reward Model for solution verification via long CoT Reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"}]

Based on the search results, here are the key findings on GenPRM, ThinkPRM, and ProcessBench results:

## GenPRM Results on ProcessBench

Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. GenPRM significantly outperforms prior PRMs with only 23K training data from MATH. The results show consistent scaling benefits with both model size and test-time compute, with larger models performing better on single samples and test-time scaling consistently improving performance across all model sizes.

## ThinkPRM Results on ProcessBench

ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. On a subset of GPQA-Diamond and LiveCodeBench, ThinkPRM surpasses discriminative verifiers trained on full PRM800K by 8% and 4.5%, respectively.

## Key Innovations

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. GenPRM is a generative process reward model that performs explicit Chain-of-Thought reasoning with code verification before providing judgment for each reasoning step, using Relative Progress Estimation and a rationale synthesis framework that incorporates code verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3b88e42-7271-4d52-816a-6f79d0624848",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "3bcff773-8f4e-4d1c-bc29-0c0ca553e9c0",
  "sourceToolAssistantUUID": "a3b88e42-7271-4d52-816a-6f79d0624848",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T17:48:12.501Z_

<details><summary>↩ Tool result · `toolu_017RecZKMTtfdvojmf5TzXPs`</summary>

```text
Web search results for query: "ProcessBench F1 scores process reward model comparison"

Links: [{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2412.06559v4"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"[Literature Review] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://www.themoonlight.io/en/review/r-prm-reasoning-driven-process-reward-modeling"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/pdf/2506.03570"},{"title":"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/pdf/2512.03244"},{"title":"Performance (F1) on ProcessBench. Results marked with * come from Zhang... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Performance-F1-on-ProcessBench-Results-marked-with-come-from-Zhang-et-alThe-best_tbl1_392105521"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=prm@8"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://github.com/NJUNLP/R-PRM"}]

Based on the search results, here's a comprehensive overview of ProcessBench F1 scores and process reward model comparisons:

## ProcessBench Overview

ProcessBench requires models to identify the earliest step that contains an error, or conclude that all steps are correct.

## Key F1 Score Comparisons

**Leading Models:**
- QwQ-32B-Preview achieves the highest performance among non-proprietary systems with 71.5% average F1 score, and this performance is competitive with and sometimes exceeds GPT-4o-0806 (61.9% F1)

**Recent Advances:**
- Aggregating multiple independent verifications at the step level produces training data for process reward models that achieve 67.5 F1 on ProcessBench compared to 66.4 for reference-guided training and 61.9 for GPT-4o

- R-PRM achieves F1 scores of 65.2 on ProcessBench, representing significant improvements over state-of-the-art baselines

- FreePRM achieves an average F1 score of 53.0% on ProcessBench, outperforming fully supervised PRM trained on Math-Shepherd by +24.1%

**Generalization Challenges:**
The Math-Shepherd-PRM-7B model achieves an F1 score of 47.9% on GSM8K but drops to 23.8% on Omni-MATH, illustrating performance variations across different mathematical reasoning datasets.

Evaluations indicate that most current process reward models underperform general language models acting as critics, and human-annotated training data is crucial for robust performance in error identification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c7fbcf7-18c9-475c-bea5-fc4c2ca1b93a",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "e705a6e2-32c8-40d4-aace-c50e6a5f11b2",
  "sourceToolAssistantUUID": "7c7fbcf7-18c9-475c-bea5-fc4c2ca1b93a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-27T17:48:15.311Z_

Good, I have initial results. Now let me dive deeper into the specific papers and pages to get exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e705a6e2-32c8-40d4-aace-c50e6a5f11b2",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVcPKWFcymtWMKnNAJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b395ad67-8b7c-4a4a-93df-06d6c25b4dec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ta7DJfACBkWRKck8Jczxz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1340,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 10109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1744,
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

_source line 17 · 2026-05-27T17:48:17.515Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DWtqfG2ap7MyZ4EvmBMk8T`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract ALL ProcessBench F1 scores reported for GenPRM models (all sizes: 1.5B, 7B, 72B) and all baseline models. Include exact numbers, model names, and any comparisons. Also extract results with test-time scaling (majority voting, best-of-N)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b395ad67-8b7c-4a4a-93df-06d6c25b4dec",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVcPKWFcymtWMKnNAJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2f245ad-e17c-4f8f-9197-d68cd0d9f4e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ta7DJfACBkWRKck8Jczxz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1340,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 10109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1744,
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

_source line 18 · 2026-05-27T17:48:19.471Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ne49JCvEitDb59BrQ13qTY`</summary>

```json
{
  "url": "https://huggingface.co/papers/2504.16828",
  "prompt": "Extract ALL ProcessBench F1 scores and other benchmark results reported for ThinkPRM models (all sizes). Include exact numbers for ThinkPRM-1.5B, ThinkPRM-7B, ThinkPRM-14B, or any other sizes. Include all baseline comparisons and discriminative vs generative comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2f245ad-e17c-4f8f-9197-d68cd0d9f4e2",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVcPKWFcymtWMKnNAJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74d611d4-72e4-4061-b40b-493746d204a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ta7DJfACBkWRKck8Jczxz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1340,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 10109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1744,
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

_source line 19 · 2026-05-27T17:48:20.346Z_

<details><summary>↩ Tool result · `toolu_01Ne49JCvEitDb59BrQ13qTY`</summary>

```text
&lt;persisted-output>
Output too large (83.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01Ne49JCvEitDb59BrQ13qTY.txt

Preview (first 2KB):
Title: Process Reward Models That Think

URL Source: https://arxiv.org/html/2504.16828

Markdown Content:
\undefine@key

newfloatplacement\undefine@key newfloatname\undefine@key newfloatfileext\undefine@key newfloatwithin

Muhammad Khalifa♡, Rishabh Agarwal♠, Lajanugen Logeswaran♢,Jaekyeom Kim♢, Hao Peng♣, Moontae Lee♢, Honglak Lee♡♢⋆, Lu Wang♡⋆

♡University of Michigan ♠Mila♢LG AI Research ♣University of Illinois Urbana-Champaign⋆Equal supervision

[khalifam@umich.edu](mailto:khalifam@umich.edu)

###### Abstract

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by _generating_ a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers—using only 1% of the process labels in PRM800K—across several challenging benchmarks. Specifically, ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME ’24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation over subsets of GPQA-Diamond and LiveCodeBench, our PRM surpasses discriminative verifiers trained with the full PRM800K by 8% and 4.5%, respectively. Lastly, under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. This work highlights the value of generative, long CoT PRMs that can scale test-time compute for verification while requiring minimal supervision for training.1 1 1 Our code, data, and models are released at [https://github.com/mukhal/thinkprm](https://github.com/mukhal/th
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74d611d4-72e4-4061-b40b-493746d204a8",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "53e2e90b-e954-46d0-8b36-650c54442c95",
  "sourceToolAssistantUUID": "74d611d4-72e4-4061-b40b-493746d204a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T17:48:20.883Z_

<details><summary>↩ Tool result · `toolu_01DWtqfG2ap7MyZ4EvmBMk8T`</summary>

```text
# GenPRM ProcessBench F1 Scores - Information Not Available

Based on the provided content, **specific ProcessBench F1 scores are not included**. The abstract only states that "GenPRM significantly outperforms prior PRMs" and mentions comparative achievements: "a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench."

However, the exact numerical F1 scores for any model sizes or baseline comparisons are absent from this webpage excerpt. The document references are limited to abstract-level information without detailed benchmark tables or quantitative results.

**To access the specific metrics you're seeking**, you would need to:
- Review the full PDF paper (linked as "View PDF")
- Check the associated code and results repository mentioned at the conclusion
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2f245ad-e17c-4f8f-9197-d68cd0d9f4e2",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "baa79430-4f05-41ad-ada3-af798b88edae",
  "sourceToolAssistantUUID": "c2f245ad-e17c-4f8f-9197-d68cd0d9f4e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T17:48:20.889Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011yz1i53BDA52FxkqwcyDti`</summary>

```json
{
  "url": "https://www.researchgate.net/figure/Performance-F1-on-ProcessBench-Results-marked-with-come-from-Zhang-et-alThe-best_tbl1_392105521",
  "prompt": "Extract the FULL table of ProcessBench F1 scores. List every model name and its F1 score. Include all columns and rows visible in the table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baa79430-4f05-41ad-ada3-af798b88edae",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVcPKWFcymtWMKnNAJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51c7d441-2b5d-4207-87e8-98a5890039a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ta7DJfACBkWRKck8Jczxz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1340,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 10109,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1744
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1340,
          "output_tokens": 447,
          "cache_read_input_tokens": 10109,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1744,
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

_source line 22 · 2026-05-27T17:48:21.119Z_

<details><summary>↩ Tool result · `toolu_011yz1i53BDA52FxkqwcyDti`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51c7d441-2b5d-4207-87e8-98a5890039a1",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "2992e1d1-f10b-4684-ab31-4669009e6088",
  "sourceToolAssistantUUID": "51c7d441-2b5d-4207-87e8-98a5890039a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-27T17:48:24.132Z_

Let me read the ThinkPRM paper content and fetch the GenPRM PDF for detailed numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2992e1d1-f10b-4684-ab31-4669009e6088",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVd1eYSY1oChfZadNMJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1325bcdb-2105-41f8-9219-08fdacbbaa08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2bCuWEfrmmuKbLidjkPW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2835,
      "cache_read_input_tokens": 11853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2835,
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

_source line 24 · 2026-05-27T17:48:25.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QGXyq9yabwVL67MPASdpqY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01Ne49JCvEitDb59BrQ13qTY.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1325bcdb-2105-41f8-9219-08fdacbbaa08",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVd1eYSY1oChfZadNMJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5b63a05-1fff-4966-973d-e8e1041cfb66",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2bCuWEfrmmuKbLidjkPW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2835,
      "cache_read_input_tokens": 11853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2835,
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

_source line 25 · 2026-05-27T17:48:25.510Z_

<details><summary>↩ Tool result · `toolu_01QGXyq9yabwVL67MPASdpqY`</summary>

```text
1	Title: Process Reward Models That Think
2	
3	URL Source: https://arxiv.org/html/2504.16828
4	
5	Markdown Content:
6	\undefine@key
7	
8	newfloatplacement\undefine@key newfloatname\undefine@key newfloatfileext\undefine@key newfloatwithin
9	
10	Muhammad Khalifa♡, Rishabh Agarwal♠, Lajanugen Logeswaran♢,Jaekyeom Kim♢, Hao Peng♣, Moontae Lee♢, Honglak Lee♡♢⋆, Lu Wang♡⋆
11	
12	♡University of Michigan ♠Mila♢LG AI Research ♣University of Illinois Urbana-Champaign⋆Equal supervision
13	
14	[khalifam@umich.edu](mailto:khalifam@umich.edu)
15	
16	###### Abstract
17	
18	Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by _generating_ a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers—using only 1% of the process labels in PRM800K—across several challenging benchmarks. Specifically, ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME ’24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation over subsets of GPQA-Diamond and LiveCodeBench, our PRM surpasses discriminative verifiers trained with the full PRM800K by 8% and 4.5%, respectively. Lastly, under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. This work highlights the value of generative, long CoT PRMs that can scale test-time compute for verification while requiring minimal supervision for training.1 1 1 Our code, data, and models are released at [https://github.com/mukhal/thinkprm](https://github.com/mukhal/thinkprm).
19	
20	![Image 1: Refer to caption](https://arxiv.org/html/2504.16828v5/x1.png)
21	
22	Figure 1: Left: Verifier F1-score on ProcessBench(Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)). ThinkPRM-14B, trained on 8K process labels or 1K synthetic examples, outperforms discriminative PRMs trained on about 100x more data. Right: Verifier-guided search accuracy on MATH-500 with Llama-3.2-3B-Instruct as generator. ThinkPRM-1.5B, trained using the same 8K labels, outperforms LLM-as-a-judge and discriminative verifiers in reward-guided search on MATH-500. The LLM-as-a-judge in both figures uses the same base model as ThinkPRM. 
23	
24	1 Introduction
25	--------------
26	
27	Reasoning with large language models (LLMs) can substantially benefit from utilizing more test-time compute (Jaech et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib21); Guo et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib15); Akyürek et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib1)). This typically depends on a high-quality process reward model (PRM)—also known as a process verifier—that scores (partial) solutions for selecting promising paths for search or ranking (Cobbe et al., [2021](https://arxiv.org/html/2504.16828v5#bib.bib11); Li et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib29); Wu et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib49); Brown et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib5)). PRMs have typically assumed the form of discriminative classifiers, trained to discern correct from incorrect reasoning (Uesato et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib43); Zhang et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib60)). However, training discriminative PRMs requires access to process labels, i.e., step-level annotations, which either require extensive human annotation (Lightman et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib30); Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)), gold step-by-step solutions (Khalifa et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib25)), or compute-intensive rollouts (Luo et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib33); Chen et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib8)). For instance, training reasonably performing math PRMs requires hundreds of thousands of step-level annotations (Lightman et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib30); Wang et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib46)).
28	
29	Generative verification either via LLM-as-a-judge(Wang et al., [2023a](https://arxiv.org/html/2504.16828v5#bib.bib45); Liu et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib32); Zheng et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib62)) or GenRM (Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58)) treats verification as a generation problem of a rationale followed by a decision. However, LLM-as-a-judge is known to perform poorly compared to specialized reward models(Lambert et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib28); Zhang et al., [2024b](https://arxiv.org/html/2504.16828v5#bib.bib59); Chen et al., [2024c](https://arxiv.org/html/2504.16828v5#bib.bib10)), as general-purpose LLMs frequently fail to recognize reasoning errors(Huang et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib19); Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58); Ye et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib54)). Moreover, GenRM is limited to outcome verification via short chain-of-thoughts (CoTs), fundamentally limiting its ability for test-time scaling.
30	
31	![Image 2: Refer to caption](https://arxiv.org/html/2504.16828v5/x2.png)
32	
33	Figure 2: ThinkPRM enables scaling verification compute with more CoT tokens.
34	
35	This paper builds on the insight that generative step-by-step verification can greatly benefit from scaling up the verifier’s inference compute—specifically, by enabling it to think through a CoT. Specifically, we repurpose open-weight large reasoning models (LRMs) as the foundation for generative PRMs through lightweight training. This training uses uses synthetic data (Kim et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib26); Zhu et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib64); Wang et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib47)), utilizing as few as 8K step labels, and yieldinga ThinkPRM —a PRM that not only surpasses LLM-as-a-judge, but also outperforms discriminative PRMs trained on two orders of magnitude more data across a variety of test-time scaling scenarios.
36	
37	We obtain ThinkPRM by training four reasoning models, namely R1-Distill-Qwen{1.5B,7B,14B} (Guo et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib15)), and QwQ-32B-Preview (Team, [2024](https://arxiv.org/html/2504.16828v5#bib.bib42)), and extensively evaluate it both as a standalone verifier on ProcessBench (Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)), and combined with a generator under Best-of-N and verifier-guided beam search. ThinkPRM-14B outperforms a discriminative PRM based on the same base model in terms of accuracy while using far fewer supervision signals as in [Fig.1](https://arxiv.org/html/2504.16828v5#S0.F1 "In Process Reward Models That Think") left. In addition, ThinkPRM-1.5B demonstrates strong performance on MATH-500 (Hendrycks et al., [2021](https://arxiv.org/html/2504.16828v5#bib.bib17)) under guided beam search, shown in [Fig.1](https://arxiv.org/html/2504.16828v5#S0.F1 "In Process Reward Models That Think") right. Lastly, as shown in [Fig.2](https://arxiv.org/html/2504.16828v5#S1.F2 "In 1 Introduction ‣ Process Reward Models That Think"), ThinkPRM can effectively utilize more verification compute than LLM-as-a-judge, by forcing it to think for more tokens. All these results are obtained while training only on 8K step labels.
38	
39	Our work highlights the promise of long CoT PRMs that verify reasoning with reasoning, effectively scaling both generator and verifier compute. Our main findings are as follows: ThinkPRM outperforms strong PRM baselines in best-of-N and guided-search setups on two math reasoning benchmarks: MATH-500 and AIME 2024, and surpasses LLM-as-a-judge baselines under the same base model by thinking longer during verification ([section 4](https://arxiv.org/html/2504.16828v5#S4 "4 Test-time Scaling Experiments ‣ Process Reward Models That Think")). Moreover, ThinkPRM generalizes under two types of domain shift. First, it outperforms baselines on out-of-domain tasks such as scientific reasoning and code generation. Second, despite being trained only on short solutions, it generalizes to long-form reasoning without explicit step delimiters ([section 5.3](https://arxiv.org/html/2504.16828v5#S5.SS3 "5.3 Reasoning traces without clear step boundaries ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think")). Third, ThinkPRM outperforms self-consistency(Wang et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib48)) when using the same compute budget, especially under high sampling regimes ([section 5.4](https://arxiv.org/html/2504.16828v5#S5.SS4 "5.4 Compute-matched comparison to self-consistency ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think")). Finally, fine-grained filtering of synthetic data based on step supervision is crucial for training high-quality PRMs ([section 5.7](https://arxiv.org/html/2504.16828v5#S5.SS7 "5.7 Filtering based on process vs. outcome labels ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think")).
40	
41	2 Background and Related Work
42	-----------------------------
43	
44	#### Discriminative PRMs.
45	
46	Discriminative PRMs are trained as classifiers that directly predict numerical correctness scores for each solution step, and typically rely on extensive step-level annotations(Uesato et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib43); Lightman et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib30); Zhang et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib60)). Given a solution prefix, discriminative PRMs encode the solution text and employ a classification head to produce step-level scores, usually optimized with binary cross-entropy. An overall correctness score for a solution is obtained by aggregating these step-level scores([Beeching et al.,](https://arxiv.org/html/2504.16828v5#bib.bib4)). PRMs are effective and straightforward but they do not utilize the language-modeling head of the base language model, making training expensive and labor-intensive(Yuan et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib56)). Additionally, they offer limited interpretability and utilize fixed compute, restricting their dynamic scalability at test-time(Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58); Mahan et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib34)). Thus, there is a need for data-efficient PRMs that can scale with more test-time compute.
47	
48	#### Generative Verification.
49	
50	Generative verification (Zheng et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib62); Zhu et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib64); Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58)) frames verification as a language-generation task, producing step-level decisions as tokens (e.g., “correct” or “incorrect”), typically accompanied by a chain-of-thought (CoT). One can train generative verifiers using the standard language modeling objective on verification rationales rather than on binary labels. This approach leverages the strengths of LLMs in text generation, making generative verifiers inherently interpretable and scalable(Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58); Mahan et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib34); Wang et al., [2023a](https://arxiv.org/html/2504.16828v5#bib.bib45); Ankner et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib2)). However, prior work on generative verifiers has relied mainly on short verification CoT (e.g., few hundred tokens) (Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58)), which highly limits their scalability. Thus, there is a need for verifiers that can “think” longer through verification, utilizing test-time compute effectively. While LLM-as-a-Judge has been employed for step-level verification(Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)). it tends to be sensitive to prompt phrasing, and prone to invalid outputs, such as infinite looping or excessive overthinking(Bavaresco et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib3))—issues we further confirm in this work. Prior results with reasoning models like QwQ-32B-Preview(Team, [2024](https://arxiv.org/html/2504.16828v5#bib.bib42)) show promise, but their practical utility in test-time scaling remains limited without additional training(Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)).
51	
52	#### Test-Time Scaling with PRMs.
53	
54	Test-time scaling techniques, such as Best-of-N selection(Charniak & Johnson, [2005](https://arxiv.org/html/2504.16828v5#bib.bib7)) and tree-based search(Yao et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib53); Chen et al., [2024c](https://arxiv.org/html/2504.16828v5#bib.bib10); Wan et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib44)), leverage additional inference-time compute to improve reasoning performance. Central to these approaches is the quality of the verifier used to score and select solutions. A major advantage of generative PRMs is that they uniquely support simultaneous scaling of both generator and verifier compute (Zhang et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib58); Kalra & Tang, [2025](https://arxiv.org/html/2504.16828v5#bib.bib23)). In particular, our work shows that generative PRMs trained based on long CoT models (Jaech et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib21); Guo et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib15)) enable both parallel and sequential scaling of verifier compute.
55	
56	3 ThinkPRM
57	----------
58	
59	![Image 3: Refer to caption](https://arxiv.org/html/2504.16828v5/x3.png)
60	
61	Figure 3: Collecting verification chains for finetuning. First, we prompt a reasoning model, in our case QwQ-32B-Preview to critique a given solution to a problem. Then, we sample multiple verification chains, which we judge against gold process labels from PRM800K, only keeping chains that match the gold process labels.
62	
63	Our goal is verbalized PRM that, given a problem-solution pair, verifies every step in the solution via an extended chain-of-thought (CoT) such as the one shown in [Fig.44](https://arxiv.org/html/2504.16828v5#A7.F44 "In Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think") in [App.G](https://arxiv.org/html/2504.16828v5#A7 "Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think"). This section introduces issues with LLM-as-a-judge verification and proposes a data collection process (shown in [Fig.3](https://arxiv.org/html/2504.16828v5#S3.F3 "In 3 ThinkPRM ‣ Process Reward Models That Think")) to curate high-quality synthetic verification CoTs for training such PRM. The rest of the paper addresses the following research questions:
64	
65	*   •RQ1: How well do LRMs perform under LLM-as-a-judge for process-level verification? [Section 3.1](https://arxiv.org/html/2504.16828v5#S3.SS1 "3.1 LLM-as-a-judge PRMs are suboptimal ‣ 3 ThinkPRM ‣ Process Reward Models That Think") 
66	*   •RQ2: Can lightweight finetuning on synthetic verification CoTs improve the reliability and effectiveness of these models as process verifiers? [Section 3.2](https://arxiv.org/html/2504.16828v5#S3.SS2 "3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think") 
67	*   •RQ3: How does a finetuned verbalized PRM (ThinkPRM) compare to discriminative PRMs and LLM-as-a-Judge baselines under different test-time scaling scenarios? [Section 4](https://arxiv.org/html/2504.16828v5#S4 "4 Test-time Scaling Experiments ‣ Process Reward Models That Think") 
68	
69	### 3.1 LLM-as-a-judge PRMs are suboptimal
70	
71	This section highlights limitations we observe when using off-the-shelf reasoning models as process verifiers, suggesting the need for finetuning. For evaluation, we use ProcessBench (Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)), which includes problem-solution pairs with problems sourced from existing math benchmarks, along with ground-truth correctness labels. We report the binary F1-score by instructing models to verify full solutions and judge whether there exists a mistake. We use two most challenging subsets of ProcessBench: OlympiadBench (He et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib16)) and OmniMath (Gao et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib14)), each comprised of 1K problem-prefix pairs. For LLM-as-a-judge, we use the same prompt template as in Zheng et al. ([2024](https://arxiv.org/html/2504.16828v5#bib.bib61)), shown in [Fig.42](https://arxiv.org/html/2504.16828v5#A6.F42 "In Appendix F More details on LLM-as-judge verification ‣ Process Reward Models That Think"), which we found to work best overall. [Table 3](https://arxiv.org/html/2504.16828v5#A4.T3 "In Appendix D Results on ProcessBench before and after finetuning ‣ Process Reward Models That Think") shows LLM-as-a-judge F1 scores and a sample output by QwQ-32B-Preview is displayed in [Fig.41](https://arxiv.org/html/2504.16828v5#A5.F41 "In E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") in [App.F](https://arxiv.org/html/2504.16828v5#A6 "Appendix F More details on LLM-as-judge verification ‣ Process Reward Models That Think").
72	
73	We observe different issues with LLM-as-a-judge verification. First, the verification quality is highly sensitive to the instruction wording: slight change in the instruction can affect the F1-score by up to 3-4 points. First, a substantial number of the generated chains include invalid judgments, i.e., chains without an extractable overall label as clear in [Fig.10](https://arxiv.org/html/2504.16828v5#S3.F10 "In Finetuning on synthetic verification CoTs substantially improves the verifier. ‣ 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think"). Such invalid judgements are caused by the following. In some cases, final decision was in the wrong format than instructed e.g., the model tries to solve the problem rather than verify the given solution—a behavior likely stemming from the model training. Second, we noted multiple instances of overthinking(Chen et al., [2024b](https://arxiv.org/html/2504.16828v5#bib.bib9); Cuadron et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib12)), which prevents the model from terminating within the token budget, and infinite looping/repetitions, where the model gets stuck trying alternative techniques to verify the solutions.
74	
75	[Fig.4](https://arxiv.org/html/2504.16828v5#S3.F4 "In Synthetic data collection. ‣ 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think") (left) shows a histogram of verification CoT lengths generated by R1-Qwen-14B in the LLM-as-a-judge setting. Accurate CoTs tend to be shorter, typically under 3K tokens, while inaccurate CoTs are more evenly distributed and spike sharply around 7K-8K tokens, highlighting the prevalence of overthinking and looping in long chains. We show examples of these behaviors in [App.B](https://arxiv.org/html/2504.16828v5#A2 "Appendix B LLM-as-a-Judge Limitations ‣ Process Reward Models That Think"). In the next section, we mostly fix these issues via lightweight finetuning over synthetic verification CoTs.
76	
77	### 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification
78	
79	Inspired by recent work on reducing overthinking in long CoT models that by training (Yu et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib55); Kang et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib24)), we aim to improve LLM-as-a-judge performance via finetuning on high-quality verification data. Collecting real data would be expensive, so we rely on filtered synthetic data (Zelikman et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib57); Singh et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib37); Dong et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib13); Zhang et al., [2024b](https://arxiv.org/html/2504.16828v5#bib.bib59); Wang et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib47)) also known as rejection sampling finetuning. To keep our approach simple, we refrain from more expensive training techniques, such as reinforcement learning or preference-based learning.
80	
81	#### Synthetic data collection.
82	
83	As training data, we sample synthetic verification CoTs from QwQ-32B-Preview, prompting it to verify each step in a solution prefix, using the instruction shown in [Fig.21](https://arxiv.org/html/2504.16828v5#A1.F21 "In A.2 Preprocessing ‣ Appendix A Training data ‣ Process Reward Models That Think"). The problems and corresponding step-by-step solutions come from the PRM800K dataset (Lightman et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib30)), which provides both model-generated solutions and human-verified step-level labels.
84	
85	The sampling process continues until we obtain 1K verification CoTs which coreepond to 8K step labels in total. For data filtering, we use the following criteria: (i) the CoT must follow the expected format (i.e., include an extractable decision label for each step inside \boxed{} as shown in [Fig.20](https://arxiv.org/html/2504.16828v5#A1.F20 "In A.1 Sampling ‣ Appendix A Training data ‣ Process Reward Models That Think"), and (ii) the generated step judgements match the gold step labels from PRM800K, and (iii) the CoT length is within a maximum budget—to avoid the excessive overthinking behavior we observed in [Fig.4](https://arxiv.org/html/2504.16828v5#S3.F4 "In Synthetic data collection. ‣ 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think") (left). The filtering process ensures our training data is of sufficient quality. note that process-based filtering is crucial for the performance of the resulting PRM as we show in [Section 5.7](https://arxiv.org/html/2504.16828v5#S5.SS7 "5.7 Filtering based on process vs. outcome labels ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think"). Data collection is illustrated in [Fig.3](https://arxiv.org/html/2504.16828v5#S3.F3 "In 3 ThinkPRM ‣ Process Reward Models That Think"), data statistics are in [Section A.1](https://arxiv.org/html/2504.16828v5#A1.SS1 "A.1 Sampling ‣ Appendix A Training data ‣ Process Reward Models That Think") and a training example is in [Fig.20](https://arxiv.org/html/2504.16828v5#A1.F20 "In A.1 Sampling ‣ Appendix A Training data ‣ Process Reward Models That Think").
86	
87	Notably, our filtering relies only on step-level annotations, not on gold verification rationales or CoTs—making this pipeline scalable and low-overhead. In the absence of gold step-level annotations, one can obtain silver labels via Monte Carlo rollouts (Wang et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib46); Chen et al., [2024a](https://arxiv.org/html/2504.16828v5#bib.bib8)). While we train only on math data, the resulting PRM remains robust under other domains such as science QA and code generation as we show in [Section 4.2](https://arxiv.org/html/2504.16828v5#S4.SS2 "4.2 Results ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think"). We then proceed to train our models on the 1K collected chains. Our training is very lightweight; finetuning QwQ-32B-Preview takes only 4.5 hours on a single A100 80GB GPU. Refer to [Section C.1](https://arxiv.org/html/2504.16828v5#A3.SS1 "C.1 Training ThinkPRM ‣ Appendix C Training details ‣ Process Reward Models That Think") for training details.
88	
89	![Image 4: Refer to caption](https://arxiv.org/html/2504.16828v5/x4.png)
90	
91	Figure 4:  Verifier performance on ProcessBench in light of CoT lengths. On the left, LLM-as-a-judge produces excessively long chains including repetition, infinite looping, and overthinking, leading to worse verifier performance since the output never terminates. Training on collected syntehtic data substantially reduces these issues as shown in the ThinkPRM plot on the right.
92	
93	#### Finetuning on synthetic verification CoTs substantially improves the verifier.
94	
95	ThinkPRM trains on the 1K chains and is evaluated on ProcessBench and compared to LLM-as-a-judge under the same base model. [Fig.10](https://arxiv.org/html/2504.16828v5#S3.F10 "In Finetuning on synthetic verification CoTs substantially improves the verifier. ‣ 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think") shows verifier accuracy of different models before and after our finetuning. We note a substantial boost in F1 across all models, with the 1.5B model gaining most improvement by over 70 F1 points, and the 14B model performing best. Looking at the ratio of invalid judgements in [Fig.10](https://arxiv.org/html/2504.16828v5#S3.F10 "In Finetuning on synthetic verification CoTs substantially improves the verifier. ‣ 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think"), we also note a significant reduction in invalid labels with all models, except for QwQ, where it slightly increases. Lastly, the reduction in overthinking and infinite looping behavior discussed in the last section is evident, as in [Fig.4](https://arxiv.org/html/2504.16828v5#S3.F4 "In Synthetic data collection. ‣ 3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think") (right), where ThinkPRM generations maintain a reasonable length (1K-5K) tokens while being substantially more accurate.
96	
97	\caption@setoptions
98	
99	floatrow\caption@setoptions figurerow\caption@setposition b
100	
101	\caption@setoptions figure\caption@setposition b![Image 5: Refer to caption](https://arxiv.org/html/2504.16828v5/x5.png)Figure 7: LLM-as-a-judge suffers from a significant ratio of verification CoTs that do not terminate with a parsable label, i.e., \boxed{yes} or \boxed{no}. Our finetuning process that yields ThinkPRM, substantially mitigates this issue. Both verifiers are based on R1-Distill-Qwen-14B. \caption@setoptions figure\caption@setposition b![Image 6: Refer to caption](https://arxiv.org/html/2504.16828v5/x6.png)Figure 10: Verification accuracy on 2K question-solution pairs from two most challenging subsets of ProcessBench: OlympiadBench and OmniMath. ThinkPRM obtained by finetuning the correponding model over only 1K verification chains performs better.
102	
103	4 Test-time Scaling Experiments
104	-------------------------------
105	
106	This section aims to answer RQ3 introduced in [section 3](https://arxiv.org/html/2504.16828v5#S3 "3 ThinkPRM ‣ Process Reward Models That Think") by comparing ThinkPRM to baselines under different scaling scenarios. We study how ThinkPRM performs under different generation budgets (i) best-of-N selection (Wu et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib49); Brown et al., [2020](https://arxiv.org/html/2504.16828v5#bib.bib6)) and (ii) guided beam search (Snell et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib39); [Beeching et al.,](https://arxiv.org/html/2504.16828v5#bib.bib4)). We also explore how ThinkPRM performs when verifier compute is scaled either in parallel by aggregating decisions over multiple verification CoTs or sequentially through longer CoTs by forcing the model to double check or self-correct its verification.
107	
108	### 4.1 Experimental Setup
109	
110	In the remainder of the the paper, we will mainly use our finetuned verifiers based on R1-Distill-Qwen-1.5B and R1-Distill-Qwen-14B as these provide the best tradeoff between size and performance. We will refer to these as ThinkPRM-1.5B and ThinkPRM-14B, respectively.
111	
112	#### Baselines.
113	
114	We compare ThinkPRM to DiscPRM, which uses the same base model as ThinkPRM, finetuned with binary cross-entropy on the entire PRM800K dataset, totaling 712K process labels, which is two orders of magnitude larger than our training data. Details on finetuning DiscPRMs are in [Section C.2](https://arxiv.org/html/2504.16828v5#A3.SS2 "C.2 Training Discriminative Verifiers ‣ Appendix C Training details ‣ Process Reward Models That Think"). We also compare to unweighted majority voting, which merely selects the most frequent answer across the samples (Wang et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib48)), and to LLM-as-a-Judge using the same base model as ThinkPRM, prompted as in [Section 3.1](https://arxiv.org/html/2504.16828v5#S3.SS1 "3.1 LLM-as-a-judge PRMs are suboptimal ‣ 3 ThinkPRM ‣ Process Reward Models That Think").
115	
116	#### Tasks and Models.
117	
118	We show results on three math reasoning tasks, namely 100 problems from MATH-500 (Hendrycks et al., [2021](https://arxiv.org/html/2504.16828v5#bib.bib17)) covering all difficulty levels (see [Section E.5](https://arxiv.org/html/2504.16828v5#A5.SS5 "E.5 MATH-500 test examples ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") for more details), and American Invitational Mathematics Examination (AIME) problems for 2024. Since ThinkPRM was finetuned only on math data, we study the out-of-domain generalization on two tasks: scientific reasoning and code generation. For scientific reasoning, we use the physics subset of GPQA-Diamond (Rein et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib36)), consisting of 86 PhD-level multiple choice questions. For code generation, we use a 200-problem subset from the v5 release of LiveCodeBench (Jain et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib22)).
119	
120	Over MATH-500, we show results with ThinkPRM-1.5B and ThinkPRM-14B on two different generator models: Qwen-2.5-14B and Llama-3.2-3B-Instruct. The former model is used for best-of-N and the latter for beam search as search is compute intensive. Showing results with different generators guarantees that our conclusions are not specific to a certain model family or size. For the more challenging tasks, namely AIME ’24 and GPQA, we use a more capable model, namely Qwen-2.5-32B-Instruct. For code generation, we use Qwen-2.5-Coder-7B (Hui et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib20)). Implementation and hyperparemter details on how we select the final answer with best-of-N and beam search are in [App.E](https://arxiv.org/html/2504.16828v5#A5 "Appendix E Evaluation details ‣ Process Reward Models That Think").
121	
122	![Image 7: Refer to caption](https://arxiv.org/html/2504.16828v5/x7.png)
123	
124	Figure 11: Best-of-N on AIME ’24 and MATH-500. Compared to LLM-as-a-judge, DiscPRM, and (unweighted) majority vote, ThinkPRM-14B exhibits best accuracy scaling curve.
125	
126	#### Scaling verifier compute.
127	
128	Compared to DiscPRMs, generative reward models enable an extra dimension of scaling to squeeze more performance: scaling the verifier compute. Specifically,ThinkPRM allows for two types of scaling. First, we use parallel scaling(Mahan et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib34); Brown et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib5)), by sampling K K independent CoTs and averaging their scores. We will refer to this scaling using “@K” throughout the rest of the paper. Second, and more specific to long reasoning models, we use sequential scaling e.g., by enabling the model to double-check its initial verification (Xiong et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib51); Kumar et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib27); Ye et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib54)). Inspired by Muennighoff et al. ([2025](https://arxiv.org/html/2504.16828v5#bib.bib35)), we use a trigger phrase such as “Let’s verify again” to elicit self-correction of earlier verification. See [Section E.4](https://arxiv.org/html/2504.16828v5#A5.SS4 "E.4 Sequential scaling of verifier compute ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") for more details.
129	
130	\caption@setoptions
131	
132	floatrow\caption@setoptions figurerow\caption@setposition b
133	
134	\caption@setoptions figure\caption@setposition b![Image 8: Refer to caption](https://arxiv.org/html/2504.16828v5/x8.png)Figure 14:  Comparison to off-the-shelf PRMs trained on much more step labels than ThinkPRM. @​K@K represents parallel scaling by averaging scores over K CoTs.\caption@setoptions figure\caption@setposition b![Image 9: Refer to caption](https://arxiv.org/html/2504.16828v5/x9.png)Figure 17: Ablating the data filtering mechanism, where our process-based filtering yields better PRMs. LLM-as-a-judge is shown with number of beams = 16.
135	
136	### 4.2 Results
137	
138	#### ThinkPRM outperforms DiscPRM and LLM-as-a-Judge.
139	
140	Under best-of-N selection with MATH-500 shown in [Fig.11](https://arxiv.org/html/2504.16828v5#S4.F11 "In Tasks and Models. ‣ 4.1 Experimental Setup ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think") (right), ThinkPRM leads to higher or comparable reasoning accuracy to DiscPRM under all sampling budgets. The trend holds on the more challenging AIME ’24, shown in [Fig.11](https://arxiv.org/html/2504.16828v5#S4.F11 "In Tasks and Models. ‣ 4.1 Experimental Setup ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think") left. Additionally, [Fig.1](https://arxiv.org/html/2504.16828v5#S0.F1 "In Process Reward Models That Think") (right) shows beam search results on MATH-500, with ThinkPRM 1.5B surpassing DiscPRM and LLM-as-a-Judge.
141	
142	#### ThinkPRM surpasses off-the-shelf PRMs.
143	
144	We compare ThinkPRM-1.5B to two strong off-the-shelf PRMs, namely RLHFFlow-Deepseek-PRM (Xiong et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib50)) and MATH-Shepherd-PRM (Wang et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib46)). These PRMs are trained on even more data than PRM800K and are larger than 1.5B. We show results under verifier-guided search on MATH-500 in [Fig.17](https://arxiv.org/html/2504.16828v5#S4.F17 "In Scaling verifier compute. ‣ 4.1 Experimental Setup ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think"), with ThinkPRM-1.5B’s scaling curve surpassing all baselines and outperforming RLHFFlow-Deepseek-PRM, the best off-the-shelf PRM among the ones we tested, by more than 7% across all beam sizes.
145	
146	#### ThinkPRM excels on out-of-domain tasks.
147	
148	As for OOD performance on GPQA-physics ([Fig.18](https://arxiv.org/html/2504.16828v5#S4.F18 "In Parallel scaling vs. sequential scaling. ‣ 4.2 Results ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think") left), ThinkPRM scales better than DiscPRM—which drops substantially at N=32—outperforming it by 8%. On LiveCodeBench ([Fig.18](https://arxiv.org/html/2504.16828v5#S4.F18 "In Parallel scaling vs. sequential scaling. ‣ 4.2 Results ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think") right), ThinkPRM also outperforms DiscPRM by 4.5%. On LiveCodeBench, Qwen2.5-7B-Math-PRM (Zhang et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib60))—a discriminative PRM trained on substantial amount of process labels obtained from LLM-as-a-judge data and Monte Carlo rollouts—struggles when applied out-of-domain. Our results shed light on the fragility of discriminative PRMs under domain shifts in contrast with generative PRMs.
149	
150	#### Scaling ThinkPRM compute boosts performance.
151	
152	Under verifier-guided search (shown in [Fig.17](https://arxiv.org/html/2504.16828v5#S4.F17 "In Scaling verifier compute. ‣ 4.1 Experimental Setup ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think")), parallel scaling with ThinkPRM-1.5B@4 boosts the accuracy by more than 5% points, and yields the best accuracy on MATH-500. In addition, parallel scaling with ThinkPRM-14B@4 and ThinkPRM-14B@8 boosts best-of-N performance on MATH-500 as shown in [Fig.31](https://arxiv.org/html/2504.16828v5#A5.F31 "In E.5 MATH-500 test examples ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") in [Section E.6](https://arxiv.org/html/2504.16828v5#A5.SS6 "E.6 Additional results on scaling verifier compute ‣ Appendix E Evaluation details ‣ Process Reward Models That Think"). Now we move to sequential scaling of verifier compute by forcing ThinkPRM to recheck its own verification. Since this can be compute-intensive, we only run this on 200 problems from OmniMath subset of ProcessBench, and observe how verification F1 improves as we force the model to think for longer as shown in [Fig.2](https://arxiv.org/html/2504.16828v5#S1.F2 "In 1 Introduction ‣ Process Reward Models That Think"). ThinkPRM exhibits better scaling behavior compared to LLM-as-a-judge, which drops after 16K tokens, and outperforms DiscPRM-14B by 15 F1 points. In summary, ThinkPRM is consistently better than LLM-as-a-judge under parallel and sequential scaling.
153	
154	#### Parallel scaling vs. sequential scaling.
155	
156	Is it preferable to scale verifier compute in parallel or sequentially? We investigate this by comparing the two modes of scaling under the same token budget. [Fig.32](https://arxiv.org/html/2504.16828v5#A5.F32 "In E.6 Additional results on scaling verifier compute ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") in [Section E.6](https://arxiv.org/html/2504.16828v5#A5.SS6 "E.6 Additional results on scaling verifier compute ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") shows performance of best-of-N with Qwen-2.5-14B under parallel and sequential scaling with K=2,4 K=2,4 under both parallel scaling and sequential scaling. Overall, the performance of both methods is fairly close, but we observe a slight advantage to parallel scaling under certain budgets.
157	
158	![Image 10: Refer to caption](https://arxiv.org/html/2504.16828v5/x10.png)
159	
160	Figure 18: Best-of-N on two out-of-domain tasks: science QA (GPQA-Physics) and code generation (LiveCodeBench). Although ThinkPRM was only finetuned on math, it exhibits superior OOD performance than the baselines, especially at larger sampling budgets, where the baselines fall short. Discriminative PRMs struggle despite being trained on orders of magnitude more process labels.
161	
162	5 Analysis and Discussion
163	-------------------------
164	
165	### 5.1 Training data efficiency
166	
167	A major strength of ThinkPRM is training data efficiency compared to discriminative versions. Here, we study the training scaling behavior of ThinkPRM-14B by training it over 500 and 1K examples in total collected using the pipeline in [Section 3.2](https://arxiv.org/html/2504.16828v5#S3.SS2 "3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think"), which roughly corresponds to 4K and 8K process labels from PRM800K in total. We compare that to DiscPRM-14B trained with 1K, 10K, 50K and 98K examples, where 98K corresponds to training on the full PRM800K train set that includes 712K step labels. [Fig.1](https://arxiv.org/html/2504.16828v5#S0.F1 "In Process Reward Models That Think") (Left) contrasts the training data scaling behavior of ThinkPRM-14B with that of DiscPRM-14B, where ThinkPRM-14B’s performance scales substantially better with two orders of magnitude fewer process labels. This primarily stems from ThinkPRM’s utilization of text generation and reasoning abilities of the underlying models.
168	
169	While we train ThinkPRM using only 1K data points, we investigate whether it will benefit from training on more data. Using the pipeline, we collect and filter additional verification CoTs and obtain a total of 65K chains. We then finetune R1-Distill-Qwen-1.5B and R1-Distill-Qwen-14B on these for a single epoch while keeping all other training hyperparameters fixed. We then compare the resulting models to the 1K-trained version of ThinkPRM under best-of-N selection on MATH-500. [Figs.38](https://arxiv.org/html/2504.16828v5#A5.F38 "In E.7 Scaling training data of ThinkPRM ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") and[38](https://arxiv.org/html/2504.16828v5#A5.F38 "Fig. 38 ‣ E.7 Scaling training data of ThinkPRM ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") in [Section E.7](https://arxiv.org/html/2504.16828v5#A5.SS7 "E.7 Scaling training data of ThinkPRM ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") show a performance boost from training on the 65K examples compared to only 1K. This suggests that ThinkPRM can utilize more training data when available.
170	
171	### 5.2 Effect of Verification CoT Length on PRM Quality
172	
173	We study whether the length of verification chains of thought affects the quality of the resulting generative verifier. Specifically, we compare ThinkPRM trained on the full, long synthetic CoTs with a variant trained on short, compressed versions of the same 1K CoTs. To obtain the short CoTs, we instruct gpt-4o-mini to rewrite each original CoT into a concise version that preserves only the essential reasoning. We then train R1-Qwen-1.5B and R1-Qwen-14B on these short CoTs and evaluate verification F1 on ProcessBench. Table[1](https://arxiv.org/html/2504.16828v5#S5.T1 "Table 1 ‣ 5.2 Effect of Verification CoT Length on PRM Quality ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think") reports the comparison.
174	
175	Table 1: Verification F1 when training R1 models on long versus short CoTs.
176	
177	The substantial performance drop when training on short CoTs emphasizes how ThinkPRM benefits from extended reasoning. Since verification is a complex task, throwing more reasoning effort at it via thinking improves performance. These results support the value of using long verification CoTs for training.
178	
179	### 5.3 Reasoning traces without clear step boundaries
180	
181	So far, we have used ThinkPRM to verify short CoTs with clear steps delimiters. Here, we investigate whether ThinkPRM can still verify long CoTs that involve extended reasoning, backtracking, and self-correction. As a generator, we use Qwen3-1.7B (Yang et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib52)) with thinking mode. Although ThinkPRM was only trained on short solutions from PRM800K, it can still verify long CoTs and outperforms the baselines as shown in [Fig.19](https://arxiv.org/html/2504.16828v5#S5.F19 "In 5.5 ThinkPRM with Monte Carlo step labels ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think") left. Inspecting ThinkPRM’s outputs, we found that it extracts and verifies individual steps embedded in the long CoT—an example is in [Fig.45](https://arxiv.org/html/2504.16828v5#A7.F45 "In Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think").
182	
183	### 5.4 Compute-matched comparison to self-consistency
184	
185	Under a fixed test-time compute budget for best-of-N, how does ThinkPRM compare to simply sampling more solutions from the generator and applying majority voting? To investigate this, we conduct a compute-matched analysis on MATH-500 and GPQA-Physics. [Fig.19](https://arxiv.org/html/2504.16828v5#S5.F19 "In 5.5 ThinkPRM with Monte Carlo step labels ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think") mid and right plot solution accuracy as a function of sampling FLOPs for MATH-500 and GPQA-physics. At low sampling budgets, best-of-N with ThinkPRM performs comparably to self-consistency, but as the compute budget increases, ThinkPRM has a clear advantage. These findings agree with recent work on outcome reward models (Singhi et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib38)).
186	
187	### 5.5 ThinkPRM with Monte Carlo step labels
188	
189	To train ThinkPRM, we have relied on manual step labels from PRM800K. Since automatic labels e.g., via Monte Carlo rollouts Luo et al. ([2024](https://arxiv.org/html/2504.16828v5#bib.bib33)) are cheaper, we validate whether we can train ThinkPRM using automatic labels. We train ThinkPRM-1.5B using 1K synthetic chains based on labels from Math-shepherd dataset (Wang et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib46)). Performance on ProcessBench is shown in [Table 4](https://arxiv.org/html/2504.16828v5#A5.T4 "In E.8 Results with automatic labels ‣ Appendix E Evaluation details ‣ Process Reward Models That Think"), where training ThinkPRM with automatic labels yields very comparable performance to training with manual labels, showing that our training pipeline is agnostic to step-labeling strategy.
190	
191	![Image 11: Refer to caption](https://arxiv.org/html/2504.16828v5/x11.png)
192	
193	![Image 12: Refer to caption](https://arxiv.org/html/2504.16828v5/x12.png)
194	
195	![Image 13: Refer to caption](https://arxiv.org/html/2504.16828v5/x13.png)
196	
197	Figure 19: Left: Best-of-N with Qwen3-1.7B on the full MATH-500 test set, showing how ThinkPRM generalizes well to verifying long reasoning traces. Mid and Right: Compute-matched comparison between best-of-N with ThinkPRM and self-consistency or majority vote.
198	
199	### 5.6 ThinkPRM helps with difficult reasoning problems
200	
201	ThinkPRM’s reasoning ability should enable it to tackle verification of hard problems. To check if this is the case, we analyze performance of ThinkPRM vs. DiscPRM in light of problem difficulty over MATH-500 and GPQA-physics (how we estimate difficulty for GPQA-Physics is explained in [Section E.9](https://arxiv.org/html/2504.16828v5#A5.SS9 "E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think")), shown in [Fig.39](https://arxiv.org/html/2504.16828v5#A5.F39 "In E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think"). The generators here are Qwen-2.5-14B for MATH-500 and Qwen-2.5-32B-Instruct for GPQA-Physics. Primarily, ThinkPRM improves reasoning on the difficult problems (levels 3, 4, 5 in MATH-500 and 2, 3, 4 in GPQA-Physics) substantially more than DiscPRM.
202	
203	### 5.7 Filtering based on process vs. outcome labels
204	
205	In [Section 3.2](https://arxiv.org/html/2504.16828v5#S3.SS2 "3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think"), we describe our process-based filtering strategy, which selects verification CoTs based on agreement between generated step-level decisions and gold process labels. To validate its effectiveness, we compare it to outcome-based filtering, as in GenRM(Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)), which retains chains solely based on final answer correctness—keeping a CoT if its final answer is correct and the final step is \boxed{correct}, or if the answer is incorrect and the final step is \boxed{incorrect}, thereby ignoring intermediate step labels. We obtain 65K and 128K CoTs using process- and outcome-based filtering, respectively. [Fig.17](https://arxiv.org/html/2504.16828v5#S4.F17 "In Scaling verifier compute. ‣ 4.1 Experimental Setup ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think") shows that finetuning R1-Distill-Qwen-1.5B on process-filtered data yields significantly better verification performance, despite using fewer examples, which reflects the importance of our process-based filtering in training strong PRMs.
206	
207	### 5.8 Limitations of Generative PRMs
208	
209	While generative PRMs are more powerful and data-efficient than their discriminative counterparts, they come with some limitations that we highlight as avenues for future work. First, overconfidence is a known issue in LLMs(Liu et al., [2023a](https://arxiv.org/html/2504.16828v5#bib.bib31); Stechly et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib40); Zhou et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib63)) and, in the case of PRMs, it can cause the predicted PRM scores to cluster near extremes: close to either 0 or 1. One reason is that we are using probabilities of certain tokens such as “yes” or “no”, which by nature will be either very high or very low. Future work should explore more reliable techniques to extract calibrated scores from generative reward models. Another limitation is due to autoregressive nature of LLMs, leading them to prematurely commit to an earlier judgment. For example, we observe a phenomenon we term step label interference, where verification errors for earlier steps impact verification of later steps. For example, we noted that if the PRM judges a particular step as incorrect, it becomes more likely to label subsequent steps as incorrect even if it is not. Lastly, generating a verification CoT introduces extra overhead compared to discriminative PRMs, but we argue that the performance gains offered by generative PRMs justify this extra cost.
210	
211	Conclusion
212	----------
213	
214	We introduced ThinkPRM, a generative process reward model trained with minimal synthetic supervision for scalable step-by-step verification. With just 8K process labels, ThinkPRM significantly outperforms LLM-as-a-judge and even surpasses discriminative PRMs trained on orders of magnitude more data. These results highlight the benefits of generative PRMs in interpretability, scalability, and data efficiency, and demonstrate their potential to scale verification compute for complex reasoning tasks in math and science.
215	
216	References
217	----------
218	
219	*   Akyürek et al. (2024) Ekin Akyürek, Mehul Damani, Linlu Qiu, Han Guo, Yoon Kim, and Jacob Andreas. The surprising effectiveness of test-time training for abstract reasoning. _arXiv preprint arXiv:2411.07279_, 2024. 
220	*   Ankner et al. (2024) Zachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-loud reward models. _arXiv preprint arXiv:2408.11791_, 2024. 
221	*   Bavaresco et al. (2024) Anna Bavaresco, Raffaella Bernardi, Leonardo Bertolazzi, Desmond Elliott, Raquel Fernández, Albert Gatt, Esam Ghaleb, Mario Giulianelli, Michael Hanna, Alexander Koller, et al. Llms instead of human judges? a large scale empirical study across 20 nlp evaluation tasks. _arXiv preprint arXiv:2406.18403_, 2024. 
222	*   (4) Edward Beeching, Lewis Tunstall, and Sasha Rush. Scaling test-time compute with open models. URL [https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute). 
223	*   Brown et al. (2024) Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large language monkeys: Scaling inference compute with repeated sampling. _arXiv preprint arXiv:2407.21787_, 2024. 
224	*   Brown et al. (2020) Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_, 33:1877–1901, 2020. 
225	*   Charniak & Johnson (2005) Eugene Charniak and Mark Johnson. Coarse-to-fine n-best parsing and maxent discriminative reranking. In _Proceedings of the 43rd Annual Meeting of the Association for Computational Linguistics (ACL’05)_, pp. 173–180, 2005. 
226	*   Chen et al. (2024a) Guoxin Chen, Minpeng Liao, Chengxi Li, and Kai Fan. Alphamath almost zero: process supervision without process. _arXiv preprint arXiv:2405.03553_, 2024a. 
227	*   Chen et al. (2024b) Xingyu Chen, Jiahao Xu, Tian Liang, Zhiwei He, Jianhui Pang, Dian Yu, Linfeng Song, Qiuzhi Liu, Mengfei Zhou, Zhuosheng Zhang, et al. Do not think that much for 2+ 3=? on the overthinking of o1-like llms. _arXiv preprint arXiv:2412.21187_, 2024b. 
228	*   Chen et al. (2024c) Ziru Chen, Michael White, Raymond Mooney, Ali Payani, Yu Su, and Huan Sun. When is tree search useful for llm planning? it depends on the discriminator. _arXiv preprint arXiv:2402.10890_, 2024c. 
229	*   Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems. _arXiv preprint arXiv:2110.14168_, 2021. 
230	*   Cuadron et al. (2025) Alejandro Cuadron, Dacheng Li, Wenjie Ma, Xingyao Wang, Yichuan Wang, Siyuan Zhuang, Shu Liu, Luis Gaspar Schroeder, Tian Xia, Huanzhi Mao, et al. The danger of overthinking: Examining the reasoning-action dilemma in agentic tasks. _arXiv preprint arXiv:2502.08235_, 2025. 
231	*   Dong et al. (2023) Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative foundation model alignment. _arXiv preprint arXiv:2304.06767_, 2023. 
232	*   Gao et al. (2024) Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. _arXiv preprint arXiv:2410.07985_, 2024. 
233	*   Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. _arXiv preprint arXiv:2501.12948_, 2025. 
234	*   He et al. (2024) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. _arXiv preprint arXiv:2402.14008_, 2024. 
235	*   Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. _arXiv preprint arXiv:2103.03874_, 2021. 
236	*   Hu et al. (2022) Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, et al. Lora: Low-rank adaptation of large language models. _ICLR_, 1(2):3, 2022. 
237	*   Huang et al. (2023) Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. _arXiv preprint arXiv:2310.01798_, 2023. 
238	*   Hui et al. (2024) Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, et al. Qwen2. 5-coder technical report. _arXiv preprint arXiv:2409.12186_, 2024. 
239	*   Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. _arXiv preprint arXiv:2412.16720_, 2024. 
240	*   Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. _arXiv preprint arXiv:2403.07974_, 2024. 
241	*   Kalra & Tang (2025) Nimit Kalra and Leonard Tang. Verdict: A library for scaling judge-time compute. _arXiv preprint arXiv:2502.18018_, 2025. 
242	*   Kang et al. (2024) Yu Kang, Xianghui Sun, Liangyu Chen, and Wei Zou. C3ot: Generating shorter chain-of-thought without compromising effectiveness. _arXiv preprint arXiv:2412.11664_, 2024. 
243	*   Khalifa et al. (2023) Muhammad Khalifa, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, and Lu Wang. GRACE: discriminator-guided chain-of-thought reasoning. In Houda Bouamor, Juan Pino, and Kalika Bali (eds.), _Findings of the Association for Computational Linguistics: EMNLP 2023, Singapore, December 6-10, 2023_, pp. 15299–15328. Association for Computational Linguistics, 2023. doi: 10.18653/V1/2023.FINDINGS-EMNLP.1022. URL [https://doi.org/10.18653/v1/2023.findings-emnlp.1022](https://doi.org/10.18653/v1/2023.findings-emnlp.1022). 
244	*   Kim et al. (2023) Seungone Kim, Jamin Shin, Yejin Cho, Joel Jang, Shayne Longpre, Hwaran Lee, Sangdoo Yun, Seongjin Shin, Sungdong Kim, James Thorne, et al. Prometheus: Inducing fine-grained evaluation capability in language models. In _The Twelfth International Conference on Learning Representations_, 2023. 
245	*   Kumar et al. (2024) Aviral Kumar, Vincent Zhuang, Rishabh Agarwal, Yi Su, John D Co-Reyes, Avi Singh, Kate Baumli, Shariq Iqbal, Colton Bishop, Rebecca Roelofs, et al. Training language models to self-correct via reinforcement learning. _arXiv preprint arXiv:2409.12917_, 2024. 
246	*   Lambert et al. (2024) Nathan Lambert, Valentina Pyatkin, Jacob Morrison, LJ Miranda, Bill Yuchen Lin, Khyathi Chandu, Nouha Dziri, Sachin Kumar, Tom Zick, Yejin Choi, et al. Rewardbench: Evaluating reward models for language modeling. _arXiv preprint arXiv:2403.13787_, 2024. 
247	*   Li et al. (2023) Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu Chen. Making language models better reasoners with step-aware verifier. In _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pp. 5315–5333, 2023. 
248	*   Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. _arXiv preprint arXiv:2305.20050_, 2023. 
249	*   Liu et al. (2023a) Xin Liu, Muhammad Khalifa, and Lu Wang. Litcab: Lightweight language model calibration over short-and long-form responses. _arXiv preprint arXiv:2310.19208_, 2023a. 
250	*   Liu et al. (2023b) Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. G-eval: Nlg evaluation using gpt-4 with better human alignment. _arXiv preprint arXiv:2303.16634_, 2023b. 
251	*   Luo et al. (2024) Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve mathematical reasoning in language models by automated process supervision. _arXiv preprint arXiv:2406.06592_, 2, 2024. 
252	*   Mahan et al. (2024) Dakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative reward models. _arXiv preprint arXiv:2410.12832_, 2024. 
253	*   Muennighoff et al. (2025) Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto. s1: Simple test-time scaling. _arXiv preprint arXiv:2501.19393_, 2025. 
254	*   Rein et al. (2024) David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. Gpqa: A graduate-level google-proof q&a benchmark. In _First Conference on Language Modeling_, 2024. 
255	*   Singh et al. (2023) Avi Singh, John D Co-Reyes, Rishabh Agarwal, Ankesh Anand, Piyush Patil, Xavier Garcia, Peter J Liu, James Harrison, Jaehoon Lee, Kelvin Xu, et al. Beyond human data: Scaling self-training for problem-solving with language models. _arXiv preprint arXiv:2312.06585_, 2023. 
256	*   Singhi et al. (2025) Nishad Singhi, Hritik Bansal, Arian Hosseini, Aditya Grover, Kai-Wei Chang, Marcus Rohrbach, and Anna Rohrbach. When to solve, when to verify: Compute-optimal problem solving and generative verification for llm reasoning. _arXiv preprint arXiv:2504.01005_, 2025. 
257	*   Snell et al. (2024) Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling llm test-time compute optimally can be more effective than scaling model parameters. _arXiv preprint arXiv:2408.03314_, 2024. 
258	*   Stechly et al. (2023) Kaya Stechly, Matthew Marquez, and Subbarao Kambhampati. Gpt-4 doesn’t know it’s wrong: An analysis of iterative prompting for reasoning problems. _arXiv preprint arXiv:2310.12397_, 2023. 
259	*   Sun et al. (2024) Zhiqing Sun, Longhui Yu, Yikang Shen, Weiyang Liu, Yiming Yang, Sean Welleck, and Chuang Gan. Easy-to-hard generalization: Scalable alignment beyond human supervision. _arXiv preprint arXiv:2403.09472_, 2024. 
260	*   Team (2024) Qwen Team. Qwq: Reflect deeply on the boundaries of the unknown, November 2024. URL [https://qwenlm.github.io/blog/qwq-32b-preview/](https://qwenlm.github.io/blog/qwq-32b-preview/). 
261	*   Uesato et al. (2022) Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. _arXiv preprint arXiv:2211.14275_, 2022. 
262	*   Wan et al. (2024) Ziyu Wan, Xidong Feng, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, and Jun Wang. Alphazero-like tree-search can guide large language model decoding and training. In _Forty-first International Conference on Machine Learning_, 2024. 
263	*   Wang et al. (2023a) Jiaan Wang, Yunlong Liang, Fandong Meng, Haoxiang Shi, Zhixu Li, Jinan Xu, Jianfeng Qu, and Jie Zhou. Is chatgpt a good nlg evaluator? a preliminary study. _arXiv preprint arXiv:2303.04048_, 2023a. 
264	*   Wang et al. (2023b) Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Y Wu, and Zhifang Sui. Math-shepherd: A label-free step-by-step verifier for llms in mathematical reasoning. _arXiv preprint arXiv:2312.08935_, 2023b. 
265	*   Wang et al. (2024) Tianlu Wang, Ilia Kulikov, Olga Golovneva, Ping Yu, Weizhe Yuan, Jane Dwivedi-Yu, Richard Yuanzhe Pang, Maryam Fazel-Zarandi, Jason Weston, and Xian Li. Self-taught evaluators. _arXiv preprint arXiv:2408.02666_, 2024. 
266	*   Wang et al. (2022) Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. _arXiv preprint arXiv:2203.11171_, 2022. 
267	*   Wu et al. (2024) Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference scaling laws: An empirical analysis of compute-optimal inference for problem-solving with language models. _arXiv preprint arXiv:2408.00724_, 2024. 
268	*   Xiong et al. (2024) Wei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm. [https://github.com/RLHFlow/RLHF-Reward-Modeling](https://github.com/RLHFlow/RLHF-Reward-Modeling), 2024. 
269	*   Xiong et al. (2025) Wei Xiong, Hanning Zhang, Chenlu Ye, Lichang Chen, Nan Jiang, and Tong Zhang. Self-rewarding correction for mathematical reasoning. _arXiv preprint arXiv:2502.19613_, 2025. 
270	*   Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. _arXiv preprint arXiv:2505.09388_, 2025. 
271	*   Yao et al. (2023) Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. _Advances in neural information processing systems_, 36:11809–11822, 2023. 
272	*   Ye et al. (2024) Tian Ye, Zicheng Xu, Yuanzhi Li, and Zeyuan Allen-Zhu. Physics of language models: Part 2.2, how to learn from mistakes on grade-school math problems. _arXiv preprint arXiv:2408.16293_, 2024. 
273	*   Yu et al. (2024) Ping Yu, Jing Xu, Jason Weston, and Ilia Kulikov. Distilling system 2 into system 1. _arXiv preprint arXiv:2407.06023_, 2024. 
274	*   Yuan et al. (2024) Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free process rewards without process labels. _arXiv preprint arXiv:2412.01981_, 2024. 
275	*   Zelikman et al. (2022) Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah Goodman. Star: Bootstrapping reasoning with reasoning. _Advances in Neural Information Processing Systems_, 35:15476–15488, 2022. 
276	*   Zhang et al. (2024a) Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative verifiers: Reward modeling as next-token prediction. _arXiv preprint arXiv:2408.15240_, 2024a. 
277	*   Zhang et al. (2024b) Yunxiang Zhang, Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, Moontae Lee, Honglak Lee, and Lu Wang. Small language models need strong verifiers to self-correct reasoning. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), _Findings of the Association for Computational Linguistics, ACL 2024, Bangkok, Thailand and virtual meeting, August 11-16, 2024_, pp. 15637–15653. Association for Computational Linguistics, 2024b. doi: 10.18653/V1/2024.FINDINGS-ACL.924. URL [https://doi.org/10.18653/v1/2024.findings-acl.924](https://doi.org/10.18653/v1/2024.findings-acl.924). 
278	*   Zhang et al. (2025) Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The lessons of developing process reward models in mathematical reasoning. _arXiv preprint arXiv:2501.07301_, 2025. 
279	*   Zheng et al. (2024) Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. Processbench: Identifying process errors in mathematical reasoning. _arXiv preprint arXiv:2412.06559_, 2024. 
280	*   Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. _Advances in Neural Information Processing Systems_, 36:46595–46623, 2023. 
281	*   Zhou et al. (2024) Kaitlyn Zhou, Jena D Hwang, Xiang Ren, and Maarten Sap. Relying on the unreliable: The impact of language models’ reluctance to express uncertainty. _arXiv preprint arXiv:2401.06730_, 2024. 
282	*   Zhu et al. (2023) Lianghui Zhu, Xinggang Wang, and Xinlong Wang. Judgelm: Fine-tuned large language models are scalable judges. _arXiv preprint arXiv:2310.17631_, 2023. 
283	
284	Appendix A Training data
285	------------------------
286	
287	### A.1 Sampling
288	
289	[Fig.3](https://arxiv.org/html/2504.16828v5#S3.F3 "In 3 ThinkPRM ‣ Process Reward Models That Think") shows the prompt used with QwQ-32B-Preview to sample verification chains for training. We use the problem-prefix pairs from PRM800K train split (Lightman et al., [2023](https://arxiv.org/html/2504.16828v5#bib.bib30)), which is based on MATH (Hendrycks et al., [2021](https://arxiv.org/html/2504.16828v5#bib.bib17)). We sample 4 verification chains for each prefix in the dataset with temperature T=0.1 T=0.1 until we have 1K verification CoTs that (1) follow the desired format i.e., the model generated an extractable label for every step in the prefix and (2) the verbalized step labels match the gold labels in the PRM800K dataset annotation, (3) at most 4096 tokens long, and are (4) roughly balanced with respect to final answer correctness.
290	
291	Roughly 20% of the initial samples satisfied criteria 1 and 2 in our case, which means that about 5K samples in total are needed to obtain 1K filtered samples. [Table 2](https://arxiv.org/html/2504.16828v5#A1.T2 "In A.2 Preprocessing ‣ Appendix A Training data ‣ Process Reward Models That Think") shows the statistics of the final dataset. We also show an example from the 1K training CoTs in [Fig.20](https://arxiv.org/html/2504.16828v5#A1.F20 "In A.1 Sampling ‣ Appendix A Training data ‣ Process Reward Models That Think").
292	
293	Figure 20: Training example from our sampled 1K synthetic chains.
294	
295	### A.2 Preprocessing
296	
297	From the sampled verification CoTs, we extract boxed predictions (e.g., `\boxed{correct}` or `\boxed{incorrect}`) for each reasoning step. Then we filter the data as follows:
298	
299	*   •CoTs with missing or malformed verification decisions are discarded. 
300	*   •CoTs where verification decisions don’t match ground truth labels are filtered out. Precisely, we require all step-by-step verification decisions to match the ground truth labels. 
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5b63a05-1fff-4966-973d-e8e1041cfb66",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "7f61dce0-04e9-4817-80c9-98d36c2da2dd",
  "sourceToolAssistantUUID": "e5b63a05-1fff-4966-973d-e8e1041cfb66",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T17:48:27.509Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0114nxxErUr2PzhpDyG9V4nB`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2504.00891",
  "prompt": "Extract ALL ProcessBench F1 scores from tables in this paper. I need exact F1 numbers for GenPRM-1.5B, GenPRM-7B, GenPRM-72B, and all baseline models (Qwen2.5-Math-PRM-72B, GPT-4o, Math-Shepherd, ReasonEval, RLHFlow, etc). Include results with and without test-time scaling (majority voting @N). Extract all tables that mention ProcessBench."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f61dce0-04e9-4817-80c9-98d36c2da2dd",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVd1eYSY1oChfZadNMJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd213521-4a25-437e-aa42-c530131b4507",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2bCuWEfrmmuKbLidjkPW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2835,
      "cache_read_input_tokens": 11853,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 11853,
          "cache_creation_input_tokens": 2835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2835,
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

_source line 27 · 2026-05-27T17:48:30.982Z_

<details><summary>↩ Tool result · `toolu_0114nxxErUr2PzhpDyG9V4nB`</summary>

```text
I apologize, but I cannot extract the ProcessBench F1 scores you've requested from the provided content. The document appears to be a PDF file encoded in binary format (showing compressed stream objects with filter encodings), which makes it impossible to read the actual text and table contents directly.

To help you extract these scores, I would need:

1. **Plain text or readable format** of the paper, or
2. **A direct link** to the paper on arXiv or a similar source, or
3. **The specific table sections** provided in text form

If you can share the paper in a more accessible format or paste the relevant table data, I'd be happy to help you compile the exact F1 scores for GenPRM variants and baseline models on ProcessBench.

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/webfetch-1779904107524-emdn5p.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd213521-4a25-437e-aa42-c530131b4507",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "07cf13ad-3a87-4db8-b31c-3d25ca6cc3e9",
  "sourceToolAssistantUUID": "fd213521-4a25-437e-aa42-c530131b4507",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-27T17:48:36.246Z_

Let me continue reading the ThinkPRM paper for specific numbers and fetch the GenPRM HTML version and other sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07cf13ad-3a87-4db8-b31c-3d25ca6cc3e9",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVdjqp77RVjq8ws9rXe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13f97e09-2780-4622-ad70-8dbd7874b90a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9QKbZ5YroVCrvymRxSdgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24133,
      "cache_read_input_tokens": 14688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24133,
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

_source line 29 · 2026-05-27T17:48:38.179Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XboqVAgFPvH9ZbmNkcCtps`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01Ne49JCvEitDb59BrQ13qTY.txt",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13f97e09-2780-4622-ad70-8dbd7874b90a",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVdjqp77RVjq8ws9rXe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "512cb985-b104-4463-a29a-fd0a6f238550",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9QKbZ5YroVCrvymRxSdgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24133,
      "cache_read_input_tokens": 14688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24133,
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

_source line 30 · 2026-05-27T17:48:38.188Z_

<details><summary>↩ Tool result · `toolu_01XboqVAgFPvH9ZbmNkcCtps`</summary>

```text
300	*   •CoTs where verification decisions don’t match ground truth labels are filtered out. Precisely, we require all step-by-step verification decisions to match the ground truth labels. 
301	
302	Then we clean the data as follows:
303	
304	*   •We standardize boxed notation formats. 
305	*   •Content after the last verification decision is removed. 
306	*   •Special tokens (e.g., `&lt;think>` and `&lt;/think>`) are added to designate verification reasoning. 
307	
308	Table 2: Statistics of the 1K finetuning dataset.
309	
310	Correctness Distribution
311	# correct 486 (48.6%)
312	# incorrect 514 (51.4%)
313	Step label distribution
314	# correct 7474 (92.3%)
315	# Incorrect 625 (7.7%)
316	Prefix statistics
317	# unique questions 869
318	average steps per prefix 9.5
319	min # steps 1
320	max # steps 53
321	Verification Chain Statistics
322	Average verification chain length (tokens)1037.0
323	Min verification chain length (tokens)207
324	Max verification chain length (tokens)3669
325	
326	Figure 21: Prompt used to generate synthetic verification chains as described in [Section 3.2](https://arxiv.org/html/2504.16828v5#S3.SS2 "3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think").
327	
328	Appendix B LLM-as-a-Judge Limitations
329	-------------------------------------
330	
331	We show examples of failures from QwQ-32B-Preview and Deepseek-R1-Distill-Qwen-14B when used for LLM-as-judge verification in [Figs.23](https://arxiv.org/html/2504.16828v5#A2.F23 "In Appendix B LLM-as-a-Judge Limitations ‣ Process Reward Models That Think") and[25](https://arxiv.org/html/2504.16828v5#A2.F25 "Fig. 25 ‣ Appendix B LLM-as-a-Judge Limitations ‣ Process Reward Models That Think").
332	
333	Figure 22: Degeneration behavior from QwQ-32B-Preview with LLM-as-judge verification. Problem and solution are omitted for brevity.
334	
335	Figure 23: Degeneration behavior from Deepseek-R1-Distill-Qwen-14B with LLM-as-judge verification. Problem and solution are omitted for brevity.
336	
337	Figure 24: An example of problem and solution from OmniMath subset of ProcessBench.
338	
339	Figure 25: Incorrect verification by Deepseek-R1-Distill-Qwen-14B for the problem-solution pair in [Fig.24](https://arxiv.org/html/2504.16828v5#A2.F24 "In Appendix B LLM-as-a-Judge Limitations ‣ Process Reward Models That Think").
340	
341	Appendix C Training details
342	---------------------------
343	
344	### C.1 Training ThinkPRM
345	
346	We train our models on the filtered 1K chains using LoRA (Hu et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib18)) with rank r=32 r=32 and α=16\alpha=16. Specifically, we finetune Qwen-14B-Instruct and R1-Deepseek (14B) for 3 epochs, and QwQ-32B-Preview for 5 epochs using LoRA. We use an effective batch size of 16 and a fixed learning rate of 4×10−4 4\times 10^{-4} without warmup is used. Training took 1.5 hours for the 14B models and 4.5 hours for QwQ-32B-Preview on a single A100 80GB GPU. Without particularly found QwQ to be hard to train with LoRA and still generates a relatively high percentage of invalid judgments after training. Full training of the model will likely resolve these issues but that would require more compute than we have.
347	
348	The R1-Distill-Qwen{1.5B,7B} models use full training with the following parameters. The 1.5B model We trained for 3 epochs with an effective batch size of 32, using a constant learning rate of 6×10−5 6\times 10^{-5} without decay or warmup. We train both models using four RTX A6000 48GB GPU using data parallel. Training the 1.5B model on the 1K chains took about half an hour and the 7B model about two hours.
349	
350	### C.2 Training Discriminative Verifiers
351	
352	We train R1-Qwen-14B for 1 epoch over the entire PRM800K dataset using two A100 80GB GPUs with a batch size of 8 and a learning rate of 6×10−5 6\times 10^{-5}. We use a constant learning rate scheduler with no warmup. Following prior work (Wang et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib46); Zhang et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib60)) We train the model using binary cross-entropy to maximize the probability of the tokens “+” and “-” for correct and incorrect steps, respectively. The R1-Qwen-1.5B model is trained with the same infrastructure with a batch size of 64 and a learning rate of 1×10−4 1\times 10^{-4} with a warm up ratio of 10%.
353	
354	Appendix D Results on ProcessBench before and after finetuning
355	--------------------------------------------------------------
356	
357	[Table 3](https://arxiv.org/html/2504.16828v5#A4.T3 "In Appendix D Results on ProcessBench before and after finetuning ‣ Process Reward Models That Think") shows the performance numbers of LLM-as-a-Judge and ThinkPRM on ProcessBench.
358	
359	Table 3: Average F1-score on OlympiadBench and OmniMath subsets of ProcessBench (Zheng et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib61)) comparing LLM-as-a-Judge to ThinkPRM finetuned on 1K examples. Random baseline for OlympiadBench is 39.1% and for OmniMath is 32.7%. Percentage of bad outputs (repetitions, invalid label formatting, overthinking, etc.) are shown in red. LLM-as-a-judge with reasoning models suffer from issues that limits their utility as generative verifiers. 
360	
361	Appendix E Evaluation details
362	-----------------------------
363	
364	This section includes exact details on the test-time scaling shown in [Section 4.2](https://arxiv.org/html/2504.16828v5#S4.SS2 "4.2 Results ‣ 4 Test-time Scaling Experiments ‣ Process Reward Models That Think")
365	
366	### E.1 Predicting verification labels
367	
368	Following prior work (Snell et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib39); [Beeching et al.,](https://arxiv.org/html/2504.16828v5#bib.bib4)), we aggregate scores from DiscPRM by using the score of the last step. For ThinkPRM, we first prompt the model to generate the verification chain up to a maximum of 8192 tokens, then we force decode the string “Is the solution correct?” and use P​(“yes”)P​(“yes”)+P​(“no”)\frac{P(\text{``yes"})}{P(\text{``yes"})+P(\text{``no"})} as the solution score.
369	
370	### E.2 Best-of-N selection
371	
372	We sample solutions using a temperature of T=0.8 T=0.8 for Llama-3.2-3B-Instruct and T=0.4 T=0.4 for Qwen-2.5-14B. We instruct all models to think step by step and put the final answer in `\boxed{}`. All our Best-of-N experiments use weighted majority voting, which scores final answers based on the sum of the verifier scores of their solutions (Uesato et al., [2022](https://arxiv.org/html/2504.16828v5#bib.bib43); Wu et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib49); Sun et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib41))except for our experiments on AIME ’24, where we use the verifier score directly to rank the solution, as we found this to perform better for all verifiers.
373	
374	### E.3 Verifier-guided beam search
375	
376	Under verifier-guided beam search, we sample candidate next steps and score them with the process verifier, then selects top-K K out of these to further expand and so on. Our implementation is based on (Snell et al., [2024](https://arxiv.org/html/2504.16828v5#bib.bib39); [Beeching et al.,](https://arxiv.org/html/2504.16828v5#bib.bib4)), which maintains N N beams in total, and samples M M candidate next steps per beam. We set M=4 M=4 for all experiments and run search for a maximum of 20 steps per beam. To sample next steps, we use T=0.6 T=0.6 and use double newlines as the step delimiter.
377	
378	### E.4 Sequential scaling of verifier compute
379	
380	We achieve budget forcing (Muennighoff et al., [2025](https://arxiv.org/html/2504.16828v5#bib.bib35)) by triggering the model to think again for R R rounds, where each round uses a unique trigger phrase that incites the model to revisit or double-check its earlier verification. We use different trigger phrases for each round since we found that using the same phrase causes the model to repeat what it did in the last round.
381	
382	We do a maximum of R=4 R=4 thinking rounds, and use the phrases “Let me double check”, “Let’s verify again”, and “Did I miss something?”, for rounds 2, 3, and 4 respectively. We do not investigate deeply into optimizing the trigger phrase, but we note that performance may depend on these and we use the same phrases for both ThinkPRM and LLM-as-a-judge to ensure fair comparison.
383	
384	### E.5 MATH-500 test examples
385	
386	As running on all 500 examples from MATH-500 will require a lot of compute, we run all our experiments on 100 randomly sampled subsets from MATH-500 (Hendrycks et al., [2021](https://arxiv.org/html/2504.16828v5#bib.bib17)). We pick the 100 problems such that they cover different difficulty levels, as shown in [Fig.31](https://arxiv.org/html/2504.16828v5#A5.F31 "In E.5 MATH-500 test examples ‣ Appendix E Evaluation details ‣ Process Reward Models That Think").
387	
388	\caption@setoptions
389	
390	floatrow\caption@setoptions figurerow\caption@setposition b
391	
392	\caption@setoptions figure\caption@setposition b![Image 14: Refer to caption](https://arxiv.org/html/2504.16828v5/x14.png)Figure 28: Histogram of difficulty levels in our 100-problem subset from MATH-500.\caption@setoptions figure\caption@setposition b![Image 15: Refer to caption](https://arxiv.org/html/2504.16828v5/x15.png)Figure 31: Scaling of verifier compute by parallel sampling of multiple verification CoTs and averaging their scores. Parallel scaling (ThinkPRM-14B@4 and ThinkPRM-14B@8) further boosts performance curve compared to scoring based on a single CoT (ThinkPRM-14B).
393	
394	### E.6 Additional results on scaling verifier compute
395	
396	[Fig.31](https://arxiv.org/html/2504.16828v5#A5.F31 "In E.5 MATH-500 test examples ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") shows results of ThinkPRM-14B of parallel scaling verifier compute by sampling K=4 K=4 and K=8 K=8 CoTs with temperature T=0.6 T=0.6 and aggregating their scores. Parallel scaling indeed lifts up the accuracy curve of ThinkPRM-14B compared to standard K=1 K=1 with greedy decoding. However, performance plateaus rather quickly and K=8 K=8 remains comparable to K=4 K=4, while slightly better at smaller sampling budgets. [Fig.32](https://arxiv.org/html/2504.16828v5#A5.F32 "In E.6 Additional results on scaling verifier compute ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") compares parallel to sequential scaling under the same token budget. While there is no clear winner, parallel scaling seems to perform slightly better at best-of-8.
397	
398	\caption@setoptions
399	
400	floatrow\caption@setoptions figurerow\caption@setposition b
401	
402	![Image 16: [Uncaptioned image]](https://arxiv.org/html/2504.16828v5/x16.png)![Image 17: [Uncaptioned image]](https://arxiv.org/html/2504.16828v5/x17.png)Figure 32: Parallel vs. sequential scaling of ThinkPRM compute under the same generation budget with Qwen-2.5-14B generator. Parallel scaling (model@K) is done by independently sampling K K verification CoTs and aggregating their scores. Sequential scaling is done by prompting the model K K times to revise its own verification for K K thinking rounds. Both setups generate up until 8192 tokens per generation. We do not observe a clear winner although parallel scaling seems slightly better especially at larger sampling budgets.
403	
404	### E.7 Scaling training data of ThinkPRM
405	
406	Here, we show results when training ThinkPRM-14B and ThinkPRM-1.5B using synthetic data from all PRM800K. The goal is to show that ThinkPRM can still benefit from training on more synthetic data. Here, we train both R1-Distill-Qwen-1.5B and R1-Distill-Qwen-14B on a total of 65K verification CoTs we obtained by sampling and filtering as explained in [Section 3.2](https://arxiv.org/html/2504.16828v5#S3.SS2 "3.2 Finetuning on synthetic data boosts LLM-as-a-judge verification ‣ 3 ThinkPRM ‣ Process Reward Models That Think"). [Figs.38](https://arxiv.org/html/2504.16828v5#A5.F38 "In E.7 Scaling training data of ThinkPRM ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") and[38](https://arxiv.org/html/2504.16828v5#A5.F38 "Fig. 38 ‣ E.7 Scaling training data of ThinkPRM ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") show best-of-N performance with ThinkPRM-1.5B and ThinkPRM-14B respectively when trained on 65K and compares it to training on 1K examples. Interestingly, ThinkPRM benefits from additional training, and can further improve the accuracy curve compared to the 1K-trained version on MATH-500. We note, however, that while training on more math data boosts performance on MATH-500, we observe some performance drop on out-of-domain tasks due to the distribution shift.
407	
408	\caption@setoptions
409	
410	floatrow\caption@setoptions figurerow\caption@setposition b
411	
412	\caption@setoptions figure\caption@setposition b![Image 18: Refer to caption](https://arxiv.org/html/2504.16828v5/x18.png)Figure 35: Best-of-N results with ThinkPRM-1.5B comparing the version trained on 1K examples (used throughout the paper) and a version trained on 65K examples. ThinkPRM benefits from training on more synthetic data as the performance can further improve with more training. \caption@setoptions figure\caption@setposition b![Image 19: Refer to caption](https://arxiv.org/html/2504.16828v5/x19.png)Figure 38: Best-of-N results with ThinkPRM-14B comparing the version trained on 1K examples (used throughout the paper) and a version trained on 65K examples. ThinkPRM benefits from training on more synthetic data as the performance can further improve with more training.
413	
414	### E.8 Results with automatic labels
415	
416	[Table 4](https://arxiv.org/html/2504.16828v5#A5.T4 "In E.8 Results with automatic labels ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") shows performance when filtering training data based on manual labels (PRM800K) vs automatic labels (Math-Shepherd) (Wang et al., [2023b](https://arxiv.org/html/2504.16828v5#bib.bib46)). ThinkPRM still performs well even with automatic labels, and comparably to manual labels.
417	
418	Table 4: Comparison of ThinkPRM-1.5B trained on PRM800K vs Math-shepherd step labels.
419	
420	### E.9 Verifier performance in terms of problem difficulty
421	
422	![Image 20: Refer to caption](https://arxiv.org/html/2504.16828v5/x20.png)
423	
424	Figure 39: ThinkPRM helps with challenging reasoning problems compared to DiscPRM. The generator model here is Qwen-2.5-14B for MATH-500 and Qwen-2.5-32B-Instruct for GPQA. 
425	
426	We the difficulty We do not estimate the difficulty over MATH problem since each problem in MATH is annotated based on 1 of 5 difficulty levels. For GPQA-Physics problems, we first compute the pass@1 rate of Qwen2.5-32B-Instruct for every problem by sampling 32 solutions for each problem. Then, we bin the pass@1 rates into four different bins and use the bin assignment for each problem as the difficulty level. As discussed in [Section 5.6](https://arxiv.org/html/2504.16828v5#S5.SS6 "5.6 ThinkPRM helps with difficult reasoning problems ‣ 5 Analysis and Discussion ‣ Process Reward Models That Think"), [Fig.39](https://arxiv.org/html/2504.16828v5#A5.F39 "In E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") show how ThinkPRM helps more with verifying hard problems compared to DiscPRM.
427	
428	Table 5: F1-score on OlympiadBench and OmniMath subsets from ProcessBench with different prompts. Ratio of invalid judgments is shown in red.
429	
430	Appendix F More details on LLM-as-judge verification
431	----------------------------------------------------
432	
433	The instruction used for LLM-as-judge verification in [Section 3.1](https://arxiv.org/html/2504.16828v5#S3.SS1 "3.1 LLM-as-a-judge PRMs are suboptimal ‣ 3 ThinkPRM ‣ Process Reward Models That Think") is shown in [Fig.42](https://arxiv.org/html/2504.16828v5#A6.F42 "In Appendix F More details on LLM-as-judge verification ‣ Process Reward Models That Think"), which we refer to as Single-label. [Table 5](https://arxiv.org/html/2504.16828v5#A5.T5 "In E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") shows performance of QwQ-32B-Preview and Qwen-Deepseek-R1-14B with two more instructions. Bad-step-index refers to instructing the model to find the index of the first incorrect step and then if a step is found generate a single yes/no label regarding the solution correctness. Decision-for-each-step instructs the model to critique and produce a boxed label for each step. This instruction is shown in [Fig.21](https://arxiv.org/html/2504.16828v5#A1.F21 "In A.2 Preprocessing ‣ Appendix A Training data ‣ Process Reward Models That Think"). We observe high ha variance in verification performance and invalid judgment ratio depending on the prompt.
434	
435	Figure 42: Prompt used for LLM-as-a-judge verification in [Section 3.1](https://arxiv.org/html/2504.16828v5#S3.SS1 "3.1 LLM-as-a-judge PRMs are suboptimal ‣ 3 ThinkPRM ‣ Process Reward Models That Think")
436	
437	We also an example from ProcessBench in [Fig.40](https://arxiv.org/html/2504.16828v5#A5.F40 "In E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think") and the generated verification chain from QwQ-32B-Preview in [Fig.41](https://arxiv.org/html/2504.16828v5#A5.F41 "In E.9 Verifier performance in terms of problem difficulty ‣ Appendix E Evaluation details ‣ Process Reward Models That Think").
438	
439	Appendix G Examples from ThinkPRM
440	---------------------------------
441	
442	[Fig.44](https://arxiv.org/html/2504.16828v5#A7.F44 "In Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think") shows an example of a verification CoT from ThinkPRM-14B on a problem and solution from the OmniMath subset in ProcessBench, shown in [Fig.43](https://arxiv.org/html/2504.16828v5#A7.F43 "In Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think").
443	
444	Figure 43: Problem and solution from the OmniMath subset of ProcessBench. The verification CoT output by ThinkPRM is shown in [Fig.44](https://arxiv.org/html/2504.16828v5#A7.F44 "In Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think")
445	
446	Figure 44: Example output by ThinkPRM-14B, where it verifies and labels every step in the provided prefix via a long verification CoT. The problem and solution are in [Fig.43](https://arxiv.org/html/2504.16828v5#A7.F43 "In Appendix G Examples from ThinkPRM ‣ Process Reward Models That Think")
447	
448	Figure 45: Example of verification of long CoT solution from Qwen3-1.7B-thinking using ThinkPRM-1.5B. ThinkPRM extracts and verifies individual steps embedded in the long CoT.
449	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "512cb985-b104-4463-a29a-fd0a6f238550",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "c241be6d-74d4-487d-974a-747c0d730d5e",
  "sourceToolAssistantUUID": "512cb985-b104-4463-a29a-fd0a6f238550",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-27T17:48:42.598Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rrx92xFsxoUdrhXSAaTCbx`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.00891v2",
  "prompt": "Extract ALL ProcessBench F1 scores from ALL tables. I need exact F1 numbers for GenPRM-1.5B, GenPRM-7B, GenPRM-72B and all baseline models including Qwen2.5-Math-PRM-72B, GPT-4o, Math-Shepherd-PRM-7B, ReasonEval-7B, RLHFlow-Deepseek-PRM-8B, o1-mini, QwQ-32B-Preview. Include results with majority voting @1, @4, @8, @16 etc. Look for tables with columns like GSM8K, MATH, Olympiad, OmniMATH, Average."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c241be6d-74d4-487d-974a-747c0d730d5e",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVdjqp77RVjq8ws9rXe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "282843c0-7185-45f8-8244-61ee469ee28d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9QKbZ5YroVCrvymRxSdgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24133,
      "cache_read_input_tokens": 14688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24133,
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

_source line 32 · 2026-05-27T17:48:42.605Z_

<details><summary>↩ Tool result · `toolu_01Rrx92xFsxoUdrhXSAaTCbx`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "282843c0-7185-45f8-8244-61ee469ee28d",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "cf32423f-5bcb-41be-96e9-730c4ac50b00",
  "sourceToolAssistantUUID": "282843c0-7185-45f8-8244-61ee469ee28d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T17:48:44.371Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018f25b2WPRuHNtZ85czhtDX`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.21295v1",
  "prompt": "Extract ALL ProcessBench F1 scores reported in this R-PRM paper. List every model and its exact F1 score on ProcessBench, including all subsets (GSM8K, MATH, OlympiadBench, OmniMATH) and averages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf32423f-5bcb-41be-96e9-730c4ac50b00",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVdjqp77RVjq8ws9rXe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e65d7d8-741c-48eb-bab0-9fdee00fe3ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9QKbZ5YroVCrvymRxSdgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24133,
      "cache_read_input_tokens": 14688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24133,
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

_source line 34 · 2026-05-27T17:48:45.016Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5vNHBeS2WvQfVr3wVPaM5`</summary>

```json
{
  "query": "ProcessBench F1 scores table GenPRM 1.5B 7B comparison 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e65d7d8-741c-48eb-bab0-9fdee00fe3ef",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVdjqp77RVjq8ws9rXe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c519d3c-fe78-4807-82bc-3ae0fe830975",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9QKbZ5YroVCrvymRxSdgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24133,
      "cache_read_input_tokens": 14688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24133,
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

_source line 35 · 2026-05-27T17:48:51.210Z_

<details><summary>↩ Tool result · `toolu_01K5vNHBeS2WvQfVr3wVPaM5`</summary>

```text
Web search results for query: "ProcessBench F1 scores table GenPRM 1.5B 7B comparison 2025"

Links: [{"title":"2025-4-8 GenPRM: Scaling Test-Time Compute of Process","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"GenPRM/GenPRM-1.5B · Hugging Face","url":"https://huggingface.co/GenPRM/GenPRM-1.5B"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/pdf/2506.03570"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"}]

Based on the search results, I found information about GenPRM's F1 scores on ProcessBench:

## Key Findings:

The 7B GenPRM model surpasses Qwen2.5-Math-PRM-72B (which is 10x larger) on average F1 score when using test-time scaling. Additionally, the 1.5B GenPRM model outperforms GPT-4o on MATH, OlympiadBench, and Omni-MATH when using test-time scaling (Maj@8).

The research paper includes Table 1: ProcessBench results reported with F1 scores, though the specific numerical F1 scores from the table are not fully visible in the search results. However, the results indicate that GenPRM-7B significantly outperforms direct generative PRM and surpasses all previous PRMs with parameters less than 72B on ProcessBench.

For more detailed F1 score numbers from Table 1, you would need to access the full paper directly at https://arxiv.org/pdf/2504.00891.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c519d3c-fe78-4807-82bc-3ae0fe830975",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "55fd89eb-05d5-4a8c-b87d-bc618aaafe90",
  "sourceToolAssistantUUID": "7c519d3c-fe78-4807-82bc-3ae0fe830975",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T17:48:51.699Z_

<details><summary>↩ Tool result · `toolu_018f25b2WPRuHNtZ85czhtDX`</summary>

```text
# ProcessBench F1 Scores from R-PRM Paper

Based on Table 1, here are all reported F1 scores on ProcessBench:

## LLM-as-Judge (Proprietary)
- GPT-4o: 79.2 (error), 63.6 (correct), 51.4 (F1), 53.5 (avg)
- o1-mini: 93.2, 88.9, 87.2, 82.4 (avg)

## LLM-as-Judge (Open-source)
- Llama-3.3-70B-Instruct: 82.9, 59.4, 46.7, 43.0 (avg)
- Qwen2.5-Math-72B-Instruct: 65.8, 52.1, 32.5, 31.7 (avg)
- Qwen2.5-72B-Instruct: 76.2, 61.8, 54.6, 52.2 (avg)

## Process Reward Models
- Math-Shepherd-7B: 47.9, 29.5, 24.8, 23.8 (avg)
- Math-PSA-7B: 62.4, 41.9, 31.5, 25.2 (avg)
- RLHFlow-Mistral-8B: 50.4, 33.4, 13.8, 15.8 (avg)
- RLHFlow-DeepSeek-8B: 38.8, 33.8, 16.9, 16.9 (avg)
- Llemma-PRM800K-7B: 48.4, 43.1, 28.5, 33.4 (avg)
- Skywork-PRM-7B: 70.8, 53.6, 22.9, 21.0 (avg)
- ReasonEval-7B: 41.0, 48.9, 36.7, 37.4 (avg)
- Qwen2.5-Math-7B-PRM800K: 68.2, 62.6, 50.7, 44.3 (avg)
- Qwen2.5-Math-PRM-7B: 82.4, 77.6, 67.5, 66.3 (avg)

## R-PRM (Proposed Method)
- **R-PRM-7B-SFT: 77.2, 71.6, 59.6, 52.3 (avg: 65.2)**
- **R-PRM-7B-DPO: 80.7, 76.9, 63.8, 60.1 (avg: 70.4)**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e65d7d8-741c-48eb-bab0-9fdee00fe3ef",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "d1100ca9-08db-464a-ae0b-43e513c94614",
  "sourceToolAssistantUUID": "6e65d7d8-741c-48eb-bab0-9fdee00fe3ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-27T17:48:54.895Z_

Excellent, I got detailed R-PRM numbers. Now let me get the GenPRM specific numbers and search for more recent papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1100ca9-08db-464a-ae0b-43e513c94614",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVfGTqVLSyWVejRKunf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "329451f2-3821-4988-aebf-3046f4fc4a74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vJBXQzciR7zyET4yVzuE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 38821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7623,
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

_source line 38 · 2026-05-27T17:48:57.262Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LvhjPFHsgCiZqbpXyasiTH`</summary>

```json
{
  "url": "https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward",
  "prompt": "Extract ALL ProcessBench F1 scores from Table 1 and any other tables. I need exact F1 numbers for GenPRM-1.5B, GenPRM-7B, GenPRM-72B at different majority voting settings (@1, @4, @8, @16). Also extract all baseline model scores. Include columns for GSM8K, MATH, OlympiadBench, OmniMATH, and Average."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "329451f2-3821-4988-aebf-3046f4fc4a74",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVfGTqVLSyWVejRKunf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "008347ca-8d0e-49db-ba2c-ed957c1cfa77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vJBXQzciR7zyET4yVzuE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 38821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7623,
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

_source line 39 · 2026-05-27T17:48:57.490Z_

<details><summary>↩ Tool result · `toolu_01LvhjPFHsgCiZqbpXyasiTH`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "008347ca-8d0e-49db-ba2c-ed957c1cfa77",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "1720a896-38d4-4eb7-876a-c09cb658f2d1",
  "sourceToolAssistantUUID": "008347ca-8d0e-49db-ba2c-ed957c1cfa77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T17:48:59.322Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017LdAE1m1w6vtig7K1iMDyb`</summary>

```json
{
  "url": "https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e",
  "prompt": "Extract ALL ProcessBench F1 scores mentioned in this article. I need exact numbers for GenPRM-1.5B, GenPRM-7B, GenPRM-72B and all baselines. Include any tables with F1 scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1720a896-38d4-4eb7-876a-c09cb658f2d1",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVfGTqVLSyWVejRKunf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e612e6f4-e281-4819-bef8-71b1649bd108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vJBXQzciR7zyET4yVzuE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 38821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7623,
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

_source line 41 · 2026-05-27T17:48:59.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AwLiPCmwzqUy9V8M9TqYTz`</summary>

```json
{
  "query": "process reward model benchmark PRMBench evaluation 2025 2026 new benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e612e6f4-e281-4819-bef8-71b1649bd108",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVfGTqVLSyWVejRKunf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d607cb1f-4a7a-4b80-bbd3-8f01a9e9a281",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vJBXQzciR7zyET4yVzuE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 38821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7623,
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

_source line 42 · 2026-05-27T17:48:59.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011snSKhhTaPzNiL59brR6mP`</summary>

```json
{
  "query": "\"ProcessBench\" \"F1\" site:arxiv.org 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d607cb1f-4a7a-4b80-bbd3-8f01a9e9a281",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVfGTqVLSyWVejRKunf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fce8d58-9bc8-4dd7-9197-2df890f2d2cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vJBXQzciR7zyET4yVzuE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 38821,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7623
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 739,
          "output_tokens": 493,
          "cache_read_input_tokens": 38821,
          "cache_creation_input_tokens": 7623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7623,
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

_source line 43 · 2026-05-27T17:49:03.567Z_

<details><summary>↩ Tool result · `toolu_017LdAE1m1w6vtig7K1iMDyb`</summary>

```text
# ProcessBench F1 Scores

Unfortunately, the article does not provide specific numerical F1 scores in the text. The author states: "Table below shows ProcessBench results reported with F1 scores" but the actual table data with numbers is not included in the provided content—only a placeholder indicating where a figure should appear.

The article mentions that "GenPRM-7B significantly outperforms direct generative PRM and surpasses all previous PRMs with parameters less than 72B on ProcessBench" and notes achievements like smaller variants exceeding larger models through test-time scaling, but exact F1 score values are not provided in this web page excerpt.

**To access the actual numerical results**, you would need to:
- Consult the original paper at https://arxiv.org/abs/2504.00891
- Review the figures/tables directly in the full Medium article
- Check the referenced GitHub repository
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e612e6f4-e281-4819-bef8-71b1649bd108",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "ef262b1b-dc62-46d0-9b86-18c983fdf539",
  "sourceToolAssistantUUID": "e612e6f4-e281-4819-bef8-71b1649bd108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-27T17:49:06.541Z_

<details><summary>↩ Tool result · `toolu_011snSKhhTaPzNiL59brR6mP`</summary>

```text
Web search results for query: ""ProcessBench" "F1" site:arxiv.org 2025"

Links: [{"title":"arXiv:2505.11966v1 [cs.AI] 17 May 2025","url":"https://arxiv.org/pdf/2505.11966"},{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"Spark: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/html/2512.03244"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/html/2504.10559"},{"title":"2025-4-8 GenPRM: Scaling Test-Time Compute of Process","url":"https://arxiv.org/pdf/2504.00891"}]

Based on the search results, here's what I found about ProcessBench and F1 scores from recent arxiv papers in 2025:

## Overview

ProcessBench (Zheng et al., 2024) is designed to assess the ability to identify erroneous steps in mathematical reasoning processes. The dataset comprises 3,400 test cases covering mathematical problems of varying difficulty levels, with each test case including a question accompanied by an LLM generated step-by-step solution, and the earliest incorrect step meticulously annotated by human experts.

## F1 Score Metric

F1 scores represent the harmonic mean of accuracies on correct and incorrect solutions to balance over-criticism and under-detection of errors. Performance is measured using the F1 score for identifying the first erroneous step.

## Recent Results

Several 2025 papers report state-of-the-art F1 scores on ProcessBench:

- ActPRM-X achieves a new SOTA performance on ProcessBench with an average F1 of 0.760, outperforming the second-place model (Universal-PRM) with a margin of 1.7%.

- PRMs trained with synthetic data achieve 67.5 F1, outperforming those trained with outcome ground-truth access (66.4 F1).

- An SFT approach achieves F1 scores of 65.2 on ProcessBench, representing significant improvements over state-of-the-art baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fce8d58-9bc8-4dd7-9197-2df890f2d2cc",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "0b7a4786-dad0-4b25-b54b-c9b75cf2d6ff",
  "sourceToolAssistantUUID": "1fce8d58-9bc8-4dd7-9197-2df890f2d2cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-27T17:49:06.790Z_

<details><summary>↩ Tool result · `toolu_01AwLiPCmwzqUy9V8M9TqYTz`</summary>

```text
Web search results for query: "process reward model benchmark PRMBench evaluation 2025 2026 new benchmarks"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1230/"},{"title":"[2501.03124v2] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124v2"},{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://arxiv.org/html/2601.12294v1"},{"title":"GitHub - ssmisya/PRMBench: [ACL' 25] The official code repository for PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models.","url":"https://github.com/ssmisya/PRMBench"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"}]

Based on the search results, I found comprehensive information about PRMBench and related process reward model benchmarks:

## PRMBench: A Fine-grained and Challenging Benchmark

PRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity. Process-level Reward Models (PRMs) are crucial for complex reasoning and decision-making tasks, where each intermediate step plays an important role in the reasoning process.

PRMBench systematically assesses the performance of PRMs across diverse error categories, including simplicity, soundness, and sensitivity, and includes 6,216 fine-grained data instances spreading across three major evaluation categories and nine sub-categories, whose quality is ensured by professional annotators.

## Recent Developments and Status

The paper, code, dataset, and project page were released on January 8, 2025. The work was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL) in July 2025 in Vienna, Austria.

Recent updates to the benchmark include support for additional models and evaluation frameworks. Qwen2.5-Math-PRM-7B implementations were added to the PRM Eval ToolKit, achieving state-of-the-art performance for open-source PRMs in PRMBench.

## Related Work: ToolPRMBench

Additionally, ToolPRMBench was introduced to evaluate the effectiveness of PRMs in tool-using, serving as a benchmark for PRMs in tool-using agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d607cb1f-4a7a-4b80-bbd3-8f01a9e9a281",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "be50abaa-388b-4a1d-8954-ebce39392ce5",
  "sourceToolAssistantUUID": "d607cb1f-4a7a-4b80-bbd3-8f01a9e9a281",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-27T17:49:10.360Z_

Interesting findings. Let me now dig into ActPRM, Universal-PRM, and other recent top performers, plus get the GenPRM specific table numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be50abaa-388b-4a1d-8954-ebce39392ce5",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVgNv4EAWYALpzg25Hr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c725ca3-e9ea-416e-a82d-ea8b2e64ba2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BenWaZQCZhsEEGE9cVdWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 700,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 46444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
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

_source line 47 · 2026-05-27T17:49:10.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011pBwZZiHnwfBGLppMjJ7fW`</summary>

```json
{
  "query": "ActPRM Universal-PRM ProcessBench SOTA F1 score 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c725ca3-e9ea-416e-a82d-ea8b2e64ba2c",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVgNv4EAWYALpzg25Hr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "264dc0ff-cfeb-4fcc-95c6-c8fab7b6b441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BenWaZQCZhsEEGE9cVdWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 700,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 46444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
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

_source line 48 · 2026-05-27T17:49:12.551Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0193VAZtxvwNXm4Mdn9T66Zh`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.10559",
  "prompt": "Extract ALL ProcessBench F1 scores from tables in this paper. I need exact F1 numbers for ActPRM and all baseline models. Include all subsets (GSM8K, MATH, OlympiadBench, OmniMATH) and averages. Also extract information about Universal-PRM if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264dc0ff-cfeb-4fcc-95c6-c8fab7b6b441",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVgNv4EAWYALpzg25Hr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00b4837a-edb7-4d90-97ed-2d6665485d67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BenWaZQCZhsEEGE9cVdWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 700,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 46444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
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

_source line 49 · 2026-05-27T17:49:13.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BwEtnyNxbc82xWKAYaSsJb`</summary>

```json
{
  "query": "GenPRM ProcessBench table 1 GSM8K MATH OlympiadBench OmniMATH F1 exact scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b4837a-edb7-4d90-97ed-2d6665485d67",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVgNv4EAWYALpzg25Hr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cbe6d8b-12a0-4067-8ca6-904901f8d9ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BenWaZQCZhsEEGE9cVdWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 700,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 46444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
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

_source line 50 · 2026-05-27T17:49:15.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KsyL56Nb86qTD8Pp2rWkRU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.06559",
  "prompt": "Extract all ProcessBench results and F1 scores reported in the original ProcessBench paper. Include scores for all models tested: GPT-4o, o1-mini, QwQ-32B-Preview, Qwen2.5-Math-PRM-72B, Math-Shepherd, RLHFlow, ReasonEval, etc. Include per-subset and average scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cbe6d8b-12a0-4067-8ca6-904901f8d9ad",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVgNv4EAWYALpzg25Hr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1132311e-ead0-49e0-a316-6558409a9dca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BenWaZQCZhsEEGE9cVdWg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 700,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 46444,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 700,
          "output_tokens": 460,
          "cache_read_input_tokens": 46444,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2373,
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

_source line 51 · 2026-05-27T17:49:16.881Z_

<details><summary>↩ Tool result · `toolu_0193VAZtxvwNXm4Mdn9T66Zh`</summary>

```text
# ProcessBench F1 Scores from Paper

## Main Results (Table 1)

**ActPRM (7B):**
- GSM8K: 0.816
- MATH: 0.798
- Olympiad Bench: 0.714
- OmniMath: 0.670
- **Average F1: 0.750**

**ActPRM-X (7B):**
- GSM8K: 0.827
- MATH: 0.820
- Olympiad Bench: 0.720
- OmniMath: 0.673
- **Average F1: 0.760**

**Universal-PRM:**
- GSM8K: 0.858
- MATH: 0.777
- Olympiad Bench: 0.676
- OmniMath: 0.664
- **Average F1: 0.743**

**Qwen2.5-Math-PRM-7B:**
- Average F1: 0.735

**Other notable baselines:**
- Math-Shepherd-PRM-7B: 0.315
- PURE-PRM-7B: 0.575
- Ensemble-PRM-PRM800K (authors' baseline): 0.560

The paper emphasizes that ActPRM achieves "new state-of-the-art (75.0% on ProcessBench)" while requiring significantly reduced annotation costs compared to prior methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00b4837a-edb7-4d90-97ed-2d6665485d67",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "0af0943c-3eb1-463d-bb6e-f6483bb58a1c",
  "sourceToolAssistantUUID": "00b4837a-edb7-4d90-97ed-2d6665485d67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-27T17:49:16.963Z_

<details><summary>↩ Tool result · `toolu_011pBwZZiHnwfBGLppMjJ7fW`</summary>

```text
Web search results for query: "ActPRM Universal-PRM ProcessBench SOTA F1 score 2025"

Links: [{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/html/2504.10559v1"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/pdf/2504.10559"},{"title":"GitHub - sail-sg/ActivePRM","url":"https://github.com/sail-sg/ActivePRM"},{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"AURORA: Automated Training Framework of Universal Process Reward","url":"https://arxiv.org/pdf/2502.11520"}]

Based on the search results, here are the key findings regarding ActPRM, Universal-PRM, and ProcessBench F1 scores in 2025:

## ActPRM Performance

ActPRM-X achieves a new SOTA performance on ProcessBench with an average F1 of 0.760, outperforming the second-place model (Universal-PRM) with a margin of 1.7%. Additionally, within 7B PRMs, ActPRM-X achieved new SOTA performance on ProcessBench (76.0%) and PRMBench (66.7%).

The base ActPRM model also performs well: ActPRM achieves an average F1 score of 0.750, outperforming Qwen2.5-Math-PRM-7B by a margin of 1.5%.

## Universal-PRM Comparison

Universal-PRM ranks as the second-place model on ProcessBench, placing it just behind ActPRM in the current leaderboard standings for same-sized models.

## Key Achievement

ActPRM achieved SOTA performance on ProcessBench (75.0%) and PRMBench (65.5%) with merely 5% labeling cost compared with Qwen/Qwen2.5-Math-PRM-7B, demonstrating both superior performance and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "264dc0ff-cfeb-4fcc-95c6-c8fab7b6b441",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "ae2cb55a-de3f-4ead-974e-87bb41b9cd8f",
  "sourceToolAssistantUUID": "264dc0ff-cfeb-4fcc-95c6-c8fab7b6b441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-27T17:49:18.134Z_

<details><summary>↩ Tool result · `toolu_01KsyL56Nb86qTD8Pp2rWkRU`</summary>

```text
I cannot provide the specific ProcessBench results and F1 scores you've requested based on the content above.

The webpage content provided is only the arXiv abstract and metadata page for the paper. It contains no actual results tables, F1 scores, or performance metrics for any of the models mentioned (GPT-4o, o1-mini, QwQ-32B-Preview, etc.).

The abstract states that the paper "conduct[s] extensive evaluation on ProcessBench, involving two types of models: process reward models (PRMs) and critic models," but the detailed numerical results are not included in this landing page excerpt.

To access the actual benchmark results and scores, you would need to review the full PDF of the paper itself, which is available at the link provided on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1132311e-ead0-49e0-a316-6558409a9dca",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "e0cbd3d6-c005-4414-b2da-a32609a46cd7",
  "sourceToolAssistantUUID": "1132311e-ead0-49e0-a316-6558409a9dca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-27T17:49:28.332Z_

<details><summary>↩ Tool result · `toolu_01BwEtnyNxbc82xWKAYaSsJb`</summary>

```text
Web search results for query: "GenPRM ProcessBench table 1 GSM8K MATH OlympiadBench OmniMATH F1 exact scores"

Links: [{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via   Generative Reasoning","url":"https://arxiv.org/pdf/2504.00891"},{"title":"LLM Benchmarks | EvalScope - Read the Docs","url":"https://evalscope.readthedocs.io/en/v1.0.0/get_started/supported_dataset/llm.html"},{"title":"[2410.07985] Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models","url":"https://arxiv.org/abs/2410.07985"},{"title":"Qwen/ProcessBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Qwen/ProcessBench"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models","url":"https://arxiv.org/html/2410.07985v1"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large   Language Models","url":"https://arxiv.org/pdf/2410.07985"},{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/html/2510.13744v1"},{"title":"Olympiad Benchmark Evaluation","url":"https://www.emergentmind.com/topics/olympiad-benchmark"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=yaqPf0KAlN"}]

I found relevant information about GenPRM and ProcessBench. The search results include the GenPRM paper, which discusses its performance on ProcessBench with the subsets you mentioned. However, the specific Table 1 scores with F1 exact scores are not fully visible in these search results. Let me search more specifically for the GenPRM table with the exact F1 scores.

Links: [{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"Retrieval-Augmented Process Reward Model for ...","url":"https://aclanthology.org/2025.findings-acl.444.pdf"},{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models","url":"https://arxiv.org/html/2410.07985v1"},{"title":"[2410.07985] Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models","url":"https://arxiv.org/abs/2410.07985"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large   Language Models","url":"https://arxiv.org/pdf/2410.07985"},{"title":"[Quick Review] Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models","url":"https://liner.com/review/omnimath-a-universal-olympiad-level-mathematic-benchmark-for-large-language"},{"title":"Omni-MATH","url":"https://omni-math.github.io/"},{"title":"Olympiad Benchmark Evaluation","url":"https://www.emergentmind.com/topics/olympiad-benchmark"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=yaqPf0KAlN"}]

Let me search more specifically for the GenPRM arxiv paper with the actual table results.

Links: [{"title":"Exploring Generative Process Reward Modeling for Semi-Structured Data: A Case Study of Table Question Answering","url":"https://arxiv.org/html/2510.20304"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Request PDF","url":"https://www.researchgate.net/publication/390404512_GenPRM_Scaling_Test-Time_Compute_of_Process_Reward_Models_via_Generative_Reasoning"},{"title":"[PDF] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GenPRM:-Scaling-Test-Time-Compute-of-Process-Reward-Zhao-Liu/bd94932b7604933a11d1538b0de6f9543089711f"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://ryanliu112.github.io/GenPRM/"}]

Based on my search results, I found information about the GenPRM paper (arxiv 2504.00891), which discusses GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset, and through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. 

However, I was unable to locate the specific Table 1 from the GenPRM paper with the exact F1 scores for each benchmark (GSM8K, MATH, OlympiadBench, and OmniMATH). While the search results confirm that GenPRM reports results on ProcessBench with these subsets, the actual numerical values from Table 1 are not visible in the search results I retrieved.

To access the specific table with exact F1 scores, you would need to directly view the GenPRM paper PDF at https://arxiv.org/pdf/2504.00891.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cbe6d8b-12a0-4067-8ca6-904901f8d9ad",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "f6de53e6-c94a-4ed9-95f0-acec8db0e459",
  "sourceToolAssistantUUID": "6cbe6d8b-12a0-4067-8ca6-904901f8d9ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-27T17:49:31.492Z_

Let me try to get the GenPRM results from its project page and the ProcessBench original paper, plus search for more recent entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6de53e6-c94a-4ed9-95f0-acec8db0e459",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVhy9sBeeNAQ6Mb583z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1755d77-4489-42d3-9a1e-a1d3dd01bb02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL1w1Q8cRJ95jYqFHuKB8Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 204,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 48817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
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

_source line 56 · 2026-05-27T17:49:33.855Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wi4RZcFhVtbxgiAqqvHWKT`</summary>

```json
{
  "url": "https://ryanliu112.github.io/GenPRM/",
  "prompt": "Extract ALL ProcessBench F1 scores from this project page. I need exact F1 numbers for GenPRM-1.5B, GenPRM-7B, GenPRM-72B at different majority voting settings (@1, @4, @8, @16). Also extract all baseline model scores from tables. Include columns for GSM8K, MATH, OlympiadBench, OmniMATH, and Average."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1755d77-4489-42d3-9a1e-a1d3dd01bb02",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVhy9sBeeNAQ6Mb583z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cacf09f-2a81-4286-b3e5-effc039f0725",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL1w1Q8cRJ95jYqFHuKB8Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 204,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 48817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
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

_source line 57 · 2026-05-27T17:49:36.266Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XofwqfotrimbAtYGRqisy7`</summary>

```json
{
  "url": "https://arxiv.deeppaper.ai/papers/2504.00891v2?locale=en",
  "prompt": "Extract ALL ProcessBench F1 scores from Table 1 and any other tables. I need exact F1 numbers for GenPRM-1.5B, GenPRM-7B, GenPRM-72B at different majority voting settings (@1, @4, @8, @16). Also extract all baseline model scores including Qwen2.5-Math-PRM-72B, GPT-4o, Math-Shepherd, ReasonEval, RLHFlow, o1-mini, QwQ-32B-Preview. Include columns for GSM8K, MATH, OlympiadBench, OmniMATH, and Average."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cacf09f-2a81-4286-b3e5-effc039f0725",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVhy9sBeeNAQ6Mb583z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a653a3e-d271-411f-9ac4-fd9ae45cdb22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL1w1Q8cRJ95jYqFHuKB8Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 204,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 48817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
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

_source line 58 · 2026-05-27T17:49:36.685Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015T1Bg2vo8fHsQQ7WsNLJjb`</summary>

```json
{
  "query": "\"ProcessBench\" \"FreePRM\" OR \"AURORA\" OR \"Hard2Verify\" process reward model evaluation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a653a3e-d271-411f-9ac4-fd9ae45cdb22",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVhy9sBeeNAQ6Mb583z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "633ffbe7-139b-4e1d-a2d5-ff9d54db1e95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL1w1Q8cRJ95jYqFHuKB8Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 204,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 48817,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 204,
          "output_tokens": 498,
          "cache_read_input_tokens": 48817,
          "cache_creation_input_tokens": 3979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3979,
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

_source line 59 · 2026-05-27T17:49:37.129Z_

<details><summary>↩ Tool result · `toolu_01Wi4RZcFhVtbxgiAqqvHWKT`</summary>

```text
I cannot extract the specific F1 scores you're requesting because the web page content provided does not include numerical data tables or detailed results. 

The page references "![](./static/images/main_processbench.png)" and other result figures, but the actual image content—which would contain the ProcessBench F1 scores for GenPRM variants and baseline comparisons across different voting settings—is not included in the text provided.

To obtain these specific metrics, you would need to:
1. Access the full paper via the provided arXiv link
2. Review the actual result images/tables on the project website
3. Consult the GitHub repository referenced in the content
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cacf09f-2a81-4286-b3e5-effc039f0725",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "b605c59a-fad7-4092-97cf-2a8851794e4e",
  "sourceToolAssistantUUID": "3cacf09f-2a81-4286-b3e5-effc039f0725",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-27T17:49:39.359Z_

<details><summary>↩ Tool result · `toolu_01XofwqfotrimbAtYGRqisy7`</summary>

```text
I appreciate your request, but I cannot extract the specific ProcessBench F1 scores you're asking for. While the webpage content provided mentions that "GenPRM significantly outperforms prior PRMs" and references "ProcessBench," the actual Table 1 with numerical F1 scores for GenPRM-1.5B, GenPRM-7B, baseline models, and their performance across different voting settings is not included in the text provided.

The document only states in general terms that models achieved strong results, such as: "a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench."

To obtain the exact numerical data you need, you would need to access the full paper directly via the arXiv link (2504.00891v2) or visit the project page mentioned at https://ryanliu112.github.io/GenPRM.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a653a3e-d271-411f-9ac4-fd9ae45cdb22",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "6de75bf5-de23-44ef-95e3-4995ec3af48d",
  "sourceToolAssistantUUID": "7a653a3e-d271-411f-9ac4-fd9ae45cdb22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-27T17:49:43.487Z_

<details><summary>↩ Tool result · `toolu_015T1Bg2vo8fHsQQ7WsNLJjb`</summary>

```text
Web search results for query: ""ProcessBench" "FreePRM" OR "AURORA" OR "Hard2Verify" process reward model evaluation 2025"

Links: [{"title":"[2506.03570] FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/abs/2506.03570"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250603570S/abstract"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.50/"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"FreePRM: Training Process Reward Models Without ...","url":"https://www.arxiv.org/pdf/2506.03570"}]

Based on the search results, here's what I found about process reward model evaluation in 2025:

## ProcessBench
ProcessBench is a benchmark for identifying process errors in mathematical reasoning, and it serves as a key evaluation framework for process reward models.

## FreePRM
FreePRM is a weakly supervised framework for training PRMs without access to ground-truth step-level labels, which generates pseudo step-level labels based on the correctness of final outcome. FreePRM achieves an average F1 score of 53.0% on ProcessBench, outperforming fully supervised PRM trained on Math-Shepherd by +24.1%.

## Hard2Verify
Hard2Verify is a human-annotated, step-level verification benchmark designed to rigorously assess step-level verifiers by requiring them to provide annotations or identify the first error in responses from frontier LLMs for challenging and open-ended math questions. It evaluates 29 generative critics and process reward models.

## AURORA
AURORA is an automated training framework of universal process reward models via ensemble prompting.

## PRMBench
PRMBench is the first comprehensive process-level reward model benchmark, comprising 6,216 carefully curated samples and 83,456 step-level labels. Gemini-2-Thinking achieves the best performance of 68.8, but still significantly falls behind the human performance of 83.8.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "633ffbe7-139b-4e1d-a2d5-ff9d54db1e95",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "5bd50301-8ed0-4ab7-96dd-82dcff5862e4",
  "sourceToolAssistantUUID": "633ffbe7-139b-4e1d-a2d5-ff9d54db1e95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-27T17:49:47.331Z_

Let me get more specific numbers and investigate Hard2Verify and the original ProcessBench paper numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bd50301-8ed0-4ab7-96dd-82dcff5862e4",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVj5qj9WhYAiEsdnNFR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c833bf56-8778-4991-a248-6894235ce3dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WnaP14ofBVbqRpBNSMbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 52796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 63 · 2026-05-27T17:49:49.048Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Vqrbt7A2YjT2TJ1rXqKUP`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13744v1",
  "prompt": "Extract all information about Hard2Verify benchmark. What models are evaluated? What are the scores? How does it compare to ProcessBench? What are the key findings about generative vs discriminative PRMs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c833bf56-8778-4991-a248-6894235ce3dc",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVj5qj9WhYAiEsdnNFR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "319b2d91-2874-49b2-aeb8-257ac3ed72f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WnaP14ofBVbqRpBNSMbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 52796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 64 · 2026-05-27T17:49:52.037Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019dceyjSZ4ENFKnb71FRwrM`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559",
  "prompt": "Extract ALL F1 scores from tables in this ProcessBench paper. I need exact F1 numbers for ALL models tested, including GPT-4o, o1-mini, QwQ-32B-Preview, Qwen2.5-Math-PRM-72B, Qwen2.5-Math-PRM-7B, Math-Shepherd-PRM-7B, ReasonEval-7B, RLHFlow-DeepSeek-PRM-8B, Llemma-PRM800K-7B, and any other models. Include all subsets (GSM8K, MATH, OlympiadBench, OmniMATH) and averages. This is the ORIGINAL ProcessBench paper so the tables should be here."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "319b2d91-2874-49b2-aeb8-257ac3ed72f3",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVj5qj9WhYAiEsdnNFR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4ecb0c5-7021-476a-9d74-103509f18d0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WnaP14ofBVbqRpBNSMbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 52796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 65 · 2026-05-27T17:49:52.045Z_

<details><summary>↩ Tool result · `toolu_019dceyjSZ4ENFKnb71FRwrM`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4ecb0c5-7021-476a-9d74-103509f18d0a",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "e3f7912c-ae90-4021-a181-6de642929b01",
  "sourceToolAssistantUUID": "a4ecb0c5-7021-476a-9d74-103509f18d0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-27T17:49:52.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NsF98BL3r1sZEg35yjqLNP`</summary>

```json
{
  "query": "GenPRM 1.5B maj@8 ProcessBench F1 \"78\" OR \"79\" OR \"80\" OR \"81\" OR \"82\" GPT-4o"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3f7912c-ae90-4021-a181-6de642929b01",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVj5qj9WhYAiEsdnNFR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65388330-9d98-4f1b-b83a-3d2d34a9b096",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WnaP14ofBVbqRpBNSMbec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 52796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1875,
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

_source line 67 · 2026-05-27T17:49:53.732Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R5qwki6Yje7r6JUDmiqoCh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.11520",
  "prompt": "Extract information about AURORA framework for process reward models and any ProcessBench results reported."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65388330-9d98-4f1b-b83a-3d2d34a9b096",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVj5qj9WhYAiEsdnNFR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1a357d9-be27-4e7d-ad66-a96122e6b8e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WnaP14ofBVbqRpBNSMbec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 52796,
      "output_tokens": 549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 549,
          "cache_read_input_tokens": 52796,
          "cache_creation_input_tokens": 1875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1875,
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

_source line 68 · 2026-05-27T17:49:56.416Z_

<details><summary>↩ Tool result · `toolu_013Vqrbt7A2YjT2TJ1rXqKUP`</summary>

```text
# Hard2Verify Benchmark: Key Findings

## Overview
Hard2Verify is a step-level verification benchmark for frontier mathematics problems, featuring 1,860 human-annotated steps across 200 model responses. The benchmark emphasizes "open-ended questions where verifiers cannot 'cheat' if they have seen the question during training."

## Evaluated Models
The study evaluates **29 models** including:
- **Proprietary generative critics**: GPT-5, Gemini 2.5 Pro, Claude Sonnet 4, o3, o4-Mini
- **Large open-weight models (≥70B)**: Qwen3 variants, DeepSeek-R1, gpt-oss-120B
- **Smaller models (<70B)**: Qwen3-8B through Qwen3-32B, gpt-oss-20B
- **Process Reward Models**: Qwen2.5-Math-PRM (7B/72B), Skywork-PRM, ReasonFlux-PRM

## Performance Scores
**Step-Level Task (Balanced F1)**:
- GPT-5: 85.83
- gpt-oss-120B: 74.64
- Qwen2.5-Math-PRM-72B: 35.50

**Error Identification Task (Balanced F1)**:
- GPT-5: 69.72
- gpt-oss-120B: 60.64
- Qwen2.5-Math-PRM-72B: 37.28

## Hard2Verify vs. ProcessBench
A critical finding: models achieving 60%+ on ProcessBench scored below 20% on Hard2Verify. Specifically, "Qwen2.5-Math-PRM-72B performance drops from ProcessBench state-of-the-art at 78.3 to 37.3 on Hard2Verify."

## Key Finding: Generative vs. Discriminative Models
**Weak verifiers cannot identify errors**—they mark nearly all steps as correct. The research reveals: "verifier performance degrades because TNR drops quickly to near 0, while TPR rises gradually to almost 1."

**PRMs significantly underperform** compared to generative models, with process reward models struggling fundamentally on frontier problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "319b2d91-2874-49b2-aeb8-257ac3ed72f3",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "82e703c4-4e91-47b6-9643-0e9de403e2b0",
  "sourceToolAssistantUUID": "319b2d91-2874-49b2-aeb8-257ac3ed72f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-27T17:49:58.152Z_

<details><summary>↩ Tool result · `toolu_01R5qwki6Yje7r6JUDmiqoCh`</summary>

```text
# AURORA Framework Overview

**Purpose and Approach:**
AURORA is an automated training system for universal process reward models (PRMs). The framework implements a two-phase strategy: first, it uses "diverse prompting strategies and ensemble methods to perform automated annotation and evaluation of processes"; second, it applies reverse verification with reference answers to enhance validation capabilities.

**Key Innovation:**
The system addresses a critical gap in LLM evaluation—assessing complex reasoning trajectories from advanced models like o1. Rather than relying solely on human evaluation, it automates the process reward assessment across diverse policy distributions.

**Benchmark Contribution:**
Beyond existing ProcessBench testing, the authors introduced UniversalBench to evaluate "reward predictions across full trajectories under diverse policy distribution with long Chain-of-Thought (CoT) outputs."

**Results:**
According to the abstract, AURORA demonstrated improvements in process evaluation accuracy and enhanced PRM performance for varied policy distributions and longer reasoning chains.

**Availability:**
The Universal-PRM-7B model is accessible via Hugging Face, with the full project promised for open-source release.

*Note: The paper was submitted February 17, 2025, and remains under review.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1a357d9-be27-4e7d-ad66-a96122e6b8e9",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "e9b3d561-99e2-4ade-a4b5-9f65eddd1a74",
  "sourceToolAssistantUUID": "d1a357d9-be27-4e7d-ad66-a96122e6b8e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-27T17:49:59.337Z_

<details><summary>↩ Tool result · `toolu_01NsF98BL3r1sZEg35yjqLNP`</summary>

```text
Web search results for query: "GenPRM 1.5B maj@8 ProcessBench F1 "78" OR "79" OR "80" OR "81" OR "82" GPT-4o"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"GenPRM Framework Overview","url":"https://www.emergentmind.com/topics/genprm-framework"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"}]

Based on the search results, I found relevant information about GenPRM 1.5B with Maj@8 (majority voting at 8 samples) on ProcessBench:

The 1.5B GenPRM model outperforms GPT-4o on MATH, OlympiadBench, and Omni-MATH when using test-time scaling (Maj@8). More specifically, through test-time scaling, a 1.5B GenPRM outperforms GPT-4o on ProcessBench.

The search results confirm that GenPRM-1.5B with majority voting (Maj@8) achieves better performance than GPT-4o on ProcessBench, though the specific F1 score values you're looking for (78, 79, 80, 81, or 82) are not explicitly stated in the search results. The results indicate this is a significant achievement, as even small models (e.g., 1.5B parameters) can surpass significantly larger discriminative PRMs and proprietary models, with GenPRM-1.5B@Maj8 exceeding GPT-4o on ProcessBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65388330-9d98-4f1b-b83a-3d2d34a9b096",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "1ad7e571-b203-4b76-8595-bcb28b4b780b",
  "sourceToolAssistantUUID": "65388330-9d98-4f1b-b83a-3d2d34a9b096",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-27T17:50:04.000Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VhLcvaVnavS1s7tiajxuhh`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/genprm-framework",
  "prompt": "Extract ALL ProcessBench F1 scores for GenPRM models. I need exact numerical F1 scores for GenPRM-1.5B, GenPRM-7B, GenPRM-72B at Maj@1, Maj@4, Maj@8, Maj@16. Also extract scores for baselines like Qwen2.5-Math-PRM-72B, GPT-4o, o1-mini, Math-Shepherd, etc. Look for any tables with ProcessBench results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ad7e571-b203-4b76-8595-bcb28b4b780b",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVkFb91rMhFGVXq7j67",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c2019c4-d3aa-488a-b1a4-31875c25e2cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNotVonhdTheuZdWjrrtm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 293,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 54671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 72 · 2026-05-27T17:50:04.988Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CQ3T7wbK1gnMAfNPPdsdef`</summary>

```json
{
  "url": "https://huggingface.co/papers/2504.00891",
  "prompt": "Extract ALL ProcessBench F1 scores for GenPRM. Look for any tables or specific numbers mentioned in comments or paper summary. I need exact F1 scores for GenPRM-1.5B, GenPRM-7B, and baselines on ProcessBench."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c2019c4-d3aa-488a-b1a4-31875c25e2cf",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVkFb91rMhFGVXq7j67",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "838a3cb1-5ac9-400f-b2d5-ef4cdb49f4a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNotVonhdTheuZdWjrrtm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 293,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 54671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 73 · 2026-05-27T17:50:05.559Z_

<details><summary>↩ Tool result · `toolu_01CQ3T7wbK1gnMAfNPPdsdef`</summary>

```text
&lt;persisted-output>
Output too large (87.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01CQ3T7wbK1gnMAfNPPdsdef.txt

Preview (first 2KB):
# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning

Jian Zhao&lt;sup>1,3\*&lt;/sup>, Runze Liu&lt;sup>1,2\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>

&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology

Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "838a3cb1-5ac9-400f-b2d5-ef4cdb49f4a1",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "dde1a6fa-59b4-47a4-bcad-562158d1ca26",
  "sourceToolAssistantUUID": "838a3cb1-5ac9-400f-b2d5-ef4cdb49f4a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-27T17:50:06.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01246eJVBWkxyk2ZrCtaJ1UF`</summary>

```json
{
  "query": "ProcessBench original paper results table GPT-4o 61.9 o1-mini QwQ-32B 71.5 Qwen2.5-Math-PRM-72B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde1a6fa-59b4-47a4-bcad-562158d1ca26",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVkFb91rMhFGVXq7j67",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "680077ea-9961-48a9-97ef-6d81473514d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNotVonhdTheuZdWjrrtm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 293,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 54671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 75 · 2026-05-27T17:50:09.552Z_

<details><summary>↩ Tool result · `toolu_01VhLcvaVnavS1s7tiajxuhh`</summary>

```text
I've reviewed the provided web page content thoroughly, but I cannot extract the specific ProcessBench F1 scores you're requesting.

The document mentions GenPRM performance on ProcessBench only in one location: "GenPRM-1.5B@Maj8 exceeding GPT-4o on ProcessBench." However, this statement provides no actual numerical F1 scores.

While the page references several research papers (including one by Zhao et al. from April 2025 that appears to discuss GenPRM scaling), the actual detailed benchmark tables with F1 scores are not included in the web page content provided. The page contains the abstract/overview framework but not the underlying research data tables.

**To obtain these specific metrics, you would need to:**
- Access the full research papers cited (particularly the Zhao et al. 2025 paper on inference-time compute scaling)
- Visit the arXiv links referenced in the document
- Review the actual benchmark result tables in those publications
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c2019c4-d3aa-488a-b1a4-31875c25e2cf",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "4ae75b7c-cb7f-43e2-9625-f6b9d1c45dc6",
  "sourceToolAssistantUUID": "5c2019c4-d3aa-488a-b1a4-31875c25e2cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-27T17:50:11.919Z_

<details><summary>↩ Tool result · `toolu_01246eJVBWkxyk2ZrCtaJ1UF`</summary>

```text
Web search results for query: "ProcessBench original paper results table GPT-4o 61.9 o1-mini QwQ-32B 71.5 Qwen2.5-Math-PRM-72B"

Links: [{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2412.06559v4"},{"title":"2025-05-21 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://www.arxiv.org/pdf/2412.06559v3"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"2024-12-10 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559v1"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"[Literature Review] Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://www.themoonlight.io/en/review/socratic-prmbench-benchmarking-process-reward-models-with-systematic-reasoning-patterns"},{"title":"QwQ 32B Preview | Open Laboratory","url":"https://openlaboratory.ai/models/qwq-32b-preview"}]

Based on the search results, I found information about the ProcessBench benchmark and the model performance metrics you mentioned:

QwQ-32B-Preview, an open-source reasoning model, achieves the highest performance among non-proprietary systems with 71.5% average F1 score, which is competitive with and sometimes exceeds GPT-4o-0806 (61.9% F1). However, a notable gap remains with specialized reasoning models like o1-mini, which achieves 87.9% F1 score.

Regarding Qwen2.5-Math-PRM-72B specifically, Qwen2.5-Math-PRM-72B exhibits substantial advantages over existing PRMs, though the exact F1 score of 71.5 you mentioned appears to refer to the QwQ-32B-Preview model rather than the Qwen2.5-Math-PRM-72B model on the ProcessBench benchmark.

The search results contain information from the original ProcessBench paper discussing these model evaluations, but I was unable to locate a complete results table showing all four models with their specific scores in a single table format from the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "680077ea-9961-48a9-97ef-6d81473514d6",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "39633279-1c24-4f5e-9e47-c220a229ac58",
  "sourceToolAssistantUUID": "680077ea-9961-48a9-97ef-6d81473514d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-27T17:50:15.010Z_

Let me read the GenPRM HuggingFace paper content which was saved, and fetch the original ProcessBench paper for exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39633279-1c24-4f5e-9e47-c220a229ac58",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVmBQQ7qNEzHihsZKEM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7c4a67c-2897-44be-af71-83e9f245b3cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9h4XvwqScj42iqcTCMBC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 56654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 78 · 2026-05-27T17:50:16.486Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qu2kiwExPE4jz32RTHgVD4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01CQ3T7wbK1gnMAfNPPdsdef.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7c4a67c-2897-44be-af71-83e9f245b3cf",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVmBQQ7qNEzHihsZKEM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0189e686-e4c9-4ef8-baa7-c183adc7bee5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9h4XvwqScj42iqcTCMBC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 56654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 79 · 2026-05-27T17:50:16.804Z_

<details><summary>↩ Tool result · `toolu_01Qu2kiwExPE4jz32RTHgVD4`</summary>

```text
0	# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
1	
2	Jian Zhao&lt;sup>1,3\*&lt;/sup>, Runze Liu&lt;sup>1,2\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>
3	
4	&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology
5	
6	Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.
7	
8	**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.
9	
10	\* Equal contribution
11	
12	† Project lead & Work done during an internship at Shanghai AI Laboratory
13	
14	‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.
15	
16	Figure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).
17	
18	## 1. Introduction
19	
20	Large Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).
21	
22	Effective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*
23	
24	In this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.
25	
26	Our contributions can be summarized as follows:
27	
28	1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.
29	2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.
30	3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries
31	
32	### 2.1. Markov Decision Process
33	
34	Following [Liu et al. \(2025\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$ , where  $\mathcal{S}$  is the state space,  $\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$  is the reward function, and  $\gamma \in [0, 1]$  is the discount factor. Starting with a prompt set  $\mathcal{X}$  and an initial state  $s_1 = x \sim \mathcal{X}$ , the policy model  $\pi_\theta$  generates an action  $a_1 \sim \pi_\theta(\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\cdot, \cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\tau = \{a_1, a_2, \dots, a_T\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).
35	
36	### 2.2. Supervised Fine-Tuning
37	
38	Supervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\mathcal{D}_{\text{SFT}} = \{(x^{(i)}, y^{(i)})\}_{i=1}^N$ , the SFT loss is:
39	
40	$$\mathcal{L}_{\text{SFT}}(\theta) = -\mathbb{E}_{(x,y) \sim \mathcal{D}_{\text{SFT}}} \left[ \sum_{t=1}^{|y|} \log \pi_\theta(y_t | x, y_{1:t-1}) \right], \quad (1)$$
41	
42	where  $\pi_\theta$  represents a model with parameters  $\theta$ .
43	
44	### 2.3. Test-Time Scaling
45	
46	In this work, we consider two test-time scaling methods, including majority voting and Best-of-N.
47	
48	**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.
49	
50	**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.
51	
52	## 3. Method
53	
54	In this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.
55	
56	### 3.1. GenPRM and Test-Time Scaling
57	
58	#### 3.1.1. From Discriminative PRM to Generative PRM
59	
60	**Discriminative PRM.** Assume we have a PRM dataset  $\mathcal{D}_{\text{Disc}} = \{(s_t, a_t), r_t\}$ , where  $r_t \in \{0, 1\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\psi$  is trained via cross-entropy loss ([Skywork](#)
61	
62	&lt;sup>1&lt;/sup>Following [Snell et al. \(2025\)](#); [Liu et al. \(2025\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:
63	
64	- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \frac{2}{3}$ .
65	- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \frac{MC(s_t, a_t)}{MC(s_t)} \geq \epsilon$ . If the reward is high,  $\hat{r}_t = 1$  (green checkmark), otherwise  $\hat{r}_t = 0$  (red X).
66	- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.
67	- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.
68	- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).
69	- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .
70	
71	Legend:
72	
73	- a Intermediate Step
74	- q Correct Answer
75	- q Incorrect Answer
76	- r Single Reward Judgement
77	- r Aggregated Reward Judgement
78	
79	**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.
80	
81	o1 Team, 2024; Zhang et al., 2025c):
82	
83	$$\mathcal{L}_{CE}(\psi) = -\mathbb{E}_{(s_t, a_t, r_t) \sim \mathcal{D}_{Disc}} [r_t \log r_\psi(s_t, a_t) + (1 - r_t) \log(1 - r_\psi(s_t, a_t))]. \quad (2)$$
84	
85	**Direct Generative PRM.** With a dataset  $\mathcal{D}_{Direct-Gen} = \{(s_t, a_t), r_t\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\hat{r}_t$ :
86	
87	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t). \quad (3)$$
88	
89	**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\mathcal{D}_{Gen} = \{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\hat{r}_t$  can be obtained via the following equation:
90	
91	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}, v_t), \quad \text{where } v_t \sim r_\psi(\cdot \mid s_t, a_t, v_{1:t-1}) \quad (4)$$
92	
93	**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:
94	
95	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \quad \text{where } v_t \sim r_\psi(\cdot \mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \quad (5)$$
96	
97	In the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.
98	
99	### 3.1.2. Test-Time Scaling
100	
101	**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.
102	
103	**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.
104	
105	**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:
106	
107	$$\hat{r}_t = \frac{1}{N} \sum_{i=1}^N r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}^i, v_t^i). \quad (6)$$
108	
109	And we can further incorporate code verification and execution feedback into this reasoning process:
110	
111	$$\hat{r}_t = \frac{1}{N} \sum_{i=1}^N r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \quad (7)$$
112	
113	Then the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.
114	
115	## 3.2. Synthesizing Data of GenPRM
116	
117	In this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.
118	
119	### 3.2.1. Solution Generation and Monte Carlo Estimation
120	
121	**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\n\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing
122	
123	Step 1: {step content}
124	
125	...
126	
127	Step T: {step content}
128	
129	The proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.
130	
131	**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):
132	
133	$$MC(s_t, a_t) = MC(s_{t+1}) = \frac{1}{K} \sum_{j=1}^K \mathbb{1}(q_j = q^*), \quad (8)$$
134	
135	where  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :
136	
137	$$K = \begin{cases} 128 & \text{if } 0 \leq MC(s_1) < 0.1, \\ 64 & \text{if } 0.1 \leq MC(s_1) < 0.9, \\ 32 & \text{if } 0.9 \leq MC(s_1) < 1. \end{cases} \quad (9)$$
138	
139	### 3.2.2. Relative Progress Estimation
140	
141	Previous work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.
142	
143	Specifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:
144	
145	$$P_t = \frac{MC(s_t, a_t)}{MC(s_t)}, \quad (10)$$
146	
147	where  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\hat{r}_t$  byintroducing a threshold  $\epsilon$ :
148	
149	$$\hat{r}_t = \begin{cases} 1 & \text{if } P_t \geq \epsilon, \\ 0 & \text{otherwise.} \end{cases} \quad (11)$$
150	
151	We also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.
152	
153	### 3.2.3. Rationale Generation, Verification and Filtering
154	
155	To obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\{a_1, \dots, a_T\}$ , the generation and verification proceed as follows:
156	
157	**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\{a_1, \dots, a_{t-1}\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.
158	
159	**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.
160	
161	**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.
162	
163	## 4. Experiments
164	
165	In this section, we aim to answer the following questions:
166	
167	- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)
168	- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)
169	- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)
170	- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)
171	
172	### 4.1. Setup
173	
174	**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>
175	
176	&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.
177	
178	**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:
179	
180	- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.
181	- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.
182	- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.
183	- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).
184	- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).
185	- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.
186	- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.
187	- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.
188	- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.
189	
190	For critic experiments, we use the following methods for comparison:
191	
192	- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.
193	- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).
194	
195	**Implementation Details.** For RPE, we set  $\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.
196	
197	&lt;table border="1">
198	&lt;thead>
199	&lt;tr>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0189e686-e4c9-4ef8-baa7-c183adc7bee5",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "8bd2154d-9e2d-40af-8893-30a4b3229d5b",
  "sourceToolAssistantUUID": "0189e686-e4c9-4ef8-baa7-c183adc7bee5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-27T17:50:18.775Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019VqSubd8GazWEKyS1VHrPk`</summary>

```json
{
  "url": "https://www.arxiv.org/pdf/2412.06559v3",
  "prompt": "Extract ALL F1 scores from all tables. I need the complete results table with F1 scores for ALL models on ProcessBench. Include GPT-4o, o1-mini, QwQ-32B-Preview, all PRM models, and all critic models. Include per-subset scores (GSM8K, MATH, OlympiadBench, OmniMATH) and averages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bd2154d-9e2d-40af-8893-30a4b3229d5b",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVmBQQ7qNEzHihsZKEM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef0cc03a-8e4d-452d-bf24-ad3690fc8b76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9h4XvwqScj42iqcTCMBC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 56654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 81 · 2026-05-27T17:50:19.825Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KW2evsxPXL2r8jhGLvVW2Z`</summary>

```json
{
  "url": "https://qwenlm.github.io/blog/qwen2.5-math-prm/",
  "prompt": "Extract ALL ProcessBench F1 scores mentioned on this page. I need exact F1 scores for Qwen2.5-Math-PRM-72B, Qwen2.5-Math-PRM-7B, and all other models on ProcessBench. Include per-subset and average numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef0cc03a-8e4d-452d-bf24-ad3690fc8b76",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVmBQQ7qNEzHihsZKEM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54600b8a-f8d8-4b86-b84e-9812145c06fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9h4XvwqScj42iqcTCMBC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 56654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2356,
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

_source line 82 · 2026-05-27T17:50:23.437Z_

<details><summary>↩ Tool result · `toolu_01KW2evsxPXL2r8jhGLvVW2Z`</summary>

```text
I've reviewed the webpage content carefully, but **no specific F1 scores are provided** on this page. 

The article mentions that ProcessBench evaluation results exist and includes a reference to a chart image showing comparisons, stating: "When compared with LLM-as-judge, Qwen2.5-Math-PRM-7B in smaller model size demonstrates superior performance over all open-source models." However, the actual numerical F1 scores are not included in the text content—they appear only in the embedded image file, which I cannot read.

To obtain the specific F1 scores you're requesting, you would need to:
1. Access the actual image at the referenced URL
2. Consult the full papers cited (arXiv:2412.06559 and arXiv:2501.07301)
3. Visit the GitHub or Hugging Face repositories linked on the page
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54600b8a-f8d8-4b86-b84e-9812145c06fa",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "d4b814c6-aebc-429b-82dd-20565283e5d4",
  "sourceToolAssistantUUID": "54600b8a-f8d8-4b86-b84e-9812145c06fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-27T17:50:23.563Z_

<details><summary>↩ Tool result · `toolu_019VqSubd8GazWEKyS1VHrPk`</summary>

```text
I appreciate your detailed request, but I need to be direct: the content provided appears to be a PDF file encoded in binary/stream format rather than readable text. The visible content shows PDF object definitions and compressed stream data, not the actual table data you're seeking.

To extract the F1 scores table you need, I would require:

1. **The actual extracted text or image** of the ProcessBench results table showing:
   - Model names (GPT-4o, o1-mini, QwQ-32B-Preview, PRM variants, critic models)
   - Per-subset scores for GSM8K, MATH, OlympiadBench, OmniMATH
   - Overall average F1 scores

2. **Alternative formats** such as:
   - A plaintext version of the table
   - A CSV or structured data export
   - A screenshot or image of the results

The binary PDF stream data present cannot be reliably converted to readable table information without proper decompression and rendering, which is beyond my current processing capabilities in this context.

Could you provide the table content in a more accessible format?

[Binary content (application/pdf, 723.4KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/webfetch-1779904219444-ryagpv.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef0cc03a-8e4d-452d-bf24-ad3690fc8b76",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "6503dea9-7746-4412-9b2f-f2a1f33d0fdd",
  "sourceToolAssistantUUID": "ef0cc03a-8e4d-452d-bf24-ad3690fc8b76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-27T17:50:26.784Z_

I found the GenPRM table. Let me read the rest of it to get the actual numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6503dea9-7746-4412-9b2f-f2a1f33d0fdd",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVn3EJRhKwQ2Ex2Lsf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da633bf-aab5-48cf-b36b-75e58664d4a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzYWcdLkx43gXdS7aZf5A1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 229,
      "cache_creation_input_tokens": 9579,
      "cache_read_input_tokens": 59010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9579,
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

_source line 85 · 2026-05-27T17:50:28.471Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BKru3tohn8SacbSrYisuWg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01CQ3T7wbK1gnMAfNPPdsdef.txt",
  "offset": 195,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1da633bf-aab5-48cf-b36b-75e58664d4a1",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVn3EJRhKwQ2Ex2Lsf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7207e25-1361-4797-83ce-efcd0a0eb582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzYWcdLkx43gXdS7aZf5A1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 229,
      "cache_creation_input_tokens": 9579,
      "cache_read_input_tokens": 59010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9579,
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

_source line 86 · 2026-05-27T17:50:28.487Z_

<details><summary>↩ Tool result · `toolu_01BKru3tohn8SacbSrYisuWg`</summary>

```text
195	
196	**Implementation Details.** For RPE, we set  $\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.
197	
198	&lt;table border="1">
199	&lt;thead>
200	&lt;tr>
201	&lt;th>Model&lt;/th>
202	&lt;th># Samples&lt;/th>
203	&lt;th>GSM8K&lt;/th>
204	&lt;th>MATH&lt;/th>
205	&lt;th>Olympiad Bench&lt;/th>
206	&lt;th>Omni-MATH&lt;/th>
207	&lt;th>Avg.&lt;/th>
208	&lt;/tr>
209	&lt;/thead>
210	&lt;tbody>
211	&lt;tr>
212	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>
213	&lt;/tr>
214	&lt;tr>
215	&lt;td>GPT-4o-0806&lt;/td>
216	&lt;td>unk&lt;/td>
217	&lt;td>79.2&lt;/td>
218	&lt;td>63.6&lt;/td>
219	&lt;td>51.4&lt;/td>
220	&lt;td>53.5&lt;/td>
221	&lt;td>61.9&lt;/td>
222	&lt;/tr>
223	&lt;tr>
224	&lt;td>o1-mini&lt;/td>
225	&lt;td>unk&lt;/td>
226	&lt;td>93.2&lt;/td>
227	&lt;td>88.9&lt;/td>
228	&lt;td>87.2&lt;/td>
229	&lt;td>82.4&lt;/td>
230	&lt;td>87.9&lt;/td>
231	&lt;/tr>
232	&lt;tr>
233	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>
234	&lt;/tr>
235	&lt;tr>
236	&lt;td>Skywork-PRM-1.5B&lt;/td>
237	&lt;td>unk&lt;/td>
238	&lt;td>&lt;b>59.0&lt;/b>&lt;/td>
239	&lt;td>48.0&lt;/td>
240	&lt;td>19.3&lt;/td>
241	&lt;td>19.2&lt;/td>
242	&lt;td>36.4&lt;/td>
243	&lt;/tr>
244	&lt;tr>
245	&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>
246	&lt;td>23K&lt;/td>
247	&lt;td>52.8&lt;/td>
248	&lt;td>&lt;b>66.6&lt;/b>&lt;/td>
249	&lt;td>&lt;b>55.1&lt;/b>&lt;/td>
250	&lt;td>&lt;b>54.5&lt;/b>&lt;/td>
251	&lt;td>&lt;b>57.3&lt;/b>&lt;/td>
252	&lt;/tr>
253	&lt;tr>
254	&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>
255	&lt;td>23K&lt;/td>
256	&lt;td>51.3&lt;/td>
257	&lt;td>&lt;b>74.4&lt;/b>&lt;/td>
258	&lt;td>&lt;b>65.3&lt;/b>&lt;/td>
259	&lt;td>&lt;b>62.5&lt;/b>&lt;/td>
260	&lt;td>&lt;b>63.4&lt;/b>&lt;/td>
261	&lt;/tr>
262	&lt;tr>
263	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>
264	&lt;/tr>
265	&lt;tr>
266	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
267	&lt;td>445K&lt;/td>
268	&lt;td>47.9&lt;/td>
269	&lt;td>29.5&lt;/td>
270	&lt;td>24.8&lt;/td>
271	&lt;td>23.8&lt;/td>
272	&lt;td>31.5&lt;/td>
273	&lt;/tr>
274	&lt;tr>
275	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
276	&lt;td>273K&lt;/td>
277	&lt;td>50.4&lt;/td>
278	&lt;td>33.4&lt;/td>
279	&lt;td>13.8&lt;/td>
280	&lt;td>15.8&lt;/td>
281	&lt;td>28.4&lt;/td>
282	&lt;/tr>
283	&lt;tr>
284	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
285	&lt;td>253K&lt;/td>
286	&lt;td>38.8&lt;/td>
287	&lt;td>33.8&lt;/td>
288	&lt;td>16.9&lt;/td>
289	&lt;td>16.9&lt;/td>
290	&lt;td>26.6&lt;/td>
291	&lt;/tr>
292	&lt;tr>
293	&lt;td>Skywork-PRM-7B&lt;/td>
294	&lt;td>unk&lt;/td>
295	&lt;td>70.8&lt;/td>
296	&lt;td>53.6&lt;/td>
297	&lt;td>22.9&lt;/td>
298	&lt;td>21.0&lt;/td>
299	&lt;td>42.1&lt;/td>
300	&lt;/tr>
301	&lt;tr>
302	&lt;td>EurusPRM-Stage1&lt;/td>
303	&lt;td>463K&lt;/td>
304	&lt;td>44.3&lt;/td>
305	&lt;td>35.6&lt;/td>
306	&lt;td>21.7&lt;/td>
307	&lt;td>23.1&lt;/td>
308	&lt;td>31.2&lt;/td>
309	&lt;/tr>
310	&lt;tr>
311	&lt;td>EurusPRM-Stage2&lt;/td>
312	&lt;td>30K&lt;/td>
313	&lt;td>47.3&lt;/td>
314	&lt;td>35.7&lt;/td>
315	&lt;td>21.2&lt;/td>
316	&lt;td>20.9&lt;/td>
317	&lt;td>31.3&lt;/td>
318	&lt;/tr>
319	&lt;tr>
320	&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>
321	&lt;td>445K&lt;/td>
322	&lt;td>62.5&lt;/td>
323	&lt;td>31.6&lt;/td>
324	&lt;td>13.7&lt;/td>
325	&lt;td>7.7&lt;/td>
326	&lt;td>28.9&lt;/td>
327	&lt;/tr>
328	&lt;tr>
329	&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>
330	&lt;td>264K&lt;/td>
331	&lt;td>68.2&lt;/td>
332	&lt;td>62.6&lt;/td>
333	&lt;td>50.7&lt;/td>
334	&lt;td>44.3&lt;/td>
335	&lt;td>56.5&lt;/td>
336	&lt;/tr>
337	&lt;tr>
338	&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>
339	&lt;td>~344K&lt;/td>
340	&lt;td>82.4&lt;/td>
341	&lt;td>77.6&lt;/td>
342	&lt;td>67.5&lt;/td>
343	&lt;td>66.3&lt;/td>
344	&lt;td>73.5&lt;/td>
345	&lt;/tr>
346	&lt;tr>
347	&lt;td>RetrievalPRM-7B&lt;/td>
348	&lt;td>404K&lt;/td>
349	&lt;td>74.6&lt;/td>
350	&lt;td>71.1&lt;/td>
351	&lt;td>60.2&lt;/td>
352	&lt;td>57.3&lt;/td>
353	&lt;td>65.8&lt;/td>
354	&lt;/tr>
355	&lt;tr>
356	&lt;td>Universal-PRM-7B&lt;/td>
357	&lt;td>unk&lt;/td>
358	&lt;td>&lt;b>85.8&lt;/b>&lt;/td>
359	&lt;td>77.7&lt;/td>
360	&lt;td>67.6&lt;/td>
361	&lt;td>66.4&lt;/td>
362	&lt;td>74.3&lt;/td>
363	&lt;/tr>
364	&lt;tr>
365	&lt;td>Direct Generative PRM-7B&lt;/td>
366	&lt;td>23K&lt;/td>
367	&lt;td>63.9&lt;/td>
368	&lt;td>65.8&lt;/td>
369	&lt;td>54.5&lt;/td>
370	&lt;td>55.9&lt;/td>
371	&lt;td>60.0&lt;/td>
372	&lt;/tr>
373	&lt;tr>
374	&lt;td>GenPRM-7B (Pass@1)&lt;/td>
375	&lt;td>23K&lt;/td>
376	&lt;td>78.7&lt;/td>
377	&lt;td>&lt;b>80.3&lt;/b>&lt;/td>
378	&lt;td>&lt;b>72.2&lt;/b>&lt;/td>
379	&lt;td>&lt;b>69.8&lt;/b>&lt;/td>
380	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
381	&lt;/tr>
382	&lt;tr>
383	&lt;td>GenPRM-7B (Maj@8)&lt;/td>
384	&lt;td>23K&lt;/td>
385	&lt;td>81.0&lt;/td>
386	&lt;td>&lt;b>85.7&lt;/b>&lt;/td>
387	&lt;td>&lt;b>78.4&lt;/b>&lt;/td>
388	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
389	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
390	&lt;/tr>
391	&lt;tr>
392	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>
393	&lt;/tr>
394	&lt;tr>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7207e25-1361-4797-83ce-efcd0a0eb582",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "25b740f1-5d4e-4cc5-b316-45d4c71ebfff",
  "sourceToolAssistantUUID": "d7207e25-1361-4797-83ce-efcd0a0eb582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-27T17:50:30.949Z_

Excellent! Now I have the detailed GenPRM table. Let me read the rest.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25b740f1-5d4e-4cc5-b316-45d4c71ebfff",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVnQdAfq2jAndnYEww4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ebdec4f-2415-49d7-8b16-993defb59f96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4yuWkp1oiYAwUjXS8C2E8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 68589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3090,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 88 · 2026-05-27T17:50:32.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DS9yyzYFUxJxipmCBarGgk`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/f12ec80c-3a4b-490a-a484-f7b2a064cfa9/tool-results/toolu_01CQ3T7wbK1gnMAfNPPdsdef.txt",
  "offset": 393,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ebdec4f-2415-49d7-8b16-993defb59f96",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVnQdAfq2jAndnYEww4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "986a74ef-d936-4453-ada8-5b9fe93a1eec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4yuWkp1oiYAwUjXS8C2E8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 68589,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 68589,
          "cache_creation_input_tokens": 3090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3090,
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

_source line 89 · 2026-05-27T17:50:32.161Z_

<details><summary>↩ Tool result · `toolu_01DS9yyzYFUxJxipmCBarGgk`</summary>

```text
393	&lt;/tr>
394	&lt;tr>
395	&lt;td>Dyve-14B&lt;/td>
396	&lt;td>117K&lt;/td>
397	&lt;td>68.5&lt;/td>
398	&lt;td>58.3&lt;/td>
399	&lt;td>49.0&lt;/td>
400	&lt;td>47.2&lt;/td>
401	&lt;td>55.8&lt;/td>
402	&lt;/tr>
403	&lt;tr>
404	&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>
405	&lt;td>~344K&lt;/td>
406	&lt;td>&lt;b>87.3&lt;/b>&lt;/td>
407	&lt;td>80.6&lt;/td>
408	&lt;td>74.3&lt;/td>
409	&lt;td>71.1&lt;/td>
410	&lt;td>78.3&lt;/td>
411	&lt;/tr>
412	&lt;tr>
413	&lt;td>GenPRM-32B (Pass@1)&lt;/td>
414	&lt;td>23K&lt;/td>
415	&lt;td>83.1&lt;/td>
416	&lt;td>&lt;b>81.7&lt;/b>&lt;/td>
417	&lt;td>72.8&lt;/td>
418	&lt;td>&lt;b>72.8&lt;/b>&lt;/td>
419	&lt;td>77.6&lt;/td>
420	&lt;/tr>
421	&lt;tr>
422	&lt;td>GenPRM-32B (Maj@8)&lt;/td>
423	&lt;td>23K&lt;/td>
424	&lt;td>85.1&lt;/td>
425	&lt;td>&lt;b>86.3&lt;/b>&lt;/td>
426	&lt;td>&lt;b>78.9&lt;/b>&lt;/td>
427	&lt;td>&lt;b>80.1&lt;/b>&lt;/td>
428	&lt;td>&lt;b>82.6&lt;/b>&lt;/td>
429	&lt;/tr>
430	&lt;/tbody>
431	&lt;/table>
432	
433	## 4.2. ProcessBench Results
434	
435	**GenPRM outperforms classification-based PRMs on ProcessBench.** As shown in Table 1, GenPRM-7B significantly outperforms direct generative PRM and surpasses **all** previous PRMs with parameters less than 72B on ProcessBench. Also, GenPRM-1.5B outperforms Skywork-PRM-1.5B by a large margin. It is noteworthy that GenPRM is trained with merely **23K** data from **MATH** (Hendrycks et al., 2021) only. By comparing the detailed results in Table 6, we can find that the performance gain of GenPRM mainly comes from the stronger abilities of finding **erroneous** steps and we provide concrete cases in Appendix C. These results demonstrating the superiority of generative modeling of PRM.
436	
437	**GenPRM enables smaller PRMs surpass 10 $\times$  larger PRMs and GPT-4o via TTS.** We also compare the TTS results of GenPRM in Table 1 and find that GenPRM-1.5B surpasses GPT-4 and GenPRM-7B exceeds Qwen2.5-Math-PRM-72B on ProcessBench via simply majority voting, showing that scaling test-time compute is highly effective for GenPRM. We also find that the performance improvement of scaling the test-time compute on **harder** problems is larger than that of easier questions.### 4.3. Policy Model Test-Time Scaling Results
438	
439	**GenPRM as a Verifier.** The results in Figure 4 (a)-(d) show that GenPRM outperforms the baselines on MATH, AMC23, AIME24, and Minerva Math with Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) as the generation model. The advantage of GenPRM becomes larger by scaling the test-time compute of GenPRM and the generation model. Figure 4 (e)-(h) demonstrates that GenPRM generalizes well to responses with Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as the generation model.
440	
441	**Figure 4:** BoN results with different generation models on multiple mathematical benchmarks.
442	
443	**GenPRM as a Critic.** We also conduct experiments by using GenPRM as a critic to refine the outputs of the policy model. The results in Table 2 and Figure 1 (right) show that GenPRM exhibits strong critique abilities than the baselines, significantly improving the performance of the policy model and the performance continues to increase with more refinement based on the critic feedback.
444	
445	### 4.4. Analysis
446	
447	**Label Estimation Method and Criterion.** To explore how different label estimation influences GenPRM, we conduct experiments with the following methods: (1) hard label (Wang et al., 2024b; Zhang et al., 2025c); (2) RPE in (10); and (3) a RPE variant ( $P_t = MC(s_t, a_t) - MC(s_t)$ ). For the RPE and its variant, we use different thresholds  $\epsilon$  for evaluation and set the labels as correct by checking whether  $P_t \geq \epsilon$ . The results in Table 3 show that RPE and its variant outperforms hard label estimation and RPE with  $\epsilon = 0.8$  achieves the best result. By scaling test-time compute with majority voting, the results in Table 4 demonstrate that RPE with  $\epsilon = 0.8$  still reaches the best.**Table 2:** Results of critique refinement experiments. The results of GenPRM are shaded. For each refinement turn, the highest values are **bolded**.
448	
449	&lt;table border="1">
450	&lt;thead>
451	&lt;tr>
452	&lt;th rowspan="2">Critic Model&lt;/th>
453	&lt;th colspan="5">Gemma-3-12b-it as Generator&lt;/th>
454	&lt;th colspan="5">Qwen2.5-7B-Instruct as Generator&lt;/th>
455	&lt;th rowspan="2">Avg.&lt;/th>
456	&lt;/tr>
457	&lt;tr>
458	&lt;th>AMC23&lt;/th>
459	&lt;th>AIME24&lt;/th>
460	&lt;th>MATH&lt;/th>
461	&lt;th>Minerva Math&lt;/th>
462	&lt;th>Avg.&lt;/th>
463	&lt;th>AMC23&lt;/th>
464	&lt;th>AIME24&lt;/th>
465	&lt;th>MATH&lt;/th>
466	&lt;th>Minerva Math&lt;/th>
467	&lt;th>Avg.&lt;/th>
468	&lt;/tr>
469	&lt;/thead>
470	&lt;tbody>
471	&lt;tr>
472	&lt;td>Zero-shot&lt;/td>
473	&lt;td>64.1&lt;/td>
474	&lt;td>15.8&lt;/td>
475	&lt;td>83.8&lt;/td>
476	&lt;td>31.9&lt;/td>
477	&lt;td>48.9&lt;/td>
478	&lt;td>51.6&lt;/td>
479	&lt;td>7.1&lt;/td>
480	&lt;td>76.2&lt;/td>
481	&lt;td>34.5&lt;/td>
482	&lt;td>42.4&lt;/td>
483	&lt;td>45.7&lt;/td>
484	&lt;/tr>
485	&lt;tr>
486	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 1&lt;/i>&lt;/td>
487	&lt;/tr>
488	&lt;tr>
489	&lt;td>Generator&lt;/td>
490	&lt;td>66.6&lt;/td>
491	&lt;td>15.8&lt;/td>
492	&lt;td>84.7&lt;/td>
493	&lt;td>33.3&lt;/td>
494	&lt;td>50.1&lt;/td>
495	&lt;td>50.6&lt;/td>
496	&lt;td>8.0&lt;/td>
497	&lt;td>76.8&lt;/td>
498	&lt;td>34.0&lt;/td>
499	&lt;td>42.4&lt;/td>
500	&lt;td>46.3&lt;/td>
501	&lt;/tr>
502	&lt;tr>
503	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
504	&lt;td>69.1&lt;/td>
505	&lt;td>17.9&lt;/td>
506	&lt;td>84.6&lt;/td>
507	&lt;td>33.0&lt;/td>
508	&lt;td>51.2&lt;/td>
509	&lt;td>50.6&lt;/td>
510	&lt;td>6.3&lt;/td>
511	&lt;td>77.7&lt;/td>
512	&lt;td>34.7&lt;/td>
513	&lt;td>42.3&lt;/td>
514	&lt;td>46.8&lt;/td>
515	&lt;/tr>
516	&lt;tr>
517	&lt;td>GenPRM-7B&lt;/td>
518	&lt;td>&lt;b>74.1&lt;/b>&lt;/td>
519	&lt;td>&lt;b>19.6&lt;/b>&lt;/td>
520	&lt;td>&lt;b>86.0&lt;/b>&lt;/td>
521	&lt;td>&lt;b>35.3&lt;/b>&lt;/td>
522	&lt;td>&lt;b>53.8&lt;/b>&lt;/td>
523	&lt;td>&lt;b>57.5&lt;/b>&lt;/td>
524	&lt;td>&lt;b>8.3&lt;/b>&lt;/td>
525	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
526	&lt;td>&lt;b>36.5&lt;/b>&lt;/td>
527	&lt;td>&lt;b>45.7&lt;/b>&lt;/td>
528	&lt;td>&lt;b>49.8&lt;/b>&lt;/td>
529	&lt;/tr>
530	&lt;tr>
531	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 2&lt;/i>&lt;/td>
532	&lt;/tr>
533	&lt;tr>
534	&lt;td>Generator&lt;/td>
535	&lt;td>66.6&lt;/td>
536	&lt;td>18.0&lt;/td>
537	&lt;td>84.8&lt;/td>
538	&lt;td>31.6&lt;/td>
539	&lt;td>50.3&lt;/td>
540	&lt;td>49.8&lt;/td>
541	&lt;td>8.0&lt;/td>
542	&lt;td>76.9&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "986a74ef-d936-4453-ada8-5b9fe93a1eec",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "32125d35-1a4e-45b7-932f-0616859b622a",
  "sourceToolAssistantUUID": "986a74ef-d936-4453-ada8-5b9fe93a1eec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 90 · 2026-05-27T17:50:35.121Z_

Now I have comprehensive data. Let me do a few more searches for the most recent developments and the ProcessBench paper's original baseline numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32125d35-1a4e-45b7-932f-0616859b622a",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVngMDUHtdZM6H5xujm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85c8c022-85e3-45a4-a804-0e3187376347",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY3FWmW4S3vMstdPn7NyKU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 71679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2700,
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

_source line 91 · 2026-05-27T17:50:36.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DAq9NBBPoXVUBXesDkAvqu`</summary>

```json
{
  "query": "\"ProcessBench\" paper 2025 2026 new results SOTA beyond GenPRM ActPRM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85c8c022-85e3-45a4-a804-0e3187376347",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVngMDUHtdZM6H5xujm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92ca25c9-1f04-4f99-89f2-f9ca06fed0f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY3FWmW4S3vMstdPn7NyKU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 71679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2700,
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

_source line 92 · 2026-05-27T17:50:36.771Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PusbztW5Po3S5FSH1a8k3H`</summary>

```json
{
  "query": "Qwen2.5-Math-PRM-72B ProcessBench 78.3 F1 average score original paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92ca25c9-1f04-4f99-89f2-f9ca06fed0f3",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVngMDUHtdZM6H5xujm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dab71716-e20c-450c-8352-640412d54d2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY3FWmW4S3vMstdPn7NyKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 71679,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2700
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 71679,
          "cache_creation_input_tokens": 2700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2700,
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

_source line 93 · 2026-05-27T17:50:42.001Z_

<details><summary>↩ Tool result · `toolu_01PusbztW5Po3S5FSH1a8k3H`</summary>

```text
Web search results for query: "Qwen2.5-Math-PRM-72B ProcessBench 78.3 F1 average score original paper"

Links: [{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"},{"title":"Qwen/Qwen2.5-Math-PRM-72B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"README.md · Qwen/Qwen2.5-Math-PRM-7B at main","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md"},{"title":"Qwen/Qwen2.5-Math-PRM-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B"},{"title":"Qwen2.5-Math-PRM-72B","url":"https://www.promptlayer.com/models/qwen25-math-prm-72b"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"arXiv:2501.07301v2 [cs.CL] 5 Jun 2025 2025-06-12","url":"https://arxiv.org/pdf/2501.07301"}]

Based on the search results, Qwen2.5-Math-PRM-72B achieves an average F1 score of 78.3 on the ProcessBench benchmark.

The original paper appears to be "PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning," which reports F1 scores on the benchmark. This paper is available at arxiv.org/pdf/2412.06559.

Additionally, ProcessBench aims to measure the model's ability to identify erroneous steps in mathematical reasoning and consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dab71716-e20c-450c-8352-640412d54d2f",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "8df681e1-e11a-402b-b76f-528fce8800f2",
  "sourceToolAssistantUUID": "dab71716-e20c-450c-8352-640412d54d2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-27T17:50:46.071Z_

<details><summary>↩ Tool result · `toolu_01DAq9NBBPoXVUBXesDkAvqu`</summary>

```text
Web search results for query: ""ProcessBench" paper 2025 2026 new results SOTA beyond GenPRM ActPRM"

Links: [{"title":"Will SotA on PaperBench (Code-Dev) surpass 75% in 2025? | Manifold","url":"https://manifold.markets/SamuelAlbanie/will-sota-on-paperbench-codedev-sur"},{"title":"Accounting for multiplicity in machine learning benchmark performance","url":"https://arxiv.org/pdf/2303.07272"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"CodeSOTA: The Open, Callable Registry of State of the Art","url":"https://www.codesota.com/"}]

I found some results, but they relate to PaperBench and PRMBench rather than ProcessBench. Let me search more specifically for ProcessBench with the GenPRM and ActPRM references.

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=ProcessBench+dataset"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/pdf/2504.10559"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM Framework Overview","url":"https://www.emergentmind.com/topics/genprm-framework"}]

Perfect! I found relevant information about ProcessBench with both GenPRM and ActPRM. Based on the search results, here's what I found:

## ProcessBench Results: GenPRM and ActPRM Performance

### GenPRM (April 2025)
GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset, with a 1.5B GenPRM outperforming GPT-4o, and a 7B GenPRM surpassing Qwen2.5-Math-PRM-72B on ProcessBench. More specifically, scaling the model from 1.5B to 7B parameters yields substantial performance gains (57.3 →75.2 and 63.4 →80.5) on ProcessBench.

### ActPRM (April 2025)
ActPRM achieved new SOTA performance of 75.0% on ProcessBench after annotation and fine-tuning. ActPRM surpasses prior SOTA models with significantly lower costs—outperforming UniversalPRM by 0.7% using only 20% of its annotation budget and exceeding Qwen2.5-Math-PRM-7B by 1.5% with just 6% of its annotation budget.

### Key Innovation
ActPRM reduces 50% annotation while achieving comparable or even better performance compared to vanilla fine-tuning in pool-based active learning settings.

Both models represent advances in process reward modeling that go beyond earlier approaches, with GenPRM focusing on generative reasoning with test-time scaling and ActPRM emphasizing annotation efficiency through active learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92ca25c9-1f04-4f99-89f2-f9ca06fed0f3",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "a305ebbe-32f3-4500-9e7d-2c20c71ab6ca",
  "sourceToolAssistantUUID": "92ca25c9-1f04-4f99-89f2-f9ca06fed0f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-27T17:50:50.915Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BF11iQRwiouf55dXN4LwZh`</summary>

```json
{
  "url": "https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md",
  "prompt": "Extract ALL ProcessBench F1 scores mentioned. I need the complete table of results for Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, and all baseline models. Include per-subset scores (GSM8K, MATH, OlympiadBench, OmniMATH) and averages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a305ebbe-32f3-4500-9e7d-2c20c71ab6ca",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVohRVDgSx7WotCTWNc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8721de14-9c3a-4a6b-89f0-852e94b3788f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9vbsQ6DHWMGf4Hdphxvxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 646,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 74379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 96 · 2026-05-27T17:50:51.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H34B6htg95eWuZbcH2fpfk`</summary>

```json
{
  "query": "ThinkPRM ProcessBench F1 score exact number 14B 7B 1.5B OlympiadBench OmniMath"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8721de14-9c3a-4a6b-89f0-852e94b3788f",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVohRVDgSx7WotCTWNc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77942071-07e5-4c40-b5d6-f7b59cee68be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9vbsQ6DHWMGf4Hdphxvxm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 646,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 74379,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 646,
          "output_tokens": 257,
          "cache_read_input_tokens": 74379,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1410,
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

_source line 97 · 2026-05-27T17:50:54.859Z_

<details><summary>↩ Tool result · `toolu_01BF11iQRwiouf55dXN4LwZh`</summary>

```text
# ProcessBench F1 Scores - Not Available in Provided Content

The webpage content you provided does **not include** the ProcessBench F1 scores table. 

## What the Page Contains

The README mentions:
- Reference to ProcessBench paper: arxiv: 2412.06559
- Statement that PRMs show "stronger error identification performance in [ProcessBench](https://huggingface.co/papers/2412.06559)"
- A link to the paper for more details

## Where to Find the Scores

To access the complete ProcessBench F1 score tables with:
- Qwen2.5-Math-PRM-7B results
- Qwen2.5-Math-PRM-72B results
- Baseline model comparisons
- Per-subset scores (GSM8K, MATH, OlympiadBench, OmniMATH)
- Average scores

**You need to consult:**
1. **The linked paper**: https://arxiv.org/pdf/2501.07301
2. **ProcessBench paper**: https://huggingface.co/papers/2412.06559

The model card README focuses on usage instructions and quick-start code rather than comprehensive benchmark results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8721de14-9c3a-4a6b-89f0-852e94b3788f",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "abc48f8e-2984-4912-8c6a-c1636c09cd24",
  "sourceToolAssistantUUID": "8721de14-9c3a-4a6b-89f0-852e94b3788f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-27T17:50:56.778Z_

<details><summary>↩ Tool result · `toolu_01H34B6htg95eWuZbcH2fpfk`</summary>

```text
Web search results for query: "ThinkPRM ProcessBench F1 score exact number 14B 7B 1.5B OlympiadBench OmniMath"

Links: [{"title":"Papers Explained 368: ThinkPRM. ThinkPRM, a long CoT verifier… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-368-thinkprm-0f530cc98ca4"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Published in Transactions on Machine Learning Research (03/2026)","url":"https://openreview.net/pdf?id=FPVCb0WMuN"},{"title":"ThinkPRM: More Than Just Chain-of-Thought (CoT 2.0)","url":"https://www.llmwatch.com/p/thinkprm-more-than-just-chain-of"},{"title":"LLM Benchmarks | EvalScope - Read the Docs","url":"https://evalscope.readthedocs.io/en/v1.0.0/get_started/supported_dataset/llm.html"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"📉 May the Best Cheater Win - LLM Watch","url":"https://www.llmwatch.com/p/may-the-best-cheater-win"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large   Language Models","url":"https://arxiv.org/pdf/2410.07985"}]

Based on the search results, here are the exact F1 score numbers for ThinkPRM on ProcessBench:

ThinkPRM-14B achieves 86.5% F1 score on ProcessBench.

The search results indicate that the F1-score is reported over the two most challenging subsets of ProcessBench: OlympiadBench and OmniMath, each comprising 1K problem-prefix pairs, so the 86.5% represents the average performance on these two subsets combined.

However, the search results do not contain the exact separate F1 scores for the 7B and 1.5B model variants on ProcessBench, nor do they provide the broken-down scores for OlympiadBench and OmniMath individually. The search results do mention that ThinkPRM-1.5B outperforms LLM-as-a-judge and discriminative verifiers in reward-guided search on MATH-500, but this is for a different benchmark (MATH-500) rather than ProcessBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77942071-07e5-4c40-b5d6-f7b59cee68be",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "6ff154a2-3107-48ed-9db5-dfa27c6f146a",
  "sourceToolAssistantUUID": "77942071-07e5-4c40-b5d6-f7b59cee68be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-27T17:51:01.324Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MePKM6D5sYbP4AgUf2GVHp`</summary>

```json
{
  "url": "https://ritvik19.medium.com/papers-explained-368-thinkprm-0f530cc98ca4",
  "prompt": "Extract ALL ProcessBench F1 scores for ThinkPRM models. I need exact numerical F1 scores for ThinkPRM-1.5B, ThinkPRM-7B, ThinkPRM-14B, ThinkPRM-QwQ-32B, and their corresponding LLM-as-a-judge baselines on ProcessBench. Include OlympiadBench and OmniMath subset scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff154a2-3107-48ed-9db5-dfa27c6f146a",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVpVDYPXpHoTC7woR4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6699b61d-2c3e-431e-b0e7-9a067f7d22de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEEhMG4bijRU8ND97MvYCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1977,
      "cache_read_input_tokens": 75789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 100 · 2026-05-27T17:51:04.508Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015GLNBwQr9ZNfri3CC9RdH6`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.16828v5",
  "prompt": "Find Table 3 in the appendix which shows 'Average F1-score on OlympiadBench and OmniMath subsets of ProcessBench comparing LLM-as-a-Judge to ThinkPRM'. Extract ALL exact F1 scores from this table for every model listed including ThinkPRM-1.5B, ThinkPRM-7B, ThinkPRM-14B, QwQ-32B variants, and all LLM-as-a-judge baselines. Also find Table 1 showing verification F1 when training on long vs short CoTs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6699b61d-2c3e-431e-b0e7-9a067f7d22de",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVpVDYPXpHoTC7woR4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f06e94ca-1a11-4888-8049-aa7aa31426bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEEhMG4bijRU8ND97MvYCC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1977,
      "cache_read_input_tokens": 75789,
      "output_tokens": 395,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1977
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 395,
          "cache_read_input_tokens": 75789,
          "cache_creation_input_tokens": 1977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1977,
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

_source line 101 · 2026-05-27T17:51:05.003Z_

<details><summary>↩ Tool result · `toolu_01MePKM6D5sYbP4AgUf2GVHp`</summary>

```text
# ThinkPRM ProcessBench F1 Scores

Based on the provided content, **specific numerical F1 scores for individual ThinkPRM models are not included in this article**. 

The article references one comparison chart showing "Average F1-score on OlympiadBench and OmniMath subsets of ProcessBench," but the actual numerical values are embedded in an image that cannot be read from the text content provided.

The document states that "The verification quality is highly sensitive to instruction wording" and discusses comparative performance, but does not list discrete F1-score metrics for ThinkPRM-1.5B, ThinkPRM-14B, or the other variants you requested.

To obtain the exact F1 scores you're seeking, you would need to:
- Access the original research paper (arXiv 2504.16828)
- View the actual image charts in the Medium article
- Consult the GitHub repository referenced in the piece
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6699b61d-2c3e-431e-b0e7-9a067f7d22de",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "58270087-8ba1-43b7-b1b2-44fe05c11d68",
  "sourceToolAssistantUUID": "6699b61d-2c3e-431e-b0e7-9a067f7d22de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-27T17:51:09.918Z_

<details><summary>↩ Tool result · `toolu_015GLNBwQr9ZNfri3CC9RdH6`</summary>

```text
# F1-Score Extraction from Tables

## Table 3: ProcessBench Results (OlympiadBench and OmniMath)

| Model | OlympiadBench LLM-as-Judge | OmniMath LLM-as-Judge | OlympiadBench ThinkPRM | OmniMath ThinkPRM |
|-------|----------------------------|----------------------|------------------------|-------------------|
| R1-Qwen-1.5B | 5.0 | 5.4 | 76.3 | 75.7 |
| R1-Qwen-7B | 44.8 | 45.7 | 73.4 | 74.0 |
| R1-Qwen-14B | 72.8 | 67.8 | 87.3 | 85.7 |
| QwQ-32B-preview | 50.6 | 55.5 | 73.1 | 73.2 |

**Note:** The table also reports percentages of problematic outputs (shown in red) for LLM-as-judge variants, ranging from 7.9% to 55.1%.

## Table 1: Long vs. Short CoT Comparison

| Model | Long CoT (OlympiadBench) | Short CoT (OlympiadBench) | Long CoT (OmniMath) | Short CoT (OmniMath) |
|-------|--------------------------|---------------------------|---------------------|----------------------|
| R1-Qwen-1.5B | 87.3 | 64.8 | 75.7 | 66.7 |
| R1-Qwen-14B | 87.3 | 55.3 | 85.7 | 60.8 |

The data demonstrates that "extended reasoning substantially improves performance" when training verification models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f06e94ca-1a11-4888-8049-aa7aa31426bc",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "c10db40e-e71e-49b9-9e3c-bb70e84c8bae",
  "sourceToolAssistantUUID": "f06e94ca-1a11-4888-8049-aa7aa31426bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-27T17:51:13.032Z_

Now I have comprehensive data from ThinkPRM too. Let me get a couple more pieces of information to round out the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c10db40e-e71e-49b9-9e3c-bb70e84c8bae",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVqTLi8iJvcidQutRFV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3b75611-3516-4a56-aba4-c0aa861c309b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qy9cihtwsRYqJtJmfzpt3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 77766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 104 · 2026-05-27T17:51:13.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YF1GZnx5c2APVP15263XAb`</summary>

```json
{
  "query": "\"Is PRM Necessary\" ProcessBench results RL implicit PRM capability 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3b75611-3516-4a56-aba4-c0aa861c309b",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVqTLi8iJvcidQutRFV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c350c8d8-c448-483b-9515-2b14ef214302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qy9cihtwsRYqJtJmfzpt3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 77766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 105 · 2026-05-27T17:51:14.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K675AVFVgYcKsRKj5ti76G`</summary>

```json
{
  "query": "PRMBench results leaderboard 2025 best model Gemini scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c350c8d8-c448-483b-9515-2b14ef214302",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVqTLi8iJvcidQutRFV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cc5d19f-2f22-4d4a-bb90-6a6a00a48b5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qy9cihtwsRYqJtJmfzpt3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 77766,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 77766,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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

_source line 106 · 2026-05-27T17:51:19.332Z_

<details><summary>↩ Tool result · `toolu_01K675AVFVgYcKsRKj5ti76G`</summary>

```text
Web search results for query: "PRMBench results leaderboard 2025 best model Gemini scores"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"Gemini 3 Pro scores 69% trust in blinded testing up from 16% for Gemini 2.5: The case for evaluating AI on real-world trust, not academic benchmarks | VentureBeat","url":"https://venturebeat.com/ai/gemini-3-pro-scores-69-trust-in-blinded-testing-up-from-16-for-gemini-2-5"},{"title":"AI Model Leaderboard: LMArena ELO and Benchmark Scores - Lambda Finance","url":"https://www.lambdafin.com/articles/ai-model-leaderboard"},{"title":"Google Gemini 3 Benchmarks (Explained) - Vellum","url":"https://www.vellum.ai/blog/google-gemini-3-benchmarks"},{"title":"Google unveils Gemini 3 claiming the lead in math, science, multimodal, and agentic AI benchmarks | VentureBeat","url":"https://venturebeat.com/ai/google-unveils-gemini-3-claiming-the-lead-in-math-science-multimodal-and"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad","url":"https://arxiv.org/pdf/2503.21934"}]

Based on the search results, here's what I found about PRMBench and Gemini model scores:

## PRMBench Results

Gemini-2-Thinking achieves the best performance of 68.8 on PRMBench, but still significantly falls behind the human performance of 83.8.

The PRMBench is the first comprehensive process-level reward model benchmark, comprising 6,216 carefully curated samples and 83,456 step-level labels for evaluations on process-level reward models. The benchmark evaluates models on their ability to assess the correctness of intermediate reasoning steps.

The benchmark includes models such as ReasonEval-7B, Math-Shepherd-7B, and Gemini-2.0-flash-thinking, among others evaluated in the research.

If you're looking for a complete leaderboard with all model rankings and detailed scores across all categories, you can access the official PRMBench website at https://prmbench.github.io/, which contains interactive leaderboard data that can be expanded to show detailed results by category.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cc5d19f-2f22-4d4a-bb90-6a6a00a48b5b",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "e1912217-72f7-462f-ae54-248dec154d29",
  "sourceToolAssistantUUID": "3cc5d19f-2f22-4d4a-bb90-6a6a00a48b5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-27T17:51:19.452Z_

<details><summary>↩ Tool result · `toolu_01YF1GZnx5c2APVP15263XAb`</summary>

```text
Web search results for query: ""Is PRM Necessary" ProcessBench results RL implicit PRM capability 2025"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1230/"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"},{"title":"Dynamic and Generalizable Process Reward Modeling","url":"https://aclanthology.org/2025.acl-long.212.pdf"},{"title":"Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning","url":"https://arxiv.org/html/2601.18984"},{"title":"2025-4-8 GenPRM: Scaling Test-Time Compute of Process","url":"https://arxiv.org/pdf/2504.00891"}]

Based on the search results, I found relevant information about the paper "Is PRM Necessary?" and its ProcessBench results:

## Key Findings

Models trained purely with reinforcement learning (RL), such as DeepSeek-R1 and QwQ-32B, exhibit strong inherent PRM capabilities, despite not being explicitly supervised with PRM-labeled data. These RL-trained models consistently outperform discriminative PRM models that were fine-tuned with RL, without the need for explicit PRM supervision.

The research evaluated these findings on ProcessBench across the GSM8K, MATH, OlympiadBench, and OmniMath datasets, demonstrating that the evaluation results of different LLMs on ProcessBench show that implicit PRM capabilities emerge from problem-solving RL training, questioning whether explicit PRM training is necessary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c350c8d8-c448-483b-9515-2b14ef214302",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "05b5aada-9ec1-4a5c-8cff-00ed345bec33",
  "sourceToolAssistantUUID": "c350c8d8-c448-483b-9515-2b14ef214302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-27T17:51:23.515Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CjS7Eqyc1EDBK2KRTjM2jd`</summary>

```json
{
  "url": "https://prmbench.github.io/",
  "prompt": "Extract the full PRMBench leaderboard with all model names and their scores. I need the top models and their overall scores, plus any category breakdowns. Include scores for Gemini-2-Thinking, QwQ, Qwen2.5-Math-PRM, and any other models listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b5aada-9ec1-4a5c-8cff-00ed345bec33",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVrAANqz6G7kPhVC9gq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4507aa14-51a1-4c2c-87c1-1358cc12be4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKNWWchBs1v3qn46mAHdW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 726,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 78888,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 726,
          "output_tokens": 145,
          "cache_read_input_tokens": 78888,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 709,
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

_source line 109 · 2026-05-27T17:51:27.312Z_

<details><summary>↩ Tool result · `toolu_01CjS7Eqyc1EDBK2KRTjM2jd`</summary>

```text
# PRMBench Leaderboard Data

Based on the webpage content provided, I cannot extract the complete leaderboard with specific numerical scores. The page indicates that:

**Available Information:**
The site contains "a leaderboard on PRMBench" with sections for "Proprietary LLMs" and "Open LLMs," organized by performance categories. The interface mentions clickable tabs for "Simplicity, Soundness, or Sensitivity to expand detailed results."

**Task Categories Referenced:**
The benchmark evaluates models across dimensions including "Non-Redundancy, Non-Circular Logic, Empirically Soundness, Step Consistency, Domain Consistency, Confidence Invariance, Prerequisite Sensitivity, Deception Resistance, and Multi-Solution Consistency."

**Limitation:**
Unfortunately, the actual numerical scores and complete model listings (including Gemini-2-Thinking, QwQ, and Qwen2.5-Math-PRM) are not included in the text content provided. The webpage appears to use interactive JavaScript tables that don't render as plain text. To access the full leaderboard with specific scores, you would need to visit the actual website directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4507aa14-51a1-4c2c-87c1-1358cc12be4c",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "81eb1f5b-ed17-4a2c-b445-2c0fa5f50e5d",
  "sourceToolAssistantUUID": "4507aa14-51a1-4c2c-87c1-1358cc12be4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 110 · 2026-05-27T17:51:30.759Z_

I now have enough data to compile a comprehensive report. Let me also verify one more thing about the ThinkPRM numbers being evaluated on 2 subsets only vs all 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81eb1f5b-ed17-4a2c-b445-2c0fa5f50e5d",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVrjiyoiudoQLttbZHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3b8286f-92d4-4b3a-96a3-938a162713b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KoHyePeDjSPPPUxDn3o1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 79597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 111 · 2026-05-27T17:51:31.361Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uo4wqPnxvatgwHoQwuJZzj`</summary>

```json
{
  "query": "ThinkPRM 14B ProcessBench all four subsets GSM8K MATH OlympiadBench OmniMATH full results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3b8286f-92d4-4b3a-96a3-938a162713b3",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVrjiyoiudoQLttbZHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "035fc76a-d805-40cc-ad92-068ae3c333c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KoHyePeDjSPPPUxDn3o1Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 79597,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 79597,
          "cache_creation_input_tokens": 1141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1141,
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

_source line 112 · 2026-05-27T17:51:37.434Z_

<details><summary>↩ Tool result · `toolu_01Uo4wqPnxvatgwHoQwuJZzj`</summary>

```text
Web search results for query: "ThinkPRM 14B ProcessBench all four subsets GSM8K MATH OlympiadBench OmniMATH full results"

Links: [{"title":"Papers Explained 368: ThinkPRM. ThinkPRM, a long CoT verifier… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-368-thinkprm-0f530cc98ca4"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"LLM Benchmarks | EvalScope - Read the Docs","url":"https://evalscope.readthedocs.io/en/v0.16.3/get_started/supported_dataset/llm.html"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models","url":"https://arxiv.org/html/2410.07985v1"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large   Language Models","url":"https://arxiv.org/pdf/2410.07985"},{"title":"[2410.07985] Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models","url":"https://arxiv.org/abs/2410.07985"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Paper page - Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models","url":"https://huggingface.co/papers/2410.07985"},{"title":"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=yaqPf0KAlN"}]

Based on the search results, I found information about ThinkPRM and ProcessBench. ThinkPRM beats baselines on ProcessBench, and ThinkPRM-14B, trained on 8K process labels or 1K synthetic examples, outperforms discriminative PRMs trained on about 100x more data.

ProcessBench includes various subsets such as GSM8K, Math, OlympiadBench, and OmniMath, each with its own set of problems that require step-by-step reasoning.

However, the search results don't contain the complete numerical results for ThinkPRM 14B across all four ProcessBench subsets. The results mention that the F1-score is reported over the two most challenging subsets of ProcessBench: OlympiadBench and OmniMath, each comprising 1K problem-prefix pairs, but specific numerical values aren't provided in the search results retrieved. You may need to access the full ThinkPRM research paper directly to find the complete results table with all four subset scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "035fc76a-d805-40cc-ad92-068ae3c333c6",
  "isSidechain": true,
  "promptId": "8859a1fe-0495-4fc1-981b-7f8db9d5108e",
  "agentId": "a195100b4dfd60a19",
  "type": "user",
  "uuid": "f9ed6fd6-299c-48fa-bd91-4ca99faf0e92",
  "sourceToolAssistantUUID": "035fc76a-d805-40cc-ad92-068ae3c333c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 113 · 2026-05-27T17:52:51.148Z_

I now have comprehensive data to provide a thorough report. Here is my synthesis:

---

## ProcessBench: State-of-the-Art and PRM Evaluation Landscape (as of May 2026)

### 1. ProcessBench Overview

ProcessBench (Zheng et al., 2024; published at ACL 2025) is the primary benchmark for evaluating process reward models' ability to identify erroneous steps in mathematical reasoning. It contains 3,400 test cases across four subsets of increasing difficulty: **GSM8K**, **MATH**, **OlympiadBench**, and **OmniMATH**. The metric is F1 score (harmonic mean of accuracy on correct and incorrect solutions).

---

### 2. Complete Leaderboard / SOTA on ProcessBench (F1 Scores)

Below is the most comprehensive table, compiled primarily from the GenPRM paper (Zhao et al., AAAI 2026), supplemented by R-PRM (March 2025), ActPRM (April 2025), and ThinkPRM (April 2025; published in TMLR 03/2026).

#### Proprietary LLM Critics
| Model | GSM8K | MATH | OlympiadBench | OmniMATH | **Avg** |
|---|---|---|---|---|---|
| GPT-4o-0806 | 79.2 | 63.6 | 51.4 | 53.5 | **61.9** |
| o1-mini | 93.2 | 88.9 | 87.2 | 82.4 | **87.9** |

#### Discriminative PRMs (7-8B)
| Model | Training Data | GSM8K | MATH | OlympiadBench | OmniMATH | **Avg** |
|---|---|---|---|---|---|---|
| Math-Shepherd-PRM-7B | 445K | 47.9 | 29.5 | 24.8 | 23.8 | **31.5** |
| RLHFlow-PRM-Mistral-8B | 273K | 50.4 | 33.4 | 13.8 | 15.8 | **28.4** |
| RLHFlow-PRM-Deepseek-8B | 253K | 38.8 | 33.8 | 16.9 | 16.9 | **26.6** |
| Skywork-PRM-7B | unk | 70.8 | 53.6 | 22.9 | 21.0 | **42.1** |
| EurusPRM-Stage1 | 463K | 44.3 | 35.6 | 21.7 | 23.1 | **31.2** |
| EurusPRM-Stage2 | 30K | 47.3 | 35.7 | 21.2 | 20.9 | **31.3** |
| Qwen2.5-Math-7B-Math-Shepherd | 445K | 62.5 | 31.6 | 13.7 | 7.7 | **28.9** |
| Qwen2.5-Math-7B-PRM800K | 264K | 68.2 | 62.6 | 50.7 | 44.3 | **56.5** |
| ReasonEval-7B | -- | 41.0 | 48.9 | 36.7 | 37.4 | **~41.0** |
| **Qwen2.5-Math-PRM-7B** | ~344K | 82.4 | 77.6 | 67.5 | 66.3 | **73.5** |
| RetrievalPRM-7B | 404K | 74.6 | 71.1 | 60.2 | 57.3 | **65.8** |
| Universal-PRM-7B | unk | 85.8 | 77.7 | 67.6 | 66.4 | **74.3** |
| R-PRM-7B-DPO | -- | 80.7 | 76.9 | 63.8 | 60.1 | **70.4** |
| ActPRM-7B | ~5% labels | 81.6 | 79.8 | 71.4 | 67.0 | **75.0** |
| **ActPRM-X-7B** | ~5% labels | 82.7 | 82.0 | 72.0 | 67.3 | **76.0** |

#### Discriminative PRMs (1.5B)
| Model | GSM8K | MATH | OlympiadBench | OmniMATH | **Avg** |
|---|---|---|---|---|---|
| Skywork-PRM-1.5B | 59.0 | 48.0 | 19.3 | 19.2 | **36.4** |

#### Larger Discriminative PRMs (14-72B)
| Model | GSM8K | MATH | OlympiadBench | OmniMATH | **Avg** |
|---|---|---|---|---|---|
| Dyve-14B | 68.5 | 58.3 | 49.0 | 47.2 | **55.8** |
| **Qwen2.5-Math-PRM-72B** | 87.3 | 80.6 | 74.3 | 71.1 | **78.3** |

#### Generative PRMs -- GenPRM (AAAI 2026)
| Model | Training Data | GSM8K | MATH | OlympiadBench | OmniMATH | **Avg** |
|---|---|---|---|---|---|---|
| Direct Generative PRM-7B | 23K | 63.9 | 65.8 | 54.5 | 55.9 | **60.0** |
| GenPRM-1.5B (Pass@1) | 23K | 52.8 | 66.6 | 55.1 | 54.5 | **57.3** |
| **GenPRM-1.5B (Maj@8)** | 23K | 51.3 | 74.4 | 65.3 | 62.5 | **63.4** |
| **GenPRM-7B (Pass@1)** | 23K | 78.7 | 80.3 | 72.2 | 69.8 | **75.2** |
| **GenPRM-7B (Maj@8)** | 23K | 81.0 | 85.7 | 78.4 | 76.8 | **80.5** |
| GenPRM-32B (Pass@1) | 23K | 83.1 | 81.7 | 72.8 | 72.8 | **77.6** |
| **GenPRM-32B (Maj@8)** | 23K | 85.1 | 86.3 | 78.9 | 80.1 | **82.6** |

#### Generative PRMs -- ThinkPRM (TMLR 2026)
ThinkPRM evaluates on only the two hardest subsets (OlympiadBench + OmniMATH):

| Model | OlympiadBench | OmniMath | **Avg (2 subsets)** |
|---|---|---|---|
| LLM-as-Judge R1-Qwen-1.5B | 5.0 | 5.4 | **5.2** |
| LLM-as-Judge R1-Qwen-7B | 44.8 | 45.7 | **45.3** |
| LLM-as-Judge R1-Qwen-14B | 72.8 | 67.8 | **70.3** |
| LLM-as-Judge QwQ-32B-Preview | 50.6 | 55.5 | **53.1** |
| **ThinkPRM-1.5B** | 76.3 | 75.7 | **76.0** |
| ThinkPRM-7B | 73.4 | 74.0 | **73.7** |
| **ThinkPRM-14B** | 87.3 | 85.7 | **86.5** |
| ThinkPRM-QwQ-32B | 73.1 | 73.2 | **73.2** |

---

### 3. Key Model Rankings (Approximate SOTA Order)

Considering all 4 subsets where available:
1. **o1-mini** (critic): 87.9 avg F1
2. **GenPRM-32B (Maj@8)**: 82.6 avg F1 (generative, 23K training data)
3. **GenPRM-7B (Maj@8)**: 80.5 avg F1 (generative, 23K training data)
4. **Qwen2.5-Math-PRM-72B**: 78.3 avg F1 (discriminative, ~344K data)
5. **GenPRM-32B (Pass@1)**: 77.6 avg F1
6. **ActPRM-X-7B**: 76.0 avg F1 (discriminative, active learning, ~5% labeling cost)
7. **GenPRM-7B (Pass@1)**: 75.2 avg F1
8. **ActPRM-7B**: 75.0 avg F1
9. **Universal-PRM-7B**: 74.3 avg F1
10. **Qwen2.5-Math-PRM-7B**: 73.5 avg F1

On the two hardest subsets only: **ThinkPRM-14B** achieves 86.5 avg F1 (OlympiadBench + OmniMATH), which would be extremely competitive.

---

### 4. Generative vs. Discriminative Gap

The gap is decisively in favor of generative approaches, especially with test-time scaling:

- **GenPRM-7B (generative, 23K data, Maj@8)** at 80.5 surpasses **Qwen2.5-Math-PRM-72B (discriminative, ~344K data)** at 78.3, despite being 10x smaller and using 15x less training data.
- **GenPRM-1.5B (Maj@8)** at 63.4 surpasses **GPT-4o** at 61.9.
- **ThinkPRM-14B** at 86.5 (on hard subsets) surpasses the corresponding **DiscPRM-14B** trained on the full PRM800K (712K labels) by ~15 F1 points, while using only 1% of the process labels.
- The **Direct Generative PRM-7B** (without CoT/code, same 23K data as GenPRM) scores only 60.0, showing that the CoT reasoning and code verification components are critical to the generative advantage.
- Key insight: generative PRMs have a unique ability to scale test-time compute (via majority voting over multiple verification CoTs), which discriminative PRMs cannot do. This is the main driver of the gap.

---

### 5. New Benchmarks Beyond ProcessBench

Several new PRM benchmarks have emerged:

1. **PRMBench** (ACL 2025): 6,216 samples, 83,456 step-level labels. Evaluates PRMs across 9 sub-categories (simplicity, soundness, sensitivity). Best model: Gemini-2-Thinking at 68.8 overall (human performance: 83.8). ActPRM-X achieves 66.7. More fine-grained than ProcessBench.

2. **Hard2Verify** (2025): 1,860 human-annotated steps across 200 responses from frontier LLMs on open-ended frontier math. Evaluates 29 models. Critical finding: models scoring 60%+ on ProcessBench scored below 20% on Hard2Verify. Qwen2.5-Math-PRM-72B drops from 78.3 (ProcessBench) to 37.3 (Hard2Verify). GPT-5 leads at 85.83 step-level F1. PRMs fundamentally struggle on frontier problems.

3. **UniversalBench** (introduced with AURORA/Universal-PRM, Feb 2025): Evaluates reward predictions across full trajectories under diverse policy distributions with long CoT outputs.

4. **ToolPRMBench**: Evaluates PRMs specifically for tool-using agents.

---

### 6. Key Papers Reporting ProcessBench Numbers (2025-2026)

| Paper | Date | Key Model | Avg F1 |
|---|---|---|---|
| **ProcessBench** (Zheng et al.) | Dec 2024 / ACL 2025 | Original benchmark paper; Qwen2.5-Math-PRM-72B=78.3, o1-mini=87.9 | Baseline |
| **R-PRM** (NJUNLP) | Mar 2025 | R-PRM-7B-DPO | 70.4 |
| **GenPRM** (Zhao et al., AAAI 2026) | Apr 2025 | GenPRM-32B Maj@8 | **82.6** |
| **ThinkPRM** (Khalifa et al., TMLR 2026) | Apr 2025 | ThinkPRM-14B (2 subsets) | **86.5** |
| **ActPRM** (SAIL, Singapore) | Apr 2025 | ActPRM-X-7B | 76.0 |
| **AURORA / Universal-PRM** | Feb 2025 | Universal-PRM-7B | 74.3 |
| **FreePRM** | Jun 2025 | FreePRM (no ground-truth labels) | 53.0 |
| **Is PRM Necessary?** | May 2025 | Shows RL-trained models (DeepSeek-R1, QwQ-32B) have implicit PRM capability | N/A |
| **Hard2Verify** | Oct 2025 | New benchmark showing ProcessBench saturation at frontier level | N/A |

---

### Summary

The current ProcessBench SOTA (excluding proprietary o1-mini at 87.9) is **GenPRM-32B (Maj@8) at 82.6 avg F1** across all four subsets. Among 7B models, **GenPRM-7B (Maj@8) at 80.5** leads, followed by ActPRM-X at 76.0. The generative approach with test-time scaling (majority voting over verification CoTs with code verification) has decisively overtaken discriminative PRMs. ThinkPRM-14B's 86.5 on the hard subsets is the highest reported number on those subsets specifically. The field is also moving beyond ProcessBench toward harder benchmarks like Hard2Verify, where even top-performing ProcessBench models collapse dramatically.

Sources:
- [ProcessBench paper (Zheng et al., 2024)](https://arxiv.org/abs/2412.06559)
- [GenPRM (Zhao et al., AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [ThinkPRM (Khalifa et al., TMLR 2026)](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/html/2503.21295v1)
- [ActPRM: Efficient PRM Training via Active Learning](https://arxiv.org/html/2504.10559v1)
- [AURORA / Universal-PRM](https://arxiv.org/abs/2502.11520)
- [FreePRM](https://arxiv.org/abs/2506.03570)
- [PRMBench (ACL 2025)](https://arxiv.org/abs/2501.03124)
- [Hard2Verify benchmark](https://arxiv.org/html/2510.13744v1)
- [Is PRM Necessary?](https://arxiv.org/pdf/2505.11227)
- [Qwen2.5-Math-PRM blog post](https://qwenlm.github.io/blog/qwen2.5-math-prm/)
- [ProcessBench on alphaXiv](https://www.alphaxiv.org/overview/2412.06559v4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ed6fd6-299c-48fa-bd91-4ca99faf0e92",
  "isSidechain": true,
  "agentId": "a195100b4dfd60a19",
  "requestId": "req_011CbTVsUyk6vXVVp2DhRE76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8bb70fc-a735-44c4-aa0b-cd0cbd1d73d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f12ec80c-3a4b-490a-a484-f7b2a064cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1b2NXfRhc4rCtxENrF2od",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 80738,
      "output_tokens": 4180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4180,
          "cache_read_input_tokens": 80738,
          "cache_creation_input_tokens": 871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 871,
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
