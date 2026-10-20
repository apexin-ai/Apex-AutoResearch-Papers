# Research conversation: Search for the very latest (2025-2026) work on adaptive inference-time strategies for LLMs, especially anything related 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a979c9872a040c901.jsonl`
- **Structured JSON:** [`92687bfa983289d1b28c.json`](../../sessions/92/92687bfa983289d1b28c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-19T22:14:31.779Z_

Search for the very latest (2025-2026) work on adaptive inference-time strategies for LLMs, especially anything related to:

1. Inference-time compute allocation / adaptive processing
2. Any new work combining tokenization with reasoning quality (not just efficiency)
3. Latest results on character-level / byte-level processing at inference time
4. Any work on "reasoning-aware preprocessing" for LLMs

Use WebSearch with queries like:
- "adaptive inference-time tokenization reasoning quality LLM 2026"
- "inference-time compute allocation reasoning LLM 2026 arxiv"
- "byte-level character-level inference LLM reasoning 2026"
- "reasoning-aware input preprocessing transformer 2026"
- "token granularity reasoning performance language model 2026"

Also check Papers with Code for any new SOTA on CharBench or SubTokenTest benchmarks.

Report findings in detail (300-400 words), focusing on any new papers I should cite or position against.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "c3e23675-2312-4f5d-af29-cb7d2992157d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T22:14:31.780Z_

```json
{
  "parentUuid": "c3e23675-2312-4f5d-af29-cb7d2992157d",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
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
  "uuid": "2ed55c71-22fb-4e98-b777-1ebec9bc10ec",
  "timestamp": "2026-05-19T22:14:31.780Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T22:14:31.781Z_

```json
{
  "parentUuid": "2ed55c71-22fb-4e98-b777-1ebec9bc10ec",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e71447ab-bd5b-4ffc-a7c9-f2a3be0d9c98",
  "timestamp": "2026-05-19T22:14:31.781Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T22:14:34.202Z_



I'll search across multiple queries in parallel to find the latest work on these topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e71447ab-bd5b-4ffc-a7c9-f2a3be0d9c98",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChSxCFKAQDiLcXYksD4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba24c7fa-2300-4c19-b6a7-a0af6cc63a0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyQVpbbpwyUEfmRryttAdi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 5 · 2026-05-19T22:14:34.608Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NgEVciRBjdorRZfNcthE4L`</summary>

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
  "parentUuid": "ba24c7fa-2300-4c19-b6a7-a0af6cc63a0c",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChSxCFKAQDiLcXYksD4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df848c99-3eeb-46dc-8ef1-7f5c6a9213c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyQVpbbpwyUEfmRryttAdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 7773,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1571
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1571,
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

_source line 6 · 2026-05-19T22:14:34.612Z_

<details><summary>↩ Tool result · `toolu_01NgEVciRBjdorRZfNcthE4L`</summary>

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
  "parentUuid": "df848c99-3eeb-46dc-8ef1-7f5c6a9213c0",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "d9c87082-1bf2-47c2-8c3f-5c3ab66b929a",
  "sourceToolAssistantUUID": "df848c99-3eeb-46dc-8ef1-7f5c6a9213c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T22:14:41.813Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9c87082-1bf2-47c2-8c3f-5c3ab66b929a",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChTAWuWMNb5YENfEDo8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15b15480-b350-4bf5-9a69-56d498bd9ad7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194WKyqRzFjMYpuTwMrLSrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 9344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 8 · 2026-05-19T22:14:42.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A5KJ4gfBo1N4EgfywTTrBk`</summary>

```json
{
  "query": "adaptive inference-time tokenization reasoning quality LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15b15480-b350-4bf5-9a69-56d498bd9ad7",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChTAWuWMNb5YENfEDo8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4433b4b8-466c-428e-888a-933cffd53995",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194WKyqRzFjMYpuTwMrLSrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 9344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 9 · 2026-05-19T22:14:42.768Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMurT7yrJ5eSFqNFxq9DoU`</summary>

```json
{
  "query": "inference-time compute allocation reasoning LLM 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4433b4b8-466c-428e-888a-933cffd53995",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChTAWuWMNb5YENfEDo8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36e7aa0f-7352-4a02-9769-4b91b2f51047",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194WKyqRzFjMYpuTwMrLSrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 9344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 10 · 2026-05-19T22:14:43.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012fjUZRddHJ54BnKz5x3yxL`</summary>

```json
{
  "query": "byte-level character-level inference LLM reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36e7aa0f-7352-4a02-9769-4b91b2f51047",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChTAWuWMNb5YENfEDo8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d25ba313-2ff5-4835-ba32-7d434e4fdb8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194WKyqRzFjMYpuTwMrLSrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 9344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 11 · 2026-05-19T22:14:43.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D29Rsk9WvBZLfSddyc3DFV`</summary>

```json
{
  "query": "reasoning-aware input preprocessing transformer 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25ba313-2ff5-4835-ba32-7d434e4fdb8b",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChTAWuWMNb5YENfEDo8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60f59e6c-c52f-4792-96eb-4db1799a1ac1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194WKyqRzFjMYpuTwMrLSrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 9344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 12 · 2026-05-19T22:14:43.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NSAoVTkgkkKN4mHxjSngBq`</summary>

```json
{
  "query": "token granularity reasoning performance language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f59e6c-c52f-4792-96eb-4db1799a1ac1",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChTAWuWMNb5YENfEDo8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fbe3d51-0357-4508-bd82-9124cfe232ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194WKyqRzFjMYpuTwMrLSrc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 9344,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 9344,
          "cache_creation_input_tokens": 624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 624,
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

_source line 13 · 2026-05-19T22:14:49.520Z_

<details><summary>↩ Tool result · `toolu_01JMurT7yrJ5eSFqNFxq9DoU`</summary>

```text
Web search results for query: "inference-time compute allocation reasoning LLM 2026 arxiv"

Links: [{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via...","url":"https://arxiv.org/abs/2604.14853"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"[2605.08057] CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation","url":"https://arxiv.org/abs/2605.08057"},{"title":"Compute Allocation for Reasoning-Intensive Retrieval Agents","url":"https://arxiv.org/pdf/2603.14635"},{"title":"[2605.08057v1] CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation","url":"https://arxiv.org/abs/2605.08057v1"},{"title":"Scaling LLM Inference with Optimized Sample Compute Allocation","url":"https://arxiv.org/pdf/2410.22480"},{"title":"ROI-Reasoning: Rational Optimization for Inference via Pre-Computation Meta-Cognition","url":"https://arxiv.org/pdf/2601.03822"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/pdf/2512.02008"}]

I found several recent arxiv papers on inference-time compute allocation for reasoning LLMs from 2026. Here are the key results:

## Recent Papers (2026)

**1. Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization**
This paper addresses the challenge of deciding which inputs deserve more compute and which can be answered cheaply during inference. The framework uses constrained optimization where oracle labels arise from Lagrangian relaxation of a well-defined primal problem, with a dual variable that controls the accuracy-cost tradeoff. Published April 16, 2026 (arxiv:2604.14853).

**2. CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation**
Published May 8, 2026 (arxiv:2605.08057), this work focuses on complexity-aware compute allocation for text-to-SQL tasks.

**3. Compute Allocation for Reasoning-Intensive Retrieval Agents**
This presents a systematic study of compute allocation in LLM-augmented retrieval using BRIGHT as a testbed, varying model capacity, inference-time thinking, and re-ranking depth. The findings suggest that compute should be concentrated on re-ranking rather than distributed uniformly across pipeline stages.

These papers address a key challenge: large reasoning models frequently waste resources by "overthinking" simple queries while failing to allocate sufficient compute to more complex problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36e7aa0f-7352-4a02-9769-4b91b2f51047",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "8a7b59ca-2f79-4c63-856f-8bc5a79b172f",
  "sourceToolAssistantUUID": "36e7aa0f-7352-4a02-9769-4b91b2f51047",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:14:49.528Z_

<details><summary>↩ Tool result · `toolu_01A5KJ4gfBo1N4EgfywTTrBk`</summary>

```text
Web search results for query: "adaptive inference-time tokenization reasoning quality LLM 2026"

Links: [{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853v1"},{"title":"DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference","url":"https://arxiv.org/html/2510.19669v2"},{"title":"Dynamic Adaptive Reasoning: Optimizing LLM Inference-Time Thinking via Intent-Aware Scheduling[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.0291/download/final_file"},{"title":"DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference","url":"https://arxiv.org/pdf/2510.19669"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/html/2505.11274v6"},{"title":"Decomposing Reasoning Efficiency in Large Language Models","url":"https://arxiv.org/pdf/2602.09805"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/pdf/2506.01084"},{"title":"Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data","url":"https://arxiv.org/pdf/2601.11038"}]

Based on the search results, here are key findings about adaptive inference-time tokenization and reasoning quality for LLMs in 2026:

## Adaptive Inference-Time Tokenization

A significant development is "zip2zip," which addresses how tokenizers convert raw text into token sequences, with tokenization efficiency having major impacts on model performance. While most LLMs use fixed, static vocabularies based on general-purpose corpora, these often fail to adapt to domain-specific distributions. More compact tokenization yields benefits including larger effective context windows, lower computational costs, and shorter response times.

## Adaptive Reasoning and Token Efficiency

Several frameworks have emerged to optimize inference-time reasoning:

- DiffAdapt is a framework that selects Easy/Normal/Hard inference strategies per question based on difficulty, achieving comparable or improved accuracy while reducing token usage by up to 22.4%.

- The Intent-Aware Reasoning Scheduler (IARS) dynamically refines inference-time reasoning by analyzing generated thought tokens to identify reasoning states and issue adaptive directives to modulate reasoning depth and style.

- Inference-time computation can significantly improve LLM performance through chain-of-thought prompting, self-consistency aggregation, tree search, and process reward models.

## Reasoning Quality Challenges

Extended reasoning traces can trade tokens for accuracy, but the "overthinking" phenomenon occurs where extended Chain-of-Thought actually degrades performance through hallucinated doubt and error propagation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4433b4b8-466c-428e-888a-933cffd53995",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "33502f6b-5f82-47da-a006-bba0576c5dbc",
  "sourceToolAssistantUUID": "4433b4b8-466c-428e-888a-933cffd53995",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T22:14:50.052Z_

<details><summary>↩ Tool result · `toolu_012fjUZRddHJ54BnKz5x3yxL`</summary>

```text
Web search results for query: "byte-level character-level inference LLM reasoning 2026"

Links: [{"title":"LLM Fundamentals — Tokens, Attention & Transformers (2026) | MyEngineeringPath","url":"https://myengineeringpath.dev/genai-engineer/llm-fundamentals/"},{"title":"Bolmo: Byteifying the Next Generation of Language Models","url":"https://arxiv.org/pdf/2512.15586"},{"title":"Don't Overthink it. Preferring Shorter Thinking Chains for Improved LLM Reasoning","url":"https://arxiv.org/pdf/2505.17813"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.27246"},{"title":"RL of Thoughts: Navigating LLM Reasoning with Inference-time Reinforcement Learning","url":"https://arxiv.org/pdf/2505.14140"},{"title":"Character-Level LLMs","url":"https://www.emergentmind.com/topics/character-level-llms"},{"title":"mrt5: dynamic token merging for efficient byte-level ...","url":"https://arxiv.org/pdf/2410.20771"}]

Based on the search results, here's what I found regarding byte-level and character-level inference for LLM reasoning in 2026:

## Byte-Level Models

Bolmo is a family of fully open byte-level LLMs that approach the capabilities of subword-based systems and excel on character-level reasoning tasks, while remaining competitive across standard benchmarks. These models achieve practical inference speeds and can be adapted at low cost using the existing ecosystem around the source LLM.

Byte-level models that operate directly on the byte encoding of text avoid limitations of subword tokenization, though until recently they lagged behind subword-based models in performance. Subword tokenization causes limited character-level understanding, which especially hinders performance on scientific data such as code and biological sequences.

## Character-Level Reasoning

Subword-tokenized LLMs struggle with basic tasks requiring character-level understanding, such as string manipulation, spelling correction, and intra-token position prediction. A divide-and-conquer approach decomposes character operations into token atomization, per-character manipulation, and controlled token reconstruction stages.

## LLM Reasoning in 2026

OpenAI's o1 and o3, Anthropic's Claude extended thinking, and Google's Gemini thinking mode introduced models that "think" before responding using chain-of-thought reasoning internally to improve accuracy on hard problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d25ba313-2ff5-4835-ba32-7d434e4fdb8b",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "35fe2caa-ac28-46a3-9289-840e78b17bc7",
  "sourceToolAssistantUUID": "d25ba313-2ff5-4835-ba32-7d434e4fdb8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T22:14:50.352Z_

<details><summary>↩ Tool result · `toolu_01NSAoVTkgkkKN4mHxjSngBq`</summary>

```text
Web search results for query: "token granularity reasoning performance language model 2026"

Links: [{"title":"[2602.14386] Beyond Token-Level Policy Gradients for Complex Reasoning with Large Language Models","url":"https://arxiv.org/abs/2602.14386"},{"title":"[2511.05722] OckBench: Measuring the Efficiency of LLM Reasoning","url":"https://arxiv.org/abs/2511.05722"},{"title":"Use large language model to enhance reasoning of another large language model through reward updated GRPO | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-39296-8"},{"title":"Decomposing Reasoning Efficiency in Large Language Models","url":"https://arxiv.org/pdf/2602.09805"},{"title":"The Impact of Token Granularity on the Predictive Power of Language Model Surprisal","url":"https://arxiv.org/html/2412.11940v1"},{"title":"The Impact of Token Granularity on the Predictive Power of Language Model Surprisal","url":"https://arxiv.org/pdf/2412.11940"}]

Based on the search results, here's what recent research shows about token granularity and reasoning performance in language models:

## Token Efficiency in Reasoning

Research shows that token-level policy gradients have limitations for complex reasoning, motivating future research to look beyond token-level granularity for reasoning-intensive language tasks. Block-level perspectives can capture the compositional structure of reasoning trajectories and support optimization over coherent, higher-level objectives.

## Token Efficiency Metrics

Models solving the same problem with similar accuracy can exhibit up to a 5.0× difference in token length, leading to massive gaps in model reasoning ability. There has been a shift from scaling pre-training to scaling inference-time compute, with models like OpenAI's o1/o3 and DeepSeek-R1 generating extended reasoning traces that trade tokens for accuracy.

## Token Granularity and Language Model Quality

Regression experiments reveal a strong influence of token granularity on the predictive power of surprisal, with tokens defined by a vocabulary size of 4,000 resulting in surprisal that is most predictive. Token granularity plays a large role on the quality of language model surprisal for cognitive modeling, with different levels of granularity being more appropriate for different tasks.

The research indicates that token granularity is a critical but often overlooked factor affecting both reasoning efficiency and the overall quality of language model performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fbe3d51-0357-4508-bd82-9124cfe232ba",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "4e914ae4-8434-4cc6-bce3-63c32f884494",
  "sourceToolAssistantUUID": "3fbe3d51-0357-4508-bd82-9124cfe232ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T22:14:52.441Z_

<details><summary>↩ Tool result · `toolu_01D29Rsk9WvBZLfSddyc3DFV`</summary>

```text
Web search results for query: "reasoning-aware input preprocessing transformer 2026"

Links: [{"title":"Transcoder Adapters for Reasoning-Model Diffing","url":"https://arxiv.org/pdf/2602.20904"},{"title":"Paper page - LoopFormer: Elastic-Depth Looped Transformers for Latent Reasoning via Shortcut Modulation","url":"https://huggingface.co/papers/2602.11451"},{"title":"[2602.11852] Prototype Transformer: Towards Language Model Architectures Interpretable by Design","url":"https://arxiv.org/abs/2602.11852"},{"title":"[2602.11852v1] Prototype Transformer: Towards Language Model Architectures Interpretable by Design","url":"https://arxiv.org/abs/2602.11852v1"},{"title":"LoopFormer: Elastic-Depth Looped Transformers for Latent Reasoning via Shortcut Modulation","url":"https://loopformer.github.io/"},{"title":"A transformer architecture alteration to incentivise externalised reasoning","url":"https://arxiv.org/pdf/2603.21376"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=Yxz92UuPLQ"},{"title":"Transformers meet Neural Algorithmic Reasoners","url":"https://arxiv.org/pdf/2406.09308"}]

Based on the search results, here are the relevant findings for "reasoning-aware input preprocessing transformer 2026":

The search returned several papers from 2026 related to reasoning-aware transformers:

1. **LoopFormer**: Accepted to ICLR 2026, LoopFormer is an elastic-depth looped Transformer for budget-conditioned language modeling and latent reasoning, trained with trajectory conditioning and shortcut-consistency regularization. LoopFormer enables budget-conditioned latent reasoning with elastic computational depth.

2. **Prototype Transformer**: Submitted in February 2026, this paper proposes language model architectures designed to be interpretable by design, addressing concerns about the opacity of model reasoning.

3. **TransNAR (Transformers meet Neural Algorithmic Reasoners)**: This work proposes a hybrid architecture combining the language understanding of a Transformer with the robustness of reasoning of a pre-trained GNN-based NAR.

4. **Reasoning-focused architecture modifications**: Papers explore Chain-of-Thought (CoT) reasoning in Language Models, which allows models to produce intermediate reasoning tokens before arriving at final answers, now standard practice to train models to produce via reinforcement learning.

These papers represent recent advances in designing transformers that incorporate reasoning awareness into their architectures and input processing mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60f59e6c-c52f-4792-96eb-4db1799a1ac1",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "1eade4a3-b75d-443c-b088-6106a2457b35",
  "sourceToolAssistantUUID": "60f59e6c-c52f-4792-96eb-4db1799a1ac1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T22:14:55.386Z_

Now let me run a few more targeted searches to cover the specific benchmarks and the zip2zip paper more closely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eade4a3-b75d-443c-b088-6106a2457b35",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChUUVv5iq1a2L1gx1iN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23a00a69-163d-4965-bedf-e9ed3977ce5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8XPnav1HzAxp8B5SSHUMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 638,
      "cache_creation_input_tokens": 3185,
      "cache_read_input_tokens": 9968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3185,
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

_source line 19 · 2026-05-19T22:14:55.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KXF6MRQ21ZqNCXAWrw3TMC`</summary>

```json
{
  "query": "zip2zip inference-time adaptive tokenization online compression arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23a00a69-163d-4965-bedf-e9ed3977ce5c",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChUUVv5iq1a2L1gx1iN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b161859b-5816-468c-a37f-c66997b1066b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8XPnav1HzAxp8B5SSHUMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 638,
      "cache_creation_input_tokens": 3185,
      "cache_read_input_tokens": 9968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3185,
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

_source line 20 · 2026-05-19T22:14:57.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KnrX1eUSt7zKa6rRVLpT1H`</summary>

```json
{
  "query": "CharBench SubTokenTest benchmark character-level LLM papers with code 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b161859b-5816-468c-a37f-c66997b1066b",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChUUVv5iq1a2L1gx1iN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebc1a563-d96b-4f5f-9703-82a9fb5939a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8XPnav1HzAxp8B5SSHUMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 638,
      "cache_creation_input_tokens": 3185,
      "cache_read_input_tokens": 9968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3185,
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

_source line 21 · 2026-05-19T22:14:57.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Fcmb32feeSzEHCdnkx7dv`</summary>

```json
{
  "query": "Bolmo byte-level language model reasoning benchmark results 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebc1a563-d96b-4f5f-9703-82a9fb5939a8",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChUUVv5iq1a2L1gx1iN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb1c8daa-2590-4b19-827e-42d667db8881",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8XPnav1HzAxp8B5SSHUMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 638,
      "cache_creation_input_tokens": 3185,
      "cache_read_input_tokens": 9968,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3185
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 638,
          "output_tokens": 202,
          "cache_read_input_tokens": 9968,
          "cache_creation_input_tokens": 3185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3185,
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

_source line 22 · 2026-05-19T22:15:01.975Z_

<details><summary>↩ Tool result · `toolu_01KXF6MRQ21ZqNCXAWrw3TMC`</summary>

```text
Web search results for query: "zip2zip inference-time adaptive tokenization online compression arxiv 2025 2026"

Links: [{"title":"[2506.01084] zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/abs/2506.01084"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/pdf/2506.01084"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression | OpenReview","url":"https://openreview.net/forum?id=Hmepi1Fm2g"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/html/2506.01084v2"},{"title":"NeurIPS Poster zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118871"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://openreview.net/pdf/ed004e39a9e62f3d9362fc1117b0756ee480c81f.pdf"}]

I found the paper you're looking for! Here's what I found about zip2zip:

zip2zip is a novel method for achieving context-adaptive tokenization in LLMs at inference time. It leverages an online data compression algorithm (Lempel-Ziv-Welch) to dynamically expand its active vocabulary at inference time by continuously replacing fragmented token sequences with more compact hypertokens.

The method consists of three key components: (1) a tokenizer based on Lempel-Ziv-Welch (LZW) compression that incrementally merges co-occurring tokens into reusable hypertokens on the fly; (2) an embedding layer that computes embeddings for newly formed hypertokens at runtime; and (3) a causal language modeling variant that trains the model to operate on hypertokenized, compressed sequences.

The resulting zip2zip LLMs effectively learn to use hypertokens at inference time, reducing input and output sequence length by 20–60%, with significant improvements in inference latency. Additionally, an existing LLM can be zip2zip-fied in 10 GPU-hours via parameter-efficient finetuning.

The paper was posted to arXiv in October 2025 (arXiv ID: 2506.01084) and has also been presented at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b161859b-5816-468c-a37f-c66997b1066b",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "4808997e-b943-46e6-a17d-08f3a4c3d056",
  "sourceToolAssistantUUID": "b161859b-5816-468c-a37f-c66997b1066b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T22:15:03.676Z_

<details><summary>↩ Tool result · `toolu_011Fcmb32feeSzEHCdnkx7dv`</summary>

```text
Web search results for query: "Bolmo byte-level language model reasoning benchmark results 2025 2026"

Links: [{"title":"[2512.15586] Bolmo: Byteifying the Next Generation of Language Models","url":"https://arxiv.org/abs/2512.15586"},{"title":"Bolmo Advances Byte-Level Language Models with Practicality | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2025/bolmo-advances-byte-level-language-models-with-practicality"},{"title":"Ai2 Unveils Bolmo: Open Byte‑Level Language Models Built on Olmo 3 for Enterprise‑Ready Multilingual Robustness – Archyde","url":"https://www.archyde.com/ai2-unveils-bolmo-open-byte-level-language-models-built-on-olmo-3-for-enterprise-ready-multilingual-robustness/"},{"title":"Bolmo: Byteifying the Next Generation of Language Models Benjamin Minixhofer","url":"https://arxiv.org/pdf/2512.15586"},{"title":"(PDF) Bolmo: Byteifying the Next Generation of Language Models","url":"https://www.researchgate.net/publication/398806418_Bolmo_Byteifying_the_Next_Generation_of_Language_Models"},{"title":"Introducing Bolmo: Byteifying the next generation of language models | Ai2","url":"https://allenai.org/blog/bolmo"},{"title":"allenai/Bolmo-7B · Hugging Face","url":"https://huggingface.co/allenai/Bolmo-7B"}]

I found comprehensive information about Bolmo, the byte-level language model from AI2. Here are the key benchmark results:

## Performance on Standard Benchmarks

Bolmo 7B performs comparably to the original subword Olmo 3 7B on broad benchmarks but substantially outperforms it on character-focused tasks like CUTE and EXECUTE, improving accuracy by nearly twenty points on character aggregates.

## Character-Level Reasoning Results

On the character aggregate, Bolmo 7B improves accuracy by nearly twenty points over Olmo 3. The resulting models outperform prior byte-level approaches and excel on character-level reasoning tasks, while remaining competitive across standard benchmarks.

## Multilingual Performance

Bolmo attains an average 0.85 BLEU score on the WMT-22 multilingual benchmark, outperforming prior open-source baselines by 12%.

## Overall Assessment

AI2 evaluated Bolmo across math, STEM reasoning, questions, general knowledge, and coding, with Bolmo 7B exceeding performance on coding, mathematical tasks, and multi-choice questions, while also showing improved accuracy over the Olmo 3 base model.

The research was published in December 2025 and updated in February 2026, with the models being made fully open-source by AI2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb1c8daa-2590-4b19-827e-42d667db8881",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "43ac0f4f-1104-4848-9870-db2526d8b22f",
  "sourceToolAssistantUUID": "eb1c8daa-2590-4b19-827e-42d667db8881",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T22:15:04.980Z_

<details><summary>↩ Tool result · `toolu_01KnrX1eUSt7zKa6rRVLpT1H`</summary>

```text
Web search results for query: "CharBench SubTokenTest benchmark character-level LLM papers with code 2025 2026"

Links: [{"title":"[2508.02591] CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/abs/2508.02591"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/html/2508.02591v2"},{"title":"SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding","url":"https://arxiv.org/pdf/2601.09089"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks | Request PDF","url":"https://www.researchgate.net/publication/402627608_CharBench_Evaluating_the_Role_of_Tokenization_in_Character-Level_Tasks"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/pdf/2508.02591"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks - Paper Detail","url":"https://deeplearn.org/arxiv/625867/charbench:-evaluating-the-role-of-tokenization-in-character-level-tasks"},{"title":"CharacterBench: Benchmarking Character Customization of Large Language   Models","url":"https://arxiv.org/pdf/2412.11912"},{"title":"(PDF) CharacterBench: Benchmarking Character Customization of Large Language Models","url":"https://www.researchgate.net/publication/387105156_CharacterBench_Benchmarking_Character_Customization_of_Large_Language_Models"},{"title":"ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code","url":"https://arxiv.org/pdf/2506.02314"}]

Based on the search results, I found relevant information about the benchmarks you're looking for:

## CharBench

CharBench is a paper titled "Evaluating the Role of Tokenization in Character-Level Tasks" by Omri Uzan and others, with the latest version updated on April 6, 2026. CharBench is a comprehensive benchmark of character-level tasks that is two orders of magnitude larger than existing alternatives. 

Code and data are available at https://github.com/omriuz/CharBench. The paper examines language models' reliance on subword units rather than characters and their struggles with character-level tasks, with recent studies offering conflicting conclusions about the role of tokenization.

## SubTokenTest

SubTokenTest is a benchmark that includes ten tasks across four domains and isolates tokenization-related failures by decoupling performance from complex reasoning, with a comprehensive evaluation of nine advanced LLMs. Code is available at Shu-Feather/SubTokenTest with a dataset at Rain-air/SubTokenTest-QA.

The benchmark further tests test-time scaling for reasoning models and examines whether internal representations encode character-level information across diverse text forms, including normal words, typos, random character sequences, and special symbols.

Both benchmarks focus on evaluating how language models handle character-level tasks and the role of tokenization in their performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebc1a563-d96b-4f5f-9703-82a9fb5939a8",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "484cfab9-9311-416f-bd5a-a64dfe80e626",
  "sourceToolAssistantUUID": "ebc1a563-d96b-4f5f-9703-82a9fb5939a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T22:15:07.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPWWxhNcxQMahDfGJniorz`</summary>

```json
{
  "query": "SelfBudgeter adaptive token allocation efficient LLM reasoning arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "484cfab9-9311-416f-bd5a-a64dfe80e626",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChVQAzfYXtCJ3c3jzuB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7643436-d81b-4080-91e4-0f86aa93d5b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5WYTqqtSFHtYUumttXtDk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 2437,
      "cache_read_input_tokens": 13153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2437,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 26 · 2026-05-19T22:15:08.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqvVLHAM7RWbxYcVzMk49w`</summary>

```json
{
  "query": "\"token granularity\" \"reasoning quality\" tokenization impact LLM performance arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7643436-d81b-4080-91e4-0f86aa93d5b1",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChVQAzfYXtCJ3c3jzuB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0a1a9b5-0727-472e-af5b-d2a04a727b27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5WYTqqtSFHtYUumttXtDk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 2437,
      "cache_read_input_tokens": 13153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2437,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 27 · 2026-05-19T22:15:14.287Z_

<details><summary>↩ Tool result · `toolu_01VPWWxhNcxQMahDfGJniorz`</summary>

```text
Web search results for query: "SelfBudgeter adaptive token allocation efficient LLM reasoning arxiv 2025"

Links: [{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250511274L/abstract"},{"title":"[PDF] SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SelfBudgeter:-Adaptive-Token-Allocation-for-LLM-Li-Dong/569a37483dd8ecebc66b145fdc8226f11474329d"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/pdf/2505.11274"},{"title":"[2505.11274] SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2505.11274"},{"title":"Paper page - SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://huggingface.co/papers/2505.11274"},{"title":"SelfBudgeter: ADAPTIVE TOKEN ALLOCATION","url":"https://openreview.net/pdf/aa5f43e556d443896b88ca5452e63b48efa12bb7.pdf"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=e7EBzbi8Qd"}]

I found the research paper on SelfBudgeter. Here's what I found:

## SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning

SelfBudgeter is authored by Zheng Li, Qingxiu Dong, Jingyuan Ma, Di Zhang, and Zhifang Sui from Peking University.

**Problem**: Reasoning models consume excessive tokens even for simple queries, leading to resource waste and prolonged user latency.

**Solution**: SelfBudgeter is a self-adaptive controllable reasoning strategy for efficient reasoning. It adopts a dual-phase training paradigm where the model learns to pre-estimate the reasoning cost based on query difficulty, then uses budget-guided GPRO for reinforcement learning to maintain accuracy while reducing output length.

**Key Features**: 
- Users can anticipate generation time and make informed decisions about continuing or interrupting the process
- The method enables direct manipulation of reasoning length via pre-filling token budget

**Performance**: SelfBudgeter achieves up to 74.47% response length compression on the MATH benchmark while maintaining nearly undiminished accuracy.

The paper was published on arXiv on May 16, 2025 (arXiv:2505.11274).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7643436-d81b-4080-91e4-0f86aa93d5b1",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "27ed5f86-3c6b-4456-94d3-6b33842eee02",
  "sourceToolAssistantUUID": "b7643436-d81b-4080-91e4-0f86aa93d5b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T22:15:15.036Z_

<details><summary>↩ Tool result · `toolu_01NqvVLHAM7RWbxYcVzMk49w`</summary>

```text
Web search results for query: ""token granularity" "reasoning quality" tokenization impact LLM performance arxiv 2025 2026"

Links: [{"title":"Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits","url":"https://arxiv.org/pdf/2505.14178"},{"title":"How Different Tokenization Algorithms Impact LLMs and Transformer Models for Binary Code Analysis","url":"https://arxiv.org/html/2511.03825v1"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/pdf/2512.21933"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.14658"},{"title":"Tokenization counts: the impact of tokenization on arithmetic in   frontier LLMs","url":"https://arxiv.org/pdf/2402.14903"},{"title":"Counting Ability of Large Language Models and Impact of Tokenization","url":"https://arxiv.org/pdf/2410.19730"},{"title":"Not All Tokens Matter: Towards Efficient LLM Reasoning via Token Significance in Reinforcement Learning","url":"https://arxiv.org/html/2506.08125v2"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/html/2601.14658v1"}]

I found several highly relevant research papers from arXiv (2025-2026) on token granularity, reasoning quality, and tokenization's impact on LLM performance:

## Key Findings:

**1. Token Granularity and Reasoning Performance**

Poor token granularity disrupts logical alignment and prevents models from generalizing symbolic procedures, with token structure dramatically affecting reasoning performance and causing failure even with Chain-of-Thought prompts, while atomically-aligned formats unlock strong generalization.

**2. Impact on Symbolic and Arithmetic Reasoning**

Symbolic reasoning ability in LLMs is not purely architectural, but deeply conditioned on token-level representations. Modern byte pair encoding (BPE) tokenization groups multiple characters into a single token for efficiency, which degrades performance in arithmetic tasks due to information loss during tokenization.

**3. Tokenization's Effect on Quantitative Reasoning**

Greedy left-to-right subword tokenization can split integers and dates into arbitrary, non-semantic fragments, thereby obscuring the positional structure required for arithmetic and temporal inference.

**4. Token Significance in Reasoning Efficiency**

Many tokens in chain-of-thought reasoning contribute little to the final answer, indicating token redundancy in LLMs.

The research papers suggest that tokenization is a fundamental, often-overlooked factor in LLM reasoning capabilities, with significant implications for model architecture design and performance optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0a1a9b5-0727-472e-af5b-d2a04a727b27",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a979c9872a040c901",
  "type": "user",
  "uuid": "17bbe1f1-7f81-418e-8be5-0f744b34d815",
  "sourceToolAssistantUUID": "b0a1a9b5-0727-472e-af5b-d2a04a727b27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T22:15:52.227Z_

Here is a detailed report of the latest findings across your four areas of interest:

---

## 1. Inference-Time Compute Allocation / Adaptive Processing

This is the most active area. Several key 2026 papers stand out:

- **Adaptive Test-Time Compute Allocation via Constrained Policy Optimization** (arXiv:2604.14853, April 2026) frames the "how much compute per input" question as a constrained optimization problem with Lagrangian relaxation, yielding a dual variable that directly controls the accuracy-cost tradeoff. This is likely the most rigorous formalization to date and should be cited.

- **SelfBudgeter** (arXiv:2505.11274, May 2025, updated through 2026) uses a dual-phase training paradigm: the model first pre-estimates reasoning cost based on query difficulty, then undergoes budget-guided GRPO reinforcement learning. Achieves 74.47% response length compression on MATH with near-zero accuracy loss.

- **DiffAdapt** (arXiv:2510.19669) selects Easy/Normal/Hard inference strategies per question, reducing token usage by up to 22.4% while maintaining or improving accuracy.

- **LoopFormer** (ICLR 2026) introduces elastic-depth looped Transformers for budget-conditioned latent reasoning, trained with trajectory conditioning and shortcut-consistency regularization -- relevant if you discuss architectural approaches to adaptive compute.

## 2. Tokenization and Reasoning Quality

This is directly in your lane. Two papers are essential to position against:

- **"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs"** (arXiv:2601.14658, Jan 2026) demonstrates that poor token granularity disrupts logical alignment and prevents generalization of symbolic procedures, while atomically-aligned tokenization formats unlock strong generalization. This is perhaps the closest existing work to your thesis.

- **"Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits"** (arXiv:2505.14178) shows that reasoning ability is deeply conditioned on token-level representations, not purely architectural. BPE tokenization degrades arithmetic performance due to information loss.

- **"The Impact of Token Granularity on the Predictive Power of Language Model Surprisal"** (arXiv:2412.11940) finds a vocabulary size of ~4,000 tokens produces the most predictive surprisal, suggesting a sweet spot in granularity.

## 3. Byte-Level / Character-Level Processing at Inference

- **Bolmo** (arXiv:2512.15586, AI2, Dec 2025 / updated Feb 2026) is the standout. This family of fully open byte-level LLMs improves character-level reasoning accuracy by nearly 20 points over subword-based OLMo 3, while remaining competitive on standard benchmarks. Models are at `allenai/Bolmo-7B` on HuggingFace.

- **zip2zip** (arXiv:2506.01084, NeurIPS 2025) is highly relevant -- it performs inference-time adaptive tokenization via online LZW compression, dynamically merging co-occurring tokens into "hypertokens." Reduces sequence length by 20-60% with significant latency gains. An existing LLM can be "zip2zip-fied" in 10 GPU-hours via PEFT. This is the closest prior work to inference-time tokenization adaptation.

## 4. Reasoning-Aware Preprocessing

No paper uses exactly the term "reasoning-aware preprocessing," which means you may have a framing advantage. The closest work is the "Say Anything but This" paper above, plus **"Beyond Token-Level Policy Gradients"** (arXiv:2602.14386, Feb 2026), which argues that block-level perspectives better capture compositional reasoning structure than token-level optimization.

## Benchmark Status (CharBench / SubTokenTest)

- **CharBench** (arXiv:2508.02591, updated April 2026) is active with code at `github.com/omriuz/CharBench`. It is two orders of magnitude larger than prior character-level benchmarks.
- **SubTokenTest** (arXiv:2601.09089) isolates tokenization-related failures from reasoning failures and tests whether internal representations encode character-level information across normal words, typos, and random sequences. Code at `Shu-Feather/SubTokenTest`.

No new SOTA claims were found on Papers with Code for either benchmark beyond the Bolmo results.

**Key positioning recommendation**: The zip2zip and "Say Anything but This" papers are the two you most need to cite and differentiate from. Your "reasoning-aware preprocessing" framing appears novel -- no one is using that terminology yet.

Sources:
- [Adaptive Test-Time Compute Allocation (2604.14853)](https://arxiv.org/abs/2604.14853)
- [SelfBudgeter (2505.11274)](https://arxiv.org/abs/2505.11274)
- [DiffAdapt (2510.19669)](https://arxiv.org/html/2510.19669v2)
- [LoopFormer (ICLR 2026)](https://huggingface.co/papers/2602.11451)
- [Say Anything but This (2601.14658)](https://arxiv.org/html/2601.14658v1)
- [Tokenization Constraints in LLMs (2505.14178)](https://arxiv.org/pdf/2505.14178)
- [Token Granularity and Surprisal (2412.11940)](https://arxiv.org/html/2412.11940v1)
- [Bolmo (2512.15586)](https://arxiv.org/abs/2512.15586)
- [zip2zip (2506.01084)](https://arxiv.org/abs/2506.01084)
- [Beyond Token-Level Policy Gradients (2602.14386)](https://arxiv.org/abs/2602.14386)
- [CharBench (2508.02591)](https://arxiv.org/abs/2508.02591)
- [SubTokenTest (2601.09089)](https://arxiv.org/pdf/2601.09089)
- [Decomposing Reasoning Efficiency (2602.09805)](https://arxiv.org/pdf/2602.09805)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17bbe1f1-7f81-418e-8be5-0f744b34d815",
  "isSidechain": true,
  "agentId": "a979c9872a040c901",
  "requestId": "req_011CbChW97uU7opRMgT8ZroL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "676642a8-3ab4-456c-94d3-20e2a935dede",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdnZe22rAzgwzM36BUw2uq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 15590,
      "output_tokens": 1554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1554,
          "cache_read_input_tokens": 15590,
          "cache_creation_input_tokens": 2394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2394,
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
