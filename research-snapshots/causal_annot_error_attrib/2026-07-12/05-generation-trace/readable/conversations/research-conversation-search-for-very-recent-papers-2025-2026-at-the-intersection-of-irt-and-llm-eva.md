# Research conversation: Search for very recent papers (2025-2026) at the intersection of IRT and LLM evaluation, and any new contamination corre

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a85ee19f30d5592dd.jsonl`
- **Structured JSON:** [`c5c9ff2710926b8bf35b.json`](../../sessions/c5/c5c9ff2710926b8bf35b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-28T12:49:56.646Z_

Search for very recent papers (2025-2026) at the intersection of IRT and LLM evaluation, and any new contamination correction methods. I need to check whether anyone has published work that overlaps with a "Gated IRT for LLM contamination-ability decomposition" approach. Search:

1. "IRT contamination LLM" on arXiv (2025-2026)
2. "contamination correction benchmark LLM IRT" 
3. "item response theory large language model decontamination"
4. "gated IRT cheating detection" to see if anyone extended Shu et al. 2013 DGM recently
5. Check if there are any new papers on combining adversarial item variants with psychometric models

Also specifically search for:
6. "LEGO-IRT LLM evaluation" to find the LEGO-IRT paper (arXiv Oct 2025)
7. Any papers from April-May 2026 on LLM benchmark contamination that might be concurrent work

Use WebSearch. Report any papers that could be concurrent/competing work, with titles, authors, dates, and how they relate. Under 400 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "3affc792-55ba-4569-9b31-b1297e69cc9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T12:49:56.652Z_

```json
{
  "parentUuid": "3affc792-55ba-4569-9b31-b1297e69cc9e",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
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
  "uuid": "141da17d-b634-45c6-93b0-f308187cd631",
  "timestamp": "2026-05-28T12:49:56.652Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T12:49:56.654Z_

```json
{
  "parentUuid": "141da17d-b634-45c6-93b0-f308187cd631",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "70b7e9a6-8c41-445f-8c94-d04f0037ea05",
  "timestamp": "2026-05-28T12:49:56.654Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T12:49:59.741Z_



I'll search for all these topics in parallel using WebSearch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b7e9a6-8c41-445f-8c94-d04f0037ea05",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzg7WEopud8E5AMo4PY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3e0b38d-58f3-4d87-8760-c2138876ee4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRjs5MiYiBuLmUi2V2DrU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1581,
      "cache_read_input_tokens": 7407,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1581
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1581,
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

_source line 5 · 2026-05-28T12:49:59.750Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T8aicTQpHPgmBYrc63fKjs`</summary>

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
  "parentUuid": "a3e0b38d-58f3-4d87-8760-c2138876ee4d",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzg7WEopud8E5AMo4PY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "027fd5ce-dd90-4d5b-a7c9-9b984422122c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRjs5MiYiBuLmUi2V2DrU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1581,
      "cache_read_input_tokens": 7407,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1581
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1581,
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

_source line 6 · 2026-05-28T12:49:59.755Z_

<details><summary>↩ Tool result · `toolu_01T8aicTQpHPgmBYrc63fKjs`</summary>

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
  "parentUuid": "027fd5ce-dd90-4d5b-a7c9-9b984422122c",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "3f518274-380c-4df4-8928-9aefe4f1fbbd",
  "sourceToolAssistantUUID": "027fd5ce-dd90-4d5b-a7c9-9b984422122c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T12:50:02.116Z_



Now I'll run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f518274-380c-4df4-8928-9aefe4f1fbbd",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecdeabb5-13bf-4aa9-8539-648b2554b201",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 8 · 2026-05-28T12:50:03.356Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DoaFDBBvpBpBZhwD1Dkat5`</summary>

```json
{
  "query": "IRT contamination LLM arXiv 2025 2026",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecdeabb5-13bf-4aa9-8539-648b2554b201",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bf69ba0-51f4-4668-8c1b-b0f1b1dead83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 9 · 2026-05-28T12:50:03.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012o9mRQ8CpWwAsL5DiuoJzx`</summary>

```json
{
  "query": "contamination correction benchmark LLM IRT item response theory 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bf69ba0-51f4-4668-8c1b-b0f1b1dead83",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d9f0d7-25de-4a61-b928-319d3193f782",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 10 · 2026-05-28T12:50:04.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DQ2GyhrHbXppY8bLzaEpwo`</summary>

```json
{
  "query": "item response theory large language model decontamination 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d9f0d7-25de-4a61-b928-319d3193f782",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3465f1a8-de2f-4760-a8f8-9fa59ca21b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 11 · 2026-05-28T12:50:04.552Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011AMhHDWvQdc2c1LDgMC2Gf`</summary>

```json
{
  "query": "gated IRT cheating detection DGM Shu 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3465f1a8-de2f-4760-a8f8-9fa59ca21b92",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9a17007-40d1-4d9a-95a3-212805e6e2f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 12 · 2026-05-28T12:50:05.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01762JMy5jmqgUdYKnNffgfo`</summary>

```json
{
  "query": "adversarial item variants psychometric models LLM evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9a17007-40d1-4d9a-95a3-212805e6e2f9",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56e47552-1ce9-4c17-9615-45f9d71a8bc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 13 · 2026-05-28T12:50:05.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113DnYCBh1oG2jUpN17F6Rh`</summary>

```json
{
  "query": "LEGO-IRT LLM evaluation arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56e47552-1ce9-4c17-9615-45f9d71a8bc8",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8200bb14-62ac-4dc3-9f97-c1f0c660f56a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 14 · 2026-05-28T12:50:05.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RvF3j4XcgzHPkotnunnomb`</summary>

```json
{
  "query": "LLM benchmark contamination detection new paper April May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8200bb14-62ac-4dc3-9f97-c1f0c660f56a",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzgLzMFV4KLHEubrgAT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67168f6c-d073-4286-950c-945e61623244",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MmDoRXDsdH5z7xSdBLi1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 8988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 15 · 2026-05-28T12:50:11.662Z_

<details><summary>↩ Tool result · `toolu_01DQ2GyhrHbXppY8bLzaEpwo`</summary>

```text
Web search results for query: "item response theory large language model decontamination 2025 2026"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Lifting the benchmark iceberg with item-response theory | OpenReview","url":"https://openreview.net/forum?id=ZyVQqK7mcP"},{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large   Language Model Evaluation","url":"https://arxiv.org/pdf/2406.13990"}]

Based on the search results, I found relevant recent research on item response theory and large language model benchmarking from 2025-2026:

## Key Research Findings

A framework called Pseudo-Siamese Network for Item Response Theory (PSN-IRT) was proposed as an enhanced Item Response Theory framework that can be utilized for accurate and reliable estimations of item characteristics and model abilities. This approach was applied to analyze 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

Research has identified a "benchmark iceberg" phenomenon where much of the variability in model rankings stems not from true capability differences, but from hidden implementation choices, and minor changes to these implementation details can alter model rankings. To address this, psychometric principles from educational testing and item response theory (IRT) were leveraged to transform benchmarks from opaque leaderboards into transparent measurement instruments.

## Related Decontamination Work

The search results also revealed LiveBench, described as a challenging, contamination-limited LLM benchmark, which represents contemporary efforts to address data contamination issues in LLM evaluation.

The research paper on Lost in Benchmarks was published as an AAAI 2026 oral presentation, indicating active ongoing work in this area during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3465f1a8-de2f-4760-a8f8-9fa59ca21b92",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "69e12231-075f-4b40-8840-2c3fee13990e",
  "sourceToolAssistantUUID": "3465f1a8-de2f-4760-a8f8-9fa59ca21b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T12:50:11.668Z_

<details><summary>↩ Tool result · `toolu_012o9mRQ8CpWwAsL5DiuoJzx`</summary>

```text
Web search results for query: "contamination correction benchmark LLM IRT item response theory 2025 2026"

Links: [{"title":"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/html/2605.00238"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v1"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"},{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/pdf/2510.00844"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"}]

Based on the search results, here are the key findings related to contamination correction, benchmarking, LLM evaluation, and Item Response Theory (IRT):

## Recent IRT Applications to LLM Evaluation

Recent work has applied IRT to LLM evaluation, including diagnosing the reliability of LLM-as-a-judge systems and modeling latent LLM abilities together with query difficulty and discrimination for routing and performance prediction.

## PSN-IRT Framework for Benchmark Analysis

A paper from 2025-2026 proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. This framework was used to conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

## Contamination-Limited Benchmarks

LiveBench is described as a challenging, contamination-limited LLM benchmark, and other contamination-resistant benchmarks include LiveCodeBench, FrontierMath, MMLU-Pro, and LiveBench.

## Inference-Time Decontamination

Inference-time decontamination mitigates contamination effects during model inference rather than by filtering benchmark items, though a common issue is that interventions strong enough to reduce contamination often affect clean accuracy as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d9f0d7-25de-4a61-b928-319d3193f782",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "82095108-d210-4c5b-b6ff-705f05035d1a",
  "sourceToolAssistantUUID": "92d9f0d7-25de-4a61-b928-319d3193f782",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T12:50:12.041Z_

<details><summary>↩ Tool result · `toolu_01DoaFDBBvpBpBZhwD1Dkat5`</summary>

```text
Web search results for query: "IRT contamination LLM arXiv 2025 2026"

Links: [{"title":"[2604.05766] The LLM Effect on IR Benchmarks: A Meta-Analysis of Effectiveness, Baselines, and Contamination","url":"https://arxiv.org/abs/2604.05766"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://arxiv.org/pdf/2308.08493"},{"title":"The LLM Effect on IR Benchmarks: A Meta-Analysis of ...","url":"https://arxiv.org/pdf/2604.05766"},{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"},{"title":"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in   Closed-Source LLMs","url":"https://arxiv.org/pdf/2402.03927"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"}]

Based on the search results, here are the relevant papers on IRT (Information Retrieval and Text) contamination and LLM contamination from arXiv in 2025-2026:

## Key Papers Found:

1. **"The LLM Effect on IR Benchmarks: A Meta-Analysis of Effectiveness, Baselines, and Contamination"** (April 2026)
   - Analyzes 143 publications reporting results on the TREC Robust04 collection and the TREC Deep Learning 2020 (DL20) passage retrieval benchmark to examine longitudinal trends in retrieval effectiveness and baseline strength. Reveals measurable contamination in both benchmarks, and while excluding contaminated topics reduces effectiveness, confidence intervals remain wide, making it difficult to determine whether the LLM effect reflects genuine methodological advances or memorization from pretraining data.

2. **"Preference Leakage: A Contamination Problem in LLM-as-a-judge"** (March 2026)
   - Exposes preference leakage, a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. Empirically confirms the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks.

3. **"Time Travel in LLMs: Tracing Data Contamination in Large Language Models"** (2023)
   - Achieves an accuracy between 92% and 100% in detecting if an LLM is contaminated with seven datasets, and findings indicate that GPT-4 is contaminated with AG News, WNLI, and XSum datasets.

4. **"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs"** (2024)
   - Addresses the issue of indirect data contamination in closed-source LLMs by conducting a systematic literature review of 255 papers and carefully detailing data leakage emerging from them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bf69ba0-51f4-4668-8c1b-b0f1b1dead83",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "02d1a325-8444-4f83-90c9-855bc8145a41",
  "sourceToolAssistantUUID": "2bf69ba0-51f4-4668-8c1b-b0f1b1dead83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T12:50:12.110Z_

<details><summary>↩ Tool result · `toolu_011AMhHDWvQdc2c1LDgMC2Gf`</summary>

```text
Web search results for query: "gated IRT cheating detection DGM Shu 2025 2026"

Links: [{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"},{"title":"(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise","url":"https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"},{"title":"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/25106396/"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-012-9311-3"},{"title":"Online Gaming Cheating Detection in 2026 | GearsME","url":"https://gearsme.com/en/online-gaming-cheating-detection-in-2026/"},{"title":"Are Exam Questions Known in Advance? Using Local Dependence to Detect Cheating","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5131967/"},{"title":"Cheating detection in remote assessment environments","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11138899"},{"title":"Detecting AI-Assisted Cheating in Online Exams through Behavior Analytics","url":"https://arxiv.org/pdf/2510.18881"}]

Based on the search results, I found information about the Deterministic, Gated Item Response Theory Model (DGM) for cheating detection by Shu:

## Overview

The Deterministic, Gated Item Response Theory Model (DGM) was proposed to identify cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items).

## How It Works

A "gated" function is introduced to decompose the observed examinees' performance into two distributions—the true ability distribution determined by examinees' true ability and the cheating distribution determined by examinees' cheating ability. Test cheaters who have score gain due to item exposure are identified through the comparison of the two distributions.

## Technical Details

Hierarchical Markov Chain Monte Carlo is used as the model's estimation framework. The model can be used to identify examinees having pre-knowledge on the exposed items.

The search results primarily reference the original 2013 publication by Shu in Psychometrika, with a Cambridge Core update dated January 1, 2025. However, the results don't show any major new publications or developments specifically from 2025-2026 beyond recent citings of the original work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9a17007-40d1-4d9a-95a3-212805e6e2f9",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "da680c2d-550a-4167-89fa-2d093676f298",
  "sourceToolAssistantUUID": "a9a17007-40d1-4d9a-95a3-212805e6e2f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T12:50:12.642Z_

<details><summary>↩ Tool result · `toolu_0113DnYCBh1oG2jUpN17F6Rh`</summary>

```text
Web search results for query: "LEGO-IRT LLM evaluation arXiv 2025"

Links: [{"title":"[2510.04051] Toward a unified framework for data-efficient evaluation of large language models","url":"https://arxiv.org/abs/2510.04051"},{"title":"Toward a unified framework for data-efficient evaluation of large language models","url":"https://arxiv.org/html/2510.04051v1"},{"title":"[2504.03048] LLM Library Learning Fails: A LEGO-Prover Case Study","url":"https://arxiv.org/abs/2504.03048"},{"title":"LEGO-Eval: Towards Fine-grained Evaluation on Synthesizing 3D Embodied Environments with Tool Augmentation","url":"https://arxiv.org/html/2511.03001"},{"title":"Moving LLM evaluation forward: lessons from human judgment research","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12149859/"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"}]

Based on the search results, I found the paper you're looking for:

**LEGO-IRT: Toward a unified framework for data-efficient evaluation of large language models**

LEGO-IRT is a unified and flexible framework for data-efficient LLM evaluation, published on arXiv on October 5, 2025 (arXiv:2510.04051).

Key features of the framework:

- LEGO-IRT's novel design natively supports both binary and continuous evaluation metrics
- It introduces a factorized architecture to explicitly model and leverage structural knowledge, decomposing model ability estimates into a general component and structure-specific (e.g., per-metric or per-benchmark) components

Performance:

- Through extensive experiments involving 70 LLMs across 5 benchmarks, LEGO-IRT achieves stable capability estimates using just 3% of the total evaluation items
- Incorporating structural knowledge reduces estimation error by up to 10% and the latent abilities estimated by the framework may align more closely with human preferences

You can access the full paper at https://arxiv.org/abs/2510.04051


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8200bb14-62ac-4dc3-9f97-c1f0c660f56a",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "0b79e12b-631b-47b3-bb3a-39d74205dd69",
  "sourceToolAssistantUUID": "8200bb14-62ac-4dc3-9f97-c1f0c660f56a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T12:50:14.522Z_

<details><summary>↩ Tool result · `toolu_01762JMy5jmqgUdYKnNffgfo`</summary>

```text
Web search results for query: "adversarial item variants psychometric models LLM evaluation 2025 2026"

Links: [{"title":"Psychometric Benchmarks for AI Evaluation","url":"https://www.emergentmind.com/topics/psychometrically-informed-benchmarks"},{"title":"Evaluating Large Language Models with Psychometrics","url":"https://arxiv.org/html/2406.17675v2"},{"title":"LLM Benchmarks","url":"https://www.emergentmind.com/topics/large-language-model-benchmarks"},{"title":"Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality","url":"https://arxiv.org/pdf/2510.11254"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"Benchmarking adversarial robustness to bias elicitation in large language models: scalable automated assessment with LLM-as-a-judge | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-025-06862-6"},{"title":"Large Language Model Evaluation in 2025: Smarter Metrics That ...","url":"https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"}]

Based on the search results, I found several relevant sources on adversarial item variants, psychometric models, and LLM evaluation from 2025-2026:

## Key Findings:

**Psychometric Models for LLM Evaluation:**
Behavioral stability and reliability including adversarial prompt robustness are essential for evaluating the internal stability and reproducibility of benchmark-based inferences. Metrics are evolving toward multi-dimensional, compositional, or item-level psychometric models such as PSN-IRT, which models item discriminability, guessing rates, and difficulty.

**Adversarial Item Variants:**
PromptBench, AdvGLUE, and BOSS introduce input perturbations (typos, paraphrase, semantic variance) to stress-test model consistency, while REALTOXICITYPROMPTS and HateXplain evaluate content appropriateness under adversarial prompt settings. Additionally, the Human-Centered Survey offers two versions: a regular version and an adversarial version.

**Challenges in Psychometric Testing of LLMs:**
Early work highlights challenges such as the prompt sensitivity of LLMs, and it remains unclear whether psychometric tests designed and validated for humans can be applied to assess LLMs in a comparable way. There is a risk of data contamination, as LLMs may have encountered psychometric items or scoring procedures during pretraining, and test results may reflect prior exposure rather than genuine characteristics.

**Item Development and Calibration:**
Psychometric screening eliminates items with poor discrimination or inappropriate difficulty, and online item selection using calibrated item banks drives Computerized Adaptive Testing (CAT), which concentrates evaluation on maximally informative items for each model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56e47552-1ce9-4c17-9615-45f9d71a8bc8",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "ff8453e4-6cd3-4944-9e04-fee69ba5ad58",
  "sourceToolAssistantUUID": "56e47552-1ce9-4c17-9615-45f9d71a8bc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T12:50:19.007Z_

<details><summary>↩ Tool result · `toolu_01RvF3j4XcgzHPkotnunnomb`</summary>

```text
Web search results for query: "LLM benchmark contamination detection new paper April May 2026"

Links: [{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models","url":"https://arxiv.org/pdf/2402.15938"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"How Can I Publish My LLM Benchmark Without Giving the True Answers Away?","url":"https://arxiv.org/pdf/2505.18102"},{"title":"Are Large Language Models Truly Smarter Than Humans?","url":"https://arxiv.org/pdf/2603.16197"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/pdf/2404.00699"},{"title":"PaCoST: Paired Confidence Significance Testing for Benchmark   Contamination Detection in Large Language Models","url":"https://arxiv.org/pdf/2406.18326"}]

Based on the search results, here are some recent papers on LLM benchmark contamination detection from April-May 2026:

## Key Recent Papers

1. **Detecting Benchmark Contamination Through Watermarking** (February 2026)
   This paper proposes embedding non-intrusive watermarks in benchmark datasets before release, enabling reporting of both model performance and a contamination p-value score that represents an upper bound to the probability that the model hasn't been trained on the benchmark questions.

2. **How Can I Publish My LLM Benchmark Without Giving the True Answers Away?** (May 2026)
   This paper presents a method that detects contamination using only model performance—no benchmark data or model internals needed—making it suitable for black-box and private benchmarks.

3. **Are Large Language Models Truly Smarter Than Humans?** (March 2026)
   This paper presents a rigorous multi-method contamination audit of six frontier LLMs—GPT-40, GPT-40-mini, DeepSeek-R1, DeepSeek-V3, Llama-3.3-70B, and Qwen3-235B—conducted entirely using public APIs and open benchmarks.

These papers represent the latest advances in detecting and addressing benchmark contamination in large language models, with various approaches ranging from watermarking techniques to performance-based detection methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67168f6c-d073-4286-950c-945e61623244",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "d02f367c-00ad-4aaa-8def-0e7751db993f",
  "sourceToolAssistantUUID": "67168f6c-d073-4286-950c-945e61623244",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-28T12:50:22.336Z_

Let me run a couple of follow-up searches to get more detail on the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02f367c-00ad-4aaa-8def-0e7751db993f",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzhm4Udhn4BuvD9GMz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bb67aee-ff2c-4847-b177-fe3c935f5c71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQ2Mgc4pYeiLrnJ99PvbbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5822,
      "cache_read_input_tokens": 9608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5822,
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

_source line 23 · 2026-05-28T12:50:23.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQWYkbLXovvx626M1E4NpL`</summary>

```json
{
  "query": "arXiv 2510.00844 \"compact representations LLM abilities item response theory\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb67aee-ff2c-4847-b177-fe3c935f5c71",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzhm4Udhn4BuvD9GMz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c286313-c899-4429-9909-0d11049c60a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQ2Mgc4pYeiLrnJ99PvbbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5822,
      "cache_read_input_tokens": 9608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5822,
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

_source line 24 · 2026-05-28T12:50:24.420Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PJXPmNjuLgETuVtVifBdHs`</summary>

```json
{
  "query": "arXiv 2601.19334 \"inference-time decontamination reusing leaked benchmarks\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c286313-c899-4429-9909-0d11049c60a6",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzhm4Udhn4BuvD9GMz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f7b4b08-aee9-4b29-980a-3e6e3da921aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQ2Mgc4pYeiLrnJ99PvbbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5822,
      "cache_read_input_tokens": 9608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5822,
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

_source line 25 · 2026-05-28T12:50:24.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzJc45DUNPC5MUphcWVXve`</summary>

```json
{
  "query": "arXiv 2602.00521 \"diagnosing reliability LLM judge item response theory\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f7b4b08-aee9-4b29-980a-3e6e3da921aa",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzhm4Udhn4BuvD9GMz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4967a8da-793e-4da1-adff-44d31016e0dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQ2Mgc4pYeiLrnJ99PvbbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5822,
      "cache_read_input_tokens": 9608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5822,
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

_source line 26 · 2026-05-28T12:50:31.098Z_

<details><summary>↩ Tool result · `toolu_01PJXPmNjuLgETuVtVifBdHs`</summary>

```text
Web search results for query: "arXiv 2601.19334 "inference-time decontamination reusing leaked benchmarks" 2026"

Links: [{"title":"[2601.19334v1] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334v1"},{"title":"[2601.19334] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large   Language Model Evaluation","url":"https://arxiv.org/pdf/2406.13990"},{"title":"[2406.13990] Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/abs/2406.13990"},{"title":"[Literature Review] Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://www.themoonlight.io/en/review/inference-time-decontamination-reusing-leaked-benchmarks-for-large-language-model-evaluation"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.532/"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation | Request PDF","url":"https://www.researchgate.net/publication/386183526_Inference-Time_Decontamination_Reusing_Leaked_Benchmarks_for_Large_Language_Model_Evaluation"}]

Based on the search results, I found information about arXiv 2601.19334:

## arXiv 2601.19334: "When Benchmarks Leak: Inference-Time Decontamination for LLMs"

The paper was submitted on January 27, 2026, with authors Jianzhe Chai, Yu Zhe, and Jun Sakuma.

**Overview:**
The paper addresses the issue that benchmark reliability is threatened by test set contamination, where test samples or their close variants leak into training data and artificially inflate reported performance.

**Problem and Solution:**
Prior mitigation efforts have attempted to identify and remove contaminated items before evaluation (but this alters the evaluation set), or suppress contaminated behavior at evaluation time (but this often interferes with normal inference and degrades performance on clean inputs). 

The paper proposes DeconIEP, a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space.

You can access the full paper on arXiv at https://arxiv.org/abs/2601.19334.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f7b4b08-aee9-4b29-980a-3e6e3da921aa",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "6ca44714-23cf-4b21-bc4f-ba0da9cd7190",
  "sourceToolAssistantUUID": "9f7b4b08-aee9-4b29-980a-3e6e3da921aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T12:50:31.306Z_

<details><summary>↩ Tool result · `toolu_01AQWYkbLXovvx626M1E4NpL`</summary>

```text
Web search results for query: "arXiv 2510.00844 "compact representations LLM abilities item response theory""

Links: [{"title":"[2510.00844] Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/abs/2510.00844"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/learning-compact-representations-llm-abilities-via-item"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory | OpenReview","url":"https://openreview.net/forum?id=uRDsLCJo2x"},{"title":"GitHub - JianhaoChen-nju/IrtNet · GitHub","url":"https://github.com/JianhaoChen-nju/IrtNet"},{"title":"(PDF) Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://www.researchgate.net/publication/396094822_Learning_Compact_Representations_of_LLM_Abilities_via_Item_Response_Theory"},{"title":"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/html/2605.00238"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/pdf/2510.00844"},{"title":"LEARNING COMPACT REPRESENTATIONS OF LLM ABILITIES ...","url":"https://openreview.net/pdf/16fbdebf6f9746da46e522a527bfcd069cbb8964.pdf"},{"title":"LEARNING COMPACT REPRESENTATIONS OF LLM ...","url":"https://openreview.net/pdf?id=uRDsLCJo2x"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://arxiv.org/pdf/2509.22888"}]

I found the arXiv paper you're looking for! Here's a summary of the research:

**Paper Title:** Learning Compact Representations of LLM Abilities via Item Response Theory

**Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, and Shuyue Hu

**Submission Date:** October 1, 2025

**Key Idea:** The work explores how to learn compact representations of LLM abilities that can facilitate downstream tasks, such as model routing and performance prediction on new benchmarks.

**Methodology:** Inspired by item response theory (IRT) in psychometrics, the authors model the probability of a model answering a query correctly as a function of three key factors: the model's multi-skill ability vector, the query's discrimination vector that separates models of differing skills, and the query's difficulty scalar. To learn these parameters jointly, they introduce a Mixture-of-Experts (MoE) network that couples model- and query-level embeddings.

**Framework:** The architecture comprises a dense MoE layer which captures the feature of queries and an IRT layer which trains LLM embeddings based on item response theory.

You can access the paper directly at https://arxiv.org/abs/2510.00844.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c286313-c899-4429-9909-0d11049c60a6",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "5105e5e8-1397-4b83-b096-6ca7e3bb860a",
  "sourceToolAssistantUUID": "6c286313-c899-4429-9909-0d11049c60a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T12:50:35.896Z_

<details><summary>↩ Tool result · `toolu_01XzJc45DUNPC5MUphcWVXve`</summary>

```text
Web search results for query: "arXiv 2602.00521 "diagnosing reliability LLM judge item response theory""

Links: [{"title":"[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/abs/2602.00521"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://www.arxiv.org/pdf/2602.00521"},{"title":"Paper page - Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://huggingface.co/papers/2602.00521"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/html/2602.00521v1"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item ...","url":"https://www.researchgate.net/publication/400369489_Diagnosing_the_Reliability_of_LLM-as-a-Judge_via_Item_Response_Theory"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/html/2412.12509v1"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/pdf/2412.12509"},{"title":"Diagnosing LLM Judge Reliability: Conformal Prediction Sets and Transitivity Violations","url":"https://arxiv.org/html/2604.15302"},{"title":"Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges","url":"https://arxiv.org/pdf/2601.20913"}]

I found the paper you're looking for! Here's what I found about arXiv paper 2602.00521:

**Paper Title:** Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory

**Authors:** Junhyuk Choi and 3 other authors (Sohhyung Park, Chanhee Cho, Hyeonchu Park, and Bugeun Kim)

**Key Contribution:** The paper introduces a two-phase diagnostic framework for assessing reliability of LLM-as-a-Judge, grounded in Item Response Theory (IRT).

**Framework Details:** The framework adopts Graded Response Model (GRM) of IRT and formalizes reliability along two complementary dimensions: (1) intrinsic consistency, defined as the stability of measurement behavior under prompt variations, and (2) human alignment, capturing correspondence with human evaluation.

**Practical Impact:** The signals from the framework provide practical guidance for verifying reliability of LLM-as-a-Judge and identifying potential causes of unreliability.

**Submission Date:** The paper was submitted on January 31, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4967a8da-793e-4da1-adff-44d31016e0dd",
  "isSidechain": true,
  "promptId": "98a3f0be-c89b-4064-8212-f2f1733d0772",
  "agentId": "a85ee19f30d5592dd",
  "type": "user",
  "uuid": "fd6bbc25-1346-4d20-b5ad-1508a7b0c651",
  "sourceToolAssistantUUID": "4967a8da-793e-4da1-adff-44d31016e0dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T12:50:58.214Z_

Here is my analysis of the landscape:

---

**Most relevant papers to a "Gated IRT for LLM contamination-ability decomposition" approach:**

**1. PSN-IRT (AAAI 2026 Oral)** -- "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" (arXiv 2505.15055, May 2025). Uses a Pseudo-Siamese Network IRT architecture to model item discriminability, guessing, and difficulty across 11 benchmarks / 41,871 items. Focuses on benchmark quality diagnosis, NOT contamination decomposition. Close in IRT+LLM space but orthogonal to your gating mechanism.

**2. LEGO-IRT** (arXiv 2510.04051, Oct 2025) -- "Toward a unified framework for data-efficient evaluation of LLMs." Factorized IRT architecture decomposing ability into general + structure-specific components. Achieves stable estimates with 3% of items. Relevant architecturally (factorized ability) but does not address contamination.

**3. IrtNet** (arXiv 2510.00844, Oct 2025) -- "Learning Compact Representations of LLM Abilities via IRT." MoE network coupling model/query embeddings with a multi-skill ability vector, discrimination vector, and difficulty scalar. Closest to a neural IRT for LLMs but no contamination component.

**4. DeconIEP** (arXiv 2601.19334, Jan 2026) -- "When Benchmarks Leak: Inference-Time Decontamination for LLMs." Applies bounded embedding-space perturbations at inference time. Addresses contamination correction but uses NO psychometric/IRT framework.

**5. IRT for LLM-as-Judge** (arXiv 2602.00521, Jan 2026) -- Uses Graded Response Model IRT to diagnose judge reliability. IRT application but unrelated to contamination.

**6. Shu et al. 2013 DGM** -- No new extensions found. The original Deterministic Gated Model in Psychometrika remains uncited in the LLM context. This is your key differentiator: nobody has adapted the gating mechanism to decompose LLM performance into genuine-ability vs. contamination-driven components.

**7. Recent contamination papers (2026):** Watermarking-based detection (arXiv 2502.17259, Feb 2026), black-box performance-based detection (arXiv 2505.18102, May 2026), and a multi-method contamination audit of frontier LLMs (arXiv 2603.16197, Mar 2026). None use IRT.

**Bottom line:** No one has published work combining a gated IRT model with LLM contamination decomposition. The IRT+LLM papers (PSN-IRT, LEGO-IRT, IrtNet) ignore contamination. The contamination papers ignore IRT. Adapting Shu et al.'s DGM gating mechanism to separate memorization from genuine ability in LLMs appears to be a clear gap. PSN-IRT and LEGO-IRT are the closest neighbors you should cite and differentiate from.

Sources:
- [PSN-IRT / Lost in Benchmarks (AAAI 2026)](https://arxiv.org/abs/2505.15055)
- [LEGO-IRT](https://arxiv.org/abs/2510.04051)
- [IrtNet / Compact Representations](https://arxiv.org/abs/2510.00844)
- [DeconIEP / When Benchmarks Leak](https://arxiv.org/abs/2601.19334)
- [IRT for LLM-as-Judge](https://arxiv.org/abs/2602.00521)
- [Shu et al. 2013 DGM](https://link.springer.com/article/10.1007/s11336-012-9311-3)
- [Benchmark Contamination via Watermarking](https://arxiv.org/abs/2502.17259)
- [Black-box contamination detection](https://arxiv.org/abs/2505.18102)
- [Multi-method contamination audit](https://arxiv.org/abs/2603.16197)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd6bbc25-1346-4d20-b5ad-1508a7b0c651",
  "isSidechain": true,
  "agentId": "a85ee19f30d5592dd",
  "requestId": "req_011CbUzj1LjoKFaWutHjKMAE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3594d6c-c409-4acc-9d24-f16d2a34f7c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "b71487b8-a467-4168-9aa3-5f9ea29849d3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jCSLVQrtb8rdajixLiy1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 15430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2600,
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
