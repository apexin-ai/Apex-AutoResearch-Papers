# Research conversation: I need to research the actual performance of Qwen3-235B-A22B on math benchmarks, especially AIME, to understand what con

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad90108251e21a4c4.jsonl`
- **Structured JSON:** [`0d57553171cbad5057de.json`](../../sessions/0d/0d57553171cbad5057de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-28T01:29:45.827Z_

I need to research the actual performance of Qwen3-235B-A22B on math benchmarks, especially AIME, to understand what constitutes "frontier-hard" problems for this model.

Please:
1. Search for "Qwen3-235B AIME 2025 performance accuracy"
2. Search for "Qwen3-235B-A22B math benchmark results"
3. Search for "Qwen3 235B pass@1 AIME AMC competition math"
4. Search for "FrontierMath benchmark LLM performance 2026"
5. Search for "hardest math benchmarks LLM 2026 beyond AIME"

I need to know:
- Qwen3-235B-A22B's actual performance on AIME 2025 (reviewer claims 81.5%)
- Which specific AIME problems (if any data available) it fails on
- What benchmarks are genuinely "frontier-hard" for current models (where pass@1 < 10%)
- FrontierMath performance data
- IMO-level problem performance
- How many problems per year on AIME/AMC are actually hard for frontier models

Report in detail (300-400 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "7ab14137-be21-4432-a6e5-c2732b50a2b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T01:29:45.831Z_

```json
{
  "parentUuid": "7ab14137-be21-4432-a6e5-c2732b50a2b9",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
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
  "uuid": "567a051e-1942-483a-84f4-62f1888e92a0",
  "timestamp": "2026-05-28T01:29:45.831Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T01:29:45.834Z_

```json
{
  "parentUuid": "567a051e-1942-483a-84f4-62f1888e92a0",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ec9f5152-ae33-4d6c-aa87-140f6fb62eb8",
  "timestamp": "2026-05-28T01:29:45.834Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T01:29:48.003Z_



I'll search for this information across the web.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec9f5152-ae33-4d6c-aa87-140f6fb62eb8",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6omimvZytWCau2KFNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4cb1e67-7183-4e21-83fc-b2148d5bdc30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVkBJDhA6p54L3JJD5zx6V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 7411,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1621
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1621,
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

### Tool call

_source line 5 · 2026-05-28T01:29:48.011Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q3B9uaBXCoXpwuPEV9GMdx`</summary>

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
  "parentUuid": "a4cb1e67-7183-4e21-83fc-b2148d5bdc30",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6omimvZytWCau2KFNF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf28b66-34f0-4eb9-b822-31508411f4b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVkBJDhA6p54L3JJD5zx6V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 7411,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1621
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1621,
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

_source line 6 · 2026-05-28T01:29:48.017Z_

<details><summary>↩ Tool result · `toolu_01Q3B9uaBXCoXpwuPEV9GMdx`</summary>

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
  "parentUuid": "ecf28b66-34f0-4eb9-b822-31508411f4b0",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "c166db02-de5b-40f5-a06d-ebb8760d3cd8",
  "sourceToolAssistantUUID": "ecf28b66-34f0-4eb9-b822-31508411f4b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T01:29:49.790Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c166db02-de5b-40f5-a06d-ebb8760d3cd8",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6owMDPDNVTTXEXmzYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b64a7a42-825f-4349-944a-525e96573e02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAEeDXyjKG44EpvFjsfsEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 617,
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

_source line 8 · 2026-05-28T01:29:50.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DTf5tQACmV9GpqT4uBCk8f`</summary>

```json
{
  "query": "Qwen3-235B AIME 2025 performance accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b64a7a42-825f-4349-944a-525e96573e02",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6owMDPDNVTTXEXmzYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17d319dd-4f71-4920-8f98-085c63ad1b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAEeDXyjKG44EpvFjsfsEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 617,
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

_source line 9 · 2026-05-28T01:29:50.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERDCGq742yjoGzsNnHR3wa`</summary>

```json
{
  "query": "Qwen3-235B-A22B math benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17d319dd-4f71-4920-8f98-085c63ad1b70",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6owMDPDNVTTXEXmzYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90386cdb-81f5-416b-9be9-8232f823b9ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAEeDXyjKG44EpvFjsfsEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 617,
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

_source line 10 · 2026-05-28T01:29:51.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J5YqrYq53DzzmrezaFuv2x`</summary>

```json
{
  "query": "Qwen3 235B pass@1 AIME AMC competition math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90386cdb-81f5-416b-9be9-8232f823b9ad",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6owMDPDNVTTXEXmzYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49b4d21a-7d36-4a8a-83ab-5739bdb59115",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAEeDXyjKG44EpvFjsfsEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 617,
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

_source line 11 · 2026-05-28T01:29:51.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012LtppzkZ2A3gMnaAJujnWz`</summary>

```json
{
  "query": "FrontierMath benchmark LLM performance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49b4d21a-7d36-4a8a-83ab-5739bdb59115",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6owMDPDNVTTXEXmzYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82bcea17-1795-4549-9778-e33a85962dbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAEeDXyjKG44EpvFjsfsEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 617,
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

_source line 12 · 2026-05-28T01:29:51.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014tw8Cixvxp521KdLtyVP5W`</summary>

```json
{
  "query": "hardest math benchmarks LLM 2026 beyond AIME"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82bcea17-1795-4549-9778-e33a85962dbb",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6owMDPDNVTTXEXmzYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7feb18ae-c0d4-4abd-b99d-4b3d99e693fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAEeDXyjKG44EpvFjsfsEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 9032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 617,
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

_source line 13 · 2026-05-28T01:29:55.452Z_

<details><summary>↩ Tool result · `toolu_01DTf5tQACmV9GpqT4uBCk8f`</summary>

```text
Web search results for query: "Qwen3-235B AIME 2025 performance accuracy"

Links: [{"title":"Qwen3 235B — AI Model | MindStudio","url":"https://www.mindstudio.ai/models/qwen3-235b-a22b-deepinfra"},{"title":"Qwen AI Review 2025: Best Qwen Model for Coding | Qwen Coder Tested | Index.dev","url":"https://www.index.dev/blog/qwen-ai-coding-review"},{"title":"Qwen3 235B A22B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen3-235b-a22b"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen 3 (235B)","url":"https://www.vals.ai/models/fireworks_qwen3-235b-a22b"},{"title":"FriendliAI Achieves 3× Faster Qwen3 235B Inference Compared to vLLM Infrastructure","url":"https://friendli.ai/blog/Qwen3-235B-benchmark"},{"title":"Qwen3–235B-A22B review: Comaprison with Gemini-2.5-Pro and -Flash, DeepSeek R1 and O3 | by Barnacle Goose | Medium","url":"https://medium.com/@leucopsis/qwen3-235b-a22b-review-comaprison-with-gemini-2-5-pro-and-flash-deepseek-r1-and-o3-78c2b88b4e37"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"Qwen3-Max 2025 Complete Release Analysis: In-Depth Review of Alibaba's Most Powerful AI Model - DEV Community","url":"https://dev.to/czmilo/qwen3-max-2025-complete-release-analysis-in-depth-review-of-alibabas-most-powerful-ai-model-3j7l"}]

Based on the search results, here's the performance information for Qwen3-235B on AIME 2025:

## Qwen3-235B AIME 2025 Performance

The flagship model Qwen3-235B-A22B achieves 81.5 on AIME'25, which represents strong mathematical reasoning capabilities. 

There are two variants with different performance levels:

1. **Non-Thinking Mode**: The model achieves 70.3% on AIME25, demonstrating solid performance for rapid responses.

2. **Thinking Mode**: Qwen3-235B-A22B-Thinking scored 81.5 on AIME 2025, demonstrating exceptional mathematical reasoning capabilities.

The thinking mode variant enables the model to allocate more computational resources to complex mathematical reasoning tasks, resulting in the higher score compared to the non-thinking variant. Released on April 29, 2025, this model employs a Mixture-of-Experts (MoE) architecture to efficiently balance high-performance reasoning and rapid, low-latency inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17d319dd-4f71-4920-8f98-085c63ad1b70",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "5e807c77-3f00-4308-b51f-f2cd173840d2",
  "sourceToolAssistantUUID": "17d319dd-4f71-4920-8f98-085c63ad1b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T01:29:56.987Z_

<details><summary>↩ Tool result · `toolu_01J5YqrYq53DzzmrezaFuv2x`</summary>

```text
Web search results for query: "Qwen3 235B pass@1 AIME AMC competition math"

Links: [{"title":"Challenging the Boundaries of Reasoning: An Olympiad-Level Math Benchmark for Large Language Models","url":"https://arxiv.org/html/2503.21380v2"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning","url":"https://intuitionlabs.ai/pdfs/aime-2025-benchmark-an-analysis-of-ai-math-reasoning.pdf"},{"title":"AIME 2025 Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/aime-2025"},{"title":"AIME 2025 Leaderboard | Kaggle","url":"https://www.kaggle.com/benchmarks/open-benchmarks/aime-2025"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"AIME 2025 Benchmark Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/aime-2025"},{"title":"AIME Problems and Solutions - AoPS Wiki","url":"https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning | IntuitionLabs","url":"https://intuitionlabs.ai/articles/aime-2025-ai-benchmark-explained"}]

Based on the search results, here are the key findings about Qwen3-235B's performance on AIME:

## Qwen3-235B Pass@1 Scores

The flagship model Qwen3-235B-A22B achieves 85.7 on AIME'24 and 81.5 on AIME'25 in pass@1 (single attempt) scoring.

## Model Details

Qwen3-235B-A22B is an MoE (Mixture-of-Experts) model with a total of 235 billion parameters and 22 billion activated ones per token.

## Training Improvements

The AIME'24 score of the Qwen3-235B-A22B model increases from 70.1 to 85.1 over a total of 170 RL training steps, demonstrating significant improvements through reinforcement learning optimization.

## Performance Context

The post-trained models, whether in thinking or non-thinking mode, perform competitively against leading proprietary models and large mixture-of-experts (MoE) models such as o1, o3-mini, and DeepSeek-V3.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49b4d21a-7d36-4a8a-83ab-5739bdb59115",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "f5f70969-6f23-4dfe-a3d0-bd8fb716da1c",
  "sourceToolAssistantUUID": "49b4d21a-7d36-4a8a-83ab-5739bdb59115",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T01:29:58.095Z_

<details><summary>↩ Tool result · `toolu_01ERDCGq742yjoGzsNnHR3wa`</summary>

```text
Web search results for query: "Qwen3-235B-A22B math benchmark results"

Links: [{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen3-235B-A22B Sparse MoE Transformer","url":"https://www.emergentmind.com/topics/qwen3-235b-a22b"},{"title":"Qwen3-VL-235B-A22B-Thinking - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/qwen3-vl-235b-a22b-thinking"},{"title":"Qwen/Qwen3-235B-A22B-Thinking-2507 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 235B and 30B MoE Quant Benchmarking Roundup · GitHub","url":"https://gist.github.com/ubergarm/0f9663fd56fc181a00ec9f634635eb38"},{"title":"Qwen3-235B-A22B-Instruct-2507: Model Overview, Benchmarks, and Community Insights - DEV Community","url":"https://dev.to/czmilo/qwen3-235b-a22b-instruct-2507-model-overview-benchmarks-and-community-insights-56b8"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://arxiv.org/pdf/2504.18428"},{"title":"Qwen3-235B-A22B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/qwen3-235b-a22b"}]

Based on the search results, here are the key math benchmark results for the Qwen3-235B-A22B model:

## Overview
Qwen3-235B-A22B is a large model with 235 billion total parameters and 22 billion activated parameters, and it achieves competitive results in benchmark evaluations of coding, math, general capabilities, etc., when compared to other top-tier models such as DeepSeek-R1, o1, o3-mini, Grok-3, and Gemini-2.5-Pro.

## Specific Math Benchmark Results

**MATH Benchmark (Highest Difficulty):** For high-stakes mathematical reasoning (MATH benchmark, difficulty 5/5), Qwen3-235B-A22B as a standalone achieves 2.8% error at 126s mean latency per query.

**PolyMath Multilingual Evaluation:** Even Qwen3-235B-A22B-Thinking and Gemini-2.5-pro achieve only 54.6 and 52.2 benchmark scores, with about 40% accuracy under the highest level on the PolyMath benchmark.

**Comparative Performance:** With only 60% activated and 35% total parameters, Qwen3-235B-A22B (Thinking) outperforms DeepSeek-R1 on 17/23 the benchmarks, particularly on the reasoning-demanded tasks.

The model supports both thinking and non-thinking modes, with thinking mode helping significantly for logic/math/coding type questions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90386cdb-81f5-416b-9be9-8232f823b9ad",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "cdae7633-c84f-4acc-895d-496fa53952dc",
  "sourceToolAssistantUUID": "90386cdb-81f5-416b-9be9-8232f823b9ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T01:29:58.486Z_

<details><summary>↩ Tool result · `toolu_012LtppzkZ2A3gMnaAJujnWz`</summary>

```text
Web search results for query: "FrontierMath benchmark LLM performance 2026"

Links: [{"title":"FrontierMath Benchmark 2026: 4 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/frontierMath"},{"title":"Best LLM for math in 2026: how AI models rank - Bracai","url":"https://www.bracai.eu/post/llm-math-benchmark"},{"title":"FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI","url":"https://epoch.ai/frontiermath/tiers-1-4/about"},{"title":"LLM Evaluation in 2026. Frontier models now saturate the… | by Milind Nair | Mar, 2026 | Medium","url":"https://medium.com/@nairmilind3/llm-evaluation-in-2026-e631a78c67dc"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Forecasting Frontier Language Model Agent Capabilities","url":"https://arxiv.org/pdf/2502.15850"},{"title":"Benchmarking Political Persuasion Risks Across Frontier Large Language Models","url":"https://arxiv.org/pdf/2603.09884"}]

Based on the search results, here's what I found about FrontierMath benchmark LLM performance in 2026:

## Current Performance Rankings

As of May 27, 2026, GPT-5.5 Pro leads the FrontierMath leaderboard with 52.4%, followed by GPT-5.5 (51.7%) and GPT-5.4 Pro (50%). The top models are clustered within 2.4 points, suggesting this benchmark is nearing saturation for frontier models.

## About the Benchmark

FrontierMath is the hardest public math benchmark, consisting of 300 Tier 1-3 problems and 50 Tier 4 problems, all original and unpublished. It is an expert-level mathematical reasoning benchmark by Epoch AI featuring original, research-level problems created by mathematicians including IMO gold medalists and Fields Medal recipients, with problems requiring deep creativity and multi-step reasoning.

## Progress Over Time

Looking at historical context, FrontierMath Tier 1-3 (research-level mathematics) has increased from 1% to 41% between June 2024 and December 2025, showing substantial improvement as models have advanced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82bcea17-1795-4549-9778-e33a85962dbb",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "72331428-fd3b-41f2-bea5-ac178e0ce929",
  "sourceToolAssistantUUID": "82bcea17-1795-4549-9778-e33a85962dbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T01:29:59.752Z_

<details><summary>↩ Tool result · `toolu_014tw8Cixvxp521KdLtyVP5W`</summary>

```text
Web search results for query: "hardest math benchmarks LLM 2026 beyond AIME"

Links: [{"title":"Best LLM for Math 2026 - AI Model Benchmark Comparison","url":"https://pricepertoken.com/leaderboards/math"},{"title":"FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI","url":"https://epoch.ai/frontiermath"},{"title":"Math Benchmarks 2026: AIME, HMMT, MATH-500 LLM Scores | BenchLM.ai","url":"https://benchlm.ai/math"},{"title":"Best LLM for math in 2026: how AI models rank - Bracai","url":"https://www.bracai.eu/post/llm-math-benchmark"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"LLM Math Benchmarks 2025–2026: GSM8K, MATH, AIME, AMC | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm/math-benchmarks"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"LLM Evaluation Guide 2026: How to Benchmark & Compare Language Models","url":"https://jobsbyculture.com/blog/llm-evaluation-guide-2026"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"}]

Based on the search results, here are the hardest math benchmarks for LLMs in 2026 beyond AIME:

## FrontierMath

FrontierMath is an AI benchmark consisting of extremely challenging math problems, including open research problems that remain unsolved by mathematicians. It is designed to test reasoning closer to research mathematics, where problems require deep understanding and long chains of deduction. Created by Epoch AI with contributions from more than 60 professional mathematicians, including Fields Medalists, it was released in 2024 to evaluate whether AI systems can reason at the level of advanced mathematics rather than memorized knowledge. The benchmark includes multiple tiers of difficulty, ranging from advanced undergraduate math to PhD-level and research-level problems.

## Humanity's Last Exam (HLE)

HLE includes math problems even harder than AIME, with frontier models scoring below 40%. HLE consists of 2,500 expert-level questions contributed by domain specialists in mathematics, science, law, and other fields. Questions were designed to be beyond the reach of AI systems in 2024.

## BRUMO and MATH-500

BRUMO and MATH-500 show meaningful separation, while AIME and HMMT are effectively solved by AI and no longer factor into the weighted score. MATH-500 tests competition-level mathematical reasoning across 500 problems drawn from AMC, AIME, and similar competitions. Unlike GSM8K, MATH-500 problems require multi-step symbolic reasoning.

These benchmarks represent the current frontier of mathematical reasoning evaluation for LLMs in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7feb18ae-c0d4-4abd-b99d-4b3d99e693fd",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "3323f5cf-dde9-4be7-afca-721cb8044651",
  "sourceToolAssistantUUID": "7feb18ae-c0d4-4abd-b99d-4b3d99e693fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-28T01:30:05.845Z_

Let me search for more specific data on which AIME problems are hardest and IMO-level performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3323f5cf-dde9-4be7-afca-721cb8044651",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6poFaYVgqYnLhtXsQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "180853be-8748-421c-886a-fde1d4349207",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeSRQEp99YLiwKCGtbQvvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4614,
      "cache_read_input_tokens": 9649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4614,
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

_source line 19 · 2026-05-28T01:30:06.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UAg7KBJ3AwimHGQHWJTqDo`</summary>

```json
{
  "query": "AIME 2025 hardest problems LLM fail problem 13 14 15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "180853be-8748-421c-886a-fde1d4349207",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6poFaYVgqYnLhtXsQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae6eefea-3b5b-4b84-becc-99ce99866725",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeSRQEp99YLiwKCGtbQvvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4614,
      "cache_read_input_tokens": 9649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4614,
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

_source line 20 · 2026-05-28T01:30:06.764Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LUNGRmia4X4GseDEtygCTJ`</summary>

```json
{
  "query": "IMO 2025 LLM performance AI math olympiad"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae6eefea-3b5b-4b84-becc-99ce99866725",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6poFaYVgqYnLhtXsQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad6ac9a9-dff5-463d-848b-999485483395",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeSRQEp99YLiwKCGtbQvvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4614,
      "cache_read_input_tokens": 9649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4614,
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

_source line 21 · 2026-05-28T01:30:07.356Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YHmgsWZ7kMBVEVEMkSX16L`</summary>

```json
{
  "query": "FrontierMath Tier 4 scores 2026 LLM performance percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6ac9a9-dff5-463d-848b-999485483395",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6poFaYVgqYnLhtXsQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89ba7b34-e698-4bde-8167-6f759eaccdfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeSRQEp99YLiwKCGtbQvvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4614,
      "cache_read_input_tokens": 9649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4614,
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

_source line 22 · 2026-05-28T01:30:12.177Z_

<details><summary>↩ Tool result · `toolu_01UAg7KBJ3AwimHGQHWJTqDo`</summary>

```text
Web search results for query: "AIME 2025 hardest problems LLM fail problem 13 14 15"

Links: [{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning | IntuitionLabs","url":"https://intuitionlabs.ai/articles/aime-2025-ai-benchmark-explained"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning","url":"https://intuitionlabs.ai/pdfs/aime-2025-benchmark-an-analysis-of-ai-math-reasoning.pdf"},{"title":"AIME 2025 Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/aime-2025"},{"title":"LLMs haven’t solved the hardest problems on math contests | Epoch AI","url":"https://epoch.ai/data-insights/math-competitions"},{"title":"AIME 2025 Benchmark Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/aime-2025"},{"title":"Challenging the Boundaries of Reasoning: An Olympiad-Level Math Benchmark for Large Language Models","url":"https://arxiv.org/html/2503.21380v2"},{"title":"AIME Benchmarks: Math & AI Evaluation","url":"https://www.emergentmind.com/topics/aime-benchmarks"},{"title":"AIME 2024 and AIME 2025 Benchmarks","url":"https://www.emergentmind.com/topics/aime-2024-and-aime-2025-benchmarks"},{"title":"Top 50 AI Model Benchmarks & Evaluation Metrics (2025 Guide)","url":"https://o-mega.ai/articles/top-50-ai-model-evals-full-list-of-benchmarks-october-2025"},{"title":"AI Did Well on the 2025 AIME - by Greg Burnham - Lemmata","url":"https://lemmata.substack.com/p/ai-did-well-on-the-2025-aime"}]

Based on the search results, here's what I found about AIME 2025's hardest problems and LLM performance:

## Difficulty of Problems 13-15

The hardest AIME 2025 problems (#14–15) correspond to an Art of Problem Solving difficulty rating of 6, making them exceptionally challenging.

## LLM Performance on the Hardest Problems

At the end of the test where the AI models struggle, o3-mini-high and o1 both get Problem 13 some of the time, but neither gets Problems 14 or 15 at all.

Publicly available models achieve >95% on problems up to a rating of 5, but these models have not fully saturated problems rated 6-7, though GPT-5 achieves >67%.

## Context on Problem 13

The analysis suggests the solution to one of these problems revolves around the fact that the number of regions that a set of chords divides a disk is the number of interior chord-chord intersection points, plus the number of chords, plus 1, reducing the problem to finding the expected number of intersections between every pair of chords.

The results demonstrate that while LLMs have made impressive progress on AIME 2025, the hardest problems—particularly 14 and 15—remain a significant challenge, with most models unable to solve them reliably.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae6eefea-3b5b-4b84-becc-99ce99866725",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "af156d07-b18d-4a81-9ccb-49644042372f",
  "sourceToolAssistantUUID": "ae6eefea-3b5b-4b84-becc-99ce99866725",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T01:30:12.255Z_

<details><summary>↩ Tool result · `toolu_01YHmgsWZ7kMBVEVEMkSX16L`</summary>

```text
Web search results for query: "FrontierMath Tier 4 scores 2026 LLM performance percentage"

Links: [{"title":"FrontierMath Benchmark 2026: 4 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/frontierMath"},{"title":"What will be the best FrontierMath Tier 4 score by Dec 31, 2026? | Manifold","url":"https://manifold.markets/Bayesian/what-will-be-the-best-frontiermath"},{"title":"FrontierMath Tier 4 | Epoch AI","url":"https://epoch.ai/benchmarks/frontiermath-tier-4"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"Share of FrontierMath problems solved correctly by AI models - Our World in Data","url":"https://ourworldindata.org/grapher/ai-frontiermath-over-time"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI","url":"https://epoch.ai/frontiermath"},{"title":"Forecasting Frontier Language Model Agent Capabilities","url":"https://arxiv.org/pdf/2502.15850"}]

Based on the search results, here's what I found about FrontierMath Tier 4 scores:

As of May 27, 2026, GPT-5.5 Pro leads the FrontierMath leaderboard with 52.4%, followed by GPT-5.5 (51.7%) and GPT-5.4 Pro (50%).

FrontierMath consists of 300 Tier 1-3 problems and 50 Tier 4 problems, all original and unpublished. Difficulty Tiers 1-3 cover undergraduate problems through exploratory problems suitable for an advanced graduate student, while Tier 4 is research-level mathematics.

Note that the search results show overall FrontierMath scores rather than Tier 4-specific scores. The leaderboard data appears to represent performance across all problem tiers combined.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89ba7b34-e698-4bde-8167-6f759eaccdfb",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "bda1db68-681c-46ba-908b-b8550f35727f",
  "sourceToolAssistantUUID": "89ba7b34-e698-4bde-8167-6f759eaccdfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T01:30:13.485Z_

<details><summary>↩ Tool result · `toolu_01LUNGRmia4X4GseDEtygCTJ`</summary>

```text
Web search results for query: "IMO 2025 LLM performance AI math olympiad"

Links: [{"title":"OpenAI LLM Achieves Breakthrough at 2025 International Math Olympiad","url":"https://www.thinkwithniche.com/blogs/news/openai-llm-achieves-breakthrough-at-2025-international-math-olympiad"},{"title":"OpenAI’s gold medal performance on the International Math Olympiad","url":"https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/"},{"title":"OpenAI on X: \"We achieved gold medal-level performance 🥇on the 2025 International Mathematical Olympiad with a general-purpose reasoning LLM! Our model solved world-class math problems—at the level of top human contestants. A major milestone for AI and mathematics.\" / X","url":"https://x.com/OpenAI/status/1946594928945148246"},{"title":"From Benchmarks to Gold: How LLMs Cracked IMO 2025 and What Comes Next for Math AI | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises","url":"https://www.apolo.us/blog-posts/from-benchmarks-to-gold-how-llms-cracked-imo-2025-and-what-comes-next-for-math-ai"},{"title":"AI Reasoning: Gold-Medal Performance at the 2025 IMO | IntuitionLabs","url":"https://intuitionlabs.ai/articles/ai-reasoning-math-olympiad-imo"},{"title":"OpenAI's Experimental AI Achieves Gold Medal at 2025 ...","url":"https://mlq.ai/news/openais-experimental-ai-achieves-gold-medal-at-2025-international-math-olympiad/"},{"title":"2025 International Mathematical Olympiad results – Maths Society","url":"https://math-soc.com/2025/07/22/2025-international-mathematical-olympiad-results-are-in/"},{"title":"Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad","url":"https://arxiv.org/pdf/2503.21934"},{"title":"MathArena - IMO Blogpost","url":"https://matharena.ai/imo/"}]

Based on the search results, here's what happened with LLM performance at the 2025 International Math Olympiad:

## Key Achievement

An experimental large language model developed by OpenAI demonstrated gold medal-level performance in the 2025 International Math Olympiad. The model successfully tackled five out of six challenging problems, achieving a score of 35 out of 42.

## Testing Conditions

The models were evaluated on the 2025 IMO problems under the same rules as human contestants: two 4.5 hour exam sessions, no tools or internet, reading the official problem statements, and writing natural language proofs. Three former IMO medalists independently graded the model's submitted proof, with scores finalized after unanimous consensus.

## Competitive Performance

AI models from OpenAI and DeepMind achieved gold-medal level performance, solving 5 out of 6 challenging math problems. Each model scored 35/42, matching the gold medal threshold and outperforming over 90% of human participants.

## Significance

This achievement represents significant progress in AI reasoning. The breakthrough was achieved through general-purpose reinforcement learning and test-time compute scaling, rather than narrow, task-specific methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad6ac9a9-dff5-463d-848b-999485483395",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "54b39e7d-8a66-4b81-91be-60ca1ad1436e",
  "sourceToolAssistantUUID": "ad6ac9a9-dff5-463d-848b-999485483395",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T01:30:15.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TxXAdy6qdeYEFi5sMw3rkt`</summary>

```json
{
  "query": "FrontierMath Tier 4 research-level scores best model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54b39e7d-8a66-4b81-91be-60ca1ad1436e",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6qoz1SLZ6W2eP62Dyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3993f326-8e90-405f-b5a1-b84d656a71e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PdfcZhqMe2bdcFvrsGLiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 1964,
      "cache_read_input_tokens": 14263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 26 · 2026-05-28T01:30:16.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BdkjaBCuoY58ayQWitB7f3`</summary>

```json
{
  "query": "\"Qwen3-235B\" AIME problem-by-problem which problems fails"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3993f326-8e90-405f-b5a1-b84d656a71e5",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6qoz1SLZ6W2eP62Dyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "351191bc-2cc3-4706-b79a-615501d5a92a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PdfcZhqMe2bdcFvrsGLiec",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 1964,
      "cache_read_input_tokens": 14263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 27 · 2026-05-28T01:30:21.292Z_

<details><summary>↩ Tool result · `toolu_01TxXAdy6qdeYEFi5sMw3rkt`</summary>

```text
Web search results for query: "FrontierMath Tier 4 research-level scores best model 2026"

Links: [{"title":"What will be the best FrontierMath Tier 4 score by Dec 31, 2026? | Manifold","url":"https://manifold.markets/Bayesian/what-will-be-the-best-frontiermath"},{"title":"FrontierMath Tier 4 | Epoch AI","url":"https://epoch.ai/benchmarks/frontiermath-tier-4"},{"title":"FrontierMath Benchmark 2026: 4 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/frontierMath"},{"title":"Share of FrontierMath problems solved correctly by AI models - Our World in Data","url":"https://ourworldindata.org/grapher/ai-frontiermath-over-time"},{"title":"AI Math Benchmarks: AI's Growing Capabilities - IEEE Spectrum","url":"https://spectrum.ieee.org/ai-math-benchmarks"},{"title":"FrontierMath: Tiers 1-4","url":"https://epoch.ai/frontiermath/tiers-1-4"},{"title":"FrontierMath benchmark shows AI struggling with advanced mathematics / AI World","url":"https://aiworld.eu/story/frontiermath-benchmark-shows-ai-struggling-with-advanced-mathematics"},{"title":"FrontierMath Tier 4: Battle Royale - Epoch AI","url":"https://epochai.substack.com/p/frontiermath-tier-4-battle-royale"},{"title":"FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI","url":"https://epoch.ai/frontiermath"},{"title":"FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI","url":"https://arxiv.org/pdf/2411.04872"}]

Based on the search results, here are the current FrontierMath Tier 4 research-level scores for 2026:

As of May 27, 2026, GPT-5.5 Pro leads the FrontierMath leaderboard with 52.4%, followed by GPT-5.5 (51.7%) and GPT-5.4 Pro (50%).

It's important to note that Tier 4 is research-level mathematics, and FrontierMath Tier 4 consists of 50 research-level math problems developed by professional mathematicians. These problems can take experts weeks to solve.

Additionally, as of May 11, 2026, Epoch AI is conducting an AI-assisted review of FrontierMath: Tiers 1-4 which has flagged fatal errors in about a third of problems, and they will release updated scores on a corrected dataset after completing a thorough human review. This suggests that the current scores may be subject to revision once the review process is complete.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3993f326-8e90-405f-b5a1-b84d656a71e5",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "ec5895df-0e13-413c-b527-d828e976b678",
  "sourceToolAssistantUUID": "3993f326-8e90-405f-b5a1-b84d656a71e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T01:30:22.137Z_

<details><summary>↩ Tool result · `toolu_01BdkjaBCuoY58ayQWitB7f3`</summary>

```text
Web search results for query: ""Qwen3-235B" AIME problem-by-problem which problems fails"

Links: [{"title":"Qwen/Qwen3-235B-A22B · Does anyone feel Qwen3 often fails to follow instructions accurately?","url":"https://huggingface.co/Qwen/Qwen3-235B-A22B/discussions/18"},{"title":"[Bug] Qwen3-235B FP8 stops responding after a certain number of requests · Issue #1423 · QwenLM/Qwen3","url":"https://github.com/QwenLM/Qwen3/issues/1423"},{"title":"Qwen/Qwen3-235B-A22B-Instruct-2507 · An interesting phenomenon","url":"https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507/discussions/18"},{"title":"[Bug]: Bedrock qwen.qwen3-vl-235b-a22b not working · Issue #17471 · BerriAI/litellm","url":"https://github.com/BerriAI/litellm/issues/17471"},{"title":"[Bug]: qwen3-235b-a22b-instruct-2507 fails on multi-node deployment · Issue #26899 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26899"},{"title":"Qwen/Qwen3-235B-A22B · Qwen3 not Using Tools in Complex Prompts Unlike QwQ-32B","url":"https://huggingface.co/Qwen/Qwen3-235B-A22B/discussions/20"},{"title":"Qwen: Qwen3 235B A22B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/qwen-qwen3-235b-a22b/"},{"title":"Qwen3 Complete Guide: Every Model from 0.6B to 235B | InsiderLLM","url":"https://insiderllm.com/guides/qwen3-complete-guide/"}]

Based on the search results, I found some information about Qwen3-235B's performance on AIME problems, though not a detailed problem-by-problem breakdown of failures.

According to benchmark data, Qwen3-235B-A22B achieves 84% on AIME and 82% on AIME 2025 competition mathematics. Additionally, Qwen3-235B-A22B beats DeepSeek-R1 and o1 on both AIME math benchmarks.

However, the search results don't contain a detailed problem-by-problem analysis of which specific AIME problems the model fails on. The results do mention some general performance observations about Qwen3-235B, such as occasional instruction-following challenges in certain contexts, but there's no specific breakdown of individual AIME problem failures.

To find the detailed problem-by-problem analysis you're looking for, you might want to check:
- Official Qwen model benchmarking reports
- Research papers or technical blogs evaluating Qwen3's mathematical reasoning
- Model evaluation repositories on GitHub or Hugging Face that may contain granular performance metrics

Would you like me to search for more specific information about this?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "351191bc-2cc3-4706-b79a-615501d5a92a",
  "isSidechain": true,
  "promptId": "4e94adbc-9607-4d33-8f79-8d296106864a",
  "agentId": "ad90108251e21a4c4",
  "type": "user",
  "uuid": "4f3b581e-eda0-4bb7-8105-cf86a9b221ce",
  "sourceToolAssistantUUID": "351191bc-2cc3-4706-b79a-615501d5a92a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T01:30:55.299Z_

Here is the detailed research report:

---

## Qwen3-235B-A22B Math Performance and "Frontier-Hard" Benchmarks

**AIME 2025 Performance -- the 81.5% claim is confirmed.** The Qwen3 Technical Report and multiple leaderboards confirm that Qwen3-235B-A22B in thinking mode achieves **81.5% on AIME 2025** (pass@1), and 85.7% on AIME 2024. In non-thinking mode, it drops to ~70.3% on AIME 2025. This places it competitively with DeepSeek-R1 and o1, though below the very top models.

**Which AIME problems does it fail on?** No problem-by-problem breakdown for Qwen3 specifically was found, but analysis from Epoch AI and IntuitionLabs shows a consistent pattern across frontier models: problems #1-12 (difficulty ratings ~3-5) are solved >95% of the time, while **problems #13-15 (difficulty rating 6-7) remain the real discriminators**. On AIME 2025, even o3-mini-high and o1 could only solve Problem 13 intermittently, and **neither could solve Problems 14 or 15 at all**. At 81.5% (roughly 24.5/30 across both AIME I and II), Qwen3 likely fails on approximately 5-6 of the hardest problems per year -- essentially the last 2-3 problems on each exam.

**How many AIME problems per year are actually hard?** Out of 30 total problems (15 per exam x 2), approximately **4-6 problems (the #13-15 slots on each exam)** remain genuinely difficult for frontier models. The first 10-12 problems on each exam are effectively saturated.

**What is genuinely "frontier-hard" (pass@1 < 10%)?**

- **FrontierMath Tier 4** (research-level math, 50 problems by professional mathematicians including Fields Medalists): The best model as of May 2026 is GPT-5.5 Pro at 52.4% overall across all tiers, but Tier 4 specifically remains much harder. Notably, Epoch AI flagged fatal errors in ~1/3 of problems during review, so scores are in flux. When FrontierMath launched in 2024, all models scored <2%. By late 2025, the best hit ~41% on Tiers 1-3 combined.

- **IMO 2025**: OpenAI's experimental model and DeepMind's system both achieved gold-medal performance (35/42, solving 5 of 6 problems). This is remarkable but used specialized test-time compute. Standard models perform much worse on proof-based olympiad problems.

- **Humanity's Last Exam (HLE)**: 2,500 expert-level problems across domains; frontier models score below 40%.

- **PolyMath**: Even Qwen3-235B-A22B-Thinking and Gemini-2.5-Pro achieve only ~54.6 and ~52.2 respectively, with ~40% accuracy on the hardest tier.

**Bottom line:** AIME is no longer a frontier-hard benchmark -- it is a mid-tier discriminator where the best models score 80-90%+. The genuinely frontier-hard benchmarks where models still struggle significantly are FrontierMath Tier 4, HLE, and proof-based olympiad problems (IMO/USAMO) when evaluated without specialized infrastructure. The reviewer's 81.5% claim for Qwen3-235B-A22B on AIME 2025 is accurate.

Sources:
- [Qwen3 Technical Report (arXiv)](https://arxiv.org/html/2505.09388v1)
- [Qwen3 Blog Post](https://qwenlm.github.io/blog/qwen3/)
- [AIME 2025 Benchmark: An Analysis of AI Math Reasoning (IntuitionLabs)](https://intuitionlabs.ai/articles/aime-2025-ai-benchmark-explained)
- [AIME 2025 Benchmark Leaderboard (llm-stats.com)](https://llm-stats.com/benchmarks/aime-2025)
- [AIME 2025 Benchmark Leaderboard (Artificial Analysis)](https://artificialanalysis.ai/evaluations/aime-2025)
- [LLMs haven't solved the hardest problems on math contests (Epoch AI)](https://epoch.ai/data-insights/math-competitions)
- [FrontierMath Benchmark 2026 (BenchLM)](https://benchlm.ai/benchmarks/frontierMath)
- [FrontierMath Tier 4 (Epoch AI)](https://epoch.ai/benchmarks/frontiermath-tier-4)
- [FrontierMath: Tiers 1-4 (Epoch AI)](https://epoch.ai/frontiermath/tiers-1-4)
- [OpenAI IMO 2025 Gold Medal Performance](https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/)
- [AI Reasoning: Gold-Medal Performance at the 2025 IMO (IntuitionLabs)](https://intuitionlabs.ai/articles/ai-reasoning-math-olympiad-imo)
- [Math Benchmarks 2026 (BenchLM)](https://benchlm.ai/math)
- [Best LLM for math in 2026 (Bracai)](https://www.bracai.eu/post/llm-math-benchmark)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f3b581e-eda0-4bb7-8105-cf86a9b221ce",
  "isSidechain": true,
  "agentId": "ad90108251e21a4c4",
  "requestId": "req_011CbU6rSvWk1KZ2AnWakxyx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5fa48ef-95d1-4325-97f7-adbeba90e7d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0651b19d-8e69-4364-8745-be64fdf1cee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2gPi2tR969jN6KyD2t441",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2382,
      "cache_read_input_tokens": 16227,
      "output_tokens": 1386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1386,
          "cache_read_input_tokens": 16227,
          "cache_creation_input_tokens": 2382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2382,
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
