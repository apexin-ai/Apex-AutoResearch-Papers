# Research conversation: Search for very recent (March-May 2026) papers on domain-adaptive or domain-conditioned autoformalization. I need to che

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a39ac29d9f4d62432.jsonl`
- **Structured JSON:** [`e11446d0d7de7f2f10cb.json`](../../sessions/e1/e11446d0d7de7f2f10cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-28T13:53:09.555Z_

Search for very recent (March-May 2026) papers on domain-adaptive or domain-conditioned autoformalization. I need to check if anyone has published work that directly competes with the idea of conditioning autoformalization on mathematical subdomain.

Search queries to try:
1. "domain adaptive autoformalization" site:arxiv.org 2026
2. "domain conditioned" autoformalization lean 2026
3. "subdomain" autoformalization mathematical 2026
4. autoformalization "domain specific" lean4 2026
5. "domain aware" formalization theorem proving 2026
6. autoformalization "error taxonomy" mathematical 2026

Also search for any new work from the teams behind CRAMF, DRIFT, Aria, StepFun-Formalizer, or ProofBridge that might have extended their systems with domain conditioning.

Use WebSearch for all queries. Report any relevant papers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "5cea949b-89a4-4c3e-ba11-364139fa929c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T13:53:09.558Z_

```json
{
  "parentUuid": "5cea949b-89a4-4c3e-ba11-364139fa929c",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
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
  "uuid": "cd067987-63dc-4e9b-807a-97d44b2d75bb",
  "timestamp": "2026-05-28T13:53:09.558Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T13:53:09.559Z_

```json
{
  "parentUuid": "cd067987-63dc-4e9b-807a-97d44b2d75bb",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eeb98650-d048-45f6-9dab-be3806258eb6",
  "timestamp": "2026-05-28T13:53:09.559Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T13:53:12.255Z_



I'll search for recent papers on domain-adaptive autoformalization using WebSearch. Let me first load the tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeb98650-d048-45f6-9dab-be3806258eb6",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VhuDhMbWz2C1k7y31",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f8999d5-f799-47b1-ae59-e2b9708d265d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Risc7tKpwXMqdgRR9AhNsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1552,
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

_source line 5 · 2026-05-28T13:53:12.647Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014CEqTDbHygAnbRR2FLtWyh`</summary>

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
  "parentUuid": "0f8999d5-f799-47b1-ae59-e2b9708d265d",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VhuDhMbWz2C1k7y31",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9413627-5472-4e8a-a178-8badbaa6fe79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Risc7tKpwXMqdgRR9AhNsj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 7407,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1552,
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

_source line 6 · 2026-05-28T13:53:12.654Z_

<details><summary>↩ Tool result · `toolu_014CEqTDbHygAnbRR2FLtWyh`</summary>

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
  "parentUuid": "f9413627-5472-4e8a-a178-8badbaa6fe79",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "9a0d617a-804d-4cab-92b3-3a2f2094f6bb",
  "sourceToolAssistantUUID": "f9413627-5472-4e8a-a178-8badbaa6fe79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T13:53:14.525Z_



Now let me run all the search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a0d617a-804d-4cab-92b3-3a2f2094f6bb",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "491bf87c-364b-4169-9279-770b9caa4a84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 8 · 2026-05-28T13:53:15.073Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015LwVpTQYuk52qA8gDWfzw4`</summary>

```json
{
  "query": "\"domain adaptive autoformalization\" site:arxiv.org 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "491bf87c-364b-4169-9279-770b9caa4a84",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70a1d57d-aa72-45e9-ae66-80f39e5b5b54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 9 · 2026-05-28T13:53:15.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ymrdxxxRVCzAMyx6B2sWN`</summary>

```json
{
  "query": "\"domain conditioned\" autoformalization lean 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70a1d57d-aa72-45e9-ae66-80f39e5b5b54",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2decc1d-6a92-49c7-9995-b797bca58d82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 10 · 2026-05-28T13:53:16.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GxjVXe156Z6HhbakUu282`</summary>

```json
{
  "query": "\"subdomain\" autoformalization mathematical 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2decc1d-6a92-49c7-9995-b797bca58d82",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8ecec8a-4e2a-46c3-8d3c-c9b3d9910e4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 11 · 2026-05-28T13:53:16.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012xtscZ6c8AVrb4b1rcEQJT`</summary>

```json
{
  "query": "autoformalization \"domain specific\" lean4 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ecec8a-4e2a-46c3-8d3c-c9b3d9910e4c",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5811ad8-c7ee-4cb2-a088-56c35f64be80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 12 · 2026-05-28T13:53:16.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ekm119MKGvvLJwTTKsRxLi`</summary>

```json
{
  "query": "\"domain aware\" formalization theorem proving 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5811ad8-c7ee-4cb2-a088-56c35f64be80",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebf076e2-138f-4825-9588-7167a688bb7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 13 · 2026-05-28T13:53:16.708Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014PhWXNfrNy2wYM2Vxn8Qof`</summary>

```json
{
  "query": "autoformalization \"error taxonomy\" mathematical 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf076e2-138f-4825-9588-7167a688bb7f",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5VwG9NvUKmmEdeKFNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "098edac4-7560-4fe9-b6ff-f64c972ea525",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jy57xcpNDMiNVfBKfVy9tE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 8959,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 632
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 8959,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 632,
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

_source line 14 · 2026-05-28T13:53:22.048Z_

<details><summary>↩ Tool result · `toolu_015ymrdxxxRVCzAMyx6B2sWN`</summary>

```text
Web search results for query: ""domain conditioned" autoformalization lean 2026"

Links: [{"title":"Autoformalization and the Future of Math Research","url":"https://www.neelsomaniblog.com/p/autoformalization-and-the-future"},{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/pdf/2602.17016"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"}]

I found several relevant results about autoformalization in Lean from 2026. However, I didn't find specific results about "domain conditioned" autoformalization. Here's what the search revealed:

## Recent Autoformalization Research in 2026

Autoformalization refers to tooling that takes human-readable math proofs and converts them into machine-checkable formats like Lean or Coq.

Several notable projects from early 2026 include:

1. **Cycle Consistency Fine-tuning**: A March 2026 paper on improving Lean4 autoformalization via cycle consistency fine-tuning explores automatically translating natural language mathematical texts into formal proof language such as Lean4.

2. **ProofBridge Framework**: A recent approach uses a joint embedding model that aligns natural language and formal language theorem+proof pairs in a shared semantic space to enable cross-modal retrieval of semantically relevant formal examples to guide translation.

3. **M2F Project**: M2F exposes document-scale autoformalization as a verifier-certified refinement loop over a pinned Lean environment.

The search results don't specifically mention "domain conditioned" autoformalization techniques. If you're looking for information about domain conditioning in the context of autoformalization, you may want to search with different terminology or check recent preprints more directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2decc1d-6a92-49c7-9995-b797bca58d82",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "734c235e-d895-441f-a470-01af945da95d",
  "sourceToolAssistantUUID": "d2decc1d-6a92-49c7-9995-b797bca58d82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T13:53:22.549Z_

<details><summary>↩ Tool result · `toolu_014PhWXNfrNy2wYM2Vxn8Qof`</summary>

```text
Web search results for query: "autoformalization "error taxonomy" mathematical 2026"

Links: [{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"Formal Error Taxonomy","url":"https://www.emergentmind.com/topics/formal-error-taxonomy"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"},{"title":"Error Taxonomy Generation with SKILL.md - Data Science x AI","url":"https://datasciencexai.substack.com/p/error-taxonomy-generation-with-skillmd"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"}]

Based on the search results, I found relevant information about autoformalization and error taxonomy in 2026:

## Key Findings

The 3rd AI for Math Workshop at ICML 2026 features an autoformalization challenge that evaluates whether autoformalization preserves mathematical intent, using the FormalRx-Test dataset built on the SCI Error Taxonomy (28 error categories).

Autoformalization is defined as the translation of natural language mathematical problems into formal, machine-verifiable statements such as those in Lean. While Large Language Models have shown proficiency in generating syntactically well-formed statements, they often struggle to faithfully capture the semantic intent of the original problem, with recent studies highlighting the pervasive issue of poor semantic fidelity in current autoformalization systems.

Additionally, a comprehensive survey on autoformalization in the era of Large Language Models provides an overview of recent advances and examines how autoformalization is applied across various mathematical domains, analyzing the end-to-end workflow from data preprocessing to model design and evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "098edac4-7560-4fe9-b6ff-f64c972ea525",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "f7f2c9b5-8fde-4e4d-aafe-569eee4ce51d",
  "sourceToolAssistantUUID": "098edac4-7560-4fe9-b6ff-f64c972ea525",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T13:53:22.658Z_

<details><summary>↩ Tool result · `toolu_015LwVpTQYuk52qA8gDWfzw4`</summary>

```text
Web search results for query: ""domain adaptive autoformalization" site:arxiv.org 2026"

Links: [{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/html/2310.07957v3"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/html/2509.09810v3"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency","url":"https://arxiv.org/pdf/2410.20936"}]

Based on the search results, I found several papers on autoformalization from arXiv, though none specifically matched the exact phrase "domain adaptive autoformalization" from 2026. Here are the most relevant findings:

The search returned recent papers on autoformalization:

1. A comprehensive survey on autoformalization highlights the diversity and challenges across mathematical domains, with each domain having unique characteristics such as graphical reasoning in geometry and symbolic manipulation in algebra, requiring autoformalization to adapt to different semantic structures and reasoning paradigms.

2. Recent work emphasizes the need for autoformalization systems that can generalize compositionally, adapt to new domains with minimal supervision, and tightly integrate with formal verification frameworks.

3. Recent approaches include integrating syntactic and consistency information as tools into the formalization process to guide models in adaptively refining statements during generation.

The most recent paper in the results is a framework paper on autoformalization from December 2025, discussing how the term originated in 2018 within mathematical formalization contexts, with recent work exploring the use of LLMs to assist with mathematical formalization.

If you're looking for a specific paper titled "domain adaptive autoformalization," it may not yet be indexed or may use different terminology. Would you like me to search with different keywords?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70a1d57d-aa72-45e9-ae66-80f39e5b5b54",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "264720f6-7c30-420e-868e-8389953d87cd",
  "sourceToolAssistantUUID": "70a1d57d-aa72-45e9-ae66-80f39e5b5b54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T13:53:22.851Z_

<details><summary>↩ Tool result · `toolu_01Ekm119MKGvvLJwTTKsRxLi`</summary>

```text
Web search results for query: ""domain aware" formalization theorem proving 2026"

Links: [{"title":"AI-Driven Formal Theorem Proving in the Lean Ecosystem","url":"https://leandojo.org/"},{"title":"Automated Theorem Proving","url":"https://www.emergentmind.com/topics/automated-theorem-proving"},{"title":"Automated Theorem Proving Systems","url":"https://www.emergentmind.com/topics/automated-theorem-proving-atp-systems"},{"title":"Interactive Theorem Proving","url":"https://itp-conference.github.io/"},{"title":"LLM-Based Theorem Provers","url":"https://www.emergentmind.com/topics/llm-based-theorem-provers"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"PhysProver: Advancing Automatic Theorem Proving for Physics","url":"https://arxiv.org/pdf/2601.15737"}]

Based on the search results, here are the relevant findings about "domain aware" formalization and theorem proving in 2026:

## Recent Developments

A 2026 paper titled "BRIDGE: Building Representations In Domain Guided Program Synthesis" by researchers including Robert Joseph George and Anima Anandkumar explores domain-guided approaches to program synthesis.

## Domain-Specific Approaches

Recent advances show that adapting automated theorem proving (ATP) techniques to new mathematical domains such as geometry, combinatorics, and analysis requires domain-specific encoding and sometimes major advances in symbolic reasoning and search.

A particularly notable example is PhysProver, which represents the first approach to enhance formal theorem proving in the physics domain, using DeepSeek-Prover-V2-7B and Reinforcement Learning with Verifiable Rewards, achieving a 2.4% improvement across multiple sub-domains with just ~5K training samples.

## Future Research Directions

Future research in LLM-based theorem proving points toward domain-adaptive training, the synthesis of abstract proof strategies, dynamic axiom discovery, and human-in-the-loop verification architectures.

The search results indicate that domain-aware and domain-specific approaches are becoming increasingly important in modern formal theorem proving, particularly as the field expands beyond pure mathematics into specialized domains like physics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebf076e2-138f-4825-9588-7167a688bb7f",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "d9acd2c3-65dd-4016-978d-61f4db21070a",
  "sourceToolAssistantUUID": "ebf076e2-138f-4825-9588-7167a688bb7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T13:53:24.352Z_

<details><summary>↩ Tool result · `toolu_019GxjVXe156Z6HhbakUu282`</summary>

```text
Web search results for query: ""subdomain" autoformalization mathematical 2026"

Links: [{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/pdf/2602.17016"},{"title":"[2602.17016v1] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/abs/2602.17016v1"},{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"Autoformalization and the Future of Mathematical Discovery: Reflections from Neel Somani","url":"https://www.lelezard.com/en/news-22140925.html"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"[2510.24592] ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/abs/2510.24592"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"}]

Based on the search results, here's what I found about autoformalization in mathematics in 2026:

## Recent Advances in Mathematical Autoformalization

M2F (Math-to-Formal) is presented as the first agentic framework for end-to-end, project-scale autoformalization in Lean, representing a significant advancement in the field. The framework operates by splitting documents into atomic blocks, ordering them via inferred dependencies, and repairing declaration skeletons until the project compiles, with a proof repair stage that closes holes using goal-conditioned local edits.

MathAtlas has been released to the community as a benchmark set for large-scale autoformalization of graduate-level mathematics in the wild. However, strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions, with performance degrading substantially as dependency depth increases.

## Notable Projects

One project has autoformalized a large portion of general topology from the Munkres textbook, producing 160k lines of formalized topology as of January 4, 2026, with about 130k lines completed in two weeks for approximately $100 in LLM subscription costs.

## General Progress

Recent work includes developing AI-based provably-correct mathematical proof tutors by combining LLMs and theorem provers, with systems composed of autoformalizers, next-step generators, and natural language feedback generators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8ecec8a-4e2a-46c3-8d3c-c9b3d9910e4c",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "15f9aedd-ef4f-4f33-8aef-ee0ee2e0c994",
  "sourceToolAssistantUUID": "d8ecec8a-4e2a-46c3-8d3c-c9b3d9910e4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T13:53:26.811Z_

<details><summary>↩ Tool result · `toolu_012xtscZ6c8AVrb4b1rcEQJT`</summary>

```text
Web search results for query: "autoformalization "domain specific" lean4 2026"

Links: [{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"[2406.01940] Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/abs/2406.01940"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4/fulltext/666038b385a4ee7261a6723b/Process-Driven-Autoformalization-in-Lean-4.pdf?origin=scientificContributions"}]

Based on the search results, here's what I found about autoformalization, domain-specific approaches, and Lean4 in 2026:

## Recent Developments in Lean4 Autoformalization (2026)

Autoformalization - automatically translating natural language mathematical texts into formal proof language such as Lean4 - can help accelerate AI-assisted mathematical research.

### Recent Research (2026)

A recent study fine-tuned Qwen3.5-2B with LoRA for natural language to Lean4 formalization on FineLeanCorpus, considering three training regimes: supervised fine-tuning with curriculum learning, SFT without curriculum ordering, and reinforcement learning using group relative policy optimization with a cycle consistency reward. Cycle consistency measures how well the meaning of a statement is preserved through a NL to Lean4 to NL' loop, computed as cosine similarity of off-the-shelf sentence embeddings.

### Domain-Specific Aspects

The research leverages domain information in training data. The FineLeanCorpus dataset contains 509k NL/Lean4 pairs annotated with difficulty scores (1 to 10) and mathematical domain labels. Additionally, evaluation includes a basic test set and a real test set whose domains differ from the training set to provide domain-general comprehensive evaluation.

### Process-Driven Approaches

A Process-Driven Autoformalization framework leverages precise feedback from Lean 4 compilers to enhance autoformalization, with experiments demonstrating improved autoformalization and higher compiler accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5811ad8-c7ee-4cb2-a088-56c35f64be80",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "b361c7d7-5814-4979-a730-c8d82912f8cd",
  "sourceToolAssistantUUID": "f5811ad8-c7ee-4cb2-a088-56c35f64be80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-28T13:53:31.842Z_

Good, I have initial results. Now let me search for the specific teams/systems mentioned, and dig deeper into the most promising leads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b361c7d7-5814-4979-a730-c8d82912f8cd",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5WyXqwuhPTMP7BzVGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a2961e8-1435-4115-968c-dc9f35c76c35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176FL3o4b1vxzpwWwPzUWYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1115,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 9591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3337,
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

_source line 21 · 2026-05-28T13:53:32.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7YfbdxiFqnLhoKaBUAELw`</summary>

```json
{
  "query": "CRAMF autoformalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a2961e8-1435-4115-968c-dc9f35c76c35",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5WyXqwuhPTMP7BzVGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03ef9664-1a07-4902-b7c2-ef92eb401112",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176FL3o4b1vxzpwWwPzUWYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1115,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 9591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3337,
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

_source line 22 · 2026-05-28T13:53:32.796Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KjDoLqbewXNwYrHE3Zm3HC`</summary>

```json
{
  "query": "DRIFT autoformalization 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03ef9664-1a07-4902-b7c2-ef92eb401112",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5WyXqwuhPTMP7BzVGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2b37c7e-75a2-4652-8275-1b86729a1b87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176FL3o4b1vxzpwWwPzUWYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1115,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 9591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3337,
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

_source line 23 · 2026-05-28T13:53:33.262Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013yM4Akzvab4buJBa4mVj8f`</summary>

```json
{
  "query": "Aria autoformalization mathematical 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2b37c7e-75a2-4652-8275-1b86729a1b87",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5WyXqwuhPTMP7BzVGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f1dd3f3-c095-4328-bbcc-2ac32ffe2335",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176FL3o4b1vxzpwWwPzUWYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1115,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 9591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3337,
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

_source line 24 · 2026-05-28T13:53:33.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JrMX1W81cVtUU2HDH84t7u`</summary>

```json
{
  "query": "StepFun-Formalizer autoformalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f1dd3f3-c095-4328-bbcc-2ac32ffe2335",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5WyXqwuhPTMP7BzVGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd988f5e-26dd-43f3-84cd-a7fad6bcfc22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176FL3o4b1vxzpwWwPzUWYC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1115,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 9591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3337,
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

_source line 25 · 2026-05-28T13:53:34.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011vnD9haPcdUqKrLc5rxbSV`</summary>

```json
{
  "query": "ProofBridge autoformalization domain 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd988f5e-26dd-43f3-84cd-a7fad6bcfc22",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5WyXqwuhPTMP7BzVGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff0ab2c5-79e3-4ae5-ad8e-e8fc20e6e74d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176FL3o4b1vxzpwWwPzUWYC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1115,
      "cache_creation_input_tokens": 3337,
      "cache_read_input_tokens": 9591,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3337
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1115,
          "output_tokens": 271,
          "cache_read_input_tokens": 9591,
          "cache_creation_input_tokens": 3337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3337,
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

_source line 26 · 2026-05-28T13:53:38.663Z_

<details><summary>↩ Tool result · `toolu_013yM4Akzvab4buJBa4mVj8f`</summary>

```text
Web search results for query: "Aria autoformalization mathematical 2026"

Links: [{"title":"ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://iclr.cc/virtual/2026/poster/10010860"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE ...","url":"https://openreview.net/pdf/388a385b7ad068290351f90757bd3af8bb6e5515.pdf"},{"title":"Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview","url":"https://openreview.net/forum?id=CPxZClPMiy"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520v1"},{"title":"[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520"}]

Based on the search results, here's what I found about Aria autoformalization:

Aria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

Accurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.

To ensure semantic correctness, Aria introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.

The system showed strong performance on benchmarks: On ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods. On FATE-X, a suite of challenging algebra problems from research literature, it outperforms the best baseline with 44.0% vs. 24.0% final accuracy, and on a dataset of homological conjectures, Aria reaches 42.9% final accuracy while all other models score 0%.

The work was presented as an ICLR 2026 poster in April 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f1dd3f3-c095-4328-bbcc-2ac32ffe2335",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "a8b4ebfe-a77a-4511-8a8d-86b7ede5c290",
  "sourceToolAssistantUUID": "2f1dd3f3-c095-4328-bbcc-2ac32ffe2335",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T13:53:38.758Z_

<details><summary>↩ Tool result · `toolu_01KjDoLqbewXNwYrHE3Zm3HC`</summary>

```text
Web search results for query: "DRIFT autoformalization 2026 arxiv"

Links: [{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/html/2510.10815v2"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/pdf/2510.10815"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Autonomous Drift Learning in Data Streams: A Unified Perspective","url":"https://arxiv.org/html/2605.01295v1"},{"title":"Drift Localization using Conformal Predictions","url":"https://arxiv.org/pdf/2602.19790"},{"title":"[2601.03298] 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/abs/2601.03298"},{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"}]

Based on the search results, I found information about DRIFT autoformalization:

DRIFT (Decompose, Retrieve, Illustrate, then Formalize Theorems) is a novel four-stage method designed to address the two main limitations of previous retrieval-augmented formalization methods: handling the complexity of informal statements and the lack of demonstrative examples.

The method addresses the challenge that automating the formalization of mathematical statements for theorem proving remains a major challenge for Large Language Models (LLMs). LLMs struggle to identify and utilize prerequisite mathematical knowledge and its formal representation in languages like Lean, and current retrieval-augmented methods query external libraries using the informal statement directly but overlook a fundamental limitation: informal mathematical statements are often complex and offer limited context on underlying math concepts.

Given an informal statement, DRIFT operates in four stages, starting with a Decompose stage where an LLM breaks down the statement into atomic, concept-focused sub-queries.

The DRIFT paper was published on arXiv in October 2025 (arxiv:2510.10815).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2b37c7e-75a2-4652-8275-1b86729a1b87",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "3c511c6c-35b0-4a0e-a71a-36e8c6af84ae",
  "sourceToolAssistantUUID": "f2b37c7e-75a2-4652-8275-1b86729a1b87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T13:53:39.654Z_

<details><summary>↩ Tool result · `toolu_01K7YfbdxiFqnLhoKaBUAELw`</summary>

```text
Web search results for query: "CRAMF autoformalization 2026"

Links: [{"title":"[2508.06931] Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/abs/2508.06931"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=09lmwhDqZ3"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"Autoformalization with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/401455895_Autoformalization_with_Large_Language_Models"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | Request PDF","url":"https://www.researchgate.net/publication/394440359_Automated_Formalization_via_Conceptual_Retrieval-Augmented_LLMs"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Patrick Shafto: Autoformalization and the future of math and science - YouTube","url":"https://www.youtube.com/watch?v=ZMO3xy1bayE"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/pdf/2508.06931"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Autoformalization and the Future of Math Research","url":"https://www.neelsomaniblog.com/p/autoformalization-and-the-future"}]

Based on the search results, here's what I found about CRAMF and autoformalization in 2026:

## CRAMF Framework

CRAMF is a Concept-driven Retrieval-Augmented Mathematical Formalization framework designed to improve automated theorem proving. CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation.

## The Problem It Addresses

Automated formalization faces two major challenges: model hallucination (e.g., undefined predicates, symbol misuse, and version incompatibility) and the semantic gap caused by ambiguous or missing premises in natural language descriptions.

## Technical Implementation

The framework automatically constructs a concept-definition knowledge base from Mathlib4, the standard mathematical library for the Lean 4 theorem prover, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts. The design includes a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval.

## Results

Experiments on miniF2F, ProofNet, and a newly proposed AdvancedMath benchmark show that CRAMF can be seamlessly integrated into LLM-based autoformalizers, yielding consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement.

The paper was last revised in March 2026 and represents recent advances in making mathematical formalization more automated and accessible.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03ef9664-1a07-4902-b7c2-ef92eb401112",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "c5173919-a8f4-48f2-9e57-a1af53d5d301",
  "sourceToolAssistantUUID": "03ef9664-1a07-4902-b7c2-ef92eb401112",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T13:53:39.925Z_

<details><summary>↩ Tool result · `toolu_01JrMX1W81cVtUU2HDH84t7u`</summary>

```text
Web search results for query: "StepFun-Formalizer autoformalization 2026"

Links: [{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40691"},{"title":"stepfun-ai/StepFun-Formalizer-32B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v3"},{"title":"stepfun-ai/StepFun-Formalizer-7B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"},{"title":"GitHub - stepfun-ai/StepFun-Formalizer: StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion · GitHub","url":"https://github.com/stepfun-ai/StepFun-Formalizer"},{"title":"[2508.04440v1] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440v1"},{"title":"[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440"}]

Based on the search results, here's what I found about StepFun-Formalizer autoformalization:

## Overview

StepFun-Formalizer is a project about unlocking the autoformalization potential of LLMs through knowledge-reasoning fusion. Autoformalization aims to translate natural-language mathematical statements into formally verifiable statements in formal languages such as Lean, Coq, and Isabelle.

## Key Problem and Solution

While LLMs have accelerated progress in autoformalization, existing methods still suffer from low accuracy. The research identifies two key abilities for effective autoformalization: comprehensive mastery of formal-language domain knowledge, and reasoning capability of natural language problem understanding and informal-formal alignment.

## ThinkingF Pipeline

To address these gaps, the researchers introduce ThinkingF, a data synthesis and training pipeline that improves both abilities. This is implemented through two key components: large-scale distillation and selection of data with formal knowledge from specialized models, and informal-to-formal reasoning trajectories synthesis guided by an expert-designed autoformalization template.

## Models Released

Based on this pipeline, the researchers developed two sizes of autoformalization LLMs: StepFun-Formalizer-7B and StepFun-Formalizer (a 32B model, as evidenced by available model cards).

## Publication

The work was published in the Proceedings of the AAAI Conference on Artificial Intelligence, Volume 40, AAAI-26 Technical Tracks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd988f5e-26dd-43f3-84cd-a7fad6bcfc22",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "05abd07f-5dd4-47a4-9034-d3d217a1f2d9",
  "sourceToolAssistantUUID": "fd988f5e-26dd-43f3-84cd-a7fad6bcfc22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T13:53:40.603Z_

<details><summary>↩ Tool result · `toolu_011vnD9haPcdUqKrLc5rxbSV`</summary>

```text
Web search results for query: "ProofBridge autoformalization domain 2026"

Links: [{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"GitHub - shreyascasturi/proofbridge-nesy-2026: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/shreyascasturi/proofbridge-nesy-2026"},{"title":"GitHub - PrithwishJana/ProofBridge: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/PrithwishJana/ProofBridge"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | OpenReview","url":"https://openreview.net/forum?id=U2jxHXuOX9"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | Request PDF","url":"https://www.researchgate.net/publication/396693100_ProofBridge_Auto-Formalization_of_Natural_Language_Proofs_in_Lean_via_Joint_Embeddings"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"Paper page - ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://huggingface.co/papers/2510.15681"}]

Based on the search results, here's what I found about ProofBridge and autoformalization in 2026:

## ProofBridge Overview

ProofBridge is a framework for auto-formalization of natural language proofs into Lean 4, presented as an ICLR 2026 paper. It is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains.

## Key Technical Features

At its core is a joint embedding model that aligns NL and FL (NL-FL) theorem-proof pairs in a shared semantic space, enabling cross-modal retrieval of semantically relevant FL examples to guide translation. ProofBridge integrates retrieval-augmented fine-tuning with iterative proof repair, leveraging Lean's type checker and semantic equivalence feedback to ensure both syntactic correctness and semantic fidelity.

## Performance

Despite being significantly smaller (22.7M + 218M + 1M parameters) than state-of-the-art encoders like Qwen3-Embedding-8B (8B parameters) and E5-Mistral-7B-Instruct (7B parameters), PROOFBRIDGE achieves a much higher mMG (0.65 compared to 0.29 and 0.10 respectively).

The research represents a significant advancement in the autoformalization domain by addressing the challenge of translating complete natural language mathematical theorems and proofs into formal languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff0ab2c5-79e3-4ae5-ad8e-e8fc20e6e74d",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "3e66e3e9-af0e-4cad-97a8-e735cb9c3de6",
  "sourceToolAssistantUUID": "ff0ab2c5-79e3-4ae5-ad8e-e8fc20e6e74d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-28T13:53:44.280Z_

Let me now dig deeper into the most promising leads -- the MathAtlas benchmark, FormalEvolve, the ICML 2026 AI4Math workshop challenge, the cycle consistency paper, and Faithful Autoformalization paper. Also let me search more specifically for domain-conditioning ideas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e66e3e9-af0e-4cad-97a8-e735cb9c3de6",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5XzeMBHjREEhGd3Usp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fe625ab-285c-4f50-8898-f7c7a435ab50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2o4YqCgwvegSB4Zecekhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 12928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5631,
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

_source line 32 · 2026-05-28T13:53:44.765Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QvbZMd87JkwHkSWpGB4vHR`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization subdomain domain 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fe625ab-285c-4f50-8898-f7c7a435ab50",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5XzeMBHjREEhGd3Usp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6a6944c-b172-4d6b-9b81-17f73bf96eaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2o4YqCgwvegSB4Zecekhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 12928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5631,
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

_source line 33 · 2026-05-28T13:53:45.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CzueCHEDxf7hRi1rPM6gGT`</summary>

```json
{
  "query": "FormalEvolve neuro-symbolic autoformalization domain 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a6944c-b172-4d6b-9b81-17f73bf96eaf",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5XzeMBHjREEhGd3Usp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ec296b8-cb03-4724-b516-7307917245f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2o4YqCgwvegSB4Zecekhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 12928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5631,
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

_source line 34 · 2026-05-28T13:53:45.718Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012xFLiUeQyvsXAcj8sbNviZ`</summary>

```json
{
  "query": "\"Faithful Autoformalization\" roundtrip verification 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ec296b8-cb03-4724-b516-7307917245f9",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5XzeMBHjREEhGd3Usp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2833f00c-a540-494d-ae72-c56a31e078b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2o4YqCgwvegSB4Zecekhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 12928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5631,
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

_source line 35 · 2026-05-28T13:53:46.720Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DXoybPUpqbXLes37sX4kQB`</summary>

```json
{
  "query": "autoformalization domain conditioning mathematical subdomain specialization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2833f00c-a540-494d-ae72-c56a31e078b9",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5XzeMBHjREEhGd3Usp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5439eb61-65a0-4122-b950-7ff53c3654c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2o4YqCgwvegSB4Zecekhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 12928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5631,
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

_source line 36 · 2026-05-28T13:53:47.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2Mhy2wZuWkSHE71DFeLUT`</summary>

```json
{
  "query": "ICML 2026 AI4Math autoformalization challenge FormalRx error taxonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5439eb61-65a0-4122-b950-7ff53c3654c8",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5XzeMBHjREEhGd3Usp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15fbe7a0-6c17-4cb9-a5e5-f8c9a72d5715",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2o4YqCgwvegSB4Zecekhh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 12928,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5631
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 12928,
          "cache_creation_input_tokens": 5631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5631,
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

_source line 37 · 2026-05-28T13:53:50.396Z_

<details><summary>↩ Tool result · `toolu_01QvbZMd87JkwHkSWpGB4vHR`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization subdomain domain 2026 arxiv"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/html/2602.24173v1"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"}]

Based on the search results, I found relevant information about MathAtlas:

MathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions.

The paper was released on May 13, 2026, and is available on arXiv (paper ID: 2605.14061). This benchmark addresses the gap in autoformalization research by focusing on graduate and research-level mathematics, rather than the olympiad and undergraduate-level mathematics that prior benchmarks emphasized.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6a6944c-b172-4d6b-9b81-17f73bf96eaf",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "20bfbaae-7a08-4737-aa77-04ac9b67403e",
  "sourceToolAssistantUUID": "f6a6944c-b172-4d6b-9b81-17f73bf96eaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T13:53:51.803Z_

<details><summary>↩ Tool result · `toolu_01CzueCHEDxf7hRi1rPM6gGT`</summary>

```text
Web search results for query: "FormalEvolve neuro-symbolic autoformalization domain 2026 arxiv"

Links: [{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"},{"title":"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/pdf/2603.19828"},{"title":"Neuro-Symbolic Autoformalization Framework","url":"https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"},{"title":"MerLean: An Agentic Framework For Autoformalization in Quantum Computation","url":"https://arxiv.org/html/2602.16554"},{"title":"[2405.17216] Autoformalizing Euclidean Geometry","url":"https://arxiv.org/abs/2405.17216"}]

Based on the search results, I found the paper you're looking for:

FormalEvolve is a compilation-gated neuro-symbolic evolutionary framework that formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires. FormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.

On CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes.

The paper was submitted to arXiv on March 20, 2026 (with a revision on March 23, 2026) with ID 2603.19828. The authors are Haijian Lu, Wei Wang, and Jing Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ec296b8-cb03-4724-b516-7307917245f9",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "e7296868-be40-4c45-9b9d-34d29c0fa6fe",
  "sourceToolAssistantUUID": "7ec296b8-cb03-4724-b516-7307917245f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-28T13:53:52.024Z_

<details><summary>↩ Tool result · `toolu_012xFLiUeQyvsXAcj8sbNviZ`</summary>

```text
Web search results for query: ""Faithful Autoformalization" roundtrip verification 2026 arxiv"

Links: [{"title":"[2604.25031] Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/abs/2604.25031"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981"},{"title":"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview","url":"https://openreview.net/forum?id=hUb2At2DsQ"},{"title":"Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization","url":"https://arxiv.org/html/2605.26457"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"}]

I found the paper you were looking for! Here are the key details:

**Paper Title:** Faithful Autoformalization via Roundtrip Verification and Repair

**Authors:** Daneshvar Amrollahi, Jerry Lopez, Clark Barrett

**Submission Date:** April 27, 2026

**arXiv ID:** 2604.25031

**Main Approach:** The paper proposes a roundtrip verification approach which formalize a statement, translate the result back to natural language, re-formalize, and use a formal tool to check logical equivalence. When the two formalizations agree, this provides evidence of a faithful formalization. When they disagree, a diagnosis step identifies which translation stage failed, and a targeted repair operator attempts to correct that stage.

**Evaluation:** The approach was evaluated on 150 traffic rules using Claude Opus 4.6 and GPT-5.2.

You can access the paper directly at: https://arxiv.org/abs/2604.25031


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2833f00c-a540-494d-ae72-c56a31e078b9",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "dd2e3ed8-2866-41c5-b630-5271aa8fc971",
  "sourceToolAssistantUUID": "2833f00c-a540-494d-ae72-c56a31e078b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T13:53:53.265Z_

<details><summary>↩ Tool result · `toolu_01R2Mhy2wZuWkSHE71DFeLUT`</summary>

```text
Web search results for query: "ICML 2026 AI4Math autoformalization challenge FormalRx error taxonomy"

Links: [{"title":"AI4Math @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"ICML 2026 AI for Math Workshop & Challenge 1 - FormalRx - Codabench","url":"https://www.codabench.org/competitions/16104/"},{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"ICML 2026 Workshop AI4Math | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FAI4Math"},{"title":"Formal Mathematical Reasoning: A New Frontier in AI","url":"https://arxiv.org/html/2412.16075v1"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"}]

Based on the search results, I found information about the ICML 2026 AI4Math challenge and the FormalRx error taxonomy:

The FormalRx challenge uses the FormalRx-Test dataset built on the SCI Error Taxonomy, which contains 28 error categories. The challenge evaluates whether autoformalization preserves mathematical intent, with the verdict being whether the formalization is semantically aligned.

In the autoformalization task, participants generate a formal proof in Lean 4 given a natural language informal proof. This is part of the broader AI4Math workshop at ICML 2026, which focuses on challenges like precise autoformalization and how to reliably translate natural language mathematics into formal languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15fbe7a0-6c17-4cb9-a5e5-f8c9a72d5715",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "a70990cd-2f94-431a-afc3-b770d6605443",
  "sourceToolAssistantUUID": "15fbe7a0-6c17-4cb9-a5e5-f8c9a72d5715",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-28T13:53:55.162Z_

<details><summary>↩ Tool result · `toolu_01DXoybPUpqbXLes37sX4kQB`</summary>

```text
Web search results for query: "autoformalization domain conditioning mathematical subdomain specialization 2026"

Links: [{"title":"Autoformalization of Mathematics","url":"https://www.emergentmind.com/topics/autoformalization-of-mathematics"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/html/2410.04194"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.233/"},{"title":"[2410.04194] Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/abs/2410.04194"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"}]

Based on the search results, here's what I found regarding autoformalization, domain conditioning, and mathematical subdomain specialization in 2026:

## Key Findings

**Autoformalization and Domain Specialization:**

LLMs alone are not capable of consistently and reliably delivering autoformalization, in particular as the complexity and specialization of the target domain grows. The challenge includes specialization and out-of-distribution (OOD) drifts: as one moves towards more specialized and newer domains to be autoformalized, models are progressively exposed to more challenging OOD cases.

**Recent Progress in Specialized Domains:**

For specialized domains, e.g., PDE control, the Translator module attains near-perfect autoformalization (IoU 0.992±0.007 on synthetic, >99.5% syntactic validity) and 64% IoU on manually written cases. PDE control marks early progress in applied mathematics autoformalization.

**2026 Initiatives:**

The 3rd AI for Math Workshop at ICML 2026 will be held Saturday, July 11, 2026. The workshop features a full autoformalization pipeline using the ShadowBench — 126 problems across 8 mathematical areas, tiered L2/L3/L4.

**Current Approaches:**

Recent work proposes the coordinated use of most-similar retrieval augmented generation (MS-RAG), denoising steps, and autocorrection with syntax error feedback (Auto-SEF) to improve autoformalization quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5439eb61-65a0-4122-b950-7ff53c3654c8",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "22cf4a94-1ad2-406c-97bc-0183ced701fb",
  "sourceToolAssistantUUID": "5439eb61-65a0-4122-b950-7ff53c3654c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-28T13:53:58.603Z_

Let me search for a few more specific angles -- the FineLeanCorpus domain labels, whether anyone has used domain-conditioned generation, and the M2F and Towards a Common Framework papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22cf4a94-1ad2-406c-97bc-0183ced701fb",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5Z4mv5otYRBb3teWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa0b1e6a-2df5-49ac-9599-19d79e7d0efb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHjT4sAx6eWjPX8Pwf5ft8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 555,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 18559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 43 · 2026-05-28T13:53:59.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KFLyzndkuDDL5Cw4Nb63Y5`</summary>

```json
{
  "query": "FineLeanCorpus domain labels mathematical category autoformalization conditioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa0b1e6a-2df5-49ac-9599-19d79e7d0efb",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5Z4mv5otYRBb3teWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adf70823-7cb0-4742-acf6-150c49d1b039",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHjT4sAx6eWjPX8Pwf5ft8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 555,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 18559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 44 · 2026-05-28T13:54:00.009Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NjPg2QYkbpefTvbBw1sZaj`</summary>

```json
{
  "query": "M2F automated formalization mathematical literature scale domain 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adf70823-7cb0-4742-acf6-150c49d1b039",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5Z4mv5otYRBb3teWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7695a446-0570-44fc-832e-89db2330801f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHjT4sAx6eWjPX8Pwf5ft8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 555,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 18559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 45 · 2026-05-28T13:54:01.061Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N73diqaxusanVXMPZ33KAi`</summary>

```json
{
  "query": "\"domain-conditioned\" OR \"domain conditioned\" OR \"subdomain-conditioned\" formalization mathematical lean 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7695a446-0570-44fc-832e-89db2330801f",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5Z4mv5otYRBb3teWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5a198e7-37db-4224-9401-1097d3bd21fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHjT4sAx6eWjPX8Pwf5ft8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 555,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 18559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 46 · 2026-05-28T13:54:01.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MAAt6yxuuPFhPeR3aQQyon`</summary>

```json
{
  "query": "autoformalization per-domain performance analysis algebra topology number theory 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a198e7-37db-4224-9401-1097d3bd21fd",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5Z4mv5otYRBb3teWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f3ec7df-071f-45f3-bab5-765995179cc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHjT4sAx6eWjPX8Pwf5ft8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 555,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 18559,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 555,
          "output_tokens": 271,
          "cache_read_input_tokens": 18559,
          "cache_creation_input_tokens": 2656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2656,
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

_source line 47 · 2026-05-28T13:54:06.423Z_

<details><summary>↩ Tool result · `toolu_01NjPg2QYkbpefTvbBw1sZaj`</summary>

```text
Web search results for query: "M2F automated formalization mathematical literature scale domain 2026"

Links: [{"title":"GitHub - optsuite/M2F · GitHub","url":"https://github.com/optsuite/M2F"},{"title":"[2602.17016v1] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/abs/2602.17016v1"},{"title":"[2602.17016] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/abs/2602.17016"},{"title":"[Literature Review] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://www.themoonlight.io/en/review/m2f-automated-formalization-of-mathematical-literature-at-scale"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/pdf/2602.17016"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.17016v1"},{"title":"(PDF) M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://www.researchgate.net/publication/400970848_M2F_Automated_Formalization_of_Mathematical_Literature_at_Scale"}]

Based on the search results, here's what I found about M2F:

## Overview

M2F (Math-to-Formal) is a framework for translating textbook- and paper-level mathematics into Lean projects that pass machine verification at scale. M2F is the first agentic framework for end-to-end, project-scale autoformalization in Lean.

## The Problem It Addresses

Automated formalization of mathematics enables mechanical verification but remains limited to isolated theorems and short snippets. Scaling to textbooks and research papers is largely unaddressed, as it requires managing cross-file dependencies, resolving imports, and ensuring that entire projects compile end-to-end.

## How It Works

The framework operates in two stages. The statement compilation stage splits the document into atomic blocks, orders them via inferred dependencies, and repairs declaration skeletons until the project compiles, allowing placeholders in proofs. The proof repair stage closes these holes under fixed signatures using goal-conditioned local edits. Throughout both stages, M2F keeps the verifier in the loop, committing edits only when toolchain feedback confirms improvement.

## Results

In approximately three weeks, M2F converts long-form mathematical sources into a project-scale Lean library of 153,853 lines from 479 pages textbooks on real analysis and convex analysis, fully formalized as Lean declarations with accompanying proofs. This represents textbook-scale formalization at a pace that would typically require months or years of expert effort.

The research paper was published on arXiv (arXiv:2602.17016) in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7695a446-0570-44fc-832e-89db2330801f",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "a09bcc12-6f21-4f9b-b193-baf942134995",
  "sourceToolAssistantUUID": "7695a446-0570-44fc-832e-89db2330801f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T13:54:07.027Z_

<details><summary>↩ Tool result · `toolu_01N73diqaxusanVXMPZ33KAi`</summary>

```text
Web search results for query: ""domain-conditioned" OR "domain conditioned" OR "subdomain-conditioned" formalization mathematical lean 2025 2026"

Links: [{"title":"Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/html/2604.16347v1"},{"title":"AI-Driven Formal Theorem Proving in the Lean Ecosystem","url":"https://leandojo.org/"},{"title":"Lean (proof assistant) - Wikipedia","url":"https://en.wikipedia.org/wiki/Lean_(proof_assistant)"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Lean-related conferences and events","url":"https://leanprover-community.github.io/events.html"},{"title":"(PDF) M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://www.researchgate.net/publication/400970848_M2F_Automated_Formalization_of_Mathematical_Literature_at_Scale"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"}]

Based on my web search, I found results related to Lean formalization and mathematical proof systems in 2025-2026, but the search did not return specific results containing the exact terms "domain-conditioned," "domain conditioned," or "subdomain-conditioned" in the mathematical formalization context you're asking about.

The search results show significant recent work on:
- Lean 4 formalization projects including physics, quantum mechanics, quantum field theory, and general relativity
- DeepSeek introducing DeepSeek-Prover-V2 in April 2025, an AI model designed for theorem proving in Lean 4
- Various approaches to formal theorem proving in Lean 4 using recursive proving pipelines

However, I did not find papers or resources specifically discussing "domain-conditioned," "domain conditioned," or "subdomain-conditioned" formalization in the mathematical context. If you're looking for work on these specific concepts, you might want to try searching on arXiv directly or check specialized proof assistant forums for more targeted results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a198e7-37db-4224-9401-1097d3bd21fd",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "b534bd1b-19a0-4ad9-ba7d-6e9931af15a1",
  "sourceToolAssistantUUID": "e5a198e7-37db-4224-9401-1097d3bd21fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T13:54:07.211Z_

<details><summary>↩ Tool result · `toolu_01KFLyzndkuDDL5Cw4Nb63Y5`</summary>

```text
Web search results for query: "FineLeanCorpus domain labels mathematical category autoformalization conditioning"

Links: [{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"M-A-P CriticLean: Critic-Guided Reinforcement Learning for","url":"https://arxiv.org/pdf/2507.06181"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/pdf/2511.11990"}]

Based on the search results, I found relevant information about FineLeanCorpus:

FineLeanCorpus is a dataset of 509k NL/Lean4 pairs annotated with difficulty scores (1 to 10) and mathematical domain labels. 

Regarding its application to autoformalization with conditioning, the search results show that FineLeanCorpus is used to fine-tune models for natural language to Lean4 formalization, with training approaches including supervised fine-tuning with curriculum learning based on difficulty levels.

In the context of category-specific conditioning in autoformalization more broadly, domain-specific context is constructed once per category, which is then reused for all problems in that category to provide consistent access to relevant definitions and enhance quality by anchoring the model with domain knowledge within each category.

The dataset also includes a specialized high-difficulty subset: FineLeanCorpus-Diamond comprises over 36,000 high-difficulty problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adf70823-7cb0-4742-acf6-150c49d1b039",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "a81f20b3-0235-47f9-829e-f1c1a069215d",
  "sourceToolAssistantUUID": "adf70823-7cb0-4742-acf6-150c49d1b039",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T13:54:09.187Z_

<details><summary>↩ Tool result · `toolu_01MAAt6yxuuPFhPeR3aQQyon`</summary>

```text
Web search results for query: "autoformalization per-domain performance analysis algebra topology number theory 2026"

Links: [{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Autoformalization of Mathematics","url":"https://www.emergentmind.com/topics/autoformalization-of-mathematics"},{"title":"Autoformalization in the Era of Large Language Models","url":"https://arxiv.org/pdf/2505.23486"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=7NL74jUiMg"},{"title":"[2601.03298] 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/abs/2601.03298"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"Autoformalizing Mathematical Statements by Symbolic ...","url":"https://openreview.net/pdf?id=8ihVBYpMV4"}]

Based on the search results, here are relevant findings on autoformalization per-domain performance analysis:

## Domain-Specific Characteristics

Autoformalization tasks vary significantly depending on the subfields they target, with representative areas including geometry and topology, algebra and number theory, and complex systems or frontier problems involving interdisciplinary reasoning.

Each domain has its own unique characteristics such as graphical reasoning in geometry, symbolic manipulation in algebra, and different requirements for formal systems. Algebraic and number theory problems focus more on references and nested relationships between various variables, as well as implicit operational logic.

## Recent 2026 Progress

A notable recent development is a project running since November 21, 2025 that has as of January 4, 2026, produced 160k lines of formalized topology, with about 130k lines completed in two weeks from December 22 to January 4, for an LLM subscription cost of about $100.

## Key Challenges

The autoformalization problem spans diverse domains—algebra, analysis, topology, PDEs, and program synthesis—posing significant challenges due to context dependence, implicit assumptions, and vast formal language vocabularies.

The search results show active research in autoformalization across these mathematical domains, with particular focus on understanding how different mathematical fields require tailored approaches for formal translation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f3ec7df-071f-45f3-bab5-765995179cc2",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "be64c4ce-5855-4a11-a9fe-db09635d1104",
  "sourceToolAssistantUUID": "0f3ec7df-071f-45f3-bab5-765995179cc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-28T13:54:14.196Z_

Let me do a few final targeted searches to cover remaining angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be64c4ce-5855-4a11-a9fe-db09635d1104",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5a6vRYfqnwYkRhNnAP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dde34e26-50aa-45ec-9494-e08508993376",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiGBQY9zgUZixpfNwE2dt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 21215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3628,
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

_source line 52 · 2026-05-28T13:54:15.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WjjjnBZPrPwKDwKbRhAzur`</summary>

```json
{
  "query": "ShadowBench ICML 2026 autoformalization 8 mathematical areas tiered benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde34e26-50aa-45ec-9494-e08508993376",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5a6vRYfqnwYkRhNnAP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "182bb4f9-56f9-4490-960e-5788776a0168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiGBQY9zgUZixpfNwE2dt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 21215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3628,
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

_source line 53 · 2026-05-28T13:54:16.204Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PUP6T6z35uYWBqNYNkBUic`</summary>

```json
{
  "query": "\"Lean Atlas\" integrated proof environment domain formalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "182bb4f9-56f9-4490-960e-5788776a0168",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5a6vRYfqnwYkRhNnAP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f360624e-27d7-4f94-b2ba-591dcbfa13c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiGBQY9zgUZixpfNwE2dt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 21215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3628,
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

_source line 54 · 2026-05-28T13:54:17.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJpHRUehpiotSXE92uHNvZ`</summary>

```json
{
  "query": "\"DO LLMS GAME FORMALIZATION\" VerifAI ICLR 2026 domain"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f360624e-27d7-4f94-b2ba-591dcbfa13c9",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5a6vRYfqnwYkRhNnAP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83cf4d96-cc76-4559-acb4-f98404ef45c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiGBQY9zgUZixpfNwE2dt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 21215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3628,
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

_source line 55 · 2026-05-28T13:54:17.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUmn6G4E1qbJkuZR1vxmUX`</summary>

```json
{
  "query": "CriticLean mathematical formalization domain reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83cf4d96-cc76-4559-acb4-f98404ef45c0",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5a6vRYfqnwYkRhNnAP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dddbd157-2fba-4c45-af32-a620400ae1bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiGBQY9zgUZixpfNwE2dt5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 21215,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 21215,
          "cache_creation_input_tokens": 3628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3628,
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

_source line 56 · 2026-05-28T13:54:20.072Z_

<details><summary>↩ Tool result · `toolu_01WjjjnBZPrPwKDwKbRhAzur`</summary>

```text
Web search results for query: "ShadowBench ICML 2026 autoformalization 8 mathematical areas tiered benchmark"

Links: [{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"},{"title":"ICML 2026 AI for Math Workshop & Challenge 4 - ShadowBench - Codabench","url":"https://www.codabench.org/competitions/16295/"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/pdf/2512.00997"},{"title":"Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions","url":"https://arxiv.org/pdf/2502.12065"},{"title":"UW Math AI Lab · GitHub","url":"https://github.com/uw-math-ai"}]

Based on the search results, I found information about ShadowBench and its presentation at ICML 2026:

ShadowBench is a full autoformalization pipeline featuring 126 problems across 8 mathematical areas, with tiered L2/L3/L4 difficulty levels. The benchmark involves generating formal proofs in Lean 4 from natural language informal proofs.

This benchmark is being presented as part of the 3rd AI for Math Workshop at ICML 2026, which is focused on advancing research in areas like formal theorem proving, precise autoformalization, and automated mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "182bb4f9-56f9-4490-960e-5788776a0168",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "8a3df9a5-0ec2-45c8-a1fe-7404e67fdc3f",
  "sourceToolAssistantUUID": "182bb4f9-56f9-4490-960e-5788776a0168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T13:54:22.833Z_

<details><summary>↩ Tool result · `toolu_01WUmn6G4E1qbJkuZR1vxmUX`</summary>

```text
Web search results for query: "CriticLean mathematical formalization domain reinforcement learning 2026"

Links: [{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://huggingface.co/papers/2507.06181"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"}]

Based on the search results, here's what I found about CriticLean:

## Overview

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. It addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code in automated theorem proving.

## Key Components

The CriticLean framework consists of three main components:

1. **CriticLeanGPT**: A model trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.

2. **CriticLeanBench**: A benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, with trained CriticLeanGPT models significantly outperforming strong open- and closed-source baselines.

3. **FineLeanCorpus**: A dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

## Significance

The findings highlight that optimizing the critic phase is essential for producing reliable formalizations. The research was published in July 2025 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dddbd157-2fba-4c45-af32-a620400ae1bf",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "d006ad79-c479-40cd-b68b-c921e3b4b861",
  "sourceToolAssistantUUID": "dddbd157-2fba-4c45-af32-a620400ae1bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T13:54:24.223Z_

<details><summary>↩ Tool result · `toolu_01WJpHRUehpiotSXE92uHNvZ`</summary>

```text
Web search results for query: ""DO LLMS GAME FORMALIZATION" VerifAI ICLR 2026 domain"

Links: [{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"The VerifAI Workshop @ ICLR'26 - VerifAI","url":"https://verifai-workshop.github.io/papers/"},{"title":"ICLR 2026 Workshop on Logical Reasoning of Large Language Models","url":"https://arxiv.org/pdf/2603.17169"},{"title":"Autoformalization of Game Descriptions using Large Language Models","url":"https://arxiv.org/pdf/2409.12300"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"van der Schaar Lab @ ICLR Workshops 2026 // van der Schaar Lab","url":"https://www.vanderschaar-lab.com/iclr-workshops-2026/"}]

I found the paper! Here's what I discovered:

The paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" was published at the VerifAI-2 Workshop at ICLR 2026, authored by Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut from EPFL.

The research addresses an important distinction: formal verification guarantees proof validity but not formalization faithfulness, which is especially acute for natural-language logical reasoning where models construct axiom systems from scratch without library constraints.

The researchers investigate whether frontier models exploit this gap when generating Lean 4 proofs, a behavior termed "formalization gaming". They evaluate GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.

The paper is available on arXiv (2604.19459) and was published in April 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83cf4d96-cc76-4559-acb4-f98404ef45c0",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "b6e9c1ed-1b63-4a63-910f-9f74a56d2435",
  "sourceToolAssistantUUID": "83cf4d96-cc76-4559-acb4-f98404ef45c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T13:54:24.566Z_

<details><summary>↩ Tool result · `toolu_01PUP6T6z35uYWBqNYNkBUic`</summary>

```text
Web search results for query: ""Lean Atlas" integrated proof environment domain formalization 2026"

Links: [{"title":"[2604.16347] Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/abs/2604.16347"},{"title":"Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/html/2604.16347v1"},{"title":"Lean for Science Formalization Przemyslaw Chojecki ulam.ai February 18, 2026","url":"https://www.ulam.ai/research/lean-science.pdf"},{"title":"Architecture of Lean Atlas. The Lean 4 backend extracts and classifies... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Architecture-of-Lean-Atlas-The-Lean-4-backend-extracts-and-classifies-the-dependency_fig1_404020517"},{"title":"Lean Proof Assistant Ecosystem","url":"https://www.emergentmind.com/topics/lean-proof-assistant-ecosystem"},{"title":"AI-Driven Formal Theorem Proving in the Lean Ecosystem","url":"https://leandojo.org/"}]

Based on the search results, here's what I found about Lean Atlas:

Lean Atlas is a Lean 4 tool that visualizes the dependency graph of a Lean 4 project as an interactive web viewer, classifying dependencies into type dependencies (proposition- and definition-level) and value dependencies (proof-level).

**Core Purpose:**
The tool addresses the problem that proof assistants' type checkers verify only logical correctness of proofs, not whether propositions and definitions faithfully capture intended mathematical content, leading to potential semantic hallucination in AI-generated formal proofs. Lean Atlas implements a human-in-the-loop approach where humans and AI collaboratively produce formal proofs with humans responsible for semantic verification.

**Key Feature - Lean Compass:**
Its core feature, Lean Compass, is an algorithm that, given a selected theorem set, automatically extracts the project-specific nodes whose semantic correctness can affect those target statements, thereby reducing the candidate set for semantic review in large-scale formalizations.

**Evaluation Results:**
The tool was evaluated on six Lean 4 formalization projects; proof-heavy projects achieved 94-99% average node reduction, a 6-theorem milestone subset of FLT achieved 59.8%, mixed PhysLib 69.0%, and definition-heavy XMSS 27.3%.

Lean Atlas is available as open-source software. The research was published as an arXiv paper in March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f360624e-27d7-4f94-b2ba-591dcbfa13c9",
  "isSidechain": true,
  "promptId": "8767c321-2551-40c1-992e-a00cbbbe019b",
  "agentId": "a39ac29d9f4d62432",
  "type": "user",
  "uuid": "127010c4-a914-4980-98f3-b02cb745a2a6",
  "sourceToolAssistantUUID": "f360624e-27d7-4f94-b2ba-591dcbfa13c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-28T13:55:10.183Z_

Now I have a comprehensive picture. Here is my report:

---

## Results: Search for Domain-Adaptive/Domain-Conditioned Autoformalization (March-May 2026)

### Key Finding: No Direct Competitor Found

After exhaustive searching across multiple query formulations, **I found no paper from March-May 2026 (or earlier) that directly proposes conditioning autoformalization on mathematical subdomain as a first-class architectural or training mechanism.** The specific phrases "domain-conditioned autoformalization," "subdomain-conditioned formalization," and "domain-adaptive autoformalization" return zero exact matches. The idea of explicitly conditioning the autoformalization model on the mathematical subdomain (e.g., feeding a domain tag like "algebraic topology" or "number theory" into the model to alter its generation behavior) does not appear to have been published as a standalone contribution.

### Closest Related Work (Potential Overlap to Monitor)

Several recent papers touch on domain-awareness in ways that could partially overlap:

1. **FineLeanCorpus domain labels in Cycle Consistency Fine-tuning** (March 2026, [arXiv:2603.24372](https://arxiv.org/abs/2603.24372)) -- The FineLeanCorpus dataset (509K NL/Lean4 pairs) includes **mathematical domain labels** and difficulty scores. The cycle consistency paper uses curriculum learning based on difficulty but does **not** condition generation on domain labels. However, it evaluates on an OOD test set with different domains from training. The domain labels exist in the dataset but are not used as conditioning signals -- this is a clear gap your work could fill.

2. **CRAMF: Concept-driven Retrieval-Augmented Mathematical Formalization** (revised March 2026, [arXiv:2508.06931](https://arxiv.org/abs/2508.06931)) -- Retrieves formal definitions from Mathlib4 to ground autoformalization. Constructs **domain-specific context once per category** and reuses it for all problems in that category. This is the closest existing mechanism to domain conditioning, but it operates via retrieval rather than model conditioning. Up to 62.1% relative improvement.

3. **Aria: Agent for Retrieval and Iterative Auto-Formalization** (ICLR 2026 poster, [arXiv:2510.04520](https://arxiv.org/abs/2510.04520)) -- Uses dependency-graph-based decomposition and AriaScorer for term-level grounding via Mathlib. Strong results (91.6% compilation, 68.5% accuracy on ProofNet). No explicit domain conditioning, but the dependency decomposition implicitly captures domain structure.

4. **MathAtlas: A Benchmark for Autoformalization in the Wild** (May 2026, [arXiv:2605.14061](https://arxiv.org/abs/2605.14061)) -- 52K items from 103 graduate textbooks with a **178K-relation dependency graph**. Covers diverse mathematical subdomains. Strong baselines achieve only 9.8% correctness on theorems. This benchmark would be ideal for evaluating domain-conditioned approaches, and its existence strengthens the motivation for your work.

5. **ShadowBench at ICML 2026 AI4Math** ([ai4math2026.github.io](https://ai4math2026.github.io/)) -- 126 problems across **8 mathematical areas** at tiered difficulty (L2/L3/L4). The FormalRx challenge uses a **28-category SCI Error Taxonomy**. These area-specific and error-taxonomy-specific evaluations are relevant but do not propose domain conditioning as a method.

6. **StepFun-Formalizer** (AAAI 2026, [arXiv:2508.04440](https://arxiv.org/abs/2508.04440)) -- Knowledge-reasoning fusion via ThinkingF pipeline. Addresses domain knowledge mastery but through general knowledge distillation, not subdomain conditioning.

7. **M2F: Automated Formalization at Scale** (February 2026, [arXiv:2602.17016](https://arxiv.org/abs/2602.17016)) -- First agentic framework for project-scale autoformalization. Operates on real analysis and convex analysis textbooks. Domain-specific but not domain-conditioned; it processes one domain at a time without a conditioning mechanism.

8. **FormalEvolve** (March 2026, [arXiv:2603.19828](https://arxiv.org/abs/2603.19828)) -- Neuro-symbolic evolutionary search for diverse autoformalization candidates. No domain conditioning.

9. **Faithful Autoformalization via Roundtrip Verification** (April 2026, [arXiv:2604.25031](https://arxiv.org/abs/2604.25031)) -- Roundtrip verification and targeted repair. Focuses on semantic faithfulness, not domain adaptation.

10. **ProofBridge** (ICLR 2026, [arXiv:2510.15681](https://arxiv.org/abs/2510.15681)) -- Joint embedding alignment of NL-FL pairs. Cross-modal retrieval. No domain conditioning extension found.

### Teams Checked for Domain-Conditioning Extensions

- **CRAMF team**: Latest revision is March 2026; retrieval-augmented but no explicit domain conditioning added.
- **DRIFT team**: No 2026 update beyond the original Oct 2025 paper ([arXiv:2510.10815](https://arxiv.org/abs/2510.10815)).
- **Aria team**: ICLR 2026 poster; no domain-conditioning extension found.
- **StepFun-Formalizer team**: AAAI 2026 publication; no domain-conditioning follow-up found.
- **ProofBridge team**: ICLR 2026 main track; no domain-conditioning extension found.

### Key Observations from the Survey Literature

The autoformalization survey by [arXiv:2505.23486](https://arxiv.org/html/2505.23486v1) explicitly notes that:
- Each mathematical domain has "unique characteristics such as graphical reasoning in geometry and symbolic manipulation in algebra"
- A key challenge is "specialization and OOD drifts: as one moves towards more specialized and newer domains, models are exposed to more challenging OOD cases"
- Future research directions include "domain-adaptive training"

This confirms the gap: the community recognizes that domain variation is a major challenge, and domain-adaptive training is listed as a future direction, but **no one has published a system that explicitly conditions autoformalization on mathematical subdomain**.

### Bottom Line

Your idea of conditioning autoformalization on mathematical subdomain appears to be **novel and unoccupied** as of late May 2026. The closest work (CRAMF) uses per-category retrieval context but not model-level conditioning. The existence of domain-labeled datasets (FineLeanCorpus), domain-stratified benchmarks (MathAtlas, ShadowBench), and explicit calls for domain-adaptive training in the survey literature all position your contribution well. The main risk is that someone could quickly implement domain conditioning using the existing FineLeanCorpus domain labels, since the infrastructure is already there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "127010c4-a914-4980-98f3-b02cb745a2a6",
  "isSidechain": true,
  "agentId": "a39ac29d9f4d62432",
  "requestId": "req_011CbV5bESPnVXwdiYowwfXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4479c58-4643-442c-9a1e-edf274a18069",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "f8313759-b4a9-45da-8c2f-cc3e03277c54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSv4Jxya9Ka73LNdk3R5FL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1272,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 24843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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
