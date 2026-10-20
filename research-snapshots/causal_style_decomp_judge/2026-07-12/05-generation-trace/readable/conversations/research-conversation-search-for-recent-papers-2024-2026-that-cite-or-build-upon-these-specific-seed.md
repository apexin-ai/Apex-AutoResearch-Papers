# Research conversation: Search for recent papers (2024-2026) that cite or build upon these specific seed papers. For each search, fetch the arxi

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 1
- **Tool calls:** 41
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a083061a3b1788628.jsonl`
- **Structured JSON:** [`840f6201e487c7e3998e.json`](../../sessions/84/840f6201e487c7e3998e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

93 recorded events

### User

_source line 1 · 2026-05-30T06:17:23.262Z_

Search for recent papers (2024-2026) that cite or build upon these specific seed papers. For each search, fetch the arxiv page of any promising result:

1. Search: "TRAQ trustworthy retrieval augmented question answering conformal prediction cited"
2. Search: "C-RAG certified generation risks retrieval augmented ICML 2024 cited by"
3. Search: "PoisonedRAG corpus poisoning defense 2025 2026"
4. Search: "RobustRAG isolate then aggregate retrieval corruption 2025 2026"
5. Search: "conformal prediction exchangeability RAG retrieval 2025 2026"
6. Search: "abstention framework RAG systems guarantees 2025 2026"
7. Search: "nonconformity score retrieval agreement 2025 2026"

For each paper found, use WebFetch to read the abstract. Focus on papers that:
- Extend conformal prediction to adversarial/poisoning settings in RAG
- Provide certified defenses for RAG with formal guarantees
- Study distribution shift or exchangeability violations in conformal prediction for NLP

Return a structured list with: title, authors, venue, URL, why important, one-line summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "957bba68-e8a5-4db3-8dcf-ad5198e91d8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:17:23.265Z_

```json
{
  "parentUuid": "957bba68-e8a5-4db3-8dcf-ad5198e91d8f",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
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
  "uuid": "75dc4b7b-9fa2-4fee-812f-17008b400558",
  "timestamp": "2026-05-30T06:17:23.265Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:17:23.266Z_

```json
{
  "parentUuid": "75dc4b7b-9fa2-4fee-812f-17008b400558",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "56d048bd-460e-406b-9c42-3e5c632df002",
  "timestamp": "2026-05-30T06:17:23.266Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:17:27.677Z_



I'll search for recent papers building on these seed papers. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d048bd-460e-406b-9c42-3e5c632df002",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGMjfCm3V3PngjkdyEF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "984cb060-0f05-4b7d-94c1-42a7ebfea358",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yQ4ButhBaMpx5MatoMBoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1633,
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

_source line 5 · 2026-05-30T06:17:27.962Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GuJ5g5KNdaARpcF2FCZqJW`</summary>

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
  "parentUuid": "984cb060-0f05-4b7d-94c1-42a7ebfea358",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGMjfCm3V3PngjkdyEF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57ab735f-3cec-45a2-971d-d9daca3624e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yQ4ButhBaMpx5MatoMBoE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 7413,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1633
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1633,
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

_source line 6 · 2026-05-30T06:17:27.966Z_

<details><summary>↩ Tool result · `toolu_01GuJ5g5KNdaARpcF2FCZqJW`</summary>

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
  "parentUuid": "57ab735f-3cec-45a2-971d-d9daca3624e0",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "fb433880-7874-4ac1-9c9c-f5650027c30b",
  "sourceToolAssistantUUID": "57ab735f-3cec-45a2-971d-d9daca3624e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:17:30.512Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb433880-7874-4ac1-9c9c-f5650027c30b",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0b78401-67c0-428a-927b-f71a7c0120c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 8 · 2026-05-30T06:17:31.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLKodbEX1gXiCfak4eeKfo`</summary>

```json
{
  "query": "TRAQ trustworthy retrieval augmented question answering conformal prediction cited 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b78401-67c0-428a-927b-f71a7c0120c4",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edfbd6c3-09e0-485e-85c3-2c88983569f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 9 · 2026-05-30T06:17:32.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CsNHu1qQ9zz5nZHTGYcJrD`</summary>

```json
{
  "query": "C-RAG certified generation risks retrieval augmented ICML 2024 cited by 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edfbd6c3-09e0-485e-85c3-2c88983569f0",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "412b6077-78f8-4a97-87d9-a02e92e87736",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 10 · 2026-05-30T06:17:33.345Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014th9dbLf3WeYtkTqnCiP1F`</summary>

```json
{
  "query": "PoisonedRAG corpus poisoning defense 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "412b6077-78f8-4a97-87d9-a02e92e87736",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e09607d7-0f2f-4199-9f17-a7588eab4d93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 11 · 2026-05-30T06:17:33.782Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UaDBGyJcgY5atzPXrTsaYj`</summary>

```json
{
  "query": "RobustRAG isolate then aggregate retrieval corruption 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09607d7-0f2f-4199-9f17-a7588eab4d93",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f49a43f4-a194-427f-8744-df2d9bab2a38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 12 · 2026-05-30T06:17:34.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFbQ9X4iQMbkC5UVjwceJm`</summary>

```json
{
  "query": "conformal prediction exchangeability RAG retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f49a43f4-a194-427f-8744-df2d9bab2a38",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e6876da-bda1-4fdc-a188-4f83e23ada0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 13 · 2026-05-30T06:17:35.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019TnTLzF1xYFZfJMciSJVzH`</summary>

```json
{
  "query": "abstention framework RAG systems guarantees 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6876da-bda1-4fdc-a188-4f83e23ada0c",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d3e637f-20da-4176-95fc-ad82fb522683",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 14 · 2026-05-30T06:17:35.630Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKi7qMmkMaaz5dYtiVjET6`</summary>

```json
{
  "query": "nonconformity score retrieval agreement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d3e637f-20da-4176-95fc-ad82fb522683",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGN5CTA6JRQsTPFRAWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3fdeda8-295c-4d15-8634-422e89ecb427",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpUiARbq56MpQMDTiV34nC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9046,
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

_source line 15 · 2026-05-30T06:17:38.030Z_

<details><summary>↩ Tool result · `toolu_01GLKodbEX1gXiCfak4eeKfo`</summary>

```text
Web search results for query: "TRAQ trustworthy retrieval augmented question answering conformal prediction cited 2025 2026"

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=N-FM_cf9BBXM"},{"title":"[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/abs/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TRAQ:-Trustworthy-Retrieval-Augmented-Question-via-Li-Park/28e078b52a761cf3fe5941d3428acb7bbf608f21"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Request PDF","url":"https://www.researchgate.net/publication/382630302_TRAQ_Trustworthy_Retrieval_Augmented_Question_Answering_via_Conformal_Prediction"}]

Based on the web search results, I found information about TRAQ:

TRAQ (Trustworthy Retrieval Augmented Question Answering) provides the first end-to-end statistical correctness guarantee for RAG. TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.

The paper was published in Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), by authors Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani. TRAQ provides the desired correctness guarantee while reducing prediction set size by 16.2% on average compared to an ablation.

Note: The paper appears to have been originally submitted in 2023 and published in 2024, which falls within your specified timeframe. The search results don't show citations specifically from 2025-2026, but the paper itself is from 2024 and has been cited in subsequent works.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edfbd6c3-09e0-485e-85c3-2c88983569f0",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "a59b5113-8fe7-4eb5-b272-69bdaf028310",
  "sourceToolAssistantUUID": "edfbd6c3-09e0-485e-85c3-2c88983569f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-30T06:17:39.458Z_

<details><summary>↩ Tool result · `toolu_01CsNHu1qQ9zz5nZHTGYcJrD`</summary>

```text
Web search results for query: "C-RAG certified generation risks retrieval augmented ICML 2024 cited by 2025 2026"

Links: [{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models | OpenReview","url":"https://openreview.net/forum?id=FMa4c5NhOe"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240203181K/abstract"},{"title":"GitHub - kangmintong/C-RAG: [ICML 2024] Codes for C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models · GitHub","url":"https://github.com/kangmintong/C-RAG"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/c-rag-certified-generation-risks-for-retrieval-augmented-language/"},{"title":"[2402.03181] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2402.03181"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://proceedings.mlr.press/v235/kang24a.html"},{"title":"C-RAG: Certiﬁed Generation Risks for Retrieval-Augmented Language Models","url":"https://par.nsf.gov/servlets/purl/10524902"},{"title":"ICML Poster C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://icml.cc/virtual/2024/poster/34539"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models","url":"https://arxiv.org/pdf/2402.03181"}]

I found comprehensive information about C-RAG. Here are the key findings:

## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models

C-RAG is the first framework to certify generation risks for RAG models. The paper was published at ICML 2024 on May 2, 2024.

### Overview
The framework provides conformal risk analysis for RAG models and certifies an upper confidence bound of generation risks, referred to as conformal generation risk, and also provides theoretical guarantees on conformal generation risks for general bounded risk functions under test distribution shifts.

### Key Findings
RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial. Intensive empirical results demonstrate the soundness and tightness of the conformal generation risk guarantees across four widely-used NLP datasets on four state-of-the-art retrieval models.

### Authors and Publication Details
The paper was authored by Kang, M., Gürel, N. M., Yu, N., Song, D., & Li, B. (2024) and published in the Proceedings of Machine Learning Research, 235, 22963-23000.

The search results contain the paper details but do not include specific information about citations from 2025-2026. You may want to check Google Scholar, arXiv, or other academic databases for more recent citation metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "412b6077-78f8-4a97-87d9-a02e92e87736",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "5840d3a7-4ee8-4f3c-9086-9f9e06ae6ec5",
  "sourceToolAssistantUUID": "412b6077-78f8-4a97-87d9-a02e92e87736",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:17:41.798Z_

<details><summary>↩ Tool result · `toolu_01UaDBGyJcgY5atzPXrTsaYj`</summary>

```text
Web search results for query: "RobustRAG isolate then aggregate retrieval corruption 2025 2026"

Links: [{"title":"ICML Certifiably Robust RAG against Retrieval Corruption","url":"https://icml.cc/virtual/2024/37487"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"[2405.15556v1] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556v1"},{"title":"Certifiably Robust RAG against Retrieval Corruption | OpenReview","url":"https://openreview.net/forum?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"}]

Based on the search results, here's what I found about RobustRAG:

## Overview

RobustRAG is the first defense framework against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

## Core Strategy: Isolate-Then-Aggregate

The key insight of RobustRAG is an isolate-then-aggregate strategy: we get LLM responses from each passage in isolation and then securely aggregate these isolated responses. More specifically, we isolate passages into disjoint groups, generate LLM responses based on the concatenated passages from each isolated group, and then securely aggregate these responses for a robust output.

## Technical Implementation

To instantiate RobustRAG, we design keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.

## Performance Results

RobustRAG achieves substantial certifiable robustness while maintaining high clean performance, e.g., 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG. Additionally, it reduces attack success rates from over 90% to approximately 10%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f49a43f4-a194-427f-8744-df2d9bab2a38",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "34ce71f3-6088-48fa-b762-3068237c1f4b",
  "sourceToolAssistantUUID": "f49a43f4-a194-427f-8744-df2d9bab2a38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T06:17:42.256Z_

<details><summary>↩ Tool result · `toolu_014th9dbLf3WeYtkTqnCiP1F`</summary>

```text
Web search results for query: "PoisonedRAG corpus poisoning defense 2025 2026"

Links: [{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714756"},{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/pdf/2602.04711"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"}]

Based on the search results, here's what I found about PoisonedRAG and corpus poisoning defenses:

## PoisonedRAG Attack

PoisonedRAG represents the first knowledge database corruption attack specifically designed against RAG systems, accepted to USENIX Security 2025. PoisonedRAG formulates knowledge corruption as an optimization problem with retrieval and generation conditions, achieving 90% attack success on standard QA benchmarks.

The attack is remarkably efficient: injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, while poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.

## Defense Mechanisms

Several defense approaches have been proposed in 2025-2026:

1. **RAGForensics**: RAGForensics is the first traceback system for RAG, designed to identify poisoned texts within the knowledge database that are responsible for the attacks.

2. **RAGPart & RAGMask**: RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.

3. **Sparse Document Attention RAG (SDAG)**: SDAG enforces block-sparse-attention over retrieved documents, with tokens in a retrieved document attending only to previous tokens in the same document; cross-attention between different retrieved documents is disabled.

However, existing defenses have been evaluated and results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e09607d7-0f2f-4199-9f17-a7588eab4d93",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "7de21e7c-d7e6-43be-bb6e-3b382034fd2e",
  "sourceToolAssistantUUID": "e09607d7-0f2f-4199-9f17-a7588eab4d93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:17:42.273Z_

<details><summary>↩ Tool result · `toolu_01SFbQ9X4iQMbkC5UVjwceJm`</summary>

```text
Web search results for query: "conformal prediction exchangeability RAG retrieval 2025 2026"

Links: [{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/html/2511.17908v1"},{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"},{"title":"CONFLARE: CONFormal LArge language model REtrieval","url":"https://arxiv.org/pdf/2404.04287"},{"title":"Conformal prediction beyond exchangeability","url":"https://arxiv.org/pdf/2202.13415"},{"title":"(PDF) Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://www.researchgate.net/publication/397932907_Principled_Context_Engineering_for_RAG_Statistical_Guarantees_via_Conformal_Prediction"},{"title":"Towards Trustworthy Retrieval Augmented Generation for ...","url":"https://arxiv.org/pdf/2502.06872"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"}]

Based on the search results, here's what I found about conformal prediction, exchangeability, and RAG retrieval in 2025-2026:

## Key Recent Work

A 2026 paper titled "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction" was published in ECIR 2026. The research demonstrates context engineering through conformal prediction, a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence.

## Main Findings

Conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval. Conformal prediction enables reliable, coverage-controlled context reduction and provides a lightweight, model-agnostic foundation for scalable RAG.

## Exchangeability Considerations

Future work will explore adaptive recalibration across topics and domains to relax the exchangeability assumption. This acknowledges that while conformal prediction relies on exchangeability assumptions, researchers are exploring ways to extend the approach beyond strict exchangeability requirements in RAG systems.

The search results show active research in applying conformal prediction to RAG retrieval with statistical guarantees, with recent papers addressing practical implementation challenges and planning future extensions to handle non-exchangeable scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e6876da-bda1-4fdc-a188-4f83e23ada0c",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "c248acbf-354e-4139-b1fe-27e6c01e0849",
  "sourceToolAssistantUUID": "8e6876da-bda1-4fdc-a188-4f83e23ada0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:17:42.909Z_

<details><summary>↩ Tool result · `toolu_019TnTLzF1xYFZfJMciSJVzH`</summary>

```text
Web search results for query: "abstention framework RAG systems guarantees 2025 2026"

Links: [{"title":"RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI","url":"https://www.techment.com/blogs/rag-in-2026/"},{"title":"Agentic RAG in 2026: The UK/EU enterprise guide to grounded GenAI — Data Nucleus","url":"https://datanucleus.dev/rag-and-agentic-ai/agentic-rag-enterprise-guide-2026"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"Beyond Component Strength: Synergistic Integration and Adaptive Calibration in Multi-Agent RAG Systems","url":"https://arxiv.org/pdf/2511.21729"},{"title":"KohakuRAG: A simple RAG framework with hierarchical document indexing","url":"https://arxiv.org/pdf/2603.07612"},{"title":"(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI","url":"https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"},{"title":"Top 10 RAG Frameworks on GitHub (By Stars) — January 2026 | by florinelchis | Medium","url":"https://florinelchis.medium.com/top-10-rag-frameworks-on-github-by-stars-january-2026-e6edff1e0d91"},{"title":"The Next Frontier of RAG: How Enterprise Knowledge Systems Will Evolve (2026-2030) - NStarX Inc.","url":"https://nstarxinc.com/blog/the-next-frontier-of-rag-how-enterprise-knowledge-systems-will-evolve-2026-2030/"}]

Based on the search results, here's what I found regarding abstention frameworks in RAG systems for 2025-2026:

## Abstention Framework in Multi-Agent RAG Systems

A recent study demonstrates that when individual enhancements to RAG systems—hybrid retrieval, ensemble verification and adaptive thresholding—are properly integrated, they achieve a 95% reduction in abstention (from 40% to 2%). 

The research reveals a critical measurement challenge: different verification strategies produce identical safe behaviors but inconsistent verdict labels ("abstained" versus "unsupported"), creating apparent hallucination rates that are actually labeling artifacts.

## RAG Systems and Guarantees in 2025-2026

The WattBot 2025 Challenge presents requirements for RAG systems to answer technical questions with ±0.1% numeric tolerance, cite exact source documents, and explicitly abstain when evidence is insufficient.

As of 2025–2026, RAG has moved into a Modular and Agentic phase where modern systems are iterative and self-correcting, with Self-RAG and Corrective RAG (CRAG) allowing models to critique their own retrieved results.

The research emphasizes that building reliable RAG systems requires careful integration of components rather than relying on individual improvements alone, and that explicit abstention mechanisms are becoming a key feature for ensuring trustworthiness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d3e637f-20da-4176-95fc-ad82fb522683",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "66cd1915-2b96-4c4c-9f43-0f6f864ae496",
  "sourceToolAssistantUUID": "9d3e637f-20da-4176-95fc-ad82fb522683",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:17:44.089Z_

<details><summary>↩ Tool result · `toolu_01AKi7qMmkMaaz5dYtiVjET6`</summary>

```text
Web search results for query: "nonconformity score retrieval agreement 2025 2026"

Links: [{"title":"2025-2026 General Assembly HOUSE BILL 378:","url":"https://dashboard.ncleg.gov/api/Services/BillSummary/2025/H378-SMRQ-57(CSRQf-17)-v-9"},{"title":"CPA Exam Score Release: Days & Testing Windows [2026]","url":"https://ipassthecpaexam.com/cpa-exam-score-release/"},{"title":"IATF 16949 News: 2025 rules and 2026 Changes","url":"https://www.smithers.com/resources/2026/april/iatf-16949-news-2025-rules-and-2026-changes"},{"title":"10 RAG Projects That Actually Teach You Retrieval in 2026","url":"https://dextralabs.com/blog/rag-projects-retrieval/"},{"title":"Non-Conformance Report (NCR): A Complete Guide for 2026","url":"https://www.invensislearning.com/blog/non-conformance-report/"},{"title":"Streamlining Conformal Information Retrieval via Score Refinement","url":"https://arxiv.org/pdf/2410.02914"},{"title":"Minnesota Issues 2022 and 2023 Nonconformity Guidance","url":"https://tax.thomsonreuters.com/news/minnesota-issues-2022-and-2023-nonconformity-guidance/"}]

Based on the web search results, here's what I found:

The search results returned information related to "nonconformity" in different contexts, but the most relevant match appears to be from a technical/quality management perspective:

Initial responses to major nonconformities must now be submitted within 15 days, down from the previous 20-day allowance, according to the IATF 16949 6th Edition Rules that went into effect in 2025.

Additionally, there are results mentioning a novel score refinement method that employs a monotone transformation to adjust the scores of information retrieval systems, which when combined with conformal prediction methods, delivers significantly smaller retrieved sets while preserving their statistical guarantees.

However, the search results do not contain specific information about a "nonconformity score retrieval agreement" specifically for 2025-2026. The results cover different uses of these terms in various contexts (quality management standards, tax guidance, and technical retrieval systems). If you're looking for information about a specific agreement or document with that exact name, could you provide more context about which industry or sector you're interested in?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3fdeda8-295c-4d15-8634-422e89ecb427",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "117d5a9a-d0b2-4823-ba0c-67f7a4a2f008",
  "sourceToolAssistantUUID": "d3fdeda8-295c-4d15-8634-422e89ecb427",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-30T06:17:47.620Z_

Good, I have initial results. Now let me fetch the abstracts of the most promising papers found and run additional targeted searches to find more citing papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "117d5a9a-d0b2-4823-ba0c-67f7a4a2f008",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d177c4f7-9ee2-4747-a001-63c980cc8ebd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 23 · 2026-05-30T06:17:48.852Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0184yhhRHDnQGAjbpyS2MyWu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.17908",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d177c4f7-9ee2-4747-a001-63c980cc8ebd",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5f03f88-9c35-4303-826b-d339e0c55c36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 24 · 2026-05-30T06:17:53.463Z_

<details><summary>↩ Tool result · `toolu_0184yhhRHDnQGAjbpyS2MyWu`</summary>

```text
# Paper Details

**Title:** "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction"

**Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh

**Abstract:** The paper addresses a key challenge in RAG systems where "LLM accuracy declines when long or noisy contexts exceed the model's effective attention span." The researchers propose using conformal prediction as a coverage-controlled filtering approach. Their method "removes irrelevant content while preserving recall of supporting evidence" and was tested on NeuCLIR and RAGTIME datasets. Results show the filtering "consistently meets its target coverage" while reducing context by 2-3x and improving downstream factual accuracy.

**Venue & Date:** Accepted at ECIR 2026 (submitted November 22, 2025; revised January 19, 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5f03f88-9c35-4303-826b-d339e0c55c36",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "e39e5ed6-830b-4983-8b3d-9ffd84851b47",
  "sourceToolAssistantUUID": "a5f03f88-9c35-4303-826b-d339e0c55c36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-30T06:17:54.591Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013f4qH9MLsCTJQF4MF8rV3L`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.24268",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e39e5ed6-830b-4983-8b3d-9ffd84851b47",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c98d4a8-975a-4888-849a-f54dc8f49fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 26 · 2026-05-30T06:17:54.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BpUUggfGWoo3k3L7LQHpSt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.15556",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c98d4a8-975a-4888-849a-f54dc8f49fbe",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cb8d561-264d-4d12-98e3-e3234700ad68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 27 · 2026-05-30T06:17:55.038Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fc9xT12FxxQ4QHWb2YFrUi`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.1145/3696410.3714756",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about RAGForensics traceback of poisoning attacks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cb8d561-264d-4d12-98e3-e3234700ad68",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f243ed16-5981-422b-a533-1945220740e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 28 · 2026-05-30T06:17:55.050Z_

<details><summary>↩ Tool result · `toolu_01Fc9xT12FxxQ4QHWb2YFrUi`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f243ed16-5981-422b-a533-1945220740e7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "4870861d-fb6e-4823-9552-ad7baba78a9c",
  "sourceToolAssistantUUID": "f243ed16-5981-422b-a533-1945220740e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-30T06:17:55.204Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ei3BNNaH2KGyTEk7SrNhrU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.04711",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about sparse attention defense against corpus poisoning in RAG."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4870861d-fb6e-4823-9552-ad7baba78a9c",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03a1a5c5-9f3c-4560-9444-4b9b1259bb9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 30 · 2026-05-30T06:17:55.358Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012yyw2YXzkXqusbhsso5CCP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.18034",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about Semantic Chameleon corpus-dependent poisoning attacks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a1a5c5-9f3c-4560-9444-4b9b1259bb9f",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5abd9527-7384-482f-ac70-50e96b8ab9fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 31 · 2026-05-30T06:17:55.480Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PyQGo6L87JKFBfs4HQQuLz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.01268",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about defending against knowledge corruption in RAG."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5abd9527-7384-482f-ac70-50e96b8ab9fd",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81627168-6474-417e-8503-9892cbe4da43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 32 · 2026-05-30T06:17:56.017Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S24Ut8FoXfjRuum6HnVpva`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06872",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about trustworthy retrieval augmented generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81627168-6474-417e-8503-9892cbe4da43",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "885c7288-0430-4dd9-af6c-66fe3fa4e401",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 33 · 2026-05-30T06:17:56.403Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Rvzm8ixjUYVv2rgSiKmLB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.02914",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about conformal information retrieval and score refinement."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "885c7288-0430-4dd9-af6c-66fe3fa4e401",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e154beb-fbee-4105-aac5-fa04b5ace571",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 34 · 2026-05-30T06:17:57.652Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YApuUNwAYP2av458iivY64`</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.04287",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper CONFLARE about conformal large language model retrieval."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e154beb-fbee-4105-aac5-fa04b5ace571",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGPFysRGNVD9Qhy63dY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72f5a5c5-c7af-470a-8fba-cdc3a1eafa38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhexfkxjDcmKjVbZYVN4Eb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6210,
      "cache_read_input_tokens": 10170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6210,
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

_source line 35 · 2026-05-30T06:17:58.757Z_

<details><summary>↩ Tool result · `toolu_01BpUUggfGWoo3k3L7LQHpSt`</summary>

```text
# Paper Information

**Title:** "Certifiably Robust RAG against Retrieval Corruption"

**Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal

**Venue/Date:** arXiv:2405.15556 [cs.LG]; submitted May 24, 2024; revised April 1, 2026

**Abstract:** 

The paper addresses vulnerabilities in retrieval-augmented generation systems where malicious passages can corrupt retrieval results. The authors introduce RobustRAG, employing an "isolate-then-aggregate strategy" that partitions passages into separate groups, generates responses from each group independently, then combines them securely. Their approach achieves formal robustness guarantees through keyword-based and decoding-based aggregation techniques. Testing on open-domain question-answering and text generation tasks across multiple datasets and language models demonstrates the framework's ability to "formally certify non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cb8d561-264d-4d12-98e3-e3234700ad68",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "127cc18c-edca-4512-b58a-6dc344b9be02",
  "sourceToolAssistantUUID": "8cb8d561-264d-4d12-98e3-e3234700ad68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T06:17:58.775Z_

<details><summary>↩ Tool result · `toolu_013f4qH9MLsCTJQF4MF8rV3L`</summary>

```text
# Paper Summary

**Title:** "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation"

**Authors:** 
- Pankayaraj Pathmanathan
- Michael-Andrei Panaitescu-Liess
- Cho-Yu Jason Chiang
- Furong Huang

**Abstract:** The paper addresses vulnerabilities in RAG systems where adversaries inject malicious documents into retrieval corpora. The researchers propose two defenses operating at the retrieval stage: RAGPart, which uses document partitioning to reduce poisoned document effects, and RAGMask, which identifies suspicious tokens through "significant similarity shifts under targeted token masking." Testing across multiple benchmarks and poisoning strategies demonstrates these approaches reduce attack success while maintaining performance under normal conditions. The work includes an interpretable attack for validation and offers insights for securing RAG systems.

**Venue & Date:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral presentation); submitted December 30, 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c98d4a8-975a-4888-849a-f54dc8f49fbe",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "2be24f20-5670-4aca-80f3-5a80d19337ca",
  "sourceToolAssistantUUID": "7c98d4a8-975a-4888-849a-f54dc8f49fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-30T06:17:59.148Z_

<details><summary>↩ Tool result · `toolu_012yyw2YXzkXqusbhsso5CCP`</summary>

```text
# Semantic Chameleon: Paper Details

**Full Title:** "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems"

**Author:** Scott Thornton

**Venue & Date:** arXiv:2603.18034 (cs.CR); submitted March 10, 2026

**Abstract Summary:**
The paper examines vulnerabilities in Retrieval-Augmented Generation systems where adversaries can compromise knowledge corpora. Researchers implemented dual-document poisoning attacks using gradient optimization techniques and tested them against the Security Stack Exchange dataset. Key findings show that "hybrid retrieval combining BM25 and vector similarity, substantially mitigates this attack," reducing success rates from 38% to 0% without modifying the language model itself. Testing across five LLM families revealed variable attack success rates (46.7–93.3%), while cross-corpus evaluation demonstrated the corpus-dependent nature of these attacks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5abd9527-7384-482f-ac70-50e96b8ab9fd",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "22652a13-eeca-4e3f-9450-8d985fda7e3b",
  "sourceToolAssistantUUID": "5abd9527-7384-482f-ac70-50e96b8ab9fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T06:17:59.166Z_

<details><summary>↩ Tool result · `toolu_01PyQGo6L87JKFBfs4HQQuLz`</summary>

```text
# Paper Summary

**Full Title:** "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems"

**Authors:** Minseok Kim, Hankook Lee, Hyungjoon Koo

**Abstract:**
The researchers address vulnerabilities in Retrieval-Augmented Generation systems where attackers inject misleading data. They propose RAGDefender, a lightweight defense mechanism that identifies and removes poisoned content during the post-retrieval phase without requiring additional model training. Testing demonstrates significant improvements—for instance, the system reduced attack success rates on Gemini from 0.89 to 0.02, substantially outperforming comparable defenses like RobustRAG and Discern-and-Answer, particularly when adversarial passages substantially outnumber legitimate ones.

**Venue & Date:** Proceedings of the 2025 Annual Computer Security Applications Conference (ACSAC); submitted November 3, 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81627168-6474-417e-8503-9892cbe4da43",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "0591e453-b1a6-48e1-89c0-0d77924f3cef",
  "sourceToolAssistantUUID": "81627168-6474-417e-8503-9892cbe4da43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-30T06:17:59.221Z_

<details><summary>↩ Tool result · `toolu_01Ei3BNNaH2KGyTEk7SrNhrU`</summary>

```text
# Paper Summary

**Full Title:** "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention"

**Authors:** Sagie Dekel, Moshe Tennenholtz, Oren Kurland

**Venue/Date:** arXiv:2602.04711 (cs.IR); Submitted February 4, 2026; Revised February 5, 2026

**Abstract Summary:**

The paper addresses vulnerabilities in Retrieval Augmented Generation systems where attackers inject misleading documents to manipulate LLM outputs. The researchers propose "Sparse Document Attention RAG (SDAG)," a block-sparse attention mechanism that "disallows cross-attention between retrieved documents." 

Key characteristics of their approach include:
- Minimal inference-time modifications to attention masks
- No fine-tuning or architectural changes required
- Empirical evaluation on LLM-based question answering tasks
- Demonstrated improvements over standard causal attention in mitigating attacks
- Enhanced performance when integrated with existing RAG defense methods

The work is categorized under Information Retrieval (cs.IR) and Artificial Intelligence (cs.AI).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a1a5c5-9f3c-4560-9444-4b9b1259bb9f",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "ac62a5ab-677e-4fd2-9ebb-215c373e32d3",
  "sourceToolAssistantUUID": "03a1a5c5-9f3c-4560-9444-4b9b1259bb9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-30T06:17:59.700Z_

<details><summary>↩ Tool result · `toolu_013Rvzm8ixjUYVv2rgSiKmLB`</summary>

```text
# Paper Summary

**Full Title:** "Streamlining Conformal Information Retrieval via Score Refinement"

**Authors:** Yotam Intrator, Ori Kelner, Regev Cohen, Roman Goldenberg, Ehud Rivlin, Daniel Freedman

**Abstract:** The researchers propose addressing a limitation in conformal prediction methods for information retrieval. They note that existing approaches "produce large-sized sets, incurring high computational costs and slow response times." Their solution involves "a simple monotone transformation to retrieval scores, leading to significantly smaller conformal sets while maintaining their statistical guarantees." The method was validated using BEIR benchmarks.

**Venue & Date:** arXiv Computer Science - Information Retrieval (cs.IR); submitted October 3, 2024

**Paper Identifier:** arXiv:2410.02914
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e154beb-fbee-4105-aac5-fa04b5ace571",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "9f9127c0-870b-4f05-80f3-0578c16c296b",
  "sourceToolAssistantUUID": "0e154beb-fbee-4105-aac5-fa04b5ace571",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-30T06:18:00.729Z_

<details><summary>↩ Tool result · `toolu_01S24Ut8FoXfjRuum6HnVpva`</summary>

```text
# Paper Summary

**Title:** "Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey"

**Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, Yongjia Lei, Yuying Zhao, Xueqi Cheng, Qingkai Zeng, Luna Dong, Yinglong Xia, Krishnaram Kenthapadi, Ryan Rossi, Franck Dernoncourt, Md Mehrab Tanjim, Nesreen Ahmed, Xiaorui Liu, Wenqi Fan, Erik Blasch, Yu Wang, Meng Jiang, and Tyler Derr

**Submission Date:** February 8, 2025 (arXiv:2502.06872)

**Venue:** Computer Science > Computation and Language; Artificial Intelligence

**Abstract Summary:** The paper examines how RAG systems address AIGC challenges while introducing new vulnerabilities. The authors present a "comprehensive roadmap for developing trustworthy RAG systems" organized around five key dimensions: reliability, privacy, safety, fairness, explainability, and accountability. They provide taxonomies and frameworks for each perspective, discuss current obstacles, evaluate existing approaches, and outline future research opportunities. The work also emphasizes practical applications where trustworthy RAG implementation significantly matters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "885c7288-0430-4dd9-af6c-66fe3fa4e401",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "09e840ab-5733-4072-86a8-70172a93869c",
  "sourceToolAssistantUUID": "885c7288-0430-4dd9-af6c-66fe3fa4e401",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-30T06:18:02.005Z_

<details><summary>↩ Tool result · `toolu_01YApuUNwAYP2av458iivY64`</summary>

```text
# CONFLARE Paper Details

**Full Title:** "CONFLARE: CONFormal LArge language model REtrieval"

**Authors:**
- Pouria Rouzrokh
- Shahriar Faghani
- Cooper U. Gamble
- Moein Shariatnia
- Bradley J. Erickson

**Venue & Date:** arXiv (Computation and Language), submitted April 4, 2024 (arXiv:2404.04287)

**Abstract Summary:**
The paper introduces a framework applying conformal prediction to measure uncertainty in retrieval-augmented generation systems. The approach involves creating a calibration dataset, comparing question embeddings against document embeddings to identify relevant chunks, and establishing a similarity threshold based on a user-specified error rate. During inference, retrieved chunks meeting this threshold are provided to the LLM with statistical confidence guarantees about answer inclusion. The authors provide an open-source Python package implementing the complete workflow without requiring human intervention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72f5a5c5-c7af-470a-8fba-cdc3a1eafa38",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "404c8ab7-6f97-4669-b3f7-cf5509572b74",
  "sourceToolAssistantUUID": "72f5a5c5-c7af-470a-8fba-cdc3a1eafa38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T06:18:05.828Z_

Good. Now let me run additional searches to find more specific papers, especially ones that extend conformal prediction to adversarial settings, and to find the RAGForensics paper and other citing works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "404c8ab7-6f97-4669-b3f7-cf5509572b74",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae32adc0-ff52-461b-b984-504e88b79994",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
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

_source line 44 · 2026-05-30T06:18:06.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FFGQ8A3DgXho35uvyCgfnp`</summary>

```json
{
  "query": "conformal prediction adversarial robustness poisoning certified defense NLP 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae32adc0-ff52-461b-b984-504e88b79994",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61f5b9f1-8ed8-4c5e-8683-638e1fc39cb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
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

_source line 45 · 2026-05-30T06:18:07.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XUHKdXgppFQJpTHfD3uz69`</summary>

```json
{
  "query": "RAGForensics traceback poisoning attacks retrieval augmented generation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f5b9f1-8ed8-4c5e-8683-638e1fc39cb4",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c2c144e-415a-4fa5-985c-352ab5b200f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
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

_source line 46 · 2026-05-30T06:18:08.189Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6W3tKjRgLKBSsHEJygmQJ`</summary>

```json
{
  "query": "certified defense RAG retrieval augmented generation formal guarantees 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c2c144e-415a-4fa5-985c-352ab5b200f7",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81bf5a87-6171-4796-ac0c-e1831028c64d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
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

_source line 47 · 2026-05-30T06:18:09.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BhWPZxv1bHpVnhvfftTS7W`</summary>

```json
{
  "query": "distribution shift conformal prediction language model NLP coverage guarantee 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81bf5a87-6171-4796-ac0c-e1831028c64d",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a8d81a1-5f55-447a-9ee6-fd940970252c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
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

_source line 48 · 2026-05-30T06:18:09.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqHf1oVPAUE6aAuYjRXyzh`</summary>

```json
{
  "query": "PoisonedRAG USENIX Security 2025 Zou cited by follow-up defense"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a8d81a1-5f55-447a-9ee6-fd940970252c",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a7b6340-f044-4a7a-9aad-9ba7b1893a85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
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

_source line 49 · 2026-05-30T06:18:10.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FzQ45LxcXmJdKryGAr4evo`</summary>

```json
{
  "query": "conformal prediction selective prediction abstention LLM retrieval augmented 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a7b6340-f044-4a7a-9aad-9ba7b1893a85",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGQc7rice31vf9k7x3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b2076e7-6708-4910-a8ac-f63bc1a6cbb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJ1EQ3Nu7MEyAUfr3u4yB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 16380,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 16380,
          "cache_creation_input_tokens": 3465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3465,
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

_source line 50 · 2026-05-30T06:18:15.468Z_

<details><summary>↩ Tool result · `toolu_01FFGQ8A3DgXho35uvyCgfnp`</summary>

```text
Web search results for query: "conformal prediction adversarial robustness poisoning certified defense NLP 2025 2026 arxiv"

Links: [{"title":"GAME-THEORETIC DEFENSES FOR ROBUST CONFORMAL PREDICTION","url":"https://arxiv.org/pdf/2411.04376"},{"title":"Game-Theoretic Defenses for Robust Conformal Prediction Against Adversarial Attacks in Medical Imaging","url":"https://arxiv.org/html/2411.04376"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks | Request PDF","url":"https://www.researchgate.net/publication/393421882_Verifiably_robust_conformal_prediction_for_probabilistic_guarantees_under_adversarial_attacks"},{"title":"Towards Poisoning Robustness Certification for Natural Language Generation","url":"https://arxiv.org/pdf/2602.09757"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"}]

I found several recent papers on ArXiv related to your search query. Here are the key findings:

## Recent Work on Conformal Prediction and Adversarial Robustness (2025-2026)

**Game-Theoretic Defenses:** A framework integrates conformal prediction with game-theoretic defensive strategies to counter both known and partially unknown adversarial perturbations.

**Attack Types in Conformal Prediction:** Two distinct types of attacks have been explored in the context of Conformal Prediction: evasion attacks and contamination (or poisoning) attacks. Methods address both continuous and discrete/sparse data by providing guarantees for evasion attacks (which perturb test inputs) as well as for contamination attacks (which perturb calibration data).

**Poisoning Attacks:** Black-box data poisoning attacks specifically target CP by manipulating the prediction uncertainty rather than directly causing misclassifications.

**Enhanced Adversarial Training:** An OPSA-AT (Adversarial Training) defense strategy integrates conformal training paradigm, and the resulting defensive model significantly enhances robustness not only against OPSA but also other adversarial attacks, and maintains reliable prediction.

**NLP-Specific Work:** Certified poisoning defenses provide provable robustness guarantees by bounding the number of training examples an adversary must modify to affect model predictions. There's also work on "Towards Poisoning Robustness Certification for Natural Language Generation" that addresses certified defenses specifically for NLP tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61f5b9f1-8ed8-4c5e-8683-638e1fc39cb4",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "7d2c7a07-82fe-4099-98b8-c62c4fb9d088",
  "sourceToolAssistantUUID": "61f5b9f1-8ed8-4c5e-8683-638e1fc39cb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-30T06:18:15.744Z_

<details><summary>↩ Tool result · `toolu_01BqHf1oVPAUE6aAuYjRXyzh`</summary>

```text
Web search results for query: "PoisonedRAG USENIX Security 2025 Zou cited by follow-up defense"

Links: [{"title":"RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems","url":"https://arxiv.org/html/2604.00387v1"},{"title":"PoisonedRAG","url":"https://www.summarizepaper.com/en/arxiv-id/2402.07867v3/"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"GitHub - thisxyz/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://github.com/thisxyz/PoisonedRAG"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"34th USENIX Security Symposium: PoisonedRAG: Knowledge Corruption Attack...","url":"https://usenixsecurity25.sched.com/event/289Bm/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-generation-of-large-language-models"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"Machine Against the RAG: Jamming Retrieval-Augmented ...","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-980-shafran.pdf"},{"title":"PoisonedRAG | Proceedings of the 34th USENIX Conference on Security Symposium","url":"https://dl.acm.org/doi/10.5555/3766078.3766275"}]

Based on the search results, here's information about PoisonedRAG and related follow-up defense work:

## PoisonedRAG Paper

PoisonedRAG is a paper by J. Zou et al. that appeared at USENIX Security 2025. PoisonedRAG is the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer. The attack could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts.

## Follow-up Defense Work

Several defenses were evaluated and results showed they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.

One notable follow-up defense is documented in the search results: RAGuard: Secure retrieval-augmented generation against poisoning attacks appeared in 2025, and there's also work titled "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems" which cites the PoisonedRAG work from the 34th USENIX Security Symposium 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a7b6340-f044-4a7a-9aad-9ba7b1893a85",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "eeb72890-7c32-449a-8008-15a706cf7996",
  "sourceToolAssistantUUID": "1a7b6340-f044-4a7a-9aad-9ba7b1893a85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-30T06:18:16.877Z_

<details><summary>↩ Tool result · `toolu_01S6W3tKjRgLKBSsHEJygmQJ`</summary>

```text
Web search results for query: "certified defense RAG retrieval augmented generation formal guarantees 2025 2026 arxiv"

Links: [{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"Provably Secure Retrieval-Augmented Generation","url":"https://arxiv.org/html/2508.01084"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models","url":"https://arxiv.org/pdf/2402.03181"},{"title":"[2508.01084] Provably Secure Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2508.01084"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"}]

Based on the search results, I found several relevant papers and resources on certified defenses for RAG (Retrieval-Augmented Generation) systems with formal guarantees from 2025-2026:

## Key Findings:

**Certified Defense Mechanisms:**
Certified defenses for RAG operate by constraining the adversary's impact, typically via ranking, aggregation, or detection strategies that admit worst-case bounds, probabilistic guarantees, or explicit certificates of robust operation.

**Notable Recent Work (2025-2026):**

1. **RobustRAG** - The first certifiably robust defense framework against retrieval corruption attacks, built around the core insight of an isolate-then-aggregate strategy.

2. **C-RAG** - The first framework to certify generation risks for RAG models, providing conformal risk analysis for RAG models and certifying an upper confidence bound of generation risks.

3. **SAG (Provably Secure RAG)** - A provably secure framework for RAG systems that employs a pre-storage full-encryption scheme to ensure dual protection of both retrieved content and vector embeddings, with formal security proofs verifying the scheme's confidentiality and integrity under a computational security model.

**Threat Models:**
Certified defenses address perturbation-based ranking attacks, retrieval corruption through replacement or insertion of retrievals, and prompt injection attacks from adversarially-crafted documents.

**Defense Techniques:**
Techniques like randomized masking smoothing in neural rankers and graph-theoretic methods provide probabilistic guarantees against perturbation and retrieval corruption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81bf5a87-6171-4796-ac0c-e1831028c64d",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "ffaf140c-18c9-4066-99ab-f43ba2b26de1",
  "sourceToolAssistantUUID": "81bf5a87-6171-4796-ac0c-e1831028c64d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-30T06:18:17.401Z_

<details><summary>↩ Tool result · `toolu_01XUHKdXgppFQJpTHfD3uz69`</summary>

```text
Web search results for query: "RAGForensics traceback poisoning attacks retrieval augmented generation 2025 arxiv"

Links: [{"title":"[Literature Review] Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://www.themoonlight.io/en/review/traceback-of-poisoning-attacks-to-retrieval-augmented-generation"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421668Z/abstract"},{"title":"[2504.21668] Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2504.21668"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.21668v2"},{"title":"(PDF) Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/391018324_Traceback_of_Poisoning_Attacks_to_Retrieval-Augmented_Generation"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation Baolei Zhang∗","url":"https://www.arxiv.org/pdf/2504.21668v2"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2504.21668"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/abs/10.1145/3696410.3714756"},{"title":"Traceback of Poisoned Texts in Poisoning Attacks to ...","url":"https://openreview.net/pdf?id=bwnWs4us0x"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation | alphaXiv","url":"https://www.alphaxiv.org/fr/overview/2504.21668v1"}]

I found relevant information about RAGForensics and traceback poisoning attacks. Here's what the search results show:

## Overview

RAGForensics is a novel traceback system designed to identify poisoned texts within the knowledge database of Retrieval-Augmented Generation (RAG) systems, introduced in a 2025 paper (arxiv 2504.21668).

## The Problem

RAG systems enhance large language models (LLMs) by retrieving relevant information from external knowledge sources, but they are vulnerable to poisoning attacks where malicious texts are injected to manipulate the system's responses. Existing defenses primarily focus on mitigating the impact of poisoned texts during inference and are insufficient against sophisticated attacks.

## The Solution

RAGForensics operates iteratively, first retrieving a subset of texts from the database and then utilizing a specially crafted prompt to guide an LLM in detecting potential poisoning texts. This study is the first to investigate the traceback of poisoned texts in RAG systems.

## Results

Empirical evaluations across multiple datasets demonstrate the effectiveness of RAGForensics against state-of-the-art poisoning attacks. Additionally, the authors designed two adaptive attacks against RAGForensics and demonstrated that RAGForensics remains robust against these powerful attacks.

The paper was published in the Proceedings of the ACM Web Conference 2025 (WWW '25), and code is available at https://github.com/zhangbl6618/RAG-Responsibility-Attribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c2c144e-415a-4fa5-985c-352ab5b200f7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "3bd72d77-767a-48f0-9404-b488c5efc00f",
  "sourceToolAssistantUUID": "7c2c144e-415a-4fa5-985c-352ab5b200f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-30T06:18:17.713Z_

<details><summary>↩ Tool result · `toolu_01FzQ45LxcXmJdKryGAr4evo`</summary>

```text
Web search results for query: "conformal prediction selective prediction abstention LLM retrieval augmented 2025 2026"

Links: [{"title":"Know Your Limits: A Survey of Abstention in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393331033_Know_Your_Limits_A_Survey_of_Abstention_in_Large_Language_Models"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/html/2502.06884v1"},{"title":"SelectLLM – Calibrating LLMs for Selective Prediction: Balancing Coverage and Risk | OpenReview","url":"https://openreview.net/forum?id=JJPAy8mvrQ"},{"title":"Selective \"Selective Prediction\": Reducing Unnecessary Abstention in   Vision-Language Reasoning","url":"https://arxiv.org/pdf/2402.15610"},{"title":"CONFLARE: CONFormal LArge language model REtrieval","url":"https://arxiv.org/pdf/2404.04287"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/pdf/2511.17908"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"}]

Based on the search results, here's what I found about conformal prediction, selective prediction, abstention, and retrieval-augmented LLMs:

## Recent Work on Conformal Prediction and LLM Abstention

Conformal prediction has been used to provide rigorous statistical guarantees on hallucination rates through calibrated abstention. This approach represents an important development in making LLMs more trustworthy.

## Adaptive Abstention Policies

A recent approach integrates reinforcement learning with conformal prediction to enable adaptive thresholding for selective abstention and risk management in LLM applications. This learned policy reportedly boosts hallucination detection by up to 22%, improves uncertainty-guided selective generation by more than 20%, and reduces expected calibration error by 70%-85% compared to standard conformal baselines.

## Conformal Prediction in Retrieval-Augmented Generation

Several papers address conformal prediction specifically for RAG systems:

- TRAQ (Trustworthy Retrieval Augmented Question Answering) provides end-to-end statistical correctness guarantees for RAG using conformal prediction to construct prediction sets that are guaranteed to contain the correct response with high probability.

- RAG grounds LLMs in retrieved evidence to reduce hallucinations, but RAG systems remain brittle with retrieval noise and prompt saturation degrading reliability. Recent work addresses this through principled context engineering.

## Selective Prediction in Vision-Language Models

Selective prediction systems aim to balance the number of predictions made (coverage) and the error rate on instances which do receive a prediction (risk), with various approaches being developed to improve this balance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b2076e7-6708-4910-a8ac-f63bc1a6cbb8",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "52467392-f2e3-419f-b451-0659e8ab5014",
  "sourceToolAssistantUUID": "1b2076e7-6708-4910-a8ac-f63bc1a6cbb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-30T06:18:17.987Z_

<details><summary>↩ Tool result · `toolu_01BhWPZxv1bHpVnhvfftTS7W`</summary>

```text
Web search results for query: "distribution shift conformal prediction language model NLP coverage guarantee 2025 2026"

Links: [{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"Domain-Shift-Aware Conformal Prediction for Large Language Models","url":"https://arxiv.org/pdf/2510.05566"},{"title":"[2602.14913] Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift","url":"https://arxiv.org/abs/2602.14913"},{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217v1"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift","url":"https://arxiv.org/pdf/2602.14913"},{"title":"Domain-Shift-Aware Conformal Prediction for Large Language Models","url":"https://arxiv.org/html/2510.05566v1"},{"title":"Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift","url":"https://arxiv.org/html/2602.14913"}]

I found several recent research papers on conformal prediction with distribution shifts and language models from 2025-2026. Here are the key findings:

## Recent Research on Conformal Prediction under Distribution Shifts

**NeurIPS 2025 Research on Robustness:**
A paper published in September 2025 addresses conformal prediction's robustness under distribution shifts, specifically analyzing how conformal prediction provides finite-sample guarantees despite challenges from distribution shifts. The research shows how propagating Lévy-Prokhorov ambiguity sets through scoring functions reduces high-dimensional distribution shifts to manageable one-dimensional shifts, enabling exact quantification of worst-case quantiles and coverage.

**Domain-Shift-Aware Conformal Prediction for LLMs (October 2025):**
A recent study notes that while conformal prediction provides finite-sample, distribution-free coverage guarantees, standard conformal prediction breaks down under domain shift, often leading to under-coverage and unreliable prediction sets. The proposed Domain-Shift-Aware Conformal Prediction (DS-CP) method demonstrates more reliable coverage than standard conformal prediction on the MMLU benchmark, especially under substantial distribution shifts, while maintaining efficiency.

**Coverage Guarantees under Distribution Shift (February 2026):**
Recent work analyzes pseudo-calibration as a tool to counter performance loss under bounded label-conditional covariate shift, deriving lower bounds on target coverage in terms of source-domain loss and Wasserstein measures of shift, and providing methods to design pseudo-calibrated sets that maintain target coverage above prescribed levels.

These papers represent the current state of research addressing the challenge of maintaining coverage guarantees when conformal prediction methods are applied to language models experiencing distribution shifts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a8d81a1-5f55-447a-9ee6-fd940970252c",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "3f1246e8-bdb7-4f21-9d96-8a3d784e0c02",
  "sourceToolAssistantUUID": "9a8d81a1-5f55-447a-9ee6-fd940970252c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-30T06:18:21.346Z_

Excellent. Let me now fetch the abstracts of the newly discovered papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f1246e8-bdb7-4f21-9d96-8a3d784e0c02",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52641997-3646-4936-9cc6-9e7f09908850",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 57 · 2026-05-30T06:18:23.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EDEMspeYqH1Ub1DrrJRWV6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.21668",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about traceback of poisoning attacks to RAG."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52641997-3646-4936-9cc6-9e7f09908850",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bbaf6c9-397f-4ba0-9ecb-cd0017d7dfe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 58 · 2026-05-30T06:18:24.171Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JQpxoX7B72VVC54atB3XGs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.09757",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about poisoning robustness certification for natural language generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bbaf6c9-397f-4ba0-9ecb-cd0017d7dfe1",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31b74a2d-c5a0-4737-8635-b5e435b505b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 59 · 2026-05-30T06:18:25.110Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EeZPXCEo4gQ6rAEBKCkLh9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.05566",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about domain-shift-aware conformal prediction for LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31b74a2d-c5a0-4737-8635-b5e435b505b0",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afc4f16d-9afa-43d0-8169-81dbb1190628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 60 · 2026-05-30T06:18:26.031Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014FzS28cC4vPsonhAtGZLmc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06884",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about conformal abstention policies for adaptive risk management in LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc4f16d-9afa-43d0-8169-81dbb1190628",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b6963e1-e21c-42e1-9cc2-a41e280a54e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 61 · 2026-05-30T06:18:27.052Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019vgAQHzTmTREkSSQ7NSLfh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.01084",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about provably secure retrieval-augmented generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b6963e1-e21c-42e1-9cc2-a41e280a54e7",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29fc35d7-4001-4bd1-9d6c-0035603f6333",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 62 · 2026-05-30T06:18:27.275Z_

<details><summary>↩ Tool result · `toolu_01EDEMspeYqH1Ub1DrrJRWV6`</summary>

```text
# Paper Details: Traceback of Poisoning Attacks to RAG

**Title:** "Traceback of Poisoning Attacks to Retrieval-Augmented Generation"

**Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, and Zheli Liu

**Abstract Summary:**
The researchers present RAGForensics, described as "the first traceback system for RAG, designed to identify poisoned texts within the knowledge database." The system works through an iterative process that retrieves text subsets and employs "a specially crafted prompt to guide an LLM in detecting potential poisoning texts." The work addresses vulnerabilities in retrieval-augmented generation systems where attackers inject malicious content into knowledge databases to manipulate model outputs.

**Venue & Date:** The Web Conference 2025 (accepted)

**Submission History:**
- Initial submission: April 30, 2025
- Revised version: October 18, 2025

**Additional Resources:** Code is available at the authors' GitHub repository for RAG Responsibility Attribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bbaf6c9-397f-4ba0-9ecb-cd0017d7dfe1",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "a59f0b35-bd2f-4abc-878c-11aef17faef1",
  "sourceToolAssistantUUID": "8bbaf6c9-397f-4ba0-9ecb-cd0017d7dfe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-30T06:18:27.941Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HsDhjB1ZZyMisRG3SjnWVr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08304",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about securing retrieval-augmented generation taxonomy of attacks and defenses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a59f0b35-bd2f-4abc-878c-11aef17faef1",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f13e6da-ba93-4311-bae4-fd768f485119",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 64 · 2026-05-30T06:18:28.896Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019Np2TGQj3d3Te3QH61QAnd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.04376",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about game-theoretic defenses for robust conformal prediction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f13e6da-ba93-4311-bae4-fd768f485119",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdd07695-65c2-4465-b463-b8f966848566",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 65 · 2026-05-30T06:18:29.243Z_

<details><summary>↩ Tool result · `toolu_01JQpxoX7B72VVC54atB3XGs`</summary>

```text
# Paper Summary

**Title:** "Towards Poisoning Robustness Certification for Natural Language Generation"

**Authors:** Mihnea Ghitu, Matthew Wicker

**Venue/Date:** arXiv:2602.09757 (cs.LG), submitted February 10, 2026

**Abstract Summary:**

The researchers address reliability challenges in language model deployment by establishing a framework for certified robustness against data poisoning attacks. They define two key security properties: stability (resistance to any generation changes) and validity (defense against specific harmful outputs).

Their main contribution is Targeted Partition Aggregation (TPA), described as "the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase." The method extends to multi-turn interactions using mixed integer linear programming for tighter guarantees.

Empirical validation spans multiple scenarios, including verifying agent tool-calling safety when adversaries compromise up to 0.5% of training data and confirming 8-token stability in preference-aligned models. The authors acknowledge inference latency as an ongoing challenge while positioning their work as enabling safer deployment of language models in security-critical environments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31b74a2d-c5a0-4737-8635-b5e435b505b0",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "66231d83-1579-4ddf-bcc9-d4e90b694515",
  "sourceToolAssistantUUID": "31b74a2d-c5a0-4737-8635-b5e435b505b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-30T06:18:28.958Z_

<details><summary>↩ Tool result · `toolu_01EeZPXCEo4gQ6rAEBKCkLh9`</summary>

```text
# Domain-Shift-Aware Conformal Prediction for Large Language Models

**Full Title:** "Domain-Shift-Aware Conformal Prediction for Large Language Models"

**Authors:**
- Zhexiao Lin
- Yuanyuan Li
- Neeraj Sarna
- Yuanyuan Gao
- Michael von Gablenz

**Abstract:**
The authors address how large language models produce unreliable outputs and hallucinations. They introduce DS-CP, a framework adapting conformal prediction to LLMs experiencing distribution shifts. The approach "reweight[s] calibration samples based on their proximity to the test prompt," aiming to maintain validity while improving adaptivity. Testing on MMLU shows their method provides "more reliable coverage than standard conformal prediction" under significant shifts while remaining computationally efficient.

**Venue & Date:**
Submitted to arXiv on October 7, 2025 (arXiv:2510.05566). The paper is categorized under Machine Learning (stat.ML) and related fields including Artificial Intelligence and Computational Linguistics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afc4f16d-9afa-43d0-8169-81dbb1190628",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "0f71705d-7b65-45e6-8b9b-ade5c2a476ac",
  "sourceToolAssistantUUID": "afc4f16d-9afa-43d0-8169-81dbb1190628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-30T06:18:30.227Z_

<details><summary>↩ Tool result · `toolu_019vgAQHzTmTREkSSQ7NSLfh`</summary>

```text
# Paper Summary

**Title:** "Provably Secure Retrieval-Augmented Generation"

**Authors:** Pengcheng Zhou, Yinglun Feng, Zhongliang Yang

**Submission Date:** August 1, 2025

**Venue:** arXiv (cs.CR - Cryptography and Security)

**Abstract:** The paper addresses security gaps in RAG systems by proposing the first framework with formal security guarantees. The researchers introduce "a pre-storage full-encryption scheme to ensure dual protection of both retrieved content and vector embeddings." They employ computational security models to verify confidentiality and integrity properties and demonstrate resistance to state-of-the-art attacks through experiments on multiple benchmarks. The work aims to establish theoretical foundations for formally secure RAG systems in AI applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29fc35d7-4001-4bd1-9d6c-0035603f6333",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "817c01d7-d9bf-4a2f-aea1-6dbfb7d38f07",
  "sourceToolAssistantUUID": "29fc35d7-4001-4bd1-9d6c-0035603f6333",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-30T06:18:30.297Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WRoBk12h4BbbH7UugQMxoG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.14913",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about coverage guarantees for pseudo-calibrated conformal prediction under distribution shift."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "817c01d7-d9bf-4a2f-aea1-6dbfb7d38f07",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82ed0eca-1391-428c-881e-116d225a126a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 69 · 2026-05-30T06:18:30.648Z_

<details><summary>↩ Tool result · `toolu_014FzS28cC4vPsonhAtGZLmc`</summary>

```text
# Paper Information

**Full Title:** "Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models"

**Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi

**Venue & Date:** arXiv:2502.06884 (Computer Science > Machine Learning), submitted February 8, 2025

**Abstract Summary:**

The research addresses how large language and vision-language models can better manage risk in safety-critical applications. The authors propose combining reinforcement learning with conformal prediction to create dynamic abstention thresholds rather than relying on fixed ones. This adaptive approach optimizes uncertainty quantification to balance prediction accuracy, coverage, and set size.

According to their findings, the method achieves notable improvements: "accuracy by up to 3.2%, boosting AUROC for hallucination detection by 22.19%, enhancing uncertainty-guided selective generation (AUARC) by 21.17%, and reducing calibration error by 70%-85%." The technique consistently maintains a 90% coverage target across multiple models and datasets, outperforming existing methods like LAC and APS.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b6963e1-e21c-42e1-9cc2-a41e280a54e7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "73278fc3-ccbc-4f65-9272-66beb50d8a6b",
  "sourceToolAssistantUUID": "0b6963e1-e21c-42e1-9cc2-a41e280a54e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-30T06:18:30.761Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X3KdJ6D6VkJ3FyGNWpbdh7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.16217",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about robust conformal prediction for LLMs via internal representations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73278fc3-ccbc-4f65-9272-66beb50d8a6b",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGRknXtKGJZh2NziFAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ea04e6f-fec7-47ca-aa9a-c895a2845759",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR3ECrtiycWFQKZtgpdmay",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 19845,
      "output_tokens": 883,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3528
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1728,
          "output_tokens": 883,
          "cache_read_input_tokens": 19845,
          "cache_creation_input_tokens": 3528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3528,
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

_source line 71 · 2026-05-30T06:18:32.102Z_

<details><summary>↩ Tool result · `toolu_01HsDhjB1ZZyMisRG3SjnWVr`</summary>

```text
# Paper Details

**Full Title:** "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions"

**Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen

**Venue/Date:** arXiv:2604.08304 (cs.CR); Submitted April 9, 2026; Revised May 27, 2026

**Abstract:** The paper frames secure RAG as "securing external knowledge access" and introduces SLOT, a framework organizing literature across four dimensions: attack Surface, defense Layer, security Objective (following CIA properties), and Target scope. The authors map attacks and defenses onto a six-stage knowledge-access pipeline, revealing structural gaps in current approaches. They identify future priorities including more realistic threat scenarios, comprehensive defense evaluation, enhanced confidentiality protections, and assessments for multimodal and agentic RAG systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f13e6da-ba93-4311-bae4-fd768f485119",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "5f4a845d-806d-4c8f-a686-437042a6b4c6",
  "sourceToolAssistantUUID": "4f13e6da-ba93-4311-bae4-fd768f485119",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-30T06:18:33.798Z_

<details><summary>↩ Tool result · `toolu_019Np2TGQj3d3Te3QH61QAnd`</summary>

```text
# Paper Summary

**Full Title:** "Game-Theoretic Defenses for Robust Conformal Prediction Against Adversarial Attacks in Medical Imaging"

**Authors:** Rui Luo, Jie Bao, Zhixin Zhou, Chuangyin Dang

**Venue/Date:** arXiv:2411.04376 [cs.LG]; submitted November 7, 2024; revised March 4, 2025

**Abstract:** The researchers present a framework combining conformal prediction with game-theoretic strategies to strengthen deep learning models against adversarial perturbations in medical imaging. Their approach addresses three key questions: creating valid conformal prediction sets under known attacks, maintaining coverage against unknown attacks using conservative thresholding, and identifying optimal defensive strategies within a zero-sum game context. The methodology employs specialized defensive models and maximum/minimum classifiers for defense aggregation. Testing on MedMNIST datasets (PathMNIST, OrganAMNIST, TissueMNIST) shows the method "maintains high coverage guarantees while minimizing prediction set sizes." Game-theoretic analysis indicates the optimal defensive strategy frequently converges to a single robust model, exceeding performance of alternative approaches across evaluated datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdd07695-65c2-4465-b463-b8f966848566",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "4ec9219d-e82c-4b5d-9028-31307620543a",
  "sourceToolAssistantUUID": "fdd07695-65c2-4465-b463-b8f966848566",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-30T06:18:34.099Z_

<details><summary>↩ Tool result · `toolu_01WRoBk12h4BbbH7UugQMxoG`</summary>

```text
# Paper Information

**Title:** "Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift"

**Authors:** Farbod Siahkali, Ashwin Verma, Vijay Gupta

**Abstract:** The paper addresses how conformal prediction can fail under data distribution shifts. The researchers analyze pseudo-calibration as a solution within a bounded label-conditional covariate shift framework. They derive a lower bound on target coverage using domain adaptation techniques, propose a method to adjust conformal thresholds via a slack parameter, and introduce a source-tuned algorithm that balances hard and randomized pseudo-labels based on classifier uncertainty. Experiments demonstrate their bounds align with actual behavior and their approach reduces coverage loss while maintaining reasonable prediction set sizes.

**Venue/Date:** arXiv preprint (cs.LG); submitted February 16, 2026; under review; 6 pages with 2 figures and 1 table
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82ed0eca-1391-428c-881e-116d225a126a",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "b29603bc-3445-44c1-8e85-a2a05b4260b6",
  "sourceToolAssistantUUID": "82ed0eca-1391-428c-881e-116d225a126a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-30T06:18:34.789Z_

<details><summary>↩ Tool result · `toolu_01X3KdJ6D6VkJ3FyGNWpbdh7`</summary>

```text
# Paper Summary

**Title:** "Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations"

**Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang

**Venue/Date:** arXiv:2604.16217 (Computer Science > Computation and Language), submitted April 17, 2026

**Abstract:** 
The researchers address reliability challenges in large language model deployment by proposing a conformal prediction framework that leverages internal model representations rather than surface-level outputs. Their approach introduces "Layer-Wise Information scores, which measure how conditioning on the input reshapes predictive entropy across model depth." These scores serve as nonconformity measures within a split conformal pipeline. Testing across question-answering benchmarks demonstrates superior validity-efficiency trade-offs compared to text-based alternatives, particularly when models encounter distribution shifts. The work suggests that internal representations offer more stable uncertainty signals than traditional output statistics under real-world deployment conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ea04e6f-fec7-47ca-aa9a-c895a2845759",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "e60df8e2-1578-480e-b22a-1b9027d74bee",
  "sourceToolAssistantUUID": "1ea04e6f-fec7-47ca-aa9a-c895a2845759",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-30T06:18:44.836Z_

Let me run a few more targeted searches to find any remaining highly relevant papers I may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e60df8e2-1578-480e-b22a-1b9027d74bee",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGSzhDt66AeyLbs9NkN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce784432-daba-4f39-8138-e2ab8f891740",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMHYoAVySJTGsp5Xvk42wn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5127,
      "cache_read_input_tokens": 23373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5127,
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

_source line 76 · 2026-05-30T06:18:45.784Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5Fx3wHdJ3bj53cjuRCpK7`</summary>

```json
{
  "query": "\"Machine Against the RAG\" jamming retrieval augmented generation USENIX 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce784432-daba-4f39-8138-e2ab8f891740",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGSzhDt66AeyLbs9NkN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18262e2a-95c4-48ad-a4c7-d2346a7b8e0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMHYoAVySJTGsp5Xvk42wn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5127,
      "cache_read_input_tokens": 23373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5127,
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

_source line 77 · 2026-05-30T06:18:47.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014VZkuoz1NkZvQ3zUHQ6jNV`</summary>

```json
{
  "query": "Xiang Chong RobustRAG cited by 2025 2026 certifiably robust retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18262e2a-95c4-48ad-a4c7-d2346a7b8e0e",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGSzhDt66AeyLbs9NkN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5307211-87a8-4245-822e-534bafe60349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMHYoAVySJTGsp5Xvk42wn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5127,
      "cache_read_input_tokens": 23373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5127,
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

_source line 78 · 2026-05-30T06:18:47.763Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HN9pfLwtGK1NNQ1rYxfBw3`</summary>

```json
{
  "query": "conformal prediction uncertainty quantification RAG hallucination detection abstention 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5307211-87a8-4245-822e-534bafe60349",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGSzhDt66AeyLbs9NkN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ff7225-2569-4123-b53a-9ce5cb2968e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMHYoAVySJTGsp5Xvk42wn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5127,
      "cache_read_input_tokens": 23373,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5127
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 23373,
          "cache_creation_input_tokens": 5127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5127,
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

_source line 79 · 2026-05-30T06:18:53.324Z_

<details><summary>↩ Tool result · `toolu_014VZkuoz1NkZvQ3zUHQ6jNV`</summary>

```text
Web search results for query: "Xiang Chong RobustRAG cited by 2025 2026 certifiably robust retrieval"

Links: [{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"[2405.15556v1] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556v1"},{"title":"[Literature Review] Certifiably Robust RAG against Retrieval Corruption","url":"https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"\"Certifiably Robust RAG against Retrieval Corruption\" by Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal | MLSecOps Community","url":"https://community.mlsecops.com/public/forum/boards/research-a45/posts/certifiably-robust-rag-against-retrieval-corruption-by-chong-xiang-tong-wu-zexuan-zhong-david-wagner-danqi-chen-prateek-mittal-1m53y449ia"},{"title":"Chong Xiang's research works | Princeton University and other places","url":"https://www.researchgate.net/scientific-contributions/Chong-Xiang-2175323098"}]

Based on the search results, I found comprehensive information about RobustRAG by Chong Xiang:

## RobustRAG: Certifiably Robust RAG

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. It was authored by Chong Xiang from NVIDIA, along with researchers from Princeton University and UC Berkeley.

### The Problem

Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

### The Solution

The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.

### Certifiable Robustness

RobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, formally certifiable non-trivial lower bounds on response quality can be assured even against an adaptive attacker with full knowledge of the defense.

### Evaluation Results

RobustRAG achieves substantial certifiable robustness while maintaining high clean performance, with 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5307211-87a8-4245-822e-534bafe60349",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "08abd745-9bb3-4597-8896-e93395c1daf7",
  "sourceToolAssistantUUID": "f5307211-87a8-4245-822e-534bafe60349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-30T06:18:56.652Z_

<details><summary>↩ Tool result · `toolu_01HN9pfLwtGK1NNQ1rYxfBw3`</summary>

```text
Web search results for query: "conformal prediction uncertainty quantification RAG hallucination detection abstention 2025 2026 arxiv"

Links: [{"title":"The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems","url":"https://arxiv.org/pdf/2512.15068"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/html/2502.06884v1"},{"title":"Conformal Prediction Beyond the Seen: A Missing Mass","url":"https://arxiv.org/pdf/2506.05497"},{"title":"Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation","url":"https://arxiv.org/html/2505.21072v1"},{"title":"INTRYGUE: Induction-Aware Entropy Gating for Reliable RAG Uncertainty Estimation","url":"https://arxiv.org/pdf/2603.21607"},{"title":"URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models","url":"https://arxiv.org/pdf/2603.19281"},{"title":"Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2505.21072"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/pdf/2405.01976"}]

Based on the search results, here are the most relevant recent papers (2025-2026) on conformal prediction, uncertainty quantification, RAG hallucination detection, and abstention:

## Key Recent Papers

**1. The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems (2025)**
This work applies conformal prediction to determine when LLMs should abstain, achieving bounded hallucination rates on open-domain QA by self-evaluating response consistency. It addresses faithfulness ("is the output supported by retrieved context?") in RAG systems.

**2. Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models (Feb 2025)**
This paper notes that conformal prediction (CP) provides statistical guarantees but relies on static thresholds, and proposes learnable conformal abstention that integrates reinforcement learning (RL) with CP to optimize abstention thresholds dynamically. The method outperforms baselines in hallucination detection (AUROC), selective generation (AUARC), and calibration error while maintaining valid coverage guarantees.

**3. Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation (May 2025)**
This work addresses how the use of retrieved information makes it challenging to detect hallucinations in LLM responses.

**4. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models (March 2026)**
This benchmark evaluates 8 standard RAG methods, measuring their performance through both accuracy and prediction-set sizes based on LAC and APS metrics.

**5. INTRYGUE: Induction-Aware Entropy Gating for Reliable RAG Uncertainty Estimation (2026)**
This paper proposes a mechanistically grounded method that gates predictive entropy based on activation patterns of induction heads, evaluated across four RAG benchmarks and six open-source LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31ff7225-2569-4123-b53a-9ce5cb2968e0",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "8583980d-8562-485f-9f1b-6c66e4bcf019",
  "sourceToolAssistantUUID": "31ff7225-2569-4123-b53a-9ce5cb2968e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-30T06:18:57.563Z_

<details><summary>↩ Tool result · `toolu_01F5Fx3wHdJ3bj53cjuRCpK7`</summary>

```text
Web search results for query: ""Machine Against the RAG" jamming retrieval augmented generation USENIX 2025"

Links: [{"title":"Machine Against the RAG: Jamming Retrieval","url":"https://www.usenix.org/system/files/usenixsecurity25-shafran.pdf"},{"title":"Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents","url":"https://arxiv.org/html/2406.05870v4"},{"title":"Machine against the RAG: jamming retrieval-augmented ...","url":"https://dl.acm.org/doi/abs/10.5555/3766078.3766273"},{"title":"Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/shafran"},{"title":"Machine Against the RAG: Jamming Retrieval-Augmented Generation with   Blocker Documents","url":"https://arxiv.org/pdf/2406.05870"},{"title":"[2406.05870] Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents","url":"https://arxiv.org/abs/2406.05870"},{"title":"AI Security - The Hidden Attack Surfaces of RAG and MCP | Deconvolute Labs","url":"https://deconvoluteai.com/blog/attack-surfaces-rag"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.05870"}]

I found the research paper you were looking for! Here's what I found:

## "Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents"

This paper was authored by Avital Shafran from The Hebrew University, Roei Schuster from Wild Moose, and Vitaly Shmatikov from Cornell Tech, and was presented at the 34th USENIX Security Symposium held August 13–15, 2025 in Seattle, WA.

### Research Overview

The paper demonstrates that retrieval-augmented generation (RAG) systems that operate on databases with untrusted content are vulnerable to denial-of-service attacks called jamming. 

An adversary can add a single "blocker" document to the database that will be retrieved in response to a specific query and result in the RAG system not answering this query, ostensibly because it lacks relevant information or because the answer is unsafe.

### Key Technical Contributions

The researchers describe and measure the efficacy of several methods for generating blocker documents, including a new method based on black-box optimization. Their method (1) does not rely on instruction injection, (2) does not require the adversary to know the embedding or LLM used by the target RAG system, and (3) does not employ an auxiliary LLM.

The paper is available through USENIX's official proceedings and has also been published on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18262e2a-95c4-48ad-a4c7-d2346a7b8e0e",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "ea59f5c5-2e41-4494-a406-8f8806f78ad7",
  "sourceToolAssistantUUID": "18262e2a-95c4-48ad-a4c7-d2346a7b8e0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-30T06:18:59.564Z_

Let me fetch the remaining highly relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea59f5c5-2e41-4494-a406-8f8806f78ad7",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGUg37hZXzFQyG7SvuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2732f934-0069-4e1e-a1ac-d99f63b1d473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzStnuvnmhf9LGm9DgKj1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1776,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 28500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1079,
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

_source line 83 · 2026-05-30T06:19:01.441Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0176irJQ8Wperzb7YyjVkkpx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.05870",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about jamming RAG with blocker documents."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2732f934-0069-4e1e-a1ac-d99f63b1d473",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGUg37hZXzFQyG7SvuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b561c48-c74a-4095-868e-2e59bc641404",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzStnuvnmhf9LGm9DgKj1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1776,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 28500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1079,
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

_source line 84 · 2026-05-30T06:19:02.390Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JwFRzo4XTfPsem6XgZvSSQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.15068",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about semantic illusion and certified limits of hallucination detection in RAG."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b561c48-c74a-4095-868e-2e59bc641404",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGUg37hZXzFQyG7SvuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af92b13d-a514-4f86-a1f0-72015a041cee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzStnuvnmhf9LGm9DgKj1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1776,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 28500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1079,
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

_source line 85 · 2026-05-30T06:19:03.338Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DuC3sbmtz517KEGmXri8Yp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19281",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about URAG benchmark for uncertainty quantification in retrieval-augmented LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af92b13d-a514-4f86-a1f0-72015a041cee",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGUg37hZXzFQyG7SvuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9758aa02-6808-4dd1-babb-e20bc29e6f2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzStnuvnmhf9LGm9DgKj1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1776,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 28500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1079,
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

_source line 86 · 2026-05-30T06:19:03.759Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sz97gVbGFU74vPorAYScWj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21072",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about faithfulness-aware uncertainty quantification for fact-checking RAG output."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9758aa02-6808-4dd1-babb-e20bc29e6f2e",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGUg37hZXzFQyG7SvuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2f166ea-44ce-45fd-830b-e4acb1ac2034",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzStnuvnmhf9LGm9DgKj1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1776,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 28500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1079,
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

_source line 87 · 2026-05-30T06:19:04.566Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01McGTLSuVvyY7K5yFXu3o6L`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.21607",
  "prompt": "Extract the full title, all authors, abstract, and venue/date of this paper about INTRYGUE induction-aware entropy gating for RAG uncertainty estimation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2f166ea-44ce-45fd-830b-e4acb1ac2034",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGUg37hZXzFQyG7SvuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63e6e095-ffef-4368-8b6f-ed752c5b672b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzStnuvnmhf9LGm9DgKj1G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1776,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 28500,
      "output_tokens": 511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1079
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1776,
          "output_tokens": 511,
          "cache_read_input_tokens": 28500,
          "cache_creation_input_tokens": 1079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1079,
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

_source line 88 · 2026-05-30T06:19:05.497Z_

<details><summary>↩ Tool result · `toolu_0176irJQ8Wperzb7YyjVkkpx`</summary>

```text
# Paper Summary

**Title:** "Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents"

**Authors:** Avital Shafran, Roei Schuster, Vitaly Shmatikov

**Abstract:** The paper demonstrates that RAG systems operating on databases with untrusted content are susceptible to denial-of-service attacks. Adversaries can insert a single "blocker document" that gets retrieved for specific queries, causing the system to refuse answering. The researchers present multiple methods for generating blocker documents, including a novel black-box optimization approach that requires no instruction injection, embedding/LLM knowledge, or auxiliary models. Their evaluation shows RAG vulnerabilities across various embeddings and LLMs, revealing that current safety metrics fail to capture this threat. The paper concludes by discussing potential defenses.

**Venue & Date:** To appear in USENIX Security Symposium 2025 (submitted June 9, 2024; final version March 10, 2025)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b561c48-c74a-4095-868e-2e59bc641404",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "d78a2bd8-06e9-4375-b31b-e2a288cc6c4b",
  "sourceToolAssistantUUID": "3b561c48-c74a-4095-868e-2e59bc641404",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-30T06:19:07.933Z_

<details><summary>↩ Tool result · `toolu_01DuC3sbmtz517KEGmXri8Yp`</summary>

```text
# URAG Paper Information

**Full Title:** "URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models"

**Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, and Suhang Wang

**Venue/Date:** arXiv:2603.19281 (Computer Science - Computation and Language), submitted March 2, 2026

**Abstract Summary:** 
The research introduces a comprehensive evaluation framework addressing a significant gap in RAG system assessment. While current evaluations emphasize correctness, this work focuses on measuring uncertainty and reliability. The authors converted open-ended generation tasks into multiple-choice questions to enable "principled uncertainty quantification via conformal prediction." Their testing of eight RAG methods revealed several key findings: accuracy improvements don't always reduce uncertainty, particularly when retrieval encounters noise; simpler modular approaches outperform complex reasoning pipelines in accuracy-uncertainty balance; and no single method proves universally dependable across different domains. The research further identifies how retrieval depth and confidence cues can intensify erroneous confident predictions and hallucinations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9758aa02-6808-4dd1-babb-e20bc29e6f2e",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "5044d9d7-3d0e-47d8-9044-362df1fbe615",
  "sourceToolAssistantUUID": "9758aa02-6808-4dd1-babb-e20bc29e6f2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-30T06:19:07.996Z_

<details><summary>↩ Tool result · `toolu_01JwFRzo4XTfPsem6XgZvSSQ`</summary>

```text
# Paper Details

**Title:** "The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems"

**Author:** Debu Sinha

**Venue/Date:** arXiv:2512.15068 (cs.LG); submitted December 17, 2025, revised December 18, 2025

**Abstract Summary:**

This research investigates hallucination detection in RAG systems using conformal prediction methods. The study reveals a critical limitation: embedding-based approaches excel on synthetic hallucinations but "fail catastrophically" on real hallucinations from RLHF-aligned models. 

The key finding demonstrates that while certain hallucinations remain "semantically indistinguishable from faithful responses," GPT-4 achieves only 7% false positive rates on the same data. The authors term this phenomenon the "Semantic Illusion"—indicating that surface-level semantic analysis cannot reliably detect certain hallucinations, though reasoning-based approaches can solve the task. This suggests embedding methods have fundamental limitations that prevent them from handling nuanced hallucination detection in safety-critical applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af92b13d-a514-4f86-a1f0-72015a041cee",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "0de87271-6f02-4038-8ed8-5daa0bea6e74",
  "sourceToolAssistantUUID": "af92b13d-a514-4f86-a1f0-72015a041cee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-30T06:19:08.103Z_

<details><summary>↩ Tool result · `toolu_01Sz97gVbGFU74vPorAYScWj`</summary>

```text
# Paper Information

**Full Title:** "Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation"

**Authors:** Ekaterina Fadeeva, Aleksandr Rubashevskii, Dzianis Piatrashyn, Roman Vashurin, Shehzaad Dhuliawala, Artem Shelmanov, Timothy Baldwin, Preslav Nakov, Mrinmaya Sachan, Maxim Panov

**Venue & Date:** arXiv (Computer Science > Computation and Language), submitted May 27, 2025; latest revision April 29, 2026 (arXiv:2505.21072)

**Abstract Summary:** 
The paper addresses hallucinations in retrieval-augmented generation systems. The authors propose FRANQ, a method that "applies distinct uncertainty quantification techniques to estimate factuality, conditioning on whether a statement is faithful to the retrieved context." They created an annotated dataset distinguishing factuality from faithfulness and demonstrated their approach outperforms existing methods at detecting factual errors across multiple datasets and language models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2f166ea-44ce-45fd-830b-e4acb1ac2034",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "b7490ecd-ffaa-4ad8-a3b5-0663b2dd15d5",
  "sourceToolAssistantUUID": "c2f166ea-44ce-45fd-830b-e4acb1ac2034",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-30T06:19:08.811Z_

<details><summary>↩ Tool result · `toolu_01McGTLSuVvyY7K5yFXu3o6L`</summary>

```text
# INTRYGUE Paper Details

**Full Title:** "INTRYGUE: Induction-Aware Entropy Gating for Reliable RAG Uncertainty Estimation"

**Authors:** Alexandra Bazarova, Andrei Volodichev, Daria Kotova, Alexey Zaytsev

**Venue & Date:** arXiv Computer Science > Artificial Intelligence (cs.AI); Submitted March 23, 2026

**Abstract Summary:** The research addresses uncertainty quantification failures in retrieval-augmented generation systems. The authors identify a mechanistic issue where "induction heads promote grounded responses by copying the correct answer" while simultaneously activating entropy neurons, inflating uncertainty signals on accurate outputs. They propose INTRYGUE, which gates predictive entropy using induction head activation patterns. The method was evaluated across four RAG benchmarks and six open-source language models (4B-13B parameters), demonstrating improved hallucination detection by combining predictive uncertainty with internal context utilization signals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63e6e095-ffef-4368-8b6f-ed752c5b672b",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a083061a3b1788628",
  "type": "user",
  "uuid": "42e959c6-ac6e-457d-8510-ff7e65b1eb37",
  "sourceToolAssistantUUID": "63e6e095-ffef-4368-8b6f-ed752c5b672b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-30T06:20:45.151Z_

Now I have comprehensive results. Here is the structured list of papers found.

---

## Structured List of Papers (2024--2026) Citing or Building on the Seed Papers

Papers are organized into three thematic clusters matching your focus areas.

---

### CLUSTER A: Certified Defenses and Formal Guarantees for RAG

**1. RobustRAG: Certifiably Robust RAG against Retrieval Corruption**
- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal
- **Venue:** arXiv:2405.15556 (submitted May 2024; revised April 2026). Presented at ICML 2024 workshop track.
- **URL:** https://arxiv.org/abs/2405.15556
- **Why important:** First certified defense for RAG against retrieval corruption; provides formal robustness certificates via an isolate-then-aggregate strategy. Directly extends the C-RAG line of work.
- **One-line summary:** Partitions retrieved passages into isolated groups, generates responses independently per group, and securely aggregates them, achieving 38% certifiable robust accuracy while maintaining 71% clean accuracy.

**2. RAGDefender -- Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems**
- **Authors:** Minseok Kim, Hankook Lee, Hyungjoon Koo
- **Venue:** ACSAC 2025 (Annual Computer Security Applications Conference); arXiv:2511.01268 (November 2025)
- **URL:** https://arxiv.org/abs/2511.01268
- **Why important:** Lightweight post-retrieval defense that outperforms RobustRAG, especially when poisoned passages outnumber clean ones. Directly benchmarks against both PoisonedRAG and RobustRAG.
- **One-line summary:** Identifies and removes poisoned content during post-retrieval without extra training, reducing attack success on Gemini from 0.89 to 0.02.

**3. Towards Poisoning Robustness Certification for Natural Language Generation**
- **Authors:** Mihnea Ghitu, Matthew Wicker
- **Venue:** arXiv:2602.09757 (February 2026)
- **URL:** https://arxiv.org/abs/2602.09757
- **Why important:** First algorithm (Targeted Partition Aggregation) to certify validity against targeted poisoning attacks in NLG. Extends certified robustness ideas from C-RAG/RobustRAG to the generation pipeline itself.
- **One-line summary:** Computes minimum poisoning budget to induce harmful outputs and certifies stability/validity properties for LLM generation under data poisoning, including multi-turn agent settings.

**4. SDAG -- Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention**
- **Authors:** Sagie Dekel, Moshe Tennenholtz, Oren Kurland
- **Venue:** arXiv:2602.04711 (February 2026)
- **URL:** https://arxiv.org/abs/2602.04711
- **Why important:** Architectural defense against PoisonedRAG-style attacks that requires no fine-tuning; complements RobustRAG's aggregation approach with attention-mask isolation.
- **One-line summary:** Enforces block-sparse attention so tokens in one retrieved document cannot attend to tokens in another, eliminating cross-document poisoning influence without model changes.

**5. Provably Secure Retrieval-Augmented Generation**
- **Authors:** Pengcheng Zhou, Yinglun Feng, Zhongliang Yang
- **Venue:** arXiv:2508.01084 (August 2025)
- **URL:** https://arxiv.org/abs/2508.01084
- **Why important:** First formally verified encryption-based RAG framework ensuring both confidentiality and integrity with computational security proofs.
- **One-line summary:** Proposes a pre-storage full-encryption scheme for retrieved content and vector embeddings with formal security proofs for confidentiality and integrity.

---

### CLUSTER B: Poisoning Attacks and Defenses for RAG (Building on PoisonedRAG)

**6. RAGForensics -- Traceback of Poisoning Attacks to Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu
- **Venue:** The Web Conference 2025 (WWW '25); arXiv:2504.21668
- **URL:** https://arxiv.org/abs/2504.21668
- **Why important:** First traceback system for RAG poisoning; complements defense-at-inference (RobustRAG) with post-hoc forensic identification of malicious documents.
- **One-line summary:** Iteratively retrieves subsets and uses LLM-guided prompts to detect poisoned texts in a knowledge database, remaining robust to adaptive attacks.

**7. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in RAG**
- **Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang
- **Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral); arXiv:2512.24268 (December 2025)
- **URL:** https://arxiv.org/abs/2512.24268
- **Why important:** Operates at retrieval stage (unlike post-retrieval defenses); RAGPart exploits document partitioning to reduce poisoned influence, and RAGMask uses token masking to detect suspicious tokens.
- **One-line summary:** Two complementary retrieval-stage defenses -- partitioning documents and masking suspicious tokens -- that reduce PoisonedRAG-style attack success while preserving normal performance.

**8. Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems**
- **Authors:** Scott Thornton
- **Venue:** arXiv:2603.18034 (March 2026)
- **URL:** https://arxiv.org/abs/2603.18034
- **Why important:** Demonstrates that PoisonedRAG-style attacks are corpus-dependent and that hybrid retrieval (BM25 + vector) can reduce attack success from 38% to 0% without modifying the LLM.
- **One-line summary:** Shows dual-document poisoning attacks have variable success rates (47--93%) across LLM families and that hybrid retrieval is a simple but effective defense.

**9. Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents**
- **Authors:** Avital Shafran, Roei Schuster, Vitaly Shmatikov
- **Venue:** USENIX Security 2025; arXiv:2406.05870
- **URL:** https://arxiv.org/abs/2406.05870
- **Why important:** Introduces a new attack modality (denial-of-service via single blocker documents) complementary to PoisonedRAG's targeted misinformation; highlights that safety metrics miss this threat.
- **One-line summary:** A single adversarial "blocker" document injected into a RAG database causes the system to refuse answering targeted queries, using black-box optimization without knowing the embedding or LLM.

---

### CLUSTER C: Conformal Prediction, Distribution Shift, and Uncertainty in RAG/NLP

**10. Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction**
- **Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh
- **Venue:** ECIR 2026; arXiv:2511.17908 (November 2025)
- **URL:** https://arxiv.org/abs/2511.17908
- **Why important:** Directly extends TRAQ by using conformal prediction for coverage-controlled context filtering in RAG. Explicitly discusses relaxing exchangeability assumptions as future work.
- **One-line summary:** Applies conformal prediction to filter irrelevant retrieved context while guaranteeing a target fraction of relevant snippets are retained, reducing context by 2--3x and improving factual accuracy.

**11. CONFLARE: CONFormal LArge language model REtrieval**
- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson
- **Venue:** arXiv:2404.04287 (April 2024)
- **URL:** https://arxiv.org/abs/2404.04287
- **Why important:** Operationalizes conformal prediction for RAG retrieval with an open-source package; establishes similarity thresholds at user-specified error rates with statistical guarantees.
- **One-line summary:** Framework that calibrates embedding similarity thresholds via conformal prediction to guarantee that retrieved chunks contain the correct answer at a specified confidence level.

**12. Streamlining Conformal Information Retrieval via Score Refinement**
- **Authors:** Yotam Intrator, Ori Kelner, Regev Cohen, Roman Goldenberg, Ehud Rivlin, Daniel Freedman
- **Venue:** arXiv:2410.02914 (October 2024)
- **URL:** https://arxiv.org/abs/2410.02914
- **Why important:** Addresses the practical bottleneck that conformal prediction produces overly large retrieval sets; proposes monotone score transformations to shrink sets while preserving coverage guarantees.
- **One-line summary:** A simple monotone transformation of retrieval scores significantly reduces conformal prediction set sizes while maintaining statistical coverage guarantees on BEIR benchmarks.

**13. Domain-Shift-Aware Conformal Prediction for Large Language Models (DS-CP)**
- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz
- **Venue:** arXiv:2510.05566 (October 2025)
- **URL:** https://arxiv.org/abs/2510.05566
- **Why important:** Directly addresses exchangeability violations in conformal prediction for LLMs by reweighting calibration samples based on proximity to test prompts. Highly relevant to adversarial distribution shift in RAG.
- **One-line summary:** Reweights conformal calibration samples by test-prompt proximity to maintain valid coverage under domain shift, demonstrating more reliable coverage than standard CP on MMLU.

**14. Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift**
- **Authors:** Farbod Siahkali, Ashwin Verma, Vijay Gupta
- **Venue:** arXiv:2602.14913 (February 2026)
- **URL:** https://arxiv.org/abs/2602.14913
- **Why important:** Provides formal coverage lower bounds under bounded label-conditional covariate shift, directly applicable to scenarios where RAG retrieval introduces distribution shift.
- **One-line summary:** Derives coverage lower bounds under covariate shift using Wasserstein distances and proposes a slack-parameter method for adjusting conformal thresholds to maintain target coverage.

**15. Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations**
- **Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang
- **Venue:** arXiv:2604.16217 (April 2026)
- **URL:** https://arxiv.org/abs/2604.16217
- **Why important:** Proposes using internal LLM representations as nonconformity scores instead of surface-level outputs, achieving better validity-efficiency tradeoffs especially under distribution shift.
- **One-line summary:** Layer-wise information scores from internal model representations serve as more robust nonconformity measures than output-based alternatives, improving conformal prediction under distribution shift.

**16. Learning Conformal Abstention Policies for Adaptive Risk Management in LLMs**
- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi
- **Venue:** arXiv:2502.06884 (February 2025)
- **URL:** https://arxiv.org/abs/2502.06884
- **Why important:** Extends conformal prediction from static to adaptive abstention thresholds via reinforcement learning; directly relevant to abstention frameworks for RAG with formal coverage guarantees.
- **One-line summary:** Integrates RL with conformal prediction to learn dynamic abstention thresholds, improving hallucination detection AUROC by 22% and reducing calibration error by 70--85% while maintaining 90% coverage.

**17. The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems**
- **Authors:** Debu Sinha
- **Venue:** arXiv:2512.15068 (December 2025)
- **URL:** https://arxiv.org/abs/2512.15068
- **Why important:** Uses conformal prediction to study fundamental limits of embedding-based hallucination detection in RAG, finding that real hallucinations from RLHF-aligned models are semantically indistinguishable from faithful responses.
- **One-line summary:** Demonstrates that embedding-based hallucination detectors with conformal guarantees fail on real (vs. synthetic) hallucinations due to a "Semantic Illusion" -- surface semantics cannot distinguish them.

**18. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**
- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang
- **Venue:** arXiv:2603.19281 (March 2026)
- **URL:** https://arxiv.org/abs/2603.19281
- **Why important:** Comprehensive benchmark using conformal prediction (LAC, APS) to evaluate uncertainty in 8 RAG methods; reveals that accuracy improvements do not always reduce uncertainty.
- **One-line summary:** Converts open-ended RAG tasks to multiple-choice format for principled conformal uncertainty quantification, finding that no single RAG method is universally dependable and that retrieval noise inflates uncertainty.

**19. Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of RAG (FRANQ)**
- **Authors:** Ekaterina Fadeeva, Aleksandr Rubashevskii, Dzianis Piatrashyn, Roman Vashurin, Shehzaad Dhuliawala, Artem Shelmanov, Timothy Baldwin, Preslav Nakov, Mrinmaya Sachan, Maxim Panov
- **Venue:** arXiv:2505.21072 (May 2025; revised April 2026)
- **URL:** https://arxiv.org/abs/2505.21072
- **Why important:** Disentangles factuality from faithfulness in RAG uncertainty quantification, applying distinct UQ techniques conditioned on whether a statement is faithful to retrieved context.
- **One-line summary:** Conditions uncertainty quantification on faithfulness to retrieved context, outperforming existing methods at detecting factual errors across multiple RAG datasets.

---

### BONUS: Survey Papers

**20. Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions**
- **Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen
- **Venue:** arXiv:2604.08304 (April 2026)
- **URL:** https://arxiv.org/abs/2604.08304
- **Why important:** Comprehensive taxonomy (SLOT framework) mapping all known RAG attacks/defenses onto a six-stage pipeline; identifies structural gaps in current defenses.
- **One-line summary:** Introduces the SLOT framework organizing RAG security literature by attack Surface, defense Layer, security Objective (CIA), and Target scope across a six-stage knowledge-access pipeline.

**21. Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey**
- **Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, et al. (20+ authors)
- **Venue:** arXiv:2502.06872 (February 2025)
- **URL:** https://arxiv.org/abs/2502.06872
- **Why important:** Comprehensive survey on trustworthy RAG covering reliability, privacy, safety, fairness, explainability, and accountability -- contextualizes all the seed papers within the broader landscape.
- **One-line summary:** Presents a roadmap for trustworthy RAG organized around six key dimensions with taxonomies and frameworks for each perspective.

---

### Summary of Coverage

| Focus Area | Papers Found |
|---|---|
| Conformal prediction extended to adversarial/poisoning settings in RAG | #3, #10, #12, #13, #14, #15, #17 |
| Certified defenses for RAG with formal guarantees | #1, #2, #3, #4, #5 |
| Distribution shift / exchangeability violations in CP for NLP | #13, #14, #15 |
| Abstention frameworks with guarantees | #16, #17 |
| RAG poisoning attacks and defenses (building on PoisonedRAG) | #2, #4, #6, #7, #8, #9 |
| Uncertainty quantification for RAG | #18, #19 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42e959c6-ac6e-457d-8510-ff7e65b1eb37",
  "isSidechain": true,
  "agentId": "a083061a3b1788628",
  "requestId": "req_011CbYGVW7Lw6MKCj7S6Uh3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80ce3f09-12ff-41dc-9578-3c584e2b1e0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012W15LVxt1hsFwjKn937KFn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3763,
      "cache_read_input_tokens": 29579,
      "output_tokens": 4439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3763
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4439,
          "cache_read_input_tokens": 29579,
          "cache_creation_input_tokens": 3763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3763,
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
