# Research conversation: You are helping with a literature survey on adaptive verification strategies for LLM inference. Use WebSearch and WebFet

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 96
- **Recorded user turns:** 1
- **Tool calls:** 42
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a042bbe02a929caec.jsonl`
- **Structured JSON:** [`cc31de0c3b49dd21660c.json`](../../sessions/cc/cc31de0c3b49dd21660c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

96 recorded events

### User

_source line 1 · 2026-05-28T10:16:12.584Z_

You are helping with a literature survey on adaptive verification strategies for LLM inference. Use WebSearch and WebFetch to find important papers (2024-2026) on:

1. Search: "process reward model PRM outcome reward model ORM 2024 2025 2026 LLM"
2. Search: "generative reward model GenRM verification LLM 2025"
3. Search: "best-of-N sampling reward model scaling 2024 2025"
4. Search: "self-consistency majority voting LLM reasoning 2024 2025"
5. Search: "verifier LLM math reasoning 2024 2025 NeurIPS ICML ICLR"
6. Search: "process reward model step-level verification 2025"
7. Search: "reward model verification granularity 2025"

For each important paper found, use WebFetch on the arXiv page to read its abstract. Focus on papers that:
- Were published at top venues (NeurIPS, ICML, ICLR, AAAI, ACL, EMNLP) or are highly cited
- Won awards or were oral/spotlight presentations
- Introduced widely-adopted methods for verification/reward modeling in LLM reasoning

Report for each paper: full title, authors (first author et al.), venue, URL, why it's important, and a one-line summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "893b727a-f237-4393-8145-1b8ef5049cf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T10:16:12.591Z_

```json
{
  "parentUuid": "893b727a-f237-4393-8145-1b8ef5049cf6",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
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
  "uuid": "60668e75-2c4d-4fb2-927b-45140936bfde",
  "timestamp": "2026-05-28T10:16:12.591Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T10:16:12.592Z_

```json
{
  "parentUuid": "60668e75-2c4d-4fb2-927b-45140936bfde",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c8c7db7b-b919-475f-9e88-5f19c4855329",
  "timestamp": "2026-05-28T10:16:12.592Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T10:16:15.302Z_



I'll conduct a comprehensive literature survey on adaptive verification strategies for LLM inference. Let me start by loading the WebSearch and WebFetch tools, then run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8c7db7b-b919-475f-9e88-5f19c4855329",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxAfHjMBhBJQUA9yz4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c83b16da-65e0-4d30-83d7-35b323a604e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eFXUcLL7Mi2iGNg4oCk92",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1630,
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

_source line 5 · 2026-05-28T10:16:15.594Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DEPBzjNJRinvijVyDKEUGE`</summary>

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
  "parentUuid": "c83b16da-65e0-4d30-83d7-35b323a604e0",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxAfHjMBhBJQUA9yz4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a55cf399-7f45-4f52-826c-3bd93b9bf2d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eFXUcLL7Mi2iGNg4oCk92",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 7407,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1630
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1630,
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

_source line 6 · 2026-05-28T10:16:15.598Z_

<details><summary>↩ Tool result · `toolu_01DEPBzjNJRinvijVyDKEUGE`</summary>

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
  "parentUuid": "a55cf399-7f45-4f52-826c-3bd93b9bf2d0",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "e1b55144-f047-4900-849e-76b341838b86",
  "sourceToolAssistantUUID": "a55cf399-7f45-4f52-826c-3bd93b9bf2d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T10:16:18.233Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1b55144-f047-4900-849e-76b341838b86",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c945d5fd-fea7-4361-9ca2-61da3e85d66d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 8 · 2026-05-28T10:16:21.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DRoq6PCpcPb4LZZkpTH3Wi`</summary>

```json
{
  "query": "process reward model PRM outcome reward model ORM 2024 2025 2026 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c945d5fd-fea7-4361-9ca2-61da3e85d66d",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77389084-6ff9-4ddb-b235-b6c5ad6fda68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 9 · 2026-05-28T10:16:22.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AVxwUV6yuHBgyLdWM6VA7f`</summary>

```json
{
  "query": "generative reward model GenRM verification LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77389084-6ff9-4ddb-b235-b6c5ad6fda68",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "496eeb05-977a-4c64-a02f-c157027eef97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 10 · 2026-05-28T10:16:22.125Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D7K7kusH28pEp2aFJ68Wko`</summary>

```json
{
  "query": "best-of-N sampling reward model scaling 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "496eeb05-977a-4c64-a02f-c157027eef97",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49b57609-eb0f-4e80-bc90-d6b08cac9dbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 11 · 2026-05-28T10:16:22.153Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tX5L4xGcY444jvCidKq3S`</summary>

```json
{
  "query": "self-consistency majority voting LLM reasoning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49b57609-eb0f-4e80-bc90-d6b08cac9dbb",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4039a99f-7cb7-4c8c-aa0f-937003ef026b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 12 · 2026-05-28T10:16:22.520Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMuxAfiD6YP5k5dg8wiYbV`</summary>

```json
{
  "query": "verifier LLM math reasoning 2024 2025 NeurIPS ICML ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4039a99f-7cb7-4c8c-aa0f-937003ef026b",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f76dd0e-d6ce-4610-96c9-01086d6b4a53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 13 · 2026-05-28T10:16:22.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DHjaK4DsheAC2c8YDHkNne`</summary>

```json
{
  "query": "process reward model step-level verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f76dd0e-d6ce-4610-96c9-01086d6b4a53",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b312d51d-0c7a-437a-8579-7c0d50f35d07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 14 · 2026-05-28T10:16:22.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A9kCyKFmFNzzc4mW26EaAs`</summary>

```json
{
  "query": "reward model verification granularity 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b312d51d-0c7a-437a-8579-7c0d50f35d07",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnxPjM98HUuwP4x8RQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e77fe37-2220-4406-8803-032ec5acaeb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCbuonGLMfNCyCDXa1K2it",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 15 · 2026-05-28T10:16:29.888Z_

<details><summary>↩ Tool result · `toolu_01AVxwUV6yuHBgyLdWM6VA7f`</summary>

```text
Web search results for query: "generative reward model GenRM verification LLM 2025"

Links: [{"title":"Generative Reward Models","url":"https://www.emergentmind.com/topics/generative-reward-models-genrm"},{"title":"Published as a conference paper at ICLR 2025 GENERATIVE VERIFIERS:","url":"https://openreview.net/attachment?id=Ccwp4tFEtE&name=pdf"},{"title":"P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling","url":"https://arxiv.org/html/2602.12116"},{"title":"[2408.15240] Generative Verifiers: Reward Modeling as Next-Token Prediction","url":"https://arxiv.org/abs/2408.15240"},{"title":"Generative Verifiers: Reward Modeling as Next-Token Prediction","url":"https://arxiv.org/pdf/2408.15240"},{"title":"Generative Verifiers: Reward Modeling as Next-Token Prediction","url":"https://arxiv.org/html/2408.15240"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via   Generative Reasoning","url":"https://arxiv.org/pdf/2504.00891"}]

Based on the search results, here's what I found about Generative Reward Models (GenRM) and verification in LLMs:

## Overview

A Generative Reward Model (GenRM) is a paradigm for reward modeling in which the evaluation or verification of model outputs is framed as a next-token prediction or text generation task, as opposed to traditional scalar-valued, discriminative classification.

## Key Features

GenRMs natively leverage the text generation capabilities of LLMs, integrating verification and solution generation into a unified architecture. This allows seamless adoption of instruction tuning, enables the use of chain-of-thought (CoT) reasoning during verification, and naturally supports scaling with both model size and inference-time compute.

## Performance Advantages

GenRM outperforms discriminative, DPO verifiers, and LLM-as-a-Judge, resulting in large performance gains with Best-of-N, namely 5% → 45.3% on algorithmic tasks and 73% → 93.4% on GSM8K. In easy-to-hard generalization settings, improvements of 28% → 44.6% on MATH, and 37.9% → 53.5% on MMLU abstract algebra are observed.

## Scalability

GenRM's next-token generative verification and CoT allow it to identify subtle errors—e.g., unit mismatches, minor arithmetic flaws—that discriminative models fail to capture. These advantages are amplified as model capacity increases and additional test-time computation is invested in verification majority voting.

The research on GenRM has been published and is actively advancing in 2025, with recent publications at ICLR 2025 and continued development in personalized variants and process-level reward models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "496eeb05-977a-4c64-a02f-c157027eef97",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "7665a872-231b-4955-893e-339a62e6fdce",
  "sourceToolAssistantUUID": "496eeb05-977a-4c64-a02f-c157027eef97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T10:16:30.461Z_

<details><summary>↩ Tool result · `toolu_01AMuxAfiD6YP5k5dg8wiYbV`</summary>

```text
Web search results for query: "verifier LLM math reasoning 2024 2025 NeurIPS ICML ICLR"

Links: [{"title":"Improving LLM Reasoning through Scaling Inference Computation with   Collaborative Verification","url":"https://arxiv.org/pdf/2410.05318"},{"title":"Right Is Not Enough: The Pitfalls of Outcome Supervision in Training LLMs for Math Reasoning","url":"https://arxiv.org/pdf/2506.06877"},{"title":"Not All Votes Count! Programs as Verifiers Improve Self-Consistency of   Language Models for Math Reasoning","url":"https://arxiv.org/pdf/2410.12608"},{"title":"GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models","url":"https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Breaking the Reasoning Barrier A Survey on LLM Complex ...","url":"https://aclanthology.org/2025.findings-acl.386.pdf"},{"title":"DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.22570"}]

Here are the search results for verifier LLM math reasoning research from 2024-2025 across NeurIPS, ICML, and ICLR:

## Key Papers and Research

**Math Verification Approaches:**

Math-Rev and Code-Rev verifiers demonstrate substantial performance gains on benchmarks such as GSM8k and MATH, even outperforming GPT-4 with Qwen-72B-Instruct as the reasoner. Reference-free preference tuning methods, such as SimPO, are the most effective for training verifiers.

PROVE consistently outperforms vanilla majority voting for mathematical reasoning tasks, increasing accuracy on the GSM8K benchmark from 48.85% to 53.83% for Qwen2-0.5B-Instruct and from 41.32% to 59.51% for Llama-2-7B-chat.

**Recent Challenges:**

The reliance on outcome-based rewards for training verifiers, such as Heimdall, is challenged by research showing this supervision masks underlying reasoning flaws. ParaStepVerifier focuses on definitively establishing the binary correctness of each reasoning step.

**Advanced Models:**

DeepSeekMath-V2 demonstrates strong theorem-proving capabilities, achieving gold-level scores on IMO 2025 and CMO 2024 and a near-perfect 118/120 on Putnam 2024 with scaled test-time compute.

The search results also indicate various papers accepted at ICLR 2024-2025, NeurIPS 2024-2025, and ICML 2024-2025 covering theorem proving, autoformalization, and verifiable reasoning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f76dd0e-d6ce-4610-96c9-01086d6b4a53",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "efb23988-1829-4300-a694-aab42ff1b169",
  "sourceToolAssistantUUID": "5f76dd0e-d6ce-4610-96c9-01086d6b4a53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T10:16:30.464Z_

<details><summary>↩ Tool result · `toolu_015tX5L4xGcY444jvCidKq3S`</summary>

```text
Web search results for query: "self-consistency majority voting LLM reasoning 2024 2025"

Links: [{"title":"Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/html/2505.10772v1"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Preprint, 2025 CAN LARGE REASONING MODELS SELF-TRAIN? Sheikh Shafayat1∗","url":"https://arxiv.org/pdf/2505.21444"},{"title":"Deep Think with Confidence DEEP THINK WITH CONFIDENCE","url":"https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf"},{"title":"TEMPORAL CONSISTENCY FOR LLM REASONING PRO","url":"https://openreview.net/pdf?id=sM5QDzIg3j"},{"title":"Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://openreview.net/pdf/16a8e329f46c67615bd64619a54566fcfc6430a5.pdf"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://aclanthology.org/2025.findings-acl.744.pdf"},{"title":"Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/pdf/2505.10772"}]

Based on the search results, here's what I found about self-consistency majority voting for LLM reasoning in 2024-2025:

## Recent Developments

Self-consistency, proposed by Wang et al. (2023), is a decoding method that improves the accuracy of LLMs by taking the majority vote of multiple reasoning paths. This foundational technique has inspired several recent advances.

### Advanced Approaches (2024-2025)

Ranked voting based self-consistency has been introduced to enhance reasoning performance of large language models, outperforming traditional majority voting techniques by generating and incorporating ranking information among multiple candidate answers.

Self-Consistency Preference Optimization (ScPO) trains models to prefer consistent answers robust under self-consistency voting, enabling unsupervised alignment without gold labels and closes the gap to supervised preference training on GSM8K and MATH.

### Limitations and Improvements

Majority voting often fails when errors are identified by only a minority of LLMs. To address this, Multi-Agent Consensus Alignment (MACA) uses ensembles of models participating in debate with gains that can exceed +27.6 percentage points on GSM8K and +23.7 pp on MATH.

### Self-Training Applications

Majority voting and self-consistency have been used to filter chain-of-thought traces that, when used as SFT training data, improve LLM performance on downstream tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4039a99f-7cb7-4c8c-aa0f-937003ef026b",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "8ca5aefb-bc19-45d1-9c62-fed6637e48fc",
  "sourceToolAssistantUUID": "4039a99f-7cb7-4c8c-aa0f-937003ef026b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T10:16:30.591Z_

<details><summary>↩ Tool result · `toolu_01A9kCyKFmFNzzc4mW26EaAs`</summary>

```text
Web search results for query: "reward model verification granularity 2025"

Links: [{"title":"arXiv:2505.11730v1 [cs.AI] 16 May 2025","url":"https://arxiv.org/pdf/2505.11730"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Reward Model Interpretability via Optimal and Pessimal Tokens | Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency","url":"https://dl.acm.org/doi/full/10.1145/3715275.3732068"},{"title":"General Reward Model: Methods & Applications","url":"https://www.emergentmind.com/topics/general-reward-model-grm"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://arxiv.org/pdf/2602.09305"}]

Based on the search results, here's what recent research shows about reward model verification granularity in 2025:

## Verification Granularity Classification

Existing approaches can be broadly classified into two categories: (i) outcome verification and (ii) process verification. Outcome verification evaluates the entire response after the generation of a complete sample. In contrast, process verification, often implemented as a process reward model (PRM), evaluates intermediate reasoning steps during generation.

## Process-Level Granularities

Within process verification, there are multiple levels of granularity being explored. Common granularities of PRMs include step-level and token-level supervision, with step-level PRMs assigning rewards to discrete reasoning steps, while token-level PRMs operate at a finer granularity, assigning rewards to individual tokens.

## Recent Advances in 2025

Recent work in 2025 has introduced several innovations for handling verification granularity:

- Partial-sequence evaluation via process reward models resolves granularity mismatch in inference-time alignment, enabling more stable and preference-consistent generation in open dialogue and summarization.

- Error-aware architectures introduce a hierarchically decoupled structure, first classifying error types at each step, then aggregating these fine-grained signals to a final reward score, which supports fine-grained attribution and improves benchmark performance.

- For robotics and agentic domains, step-wise or trajectory-level progress scoring enhances reward granularity and enables intermediate feedback.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e77fe37-2220-4406-8803-032ec5acaeb6",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "818b3134-ebf7-455f-9de4-161124de66fa",
  "sourceToolAssistantUUID": "9e77fe37-2220-4406-8803-032ec5acaeb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T10:16:31.298Z_

<details><summary>↩ Tool result · `toolu_01DHjaK4DsheAC2c8YDHkNne`</summary>

```text
Web search results for query: "process reward model step-level verification 2025"

Links: [{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for","url":"https://www.arxiv.org/pdf/2601.17223"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning","url":"https://arxiv.org/html/2601.17223"},{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/pdf/2510.13744"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the search results, here's what I found about process reward models and step-level verification in 2025:

## Overview of Process Reward Models with Step-Level Verification

Process reward models (PRMs) require step-level supervision, which is expensive to train, and recent work has focused on building data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought.

## Recent 2025 Developments

Several key advances have emerged in 2025:

1. **Generative Approaches**: Models such as ThinkPRM and GenPRM provide long-form verification chains, requiring orders of magnitude less annotation by leveraging the LLM's reasoning capacity.

2. **Error-Aware Labeling**: Decoupled error detection (math/logic/consistency) before reward computation yields better interpretability and sample efficiency.

3. **Efficient Supervision**: Training PRMs without ground-truth step labels (FreePRM) or with active, entropy-based, or Monte Carlo data selection enables scalable learning and extension to new problem domains.

4. **Formal Verification**: FOVER uses formal verification tools (e.g., Z3, Isabelle) to automatically generate PRM training data with accurate step-level error labels.

## Applications

Process Reward Models have exhibited remarkable success in domains such as mathematical reasoning and code generation, and by providing step-level supervision and fine-grained verification during both training and inference time, PRMs can significantly boost the models' reasoning reliability and performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b312d51d-0c7a-437a-8579-7c0d50f35d07",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "5278e15d-9863-4c95-9c90-39ff6f376f8d",
  "sourceToolAssistantUUID": "b312d51d-0c7a-437a-8579-7c0d50f35d07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T10:16:32.037Z_

<details><summary>↩ Tool result · `toolu_01D7K7kusH28pEp2aFJ68Wko`</summary>

```text
Web search results for query: "best-of-N sampling reward model scaling 2024 2025"

Links: [{"title":"Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling","url":"https://arxiv.org/html/2505.12225v3"},{"title":"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment","url":"https://proceedings.mlr.press/v267/huang25c.html"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/pdf/2502.18581"},{"title":"Reward Inside the Model: A Lightweight Hidden-State Reward Model for LLM’s Best-of-N sampling","url":"https://arxiv.org/html/2505.12225v1"},{"title":"CarBoN: Calibrated Best-of-N Sampling Improves Test-time Reasoning","url":"https://arxiv.org/pdf/2510.15674"},{"title":"GenSelect: A Generative Approach to Best-of-N","url":"https://arxiv.org/pdf/2507.17797"},{"title":"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in   Inference-Time Alignment","url":"https://arxiv.org/pdf/2503.21878"},{"title":"Regularized Best-of-N Sampling with Minimum Bayes Risk ...","url":"https://aclanthology.org/2025.naacl-long.472.pdf"}]

Based on the search results, here's what recent research shows about best-of-N sampling and reward model scaling in 2024-2025:

## Key Findings on Best-of-N Sampling

Best-of-N sampling is a test-time scaling strategy where a reward model selects the best response from a set of candidates. These algorithms are widely used throughout post-training for frontier models and serve as a cornerstone of fine-tuning and inference.

## Reward Model Limitations and Scaling Challenges

Naively scaling compute through best-of-N sampling can cause performance to degrade due to reward hacking. Simply increasing test-time compute does not guarantee optimal performance, as models may spend additional computation on low-quality reasoning paths without effective verification.

## Recent Advances in 2025

Several approaches have been proposed to improve best-of-N sampling:

1. **Calibrated Selection**: Calibrated accuracy at N=64 can match or exceed uncalibrated accuracy at N=256, corresponding to up to a 4× reduction in rollout budgets.

2. **Hidden State Rewards**: The Efficient Linear Hidden State Reward (ELHSR) model learns a linear gating and reward projection per token, with the final reward computed as a weighted average of token-level rewards.

3. **Generative Reward Models**: Recent work has demonstrated the efficacy of generative reward models (GenRMs), which offer another axis for leveraging test-time computation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49b57609-eb0f-4e80-bc90-d6b08cac9dbb",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "669a2477-a756-4a2a-b560-eb03125f992f",
  "sourceToolAssistantUUID": "49b57609-eb0f-4e80-bc90-d6b08cac9dbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T10:16:32.100Z_

<details><summary>↩ Tool result · `toolu_01DRoq6PCpcPb4LZZkpTH3Wi`</summary>

```text
Web search results for query: "process reward model PRM outcome reward model ORM 2024 2025 2026 LLM"

Links: [{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM   Reasoning","url":"https://arxiv.org/pdf/2410.08146"}]

Based on the search results, here's a comprehensive overview of Process Reward Models (PRMs) and Outcome Reward Models (ORMs) in recent LLM research:

## Key Definitions

Process Reward Models (PRMs) are designed to assess the correctness of each intermediate step within a multi-step reasoning trajectory generated by an LLM. In contrast, Outcome Reward Models (ORMs) provide a reward signal only for the final output, typically mapping an entire output sequence to a scalar reward.

## Advantages of PRMs

Traditional outcome reward models (ORMs) provide feedback only on the final model output, creating a sparse credit assignment problem: failures or shortcomings in intermediate steps cannot be localized or corrected effectively, leading to inefficient learning and error propagation. The step-level nature of PRMs allows the discovery and correction of localized errors, enabling improved explainability and targeted feedback during generation or evaluation.

## Recent Developments (2024-2025)

Most models use a binary label at each step (correct/incorrect), though recent variants allow for multi-level or probabilistic scoring. PRMs deliver step-level (and, in recent work, token-level) reward signals, with significant research contributions across 2024 and 2025.

## Applications

PRMs have demonstrated efficacy across mathematical reasoning tasks, including stepwise error detection, chain-of-thought evaluation, and inference-time candidate reranking for improved answer rates on GSM8K, MATH500, AIME24, and other benchmarks. PRMs are also used as critics in LLM-driven planning and control agents, where process feedback is delivered on each action or subgoal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77389084-6ff9-4ddb-b235-b6c5ad6fda68",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "a9c6d827-80c8-4e21-bdf9-bfdd6bfbd5ee",
  "sourceToolAssistantUUID": "77389084-6ff9-4ddb-b235-b6c5ad6fda68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-28T10:16:34.772Z_

Good, I have a solid set of leads. Now let me fetch the abstracts of the most important papers identified. Let me start with the key papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c6d827-80c8-4e21-bdf9-bfdd6bfbd5ee",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0f03a1a-f59f-49cd-99cd-fc8742f799d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 23 · 2026-05-28T10:16:36.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0189S4tysSeWjZESydENNZHs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.15240",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0f03a1a-f59f-49cd-99cd-fc8742f799d7",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5f83259-d612-483f-a6f6-157de2fd85ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 24 · 2026-05-28T10:16:36.671Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RJhjUM5V14xBg4kutkhyxZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5f83259-d612-483f-a6f6-157de2fd85ab",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2637a17-d8d1-4311-b83c-776222bbf2a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 25 · 2026-05-28T10:16:37.602Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017RYv8u3gedHe9XLyNfs4tK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.16828",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2637a17-d8d1-4311-b83c-776222bbf2a9",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a96a8353-0739-4b48-9ea4-edaf13b1ad8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 26 · 2026-05-28T10:16:38.072Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lzs8qV4nDo4Rmkkk5zUAbZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.08146",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a96a8353-0739-4b48-9ea4-edaf13b1ad8a",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "298b0846-e780-41fd-94da-bbb9101db7c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 27 · 2026-05-28T10:16:39.013Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S4vdA34ztaghNrfbQJY8or`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.08049",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "298b0846-e780-41fd-94da-bbb9101db7c0",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d11b5448-b97d-4467-bf40-50e014e48ab2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 28 · 2026-05-28T10:16:39.484Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CnMjEaMzjdxJHruTA7NenH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.05318",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d11b5448-b97d-4467-bf40-50e014e48ab2",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af586095-8cbf-4292-9ce2-b74ae072f8c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
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

_source line 29 · 2026-05-28T10:16:39.901Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013NEzrC2qgXWv7wJimgDGnk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.12608",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af586095-8cbf-4292-9ce2-b74ae072f8c3",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnyc5my715bJNgvRLFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "deb7c218-2a1b-444a-9dc8-135ea54d4385",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSe8uUDtHVFZSK3afKP3iT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4652,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 10178,
      "output_tokens": 631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4652,
          "output_tokens": 631,
          "cache_read_input_tokens": 10178,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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

_source line 30 · 2026-05-28T10:16:40.454Z_

<details><summary>↩ Tool result · `toolu_0189S4tysSeWjZESydENNZHs`</summary>

```text
# Paper Summary

**Title:** "Generative Verifiers: Reward Modeling as Next-Token Prediction"

**Authors:** Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, Rishabh Agarwal

**Publication Venue:** ICLR 2025

**Abstract:** 
The researchers propose training verification models using next-token prediction rather than traditional discriminative classifiers. Their approach, called GenRM, trains verifiers jointly on verification and solution generation tasks. The method leverages language model capabilities including chain-of-thought reasoning and majority voting. Results demonstrate substantial improvements: algorithmic task performance increased from 5% to 45.3%, GSM8K improved from 73% to 93.4%, MATH showed gains from 28% to 44.6%, and MMLU abstract algebra rose from 37.9% to 53.5%. The authors find that synthetic verification rationales suffice for identifying subtle mathematical errors and that performance scales favorably with model size.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5f83259-d612-483f-a6f6-157de2fd85ab",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "aa20336f-faf9-4c46-92a4-6ee849247acf",
  "sourceToolAssistantUUID": "d5f83259-d612-483f-a6f6-157de2fd85ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T10:16:41.961Z_

<details><summary>↩ Tool result · `toolu_01RJhjUM5V14xBg4kutkhyxZ`</summary>

```text
# Paper Details

**Full Title:**
"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"

**Authors:**
Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou

**Publication Venue:**
arXiv:2504.00891 [cs.CL] (Computer Science > Computation and Language)

**Complete Abstract:**
The researchers introduce GenPRM, which performs "explicit Chain-of-Thought reasoning with code verification" to evaluate reasoning steps. The system addresses three limitations of current process reward models: weak generalization, inability to leverage language model generative capabilities, and lack of test-time compute scaling. The authors propose Relative Progress Estimation and a rationale synthesis framework incorporating code verification to create training data. Results demonstrate that their 1.5B model surpasses GPT-4o on ProcessBench, while their 7B version outperforms Qwen2.5-Math-PRM-72B, using only 23K training examples from the MATH dataset. The work bridges process supervision approaches with critic models for policy refinement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2637a17-d8d1-4311-b83c-776222bbf2a9",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "c601db40-9636-4c70-82c1-7aded3fc2025",
  "sourceToolAssistantUUID": "a2637a17-d8d1-4311-b83c-776222bbf2a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T10:16:42.515Z_

<details><summary>↩ Tool result · `toolu_017RYv8u3gedHe9XLyNfs4tK`</summary>

```text
# Paper Extraction

**Full Title:**
"Process Reward Models That Think"

**Authors:**
Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang

**Publication Venue:**
arXiv:2504.16828 (Computer Science - Machine Learning)

**Abstract:**
The researchers introduce ThinkPRM, a generative verification approach that "generate[s] a verification chain-of-thought (CoT)" to evaluate solution steps. This method requires substantially less supervision than traditional process reward models, needing only 1% of labels from PRM800K while outperforming discriminative verifiers across benchmarks including ProcessBench, MATH-500, and AIME '24. The approach demonstrates particular strength in out-of-domain evaluations, surpassing standard verifiers by 8% on GPQA-Diamond and 4.5% on LiveCodeBench. Under equivalent computational budgets, ThinkPRM scales verification more efficiently than LLM-as-a-Judge approaches, achieving 7.2% improvement on ProcessBench, demonstrating that leveraging long reasoning chains can enable more efficient test-time compute scaling with minimal training supervision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a96a8353-0739-4b48-9ea4-edaf13b1ad8a",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "025f2ec0-d0fe-4dd0-a1ae-782d45422f66",
  "sourceToolAssistantUUID": "a96a8353-0739-4b48-9ea4-edaf13b1ad8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T10:16:43.014Z_

<details><summary>↩ Tool result · `toolu_01Lzs8qV4nDo4Rmkkk5zUAbZ`</summary>

```text
# Paper Summary

**Title:** "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning"

**Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar

**Publication Venue:** arXiv (Computer Science - Machine Learning and Computation and Language)

**Abstract:**

The researchers address improving reasoning in large language models through process reward models that give feedback at each step. They identify a key design principle: process rewards should measure "progress: a change in the likelihood of producing a correct response in the future, before and after taking the step." Their contribution involves training process advantage verifiers to predict this progress under specialized prover policies. The results demonstrate that compared to outcome reward models, test-time search achieves greater than 8% accuracy improvement and 1.5-5x better compute efficiency. Additionally, reinforcement learning with their dense reward approach yields "5-6x gain in sample efficiency, and >6% gain in accuracy" relative to traditional outcome-based methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "298b0846-e780-41fd-94da-bbb9101db7c0",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "0accc09d-bf01-4714-b056-c102e7548de1",
  "sourceToolAssistantUUID": "298b0846-e780-41fd-94da-bbb9101db7c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T10:16:43.550Z_

<details><summary>↩ Tool result · `toolu_01S4vdA34ztaghNrfbQJY8or`</summary>

```text
# Paper Information

**Full Title:** "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models"

**Authors:** Congmin Zheng, Jiachen Zhu, Zhuoying Ou, Yuxiang Chen, Kangning Zhang, Rong Shan, Zeyu Zheng, Mengyue Yang, Jianghao Lin, Yong Yu, and Weinan Zhang

**Publication Venue:** arXiv (Computer Science > Computation and Language)

**Complete Abstract:**

This survey examines how Process Reward Models (PRMs) evaluate reasoning step-by-step, contrasting with traditional outcome reward models that only assess final answers. The authors provide comprehensive coverage of the complete workflow: generating process-level data, constructing PRMs, and leveraging them for scaling at test time and reinforcement learning. The work covers implementations across diverse domains including mathematics, programming, natural language, multimodal reasoning, robotics, and autonomous agents, while also reviewing relevant benchmarks. The survey aims to clarify design choices, identify unresolved issues, and direct forthcoming scholarship toward developing more nuanced and dependable reasoning alignment systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d11b5448-b97d-4467-bf40-50e014e48ab2",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "6a7676dd-cd83-4da8-b377-4386e8472342",
  "sourceToolAssistantUUID": "d11b5448-b97d-4467-bf40-50e014e48ab2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T10:16:44.192Z_

<details><summary>↩ Tool result · `toolu_013NEzrC2qgXWv7wJimgDGnk`</summary>

```text
# Paper Information

**Full Title:** "Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning"

**Authors:** Vernon Y.H. Toh, Deepanway Ghosal, Soujanya Poria

**Publication Venue:** arXiv:2410.12608 (cs.CL - Computation and Language)

**Complete Abstract:**

Large language models demonstrate increasing capability in mathematical reasoning tasks, yet open-source variants frequently encounter calculation errors and semantic misunderstandings in intermediate steps. This work presents Prove, a framework that converts natural language solutions into executable programs for verification, filtering unreliable reasoning paths before final answer aggregation. Rather than using simple majority voting, the method retains only solutions whose program outputs align with generated responses. Testing across 13 open-source models (0.5B-13B parameters) and eight mathematical benchmarks showed consistent improvements, with gains reaching 18% on GSM8K and 8% on MATH-500. The authors made their implementation publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deb7c218-2a1b-444a-9dc8-135ea54d4385",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "f279bea5-964b-422d-8510-c64b5c778b4d",
  "sourceToolAssistantUUID": "deb7c218-2a1b-444a-9dc8-135ea54d4385",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T10:16:44.572Z_

<details><summary>↩ Tool result · `toolu_01CnMjEaMzjdxJHruTA7NenH`</summary>

```text
# Paper Information

**Full Title:** "Improving LLM Reasoning through Scaling Inference Computation with Collaborative Verification"

**Authors:** Zhenwen Liang, Ye Liu, Tong Niu, Xiangliang Zhang, Yingbo Zhou, Semih Yavuz

**Publication Venue:** arXiv (Computer Science > Machine Learning); arXiv:2410.05318

**Abstract:**

Despite advances in LLM capabilities, they struggle with consistent reasoning in complex tasks like mathematics and code. The authors identify that models trained primarily on correct solutions lack ability to detect errors and verify outputs effectively. 

Their approach involves "generating multiple reasoning paths and employing verifiers to assess and rank the generated outputs by correctness." They introduce a dataset of both correct and incorrect solutions across math and code tasks. Notably, they propose "a novel collaborative method integrating Chain-of-Thought (CoT) and Program-of-Thought (PoT) solutions for verification," where "CoT provides a clear, step-by-step reasoning process" while "PoT, being executable, offers a precise and error-sensitive validation mechanism."

The resulting verifiers, Math-Rev and Code-Rev, achieve strong performance on GSM8k and MATH benchmarks, even outperforming GPT-4o when paired with Qwen-72B-Instruct as the reasoner.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af586095-8cbf-4292-9ce2-b74ae072f8c3",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "ba439cf0-cf73-4822-9e6d-e33fb398bd73",
  "sourceToolAssistantUUID": "af586095-8cbf-4292-9ce2-b74ae072f8c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-28T10:16:47.674Z_

Now let me fetch more key papers, including some foundational ones and recent important works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba439cf0-cf73-4822-9e6d-e33fb398bd73",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d3942c7-683d-4acd-ab4c-bb8a7d714e44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7103,
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

_source line 38 · 2026-05-28T10:16:48.529Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MmjMDCtdncTdeAAPorkX1Q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15960",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d3942c7-683d-4acd-ab4c-bb8a7d714e44",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2646a381-3956-49f4-8ec5-6fd831d6a2a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7103,
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

_source line 39 · 2026-05-28T10:16:49.000Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CxWA27wv8D8gRGFaYFxyFe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.17223",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2646a381-3956-49f4-8ec5-6fd831d6a2a5",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d2ac78b-6294-400c-b7ce-55684c3b6b1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7103,
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

_source line 40 · 2026-05-28T10:16:49.472Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CXsNurFm7ft9LnEEcZ9CRp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.09305",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d2ac78b-6294-400c-b7ce-55684c3b6b1c",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65c65f22-53f1-4302-bd7f-d946759c3fed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7103,
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

_source line 41 · 2026-05-28T10:16:50.413Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019iMS8ZN7iBHMnVPFazCeX6`</summary>

```json
{
  "url": "https://proceedings.mlr.press/v267/huang25c.html",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65c65f22-53f1-4302-bd7f-d946759c3fed",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e022713-e473-4b9e-861c-f6b30979000c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7103,
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

_source line 42 · 2026-05-28T10:16:51.354Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FrNzGZaHE9Q4JC5xmDqy5B`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.18581",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e022713-e473-4b9e-861c-f6b30979000c",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e5b881f-2f8e-4833-b262-736577221b12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7103,
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

_source line 43 · 2026-05-28T10:16:52.188Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PXUqACXjudFuAZXjV9hxEJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.26578",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper. Note that if the paper ID seems wrong, report what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e5b881f-2f8e-4833-b262-736577221b12",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUnzXN3EaXYBWwUWnunK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40141846-fd85-4adf-96e5-97b2b231bc02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017m6doejQUbzZcZ5cwwydDg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 11215,
      "output_tokens": 551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 265,
          "output_tokens": 551,
          "cache_read_input_tokens": 11215,
          "cache_creation_input_tokens": 7103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7103,
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

_source line 44 · 2026-05-28T10:16:52.871Z_

<details><summary>↩ Tool result · `toolu_01MmjMDCtdncTdeAAPorkX1Q`</summary>

```text
# Paper Summary

**Title:** "Efficient PRM Training Data Synthesis via Formal Verification"

**Authors:** Ryo Kamoi, Yusen Zhang, Nan Zhang, Sarkar Snigdha Sarathi Das, Ranran Haoran Zhang, Wenpeng Yin, Rui Zhang

**Publication Venue:** ACL 2026 Findings

**Abstract:** The researchers present FoVer, a framework addressing costly and noisy PRM training data construction. Rather than relying on human annotation or repeated LLM calls, they "synthesize PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools." Experiments across 12 benchmarks demonstrate that models fine-tuned on this data improve performance not only on math and logic tasks but also on "NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data." This shows formal verification-based training data enhances PRM capabilities on informal natural language reasoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2646a381-3956-49f4-8ec5-6fd831d6a2a5",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "182ab5ed-a2a0-4fe9-bf2e-9f0dff8c6e91",
  "sourceToolAssistantUUID": "2646a381-3956-49f4-8ec5-6fd831d6a2a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T10:16:53.570Z_

<details><summary>↩ Tool result · `toolu_019iMS8ZN7iBHMnVPFazCeX6`</summary>

```text
# Paper Information

**Full Title:** "Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment"

**Authors:** Audrey Huang, Adam Block, Qinghua Liu, Nan Jiang, Akshay Krishnamurthy, Dylan J Foster

**Publication Venue:** Proceedings of the 42nd International Conference on Machine Learning (PMLR Volume 267), July 13-19, 2025

**Complete Abstract:**

Recent advances in inference-time alignment demonstrate computational benefits for language models, yet naive scaling through Best-of-N sampling risks performance degradation via reward hacking. This work develops theory for optimally using additional compute during inference with imperfect reward models. Key findings show Best-of-N achieves optimality under strict coverage assumptions but "provably suffers from reward hacking when N is large." The authors introduce InferenceTimePessimism, an algorithm using deliberate pessimism to prevent reward hacking while maintaining "optimal and scaling-monotonic" performance that doesn't degrade as N increases. Empirical validation across multiple tasks and models confirms the approach's practical viability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e022713-e473-4b9e-861c-f6b30979000c",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "669cab7f-0131-454a-bbef-229ab1cdd88a",
  "sourceToolAssistantUUID": "4e022713-e473-4b9e-861c-f6b30979000c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T10:16:53.646Z_

<details><summary>↩ Tool result · `toolu_01CXsNurFm7ft9LnEEcZ9CRp`</summary>

```text
# Paper Information

**Full Title:** "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation"

**Authors:** Pei-Chi Pan, Yingbin Liang, Sen Lin

**Publication Venue:** arXiv (Computer Science > Machine Learning), submitted February 10, 2026

**Complete Abstract:**

The paper examines how reward design shapes LLM reasoning through reinforcement learning. The authors argue that "reward modeling is not merely an implementation detail but a central architect of reasoning alignment," influencing what models learn and whether outputs are trustworthy. They introduce Reasoning-Aligned Reinforcement Learning (RARL), a framework organizing different reward approaches for multi-step reasoning. The work presents a taxonomy of reward mechanisms, analyzes reward hacking as a failure mode, and evaluates how reward signals address challenges like hallucination and inference-time scaling. The authors critically assess existing benchmarks for vulnerabilities including data contamination and misalignment, ultimately providing a roadmap for developing reasoning models that are "robust, verifiable, and trustworthy."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65c65f22-53f1-4302-bd7f-d946759c3fed",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "057d682d-c9ed-4ea4-9320-3fb9d422bd67",
  "sourceToolAssistantUUID": "65c65f22-53f1-4302-bd7f-d946759c3fed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T10:16:53.921Z_

<details><summary>↩ Tool result · `toolu_01CxWA27wv8D8gRGFaYFxyFe`</summary>

```text
# Paper Details

**Full Title:** "Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning"

**Authors:** 
- Massimiliano Pronesti
- Anya Belz
- Yufang Hou

**Publication Venue:** arXiv (Computer Science > Computation and Language)

**Complete Abstract:**

Recent advances in reinforcement learning with verifiable rewards have demonstrated that large language models can be meaningfully enhanced through outcome-level verification like unit tests or exact-match evaluations. While process supervision has explored shaping intermediate reasoning, existing neural judge approaches introduce concerns around interpretability and potential reward hacking. The authors introduce a novel framework employing deterministic, rule-based verifiers to evaluate intermediate reasoning steps rather than relying on neural scoring. They demonstrate this approach on medical evidence synthesis risk-of-bias assessment, where guideline-defined criteria enable programmatic verification. Results indicate reasoning adheres closely to domain rules with substantially improved coherence between step-level decisions and final labels, achieving "up to 20% higher F1 than state-of-the-art models and 6.5% higher than verifiable outcome rewards" with notable enhancements in evidence grounding and logical coherence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d2ac78b-6294-400c-b7ce-55684c3b6b1c",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "4cbefe83-dc8d-4004-adc0-83f5c49fb848",
  "sourceToolAssistantUUID": "7d2ac78b-6294-400c-b7ce-55684c3b6b1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T10:16:55.863Z_

<details><summary>↩ Tool result · `toolu_01FrNzGZaHE9Q4JC5xmDqy5B`</summary>

```text
# Paper Summary

**Title:** "Scalable Best-of-N Selection for Large Language Models via Self-Certainty"

**Authors:** Zhewei Kang, Xuandong Zhao, Dawn Song

**Publication Venue:** NeurIPS 2025

**Abstract:**
The researchers present self-certainty, a novel technique for improving LLM reasoning without expensive reward models. Rather than relying on external evaluators, the method leverages the probability distributions inherent in model outputs to assess response quality. The authors hypothesize that "higher distributional self-certainty, aggregated across multiple samples, correlates with improved response accuracy." Their experiments demonstrate three key benefits: effective scaling with larger sample sizes N, improved performance when combined with chain-of-thought reasoning, and applicability to open-ended tasks where existing alternatives struggle. The work provides a computationally efficient alternative to traditional reward-based selection approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e5b881f-2f8e-4833-b262-736577221b12",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "dfae3cad-6b01-4abe-8e79-9dcac0cffec1",
  "sourceToolAssistantUUID": "8e5b881f-2f8e-4833-b262-736577221b12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T10:16:56.579Z_

<details><summary>↩ Tool result · `toolu_01PXUqACXjudFuAZXjV9hxEJ`</summary>

```text
# Paper Extraction

**Full Title:**
"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning"

**Authors:**
Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren

**Publication Venue:**
arXiv (Computer Science > Machine Learning), identifier 2509.26578

**Complete Abstract:**
The paper addresses limitations in existing Process Reward Models by proposing Conditional Reward Modeling (CRM). This approach "frames LLM reasoning as a temporal process leading to a correct answer," where "the reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome." Through conditional probability enforcement, CRM captures causal relationships among reasoning steps and improves credit assignment. The authors demonstrate their method's effectiveness across multiple evaluation approaches, showing that CRM "is more robust to reward hacking and delivers stable downstream improvements" compared to alternative reward modeling techniques.

**Note:** The paper ID appears valid; this is a legitimate arXiv submission (v1: September 30, 2025; v2: February 27, 2026).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40141846-fd85-4adf-96e5-97b2b231bc02",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "4e5a7290-527c-4213-9f6b-d17de9e0556e",
  "sourceToolAssistantUUID": "40141846-fd85-4adf-96e5-97b2b231bc02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-28T10:16:59.633Z_

Now let me search for a few more important papers that I know are foundational in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e5a7290-527c-4213-9f6b-d17de9e0556e",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo1Qfjo8yjrTS2e3cQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37712180-40a2-4e95-8ef3-c0c366ad52ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcByEFpnm66mR97YWGG99W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 18318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2429,
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

_source line 51 · 2026-05-28T10:17:00.119Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F93ZyTePBivmG6BccwtRFk`</summary>

```json
{
  "query": "Math-Shepherd process reward model 2024 NeurIPS ICML paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37712180-40a2-4e95-8ef3-c0c366ad52ec",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo1Qfjo8yjrTS2e3cQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05c4c60f-40f1-4543-b5f9-a07b8d8453d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcByEFpnm66mR97YWGG99W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 18318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2429,
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

_source line 52 · 2026-05-28T10:17:01.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012KnMN2VEujpFrvD1Exbdhj`</summary>

```json
{
  "query": "\"scaling LLM test-time compute\" optimal 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c4c60f-40f1-4543-b5f9-a07b8d8453d9",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo1Qfjo8yjrTS2e3cQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "965c0d19-4bf7-4866-b0cf-ea3ca46ad618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcByEFpnm66mR97YWGG99W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 18318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2429,
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

_source line 53 · 2026-05-28T10:17:01.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ATfPoERT9wiMA7jJvTHe5w`</summary>

```json
{
  "query": "OmegaPRM Monte Carlo tree search process reward model 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "965c0d19-4bf7-4866-b0cf-ea3ca46ad618",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo1Qfjo8yjrTS2e3cQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b8feb1c-6a3d-48c3-b815-d55241ff790a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcByEFpnm66mR97YWGG99W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 18318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2429,
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

_source line 54 · 2026-05-28T10:17:02.040Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K48ngm877jhHUdQTWLoDN2`</summary>

```json
{
  "query": "\"PRM800K\" \"let's verify step by step\" OpenAI process supervision 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8feb1c-6a3d-48c3-b815-d55241ff790a",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo1Qfjo8yjrTS2e3cQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5a95b19-0751-414a-a307-4a2d5162cc67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcByEFpnm66mR97YWGG99W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 18318,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2429
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 18318,
          "cache_creation_input_tokens": 2429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2429,
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

_source line 55 · 2026-05-28T10:17:08.089Z_

<details><summary>↩ Tool result · `toolu_01F93ZyTePBivmG6BccwtRFk`</summary>

```text
Web search results for query: "Math-Shepherd process reward model 2024 NeurIPS ICML paper"

Links: [{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.510/"},{"title":"Math-Shepherd: LLM Step-by-Step Verification","url":"https://www.emergentmind.com/papers/2312.08935"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Math-Shepherd: Process-Oriented Reward Modeling","url":"https://www.emergentmind.com/topics/math-shepherd"},{"title":"[2312.08935] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935"},{"title":"What Are Step-Level Reward Models Rewarding?","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34663/36818"},{"title":"Papers Explained 366: Math Shepherd | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-366-math-shepherd-234b1bdfbcae"},{"title":"Paper page - Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://huggingface.co/papers/2312.08935"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"DuaShepherd: Integrating Stepwise Correctness and Potential Rewards for Mathematical Reasoning","url":"https://arxiv.org/pdf/2506.17533"}]

Based on the search results, I found information about the Math-Shepherd paper:

## Math-Shepherd: Process Reward Model for Mathematical Reasoning

Math-Shepherd is an innovative process-oriented math process reward model that assigns a reward score to each step of math problem solutions. The training of Math-Shepherd is achieved using automatically constructed process-wise supervision data, breaking the bottleneck of heavy reliance on manual annotation in existing work.

**Publication Details:**
The paper was presented at the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in August 2024, not at NeurIPS or ICML as you mentioned. The paper was authored by Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui.

**Key Capabilities:**
The paper introduces a process-oriented reward model that evaluates each reasoning step to both verify and reinforce LLM outputs in mathematical tasks, employing automatic process annotation inspired by Monte Carlo Tree Search to generate supervision labels without the need for costly human annotations.

**Results:**
Process RL with Math-Shepherd significantly enhances Mistral-7B (77.9%→84.1% on GSM8K and 28.6%→33.0% on MATH), with accuracy further improved to 89.1% and 43.5% on two benchmarks with verification of Math-Shepherd.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05c4c60f-40f1-4543-b5f9-a07b8d8453d9",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "906d5722-1f32-4b61-b2b9-4f6d2345b144",
  "sourceToolAssistantUUID": "05c4c60f-40f1-4543-b5f9-a07b8d8453d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-28T10:17:08.181Z_

<details><summary>↩ Tool result · `toolu_01ATfPoERT9wiMA7jJvTHe5w`</summary>

```text
Web search results for query: "OmegaPRM Monte Carlo tree search process reward model 2024"

Links: [{"title":"2024-12-10 Improve Mathematical Reasoning in Language","url":"https://arxiv.org/pdf/2406.06592"},{"title":"[PDF] Improve Mathematical Reasoning in Language Models by Automated Process Supervision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improve-Mathematical-Reasoning-in-Language-Models-Luo-Liu/f32bcc2155997110a7905da050df4c8404867b24"},{"title":"[2406.06592] Improve Mathematical Reasoning in Language Models by Automated Process Supervision","url":"https://arxiv.org/abs/2406.06592"},{"title":"Philipp Schmid on X: \"Let's think step by step and verify, but without humans. 🔥 Improve Mathematical Reasoning in Language Models by Automated Process Supervision from @GoogleDeepMind proposes a new divide-and-conquer style Monte Carlo Tree Search (OmegaPRM) to improve multi-hop reasoning chains https://t.co/AZIhfzy3Ip\" / X","url":"https://x.com/_philschmid/status/1838865177116045533"},{"title":"Google DeepMind Researchers Propose a Novel Divide-and-Conquer Style Monte Carlo Tree Search (MCTS) Algorithm 'OmegaPRM' for Efficiently Collecting High-Quality Process Supervision Data - MarkTechPost","url":"https://www.marktechpost.com/2024/06/16/google-deepmind-researchers-propose-a-novel-divide-and-conquer-style-monte-carlo-tree-search-mcts-algorithm-omegaprm-for-efficiently-collecting-high-quality-process-supervision-data/"},{"title":"[Quick Review] Improve Mathematical Reasoning in Language Models by Automated Process\\n Supervision","url":"https://liner.com/review/improve-mathematical-reasoning-in-language-models-by-automated-process-supervision"},{"title":"Improve Mathematical Reasoning in Language Models with Automated Process Supervision | OpenReview","url":"https://openreview.net/forum?id=KwPUQOQIKt"},{"title":"RPM-MCTS: Knowledge-Retrieval as Process Reward Model with Monte Carlo Tree Search for Code Generation","url":"https://arxiv.org/pdf/2511.19895"}]

Based on the search results, here's information about OmegaPRM:

## Overview

OmegaPRM is a novel divide-and-conquer style Monte Carlo Tree Search (MCTS) algorithm for the efficient collection of high-quality process supervision data. It was introduced by researchers at Google DeepMind and Google.

## Purpose and Problem It Solves

Previous methods for collecting process supervision data relied on either human annotation or per-step Monte Carlo estimation, both prohibitively expensive to scale. Process supervision addresses this by assigning intermediate rewards during the reasoning process.

## How It Works

OmegaPRM identifies the first error in the Chain of Thought (CoT) with binary search and balances the positive and negative examples to then train a Process Reward Model (PRM).

## Results and Performance

OmegaPRM was able to collect over 1.5 million process supervision annotations to train Process Reward Models (PRMs) and enhance LLMs' math reasoning performances. Using the weighted self-consistency algorithm alongside automated process supervision, the Gemini Pro model achieved a 69.4% success rate on the MATH benchmark, representing a 36% relative improvement from the base model's 51% performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b8feb1c-6a3d-48c3-b815-d55241ff790a",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "d9513340-30d9-4ffa-b584-75623085d5cf",
  "sourceToolAssistantUUID": "7b8feb1c-6a3d-48c3-b815-d55241ff790a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T10:17:08.587Z_

<details><summary>↩ Tool result · `toolu_01K48ngm877jhHUdQTWLoDN2`</summary>

```text
Web search results for query: ""PRM800K" "let's verify step by step" OpenAI process supervision 2024"

Links: [{"title":"Process supervision — Grokipedia","url":"https://grokipedia.com/page/Process_supervision"},{"title":"[2305.20050] Let's Verify Step by Step - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.20050"},{"title":"Let's Verify Step by Step","url":"https://www.researchgate.net/publication/371175770_Let's_Verify_Step_by_Step"},{"title":"GitHub - openai/prm800k: 800,000 step-level correctness labels on LLM solutions to MATH problems · GitHub","url":"https://github.com/openai/prm800k"},{"title":"Let's Verify Step by Step: How OpenAI o1 was created - DEV Community","url":"https://dev.to/shagun_mistry/lets-verify-step-by-step-how-openai-o1-was-created-2mll"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"Let's Verify Step by Step | OpenReview","url":"https://openreview.net/forum?id=v8L0pN6EOi"},{"title":"Let's Verify Step by Step","url":"https://arxiv.org/pdf/2305.20050"},{"title":"Let's Verify Step by Step","url":"https://blog.athina.ai/let-s-verify-step-by-step"}]

Based on the search results, here's what I found:

## Summary

OpenAI's "Let's Verify Step by Step" paper, published in 2023, formalized process supervision as a training paradigm superior to outcome supervision for mathematical reasoning. To facilitate further research, the authors released the PRM800K dataset, comprising 800,000 human-annotated step-level correctness labels across 75,000 solutions derived from the MATH dataset.

## Key Results

Models trained with process reward models (PRMs) achieved substantially higher accuracy on the MATH dataset—reaching 78.2% compared to 72.4% for outcome supervision on a representative subset—by providing step-level feedback to correct errors early in the reasoning chain.

## Impact and Adoption

Process supervision rapidly gained adoption in 2023 and 2024, particularly for enhancing mathematical reasoning in language models, with subsequent studies leveraging PRM800K to improve performance on benchmarks such as GSM8K.

The research demonstrates that providing feedback at each reasoning step (process supervision) is more effective than only evaluating final answers (outcome supervision) for improving AI model performance on complex mathematical problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5a95b19-0751-414a-a307-4a2d5162cc67",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "10c417e0-466d-449d-bb71-f4eba5e19ae0",
  "sourceToolAssistantUUID": "b5a95b19-0751-414a-a307-4a2d5162cc67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T10:17:09.582Z_

<details><summary>↩ Tool result · `toolu_012KnMN2VEujpFrvD1Exbdhj`</summary>

```text
Web search results for query: ""scaling LLM test-time compute" optimal 2024 2025 paper"

Links: [{"title":"Scaling Test-time Compute for LLM Agents","url":"https://arxiv.org/html/2506.12928v1"},{"title":"Scaling LLM Test Time Compute","url":"https://www.jonvet.com/blog/llm-test-time-compute"},{"title":"SCALING LLM TEST-TIME COMPUTE OPTIMALLY CAN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/scaling-llm-test-time-compute-optimally-can-be-more-effective-than-scaling-model-parameters-19a0c9fb7c44"},{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time   Scaling","url":"https://arxiv.org/pdf/2502.06703"}]

Based on the search results, I found several key papers on scaling LLM test-time compute:

## Primary Papers

**2024 Paper - Foundational Work:**
Snell et al. (2024) showed that "scaling llm test-time compute optimally can be more effective than scaling model parameters" (arXiv:2408.03314). This paper demonstrated that using more test-time compute can be more effective than scaling model size, and shows that different test-time compute strategies have different effectiveness depending on problem difficulty, proposing a compute-optimal scaling strategy that is adaptively applied per prompt.

**2025 Paper - Recent Analysis:**
Liu et al. (2025) published "Can 1B LLM surpass 405B LLM? rethinking compute-optimal test-time scaling" (arXiv:2502.06703). This paper categorizes test-time scaling (TTS) into internal TTS (which trains LLMs to "think" slowly) and external TTS (which improves reasoning via sampling/search methods), addressing the key challenge of how to scale compute optimally.

**December 2025 Paper:**
A recent paper on "The Art of Scaling Test-Time Compute for Large Language Models" illustrates that "there is no free lunch for TTS strategies: no single strategy is optimal and optimality depends on compute budget".

These papers collectively explore how test-time compute allocation strategies vary by problem difficulty and provide frameworks for optimal scaling decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "965c0d19-4bf7-4866-b0cf-ea3ca46ad618",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "19297ae9-ecb6-4be8-b9e2-0e70b5722b47",
  "sourceToolAssistantUUID": "965c0d19-4bf7-4866-b0cf-ea3ca46ad618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-28T10:17:11.871Z_

Let me now fetch the remaining key papers' abstracts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19297ae9-ecb6-4be8-b9e2-0e70b5722b47",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35cf33d5-0867-4dc4-a042-1af92283503f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 60 · 2026-05-28T10:17:12.867Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Ldq6oNWQhwp7Z6zPtoQBp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.03314",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35cf33d5-0867-4dc4-a042-1af92283503f",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19b332c7-2a52-42ea-9241-36089f4f284d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 61 · 2026-05-28T10:17:13.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014D6iLykCnjADMA9sJzQS5v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.06592",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19b332c7-2a52-42ea-9241-36089f4f284d",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d36fd436-a364-44e1-9a39-034d4a1384b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 62 · 2026-05-28T10:17:14.285Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JiKrBtbVdiDApp6dE6CgFx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2312.08935",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36fd436-a364-44e1-9a39-034d4a1384b5",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f094f2a2-00a3-477a-ad7d-28846fed5059",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 63 · 2026-05-28T10:17:14.756Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018jaZ66jeBiPQhcEoY6vEUK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.20050",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f094f2a2-00a3-477a-ad7d-28846fed5059",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c550eced-0d89-4856-9fb4-ba15d883c893",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 64 · 2026-05-28T10:17:15.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017pPF1MNvX7ZkL1gtuddgrf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06703",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c550eced-0d89-4856-9fb4-ba15d883c893",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0e84370-5e67-4355-b9de-ff168b6d5b86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 65 · 2026-05-28T10:17:16.058Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013LS4MpSwpJ98x5bMhKiedR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.13744",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e84370-5e67-4355-b9de-ff168b6d5b86",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo2NGu77mgHsRAB99o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed3a8a90-dcd1-4519-96f1-3eb267fc8b6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMEKrLYT6eZ7Qkjm46BEjs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1619,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 20747,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2027
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1619,
          "output_tokens": 528,
          "cache_read_input_tokens": 20747,
          "cache_creation_input_tokens": 2027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2027,
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

_source line 66 · 2026-05-28T10:17:17.359Z_

<details><summary>↩ Tool result · `toolu_013Ldq6oNWQhwp7Z6zPtoQBp`</summary>

```text
# Paper Information

**Full Title:** "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"

**Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar

**Publication Venue:** arXiv (cs.LG - Computer Science, Machine Learning); submitted August 6, 2024

**Complete Abstract:**

The research examines how large language models can leverage additional computational resources during inference to enhance performance. The authors investigate two primary strategies: (1) employing process-based verifier models for searching responses, and (2) adaptively updating the model's response distribution based on input prompts. 

A key finding is that strategy effectiveness varies significantly based on problem difficulty. The authors propose a "compute-optimal" allocation approach that dynamically distributes test-time resources per prompt. This method achieves "more than 4x" efficiency gains compared to standard sampling baselines. Notably, they demonstrate that when matched by total computational budget, a smaller base model augmented with test-time computation can surpass a substantially larger model by approximately 14x parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19b332c7-2a52-42ea-9241-36089f4f284d",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "c69096f4-20e8-4d1b-906f-8d91b2bf51d4",
  "sourceToolAssistantUUID": "19b332c7-2a52-42ea-9241-36089f4f284d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-28T10:17:18.920Z_

<details><summary>↩ Tool result · `toolu_01JiKrBtbVdiDApp6dE6CgFx`</summary>

```text
# Paper Details

**Full Title:** "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"

**Authors:** Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, Damai Dai, Yifei Li, Deli Chen, Y.Wu, Zhifang Sui

**Publication Venue:** arXiv (Computer Science - Artificial Intelligence)

**Complete Abstract:**

The paper presents Math-Shepherd, a process-oriented reward model that assigns scores to individual steps in mathematical problem solutions. Rather than depending on manual labeling, the model trains on automatically generated supervisory data. The research demonstrates two applications: first, using Math-Shepherd to rerank multiple LLM outputs, and second, employing it within a reinforcement learning framework with step-by-step Proximal Policy Optimization. Results show significant improvements—for example, Mistral-7B's accuracy jumped from 77.9% to 84.1% on GSM8K and from 28.6% to 33.0% on MATH through PPO training. Verification further enhanced these results to 89.1% and 43.5% respectively. The authors argue that "automatic process supervision holds significant potential for the future evolution of LLMs."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f094f2a2-00a3-477a-ad7d-28846fed5059",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "58ff30de-eef4-43ac-bab6-263219687518",
  "sourceToolAssistantUUID": "f094f2a2-00a3-477a-ad7d-28846fed5059",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-28T10:17:18.997Z_

<details><summary>↩ Tool result · `toolu_014D6iLykCnjADMA9sJzQS5v`</summary>

```text
# Paper Information

**Full Title:** "Improve Mathematical Reasoning in Language Models by Automated Process Supervision"

**Authors:** Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi

**Publication Venue:** arXiv (cs.CL - Computation and Language category)

**Complete Abstract:**

The paper addresses challenges in multi-step reasoning tasks for large language models. The authors propose an algorithm called OmegaPRM that uses Monte Carlo Tree Search to collect process supervision data efficiently without human annotation. This method identifies errors in reasoning chains through binary search and balances training examples. The team collected over 1.5 million process supervision annotations to train Process Reward Models. Results show significant improvements: Gemini Pro's performance increased from 51% to 69.4% on MATH500 and from 86.4% to 93.6% on GSM8K; Gemma2 27B improved from 42.3% to 58.2% on MATH500 and from 74.0% to 92.2% on GSM8K. The entire approach operates "without any human intervention or supervision," making it both scalable and cost-effective.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d36fd436-a364-44e1-9a39-034d4a1384b5",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "a2d808bb-a82a-4b65-b1af-8d6ac0949525",
  "sourceToolAssistantUUID": "d36fd436-a364-44e1-9a39-034d4a1384b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-28T10:17:19.119Z_

<details><summary>↩ Tool result · `toolu_018jaZ66jeBiPQhcEoY6vEUK`</summary>

```text
# Paper Details

**Full Title:** "Let's Verify Step by Step"

**Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe

**Publication Venue:** arXiv (Computer Science > Machine Learning), submitted May 31, 2023

**Abstract:** 
The researchers investigate training methods for improving large language model reliability on complex reasoning tasks. They compare two feedback approaches: outcome supervision (evaluating final results) and process supervision (evaluating intermediate steps). Their findings demonstrate that process supervision substantially outperforms outcome supervision when training models on challenging mathematics problems, with their best model achieving a 78% solution rate on representative test samples. The study also shows active learning enhances process supervision effectiveness. The team released PRM800K, a dataset containing 800,000 step-level human feedback annotations used to develop their top-performing reward model, supporting future related research in this domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c550eced-0d89-4856-9fb4-ba15d883c893",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "87e0feea-2c5a-4f2f-b433-4c8a7ac68acb",
  "sourceToolAssistantUUID": "c550eced-0d89-4856-9fb4-ba15d883c893",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-28T10:17:20.415Z_

<details><summary>↩ Tool result · `toolu_017pPF1MNvX7ZkL1gtuddgrf`</summary>

```text
# Paper Summary

**Full Title:** "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"

**Authors:** Runze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, Bowen Zhou

**Publication Venue:** arXiv (Computer Science > Computation and Language), submitted February 10, 2025

**Abstract:**

The research examines how test-time scaling can enhance language model performance through additional inference computation. The authors investigate how policy models, Process Reward Models, and task difficulty affect scaling strategies. Testing on MATH-500 and AIME24 benchmarks, they find that "optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty." Their key finding demonstrates that smaller models with optimized compute-scaling strategies can significantly outperform larger ones—including a 1B model exceeding a 405B model on certain tasks, and smaller models surpassing GPT-4o and o1 while maintaining greater efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0e84370-5e67-4355-b9de-ff168b6d5b86",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "3b4e2cfa-1519-4353-9470-8f9010dc86c0",
  "sourceToolAssistantUUID": "d0e84370-5e67-4355-b9de-ff168b6d5b86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-28T10:17:21.149Z_

<details><summary>↩ Tool result · `toolu_013LS4MpSwpJ98x5bMhKiedR`</summary>

```text
# Hard2Verify Paper Information

**Full Title:** "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math"

**Authors:** Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, Shafiq Joty

**Publication Venue:** arXiv (Computer Science > Artificial Intelligence)
- arXiv ID: 2510.13744
- Submission Date: October 15, 2025

**Abstract:** 
The researchers introduce a human-annotated benchmark for evaluating step-level verification in mathematical reasoning. They note that "Large language model (LLM)-based reasoning systems have recently achieved gold medal-level performance in the IMO 2025 competition," and created Hard2Verify to assess verifiers' ability to catch errors in frontier LLM outputs. The benchmark required over 500 hours of human annotation. Their evaluation of 29 different verification models reveals that "beyond a few standouts, open-source verifiers lag closed source models." The work examines performance drivers, scaling effects, and dynamics between verification and generation processes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed3a8a90-dcd1-4519-96f1-3eb267fc8b6e",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "997aa532-44a6-4436-9c99-17411663edd8",
  "sourceToolAssistantUUID": "ed3a8a90-dcd1-4519-96f1-3eb267fc8b6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-28T10:17:23.424Z_

Let me search for a few more important papers in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "997aa532-44a6-4436-9c99-17411663edd8",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo3Dij8tpaMR2X7nmFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d14234d3-e9b4-4848-8872-07ae6dae93be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UYWsjh1CUb3mgDweNKcRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3926,
      "cache_read_input_tokens": 22774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3926,
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

_source line 73 · 2026-05-28T10:17:24.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UNAYgEGAVTxVo5yAQfKsai`</summary>

```json
{
  "query": "\"adaptive verification\" \"compute allocation\" LLM reasoning inference-time 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d14234d3-e9b4-4848-8872-07ae6dae93be",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo3Dij8tpaMR2X7nmFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0291a4a2-8c0c-4146-aa60-66a87c845950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UYWsjh1CUb3mgDweNKcRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3926,
      "cache_read_input_tokens": 22774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3926,
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

_source line 74 · 2026-05-28T10:17:24.833Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016jCiXRmv4V3P6hZpsMwH34`</summary>

```json
{
  "query": "DeepSeek R1 reinforcement learning reasoning verification 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0291a4a2-8c0c-4146-aa60-66a87c845950",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo3Dij8tpaMR2X7nmFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7ac7943-5853-485b-b975-ade949fbda40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UYWsjh1CUb3mgDweNKcRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3926,
      "cache_read_input_tokens": 22774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3926,
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

_source line 75 · 2026-05-28T10:17:25.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sf2pqYFGk53eceFiBN3336`</summary>

```json
{
  "query": "\"token-level reward\" \"step-level reward\" process reward model granularity comparison 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7ac7943-5853-485b-b975-ade949fbda40",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo3Dij8tpaMR2X7nmFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9706752b-2f67-4e3d-9749-7afe30919906",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UYWsjh1CUb3mgDweNKcRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3926,
      "cache_read_input_tokens": 22774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3926,
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

_source line 76 · 2026-05-28T10:17:32.205Z_

<details><summary>↩ Tool result · `toolu_016jCiXRmv4V3P6hZpsMwH34`</summary>

```text
Web search results for query: "DeepSeek R1 reinforcement learning reasoning verification 2025 paper"

Links: [{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature · HUMAN TECHNOLOGY eXCELLENCE","url":"https://ht-x.com/en/posts/2025/09/deepseek-r1-incentivizes-reasoning-in-llms-through/"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2501.12948"},{"title":"DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning · Pablo Stafforini","url":"https://stafforini.com/works/deepseek-ai-2025-deepseek-r-1-incentivizing/"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12443585/"},{"title":"Paper Summary: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://queirozf.com/entries/paper-summary-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"Paper page - DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://huggingface.co/papers/2501.12948"}]

I've found comprehensive information about the DeepSeek R1 paper on reinforcement learning and reasoning. Here are the key findings:

## Paper Overview

The paper is titled "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" and was published in 2025 with the arXiv identifier 2501.12948. It was later published in Nature on September 17, 2025.

## Main Research Focus

The research demonstrates that reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation.

## Key Models

The paper introduces two first-generation reasoning models: DeepSeek-R1-Zero and DeepSeek-R1, where DeepSeek-R1-Zero is trained via large-scale reinforcement learning without supervised fine-tuning as a preliminary step. While DeepSeek-R1-Zero encounters challenges such as endless repetition, poor readability, and language mixing, DeepSeek-R1 addresses these issues by incorporating cold-start data before RL.

## Performance

DeepSeek-R1 achieves performance comparable to OpenAI-o1 across math, code, and reasoning tasks.

## Verification Approach

The training data for RL is generated by sampling the model to create math and code problems (which can be verified automatically with a math solver or a compiler), with the reward given by the verifier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7ac7943-5853-485b-b975-ade949fbda40",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "702167e9-c9ea-45f0-874e-c6f948723bbf",
  "sourceToolAssistantUUID": "a7ac7943-5853-485b-b975-ade949fbda40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-28T10:17:32.386Z_

<details><summary>↩ Tool result · `toolu_01UNAYgEGAVTxVo5yAQfKsai`</summary>

```text
Web search results for query: ""adaptive verification" "compute allocation" LLM reasoning inference-time 2024 2025"

Links: [{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853v1"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/html/2602.03975v1"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"A Survey of Adaptive and Controllable Test-Time Compute ...","url":"https://arxiv.org/pdf/2507.02076"},{"title":"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation","url":"https://arxiv.org/html/2410.02725v1"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/pdf/2602.01070"}]

I found several highly relevant research papers on adaptive test-time compute allocation for LLM reasoning. Here are the key findings:

## Overview of Adaptive Verification and Compute Allocation

Test-time compute (TTC) methods aim to improve LLM reasoning by allocating additional computation at inference time. A two-tiered taxonomy distinguishes between L1 controllability—methods that operate under fixed compute budgets—and L2 adaptiveness—methods that dynamically scale inference based on input difficulty or model confidence.

## Recent Research (2024-2025)

Recent progress in LLM reasoning increasingly relies on test-time computation: rather than emitting a single completion, systems sample multiple candidates, branch over intermediate steps, and apply explicit selection or verification to filter errors before committing to an answer.

A key challenge is efficiency. As the number of branches and checks increases, verification often becomes the dominant marginal cost because it requires additional model calls.

## Practical Implementation

Recent large reasoning models have the ability to control the amount of thinking (computation) allocated at inference time, with the o-series supporting a "reasoning effort" parameter that can be set to low, medium, or high to control the amount computation a user wants the model to spend.

## Specific Methods

Notable papers include:
- Research showing that scaling LLM test-time compute optimally can be more effective than scaling model parameters, presented at ICLR 2025
- Work introducing capability-aware self-evaluation, which allows a model to understand its own generation capability to enable dynamic allocation of computational resources during test-time inference
- A method that achieves higher accuracy than best-of-N, majority voting, and beam search while using 44% fewer verifier calls on the MATH benchmark


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0291a4a2-8c0c-4146-aa60-66a87c845950",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "4a38e69e-91a5-4022-8d70-9b4d9cdd4436",
  "sourceToolAssistantUUID": "0291a4a2-8c0c-4146-aa60-66a87c845950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-28T10:17:33.105Z_

<details><summary>↩ Tool result · `toolu_01Sf2pqYFGk53eceFiBN3336`</summary>

```text
Web search results for query: ""token-level reward" "step-level reward" process reward model granularity comparison 2024 2025"

Links: [{"title":"Token-Level Reward Model Overview","url":"https://www.emergentmind.com/topics/token-level-reward-model"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"The Revolution of Token-Level Rewards - LevroAI","url":"https://www.levroai.com/blog/revolution-of-token-rewards-08-01-2025"},{"title":"Discriminative Policy Optimization for Token-Level Reward Models","url":"https://arxiv.org/html/2505.23363"},{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"},{"title":"[2505.23363] Discriminative Policy Optimization for Token-Level Reward Models","url":"https://arxiv.org/abs/2505.23363"},{"title":"Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards","url":"https://arxiv.org/html/2604.17957"}]

Based on the search results, here's a comprehensive overview of token-level and step-level rewards in process reward models:

## Key Differences in Granularity

Token-level PRMs operate at a finer granularity, assigning rewards to individual tokens, which allows for continuous feedback throughout the reasoning trajectory, while step-level PRMs provide more granular reward signals compared to sequence-level approaches.

## Comparative Advantages

Token-level rewards provide more precise learning signals, especially in long or structured outputs, reducing gradient variance and accelerating convergence. However, process supervision faced significant hurdles for LLMs in that it was difficult to consistently define what a "step" meant within complex, varied outputs.

## Recent Advances (2024-2025)

Recent efforts have advanced PRMs from step-level to token-level granularity by integrating reward modeling into the training of generative models, with reward scores derived from token generation probabilities. Additionally, PRMs address issues by delivering step-level (and, in recent work, token-level) reward signals.

The effectiveness of PRMs depends on the quality of the step-level (or token-level) supervision signal, choice of reward granularity, and the fidelity of process annotations.

The research landscape shows a clear trend toward finer-grained token-level rewards as a superior alternative to coarser step-level approaches, though both represent meaningful improvements over traditional outcome reward models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9706752b-2f67-4e3d-9749-7afe30919906",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "852dfec1-3bab-4c05-9b19-8f7575536ace",
  "sourceToolAssistantUUID": "9706752b-2f67-4e3d-9749-7afe30919906",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-28T10:17:36.282Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014wB7RNmx6agk4EU9p2XLbG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.12948",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "852dfec1-3bab-4c05-9b19-8f7575536ace",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo46qGgE7Cy3DnkRPre",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7785311-2d67-464b-920e-bb6c73cd8e6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VXeWiiGNwt6xo8mZKBDuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 26700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 80 · 2026-05-28T10:17:36.758Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PSej6czPnozu4fsyYn2Hf1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.02725",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7785311-2d67-464b-920e-bb6c73cd8e6a",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo46qGgE7Cy3DnkRPre",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1da7d21-5720-4eae-8770-7751bcb262b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VXeWiiGNwt6xo8mZKBDuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 26700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 81 · 2026-05-28T10:17:37.290Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H6FN5jgFHCq1vT4fA264EK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.01070",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1da7d21-5720-4eae-8770-7751bcb262b1",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo46qGgE7Cy3DnkRPre",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "032c5650-5671-4d85-89e7-57754c4ab56c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VXeWiiGNwt6xo8mZKBDuN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 26700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 82 · 2026-05-28T10:17:37.942Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EgTKj2XkkHqE1QNxbYZTS3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.02008",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "032c5650-5671-4d85-89e7-57754c4ab56c",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo46qGgE7Cy3DnkRPre",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5526c78f-d62f-4abe-a122-2f4ff8123bdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VXeWiiGNwt6xo8mZKBDuN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 26700,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 349,
          "cache_read_input_tokens": 26700,
          "cache_creation_input_tokens": 2673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2673,
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

_source line 83 · 2026-05-28T10:17:41.287Z_

<details><summary>↩ Tool result · `toolu_014wB7RNmx6agk4EU9p2XLbG`</summary>

```text
# Paper Details

**Full Title:** "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"

**Publication Venue:** Nature, volume 645, pages 633-638 (2025)

**Authors:** DeepSeek-AI and 199 co-authors, including Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, and numerous additional contributors.

**Abstract:**

The paper addresses reasoning capabilities in large language models through reinforcement learning rather than supervised learning. Key findings include:

- The researchers demonstrate that LLM reasoning abilities can be developed "through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories"
- The RL approach enables emergent behaviors including "self-reflection, verification, and dynamic strategy adaptation"
- Models trained this way achieve superior performance on "verifiable tasks such as mathematics, coding competitions, and STEM fields" compared to supervised alternatives
- The reasoning patterns learned can be applied to improve smaller models' capabilities
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7785311-2d67-464b-920e-bb6c73cd8e6a",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "8b8be9c6-de10-4db7-8d14-90331139eeb0",
  "sourceToolAssistantUUID": "a7785311-2d67-464b-920e-bb6c73cd8e6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-28T10:17:41.405Z_

<details><summary>↩ Tool result · `toolu_01PSej6czPnozu4fsyYn2Hf1`</summary>

```text
# Paper Information

**Full Title:**
"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation"

**Authors:**
- Rohin Manvi
- Anikait Singh
- Stefano Ermon

**Publication Venue:**
arXiv:2410.02725 (Computer Science > Computation and Language), submitted October 3, 2024

**Abstract:**
The researchers propose a method enabling language models to assess during generation whether restarting would produce superior results. Rather than requiring external reward models, their "generative self-evaluation scheme" allows predictions via a single token. Testing with Llama 3.1 8B showed substantial gains: AlpacaEval win rate against GPT-4 increased from 21% to 34% using 16 samples, while GSM8K math performance improved from 84% to 91%. By sampling selectively based on model confidence, they achieved "74% of the improvement from using 16 samples" with merely 1.2 average samples, and demonstrated pruning 50-75% of samples with minimal performance loss.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1da7d21-5720-4eae-8770-7751bcb262b1",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "75568b25-f95d-4db1-b784-6a704a6ab45b",
  "sourceToolAssistantUUID": "b1da7d21-5720-4eae-8770-7751bcb262b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-28T10:17:42.058Z_

<details><summary>↩ Tool result · `toolu_01EgTKj2XkkHqE1QNxbYZTS3`</summary>

```text
# Paper Information

**Full Title:** "The Art of Scaling Test-Time Compute for Large Language Models"

**Authors:** Aradhye Agarwal, Ayan Sengupta, Tanmoy Chakraborty

**Publication Venue:** arXiv (Computer Science > Computation and Language)

**Complete Abstract:**

The paper investigates test-time scaling—dynamically allocating computational resources during model inference—as a method for enhancing reasoning capabilities in large language models. The authors conducted an extensive empirical evaluation spanning over thirty billion generated tokens using eight open-source models ranging from 7B to 235B parameters across four reasoning benchmarks. 

Their key findings indicate that: (1) no single test-time scaling strategy consistently outperforms others across all scenarios; (2) reasoning models demonstrate distinct performance patterns correlated with problem difficulty and sequence length, falling into distinct categories; and (3) optimal performance scales monotonically with increased compute resources for a given model type. Based on these observations, the researchers provide practical guidance for selecting appropriate test-time scaling strategies, accounting for problem difficulty, model characteristics, and available computational budgets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5526c78f-d62f-4abe-a122-2f4ff8123bdc",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "cf988e06-d21b-424e-b6fe-79b0ae6a4774",
  "sourceToolAssistantUUID": "5526c78f-d62f-4abe-a122-2f4ff8123bdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-28T10:17:43.102Z_

<details><summary>↩ Tool result · `toolu_01H6FN5jgFHCq1vT4fA264EK`</summary>

```text
# Paper Information

**Full Title:** "What If We Allocate Test-Time Compute Adaptively?"

**Authors:** Ahsan Bilal, Ahmed Mohsin, Muhammad Umer, Ali Subhan, Hassan Rizwan, Ayesha Mohsin, Dean Hougen

**Publication Venue:** arXiv (cs.CL - Computation and Language)

**Complete Abstract:**

The authors propose a verifier-guided adaptive framework that dynamically allocates inference computation, in contrast to traditional uniform test-time scaling approaches. Their system treats reasoning as "iterative trajectory generation and selection," running multiple inference iterations per problem. Within each iteration, the agent produces planning steps, selects reasoning tools and compute strategies, then generates candidate reasoning trajectories.

A process reward model (PRM) serves as the central control mechanism, guiding pruning and expansion during generation at the step level, and enabling trajectory selection across iterations. The framework demonstrates consistent improvements over direct test-time scaling, with particularly strong results on MATH-500, AIME24, and AMO-Bench benchmarks. The authors characterize efficiency using theoretical FLOPs and a compute intensity metric, showing that "verification-guided allocation concentrates computation on high-utility reasoning paths."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "032c5650-5671-4d85-89e7-57754c4ab56c",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "684ec893-a9f8-4506-b6f3-aa48d33368a2",
  "sourceToolAssistantUUID": "032c5650-5671-4d85-89e7-57754c4ab56c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-28T10:17:46.298Z_

Now let me search for a couple more highly-cited papers in this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "684ec893-a9f8-4506-b6f3-aa48d33368a2",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo4qbGhqibCQVhvnFc5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "935aa523-6d04-444e-995c-989848727560",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFk3HbMNwm8NwJo2LCsp4Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 1199,
      "cache_read_input_tokens": 29373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1199,
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

_source line 88 · 2026-05-28T10:17:47.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y59RKA6H4pzxjrBa3Da7g7`</summary>

```json
{
  "query": "\"What Are Step-Level Reward Models Rewarding\" AAAI 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "935aa523-6d04-444e-995c-989848727560",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo4qbGhqibCQVhvnFc5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ed91057-34bb-4d2d-86a3-5dec8c9424d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFk3HbMNwm8NwJo2LCsp4Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 1199,
      "cache_read_input_tokens": 29373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1199,
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

_source line 89 · 2026-05-28T10:17:47.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P2aYqMdx6xtmC696gCLhiW`</summary>

```json
{
  "query": "STILL-2 \"slow thinking\" LLM inference time scaling reward model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ed91057-34bb-4d2d-86a3-5dec8c9424d7",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo4qbGhqibCQVhvnFc5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfbf5a52-5a43-461f-a4d4-c86f90c28f6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFk3HbMNwm8NwJo2LCsp4Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 1199,
      "cache_read_input_tokens": 29373,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1199
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 279,
          "output_tokens": 144,
          "cache_read_input_tokens": 29373,
          "cache_creation_input_tokens": 1199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1199,
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

_source line 90 · 2026-05-28T10:17:54.029Z_

<details><summary>↩ Tool result · `toolu_01Y59RKA6H4pzxjrBa3Da7g7`</summary>

```text
Web search results for query: ""What Are Step-Level Reward Models Rewarding" AAAI 2025 paper"

Links: [{"title":"What Are Step-Level Reward Models Rewarding?","url":"https://arxiv.org/pdf/2412.15904v2"},{"title":"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34663"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241215904M/abstract"},{"title":"What are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-boosted Mathematical Reasoning","url":"https://arxiv.org/html/2412.15904v1"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"[2412.15904] What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning","url":"https://arxiv.org/abs/2412.15904"},{"title":"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings   from MCTS-Boosted Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.15904"},{"title":"What Are Step-Level Reward Models Rewarding?","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34663/36818"}]

I found the paper for you! Here are the details:

"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning" was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 39(23), 24812-24820.

**Key Findings:**

Step-level reward models (SRMs) can significantly enhance mathematical reasoning performance through process supervision or step-level preference alignment based on reinforcement learning. 

The paper's main discoveries include:

- The removal of natural language descriptions of thought processes has minimal impact on the efficacy of SRMs
- SRMs are adept at assessing the complex logical coherence present in mathematical language while having difficulty in natural language

These insights provide a nuanced understanding of the core elements that drive effective step-level reward modeling in mathematical reasoning, offering valuable guidance for developing more efficient and streamlined SRMs by focusing on the crucial parts of mathematical reasoning.

You can access the full paper on arXiv (https://arxiv.org/abs/2412.15904) or through the AAAI proceedings (https://ojs.aaai.org/index.php/AAAI/article/view/34663).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ed91057-34bb-4d2d-86a3-5dec8c9424d7",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "51c3c17f-4a5b-430a-9ef2-a47e67b88a6f",
  "sourceToolAssistantUUID": "5ed91057-34bb-4d2d-86a3-5dec8c9424d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-28T10:17:56.651Z_

<details><summary>↩ Tool result · `toolu_01P2aYqMdx6xtmC696gCLhiW`</summary>

```text
Web search results for query: "STILL-2 "slow thinking" LLM inference time scaling reward model 2025"

Links: [{"title":"GitHub - RUCAIBox/Slow_Thinking_with_LLMs: A series of technical report on Slow Thinking with LLM · GitHub","url":"https://github.com/RUCAIBox/Slow_Thinking_with_LLMs"},{"title":"A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning and Inference-time Scaling Law","url":"https://arxiv.org/html/2505.02665v2"},{"title":"A survey of slow thinking-based reasoning LLMs using reinforcement learning and test-time scaling law - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325003358"},{"title":"[2505.02665] A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning and Inference-time Scaling Law","url":"https://arxiv.org/abs/2505.02665"},{"title":"Inference-Time Scaling for Generalist Reward Modeling","url":"https://arxiv.org/html/2504.02495v3"},{"title":"Demystifying LLM-as-a-Judge: Analytically Tractable Model for Inference-Time Scaling","url":"https://arxiv.org/pdf/2512.19905"},{"title":"A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning   and Inference-time Scaling Law","url":"https://arxiv.org/pdf/2505.02665"}]

Based on the search results, here's what I found about STILL-2 and related topics:

## STILL-2

STILL-2 is a slow-thinking reasoning system announced in December 2024 that achieved competitive performance compared to industry-level reasoning systems on various benchmarks. The project released a technical report presenting details about the reproduction.

## Slow Thinking and LLM Inference-Time Scaling

The broader research field encompasses several key methodologies:

Methods are categorized into three areas: (1) test-time scaling that dynamically adjusts computation based on task complexity via search and sampling; (2) reinforced learning that refines decision-making through iterative improvement leveraging policy networks, reward models, and self-evolution strategies; and (3) slow-thinking frameworks like long chain-of-thought and hierarchical processes.

Recent innovations such as OpenAI's o1 and Deepseek R1 exemplify this paradigm by leveraging principles of test-time computation scaling to dynamically allocate computational resources during task execution.

## Reward Models for Inference-Time Scaling

Reward modeling is a crucial component in reinforcement learning, essential for generating accurate reward signals for LLM responses. Current studies show that with high-quality and robust rewards in either training or inference time, LLMs can achieve strong performance in specific domains.

The research in this area has been very active in 2025, with multiple surveys and technical papers examining how slow thinking, inference-time scaling, and reward models work together in modern reasoning LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfbf5a52-5a43-461f-a4d4-c86f90c28f6d",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "15e01078-d6d2-49d9-9798-6b3d96bd1b38",
  "sourceToolAssistantUUID": "bfbf5a52-5a43-461f-a4d4-c86f90c28f6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-28T10:17:59.763Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KiqZktrnH8vJRWaQdkCxWX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.15904",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15e01078-d6d2-49d9-9798-6b3d96bd1b38",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo5rBGPH2LYtTsXoebn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19781f1a-c9cb-463a-a325-b2865788e0e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmbDZ8CRJqfJHQyUkVMSde",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2051,
      "cache_read_input_tokens": 30572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2051,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 93 · 2026-05-28T10:18:00.174Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012AHUKHvXbesJoEoM5rZUJA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.02495",
  "prompt": "Extract the full title, all authors, publication venue, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19781f1a-c9cb-463a-a325-b2865788e0e9",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo5rBGPH2LYtTsXoebn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3717db0c-d270-4830-ac6b-cf071593489d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmbDZ8CRJqfJHQyUkVMSde",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2051,
      "cache_read_input_tokens": 30572,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2051
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 30572,
          "cache_creation_input_tokens": 2051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2051,
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

_source line 94 · 2026-05-28T10:18:04.816Z_

<details><summary>↩ Tool result · `toolu_012AHUKHvXbesJoEoM5rZUJA`</summary>

```text
# Paper Information

**Title:** "Inference-Time Scaling for Generalist Reward Modeling"

**Authors:** Zijun Liu, Peiyi Wang, Runxin Xu, Shirong Ma, Chong Ruan, Peng Li, Yang Liu, Yu Wu

**Publication Venue:** arXiv (cs.CL - Computation and Language); preprint under review

**Abstract:** 

This work addresses how to enhance reward modeling systems through increased computational resources during inference for general queries. The researchers adopt pointwise generative reward modeling to accommodate diverse input types and enable inference-time scalability. They introduce "Self-Principled Critique Tuning (SPCT)" via online reinforcement learning to develop scalable reward generation behaviors, creating the DeepSeek-GRM models. The approach combines parallel sampling with a meta reward model to optimize voting outcomes. Results demonstrate that SPCT substantially improves quality and scalability across various benchmarks, achieving "better performance compared to training-time scaling" while avoiding notable biases. The authors acknowledge some remaining limitations and have released their models publicly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3717db0c-d270-4830-ac6b-cf071593489d",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "91688bb2-adf8-4f15-8496-b58fcd565477",
  "sourceToolAssistantUUID": "3717db0c-d270-4830-ac6b-cf071593489d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-28T10:18:04.971Z_

<details><summary>↩ Tool result · `toolu_01KiqZktrnH8vJRWaQdkCxWX`</summary>

```text
# Paper Information

**Full Title:**
"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning"

**Authors:**
Yiran Ma, Zui Chen, Tianqiao Liu, Mi Tian, Zhuo Liu, Zitao Liu, Weiqi Luo

**Publication Venue:**
AAAI 2025

**Complete Abstract:**
Step-level reward models enhance mathematical reasoning through process supervision or step-level preference alignment using reinforcement learning. While recent AlphaZero-like methods employing Monte Carlo Tree Search for automatic annotation have proven effective, the underlying mechanisms remain poorly understood. This investigation reveals surprising findings: removing natural language descriptions of thought processes has negligible impact on step-level reward model performance. Additionally, these models excel at evaluating logical coherence in mathematical language but struggle with natural language. These insights offer guidance for developing more efficient reward models by emphasizing crucial mathematical reasoning components rather than extraneous elements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19781f1a-c9cb-463a-a325-b2865788e0e9",
  "isSidechain": true,
  "promptId": "652e70e0-0c9f-4ff9-9fb0-1842c84410b3",
  "agentId": "a042bbe02a929caec",
  "type": "user",
  "uuid": "79f55ffe-1f1f-443a-828c-89e75a37f28c",
  "sourceToolAssistantUUID": "19781f1a-c9cb-463a-a325-b2865788e0e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-28T10:19:47.284Z_

Now I have comprehensive data. Let me compile the final report.

---

## Literature Survey: Adaptive Verification Strategies for LLM Inference (2024--2026)

Below are the most important papers organized thematically. For each paper I provide the full title, lead author, venue, URL, importance rationale, and a one-line summary.

---

### 1. FOUNDATIONAL WORK: Process vs. Outcome Supervision

**"Let's Verify Step by Step"**
- **Authors:** Lightman et al. (OpenAI)
- **Venue:** ICLR 2024 (originally arXiv May 2023)
- **URL:** https://arxiv.org/abs/2305.20050
- **Why important:** Seminal paper that formalized process supervision as superior to outcome supervision; released the PRM800K dataset (800K step-level human annotations) that became the standard training/evaluation resource for subsequent PRM research.
- **Summary:** Demonstrates that process reward models providing step-level feedback substantially outperform outcome reward models on MATH, achieving 78% solve rate, and that active learning further enhances process supervision.

---

### 2. GENERATIVE VERIFICATION PARADIGM

**"Generative Verifiers: Reward Modeling as Next-Token Prediction"**
- **Authors:** Zhang et al. (Google DeepMind)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2408.15240
- **Why important:** Introduced the GenRM paradigm -- recasting verification as generation rather than classification -- which became the foundation for subsequent generative reward model research (ThinkPRM, GenPRM, DeepSeek-GRM). Published at a top venue.
- **Summary:** By training verifiers jointly on verification and solution generation using next-token prediction and chain-of-thought reasoning, GenRM achieves massive gains (e.g., 73% to 93.4% on GSM8K) and scales favorably with model size.

**"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"**
- **Authors:** Zhao et al.
- **Venue:** arXiv, April 2025
- **URL:** https://arxiv.org/abs/2504.00891
- **Why important:** Bridges process supervision and generative critic models; shows that a 1.5B generative PRM can surpass GPT-4o on ProcessBench using only 23K training examples, demonstrating extreme data efficiency.
- **Summary:** GenPRM performs explicit chain-of-thought reasoning with code verification to evaluate reasoning steps, addressing weak generalization and lack of test-time compute scaling in existing PRMs.

**"Process Reward Models That Think" (ThinkPRM)**
- **Authors:** Khalifa et al. (including Rishabh Agarwal)
- **Venue:** arXiv, April 2025
- **URL:** https://arxiv.org/abs/2504.16828
- **Why important:** Shows that generative verification chains can replace expensive step-level annotation -- ThinkPRM needs only 1% of PRM800K labels while outperforming discriminative verifiers, with strong out-of-domain transfer (8% gain on GPQA-Diamond).
- **Summary:** Introduces a generative process reward model that produces verification chains-of-thought, achieving superior performance with minimal supervision and efficient test-time compute scaling.

**"Inference-Time Scaling for Generalist Reward Modeling" (DeepSeek-GRM)**
- **Authors:** Liu et al. (DeepSeek)
- **Venue:** arXiv, April 2025 (under review)
- **URL:** https://arxiv.org/abs/2504.02495
- **Why important:** Extends generative reward modeling to general (non-math) queries; introduces Self-Principled Critique Tuning (SPCT) via online RL, showing inference-time scaling of reward models outperforms training-time scaling.
- **Summary:** Develops generalist generative reward models via SPCT that scale reward quality at inference time through parallel sampling and meta-RM aggregation, outperforming training-time scaling approaches.

---

### 3. AUTOMATED PROCESS SUPERVISION DATA COLLECTION

**"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"**
- **Authors:** Wang et al.
- **Venue:** ACL 2024 (Long Paper)
- **URL:** https://arxiv.org/abs/2312.08935
- **Why important:** Pioneered automatic process annotation for PRM training without human labels, using MCTS-inspired methods. Widely cited and adopted as a baseline in subsequent PRM research.
- **Summary:** Introduces an automatic process-oriented reward model trained on self-generated supervision data, improving Mistral-7B from 77.9% to 84.1% on GSM8K via step-level PPO.

**"Improve Mathematical Reasoning in Language Models by Automated Process Supervision" (OmegaPRM)**
- **Authors:** Luo et al. (Google DeepMind)
- **Venue:** arXiv, June 2024
- **URL:** https://arxiv.org/abs/2406.06592
- **Why important:** Introduced the divide-and-conquer MCTS algorithm OmegaPRM for scalable, fully automated collection of process supervision data (1.5M+ annotations without human intervention).
- **Summary:** OmegaPRM uses Monte Carlo Tree Search with binary search for error localization to automatically generate high-quality process supervision data, boosting Gemini Pro from 51% to 69.4% on MATH.

**"FoVer: Generalizable Process Reward Models via Formally Verified Training Data"**
- **Authors:** Kamoi et al.
- **Venue:** ACL 2026 Findings
- **URL:** https://arxiv.org/abs/2505.15960
- **Why important:** Uses formal verification tools (Z3, Isabelle) to synthesize PRM training data with provably correct step-level labels, showing transfer to informal NL reasoning tasks across 12 benchmarks.
- **Summary:** Synthesizes PRM training data from formal reasoning tasks using formal verification tools, demonstrating that models fine-tuned on this data generalize to informal natural language reasoning benchmarks.

---

### 4. TEST-TIME COMPUTE SCALING AND ADAPTIVE ALLOCATION

**"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"**
- **Authors:** Snell et al. (Google DeepMind)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2408.03314
- **Why important:** Foundational paper on compute-optimal test-time scaling. Demonstrated that a smaller model with optimal test-time compute allocation can outperform a 14x larger model, using process-based verifiers and adaptive response distribution updating. Published at ICLR 2025.
- **Summary:** Proposes compute-optimal test-time allocation that dynamically distributes inference resources per prompt, achieving 4x+ efficiency over uniform baselines with strategy effectiveness varying by problem difficulty.

**"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"**
- **Authors:** Liu et al.
- **Venue:** arXiv, February 2025
- **URL:** https://arxiv.org/abs/2502.06703
- **Why important:** Provides systematic analysis of how policy model choice, PRM quality, and problem difficulty interact to determine optimal test-time scaling strategy. Demonstrates extreme scaling results (1B surpassing 405B).
- **Summary:** Shows that the optimal test-time scaling strategy is highly dependent on the interplay of policy model, PRM, and problem difficulty, with smaller models potentially surpassing GPT-4o under optimized compute allocation.

**"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning"**
- **Authors:** Setlur et al. (Google DeepMind)
- **Venue:** arXiv, October 2024
- **URL:** https://arxiv.org/abs/2410.08146
- **Why important:** Introduces the key design principle that process rewards should measure "progress" (change in likelihood of future correctness), yielding 8%+ accuracy gains over ORMs and 1.5-5x compute efficiency improvement.
- **Summary:** Defines process rewards as measuring progress toward correct answers and trains process advantage verifiers that achieve superior accuracy and 5-6x sample efficiency gains over outcome-based methods.

**"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation"**
- **Authors:** Manvi et al. (Stanford)
- **Venue:** arXiv, October 2024
- **URL:** https://arxiv.org/abs/2410.02725
- **Why important:** Proposes self-evaluation for adaptive compute without external reward models -- the model itself predicts whether restarting generation would help, achieving 74% of best-of-16 gains with only 1.2 average samples.
- **Summary:** Enables LLMs to self-evaluate mid-generation and adaptively decide whether to restart, achieving efficient best-of-N gains with minimal samples through a single-token confidence prediction scheme.

**"What If We Allocate Test-Time Compute Adaptively?"**
- **Authors:** Bilal et al.
- **Venue:** arXiv, February 2025
- **URL:** https://arxiv.org/abs/2602.01070
- **Why important:** Proposes a PRM-guided adaptive framework that dynamically allocates compute via iterative trajectory generation, with the PRM controlling pruning, expansion, and selection at step level.
- **Summary:** Introduces a verifier-guided adaptive framework using PRMs to dynamically allocate inference computation, concentrating resources on high-utility reasoning paths across iterative trajectory generation.

**"The Art of Scaling Test-Time Compute for Large Language Models"**
- **Authors:** Agarwal et al.
- **Venue:** arXiv, December 2025
- **URL:** https://arxiv.org/abs/2512.02008
- **Why important:** Largest empirical study (30B+ tokens, 8 models, 7B-235B) establishing that no single test-time scaling strategy is universally optimal -- effectiveness depends on problem difficulty, model type, and compute budget.
- **Summary:** Comprehensive empirical study demonstrating that no single test-time scaling strategy dominates, with optimal strategy selection depending on the interaction of problem difficulty, model characteristics, and compute budget.

---

### 5. BEST-OF-N SAMPLING AND SELECTION IMPROVEMENTS

**"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment"**
- **Authors:** Huang et al.
- **Venue:** ICML 2025 (PMLR Vol. 267)
- **URL:** https://proceedings.mlr.press/v267/huang25c.html
- **Why important:** Provides rigorous theoretical analysis showing best-of-N provably suffers from reward hacking at large N. Introduces InferenceTimePessimism algorithm that is both optimal and scaling-monotonic. Published at ICML 2025.
- **Summary:** Proves best-of-N sampling degrades under reward hacking at large N and introduces a pessimism-based algorithm that achieves optimal, monotonically scaling performance without reward hacking.

**"Scalable Best-of-N Selection for Large Language Models via Self-Certainty"**
- **Authors:** Kang et al. (UC Berkeley)
- **Venue:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2502.18581
- **Why important:** Eliminates the need for external reward models entirely by using distributional self-certainty from the LLM's own output probabilities for best-of-N selection. Published at NeurIPS 2025.
- **Summary:** Proposes self-certainty -- using a model's own output probability distributions to assess response quality -- as a computationally efficient reward-model-free alternative for best-of-N selection.

---

### 6. PROGRAMMATIC AND COLLABORATIVE VERIFICATION

**"Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning" (PROVE)**
- **Authors:** Toh et al.
- **Venue:** arXiv, October 2024
- **URL:** https://arxiv.org/abs/2410.12608
- **Why important:** Introduces program-based verification as a filter before majority voting, converting NL solutions to executable programs. Achieves up to 18% gain on GSM8K across 13 models.
- **Summary:** Converts natural language math solutions to executable programs for verification, filtering unreliable reasoning paths before majority voting to achieve consistent improvements across 13 open-source models.

**"Improving LLM Reasoning through Scaling Inference Computation with Collaborative Verification"**
- **Authors:** Liang et al.
- **Venue:** arXiv, October 2024
- **URL:** https://arxiv.org/abs/2410.05318
- **Why important:** Introduces collaborative verification integrating Chain-of-Thought (human-readable reasoning) and Program-of-Thought (executable validation), with resulting verifiers outperforming GPT-4o.
- **Summary:** Proposes collaborative CoT+PoT verification combining step-by-step reasoning with executable program validation, training verifiers that outperform GPT-4o when paired with Qwen-72B-Instruct.

---

### 7. UNDERSTANDING AND ANALYZING REWARD MODELS

**"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning"**
- **Authors:** Ma et al.
- **Venue:** AAAI 2025
- **URL:** https://arxiv.org/abs/2412.15904
- **Why important:** Reveals that step-level reward models primarily evaluate mathematical language coherence rather than natural language thought descriptions -- removing NL thought processes has negligible impact. Important for understanding what PRMs actually learn.
- **Summary:** Discovers that step-level reward models excel at assessing mathematical logical coherence but are largely indifferent to natural language descriptions of reasoning processes.

**"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning" (CRM)**
- **Authors:** Zhang et al.
- **Venue:** arXiv, September 2025
- **URL:** https://arxiv.org/abs/2509.26578
- **Why important:** Addresses the disconnect between step-level rewards and outcome quality by conditioning step rewards on the final outcome, improving credit assignment and robustness to reward hacking.
- **Summary:** Frames LLM reasoning as a temporal process where step rewards are conditioned on both preceding steps and final outcomes, yielding more robust reward signals resistant to reward hacking.

**"Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning"**
- **Authors:** Pronesti et al.
- **Venue:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.17223
- **Why important:** Proposes deterministic, rule-based verifiers for intermediate steps (instead of neural judges) to address interpretability and reward hacking concerns, achieving 20% higher F1 than SOTA.
- **Summary:** Introduces deterministic rule-based verifiers for intermediate reasoning steps instead of neural scoring, achieving 20% higher F1 and substantially improved logical coherence in domain-specific reasoning.

---

### 8. REINFORCEMENT LEARNING WITH VERIFIABLE REWARDS

**"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"**
- **Authors:** DeepSeek-AI (Guo et al.)
- **Venue:** Nature, 2025 (vol. 645, pp. 633-638)
- **URL:** https://arxiv.org/abs/2501.12948
- **Why important:** Landmark paper showing that pure RL with verifiable rewards (math solvers, compilers) -- without human-labeled reasoning trajectories -- can produce reasoning capabilities matching OpenAI o1. Emergent behaviors include self-verification. Published in Nature.
- **Summary:** Demonstrates that pure reinforcement learning with verifiable rewards incentivizes emergent reasoning behaviors including self-reflection and verification, achieving performance comparable to o1 on math, code, and STEM tasks.

---

### 9. SURVEYS

**"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models"**
- **Authors:** Zheng et al.
- **Venue:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.08049
- **Why important:** Most comprehensive survey of the PRM landscape, covering data generation, model construction, and downstream applications across math, code, multimodal, robotics, and agents.
- **Summary:** Comprehensive survey covering the complete PRM workflow from process-level data generation to model construction and applications across mathematics, programming, multimodal reasoning, and robotics.

**"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation"**
- **Authors:** Pan et al.
- **Venue:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.09305
- **Why important:** Introduces the RARL (Reasoning-Aligned Reinforcement Learning) framework organizing reward approaches for multi-step reasoning, with systematic treatment of reward hacking and benchmark vulnerabilities.
- **Summary:** Introduces a taxonomy of reward mechanisms for LLM reasoning via the RARL framework, analyzing reward hacking failure modes and benchmark vulnerabilities to guide development of trustworthy reasoning models.

---

### 10. BENCHMARKS

**"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math"**
- **Authors:** Pandit et al. (Salesforce)
- **Venue:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.13744
- **Why important:** Provides a human-annotated (500+ hours) benchmark for evaluating step-level verifiers on frontier-level math, revealing that most open-source verifiers significantly lag behind closed-source models.
- **Summary:** Introduces a human-annotated step-level verification benchmark for frontier math, evaluating 29 verification models and revealing significant gaps between open-source and closed-source verifiers.

---

### Key Themes and Takeaways

1. **Generative verification is displacing discriminative verification.** GenRM (ICLR 2025) sparked a line of work (ThinkPRM, GenPRM, DeepSeek-GRM) showing that framing verification as generation -- with chain-of-thought reasoning during verification -- dramatically outperforms scalar classifiers and requires far less training data.

2. **Automated process supervision data is now scalable.** Math-Shepherd (ACL 2024), OmegaPRM (2024), and FoVer (ACL 2026) have eliminated the need for expensive human annotation of step-level labels through MCTS-based and formal-verification-based approaches.

3. **Adaptive test-time compute allocation is critical.** The Snell et al. (ICLR 2025) paper established that compute-optimal allocation per problem outperforms uniform scaling by 4x+. Multiple follow-ups show that no single strategy is universally optimal -- the best approach depends on problem difficulty, model, and PRM quality.

4. **Best-of-N sampling has fundamental limitations.** Huang et al. (ICML 2025) proved that naive best-of-N suffers from reward hacking at scale, motivating pessimism-based and self-certainty-based alternatives (NeurIPS 2025).

5. **Pure RL with verifiable rewards can produce emergent verification.** DeepSeek-R1 (Nature 2025) showed that self-verification emerges as a behavior from RL training, without explicit process supervision.

6. **Verification granularity is evolving.** The field is moving from outcome-level to step-level to token-level reward signals, with generative approaches enabling flexible granularity that adapts to the problem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79f55ffe-1f1f-443a-828c-89e75a37f28c",
  "isSidechain": true,
  "agentId": "a042bbe02a929caec",
  "requestId": "req_011CbUo6TBgkBMHqfBH3QRg7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "739231a5-5c7f-4c46-a065-1feb69e56bbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "ce13dcc4-e61d-429d-b2e8-edb9758de784",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019A3wXzELZp5dQk1pwLXv6x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 274,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 32623,
      "output_tokens": 4885,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 274,
          "output_tokens": 4885,
          "cache_read_input_tokens": 32623,
          "cache_creation_input_tokens": 439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 439,
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
