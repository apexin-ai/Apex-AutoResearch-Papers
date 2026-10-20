# Research conversation: I need to verify code availability for these selective RAG baseline methods. For each one, search GitHub and the web to 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a08504024f81fce29.jsonl`
- **Structured JSON:** [`cd254017e6e1a0d6cc73.json`](../../sessions/cd/cd254017e6e1a0d6cc73.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-19T09:29:35.744Z_

I need to verify code availability for these selective RAG baseline methods. For each one, search GitHub and the web to determine if public code is available:

1. Probing-RAG (arXiv:2410.13339) - self-probing for selective document retrieval
2. SeaKR (arXiv:2406.19215) - self-aware knowledge retrieval, ACL 2025
3. TARG (arXiv:2511.09803) - training-free adaptive retrieval gating
4. Skill-RAG (arXiv:2604.15771) - failure-state-aware retrieval via hidden-state probing
5. INKER - adaptive dynamic RAG with internal-external knowledge, IPM 2025
6. Self-Routing RAG (arXiv:2504.01018) - selective retrieval with knowledge verbalization
7. Rep-Con / Rep-PCA from "Towards Knowledge Checking in RAG" (arXiv:2411.14572)
8. Token-entropy thresholding (standard method, likely easy to implement)

For each, search for "[paper name] github code" and check the arXiv page. Report:
- Whether code is publicly available (with GitHub URL if found)
- If not available, how complex the reimplementation would be
- Any alternative implementations

Use WebSearch for each baseline. This is critical for timeline planning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "7522d23f-4be8-45eb-b7d0-3c1057a42ca3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:29:35.746Z_

```json
{
  "parentUuid": "7522d23f-4be8-45eb-b7d0-3c1057a42ca3",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
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
  "uuid": "e83b0019-88dc-4083-acc3-1c9aa18b8adc",
  "timestamp": "2026-05-19T09:29:35.746Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:29:35.747Z_

```json
{
  "parentUuid": "e83b0019-88dc-4083-acc3-1c9aa18b8adc",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "26df0656-fa50-462e-86ae-10d31a288e3a",
  "timestamp": "2026-05-19T09:29:35.747Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:29:38.963Z_



I'll search for code availability for each of these baselines systematically. Let me start by loading the WebSearch tool, then search for each method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26df0656-fa50-462e-86ae-10d31a288e3a",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh7ky2U4c5eYqMqTSRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19286b06-f200-4f0c-9507-c7a2747c2e88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHtwbWDMAyzo6NiEP3qKkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1669,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1669,
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

_source line 5 · 2026-05-19T09:29:39.180Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CNq1b6KHHmznbgnuKxbyGB`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19286b06-f200-4f0c-9507-c7a2747c2e88",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh7ky2U4c5eYqMqTSRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ad192b9-ffa3-48cd-b16d-6991e66778d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHtwbWDMAyzo6NiEP3qKkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1669,
      "cache_read_input_tokens": 7773,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1669
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1669,
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

_source line 6 · 2026-05-19T09:29:39.183Z_

<details><summary>↩ Tool result · `toolu_01CNq1b6KHHmznbgnuKxbyGB`</summary>

````text
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
  "parentUuid": "3ad192b9-ffa3-48cd-b16d-6991e66778d7",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "8d98d93d-8185-4448-bf03-fb2d9e12790a",
  "sourceToolAssistantUUID": "3ad192b9-ffa3-48cd-b16d-6991e66778d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:29:42.355Z_



Now let me search for all 8 baselines. I'll run the searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d98d93d-8185-4448-bf03-fb2d9e12790a",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh81qEa9XivH73pb3ko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07bcd13b-0c57-4221-9350-7c4e9f96b5b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMaRVT7fao5yaQPmzEuJeR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 8 · 2026-05-19T09:29:42.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WaY5EgrpuLWcwGmSwHS6xP`</summary>

```json
{
  "query": "Probing-RAG arXiv 2410.13339 github code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07bcd13b-0c57-4221-9350-7c4e9f96b5b3",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh81qEa9XivH73pb3ko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fc16cf0-a800-42c4-9b0b-f3c09eaab708",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMaRVT7fao5yaQPmzEuJeR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 9 · 2026-05-19T09:29:43.349Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W7rNLyJ6wBWm8KP5bCL3go`</summary>

```json
{
  "query": "SeaKR self-aware knowledge retrieval arXiv 2406.19215 github code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fc16cf0-a800-42c4-9b0b-f3c09eaab708",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh81qEa9XivH73pb3ko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b36a031e-9e68-405a-8b48-ac32975b4023",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMaRVT7fao5yaQPmzEuJeR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 10 · 2026-05-19T09:29:43.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Anw13sXNXfkdvqH9MyA226`</summary>

```json
{
  "query": "TARG training-free adaptive retrieval gating arXiv 2511.09803 github code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b36a031e-9e68-405a-8b48-ac32975b4023",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh81qEa9XivH73pb3ko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3d0e04c-83b4-4005-a352-d0771185b27f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMaRVT7fao5yaQPmzEuJeR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 11 · 2026-05-19T09:29:43.928Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SQMJVxsG3gfNLiUScoSk77`</summary>

```json
{
  "query": "Skill-RAG arXiv 2604.15771 github code failure-state-aware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3d0e04c-83b4-4005-a352-d0771185b27f",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh81qEa9XivH73pb3ko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b163cfc-1f0e-4a3e-93a6-596a43f546bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMaRVT7fao5yaQPmzEuJeR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9442,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 9442,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 638,
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

_source line 12 · 2026-05-19T09:29:50.132Z_

<details><summary>↩ Tool result · `toolu_01W7rNLyJ6wBWm8KP5bCL3go`</summary>

```text
Web search results for query: "SeaKR self-aware knowledge retrieval arXiv 2406.19215 github code"

Links: [{"title":"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240619215Y/abstract"},{"title":"[2406.19215v1] SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation","url":"https://arxiv.org/abs/2406.19215v1"},{"title":"[2406.19215] SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation","url":"https://arxiv.org/abs/2406.19215"},{"title":"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=NhIaRz9Qf5"},{"title":"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented   Generation","url":"https://arxiv.org/pdf/2406.19215"},{"title":"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation","url":"https://arxiv.org/html/2406.19215"},{"title":"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation | Request PDF","url":"https://www.researchgate.net/publication/381771120_SeaKR_Self-aware_Knowledge_Retrieval_for_Adaptive_Retrieval_Augmented_Generation"},{"title":"[Literature Review] SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation","url":"https://www.themoonlight.io/en/review/seakr-self-aware-knowledge-retrieval-for-adaptive-retrieval-augmented-generation"},{"title":"Paper page - SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation","url":"https://huggingface.co/papers/2406.19215"},{"title":"SEAKR: Self-aware Knowledge Retrieval for Adaptive ...","url":"https://openreview.net/pdf?id=JyjbGaYs2e"}]

Based on the search results, here's information about SeaKR:

## Overview

SeaKR is a novel adaptive RAG model that extracts self-aware uncertainty of LLMs from their internal states.

## Key Features

SeaKR activates retrieval when the LLMs present high self-aware uncertainty for generation, and re-ranks retrieved knowledge snippets based on LLM's self-aware uncertainty to preserve the snippet that reduces their uncertainty to the utmost. To facilitate solving complex tasks that require multiple retrievals, SeaKR utilizes their self-aware uncertainty to choose among different reasoning strategies.

## Technical Details

The self-aware uncertainty of LLMs is extracted from the internal states in the feedforward network (FFN) of each layer corresponding to the last generated token, with consistency measured across multiple generations to the same prompt.

## Results and Code

Experiments on both complex and simple Question Answering datasets show that SeaKR outperforms existing adaptive RAG methods. The code is available at https://github.com/THU-KEG/SeaKR.

The paper was submitted on June 27, 2024, with arXiv identifier 2406.19215.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b36a031e-9e68-405a-8b48-ac32975b4023",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "a11b0768-e403-4dc2-9d11-d9e3c3319635",
  "sourceToolAssistantUUID": "b36a031e-9e68-405a-8b48-ac32975b4023",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T09:29:50.598Z_

<details><summary>↩ Tool result · `toolu_01SQMJVxsG3gfNLiUScoSk77`</summary>

```text
Web search results for query: "Skill-RAG arXiv 2604.15771 github code failure-state-aware"

Links: [{"title":"[2604.15771] Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing","url":"https://arxiv.org/abs/2604.15771"},{"title":"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing","url":"https://arxiv.org/html/2604.15771"},{"title":"SKILL-RAG: Self-Knowledge Induced Learning and Filtering for Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2509.20377"},{"title":"Fine-tuning with RAG for Improving LLM Learning of New Skills","url":"https://arxiv.org/pdf/2510.01375"},{"title":"Failure-Aware Enhancements for Large Language Model (LLM) Code Generation: An Empirical Study on Decision Framework","url":"https://arxiv.org/pdf/2602.02896"}]

Based on the search results, I found the paper you're looking for:

Skill-RAG is a failure-aware RAG framework that couples a lightweight hidden-state prober with a prompt-based skill router. The prober gates retrieval at two pipeline stages; upon detecting a failure state, the skill router diagnoses the underlying cause and selects among four retrieval skills -- query rewriting, question decomposition, evidence focusing, and an exit skill for truly irreducible cases -- to correct misalignment.

The research observes that a significant portion of persistent retrieval failures stem not from the absence of relevant evidence but from an alignment gap between the query and the evidence space.

The paper (arXiv:2604.15771) was submitted on April 17, 2026, and is available on arXiv. However, the search results do not include information about the GitHub repository for the code. You may want to check the arXiv page directly or look for a link to the authors' GitHub profile for the implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b163cfc-1f0e-4a3e-93a6-596a43f546bf",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "6e60f4d0-a431-409a-b9f2-10036d5bfc81",
  "sourceToolAssistantUUID": "3b163cfc-1f0e-4a3e-93a6-596a43f546bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T09:29:51.463Z_

<details><summary>↩ Tool result · `toolu_01WaY5EgrpuLWcwGmSwHS6xP`</summary>

```text
Web search results for query: "Probing-RAG arXiv 2410.13339 github code"

Links: [{"title":"[2410.13339] Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval","url":"https://arxiv.org/abs/2410.13339"},{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval","url":"https://arxiv.org/html/2410.13339"},{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document   Retrieval","url":"https://arxiv.org/pdf/2410.13339"},{"title":"GitHub - pejakovic/rag-arxiv: RAG for arXiv papers","url":"https://github.com/pejakovic/rag-arxiv"},{"title":"Federated knowledge retrieval elevates large language model performance on biomedical benchmarks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12888809/"}]

Based on the search results, I found information about the Probing-RAG paper (arXiv 2410.13339):

Probing-RAG utilizes the hidden state representations from the intermediate layers of language models to adaptively determine the necessity of additional retrievals for a given query. By employing a pre-trained prober, Probing-RAG effectively captures the model's internal cognition, enabling reliable decision-making about retrieving external documents.

Experimental results across five open-domain QA datasets demonstrate that Probing-RAG outperforms previous methods while reducing the number of redundant retrieval steps.

However, the search results include links to the arXiv paper itself (both abstract and PDF versions), but I did not find a dedicated GitHub repository for the code in these particular search results. To locate the official code repository, you may want to:

1. Check the paper directly on arXiv at https://arxiv.org/abs/2410.13339 - the authors often link to their code repository there
2. Search for the authors' names (Ingeol Baek, Hwan Chang, Byeongjeong Kim, Jimin Lee, Hwanhee Lee) on GitHub
3. Check the Chung-Ang University Department of AI's GitHub organization

Would you like me to search more specifically for the GitHub repository?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fc16cf0-a800-42c4-9b0b-f3c09eaab708",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "791baf90-f764-4769-82fa-405e6eabefe3",
  "sourceToolAssistantUUID": "7fc16cf0-a800-42c4-9b0b-f3c09eaab708",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T09:29:53.180Z_

<details><summary>↩ Tool result · `toolu_01Anw13sXNXfkdvqH9MyA226`</summary>

```text
Web search results for query: "TARG training-free adaptive retrieval gating arXiv 2511.09803 github code"

Links: [{"title":"[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/abs/2511.09803"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://arxiv.org/html/2511.09803v1"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG Yufeng Wang†","url":"https://arxiv.org/pdf/2511.09803"},{"title":"[Literature Review] TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://www.themoonlight.io/en/review/targ-training-free-adaptive-retrieval-gating-for-efficient-rag"},{"title":"Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/html/2511.09803"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG | OpenReview","url":"https://openreview.net/forum?id=bMDdjg75NS"},{"title":"(PDF) TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://www.researchgate.net/publication/397595362_TARG_Training-Free_Adaptive_Retrieval_Gating_for_Efficient_RAG"},{"title":"Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG | OpenReview","url":"https://openreview.net/forum?id=L8gYtUZfVU"},{"title":"Training-Free Adaptive Gating for Efficient RAG","url":"https://openreview.net/pdf/47141b2086666b2d28bc01f36cafafb9fafed816.pdf"}]

Now let me search for the GitHub code:

Links: [{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://arxiv.org/html/2511.09803v1"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG Yufeng Wang†","url":"https://arxiv.org/pdf/2511.09803"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG | OpenReview","url":"https://openreview.net/forum?id=bMDdjg75NS"},{"title":"[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/abs/2511.09803"},{"title":"[Literature Review] TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://www.themoonlight.io/en/review/targ-training-free-adaptive-retrieval-gating-for-efficient-rag"},{"title":"(PDF) TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://www.researchgate.net/publication/397595362_TARG_Training-Free_Adaptive_Retrieval_Gating_for_Efficient_RAG"},{"title":"TARG: TRAINING-FREE ADAPTIVE RETRIEVAL GAT","url":"https://openreview.net/pdf/e98caa1cd7e096e8428e40d1303cfa3aff813d39.pdf"}]

## Summary of Search Results

I found comprehensive information about TARG from arXiv paper 2511.09803. Here's what I found:

### Paper Overview

TARG (Training-free Adaptive Retrieval Gating) is a single-shot policy that decides when to retrieve using only a short, no-context draft from the base model.

### Key Features

From the draft's prefix logits, TARG computes lightweight uncertainty scores—mean token entropy, a margin signal derived from the top-1/top-2 logit gap via a monotone link, or small-N variance across a handful of stochastic prefixes—and triggers retrieval only when the score exceeds a threshold.

The gate is model-agnostic, adds only tens to hundreds of draft tokens, and requires no additional training or auxiliary heads.

### Performance

On NQ-Open, TriviaQA, and PopQA, TARG consistently shifts the accuracy–efficiency frontier: relative to Always-RAG it matches or improves EM/F1 while reducing retrieval by 70–90% and cutting end-to-end latency.

### Regarding GitHub Code

Unfortunately, the search results don't contain information about a publicly available GitHub repository for the TARG code. The paper abstract and related pages don't mention a code repository link. You may want to check the arXiv paper directly (https://arxiv.org/abs/2511.09803) or the authors' institutions (Stony Brook University and Westlake University based on the paper) for code availability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3d0e04c-83b4-4005-a352-d0771185b27f",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "65454e82-503d-4f25-95b7-8d397d04517b",
  "sourceToolAssistantUUID": "b3d0e04c-83b4-4005-a352-d0771185b27f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T09:29:55.660Z_

Now let me search for the remaining 4 baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65454e82-503d-4f25-95b7-8d397d04517b",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh93TVX1vWPhSqj6x94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be7fb932-25ae-415a-aafc-5bb0c947623f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Bvx7EQt7cgyprcc6sE1mS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 10080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
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

_source line 17 · 2026-05-19T09:29:56.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MyDqcv8CZY1owPpQjmNbU2`</summary>

```json
{
  "query": "INKER adaptive dynamic RAG internal external knowledge IPM 2025 github code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be7fb932-25ae-415a-aafc-5bb0c947623f",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh93TVX1vWPhSqj6x94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0040f3fe-b4d1-4d90-b96e-29643c176ef6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Bvx7EQt7cgyprcc6sE1mS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 10080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
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

_source line 18 · 2026-05-19T09:29:57.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HJDrCWQ5arhYGSDPXTHRga`</summary>

```json
{
  "query": "Self-Routing RAG arXiv 2504.01018 github code selective retrieval knowledge verbalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0040f3fe-b4d1-4d90-b96e-29643c176ef6",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh93TVX1vWPhSqj6x94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da1a5bbf-e0e6-4eaf-8a94-0c800770a901",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Bvx7EQt7cgyprcc6sE1mS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 10080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
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

_source line 19 · 2026-05-19T09:29:58.540Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QQ5Yehz3nr2KZ3k7598JZr`</summary>

```json
{
  "query": "\"Towards Knowledge Checking in RAG\" arXiv 2411.14572 Rep-Con Rep-PCA github code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da1a5bbf-e0e6-4eaf-8a94-0c800770a901",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh93TVX1vWPhSqj6x94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea838b04-2649-42da-9165-550c64c5f11c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Bvx7EQt7cgyprcc6sE1mS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 10080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
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

_source line 20 · 2026-05-19T09:29:58.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuD7PPRUmyUMEj1dUWMsoU`</summary>

```json
{
  "query": "token entropy thresholding RAG retrieval decision github implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea838b04-2649-42da-9165-550c64c5f11c",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBh93TVX1vWPhSqj6x94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8114b25c-3e32-4d9f-b74f-809ef6dbc295",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Bvx7EQt7cgyprcc6sE1mS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 10080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
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

_source line 21 · 2026-05-19T09:30:03.039Z_

<details><summary>↩ Tool result · `toolu_01MyDqcv8CZY1owPpQjmNbU2`</summary>

```text
Web search results for query: "INKER adaptive dynamic RAG internal external knowledge IPM 2025 github code"

Links: [{"title":"Weixin Zeng","url":"https://dexterzeng.github.io/"},{"title":"INKER: Adaptive dynamic retrieval augmented generation with internal-external knowledge integration - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325004753"},{"title":"R1-Searcher++: Incentivizing the Dynamic Knowledge Acquisition of LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.17005"},{"title":"Modeling Uncertainty Trends for Timely Retrieval in Dynamic RAG","url":"https://arxiv.org/pdf/2511.09980"},{"title":"Dynamic and Parametric Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2506.06704"},{"title":"GitHub - FUTUREEEEEE/Dynamic-RAG: AAAI 2025: Adapting to Non-Stationary Environments: Multi-Armed Bandit Enhanced Retrieval-Augmented Generation on Knowledge Graphs · GitHub","url":"https://github.com/FUTUREEEEEE/Dynamic-RAG"},{"title":"Dynamic Parametric Retrieval Augmented Generation for Test-time   Knowledge Enhancement","url":"https://arxiv.org/pdf/2503.23895"},{"title":"arXiv:submit/6596874 [cs.CL] 4 Jul 2025 MemOS: A Memory OS for AI System","url":"https://statics.memtensor.com.cn/files/MemOS_0707.pdf"}]

Based on the search results, I found information about INKER:

INKER is an adaptive dynamic retrieval augmented generation framework with internal-external knowledge integration, and it was published in IPM in 2026 (note: the publication appears to be forthcoming/recent). The authors are Mingjun Zhou, Jiuyang Tang, Weixin Zeng, and Xiang Zhao.

INKER integrates both internal and external knowledge involved in the LLM text generation process to decide when and what to retrieve. Experiments on 2WikiMultihopQA, HotpotQA, StrategyQA, and Natural Questions (NQ) demonstrate that INKER outperforms six advanced RAG methods in terms of accuracy, while also reducing retrieval frequency by approximately 40% on average.

However, the search results do not provide a direct link to the GitHub code repository for INKER. The search results show information about the paper on Weixin Zeng's personal website and the ScienceDirect publication, but no explicit GitHub link for the INKER code was found. You may want to check the author's GitHub profile or the paper's supplementary materials for code availability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0040f3fe-b4d1-4d90-b96e-29643c176ef6",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "041c12e3-5dd6-4724-b1a8-75d52953ebd6",
  "sourceToolAssistantUUID": "0040f3fe-b4d1-4d90-b96e-29643c176ef6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T09:30:07.260Z_

<details><summary>↩ Tool result · `toolu_01RuD7PPRUmyUMEj1dUWMsoU`</summary>

```text
Web search results for query: "token entropy thresholding RAG retrieval decision github implementation"

Links: [{"title":"GitHub - Nomothings/Entropy-RAG: Entropy-RAG: Rethinking Retrieval-Augmented Generation from the Perspective of Entropy · GitHub","url":"https://github.com/Nomothings/Entropy-RAG"},{"title":"GitHub - WisdomShell/ETC: [AAAI'26, Oral] Modeling Uncertainty Trends for Timely Retrieval in Dynamic RAG · GitHub","url":"https://github.com/WisdomShell/ETC"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://arxiv.org/pdf/2511.09803"},{"title":"Modeling Uncertainty Trends for Timely Retrieval in Dynamic RAG","url":"https://arxiv.org/pdf/2511.09980"},{"title":"feat: Automatic RAG/Full Context Strategy Based on Configurable Token Threshold · open-webui/open-webui · Discussion #19177","url":"https://github.com/open-webui/open-webui/discussions/19177"},{"title":"L-RAG: Balancing Context and Retrieval with Entropy-Based Lazy Loading","url":"https://arxiv.org/pdf/2601.06551"},{"title":"SF-RAG: Structure-Fidelity Retrieval-Augmented Generation for Academic Question Answering","url":"https://arxiv.org/pdf/2602.13647"}]

I found several relevant implementations related to token entropy thresholding for RAG retrieval decisions:

## Key GitHub Implementations

**1. Entropy-RAG** (A framework that integrates entropy across the entire retrieval and generation pipeline to optimize both the necessity and quality of retrieval. It introduces three key components: Entropy-Awareness (using response entropy to determine if retrieval is required), Entropy-Retrieval (identifying uncertain tokens to guide retrieval queries), and Entropy-Reranking (re-ranking contexts based on entropy reduction).
- GitHub: https://github.com/Nomothings/Entropy-RAG

**2. ETC (Entropy-Trend Constraint)** (A training-free method for timely retrieval in dynamic retrieval-augmented generation. Instead of reacting to isolated token-level confidence drops, ETC models the trend of token-level uncertainty during generation using entropy sequences, their first- and second-order differences, and a dynamic smoothing mechanism.
- GitHub: https://github.com/WisdomShell/ETC
- Paper: https://arxiv.org/pdf/2511.09980

**3. TARG (Training-free Adaptive Retrieval Gating)** - Uses a short, no-context draft to read the model's prefix logits and compute uncertainty scores, including mean token entropy, margin-based scores from logit gaps, and variance from stochastic prefixes.
- Paper: https://arxiv.org/pdf/2511.09803

**4. L-RAG (Lazy Retrieval-Augmented Generation)** - Employs a two-tier architecture where expensive chunk retrieval is triggered only when the model's predictive entropy exceeds a calibrated threshold.
- Paper: https://arxiv.org/pdf/2601.06551

These implementations represent different approaches to using token entropy as a signal for deciding when retrieval is necessary in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8114b25c-3e32-4d9f-b74f-809ef6dbc295",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "936ae1c4-474b-4465-ba99-bd19919c4d12",
  "sourceToolAssistantUUID": "8114b25c-3e32-4d9f-b74f-809ef6dbc295",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T09:30:09.425Z_

<details><summary>↩ Tool result · `toolu_01HJDrCWQ5arhYGSDPXTHRga`</summary>

```text
Web search results for query: "Self-Routing RAG arXiv 2504.01018 github code selective retrieval knowledge verbalization"

Links: [{"title":"[2504.01018] Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization","url":"https://arxiv.org/abs/2504.01018"},{"title":"Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization","url":"https://arxiv.org/pdf/2504.01018"},{"title":"Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization","url":"https://arxiv.org/html/2504.01018"},{"title":"GitHub - xiaowu0162/self-routing-rag","url":"https://github.com/xiaowu0162/self-routing-rag"},{"title":"Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive   Study and Hybrid Approach","url":"https://arxiv.org/pdf/2407.16833"}]

Based on the search results, here's what I found about Self-Routing RAG (arXiv 2504.01018):

## Overview

Self-Routing RAG (SR-RAG) casts selective retrieval as knowledge source selection and treats the LLM itself as a first-class knowledge source. SR-RAG is a novel framework that binds selective retrieval with knowledge verbalization, enabling an LLM to dynamically decide between external retrieval and verbalizing its own parametric knowledge.

## Key Features

SR-RAG learns to select an appropriate knowledge source, optionally verbalize parametric knowledge, and answer using the selected source, all within a single left-to-right generation pass. SR-RAG further augments source selection by combining LLM-based uncertainty with a flexible external policy datastore to improve decision calibration.

## Performance Results

Across four benchmarks and three 7B-class LLMs, SR-RAG outperforms a strong selective retrieval baseline by 8.5%/2.1%/4.7% while performing 26%/40%/21% fewer retrievals.

## Code Availability

Data and code are publicly released at https://github.com/xiaowu0162/self-routing-rag.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da1a5bbf-e0e6-4eaf-8a94-0c800770a901",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "121f693c-8b67-4b14-b750-4a63b9c068fa",
  "sourceToolAssistantUUID": "da1a5bbf-e0e6-4eaf-8a94-0c800770a901",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T09:30:14.151Z_

<details><summary>↩ Tool result · `toolu_01QQ5Yehz3nr2KZ3k7598JZr`</summary>

```text
Web search results for query: ""Towards Knowledge Checking in RAG" arXiv 2411.14572 Rep-Con Rep-PCA github code"

Links: [{"title":"[2411.14572] Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective","url":"https://arxiv.org/abs/2411.14572"},{"title":"(PDF) Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective","url":"https://www.researchgate.net/publication/386093800_Towards_Knowledge_Checking_in_Retrieval-augmented_Generation_A_Representation_Perspective"},{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A   Representation Perspective","url":"https://arxiv.org/pdf/2411.14572"},{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective","url":"https://arxiv.org/html/2411.14572"},{"title":"Towards knowledge checking in retrieval-augmented generation: A representation perspective - Amazon Science","url":"https://www.amazon.science/publications/towards-knowledge-checking-in-retrieval-augmented-generation-a-representation-perspective"},{"title":"Empowering GraphRAG with Knowledge Filtering and Integration","url":"https://arxiv.org/html/2503.13804v1"},{"title":"Machine Learning Nov 2024","url":"https://www.arxiv.org/list/cs.LG/2024-11?skip=1200&show=2000"}]

Now let me search for information about the Rep-Con and Rep-PCA methods and GitHub code:

Links: [{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective","url":"https://arxiv.org/html/2411.14572"},{"title":"Towards Knowledge Checking in Retrieval-augmented ...","url":"https://aclanthology.org/2025.naacl-long.151.pdf"},{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A   Representation Perspective","url":"https://arxiv.org/pdf/2411.14572"},{"title":"GitHub - gORILLA453/knowledge-rag: 🔍 Enhance your knowledge base with a local RAG system that leverages hybrid search for precise information retrieval and optimal results.","url":"https://github.com/gORILLA453/knowledge-rag"},{"title":"On The Reproducibility Limitations of RAG Systems","url":"https://arxiv.org/pdf/2509.18869"},{"title":"GitHub - lyonzin/knowledge-rag: Drop docs, search instantly from Claude Code — 12 MCP tools, 20 format parsers, hybrid search + reranking. Zero servers, zero API keys, 100% local.","url":"https://github.com/lyonzin/knowledge-rag"}]

Now let me search more specifically for the GitHub repository for this paper:

Links: [{"title":"[2411.14572] Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective","url":"https://arxiv.org/abs/2411.14572"}]

Let me search for the actual paper code repository:

Links: [{"title":"Towards knowledge checking in retrieval-augmented generation: A representation perspective - Amazon Science","url":"https://www.amazon.science/publications/towards-knowledge-checking-in-retrieval-augmented-generation-a-representation-perspective"},{"title":"GitHub - amazon-science/RAGChecker: RAGChecker: A Fine-grained Framework For Diagnosing RAG · GitHub","url":"https://github.com/amazon-science/RAGChecker"},{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A   Representation Perspective","url":"https://arxiv.org/pdf/2411.14572"},{"title":"GitHub - amazon-science/auto-rag-eval: Code repo for the ICML 2024 paper \"Automated Evaluation of Retrieval-Augmented Language Models with Task-Specific Exam Generation\" · GitHub","url":"https://github.com/amazon-science/auto-rag-eval"},{"title":"Releases · amazon-science/RAGChecker","url":"https://github.com/amazon-science/RAGChecker/releases"},{"title":"GitHub - aws-samples/rag-workshop-amazon-bedrock-knowledge-bases · GitHub","url":"https://github.com/aws-samples/rag-workshop-amazon-bedrock-knowledge-bases"},{"title":"GitHub - aws-samples/bedrock-kb-rag-workshop: Bedrock Knowledge Base and Agents for Retrieval Augmented Generation (RAG) · GitHub","url":"https://github.com/aws-samples/bedrock-kb-rag-workshop"}]

Based on my search results, I can provide you with comprehensive information about the paper and the methods it describes:

## Summary of "Towards Knowledge Checking in RAG" (arXiv 2411.14572)

This work aims to provide a systematic study on knowledge checking in RAG systems, conducting a comprehensive analysis of LLM representation behaviors and demonstrating the significance of using representations in knowledge checking.

### Key Challenge
RAG systems face challenges in effectively integrating external knowledge with the LLM's internal knowledge, often leading to issues with misleading or unhelpful information.

### Core Methods
The paper develops two representation-based knowledge checking approaches:

1. **Rep-PCA** (PCA-based checking): A PCA-based checking method for representation-based knowledge checking

2. **Rep-Con** (Contrastive-learning-based checking): A contrastive-learning-based checking method for representation-based knowledge checking

### Key Findings and Results
The analysis reveals that positive and negative samples exhibit different behaviors in the representation space, and representation-based methods demonstrate significantly superior performance in the aforementioned tasks. Results show that simple filtering of contradictory and irrelevant information substantially improves RAG performance, even in scenarios with poisoned knowledge databases.

### Paper Details
The paper is authored by Shenglai Zeng, Jiankun Zhang, Bingheng Li, Yuping Lin, Tianqi Zheng, Dante Everaert, Hanqing Lu, Hui Liu, Yue Xing, Monica Xiao Cheng, and Jiliang Tang from Michigan State University and Amazon.

**Note on Code**: While my search found the arXiv paper and Amazon Science publication page, I was unable to locate a specific GitHub repository for this paper's code in the search results. You may want to check the paper directly on arXiv (arxiv.org/abs/2411.14572) for links to supplementary materials or code repositories that may be referenced in the paper itself.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea838b04-2649-42da-9165-550c64c5f11c",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "fd00da24-e2bf-4ed4-a6c0-65379ff7ef86",
  "sourceToolAssistantUUID": "ea838b04-2649-42da-9165-550c64c5f11c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T09:30:17.164Z_

Let me do a few more targeted searches for the ones where I didn't find code yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd00da24-e2bf-4ed4-a6c0-65379ff7ef86",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhAbAWSFLjyVW36QTGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9db3d98d-ab3c-4f61-ba1e-1a98742ad648",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M93jpAsM2ifo4JJ6BNukX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 13155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3856,
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

_source line 26 · 2026-05-19T09:30:18.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FSvUm816PVvCj82jouXN8g`</summary>

```json
{
  "query": "Probing-RAG github Ingeol Baek Hwanhee Lee code implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9db3d98d-ab3c-4f61-ba1e-1a98742ad648",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhAbAWSFLjyVW36QTGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1db68c27-0324-436d-b955-1e8de6c82fb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M93jpAsM2ifo4JJ6BNukX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 13155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3856,
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

_source line 27 · 2026-05-19T09:30:19.107Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M6UuzXRKFCTacPB3qXCmgM`</summary>

```json
{
  "query": "TARG github Yufeng Wang training-free adaptive retrieval gating code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db68c27-0324-436d-b955-1e8de6c82fb5",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhAbAWSFLjyVW36QTGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7602690-3a3d-4d31-a9da-2c5ad0020f5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M93jpAsM2ifo4JJ6BNukX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 13155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3856,
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

_source line 28 · 2026-05-19T09:30:19.578Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VGsGgvzqEsTdoe4DdNkkiB`</summary>

```json
{
  "query": "INKER github Mingjun Zhou Xiang Zhao adaptive dynamic retrieval augmented generation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7602690-3a3d-4d31-a9da-2c5ad0020f5c",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhAbAWSFLjyVW36QTGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a94d511-8362-4fb3-aaf4-b6f01d9f98e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M93jpAsM2ifo4JJ6BNukX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 13155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3856,
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

_source line 29 · 2026-05-19T09:30:19.934Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PiEEX83qiupiyfEVcWQ8Ue`</summary>

```json
{
  "query": "Rep-Con Rep-PCA knowledge checking RAG Shenglai Zeng github code Michigan State"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a94d511-8362-4fb3-aaf4-b6f01d9f98e4",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhAbAWSFLjyVW36QTGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0300fa43-bfdd-40d8-b803-6b828fa1f82b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M93jpAsM2ifo4JJ6BNukX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 13155,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3856
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 865,
          "output_tokens": 257,
          "cache_read_input_tokens": 13155,
          "cache_creation_input_tokens": 3856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3856,
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

_source line 30 · 2026-05-19T09:30:25.071Z_

<details><summary>↩ Tool result · `toolu_01VGsGgvzqEsTdoe4DdNkkiB`</summary>

```text
Web search results for query: "INKER github Mingjun Zhou Xiang Zhao adaptive dynamic retrieval augmented generation code"

Links: [{"title":"INKER: Adaptive dynamic retrieval augmented generation with internal-external knowledge integration - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325004753"},{"title":"Weixin Zeng","url":"https://dexterzeng.github.io/"},{"title":"Dynamic Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2312.08976"},{"title":"Context-Guided Dynamic Retrieval for Improving Generation Quality in RAG   Models","url":"https://arxiv.org/pdf/2504.19436"},{"title":"Dynamic and Parametric Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2506.06704"},{"title":"Active Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2305.06983"},{"title":"Accelerating Adaptive Retrieval Augmented Generation via Instruction-Driven Representation Reduction of Retrieval Overlaps","url":"https://arxiv.org/pdf/2505.12731"}]

Based on the search results, I found information about INKER:

INKER is an adaptive dynamic retrieval augmented generation framework that integrates both internal and external knowledge involved in the LLM text generation process to decide when and what to retrieve. The work was led by Mingjun Zhou and Xiang Zhao among other contributors.

The framework was evaluated on benchmarks including 2WikiMultihopQA, HotpotQA, StrategyQA, and Natural Questions, demonstrating that INKER outperforms advanced RAG methods in accuracy while reducing retrieval frequency by approximately 40% on average.

However, the search results reference the academic paper rather than a specific GitHub repository. The paper appears to have been published in IPM (Information Processing & Management) in 2026. If you're looking for the code repository specifically, you may need to search directly on GitHub or check the paper's supplementary materials for the code availability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a94d511-8362-4fb3-aaf4-b6f01d9f98e4",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "0e2f652f-1b56-4b0a-a378-716e83a9c9ef",
  "sourceToolAssistantUUID": "5a94d511-8362-4fb3-aaf4-b6f01d9f98e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T09:30:25.442Z_

<details><summary>↩ Tool result · `toolu_01PiEEX83qiupiyfEVcWQ8Ue`</summary>

```text
Web search results for query: "Rep-Con Rep-PCA knowledge checking RAG Shenglai Zeng github code Michigan State"

Links: [{"title":"Shenglai Zeng","url":"https://slz-ai.github.io/"},{"title":"Shenglai Zeng | Semantic Scholar","url":"https://www.semanticscholar.org/author/Shenglai-Zeng/2253682835"},{"title":"Towards knowledge checking in retrieval-augmented generation: A representation perspective - Amazon Science","url":"https://www.amazon.science/publications/towards-knowledge-checking-in-retrieval-augmented-generation-a-representation-perspective"},{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.151/"},{"title":"[2411.14572] Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective","url":"https://arxiv.org/abs/2411.14572"},{"title":"The Good and The Bad: Exploring Privacy Issues in Retrieval-Augmented Generation (RAG) - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.267/"},{"title":"Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1247/"},{"title":"Towards Knowledge Checking in Retrieval-augmented Generation: A   Representation Perspective","url":"https://arxiv.org/pdf/2411.14572"}]

Based on the search results, I found relevant information about the knowledge checking in RAG research by Shenglai Zeng and team at Michigan State University:

Shenglai Zeng is a third-year Ph.D. student from Michigan State University, advised by professor Jiliang Tang.

The work aims to provide a systematic study on knowledge checking in RAG systems, conducting a comprehensive analysis of LLM representation behaviors and demonstrating the significance of using representations in knowledge checking. The researchers developed representation-based classifiers for knowledge filtering, showing substantial improvements in RAG performance, even when dealing with noisy knowledge databases.

The paper titled "Towards Knowledge Checking in Retrieval-augmented Generation: A Representation Perspective" was published at NAACL 2025, with researchers from Michigan State University and Amazon.com, with email domains showing affiliations at msu.edu and amazon.com.

However, the search results did not contain specific information about "Rep-Con" or "Rep-PCA" methods, nor did they provide direct GitHub repository links. For the most up-to-date code repository information, you may want to check Shenglai Zeng's personal GitHub profile or the official research repositories linked from the academic publications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0300fa43-bfdd-40d8-b803-6b828fa1f82b",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "011c40bb-b325-401a-8d2f-72d7d0fe3f73",
  "sourceToolAssistantUUID": "0300fa43-bfdd-40d8-b803-6b828fa1f82b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T09:30:26.209Z_

<details><summary>↩ Tool result · `toolu_01M6UuzXRKFCTacPB3qXCmgM`</summary>

```text
Web search results for query: "TARG github Yufeng Wang training-free adaptive retrieval gating code"

Links: [{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://arxiv.org/html/2511.09803v1"},{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG Yufeng Wang†","url":"https://arxiv.org/pdf/2511.09803"},{"title":"[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/abs/2511.09803"},{"title":"Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/html/2511.09803"},{"title":"TARG: TRAINING-FREE ADAPTIVE RETRIEVAL GAT","url":"https://openreview.net/pdf/e98caa1cd7e096e8428e40d1303cfa3aff813d39.pdf"},{"title":"[Literature Review] TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://www.themoonlight.io/en/review/targ-training-free-adaptive-retrieval-gating-for-efficient-rag"},{"title":"(PDF) TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://www.researchgate.net/publication/397595362_TARG_Training-Free_Adaptive_Retrieval_Gating_for_Efficient_RAG"}]

Based on the search results, I found information about TARG and its research:

TARG (Training-free Adaptive Retrieval Gating) is a single-shot policy that decides when to retrieve using only a short, no-context draft from the base model. The work is authored by Yufeng Wang and colleagues from Stony Brook University.

TARG uses a short, no-context draft to read the model's prefix logits and compute a lightweight uncertainty score, with three signals: (1) mean token entropy, (2) a margin-based score from the top-1 versus top-2 logit gap via a monotone link, and (3) a small-N variance from stochastic prefixes.

The gate is model-agnostic, adds only tens to hundreds of draft tokens, and requires no additional training or auxiliary heads, and on five QA benchmarks (NQ-Open, TriviaQA, PopQA, MuSiQue, and ASQA), TARG matches or improves EM/F1 while reducing retrieval by 70-90% and cutting end-to-end latency.

The paper was published recently (November 2025, with an update in April 2026) and is available on arXiv. However, the search results provided don't include a direct link to a GitHub repository for the code. You may want to check the paper's official page or the authors' GitHub profiles directly for code availability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7602690-3a3d-4d31-a9da-2c5ad0020f5c",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "6104a788-fcd4-4a08-aeb4-36e4cabcb8fc",
  "sourceToolAssistantUUID": "d7602690-3a3d-4d31-a9da-2c5ad0020f5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T09:30:27.386Z_

<details><summary>↩ Tool result · `toolu_01FSvUm816PVvCj82jouXN8g`</summary>

```text
Web search results for query: "Probing-RAG github Ingeol Baek Hwanhee Lee code implementation"

Links: [{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.181/"},{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval","url":"https://arxiv.org/html/2410.13339"},{"title":"GitHub - baekingeol/Probing-RAG: [NAACL 2025] Official Code Repository for the paper \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval\"","url":"https://github.com/baekingeol/Probing-RAG"},{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document   Retrieval","url":"https://arxiv.org/pdf/2410.13339"},{"title":"[2410.13339] Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval","url":"https://arxiv.org/abs/2410.13339"},{"title":"Hwanhee Lee | Assistant Professor at Chung-Ang University","url":"https://hwanheelee1993.github.io/"},{"title":"Hwanhee Lee (이환희) ASSISTANT PROFESSOR @ CHUNG-ANG UNIVERSITY","url":"https://hwanheelee1993.github.io/materials/CV_Hwanhee_Lee.pdf"},{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval | Request PDF","url":"https://www.researchgate.net/publication/385010067_Probing-RAG_Self-Probing_to_Guide_Language_Models_in_Selective_Document_Retrieval"}]

Based on the search results, I found comprehensive information about Probing-RAG:

## Overview

Probing-RAG utilizes the hidden state representations from the intermediate layers of language models to adaptively determine the necessity of additional retrievals for a given query.

## Authors and Paper Details

The paper was authored by Ingeol Baek, Hwan Chang, ByeongJeong Kim, Jimin Lee, and Hwanhee Lee. The paper titled "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval" was published in Findings of the Association for Computational Linguistics: NAACL 2025, pages 3287–3304, in Albuquerque, New Mexico.

## Official GitHub Repository

The official code repository is available at GitHub (baekingeol/Probing-RAG) and is described as the official code repository for the paper "Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval".

## How It Works

By employing a pre-trained prober, Probing-RAG effectively captures the model's internal cognition, enabling reliable decision-making about retrieving external documents.

You can access the official GitHub repository at: https://github.com/baekingeol/Probing-RAG


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1db68c27-0324-436d-b955-1e8de6c82fb5",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "29de64fd-d402-47e0-b68f-a57649ef135e",
  "sourceToolAssistantUUID": "1db68c27-0324-436d-b955-1e8de6c82fb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-19T09:30:30.762Z_

Let me do a few final targeted searches for the repos I haven't confirmed yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29de64fd-d402-47e0-b68f-a57649ef135e",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhBZhUheB6btsKf3ybG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0522ac7f-0b7d-4d6b-b77e-cc9e945238fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GAYHiakTW67PZ8uYZSaTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2071,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 17011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1958,
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

_source line 35 · 2026-05-19T09:30:31.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013HJ96qVitss4FBcDCLPRN9`</summary>

```json
{
  "query": "github.com slz-ai knowledge checking RAG representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0522ac7f-0b7d-4d6b-b77e-cc9e945238fb",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhBZhUheB6btsKf3ybG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07028daa-f4e6-404b-9dc4-68bbd1082b57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GAYHiakTW67PZ8uYZSaTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2071,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 17011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1958,
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

_source line 36 · 2026-05-19T09:30:31.758Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DBTsGGm3mx1gtNcN5xDgpZ`</summary>

```json
{
  "query": "SeaKR github THU-KEG code repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07028daa-f4e6-404b-9dc4-68bbd1082b57",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhBZhUheB6btsKf3ybG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7587a618-5078-4c12-93b1-9cf23ab449f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GAYHiakTW67PZ8uYZSaTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2071,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 17011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1958,
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

_source line 37 · 2026-05-19T09:30:32.710Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PTXV1gibPswBPM9iuev2Sy`</summary>

```json
{
  "query": "Skill-RAG 2604.15771 github code hidden state probing skill routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7587a618-5078-4c12-93b1-9cf23ab449f7",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhBZhUheB6btsKf3ybG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bad4e5a7-ab15-4cf6-acc6-2c30d8cc2df1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GAYHiakTW67PZ8uYZSaTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2071,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 17011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1958,
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

_source line 38 · 2026-05-19T09:30:33.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013TP7Ltp2j7kWJf7x1ZhNJt`</summary>

```json
{
  "query": "INKER code repository \"internal-external knowledge\" RAG Mingjun Zhou github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bad4e5a7-ab15-4cf6-acc6-2c30d8cc2df1",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhBZhUheB6btsKf3ybG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed078d9f-453f-426f-b1cf-54ff1bf79761",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GAYHiakTW67PZ8uYZSaTm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2071,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 17011,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2071,
          "output_tokens": 234,
          "cache_read_input_tokens": 17011,
          "cache_creation_input_tokens": 1958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1958,
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

_source line 39 · 2026-05-19T09:30:35.815Z_

<details><summary>↩ Tool result · `toolu_01DBTsGGm3mx1gtNcN5xDgpZ`</summary>

```text
Web search results for query: "SeaKR github THU-KEG code repository"

Links: [{"title":"SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240619215Y/abstract"},{"title":"GitHub - THU-KEG/SeaKR","url":"https://github.com/thu-keg/seakr"},{"title":"SeaKR/README.md at main · THU-KEG/SeaKR","url":"https://github.com/THU-KEG/SeaKR/blob/main/README.md"},{"title":"GitHub - THU-KEG/Event-Level-Knowledge-Editing","url":"https://github.com/THU-KEG/Event-Level-Knowledge-Editing"},{"title":"THU-KEG repositories · GitHub","url":"https://github.com/orgs/THU-KEG/repositories"},{"title":"GitHub - THU-KEG/KNOT","url":"https://github.com/THU-KEG/KNOT"},{"title":"THU-KEG · GitHub","url":"https://github.com/THU-KEG"},{"title":"GitHub - THU-KEG/KECG: Source code and datasets for EMNLP 2019 paper \"Semi-supervised Entity Alignment via Joint Knowledge Embedding Model and Cross-graph Model\".","url":"https://github.com/THU-KEG/KECG"},{"title":"GitHub - THU-KEG/RM-Bench: [ICLR 25 Oral] RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style · GitHub","url":"https://github.com/THU-KEG/RM-Bench"},{"title":"Evaluating large language models in biomedical data science challenges through a classroom experiment","url":"https://www.biorxiv.org/content/10.1101/2025.07.12.664517.full.pdf"}]

Based on the search results, I found information about the SeaKR repository:

The SeaKR code is available at https://github.com/THU-KEG/SeaKR. 

SeaKR is a method for self-aware knowledge retrieval that outperforms existing adaptive RAG (Retrieval Augmented Generation) methods on both complex and simple Question Answering datasets.

The repository contains implementation details and setup instructions, including Python environment configuration with specific dependencies like BEIR, spacy, and others for running the SeaKR system.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7587a618-5078-4c12-93b1-9cf23ab449f7",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "54023ad2-3200-4da6-8d46-dd032b41c033",
  "sourceToolAssistantUUID": "7587a618-5078-4c12-93b1-9cf23ab449f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T09:30:37.069Z_

<details><summary>↩ Tool result · `toolu_013HJ96qVitss4FBcDCLPRN9`</summary>

```text
Web search results for query: "github.com slz-ai knowledge checking RAG representation"

Links: [{"title":"GitHub - HKUDS/RAG-Anything: \"RAG-Anything: All-in-One RAG Framework\" · GitHub","url":"https://github.com/HKUDS/RAG-Anything"},{"title":"GitHub - lyonzin/knowledge-rag: Drop docs, search instantly from Claude Code — 12 MCP tools, 20 format parsers, hybrid search + reranking. Zero servers, zero API keys, 100% local.","url":"https://github.com/lyonzin/knowledge-rag"},{"title":"GitHub - gORILLA453/knowledge-rag: 🔍 Enhance your knowledge base with a local RAG system that leverages hybrid search for precise information retrieval and optimal results.","url":"https://github.com/gORILLA453/knowledge-rag"},{"title":"GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub","url":"https://github.com/DavidZWZ/Awesome-RAG-Reasoning"},{"title":"GitHub - kaushikacharya/Knowledge_Graphs_for_RAG: DeepLearning.ai course: Knowledge Graphs for RAG · GitHub","url":"https://github.com/kaushikacharya/Knowledge_Graphs_for_RAG"},{"title":"Welcome - GraphRAG","url":"https://microsoft.github.io/graphrag/"},{"title":"GitHub - amazon-science/RAGChecker: RAGChecker: A Fine-grained Framework For Diagnosing RAG · GitHub","url":"https://github.com/amazon-science/RAGChecker"},{"title":"GitHub - cristianleoo/rag-knowledge-graph · GitHub","url":"https://github.com/cristianleoo/rag-knowledge-graph"},{"title":"GitHub - microsoft/RAG-Knowledge · GitHub","url":"https://github.com/microsoft/RAG-Knowledge"},{"title":"GitHub - NirDiamant/RAG_Techniques: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial. · GitHub","url":"https://github.com/NirDiamant/RAG_Techniques"}]

Based on the search results, I found various GitHub repositories related to RAG (Retrieval-Augmented Generation) systems and knowledge representation, but I did not find a specific project at "github.com/slz-ai" with the exact combination of "knowledge checking RAG representation" you mentioned.

The search returned several relevant RAG-related projects including:

1. **RAGChecker** (Amazon Science) - An advanced automatic evaluation framework designed to assess and diagnose Retrieval-Augmented Generation (RAG) systems, providing a comprehensive suite of metrics and tools for in-depth analysis of RAG performance.

2. **GraphRAG** (Microsoft) - A structured, hierarchical approach to Retrieval Augmented Generation (RAG), which involves extracting a knowledge graph out of raw text, building a community hierarchy, generating summaries for these communities, and leveraging these structures when performing RAG-based tasks.

3. **Knowledge Graphs for RAG** - Various implementations showing how to leverage structured knowledge representations to enhance RAG systems.

If you're looking for a specific repository from the "slz-ai" organization, you might want to:
- Check the organization's GitHub page directly at github.com/slz-ai
- Verify the exact repository name
- Search with different keywords related to the specific project you're interested in

Would you like me to search for more specific information about the slz-ai organization or a particular aspect of RAG systems?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07028daa-f4e6-404b-9dc4-68bbd1082b57",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "c0c43d8c-4f4c-45a7-b18d-f8d3b5ca8c4f",
  "sourceToolAssistantUUID": "07028daa-f4e6-404b-9dc4-68bbd1082b57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T09:30:38.474Z_

<details><summary>↩ Tool result · `toolu_013TP7Ltp2j7kWJf7x1ZhNJt`</summary>

```text
Web search results for query: "INKER code repository "internal-external knowledge" RAG Mingjun Zhou github"

Links: [{"title":"INKER: Adaptive dynamic retrieval augmented generation with internal-external knowledge integration - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325004753"},{"title":"Weixin Zeng","url":"https://dexterzeng.github.io/"},{"title":"R1-Searcher++: Incentivizing the Dynamic Knowledge Acquisition of LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.17005"},{"title":"LFD: Layer Fused Decoding to Exploit External Knowledge in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2508.19614"},{"title":"A novel framework for educational Q&A: Leveraging RAG and Code Interpreters for knowledge retrieval and logical computation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12668533/"},{"title":"From RAGs to rich parameters: Probing how language models utilize   external knowledge over parametric information for factual queries","url":"https://arxiv.org/pdf/2406.12824"}]

Based on the search results, I found information about the INKER framework and its connection to Mingjun Zhou:

INKER is an adaptive dynamic RAG framework called "Internal-External Knowledge Integration based Retrieval", which was published in IPM (Information Processing & Management) in 2026. Mingjun Zhou was involved in writing, visualization, software development, methodology, and other key aspects of the work.

The research shows that INKER significantly outperforms existing methods across multiple benchmarks while improving efficiency, reducing retrieval steps by approximately 40% on average.

However, the search results do not contain a direct link to a GitHub code repository for INKER. The academic paper appears to be published on ScienceDirect, but no GitHub repository link is mentioned in the search results. You may want to check the official paper or the authors' institutional pages for code availability information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed078d9f-453f-426f-b1cf-54ff1bf79761",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "9fb73a33-ef6c-4e91-8243-4d1f0fd4fb88",
  "sourceToolAssistantUUID": "ed078d9f-453f-426f-b1cf-54ff1bf79761",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T09:30:39.196Z_

<details><summary>↩ Tool result · `toolu_01PTXV1gibPswBPM9iuev2Sy`</summary>

```text
Web search results for query: "Skill-RAG 2604.15771 github code hidden state probing skill routing"

Links: [{"title":"[2604.15771] Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing","url":"https://arxiv.org/abs/2604.15771"},{"title":"Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing","url":"https://arxiv.org/html/2604.15771"},{"title":"SkillRouter: Skill Routing for LLM Agents at Scale","url":"https://arxiv.org/html/2603.22455v3"},{"title":"SkillRouter: Skill Routing for LLM Agents at Scale","url":"https://arxiv.org/pdf/2603.22455"},{"title":"ReLope: KL-Regularized LoRA Probes for Multimodal LLM Routing","url":"https://arxiv.org/pdf/2603.24787"},{"title":"Probing-RAG: Self-Probing to Guide Language Models in Selective Document   Retrieval","url":"https://arxiv.org/pdf/2410.13339"},{"title":"GitHub - baekingeol/Probing-RAG: [NAACL 2025] Official Code Repository for the paper \"Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval\"","url":"https://github.com/baekingeol/Probing-RAG"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"}]

Based on the search results, I found information about the Skill-RAG paper (arxiv 2604.15771):

Skill-RAG is a failure-aware RAG framework that couples a lightweight hidden-state prober with a prompt-based skill router. The prober gates retrieval at two pipeline stages; upon detecting a failure state, the skill router diagnoses the underlying cause and selects among four retrieval skills -- query rewriting, question decomposition, evidence focusing, and an exit skill for truly irreducible cases -- to correct misalignment.

The paper notes that while adaptive retrieval mechanisms have improved retrieval efficiency, existing approaches treat post-retrieval failure as a signal to retry rather than to diagnose, leaving structural causes of query-evidence misalignment unaddressed. The authors observe that a significant portion of persistent retrieval failures stem not from the absence of relevant evidence but from an alignment gap between the query and the evidence space.

The paper was published on arxiv on April 17, 2026. However, the search results did not return a specific GitHub repository link for the Skill-RAG code. If you're looking for the official code repository, you may need to check the paper itself on arxiv.org or contact the authors directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bad4e5a7-ab15-4cf6-acc6-2c30d8cc2df1",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "490041e1-bdc6-40f4-97d0-c5a1ba82ce3f",
  "sourceToolAssistantUUID": "bad4e5a7-ab15-4cf6-acc6-2c30d8cc2df1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-19T09:30:42.732Z_

Let me do one final round to check for TARG's code (checking the arXiv page directly) and verify the Skill-RAG situation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "490041e1-bdc6-40f4-97d0-c5a1ba82ce3f",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhCSF2wxzc8YstTMerH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c24b35b1-8c58-4348-8797-1acb549a43d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy2sUW2CpHYozA3rX7kAMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 556,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 18969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4784,
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

_source line 44 · 2026-05-19T09:30:43.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EPK69PJgp8GjDzZXSPR3G6`</summary>

```json
{
  "query": "site:github.com TARG adaptive retrieval gating Yufeng Wang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c24b35b1-8c58-4348-8797-1acb549a43d7",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhCSF2wxzc8YstTMerH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc9b9b74-877d-49e2-9a48-268f621d28d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy2sUW2CpHYozA3rX7kAMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 556,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 18969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4784,
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

_source line 45 · 2026-05-19T09:30:44.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XU37SPMR4oiEeDg1WgeVZY`</summary>

```json
{
  "query": "xiaowu0162 self-routing-rag github repository contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc9b9b74-877d-49e2-9a48-268f621d28d7",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhCSF2wxzc8YstTMerH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc452ff7-14fa-428f-aa3d-44a7987bf1ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy2sUW2CpHYozA3rX7kAMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 556,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 18969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4784,
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

_source line 46 · 2026-05-19T09:30:44.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ViQKoHyN5KrZeeYFvaLw5S`</summary>

```json
{
  "query": "Entropy-RAG github Nomothings code token entropy threshold"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc452ff7-14fa-428f-aa3d-44a7987bf1ec",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhCSF2wxzc8YstTMerH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8993a9d3-dafb-4a7e-94fa-8f5b0b598032",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy2sUW2CpHYozA3rX7kAMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 556,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 18969,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 556,
          "output_tokens": 200,
          "cache_read_input_tokens": 18969,
          "cache_creation_input_tokens": 4784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4784,
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

_source line 47 · 2026-05-19T09:30:50.078Z_

<details><summary>↩ Tool result · `toolu_01XU37SPMR4oiEeDg1WgeVZY`</summary>

```text
Web search results for query: "xiaowu0162 self-routing-rag github repository contents"

Links: [{"title":"GitHub - xiaowu0162/self-routing-rag","url":"https://github.com/xiaowu0162/self-routing-rag"},{"title":"Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization","url":"https://arxiv.org/html/2504.01018v1"},{"title":"Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization","url":"https://arxiv.org/pdf/2504.01018"},{"title":"xiaowu0162 (Di Wu) · GitHub","url":"https://github.com/xiaowu0162"},{"title":"GitHub - xiaowu0162/LongMemEval-V2: Official repository for LongMemEval-V2 · GitHub","url":"https://github.com/xiaowu0162/LongMemEval-V2"},{"title":"self-rag · GitHub Topics · GitHub","url":"https://github.com/topics/self-rag"}]

Based on the search results, here's information about the xiaowu0162 self-routing-rag GitHub repository:

The repository is the official repository for the paper "Self-Routing RAG: Binding Selective Retrieval with Knowledge Verbalization."

The Self-Routing RAG framework has the following key characteristics:

- It enables an LLM to dynamically decide between external retrieval and verbalizing its own parametric knowledge.

- It uses a multi-task objective that jointly optimizes an LLM on knowledge source selection, knowledge verbalization, and response generation.

- It introduces dynamic knowledge source inference via nearest neighbor search to improve the accuracy of knowledge source decision under domain shifts.

- Compared to the strongest selective retrieval baseline, SR-RAG reduces retrievals by 29% while improving the performance by 5.1%.

The repository can be accessed at https://github.com/xiaowu0162/self-routing-rag. The author is a PhD student at UCLA's NLP lab.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc452ff7-14fa-428f-aa3d-44a7987bf1ec",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "812276bb-55b8-4937-95fa-d9d8b4307158",
  "sourceToolAssistantUUID": "bc452ff7-14fa-428f-aa3d-44a7987bf1ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T09:30:50.784Z_

<details><summary>↩ Tool result · `toolu_01ViQKoHyN5KrZeeYFvaLw5S`</summary>

```text
Web search results for query: "Entropy-RAG github Nomothings code token entropy threshold"

Links: [{"title":"GitHub - Nomothings/Entropy-RAG: Entropy-RAG: Rethinking Retrieval-Augmented Generation from the Perspective of Entropy · GitHub","url":"https://github.com/Nomothings/Entropy-RAG"},{"title":"entropy-checking · GitHub Topics · GitHub","url":"https://github.com/topics/entropy-checking"},{"title":"[BUG] Project files switch to RAG search at 2% capacity — threshold based on file count, not token size · Issue #25759 · anthropics/claude-code","url":"https://github.com/anthropics/claude-code/issues/25759"},{"title":"Entropy · GitHub","url":"https://github.com/entropyxyz"},{"title":"Entropix - new insights on entropy-based language model reasoning | by Michael Alexander Riegler | Medium","url":"https://medium.com/@michael_79773/entropix-new-insights-on-entropy-based-language-model-reasoning-fd06f2f5ce89"},{"title":"A new, and possibly groundbreaking, method to enhancing language model reasoning with entropy-based sampling and parallel chain-of-thought decoding — Entropix | by Michael Alexander Riegler | Medium","url":"https://medium.com/@michael_79773/a-new-and-possibly-groundbreaking-method-to-enhancing-language-model-reasoning-with-entropy-based-0d38bcfe9dc5"},{"title":"GitHub Changes Token Format to Improve Identifiability, Secret Scanning, and Entropy - InfoQ","url":"https://www.infoq.com/news/2021/04/github-new-token-format/"},{"title":"feat: Automatic RAG/Full Context Strategy Based on Configurable Token Threshold · open-webui/open-webui · Discussion #19177","url":"https://github.com/open-webui/open-webui/discussions/19177"},{"title":"Insufficient Password Login Token Entropy Leads to Account Takeover","url":"https://github.com/lukevella/rallly/security/advisories/GHSA-gm8g-3r3j-48hv"},{"title":"BM𝒳: Entropy-weighted Similarity and Semantic-enhanced Lexical Search Paying tribute to BM25, the naming style of BM𝒳 follows that of BM25. 𝒳 means extension.","url":"https://arxiv.org/html/2408.06643v1"}]

Based on the search results, I found the Entropy-RAG repository on GitHub. Here's what I found:

## Entropy-RAG Overview

Entropy-RAG is a framework that integrates entropy across the entire retrieval and generation pipeline to optimize both the necessity and quality of retrieval.

## Key Components

The approach introduces three key components: (1) Entropy-Awareness, which leverages the entropy of the generated response to determine whether retrieval is required; (2) Entropy-Retrieval, which identifies the most uncertain tokens in the response to guide the generation of targeted retrieval queries; and (3) Entropy-Reranking, where retrieved contexts are re-ranked based on their entropy reduction, ensuring that only the most informative contexts contribute to the final response.

## Results

Through comprehensive evaluation on multiple standard benchmarks, Entropy-RAG significantly improves retrieval relevance and the overall quality of generated responses, with results showing substantial improvement in both the stability and accuracy of generative outputs.

The code is publicly available at https://github.com/Nomothings/Entropy-RAG.

However, the search results did not contain specific details about token entropy thresholds or their exact values in the Entropy-RAG implementation. For those specific technical details, you would need to examine the actual code repository directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8993a9d3-dafb-4a7e-94fa-8f5b0b598032",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "9d17a860-b636-4203-b537-d0d13bdaaebf",
  "sourceToolAssistantUUID": "8993a9d3-dafb-4a7e-94fa-8f5b0b598032",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T09:30:51.673Z_

<details><summary>↩ Tool result · `toolu_01EPK69PJgp8GjDzZXSPR3G6`</summary>

```text
Web search results for query: "site:github.com TARG adaptive retrieval gating Yufeng Wang"

Links: [{"title":"TARG: Training-Free Adaptive Retrieval Gating for Efficient RAG","url":"https://arxiv.org/pdf/2511.09803"},{"title":"A Note on k-NN Gating in RAG","url":"https://arxiv.org/pdf/2601.13744"},{"title":"Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2601.11443"},{"title":"Neuromodulation-inspired gated associative memory networks:extended memory retrieval and emergent multistability","url":"https://arxiv.org/pdf/2512.13859"},{"title":"TeleRAG: Efficient Retrieval-Augmented Generation Inference with Lookahead Retrieval","url":"https://arxiv.org/pdf/2502.20969"},{"title":"L-RAG: Balancing Context and Retrieval with Entropy-Based Lazy Loading","url":"https://arxiv.org/pdf/2601.06551"}]

The search results show several papers related to adaptive retrieval gating in RAG systems. The most directly relevant result is the first one:

TARG (Training-Free Adaptive Retrieval Gating for Efficient RAG) is a single-shot policy by Yufeng Wang and colleagues at Stony Brook University that decides when to retrieve using only a short, no-context draft from the base model.

From the draft's prefix logits, TARG computes lightweight uncertainty scores—including mean token entropy, a margin signal derived from the top-1/top-2 logit gap, or small-N variance across stochastic prefixes—and the gate is model-agnostic, adds only tens to hundreds of draft tokens, and requires no additional training or auxiliary heads.

On NQ-Open, TriviaQA, and PopQA benchmarks, TARG consistently shifts the accuracy-efficiency frontier compared with Always-RAG, matching or improving EM/F1 while reducing retrieval by 70-90% and cutting end-to-end latency.

However, the search results did not specifically return GitHub repository links matching the site:github.com criteria. The first result points to an arXiv PDF of the paper. You may want to search directly on GitHub for the TARG repository if you need the code implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc9b9b74-877d-49e2-9a48-268f621d28d7",
  "isSidechain": true,
  "promptId": "9f8f9822-4885-40c0-85ce-c840f5a13bf2",
  "agentId": "a08504024f81fce29",
  "type": "user",
  "uuid": "4214c7ca-8ce5-405a-8101-c66774dbe8d1",
  "sourceToolAssistantUUID": "dc9b9b74-877d-49e2-9a48-268f621d28d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-19T09:31:26.816Z_

Here is the comprehensive code availability report for all 8 selective RAG baselines:

---

## Code Availability Report for Selective RAG Baselines

### 1. Probing-RAG (arXiv:2410.13339)
- **Code available: YES**
- **GitHub URL:** https://github.com/baekingeol/Probing-RAG
- Official repo from the first author (Ingeol Baek). Published at NAACL 2025 Findings.
- Trains a lightweight prober on LLM hidden states to decide retrieval necessity.

### 2. SeaKR (arXiv:2406.19215)
- **Code available: YES**
- **GitHub URL:** https://github.com/THU-KEG/SeaKR
- Official repo from the Tsinghua KEG group. Includes dependencies (BEIR, spacy, etc.) and full experimental setup.
- Extracts self-aware uncertainty from FFN internal states.

### 3. TARG (arXiv:2511.09803)
- **Code available: NO (not found)**
- No GitHub repository found despite thorough searching. The paper (Yufeng Wang et al., Stony Brook/Westlake) does not appear to link to a code release.
- **Reimplementation complexity: LOW-MEDIUM.** TARG is explicitly "training-free" -- it computes mean token entropy, top-1/top-2 logit margin, or small-N variance from a short no-context draft. The gating logic is straightforward once you have access to model logits. The core algorithm could likely be reimplemented in a few hundred lines.

### 4. Skill-RAG (arXiv:2604.15771)
- **Code available: NO (not found)**
- Very recent paper (April 2026). No GitHub link found.
- **Reimplementation complexity: MEDIUM-HIGH.** It has two components: (1) a hidden-state prober (similar to Probing-RAG, so that part could borrow from their codebase), and (2) a prompt-based skill router that selects among four retrieval skills (query rewriting, question decomposition, evidence focusing, exit). The prober training and the skill routing logic together represent non-trivial engineering.
- **Alternative:** Could potentially adapt Probing-RAG's prober code for the hidden-state gating component.

### 5. INKER (IPM 2025)
- **Code available: NO (not found)**
- Published in Information Processing & Management. Authors (Mingjun Zhou, Xiang Zhao et al.) do not appear to have released code publicly.
- **Reimplementation complexity: MEDIUM-HIGH.** INKER integrates both internal and external knowledge signals during generation to make retrieval decisions. The multi-signal integration and the training pipeline for the adaptive gating would require substantial implementation effort.

### 6. Self-Routing RAG (arXiv:2504.01018)
- **Code available: YES**
- **GitHub URL:** https://github.com/xiaowu0162/self-routing-rag
- Official repo from Di Wu (UCLA NLP lab). Includes the full training pipeline (multi-task objective for source selection, knowledge verbalization, and response generation) and evaluation code.
- This is the most feature-complete release among the available baselines.

### 7. Rep-Con / Rep-PCA (arXiv:2411.14572)
- **Code available: NO (not found)**
- Published at NAACL 2025 by Shenglai Zeng et al. (Michigan State / Amazon). Despite the Amazon Science affiliation, no public code repository was found.
- **Reimplementation complexity: LOW-MEDIUM.** Rep-PCA applies PCA to LLM hidden representations to classify knowledge relevance -- a fairly standard linear probe approach. Rep-Con uses contrastive learning on representations, which is slightly more involved but still well-understood methodology. Both methods operate on extracted hidden states, so implementation mainly requires: (1) extracting representations at the right layer, (2) training a PCA-based or contrastive classifier.

### 8. Token-Entropy Thresholding
- **Code available: YES (multiple implementations)**
- **Entropy-RAG:** https://github.com/Nomothings/Entropy-RAG -- Uses response entropy to gate retrieval, with entropy-based reranking.
- **ETC (Entropy-Trend Constraint):** https://github.com/WisdomShell/ETC -- AAAI 2026 Oral; models entropy trends rather than isolated thresholds.
- **Reimplementation complexity: VERY LOW** even without these repos. The core idea is: compute token-level entropy from the LLM's output distribution, threshold it, and trigger retrieval when entropy exceeds the threshold. This is ~50-100 lines of code on top of any HuggingFace generation loop.

---

## Summary Table

| Baseline | Code Available | Reimplementation Difficulty |
|---|---|---|
| Probing-RAG | YES | N/A |
| SeaKR | YES | N/A |
| TARG | NO | Low-Medium |
| Skill-RAG | NO | Medium-High |
| INKER | NO | Medium-High |
| Self-Routing RAG | YES | N/A |
| Rep-Con / Rep-PCA | NO | Low-Medium |
| Token-Entropy | YES (multiple) | Very Low |

**Timeline implications:** 4 out of 8 baselines have public code (Probing-RAG, SeaKR, Self-Routing RAG, Token-Entropy). TARG and Rep-Con/Rep-PCA would be relatively straightforward to reimplement. Skill-RAG and INKER represent the biggest risks for timeline -- they have no code and non-trivial architectures. If Skill-RAG is your own work, you presumably already have the implementation. For INKER, you may want to consider whether it is essential or could be deprioritized given the lack of public code.

Sources:
- [Probing-RAG GitHub](https://github.com/baekingeol/Probing-RAG)
- [SeaKR GitHub](https://github.com/THU-KEG/SeaKR)
- [TARG arXiv](https://arxiv.org/abs/2511.09803)
- [Skill-RAG arXiv](https://arxiv.org/abs/2604.15771)
- [INKER on ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0306457325004753)
- [Self-Routing RAG GitHub](https://github.com/xiaowu0162/self-routing-rag)
- [Rep-Con/Rep-PCA arXiv](https://arxiv.org/abs/2411.14572)
- [Entropy-RAG GitHub](https://github.com/Nomothings/Entropy-RAG)
- [ETC GitHub](https://github.com/WisdomShell/ETC)
- [TARG OpenReview](https://openreview.net/forum?id=bMDdjg75NS)
- [Rep-Con/Rep-PCA NAACL](https://aclanthology.org/2025.naacl-long.151/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4214c7ca-8ce5-405a-8101-c66774dbe8d1",
  "isSidechain": true,
  "agentId": "a08504024f81fce29",
  "requestId": "req_011CbBhDMaXLoTA8Rxs8r3JH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40fc25ce-d6eb-4c46-8055-20938f6e3aee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "02d9da0e-8e85-4f5e-ab8a-8e056918e4ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Srey4pugyMRg6g9E2NdA88",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1501,
      "cache_creation_input_tokens": 1379,
      "cache_read_input_tokens": 23753,
      "output_tokens": 1777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1501,
          "output_tokens": 1777,
          "cache_read_input_tokens": 23753,
          "cache_creation_input_tokens": 1379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1379,
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
