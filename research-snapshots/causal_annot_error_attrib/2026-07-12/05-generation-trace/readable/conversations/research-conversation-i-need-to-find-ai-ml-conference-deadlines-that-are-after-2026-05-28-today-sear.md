# Research conversation: I need to find AI/ML conference deadlines that are AFTER 2026-05-28 (today). Search for the following venues and their 2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac0166e9888b16594.jsonl`
- **Structured JSON:** [`c49c76331108df26483c.json`](../../sessions/c4/c49c76331108df26483c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-28T11:34:19.887Z_

I need to find AI/ML conference deadlines that are AFTER 2026-05-28 (today). Search for the following venues and their 2026/2027 paper submission deadlines:

1. AAAI 2027 - search "AAAI 2027 call for papers deadline"
2. NeurIPS 2026 - search "NeurIPS 2026 submission deadline"
3. ICLR 2027 - search "ICLR 2027 submission deadline"
4. ACL 2027 - search "ACL 2027 submission deadline"
5. EMNLP 2026 - search "EMNLP 2026 submission deadline"
6. ICML 2026 - search "ICML 2026 submission deadline" (probably already passed, but check)
7. NAACL 2027 - search "NAACL 2027 deadline"
8. COLM 2026 - search "COLM 2026 submission deadline"
9. AISTATS 2027 - search "AISTATS 2027 deadline"

For each venue, report:
- Abstract deadline (if any)
- Full paper deadline
- Whether the deadline is before or after 2026-05-28
- Conference dates
- Whether they accept work on LLM evaluation/benchmarking

Only include venues whose deadlines have NOT yet passed as of 2026-05-28.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "05491b4a-eb20-40e6-8a9c-2da282505fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T11:34:19.895Z_

```json
{
  "parentUuid": "05491b4a-eb20-40e6-8a9c-2da282505fbe",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
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
  "uuid": "13f64d45-79ac-4d61-8de1-1427ec17182d",
  "timestamp": "2026-05-28T11:34:19.895Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T11:34:19.897Z_

```json
{
  "parentUuid": "13f64d45-79ac-4d61-8de1-1427ec17182d",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c1fcb46e-e922-4ca1-afe5-a75faaee77ec",
  "timestamp": "2026-05-28T11:34:19.897Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T11:34:23.704Z_



I'll search for all these conference deadlines in parallel. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1fcb46e-e922-4ca1-afe5-a75faaee77ec",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuh2mdiq8LbFDLLnCh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82cf04df-778d-4161-87e2-0a4b65d9306e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Prb9n4sJ2vhfQfdVFF8vCv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1657,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1657,
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

_source line 5 · 2026-05-28T11:34:23.860Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L8MR2VRxS4V4UmprUMNbmA`</summary>

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
  "parentUuid": "82cf04df-778d-4161-87e2-0a4b65d9306e",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuh2mdiq8LbFDLLnCh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f674228-ccc2-46cc-b7e1-a4db09637a93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Prb9n4sJ2vhfQfdVFF8vCv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1657,
      "cache_read_input_tokens": 7407,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1657
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1657,
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

_source line 6 · 2026-05-28T11:34:23.863Z_

<details><summary>↩ Tool result · `toolu_01L8MR2VRxS4V4UmprUMNbmA`</summary>

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
  "parentUuid": "5f674228-ccc2-46cc-b7e1-a4db09637a93",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "77c47df1-5b2e-4e60-b51d-450d3639228f",
  "sourceToolAssistantUUID": "5f674228-ccc2-46cc-b7e1-a4db09637a93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T11:34:30.557Z_



Now let me search for all 9 conferences in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77c47df1-5b2e-4e60-b51d-450d3639228f",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd3ce33f-7218-440f-996a-f3def1fa77d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 8 · 2026-05-28T11:34:30.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EVFXTg4GQB19WH1cnBqkiL`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd3ce33f-7218-440f-996a-f3def1fa77d4",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbbce65b-4770-4f04-8651-64e16ad46c3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 9 · 2026-05-28T11:34:31.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DDnd7GdHPzAZyVjCWKEeLK`</summary>

```json
{
  "query": "NeurIPS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbbce65b-4770-4f04-8651-64e16ad46c3a",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17a944a4-4011-4023-81f0-8677fa811712",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 10 · 2026-05-28T11:34:31.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TDTWmk74pwyfYqgZCdo3gN`</summary>

```json
{
  "query": "ICLR 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a944a4-4011-4023-81f0-8677fa811712",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8586156e-40dc-43ea-b97c-25afbb158861",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 11 · 2026-05-28T11:34:31.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAw9bwoBVX3bmnmz94QnZg`</summary>

```json
{
  "query": "ACL 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8586156e-40dc-43ea-b97c-25afbb158861",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c3affbb-b440-4291-9a69-2b7096c911c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 12 · 2026-05-28T11:34:31.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fcj3ZckU3sWvgKkk94o3fs`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c3affbb-b440-4291-9a69-2b7096c911c7",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc8761d2-4685-496c-905b-63f35c6f98de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 13 · 2026-05-28T11:34:32.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AB6uFiqgmMa9Gpr2g8aTUg`</summary>

```json
{
  "query": "ICML 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc8761d2-4685-496c-905b-63f35c6f98de",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d233dcad-ab4f-4996-872a-6f66badf92eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 14 · 2026-05-28T11:34:32.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FmHVfpmaayzBu4JTz6n1SQ`</summary>

```json
{
  "query": "NAACL 2027 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d233dcad-ab4f-4996-872a-6f66badf92eb",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92bb6279-0a6c-4d08-b1ae-1ce3cc4072cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 15 · 2026-05-28T11:34:32.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4Urwv82ANmKbmVP4zMEQm`</summary>

```json
{
  "query": "COLM 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92bb6279-0a6c-4d08-b1ae-1ce3cc4072cf",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "044cb31f-e5ce-47e8-86ac-968ff2c99a70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 628,
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

_source line 16 · 2026-05-28T11:34:33.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015cqQkq3Zx7xx2fUJEQFuFv`</summary>

```json
{
  "query": "AISTATS 2027 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "044cb31f-e5ce-47e8-86ac-968ff2c99a70",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtuz7vXWxVxLLv66yTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5420917d-a38a-4252-86af-9486fe4001a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgxi8YMXDaQxgkxQnMSPY5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 9064,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 425,
          "cache_read_input_tokens": 9064,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 628,
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

_source line 17 · 2026-05-28T11:34:35.444Z_

<details><summary>↩ Tool result · `toolu_01TDTWmk74pwyfYqgZCdo3gN`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, I found that ICLR 2027 is predicted to be held on July 31, 2027, with the location to be announced (TBA), based on the 2026 schedule pattern. However, you should verify this on the official conference website as these are predictions rather than confirmed official deadlines.

The search results did not contain a specific submission deadline date for ICLR 2027. For the most current and official information about submission deadlines for ICLR 2027, I recommend checking the official ICLR website at iclr.cc once the call for papers is formally announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8586156e-40dc-43ea-b97c-25afbb158861",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "b9670f60-9eec-4b44-8786-71eb4b2b7a72",
  "sourceToolAssistantUUID": "8586156e-40dc-43ea-b97c-25afbb158861",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T11:34:35.564Z_

<details><summary>↩ Tool result · `toolu_01NAw9bwoBVX3bmnmz94QnZg`</summary>

```text
Web search results for query: "ACL 2027 submission deadline"

Links: [{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Association - 📢 We are thrilled to announce that the official ...","url":"https://www.facebook.com/aclmeeting/photos/-we-are-thrilled-to-announce-that-the-official-website-for-the-20th-conference-o/1290337343275281/"},{"title":"Second Call for SemEval Task Proposals 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/second-call-semeval-task-proposals-2027"}]

Based on the search results, here's the information about ACL 2027 submission deadlines:

For EACL 2027, the final ARR (ACL Rolling Review) submission date is August 3, 2026, with a commitment date of October 11, 2026.

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Note that starting from 2024, all main *ACL conferences use ARR exclusively, so submissions to ACL 2027 must go through the ACL Rolling Review platform rather than through direct submission to the conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c3affbb-b440-4291-9a69-2b7096c911c7",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "34721f9a-2a50-48ca-9f05-dd194f2c12db",
  "sourceToolAssistantUUID": "5c3affbb-b440-4291-9a69-2b7096c911c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T11:34:35.600Z_

<details><summary>↩ Tool result · `toolu_01DDnd7GdHPzAZyVjCWKEeLK`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"}]

Based on the search results, here are the key submission deadlines for NeurIPS 2026:

**Main Track:**
- Abstract submission deadline: May 4, 2026 (AOE)
- Full paper submission deadline, including all supplementary materials: May 6, 2026 AOE

**Evaluations & Datasets Track:**
- Abstract submission deadline: May 4, 2026 (AoE)
- Full paper submission deadline (including all supplementary materials): May 6, 2026 (AoE)

**Other Tracks:**
- Competition proposal submission deadline: May 15, 2026
- Workshop Application Deadline: June 06, 2026, AoE

Note that the different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines. All authors must have an OpenReview profile when submitting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17a944a4-4011-4023-81f0-8677fa811712",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "b620b45f-b494-4e13-9926-7bfb51f2a81f",
  "sourceToolAssistantUUID": "17a944a4-4011-4023-81f0-8677fa811712",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T11:34:35.906Z_

<details><summary>↩ Tool result · `toolu_01S4Urwv82ANmKbmVP4zMEQm`</summary>

```text
Web search results for query: "COLM 2026 submission deadline"

Links: [{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"COLM 2026: Call for Papers","url":"https://colmweb.org/cfp.html"},{"title":"COLM 2026: Submission Instructions","url":"https://colmweb.org/submission-instructions.html"},{"title":"Conference on Language Modeling on X: \"COLM 2026 is just around the corner! Mark your calendars for: 💡Abstract deadline: Thursday, March 26, 2026 📄Full paper submission deadline: Tuesday, March 31, 2026 Call for papers in thread (website coming soon). https://t.co/YfjLxzCqxO\" / X","url":"https://x.com/COLM_conf/status/2000952051212415394"},{"title":"Conference on Language Modeling (COLM), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-colm.html"},{"title":"When is COLM 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/colm"},{"title":"COLM 2026","url":"https://colmweb.org/"},{"title":"COLM 2026: Call for Workshops","url":"https://colmweb.org/cfw.html"},{"title":"COLM 2026 - Conference on Language Modeling Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/colm"},{"title":"Aviral Kumar on X: \"Submit your papers to COLM (deadline: March 31)!\" / X","url":"https://x.com/aviral_kumar2/status/2000963068717625813"}]

Based on the search results, here are the key submission deadlines for COLM 2026:

**Main Conference Paper Submissions:**
- Abstract deadline: Thursday, March 26, 2026
- Full paper submission deadline: Tuesday, March 31, 2026

**Workshop Submissions:**
- Suggested submission deadline for workshop contributions: June 23, 2026

COLM 2026 will take place at the Hilton Union Square in San Francisco, USA from October 6-9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "044cb31f-e5ce-47e8-86ac-968ff2c99a70",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "1cb35ed7-3c00-46ad-b5a9-c6f886ad1b23",
  "sourceToolAssistantUUID": "044cb31f-e5ce-47e8-86ac-968ff2c99a70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T11:34:36.039Z_

<details><summary>↩ Tool result · `toolu_01Fcj3ZckU3sWvgKkk94o3fs`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, here is the information about the EMNLP 2026 submission deadline:

The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12). The conference will be held in Budapest, Hungary from October 24th to October 29th, 2026.

The submission is through ACL Rolling Review (ARR).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc8761d2-4685-496c-905b-63f35c6f98de",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "d46d86d5-3d76-47af-ac98-1b4ed8c226a5",
  "sourceToolAssistantUUID": "dc8761d2-4685-496c-905b-63f35c6f98de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T11:34:36.088Z_

<details><summary>↩ Tool result · `toolu_01EVFXTg4GQB19WH1cnBqkiL`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline"

Links: [{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Ethical and Social Considerations of Applying Artificial Intelligence in Healthcare; a Two-Pronged Scoping Review","url":"https://www.medrxiv.org/content/10.1101/2025.02.10.25321994.full.pdf"}]

Based on the search results, here's what I found about the AAAI 2027 call for papers deadline:

For the Main Technical Track, abstracts are due July 21, 2026 at 11:59 PM UTC-12, and full papers are due July 28, 2026 at 11:59 PM UTC-12. Supplementary material and code are due July 31, 2026 by 11:59 PM UTC-12.

The Open Review submission site opens for author registration on June 17, 2026, and opens for paper submission on June 24, 2026.

It's worth noting that deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective CFP. AAAI-27 will be held in Montréal, Canada, from February 16 to February 23, 2027.

For the most up-to-date information, you can visit the official AAAI 2027 call for papers at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbbce65b-4770-4f04-8651-64e16ad46c3a",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "40c81c51-44fc-45d9-a8f6-70d404b0b92a",
  "sourceToolAssistantUUID": "dbbce65b-4770-4f04-8651-64e16ad46c3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T11:34:37.188Z_

<details><summary>↩ Tool result · `toolu_01FmHVfpmaayzBu4JTz6n1SQ`</summary>

```text
Web search results for query: "NAACL 2027 deadline"

Links: [{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"naacl 2027 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=naacl27"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"},{"title":"NAACL HLT 2027 (@naaclmeeting) / Posts / X","url":"https://x.com/naaclmeeting"},{"title":"Links - Human Language Intelligence Lab","url":"https://hli.skku.edu/links"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"}]

Based on the search results, here's what I found about NAACL 2027:

NAACL 2027 is scheduled for April 29 - May 4, 2027. However, the specific submission deadline has not yet been officially announced. 

The deadline information is predicted based on previous year schedules, and it's recommended that you verify on the official conference website.

For reference, NAACL paper submission deadlines are usually in December, and the conference is usually held in June (though the 2027 dates appear to be in late April/early May based on recent scheduling patterns).

For the most accurate and up-to-date deadline information, I recommend checking the official NAACL website at naacl.org or the 2027 conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92bb6279-0a6c-4d08-b1ae-1ce3cc4072cf",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "a5bd3cbe-92d2-42cf-a9db-99d83bcec506",
  "sourceToolAssistantUUID": "92bb6279-0a6c-4d08-b1ae-1ce3cc4072cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T11:34:37.703Z_

<details><summary>↩ Tool result · `toolu_01AB6uFiqgmMa9Gpr2g8aTUg`</summary>

```text
Web search results for query: "ICML 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"}]

Based on the search results, here is the information about the ICML 2026 submission deadline:

## ICML 2026 Paper Submission Deadlines

The submission deadline for ICML 2026 papers is January 28, 2026. 

There are actually two key deadlines for paper submissions:

1. **Abstract Submission Deadline**: January 24, 2026, 12 Noon UTC-0 (AoE)
2. **Full Paper Submission Deadline**: January 28, 2026

Abstract and paper submission deadlines are strict, and in no circumstances will extensions be given.

For position papers specifically, the submission deadline is January 29, 2026, 12 Noon UTC-0 (AoE).

Additional information:
- The conference will be held July 6th through July 11th, 2026 at the Coex Convention & Exhibition Center.
- Papers must be submitted as a single file: 8 pages for the main paper, with unlimited pages for references, the impact statement, and appendices.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d233dcad-ab4f-4996-872a-6f66badf92eb",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "da4b2bb6-e560-4b8d-9814-6c3bb099c771",
  "sourceToolAssistantUUID": "d233dcad-ab4f-4996-872a-6f66badf92eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T11:34:37.834Z_

<details><summary>↩ Tool result · `toolu_015cqQkq3Zx7xx2fUJEQFuFv`</summary>

```text
Web search results for query: "AISTATS 2027 deadline"

Links: [{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"aistats 2026","url":"https://virtual.aistats.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"2026 Dates and Deadlines","url":"https://virtual.aistats.org/Conferences/2026/Dates"},{"title":"Home| Society for Artificial Intelligence and Statistics","url":"https://aistats.org/"},{"title":"Meetings| Society for Artificial Intelligence and Statistics","url":"https://aistats.org/other.html"},{"title":"Upcoming Conferences | Conference List","url":"https://conferencelist.info/upcoming/"},{"title":"https://ivader.unist.ac.kr/importantDates","url":"https://ivader.unist.ac.kr/importantDates"},{"title":"Call for Papers: AISTATS 2026","url":"https://virtual.aistats.org/Conferences/2026/CallForPapers"}]

Based on the search results, here's what I found about AISTATS 2027:

AISTATS 2027 is scheduled for May 2-5, 2027, and the conference will be held in Montréal, Canada.

However, the specific submission deadline is predicted based on previous year schedule, and it is recommended to verify on the official conference website. The search results do not contain the exact submission deadlines for AISTATS 2027 yet, as these details are typically announced closer to the conference date.

For reference, AISTATS 2026 had these deadlines:
- Abstract submission deadline: September 25, 2025 AOE
- Full paper submission deadline: October 2, 2025 AOE

I recommend checking the official AISTATS website (aistats.org) periodically for the official AISTATS 2027 call for papers and submission deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5420917d-a38a-4252-86af-9486fe4001a0",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "c4099c37-7734-407c-99ea-a031fe344d46",
  "sourceToolAssistantUUID": "5420917d-a38a-4252-86af-9486fe4001a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T11:34:41.532Z_

Let me do a few follow-up searches for more details on venues where I need additional information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4099c37-7734-407c-99ea-a031fe344d46",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtw1Zmgvn4M3CZZds5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b16dd7ad-108a-4574-a5e9-0523f949cd48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNjpxxaawkYAjyric5S8G3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6381,
      "cache_read_input_tokens": 9692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6381,
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

_source line 27 · 2026-05-28T11:34:42.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ANESCJofH1YQDoSZQ4Tdb7`</summary>

```json
{
  "query": "ACL 2027 conference dates location ARR deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b16dd7ad-108a-4574-a5e9-0523f949cd48",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtw1Zmgvn4M3CZZds5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b021be0-0fd9-4fd1-9ca5-be8ecdaa973c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNjpxxaawkYAjyric5S8G3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6381,
      "cache_read_input_tokens": 9692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6381,
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

_source line 28 · 2026-05-28T11:34:42.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xpq9cRHucTXa1oUeoDKoZe`</summary>

```json
{
  "query": "NAACL 2027 ARR submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b021be0-0fd9-4fd1-9ca5-be8ecdaa973c",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtw1Zmgvn4M3CZZds5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dea76a13-af3c-402f-a060-b38a5cd6e78f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNjpxxaawkYAjyric5S8G3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6381,
      "cache_read_input_tokens": 9692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6381,
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

_source line 29 · 2026-05-28T11:34:43.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019QrrxBEcTxe2kJ2BZRzADP`</summary>

```json
{
  "query": "AISTATS 2027 call for papers submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dea76a13-af3c-402f-a060-b38a5cd6e78f",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtw1Zmgvn4M3CZZds5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e274728-7fcf-4332-9c7c-e3aefc716997",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNjpxxaawkYAjyric5S8G3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6381,
      "cache_read_input_tokens": 9692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6381,
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

_source line 30 · 2026-05-28T11:34:43.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XkD3nhPKcotbhyaUY7sJoC`</summary>

```json
{
  "query": "EMNLP 2026 ARR commitment deadline dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e274728-7fcf-4332-9c7c-e3aefc716997",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtw1Zmgvn4M3CZZds5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d03aebdd-7c7b-406e-acae-53ad558c7464",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNjpxxaawkYAjyric5S8G3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6381,
      "cache_read_input_tokens": 9692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6381,
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

_source line 31 · 2026-05-28T11:34:44.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0115JQcong4R9Kjq5TDSHwft`</summary>

```json
{
  "query": "ICLR 2027 call for papers dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d03aebdd-7c7b-406e-acae-53ad558c7464",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtw1Zmgvn4M3CZZds5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f53dfb94-4802-4a4e-b436-1ea801230822",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNjpxxaawkYAjyric5S8G3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6381,
      "cache_read_input_tokens": 9692,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 9692,
          "cache_creation_input_tokens": 6381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6381,
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

_source line 32 · 2026-05-28T11:34:46.792Z_

<details><summary>↩ Tool result · `toolu_01ANESCJofH1YQDoSZQ4Tdb7`</summary>

```text
Web search results for query: "ACL 2027 conference dates location ARR deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_date&sort=desc"},{"title":"AI Conference Deadlines","url":"https://hlr.github.io/deadlines/"},{"title":"Annual Meetings of the Association for Computational Linguistics | ACL Member Portal","url":"https://www.aclweb.org/portal/acl"}]

Based on the search results, here's what I found regarding ACL 2027:

## EACL 2027 (European Chapter of ACL)
The ARR submission deadline for long and short papers is August 3, 2026, and all deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth"). The conference itself will be held in Athens, Greece from March 9-14, 2027.

## Main ACL 2027
For the main ACL conference in 2027, the search results indicate it is predicted to be in July 2027 with location TBA, based on historical pattern.

Note that specific details for the main ACL 2027 conference (such as exact dates and location) are not yet fully confirmed, though predictions suggest it will follow the typical July timeframe based on previous years' schedules.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b021be0-0fd9-4fd1-9ca5-be8ecdaa973c",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "d0a54da9-fe1b-49a7-b939-7b5ead8fb625",
  "sourceToolAssistantUUID": "3b021be0-0fd9-4fd1-9ca5-be8ecdaa973c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T11:34:47.513Z_

<details><summary>↩ Tool result · `toolu_019QrrxBEcTxe2kJ2BZRzADP`</summary>

```text
Web search results for query: "AISTATS 2027 call for papers submission deadline"

Links: [{"title":"aistats 2026","url":"https://virtual.aistats.org/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"2026 Dates and Deadlines","url":"https://virtual.aistats.org/Conferences/2026/Dates"},{"title":"Call for Papers: AISTATS 2026","url":"https://virtual.aistats.org/Conferences/2026/CallForPapers"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Submission FAQ","url":"https://virtual.aistats.org/Conferences/2026/SubmissionFAQ"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Area Chair (AC) Guidelines","url":"https://virtual.aistats.org/Conferences/2026/ACGuidelines"},{"title":"Call for Papers| Artificial Intelligence and Statistics Conference","url":"http://aistats.org/aistats2023/call-for-papers.html"},{"title":"Computer Science conferences timeline","url":"https://lucjaulmes.github.io/cfp-timeline/"}]

Based on the search results, I found information about AISTATS 2027. AISTATS 2027 will be held February 16-23, 2027 in Montréal, Québec, Canada.

However, the specific submission deadline for the call for papers for AISTATS 2027 is not yet available in the search results. The search results primarily contain information about AISTATS 2026, which has already passed its submission deadlines. Since AISTATS 2027 is still several months away, the detailed call for papers with specific submission deadlines has likely not yet been officially announced.

To find the AISTATS 2027 call for papers and submission deadline, I recommend checking the official AISTATS website directly once the call for papers is released, which typically happens several months before the conference date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e274728-7fcf-4332-9c7c-e3aefc716997",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "9dd87f75-bfa2-4a75-8184-fd69f6a6c493",
  "sourceToolAssistantUUID": "8e274728-7fcf-4332-9c7c-e3aefc716997",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T11:34:47.984Z_

<details><summary>↩ Tool result · `toolu_01Xpq9cRHucTXa1oUeoDKoZe`</summary>

```text
Web search results for query: "NAACL 2027 ARR submission deadline commitment deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Submission Dates and Process for EACL/NAACL and ACL 2024 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/submission-dates-and-process-eaclnaacl-and-acl-2024"},{"title":"NAACL publications","url":"http://naacl.org/naacl-pubs/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, I found some information about NAACL and ARR deadlines, but the specific details for NAACL 2027 ARR submission and commitment deadlines are not yet published. Here's what I found:

NAACL 2027 is predicted to be held May 19-23, 2027, with details marked as "TBA" based on the 2026 schedule pattern, with a note to verify on the official conference website.

The search results show that after extensive deliberation and soliciting community feedback, the ACL Peer Review Committee recommended switching to 10-week review cycles, with the new schedule starting in May 2025. However, the specific ARR submission and commitment deadlines for NAACL 2027 have not yet been announced in these sources.

For the most current and official NAACL 2027 deadlines, I recommend checking:
- The official NAACL website
- The ACL Rolling Review (ARR) website at aclrollingreview.org
- The NAACL 2027 Call for Papers when it is published


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dea76a13-af3c-402f-a060-b38a5cd6e78f",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "9c4e7a09-cac6-4f59-8fb2-7d7140a147e5",
  "sourceToolAssistantUUID": "dea76a13-af3c-402f-a060-b38a5cd6e78f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T11:34:48.165Z_

<details><summary>↩ Tool result · `toolu_01XkD3nhPKcotbhyaUY7sJoC`</summary>

```text
Web search results for query: "EMNLP 2026 ARR commitment deadline dates"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Submitting to the May 19th ARR deadline? ✅ Make sure your profile is complete, including your DBLP link: https://t.co/jr60DoKZ2R 📄 Do not forget to review: (1) Author Guidelines https://t.co/QTDyAWZtKS (2) ACL Publication policy https://t.co/nImuaa9cez #NLProc #EMNLP25 #ARR\" / X","url":"https://x.com/emnlpmeeting/status/1923431912778895593"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org//calls/papers/"}]

Based on the search results, here are the key ARR commitment deadline dates for EMNLP 2026:

The EMNLP commitment deadline is August 2, 2026.

Additionally, here are the other important related dates:

- ARR submission deadline (long & short papers): May 25, 2026
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d03aebdd-7c7b-406e-acae-53ad558c7464",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "21f6496f-30e0-424c-8f2c-4b8ee7e94200",
  "sourceToolAssistantUUID": "d03aebdd-7c7b-406e-acae-53ad558c7464",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T11:34:49.165Z_

<details><summary>↩ Tool result · `toolu_0115JQcong4R9Kjq5TDSHwft`</summary>

```text
Web search results for query: "ICLR 2027 call for papers dates"

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"International Conference on Learning Representations ICLR on February 08-09, 2027 in Lisbon, Portugal - Conference Index","url":"https://conferenceindex.org/event/international-conference-on-learning-representations-iclr-2027-february-lisbon-pt"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning and Reinforcement ICLR in August 2027 in Barcelona","url":"https://waset.org/learning-and-reinforcement-conference-in-august-2027-in-barcelona"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"International Conference on Learning Representations (ICLR)","url":"https://waset.org/learning-representations-conference"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"}]

Based on the search results, I found information about call for papers dates for ICLR 2027. However, it's important to note that the results show multiple conferences using the ICLR acronym, including some organized by the World Academy of Science, Engineering and Technology (WASET). 

For the official ICLR (International Conference on Learning Representations), the 2027 conference is predicted to be held April 24-28, 2027, though specific dates are TBA and should be verified on the official conference website.

Additionally, the search results show several ICLR conferences organized by WASET scheduled for 2027 at different locations with different submission deadlines. For example, one ICLR event in Sydney has a paper submission deadline of April 01, 2026 with notification on May 01, 2026, and the conference date of August 30-31, 2027.

For the most accurate and official ICLR 2027 call for papers dates, I'd recommend checking the official ICLR website directly at iclr.cc, as the call for papers details may not yet be widely published given that today's date is May 28, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f53dfb94-4802-4a4e-b436-1ea801230822",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "e6ec0090-2e45-4b75-aa9b-12e29c37d686",
  "sourceToolAssistantUUID": "f53dfb94-4802-4a4e-b436-1ea801230822",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-28T11:34:51.596Z_

Now let me get more specific details on a couple more venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6ec0090-2e45-4b75-aa9b-12e29c37d686",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtwr2pBJ7ncJPm4xpGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afe220a2-7e53-4bd8-8bc6-0da9e0160a64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeQypozUnqzH6pkv4fxHf9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3970,
      "cache_read_input_tokens": 16073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3970,
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

_source line 38 · 2026-05-28T11:34:52.072Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016AZkDezyu7E3e2p6Qm9CGh`</summary>

```json
{
  "query": "AAAI 2027 topics LLM evaluation benchmarking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe220a2-7e53-4bd8-8bc6-0da9e0160a64",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtwr2pBJ7ncJPm4xpGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12782f02-cc23-478b-b0db-1b26cf5502b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeQypozUnqzH6pkv4fxHf9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3970,
      "cache_read_input_tokens": 16073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3970,
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

_source line 39 · 2026-05-28T11:34:53.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HoerLESJwxc2s83a2EzuFW`</summary>

```json
{
  "query": "NeurIPS 2026 datasets benchmarks track topics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12782f02-cc23-478b-b0db-1b26cf5502b5",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtwr2pBJ7ncJPm4xpGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "209b3e7f-719b-4bff-8ec1-8b035542c0ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeQypozUnqzH6pkv4fxHf9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3970,
      "cache_read_input_tokens": 16073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3970,
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

_source line 40 · 2026-05-28T11:34:53.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014sayNw2rAmyHJonmKrFuoW`</summary>

```json
{
  "query": "ACL 2027 dates location July 2027"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "209b3e7f-719b-4bff-8ec1-8b035542c0ca",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtwr2pBJ7ncJPm4xpGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "857784b8-e0c4-4918-baa6-850ddb7c4e32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeQypozUnqzH6pkv4fxHf9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3970,
      "cache_read_input_tokens": 16073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3970,
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

_source line 41 · 2026-05-28T11:34:53.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JifSVUyUmhKNzJFXGpxaZt`</summary>

```json
{
  "query": "NAACL 2027 location dates April May 2027"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "857784b8-e0c4-4918-baa6-850ddb7c4e32",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtwr2pBJ7ncJPm4xpGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5053246c-f554-4e5d-abab-3d351f4f98ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeQypozUnqzH6pkv4fxHf9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3970,
      "cache_read_input_tokens": 16073,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3970
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 16073,
          "cache_creation_input_tokens": 3970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3970,
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

_source line 42 · 2026-05-28T11:34:57.449Z_

<details><summary>↩ Tool result · `toolu_014sayNw2rAmyHJonmKrFuoW`</summary>

```text
Web search results for query: "ACL 2027 dates location July 2027"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Events | Austin City Limits Live","url":"https://www.acllive.com/events"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_date&sort=desc"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"Austin City Limits Music Festival | Oct 2-4 & 9-11, 2026 | Austin, TX","url":"https://www.aclfestival.com/"}]

Based on the search results, here's what I found about ACL 2027:

ACL 2027 is scheduled for July 2027, with the location TBA (To Be Announced). The dates are predicted based on historical pattern.

The search results indicate that specific location details have not yet been finalized. For reference, the most recent ACL conference (ACL 2026) took place in San Diego, California from July 2-7, 2026, so ACL 2027 will likely follow a similar timeframe in July, though the exact dates and venue are still to be determined.

I'd recommend checking the official ACL website (aclweb.org) for the most up-to-date information as it becomes available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "857784b8-e0c4-4918-baa6-850ddb7c4e32",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "bf508756-cd32-4915-8706-ebd35157d287",
  "sourceToolAssistantUUID": "857784b8-e0c4-4918-baa6-850ddb7c4e32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T11:34:57.703Z_

<details><summary>↩ Tool result · `toolu_01JifSVUyUmhKNzJFXGpxaZt`</summary>

```text
Web search results for query: "NAACL 2027 location dates April May 2027"

Links: [{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"},{"title":"NAACL HLT 2027 (@naaclmeeting) / Posts / X","url":"https://x.com/naaclmeeting"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"NAACL 2026 Albuquerque Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"naacl 2027 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=naacl27"}]

Based on the search results, I found information about NAACL 2027:

NAACL 2027 is scheduled for May 2-5, 2027, with the location to be announced (TBA), and the dates are predicted based on previous year schedules.

The search results indicate that the specific location for NAACL 2027 has not yet been announced, though the dates fall within the April-May 2027 timeframe you mentioned (specifically May 2-5).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5053246c-f554-4e5d-abab-3d351f4f98ff",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "4c35d7de-8d3a-4218-8528-663f4c70ac98",
  "sourceToolAssistantUUID": "5053246c-f554-4e5d-abab-3d351f4f98ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T11:34:59.673Z_

<details><summary>↩ Tool result · `toolu_016AZkDezyu7E3e2p6Qm9CGh`</summary>

```text
Web search results for query: "AAAI 2027 topics LLM evaluation benchmarking"

Links: [{"title":"Autonomous Evaluation of LLMs for Truth Maintenance and Reasoning Tasks","url":"https://arxiv.org/pdf/2410.08437"},{"title":"Debatable Intelligence: Benchmarking LLM Judges via Debate Speech Evaluation","url":"https://arxiv.org/pdf/2506.05062"},{"title":"Evaluating the Performance of Large Language Models via Debates","url":"https://arxiv.org/pdf/2406.11044"},{"title":"From Raw Corpora to Domain Benchmarks: Automated Evaluation of LLM Domain Expertise","url":"https://arxiv.org/pdf/2506.07658"},{"title":"Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs","url":"https://arxiv.org/pdf/2602.11674"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark","url":"https://arxiv.org/pdf/2406.19314"}]

Based on the web search results, here's what I found regarding LLM evaluation and benchmarking topics that are relevant to AI research:

## Key Topics in LLM Evaluation and Benchmarking

**Benchmark Contamination and Data Issues:**
Existing benchmarks and evaluation methodologies are susceptible to the Benchmark Contamination Problem due to their use of static datasets, which remains a major challenge in the field.

**LLM-as-a-Judge Paradigm:**
Powerful LLMs are used to evaluate responses generated by humans or other models, offering a scalable alternative to the costly process of collecting human-written references or annotations.

**Benchmark Quality Assessment:**
Recent work introduces frameworks for auditing evaluation sets along three orthogonal axes: Capability Discrimination (measuring how sharply a benchmark separates model performance), Anti-Saturation (estimating remaining headroom before ceiling effects), and Impact (quantifying influence across academic and industrial ecosystems).

**Domain-Specific Evaluation:**
Multiple-choice question benchmarks like MMLU suffer from documented biases, including sensitivity to answer choice ordering, and can often be answered without seeing the question.

**Contamination-Limited Approaches:**
Recent frameworks for benchmarking LLMs are designed to minimize both test set contamination and pitfalls of LLM judging, with frequently-updated questions based on recent information sources and automatic scoring according to objective ground truth.

These represent current challenges and solutions in LLM evaluation that would likely be relevant topics for AI conferences such as AAAI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12782f02-cc23-478b-b0db-1b26cf5502b5",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "5a6b75e2-e018-4660-93f1-7d82370b2289",
  "sourceToolAssistantUUID": "12782f02-cc23-478b-b0db-1b26cf5502b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T11:35:03.272Z_

<details><summary>↩ Tool result · `toolu_01HoerLESJwxc2s83a2EzuFW`</summary>

```text
Web search results for query: "NeurIPS 2026 datasets benchmarks track topics"

Links: [{"title":"Introducing the Evaluations & Datasets Track at NeurIPS 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/"},{"title":"NeurIPS Conference on X: \"The Datasets &amp; Benchmarks track is now \"Evaluation and Datasets\", with an expanded scope for NeurIPS 2026! Read the call for papers https://t.co/ssclVjxu4E, and learn more about the changes in our blog post: https://t.co/ZI6v4IeoJv\" / X","url":"https://x.com/NeurIPSConf/status/2036184924001022405"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS Datasets & Benchmarks Track: From Art to Science in AI Evaluations – NeurIPS Blog","url":"https://blog.neurips.cc/2025/12/05/neurips-datasets-benchmarks-track-from-art-to-science-in-ai-evaluations/"},{"title":"NeurIPS 2026 Evaluations & Datasets FAQ","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ"},{"title":"NeurIPS 2026 Evaluations and Datasets Track | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FEvaluations_and_Datasets_Track"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://www.linkedin.com/posts/drouinalexandre_neurips-2026-evaluations-datasets-track-activity-7442218476561141760-yqC3"}]

Based on the search results, here's what I found about the NeurIPS 2026 Datasets and Benchmarks track:

## Track Name and Scope Change

The Datasets & Benchmarks track is now "Evaluation and Datasets", with an expanded scope for NeurIPS 2026! The track continues to align with the main conference in terms of requirements and timeline, and this year introduces an important refinement with an expanded scope that explicitly positions evaluation as a scientific object of study.

## Topics and Focus Areas

The ED Track welcomes contributions that advance the science of AI evaluation, including work that analyzes strengths, limitations, or failure modes of existing benchmarks or evaluation practices, studies benchmark saturation or overfitting and their impact on scientific conclusions, and compares evaluation designs and demonstrates how different assumptions lead to different results or conclusions.

The track welcomes submissions that introduce datasets and clearly explain their scope, assumptions, limitations, and how they are intended to support or shape evaluative claims across the AI/ML lifecycle, as well as submissions that contribute tools, analyses, or frameworks that improve how evaluative claims are constructed or interpreted.

## Additional Submission Categories

The track includes in-depth analyses of machine learning challenges and competitions (by organizers and/or participants) that yield important new insights and competition papers from prior NeurIPS competitions.

In 2025, the track saw alignment with main track trends, particularly increased focus on large language model evaluation, alongside continued activity in AI for science, domain-specific applications and socially beneficial AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "209b3e7f-719b-4bff-8ec1-8b035542c0ca",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "5344f7ce-3cc1-4bcd-93dd-b0094421947a",
  "sourceToolAssistantUUID": "209b3e7f-719b-4bff-8ec1-8b035542c0ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-28T11:35:06.955Z_

Let me get the ARR rolling review dates to understand the submission cycles for ACL/NAACL 2027.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5344f7ce-3cc1-4bcd-93dd-b0094421947a",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtxtZ9FX3HNCcfRm2bS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd85f70d-c474-42c5-8c76-ebcaf637c7d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhTuiz17TCD9i24H5QDyN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1264,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 20043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1800,
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

_source line 47 · 2026-05-28T11:35:07.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ZBovYiWi2NoQnF9tbDvD6`</summary>

```json
{
  "query": "ACL Rolling Review 2026 2027 submission cycles dates schedule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd85f70d-c474-42c5-8c76-ebcaf637c7d0",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtxtZ9FX3HNCcfRm2bS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2838c7d-285e-4183-9207-5b3ee7201e54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhTuiz17TCD9i24H5QDyN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1264,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 20043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1800,
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

_source line 48 · 2026-05-28T11:35:07.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01416oL2i4n56xQWQkogXt5K`</summary>

```json
{
  "query": "AAAI 2027 call for papers topics areas"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2838c7d-285e-4183-9207-5b3ee7201e54",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtxtZ9FX3HNCcfRm2bS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92e02a20-97cc-4604-b7d2-e8a9cc331d9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhTuiz17TCD9i24H5QDyN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1264,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 20043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1800,
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

_source line 49 · 2026-05-28T11:35:12.872Z_

<details><summary>↩ Tool result · `toolu_01416oL2i4n56xQWQkogXt5K`</summary>

```text
Web search results for query: "AAAI 2027 call for papers topics areas"

Links: [{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"Embodied AI Agents: Modeling the World","url":"https://arxiv.org/pdf/2506.22355"},{"title":"Direct Human-AI Comparison in the Animal-AI Environment","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9172850/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"Evaluating Large Reasoning Model Performance on Complex Medical Scenarios In The MMLU-Pro Benchmark","url":"https://www.medrxiv.org/content/10.1101/2025.04.07.25325385.full.pdf"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"CardiacGPT™: A Real-Time AI Assistant for Intraoperative Guidance and Postoperative Decision Support in Cardiac Surgery","url":"https://www.medrxiv.org/content/10.1101/2025.08.30.25334720.full.pdf"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"}]

Based on the search results, the official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/. However, the specific topic areas for the AAAI 2027 call for papers are not detailed in the current search results.

The search results indicate that the Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027, and that the purpose of the AAAI conference series is to promote research in Artificial Intelligence (AI) and foster scientific exchange between researchers, practitioners, scientists, students, and engineers across the entirety of AI and its affiliated disciplines.

For the complete list of topic areas and submission guidelines, I recommend visiting the official AAAI 2027 conference website directly at https://aaai.org/conference/aaai/aaai-27/, as the detailed call for papers information appears to still be under development (with submission deadlines marked as "TBD").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92e02a20-97cc-4604-b7d2-e8a9cc331d9f",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "de740d68-a5dc-4c82-9bfa-a1c3e0d8a432",
  "sourceToolAssistantUUID": "92e02a20-97cc-4604-b7d2-e8a9cc331d9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T11:35:14.211Z_

<details><summary>↩ Tool result · `toolu_012ZBovYiWi2NoQnF9tbDvD6`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 2027 submission cycles dates schedule"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Allow Early Submissions to ACL 2026 in the October ARR Cycle | ACL Member Portal","url":"https://www.aclweb.org/portal/content/allow-early-submissions-acl-2026-october-arr-cycle"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org//calls/papers/"}]

Based on the search results, here's information about ACL Rolling Review 2026-2027 submission cycles and dates:

## Review Cycle Schedule Changes

The ACL Peer Review Committee recommended switching from 8-week to 10-week review cycles, with the new schedule starting in May 2025. This means instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.

## Key Dates for 2026-2027 Venues

For EMNLP 2026 and AACL 2026, the final ARR submission date is May 25, 2026, with a commitment date of August 2, 2026. For EACL 2027, the final ARR submission date is August 3, 2026, with a commitment date of October 11, 2026.

## ACL 2026 Specific Timeline

For the January ARR cycle, ARR reviews and meta-reviews will be available to authors on March 10, 2026.

## General ARR Process

The cycles will allow the cycles to always start on Mondays, and develop a consistent schedule that clashes with weekends less.

For the most up-to-date and complete submission schedule, you can visit the official ACL Rolling Review dates page at aclrollingreview.org/dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2838c7d-285e-4183-9207-5b3ee7201e54",
  "isSidechain": true,
  "promptId": "298c40b0-b1f7-4a5c-afc3-3dc8b1de86bd",
  "agentId": "ac0166e9888b16594",
  "type": "user",
  "uuid": "465aa6d4-ee5b-48cd-be38-c58cd6647f46",
  "sourceToolAssistantUUID": "b2838c7d-285e-4183-9207-5b3ee7201e54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-28T11:35:53.869Z_

Here is my compiled report of AI/ML conference deadlines that are **after 2026-05-28** (today).

---

## Venues with Upcoming Deadlines (After 2026-05-28)

### 1. AAAI 2027
- **Abstract deadline:** July 21, 2026 (11:59 PM UTC-12) -- AFTER today
- **Full paper deadline:** July 28, 2026 (11:59 PM UTC-12) -- AFTER today
- **Supplementary material deadline:** July 31, 2026
- **Conference dates:** February 16-23, 2027, Montreal, Canada
- **LLM evaluation/benchmarking:** Yes. AAAI covers all areas of AI including machine learning evaluation, NLP benchmarking, and LLM assessment. Papers on LLM evaluation and benchmarking are regularly accepted.

### 2. EACL 2027 (via ACL Rolling Review)
- **ARR submission deadline:** August 3, 2026 (11:59 PM UTC-12) -- AFTER today
- **Commitment deadline:** October 11, 2026
- **Conference dates:** March 9-14, 2027, Athens, Greece
- **LLM evaluation/benchmarking:** Yes. EACL is an ACL-affiliated venue and regularly publishes work on NLP evaluation, LLM benchmarking, and related topics.

### 3. EMNLP 2026 (via ACL Rolling Review)
- **ARR submission deadline:** May 25, 2026 -- BEFORE today (passed by 3 days)
- **Commitment deadline:** August 2, 2026 -- AFTER today
- **Conference dates:** October 24-29, 2026, Budapest, Hungary
- **LLM evaluation/benchmarking:** Yes. EMNLP is one of the premier venues for empirical NLP work including LLM evaluation and benchmarking.
- **Note:** While the paper submission deadline has just passed, you can still commit a paper from a prior ARR cycle (the commitment deadline of August 2, 2026 is still open). If you already have a reviewed ARR submission, this is still viable.

---

## Venues with Deadlines Not Yet Announced (Likely After Today)

### 4. ICLR 2027
- **Deadlines:** Not yet announced
- **Predicted conference dates:** ~April 24-28, 2027 (based on historical patterns)
- **Expected submission deadline:** ~October 2026 (based on ICLR 2026's pattern of October 2025 deadline)
- **LLM evaluation/benchmarking:** Yes. ICLR is a top venue for representation learning and regularly accepts work on model evaluation and benchmarks.

### 5. ACL 2027
- **Deadlines:** Not yet announced
- **Predicted conference dates:** July 2027, location TBA
- **Expected ARR submission deadline:** ~January-February 2027 (based on historical pattern)
- **LLM evaluation/benchmarking:** Yes. ACL is the flagship NLP conference and a premier venue for LLM evaluation work.

### 6. NAACL 2027
- **Deadlines:** Not yet announced
- **Predicted conference dates:** May 2-5, 2027, location TBA
- **Expected ARR submission deadline:** ~December 2026-January 2027 (based on historical pattern)
- **LLM evaluation/benchmarking:** Yes. NAACL regularly publishes NLP evaluation and benchmarking work.

### 7. AISTATS 2027
- **Deadlines:** Not yet announced
- **Predicted conference dates:** February 16-23, 2027, Montreal, Canada (note: same dates/location as AAAI 2027 -- this may need verification)
- **Expected submission deadline:** ~September-October 2026 (based on AISTATS 2026 having a September 25/October 2 deadline)
- **LLM evaluation/benchmarking:** Partially. AISTATS focuses on the intersection of AI, ML, and statistics. Methodological evaluation work is accepted, but it is less focused on LLM-specific benchmarking compared to NLP venues.

---

## Venues Whose Deadlines Have Already Passed (EXCLUDE)

### 8. NeurIPS 2026
- **Abstract deadline:** May 4, 2026 -- BEFORE today (passed)
- **Full paper deadline:** May 6, 2026 -- BEFORE today (passed)
- **Conference dates:** Late 2026 (typically December)
- **Status:** EXCLUDED -- deadline passed ~3 weeks ago
- **Note:** NeurIPS 2026 introduced a renamed "Evaluations & Datasets Track" (formerly "Datasets & Benchmarks") with expanded scope explicitly covering LLM evaluation -- but the deadline has passed.

### 9. ICML 2026
- **Abstract deadline:** January 24, 2026 -- BEFORE today (passed)
- **Full paper deadline:** January 28, 2026 -- BEFORE today (passed)
- **Conference dates:** July 6-11, 2026, Seoul (Coex Convention Center)
- **Status:** EXCLUDED -- deadline passed ~4 months ago

### 10. COLM 2026
- **Abstract deadline:** March 26, 2026 -- BEFORE today (passed)
- **Full paper deadline:** March 31, 2026 -- BEFORE today (passed)
- **Conference dates:** October 6-9, 2026, San Francisco (Hilton Union Square)
- **Status:** EXCLUDED -- deadline passed ~2 months ago

---

## Summary: Actionable Deadlines Still Open

| Venue | Next Deadline | Date | Type |
|-------|--------------|------|------|
| **AAAI 2027** | Abstract | Jul 21, 2026 | Direct submission |
| **AAAI 2027** | Full paper | Jul 28, 2026 | Direct submission |
| **EACL 2027** | ARR submission | Aug 3, 2026 | Via ACL Rolling Review |
| **EMNLP 2026** | Commitment only | Aug 2, 2026 | Commit existing ARR review |
| **ICLR 2027** | TBA | ~Oct 2026 | Direct submission (expected) |
| **AISTATS 2027** | TBA | ~Sep-Oct 2026 | Direct submission (expected) |
| **NAACL 2027** | TBA | ~Dec 2026-Jan 2027 | Via ACL Rolling Review (expected) |
| **ACL 2027** | TBA | ~Jan-Feb 2027 | Via ACL Rolling Review (expected) |

The most immediate actionable deadlines are **AAAI 2027** (July 21/28) and **EACL 2027** (August 3 via ARR). All of these venues accept work on LLM evaluation and benchmarking.

---

Sources:
- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI-27 Conference Page](https://aaai.org/conference/aaai/aaai-27/)
- [NeurIPS 2026 Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers)
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [NeurIPS 2026 Evaluations & Datasets Track](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)
- [NeurIPS 2026 Evaluations & Datasets Blog Post](https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [ACL Rolling Review Dates and Venues](http://aclrollingreview.org/dates)
- [EACL 2027](https://2027.eacl.org/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Conference Page](https://2026.emnlp.org/)
- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)
- [ICML 2026 Call for Papers](https://icml.cc/Conferences/2026/CallForPapers)
- [NAACL Website](https://naacl.org/)
- [COLM 2026 Key Dates](https://colmweb.org/dates.html)
- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)
- [AISTATS 2026](https://virtual.aistats.org/)
- [AI Conference Deadlines (mlciv)](https://mlciv.com/ai-deadlines/)
- [AI & ML Conference Deadlines 2026-2027 (Bibby)](https://trybibby.com/conference-deadlines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "465aa6d4-ee5b-48cd-be38-c58cd6647f46",
  "isSidechain": true,
  "agentId": "ac0166e9888b16594",
  "requestId": "req_011CbUtyh5cSU4K7zGgRJb3N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cd177e1-cb5e-406e-a128-5ffe478fa05a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c634caab-4e73-4d2e-8d06-c7c8f95042a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014C4myE61X6cSxbwrFq7dec",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 774,
      "cache_creation_input_tokens": 2221,
      "cache_read_input_tokens": 21843,
      "output_tokens": 2298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 774,
          "output_tokens": 2298,
          "cache_read_input_tokens": 21843,
          "cache_creation_input_tokens": 2221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2221,
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
