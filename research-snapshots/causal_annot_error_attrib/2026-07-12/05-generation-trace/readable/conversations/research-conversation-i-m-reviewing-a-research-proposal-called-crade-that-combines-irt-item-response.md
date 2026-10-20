# Research conversation: I'm reviewing a research proposal called "CRADE" that combines IRT (Item Response Theory) with contamination detection a

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af89ed972f0b00e1c.jsonl`
- **Structured JSON:** [`842f1fcb3e8e72ff873e.json`](../../sessions/84/842f1fcb3e8e72ff873e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-28T12:39:35.801Z_

I'm reviewing a research proposal called "CRADE" that combines IRT (Item Response Theory) with contamination detection and adversarial robustness for LLM evaluation. The proposal claims no existing work sits at this three-way intersection. I need you to do an adversarial search for competing or concurrent work that the authors may have missed.

Search for ALL of these queries using WebSearch:

1. "contamination-aware IRT" OR "contamination item response theory" LLM 2025 2026
2. "benchmark contamination correction" "item response theory" 2026
3. "decontamination" "IRT" "large language model" 2026
4. "gated IRT" language model
5. site:arxiv.org "contamination" "adversarial" "IRT" LLM evaluation 2026
6. site:openreview.net contamination IRT LLM evaluation 2026
7. "joint contamination ability" OR "contamination-adjusted scoring" LLM 2026
8. "benchmark integrity" "measurement theory" LLM 2025 2026
9. "paired item" contamination LLM evaluation
10. site:arxiv.org "psychometric" "contamination" "language model" 2026

For each search, report: what you found, whether any paper addresses the same three-way intersection (IRT + contamination + adversarial variants), and any paper that could be a direct competitor. Be thorough — the goal is to find work the proposal authors missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "56d95603-c41d-4c6f-b1fc-e7700091f1bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T12:39:35.804Z_

```json
{
  "parentUuid": "56d95603-c41d-4c6f-b1fc-e7700091f1bb",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
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
  "uuid": "0a14936d-221b-43c6-8f4f-1ee56057c88f",
  "timestamp": "2026-05-28T12:39:35.804Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T12:39:35.805Z_

```json
{
  "parentUuid": "0a14936d-221b-43c6-8f4f-1ee56057c88f",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7179a6f6-a721-4a2b-b3ab-c1143e4ee434",
  "timestamp": "2026-05-28T12:39:35.805Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T12:39:41.854Z_



I'll conduct all 10 searches systematically. Let me start by loading the WebSearch tool, then run the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7179a6f6-a721-4a2b-b3ab-c1143e4ee434",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytM4HQtWAWDwNVehHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff91797d-fbe5-451f-9951-b54ebf5600e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdDkBNMQ6RD3rZYkFEYW5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1695,
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

_source line 5 · 2026-05-28T12:39:42.485Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XiQYj2mnHoUkwgygXcV8gh`</summary>

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
  "parentUuid": "ff91797d-fbe5-451f-9951-b54ebf5600e2",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytM4HQtWAWDwNVehHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8938f30e-1bb0-4469-8e8f-afe75989254c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdDkBNMQ6RD3rZYkFEYW5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 7407,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1695
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1695,
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

_source line 6 · 2026-05-28T12:39:42.493Z_

<details><summary>↩ Tool result · `toolu_01XiQYj2mnHoUkwgygXcV8gh`</summary>

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
  "parentUuid": "8938f30e-1bb0-4469-8e8f-afe75989254c",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "07a5e1ee-0143-4c42-8430-aaf29b9b035d",
  "sourceToolAssistantUUID": "8938f30e-1bb0-4469-8e8f-afe75989254c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T12:39:45.672Z_



Now I'll run all 10 searches. I'll batch them in groups since they're independent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a5e1ee-0143-4c42-8430-aaf29b9b035d",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytrmxZn788awLE24dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d044518a-3f22-4a0d-b826-b1e92df47faa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvkV43EGEybLWWyboYE2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 633,
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

_source line 8 · 2026-05-28T12:39:46.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N83FU7jtf7QHQv4GwiG7Gp`</summary>

```json
{
  "query": "\"contamination-aware IRT\" OR \"contamination item response theory\" LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d044518a-3f22-4a0d-b826-b1e92df47faa",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytrmxZn788awLE24dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1476a1b9-f456-453c-96c8-6a482f60611a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvkV43EGEybLWWyboYE2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 633,
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

_source line 9 · 2026-05-28T12:39:46.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BT9NA4iLL79AQCP5nChef`</summary>

```json
{
  "query": "\"benchmark contamination correction\" \"item response theory\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1476a1b9-f456-453c-96c8-6a482f60611a",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytrmxZn788awLE24dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39e1c54b-5f63-4763-8fdb-d460de7c1fd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvkV43EGEybLWWyboYE2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 633,
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

_source line 10 · 2026-05-28T12:39:47.535Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NcsTgL32YaCf2PS1zLDFpm`</summary>

```json
{
  "query": "\"decontamination\" \"IRT\" \"large language model\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39e1c54b-5f63-4763-8fdb-d460de7c1fd3",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytrmxZn788awLE24dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12eaba5d-64a5-431c-a0dc-fd5f27a1a54d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvkV43EGEybLWWyboYE2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 633,
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

_source line 11 · 2026-05-28T12:39:47.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FDCNKYwQA8EkYdt71J2npD`</summary>

```json
{
  "query": "\"gated IRT\" language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12eaba5d-64a5-431c-a0dc-fd5f27a1a54d",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytrmxZn788awLE24dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0101e87-7a09-44d8-8a8a-c67494f84714",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvkV43EGEybLWWyboYE2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 633,
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

_source line 12 · 2026-05-28T12:39:47.593Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012pEm4UZ3c6cDh3botbNWtE`</summary>

```json
{
  "query": "site:arxiv.org \"contamination\" \"adversarial\" \"IRT\" LLM evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0101e87-7a09-44d8-8a8a-c67494f84714",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUytrmxZn788awLE24dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "680d9cb3-e3e6-4750-8fe2-3692cce04fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvkV43EGEybLWWyboYE2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 633,
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

_source line 13 · 2026-05-28T12:39:53.814Z_

<details><summary>↩ Tool result · `toolu_01N83FU7jtf7QHQv4GwiG7Gp`</summary>

```text
Web search results for query: ""contamination-aware IRT" OR "contamination item response theory" LLM 2025 2026"

Links: [{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v1"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/pdf/2510.00844"},{"title":"[2506.01048] IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory","url":"https://arxiv.org/abs/2506.01048"},{"title":"IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.761/"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"}]

Based on the search results, I found several relevant papers on Item Response Theory (IRT) applied to Large Language Models in 2025-2026, though specific results on "contamination-aware IRT" are limited. Here are the key findings:

## Main Research Papers Found:

1. **"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"** (Zhou et al., 2025-2026): This paper proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. The authors conducted extensive analysis on 11 LLM benchmarks comprising 41,871 items.

2. **"IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory"** (Song et al., 2025): This work is inspired by Item Response Theory, a psychological measurement methodology, and explicitly models the relationship between LLM capabilities and user query attributes, enabling accurate prediction of response performance.

3. **"Learning Compact Representations of LLM Abilities via Item Response Theory"** (2025): This paper proposes a novel approach to construct compact representations of model abilities, drawing inspiration from item response theory (IRT), a well-established statistical framework used in education and psychology to measure latent abilities through standardized tests.

4. **"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory"** (2026): This paper examines diverse LLM judges and shows that leveraging IRT-GRM yields interpretable signals for diagnosing judgments systematically.

While these papers apply IRT to LLM evaluation and benchmarking, they don't appear to specifically focus on "contamination-aware" IRT. However, one relevant benchmark project is "Livebench: A challenging, contamination-limited LLM benchmark" (2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1476a1b9-f456-453c-96c8-6a482f60611a",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "7443be95-a0c5-4ee2-b099-aa9dd3c20382",
  "sourceToolAssistantUUID": "1476a1b9-f456-453c-96c8-6a482f60611a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T12:39:53.819Z_

<details><summary>↩ Tool result · `toolu_01FDCNKYwQA8EkYdt71J2npD`</summary>

```text
Web search results for query: ""gated IRT" language model"

Links: [{"title":"Gated Word-Character Recurrent Language Model","url":"https://arxiv.org/pdf/1606.01700"},{"title":"Gated Word-Character Recurrent Language Model","url":"https://www.researchgate.net/publication/303821974_Gated_Word-Character_Recurrent_Language_Model"},{"title":"Gated Word-Character Recurrent Language Model","url":"https://aclanthology.org/D16-1209.pdf"},{"title":"Behavior Gated Language Models","url":"https://arxiv.org/pdf/1909.00107"},{"title":"Language Modeling with Gated Convolutional Networks","url":"https://arxiv.org/pdf/1612.08083"}]

Based on the search results, here's what I found about "gated" language models:

The search results primarily feature the "Gated Word-Character Recurrent Language Model," an RNN-LM with LSTM units that utilizes both character-level and word-level inputs, with a gate that adaptively finds the optimal mixture of the two input types.

This model with the gating mechanism effectively utilizes character-level inputs for rare and out-of-vocabulary words and outperforms word-level language models on several English corpora.

The search results also mention other gated approaches to language modeling:

- Gated convolutional networks applied to language modeling, which achieve higher accuracy and converge faster than LSTM-style gating

- Behavior Gated Language Models, which use behavioral information to gate the outputs of the language model before final word prediction

However, I should note that the search results don't specifically address "gated IRT" (Item Response Theory) language models. If you're looking for information about that specific combination, you may want to clarify or search with different terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0101e87-7a09-44d8-8a8a-c67494f84714",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "a242d18b-43f2-4c15-9e80-21e7a273c8ae",
  "sourceToolAssistantUUID": "b0101e87-7a09-44d8-8a8a-c67494f84714",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T12:39:53.934Z_

<details><summary>↩ Tool result · `toolu_011BT9NA4iLL79AQCP5nChef`</summary>

```text
Web search results for query: ""benchmark contamination correction" "item response theory" 2026"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.24210"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"Fantastic Bugs and Where to Find Them in AI Benchmarks","url":"https://arxiv.org/pdf/2511.16842"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"}]

I found relevant research on this topic! Here are the key results:

## Primary Finding: PSN-IRT Framework

The main work is PSN-IRT, a framework based on Item Response Theory (IRT), for a deep analysis of LLM benchmark quality. This research, titled "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory," is an AAAI 2026 oral presentation.

## Key Problem Being Addressed

LLM benchmarks exhibit data contamination in numerous items, compromising their reliability. Through extensive experiments on 12 LLMs across 11 diverse datasets, researchers demonstrated that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.

## Solution and Impact

Model rankings derived from high-quality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models. Based on PSN-IRT, researchers conducted extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality, and demonstrated that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.

This research addresses the important problem of benchmark contamination in LLM evaluation by applying Item Response Theory to identify and correct for contaminated items in benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39e1c54b-5f63-4763-8fdb-d460de7c1fd3",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "cfae5914-3f2d-489f-9255-c46d2dce874b",
  "sourceToolAssistantUUID": "39e1c54b-5f63-4763-8fdb-d460de7c1fd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T12:39:55.364Z_

<details><summary>↩ Tool result · `toolu_012pEm4UZ3c6cDh3botbNWtE`</summary>

```text
Web search results for query: "site:arxiv.org "contamination" "adversarial" "IRT" LLM evaluation 2026"

Links: [{"title":"2025 Year in Review for LLM Evaluation: When the Scorecard Broke | Goodeye Labs","url":"https://www.goodeyelabs.com/insights/llm-evaluation-2025-review"},{"title":"LLM Benchmark Datasets Should Be Contamination-Resistant","url":"https://arxiv.org/html/2605.19999v1"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"A Survey on the Security of Long-Term Memory in LLM Agents: Toward Mnemonic Sovereignty","url":"https://arxiv.org/html/2604.16548v1"},{"title":"A Comprehensive Survey of Contamination Detection Meth","url":"https://openreview.net/pdf?id=SxNMjbtdFm"},{"title":"Evaluation data contamination in LLMs: how do we measure it and (when)   does it matter?","url":"https://arxiv.org/pdf/2411.03923"},{"title":"The Evaluation Challenge of Agency: Reliability, Contamination,","url":"https://www.techrxiv.org/users/1027157/articles/1386937/master/file/data/LLMAgentSurvey_KDD2026/LLMAgentSurvey_KDD2026.pdf"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"}]

Based on the search results, I found relevant research about contamination and adversarial evaluation in LLM benchmarking, though the results don't specifically focus on "IRT" (Item Response Theory) evaluation. Here are the key findings:

## Recent Research on Contamination and Adversarial Evaluation

Recent work by Luo et al. (2026) examines how inversion attacks affect different model architectures, finding that inversion is feasible for models using Multi-Head Attention but much less effective on models using Grouped-Query Attention and related modern architectures.

By December 2025, the AI industry recognized that static, public tests had become training data, which triggered a fundamental shift toward dynamic, adversarial, and expert-grounded evaluation.

## Detection Methods

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

## Contamination-Resistant Benchmarks

The fix involves contamination-resistant benchmarks: LiveCodeBench, FrontierMath, MMLU-Pro, and LiveBench.

The search results included papers from arXiv and related sources discussing contamination and adversarial methods in LLM evaluation, but I did not find papers specifically addressing IRT (Item Response Theory) in this context. If you're looking for research that combines IRT methodology with LLM contamination assessment, you may need to search with more specific IRT-related terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "680d9cb3-e3e6-4750-8fe2-3692cce04fc4",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "4b7838e6-803e-481b-a225-ba178d5d81c4",
  "sourceToolAssistantUUID": "680d9cb3-e3e6-4750-8fe2-3692cce04fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T12:39:55.879Z_

<details><summary>↩ Tool result · `toolu_01NcsTgL32YaCf2PS1zLDFpm`</summary>

```text
Web search results for query: ""decontamination" "IRT" "large language model" 2026"

Links: [{"title":"[Quick Review] Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://liner.com/review/inferencetime-decontamination-reusing-leaked-benchmarks-for-large-language-model-evaluation"},{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large   Language Model Evaluation","url":"https://arxiv.org/pdf/2406.13990"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Contamination Detection for VLMs Using Multi‑Modal Semantic Perturbations | OpenReview","url":"https://openreview.net/forum?id=gk6OC3XIZW"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"KNOWLEDGE DISTILLATION AS DECONTAMINATION? ...","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"}]

Based on the search results, I found relevant information about decontamination and IRT (Item Response Theory) in the context of large language models:

## Inference-Time Decontamination (ITD)

Inference-Time Decontamination (ITD) is a novel framework to mitigate evaluation result inflation caused by data contamination in Large Language Models. ITD is a novel technique that identifies and rewrites potentially memorized responses during model inference.

## Item Response Theory (IRT) Framework

PSN-IRT is a framework based on Item Response Theory (IRT), for a deep analysis of LLM benchmark quality. This AAAI 2026 oral paper introduces an approach that uses Item Response Theory (IRT) for a deep analysis of LLM benchmark quality.

## Context

Large Language Models (LLMs) often exhibit inflated performance on benchmarks due to test data contamination, where training data inadvertently includes benchmark examples. These frameworks represent recent approaches (2024-2026) to address the challenge of ensuring accurate evaluation of LLM capabilities despite potential data contamination in their training datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12eaba5d-64a5-431c-a0dc-fd5f27a1a54d",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "2f5f7f63-ba5e-4aa7-a3f0-d0ee28466840",
  "sourceToolAssistantUUID": "12eaba5d-64a5-431c-a0dc-fd5f27a1a54d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-28T12:39:58.725Z_

Now let me run the remaining 5 searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5f7f63-ba5e-4aa7-a3f0-d0ee28466840",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyupzLBEmeAwnkecbgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8028ce1-fb2f-412b-a578-10e3e03cf0e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFoCLdVSt4NLwJ7azKUoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1384,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 9735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
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

_source line 19 · 2026-05-28T12:39:59.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011H5HmGD5B8GPDdgSRuXZZH`</summary>

```json
{
  "query": "site:openreview.net contamination IRT LLM evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8028ce1-fb2f-412b-a578-10e3e03cf0e7",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyupzLBEmeAwnkecbgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cbc824b-f566-42c8-9e0f-1602e86b86ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFoCLdVSt4NLwJ7azKUoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1384,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 9735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
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

_source line 20 · 2026-05-28T12:40:00.163Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RgJv7tHNMQPqNqoRwomZTg`</summary>

```json
{
  "query": "\"joint contamination ability\" OR \"contamination-adjusted scoring\" LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cbc824b-f566-42c8-9e0f-1602e86b86ce",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyupzLBEmeAwnkecbgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c292d576-77b9-4932-ae95-8b3bd5f02dd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFoCLdVSt4NLwJ7azKUoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1384,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 9735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
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

_source line 21 · 2026-05-28T12:40:00.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ap9K3PKxHq8aXgajNhq6GV`</summary>

```json
{
  "query": "\"benchmark integrity\" \"measurement theory\" LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c292d576-77b9-4932-ae95-8b3bd5f02dd0",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyupzLBEmeAwnkecbgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08be59b3-d799-4d26-8de7-6d5d5bf5a851",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFoCLdVSt4NLwJ7azKUoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1384,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 9735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
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

_source line 22 · 2026-05-28T12:40:01.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wr5BJVFXEYJ95dGGBFrSo`</summary>

```json
{
  "query": "\"paired item\" contamination LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08be59b3-d799-4d26-8de7-6d5d5bf5a851",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyupzLBEmeAwnkecbgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3e8b60a-80ad-4825-a54a-7f7d34df246d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFoCLdVSt4NLwJ7azKUoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1384,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 9735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
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

_source line 23 · 2026-05-28T12:40:01.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXVGnhypXNZAygJEpyH3xG`</summary>

```json
{
  "query": "site:arxiv.org \"psychometric\" \"contamination\" \"language model\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3e8b60a-80ad-4825-a54a-7f7d34df246d",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyupzLBEmeAwnkecbgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11a72f9c-d5f3-4c1b-bde4-412858067afe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFoCLdVSt4NLwJ7azKUoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1384,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 9735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2673,
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

_source line 24 · 2026-05-28T12:40:07.046Z_

<details><summary>↩ Tool result · `toolu_011H5HmGD5B8GPDdgSRuXZZH`</summary>

```text
Web search results for query: "site:openreview.net contamination IRT LLM evaluation 2026"

Links: [{"title":"Auditing Test Data Contamination with Error Rate Control for Reliable LLM Evaluation | OpenReview","url":"https://openreview.net/forum?id=YsoabhpS7z"},{"title":"Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination’s Impact on Machine Translation | OpenReview","url":"https://openreview.net/forum?id=MpjtvkvXDo"},{"title":"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination | OpenReview","url":"https://openreview.net/forum?id=TuvDxubEfE"},{"title":"OBSCURING DATA CONTAMINATION THROUGH TRANSLATION","url":"https://openreview.net/pdf?id=omg9K6lI93"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview","url":"https://openreview.net/forum?id=sKYHBTAxVa"},{"title":"Towards Contamination Resistant Benchmarks","url":"https://arxiv.org/pdf/2505.08389"},{"title":"Detecting Benchmark Contamination Through Watermarking | OpenReview","url":"https://openreview.net/forum?id=WFGxFzFDmQ"},{"title":"Evaluation data contamination in LLMs: how do we measure it and (when)   does it matter?","url":"https://arxiv.org/pdf/2411.03923"}]

The search returned several relevant papers from OpenReview related to data contamination in LLM evaluation from 2025-2026. Here are the key findings:

## Main Results

1. **Auditing Test Data Contamination with Error Rate Control** - A paper submitted to ICLR 2026 that addresses controlling the false discovery rate (FDR) of contaminated data mistakenly identified as clean while maximizing clean data retained.

2. **Overestimation in LLM Evaluation** - Research showing that contamination with both source and target substantially inflates BLEU scores, with inflation 2.5 times larger (up to 30 BLEU points) for 8B compared to 1B models.

3. **Benchmark Data Contamination Mitigation** - A study with 10 LLMs, 5 benchmarks, and 20 BDC mitigation strategies revealing that no existing strategy effectively balances fidelity and contamination resistance.

4. **Detecting Benchmark Contamination Through Watermarking** - A proactive approach proposing embedding cryptographic watermarks into benchmarks before release through question reformulation.

5. **LiveBench** - A new benchmark designed to be resistant to test set contamination, containing frequently-updated questions from recent information sources with automatic objective scoring.

Notably, I did not find results specifically mentioning "IRT" (Item Response Theory) in the search results, though the results are highly relevant to contamination and LLM evaluation in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cbc824b-f566-42c8-9e0f-1602e86b86ce",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "b29e65fb-82dd-4a54-a6ca-9f876d297600",
  "sourceToolAssistantUUID": "8cbc824b-f566-42c8-9e0f-1602e86b86ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T12:40:08.037Z_

<details><summary>↩ Tool result · `toolu_01Ap9K3PKxHq8aXgajNhq6GV`</summary>

```text
Web search results for query: ""benchmark integrity" "measurement theory" LLM 2025 2026"

Links: [{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs","url":"https://arxiv.org/pdf/2602.11674"},{"title":"Leaving the barn door open for Clever Hans: Simple features predict LLM   benchmark answers","url":"https://arxiv.org/pdf/2410.11672"},{"title":"Quantifying construct validity in large language model evaluations","url":"https://arxiv.org/pdf/2602.15532"},{"title":"INTEGRALBENCH: Benchmarking LLMs with Definite Integral Problems","url":"https://arxiv.org/pdf/2507.21130"},{"title":"LLM Evaluation and Benchmarking 2026 | Zylos Research","url":"https://zylos.ai/research/2026-01-16-llm-evaluation-benchmarking"},{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/pdf/2602.24173"}]

I found several relevant results about benchmark integrity and measurement theory for LLMs in 2025-2026. Here are the key findings:

## Benchmark Health and Integrity Framework

A new Benchmark Health Index (BHI) framework has been introduced to audit evaluation sets along three axes: Capability Discrimination (measuring how sharply a benchmark separates model performance), Anti-Saturation (estimating remaining headroom before ceiling effects), and Impact (quantifying influence across academic and industrial ecosystems). This framework, based on analysis of 106 validated benchmarks from 91 representative models in 2025, is the first to quantify benchmark health at a macro level and provides a principled basis for benchmark selection.

## Measurement and Validity Concerns

Benchmarks play an essential role in orienting progress in AI, but there are significant validity concerns. Prior work has outlined criteria that NLP benchmarks should meet related to construct and internal validity, and spurious correlations have been demonstrated in NLP benchmarks, with studies showing that models can achieve performance above chance by relying on simple features despite removing necessary elements for determining correct answers.

## Current State of LLM Benchmarking (2026)

As of 2026, traditional benchmarks like MMLU show saturation (88%+ scores), pushing the field toward harder tests like GPQA and domain-specific evaluations. The field faces ongoing challenges including benchmark gaming, position bias in LLM judges, and the need for continuous evaluation strategies that blend automated metrics with human judgment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08be59b3-d799-4d26-8de7-6d5d5bf5a851",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "d212dc49-1482-4cef-8a2f-d27537e8d900",
  "sourceToolAssistantUUID": "08be59b3-d799-4d26-8de7-6d5d5bf5a851",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T12:40:08.222Z_

<details><summary>↩ Tool result · `toolu_01RgJv7tHNMQPqNqoRwomZTg`</summary>

```text
Web search results for query: ""joint contamination ability" OR "contamination-adjusted scoring" LLM 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Evaluating Large Language Models on the 2026 Korean CSAT Mathematics Exam: Measuring Mathematical Ability in a Zero-Data-Leakage Setting","url":"https://arxiv.org/pdf/2511.18649"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/pdf/2603.21636"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"}]

Based on the search results, here's what I found related to your query:

## Contamination-Adjusted Scoring in LLM Evaluation (2026)

One approach is the DCR (Data Contamination Rating) framework, which synthesizes contamination scores via a fuzzy inference system to produce a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance, validated across 9 LLMs on multiple benchmark tasks.

## Joint Contamination Ability & Detection Methods

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

## Key 2026 Context

A model's published benchmark score predicts production performance only when three conditions hold: the benchmark tests tasks similar to your use case, the test set is clean of training data contamination, and the benchmark hasn't saturated to the point where score differences are statistically meaningless.

An audit framework has been proposed for analyzing contamination sensitivity and score confidence in LLM benchmarks, using a router-worker setup to compare clean-control conditions with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed.

The search results show that contamination-adjusted scoring and joint contamination assessment are active areas of research in 2026 LLM evaluation methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c292d576-77b9-4932-ae95-8b3bd5f02dd0",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "6ace7886-a973-4111-8be3-869ae8e937d6",
  "sourceToolAssistantUUID": "c292d576-77b9-4932-ae95-8b3bd5f02dd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T12:40:08.269Z_

<details><summary>↩ Tool result · `toolu_011wr5BJVFXEYJ95dGGBFrSo`</summary>

```text
Web search results for query: ""paired item" contamination LLM evaluation"

Links: [{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"},{"title":"Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?","url":"https://arxiv.org/html/2411.03923v1"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"LLM Datasets and Contamination. Large Language Models (LLMs) are in the… | by Andrej | Prem Blog | Medium","url":"https://medium.com/prem-blog/llm-datasets-and-contamination-bcff3ad708aa"},{"title":"LLM Datasets and Contamination","url":"https://www.linkedin.com/pulse/llm-datasets-contamination-premai-bzj5f"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v4"},{"title":"(PDF) Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?","url":"https://www.researchgate.net/publication/385595167_Evaluation_data_contamination_in_LLMs_how_do_we_measure_it_and_when_does_it_matter"},{"title":"LatestEval: Addressing Data Contamination in Language Model Evaluation","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29822/31427"}]

Based on the search results, here's what I found about "paired item" contamination in LLM evaluation:

PaCoST (Paired Confidence Significance Testing) is a method designed to detect benchmark contamination in LLMs. The method constructs a counterpart for each piece of data with the same distribution, and performs statistical analysis of the corresponding confidence to test whether the model is significantly more confident under the original benchmark.

Evaluation data contamination refers to the inadvertent mixing of samples from evaluation benchmarks into pre-training corpora, which makes it difficult to interpret evaluation benchmark scores. When input-output pairs from test sets or benchmarks are included in training data, this contaminates the model with the test data and correct answers, artificially inflating the model's performance metrics.

The search results also show broader research on contamination detection, including the "LLM decontaminator" method, which identifies the top-k training items with highest similarity using embedding similarity search, then evaluates each pair to determine if they are the same using an advanced LLM like GPT-4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3e8b60a-80ad-4825-a54a-7f7d34df246d",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "c5cc3d93-a934-402e-8e74-7f46d21cfa9a",
  "sourceToolAssistantUUID": "e3e8b60a-80ad-4825-a54a-7f7d34df246d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T12:40:08.946Z_

<details><summary>↩ Tool result · `toolu_01WXVGnhypXNZAygJEpyH3xG`</summary>

```text
Web search results for query: "site:arxiv.org "psychometric" "contamination" "language model" 2026"

Links: [{"title":"[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/abs/2510.07175"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"Proving Test Set Contamination in Black Box Language Models","url":"https://arxiv.org/pdf/2310.17623"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/pdf/2404.00699"},{"title":"Estimating Contamination via Perplexity: Quantifying Memorisation in   Language Model Evaluation","url":"https://arxiv.org/pdf/2309.10677"},{"title":"Are Large Language Models Truly Smarter Than Humans?","url":"https://arxiv.org/pdf/2603.16197"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/html/2510.07175v2"}]

Based on the search results, I found relevant research on arxiv.org about psychometric contamination in language models from 2026:

## Key Finding

Popular psychometric inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination, where models not only memorize items but can also adjust their responses to achieve specific target scores.

## Main Paper

Recent studies apply psychometric questionnaires to Large Language Models to assess psychological constructs such as values, personality, moral foundations, and dark traits. Although prior work has raised concerns about possible data contamination from psychometric inventories, there has been no systematic attempt to quantify the extent of this contamination. A framework proposes to systematically measure data contamination in psychometric evaluations of LLMs, evaluating three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching.

The primary paper on this topic is "Quantifying Data Contamination in Psychometric Evaluations of LLMs" by Jongwook Han and colleagues from Seoul National University (arxiv paper 2510.07175, last updated January 30, 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11a72f9c-d5f3-4c1b-bde4-412858067afe",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "74953c24-0de5-4775-b7fc-36f06d8e348b",
  "sourceToolAssistantUUID": "11a72f9c-d5f3-4c1b-bde4-412858067afe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T12:40:12.684Z_

Now let me do a few targeted follow-up searches to dig deeper into the most promising leads -- particularly the PSN-IRT paper, the DCR paper, and the "Silicon Bureaucracy" paper which seemed highly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74953c24-0de5-4775-b7fc-36f06d8e348b",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyvnmASGFDPnWEMZ9Av",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b12e642-7cf9-4fd0-a431-1cbf85ec860f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GQ2yYcmhsZVdmyu6cwvWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 12408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5441,
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

_source line 30 · 2026-05-28T12:40:13.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GKpJ8AbBkir7TbcgrUGcws`</summary>

```json
{
  "query": "PSN-IRT \"contamination\" \"adversarial\" Zhou AAAI 2026 benchmark quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b12e642-7cf9-4fd0-a431-1cbf85ec860f",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyvnmASGFDPnWEMZ9Av",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d61d956f-04e9-4410-b52a-0ff930989e83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GQ2yYcmhsZVdmyu6cwvWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 12408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5441,
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

_source line 31 · 2026-05-28T12:40:14.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JnEPMbaKhAhJKtAmpjheym`</summary>

```json
{
  "query": "\"Silicon Bureaucracy\" \"contamination sensitivity\" \"score confidence\" LLM benchmarks 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d61d956f-04e9-4410-b52a-0ff930989e83",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyvnmASGFDPnWEMZ9Av",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48dda7af-7cef-44e0-a946-a12d97e6abee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GQ2yYcmhsZVdmyu6cwvWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 12408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5441,
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

_source line 32 · 2026-05-28T12:40:15.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USAQvBmkYPAp29iLnW1kYU`</summary>

```json
{
  "query": "DCR \"Data Contamination Rating\" \"contamination-aware\" LLM accuracy adjustment 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48dda7af-7cef-44e0-a946-a12d97e6abee",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyvnmASGFDPnWEMZ9Av",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c14a17a4-0f25-4fe9-9034-21c9fe2354c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GQ2yYcmhsZVdmyu6cwvWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 12408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5441,
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

_source line 33 · 2026-05-28T12:40:15.705Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WdPg2b1zkSDpuGbwTPGryE`</summary>

```json
{
  "query": "\"Quantifying Data Contamination\" \"Psychometric Evaluations\" LLMs Han Seoul 2025 2026 IRT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c14a17a4-0f25-4fe9-9034-21c9fe2354c1",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyvnmASGFDPnWEMZ9Av",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53e89a42-f8a4-431d-b506-b122decaea44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GQ2yYcmhsZVdmyu6cwvWE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 12408,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5441
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 12408,
          "cache_creation_input_tokens": 5441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5441,
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

_source line 34 · 2026-05-28T12:40:20.749Z_

<details><summary>↩ Tool result · `toolu_01GKpJ8AbBkir7TbcgrUGcws`</summary>

```text
Web search results for query: "PSN-IRT "contamination" "adversarial" Zhou AAAI 2026 benchmark quality"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814/44775"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2508.00552"},{"title":"IO-RAE: Information-Obfuscation Reversible Adversarial Example for Audio Privacy Protection | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/37140"},{"title":"Sure! Here's a short and concise title for your paper: \"Contamination in Generated Text Detection Benchmarks\"","url":"https://arxiv.org/pdf/2511.09200"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"},{"title":"Are Large Language Models Truly Smarter Than Humans?","url":"https://arxiv.org/pdf/2603.16197"}]

Based on the web search results, I found relevant information about PSN-IRT and related benchmark quality research:

## PSN-IRT Framework

PSN-IRT is a framework based on Item Response Theory (IRT) for a deep analysis of LLM benchmark quality. PSN-IRT is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture and can be utilized for accurate and reliable estimations of item characteristics and model abilities.

## Benchmark Analysis

PSN-IRT was used to conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. The evaluation results included 12 LLMs on 11 benchmarks, totaling 41,871 items.

## AAAI 2026 Publication

The work "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" by Zhou, Hongli and colleagues was published in the Proceedings of the AAAI Conference on Artificial Intelligence in 2026.

The search results also show related research on benchmark contamination in LLMs, though the specific connection to the PSN-IRT work regarding "adversarial" contamination wasn't explicitly detailed in these particular results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d61d956f-04e9-4410-b52a-0ff930989e83",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "70e39b91-df1d-4c43-bd24-271d69ce3425",
  "sourceToolAssistantUUID": "d61d956f-04e9-4410-b52a-0ff930989e83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T12:40:22.338Z_

<details><summary>↩ Tool result · `toolu_01JnEPMbaKhAhJKtAmpjheym`</summary>

```text
Web search results for query: ""Silicon Bureaucracy" "contamination sensitivity" "score confidence" LLM benchmarks 2026"

Links: [{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks | Request PDF","url":"https://www.researchgate.net/publication/403073188_Silicon_Bureaucracy_and_AI_Test-Oriented_Education_Contamination_Sensitivity_and_Score_Confidence_in_LLM_Benchmarks"},{"title":"[2603.21636] Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/abs/2603.21636"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education:","url":"https://arxiv.org/pdf/2603.21636"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/html/2603.21636v1"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"}]

I found relevant research on your query. Here are the results:

Public benchmarks increasingly govern how large language models (LLMs) are ranked, selected, and deployed. The benchmark-centered regime is framed as Silicon Bureaucracy and AI Test-Oriented Education, and it rests on a fragile assumption that benchmark scores directly reflect genuine generalization.

In practice, such scores may conflate exam-oriented competence with principled capability, especially when contamination and semantic leakage are difficult to exclude from modern training pipelines.

An audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks is proposed using a router-worker setup that compares a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream.

Across multiple models, widespread but heterogeneous above-baseline gains under noisy conditions indicate that benchmark-related cues may be reassembled and can reactivate contamination-related memory. These results suggest that similar benchmark scores may carry substantially different levels of confidence.

Rather than rejecting benchmarks altogether, the research argues that benchmark-based evaluation should be supplemented with explicit audits of contamination sensitivity and score confidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48dda7af-7cef-44e0-a946-a12d97e6abee",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "32aa47bb-4a63-4db6-b058-45d2f98aa95b",
  "sourceToolAssistantUUID": "48dda7af-7cef-44e0-a946-a12d97e6abee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T12:40:22.818Z_

<details><summary>↩ Tool result · `toolu_01USAQvBmkYPAp29iLnW1kYU`</summary>

```text
Web search results for query: "DCR "Data Contamination Rating" "contamination-aware" LLM accuracy adjustment 2026"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"}]

Based on the search results, I found comprehensive information about DCR and data contamination in LLMs:

## DCR Framework Overview

The Data Contamination Risk (DCR) framework is a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.

## Contamination-Aware Accuracy Adjustment

By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. The DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline.

## Problem Context

The rapid advancement of large language models (LLMs) has heightened concerns about benchmark data contamination (BDC), where models inadvertently memorize evaluation data during the training process, inflating performance metrics, and undermining genuine generalization assessment.

## Practical Significance

DCR provides a practical tool for integrating contamination assessment into routine evaluations, fostering fairer comparisons and enhancing the credibility of LLM benchmarking practices.

The research was published in 2025 at EMNLP and represents a recent advancement in addressing fairness and reliability in LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c14a17a4-0f25-4fe9-9034-21c9fe2354c1",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "48f40e57-fc33-4e17-a2fa-ba3d8e3f044d",
  "sourceToolAssistantUUID": "c14a17a4-0f25-4fe9-9034-21c9fe2354c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T12:40:22.991Z_

<details><summary>↩ Tool result · `toolu_01WdPg2b1zkSDpuGbwTPGryE`</summary>

```text
Web search results for query: ""Quantifying Data Contamination" "Psychometric Evaluations" LLMs Han Seoul 2025 2026 IRT"

Links: [{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/abs/2510.07175"},{"title":"Quantifying Data Contamination in Psychometric ...","url":"https://aclanthology.org/2026.findings-eacl.319.pdf"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.319/"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3475&show=50"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"}]

I found relevant research on your query! Here are the key results:

## Main Publication

"Quantifying Data Contamination in Psychometric Evaluations of LLMs" is a paper by Jongwook Han, Woojung Song, Jonggeun Lee, and Yohan Jo, published in Findings of the Association for Computational Linguistics: EACL 2026.

## Research Overview

The research applies psychometric questionnaires to Large Language Models (LLMs) to assess high-level psychological constructs such as values, personality, moral foundations, and dark traits. 

Although prior work raised concerns about possible data contamination from psychometric inventories which may threaten evaluation reliability, there had been no systematic attempt to quantify this contamination. The authors proposed a framework to systematically measure data contamination in psychometric evaluations, evaluating three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching.

## Key Findings

Applying this framework to 21 models from major families and four widely used psychometric inventories, they provided evidence that popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination, where models not only memorize items but can also adjust their responses to achieve specific target scores.

The paper appears to be available on arXiv (2510.07175) and through the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53e89a42-f8a4-431d-b506-b122decaea44",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "fc4b947f-7082-401a-831b-2dd22b4718f9",
  "sourceToolAssistantUUID": "53e89a42-f8a4-431d-b506-b122decaea44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-28T12:40:27.782Z_

Let me do a few more targeted searches to ensure thoroughness, specifically looking for the exact three-way intersection and any very recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc4b947f-7082-401a-831b-2dd22b4718f9",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUywppxwtUigDDzjuvZ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d06f8a-c6cb-48e2-b7cf-84d3e6f68c24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6epjtnfpBrAN2uGfiAYsp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 17849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 39 · 2026-05-28T12:40:28.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UPcxihioQpcXCZEAoCShti`</summary>

```json
{
  "query": "\"item response theory\" \"adversarial\" \"robustness\" LLM benchmark evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90d06f8a-c6cb-48e2-b7cf-84d3e6f68c24",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUywppxwtUigDDzjuvZ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91d355a1-3fe7-4e43-ab1c-719ee50cdaae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6epjtnfpBrAN2uGfiAYsp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 17849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 40 · 2026-05-28T12:40:29.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012vksYNriVtkfVgzenW7yeK`</summary>

```json
{
  "query": "\"Benchmark Health Index\" IRT contamination adversarial LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91d355a1-3fe7-4e43-ab1c-719ee50cdaae",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUywppxwtUigDDzjuvZ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "164bcb47-1a28-4c75-84e3-57772117d998",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6epjtnfpBrAN2uGfiAYsp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 17849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 41 · 2026-05-28T12:40:30.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xdfw6eYy7jKnwSKe8juAsw`</summary>

```json
{
  "query": "\"contamination-resistant\" \"item response theory\" OR \"IRT\" language model adversarial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "164bcb47-1a28-4c75-84e3-57772117d998",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUywppxwtUigDDzjuvZ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb248ce9-a88a-4229-9209-75dcbab59441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6epjtnfpBrAN2uGfiAYsp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 17849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 42 · 2026-05-28T12:40:36.316Z_

<details><summary>↩ Tool result · `toolu_01UPcxihioQpcXCZEAoCShti`</summary>

```text
Web search results for query: ""item response theory" "adversarial" "robustness" LLM benchmark evaluation 2025 2026"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Lifting the benchmark iceberg with item-response theory | OpenReview","url":"https://openreview.net/forum?id=ZyVQqK7mcP"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"}]

I found several highly relevant recent results combining item response theory with LLM evaluation. Here are the key findings:

## Recent Research on Item Response Theory and LLM Benchmarking

A recent paper proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. The research conducts extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

Another relevant 2025 study from ICLR reports a "benchmark iceberg" phenomenon where much of the variability in model rankings stems not from true capability differences, but from hidden implementation choices, and demonstrates how minor changes to these implementation details can alter model rankings.

## Item Response Theory and Adversarial Robustness

There is an urgent need for a more adversarial evaluation benchmark that can faithfully characterize the robustness of mathematical reasoning. A 2026 paper called RIDE (Difficulty Evolving Perturbation with Item Response Theory) applies adversarial perturbations guided by IRT to competition-level mathematical benchmarks, yielding perturbed versions that degrade advanced LLM performance, with experiments showing an average 21.73% drop across 26 models, thereby exposing limited robustness in mathematical reasoning.

These recent works demonstrate how item response theory is being applied to improve LLM benchmark evaluation and assess model robustness to adversarial variations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91d355a1-3fe7-4e43-ab1c-719ee50cdaae",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "3667fa7a-f480-46f1-9f51-ca5a8b35f9be",
  "sourceToolAssistantUUID": "91d355a1-3fe7-4e43-ab1c-719ee50cdaae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T12:40:36.618Z_

<details><summary>↩ Tool result · `toolu_01Xdfw6eYy7jKnwSKe8juAsw`</summary>

```text
Web search results for query: ""contamination-resistant" "item response theory" OR "IRT" language model adversarial"

Links: [{"title":"A Comparative Study of Item Response Theory Models for Mixed Discrete-Continuous Responses","url":"https://www.mdpi.com/2079-3200/12/3/26"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Item Response Theory for Natural Language Processing","url":"https://eacl2024irt.github.io/"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v1"},{"title":"Item Response Theory Overview","url":"https://www.emergentmind.com/topics/item-response-theory-irt"}]

The search results show several relevant works connecting Item Response Theory with language models and adversarial evaluation:

1. **RIDE Framework**: A novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical questions.

2. **PSN-IRT for LLM Benchmarking**: Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture for accurate and reliable estimations of item characteristics and model abilities. Notably, LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.

3. **IRT Applications in NLP**: Recently, there has been an uptick in work applying IRT to tasks in NLP.

4. **Robust IRT Methods**: Recent developments employ methods with Bayesian and Nonparametric approaches that yield robust, outlier-resistant inference for both person and item parameters.

The search results indicate that researchers are using IRT in conjunction with language models for adversarial evaluation and benchmark assessment, with particular attention to data quality and contamination issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb248ce9-a88a-4229-9209-75dcbab59441",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "255c5b41-d8ed-499f-9035-f66840a35eef",
  "sourceToolAssistantUUID": "fb248ce9-a88a-4229-9209-75dcbab59441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T12:40:37.112Z_

<details><summary>↩ Tool result · `toolu_012vksYNriVtkfVgzenW7yeK`</summary>

```text
Web search results for query: ""Benchmark Health Index" IRT contamination adversarial LLM 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs","url":"https://arxiv.org/pdf/2602.11674"},{"title":"LLM Benchmark Datasets Should Be Contamination-Resistant","url":"https://arxiv.org/html/2605.19999v1"},{"title":"Selective Adversarial Attacks on LLM Benchmarks","url":"https://arxiv.org/pdf/2510.13570"},{"title":"Published as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2602.06526"}]

I found relevant results for your search. Here's what I found:

## Benchmark Health Index (BHI)

The Benchmark Health Index (BHI) was published on February 9, 2026, and it's a comprehensive framework for evaluating benchmarks used in LLM research.

**What BHI Does:**
The BHI framework quantifies benchmark effectiveness and longevity along three dimensions: Capability Discrimination, Anti-Saturation, and Impact. The study conducted a systematic meta-analysis of 106 benchmarks extracted from technical reports of 91 representative LLMs released in 2025, distinguishing effective benchmarks that retain high discriminative power from those that have become obsolete.

**Relationship to Contamination and Adversarial Testing:**
The research community in 2026 is addressing multiple concerns related to benchmark integrity:

- Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

- Adversarial robustness testing checks whether a model's strong benchmark performance holds under rephrased or modified versions of the same questions, catching models that memorized specific phrasings rather than understanding underlying concepts.

The BHI framework appears to be part of broader efforts to establish more rigorous evaluation standards for LLM benchmarks in response to contamination concerns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "164bcb47-1a28-4c75-84e3-57772117d998",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "0aaa4fe5-1526-4310-8801-9901831725bf",
  "sourceToolAssistantUUID": "164bcb47-1a28-4c75-84e3-57772117d998",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-28T12:40:45.633Z_

Let me do one more round of targeted searches on the RIDE paper (which looks very relevant) and a couple more specific queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aaa4fe5-1526-4310-8801-9901831725bf",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyxsZhC6urZNYb7gyPM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f9cf8a3-45c1-4feb-9f36-34876e5ce5fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4DNDPC4ziufhyKfX1soAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 20985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 46 · 2026-05-28T12:40:46.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mod2Zfp8Rk4Gtv9DfdeYk5`</summary>

```json
{
  "query": "RIDE \"Difficulty Evolving Perturbation\" IRT mathematical reasoning adversarial contamination 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f9cf8a3-45c1-4feb-9f36-34876e5ce5fd",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyxsZhC6urZNYb7gyPM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e71bfcf-d7c0-49ec-914d-fbd3b8fa9b49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4DNDPC4ziufhyKfX1soAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 20985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 47 · 2026-05-28T12:40:47.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6uxvvVXQQnnkJ7x9AL9fZ`</summary>

```json
{
  "query": "\"inference-time decontamination\" IRT item response theory LLM benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e71bfcf-d7c0-49ec-914d-fbd3b8fa9b49",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyxsZhC6urZNYb7gyPM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dec3083-3177-4971-8a2d-d7735c6c08b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4DNDPC4ziufhyKfX1soAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 20985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 48 · 2026-05-28T12:40:47.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JXyCMerZWVZeAt4rthPifr`</summary>

```json
{
  "query": "\"LLM Benchmark Datasets Should Be Contamination-Resistant\" 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dec3083-3177-4971-8a2d-d7735c6c08b5",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyxsZhC6urZNYb7gyPM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8145493c-32b1-4dae-a1af-9823eb4b1488",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4DNDPC4ziufhyKfX1soAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 20985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 49 · 2026-05-28T12:40:53.611Z_

<details><summary>↩ Tool result · `toolu_01N6uxvvVXQQnnkJ7x9AL9fZ`</summary>

```text
Web search results for query: ""inference-time decontamination" IRT item response theory LLM benchmark"

Links: [{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"[2601.19334v1] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334v1"},{"title":"[2601.19334] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large   Language Model Evaluation","url":"https://arxiv.org/pdf/2406.13990"}]

Based on the search results, I found information about inference-time decontamination for LLMs, though I notice that your query includes "IRT item response theory" which doesn't appear directly in these results. Here's what the search revealed:

## Inference-Time Decontamination Framework

Test set contamination occurs when test samples or their close variants leak into training data and artificially inflate reported performance. To address this problem, researchers have proposed different approaches:

**DeconIEP**: DeconIEP is a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space, guided by a relatively less-contaminated reference model to steer models away from memorization-driven shortcut pathways. DeconIEP achieves strong decontamination effectiveness while incurring only minimal degradation in benign utility.

**Inference-Time Decontamination (ITD)**: ITD addresses this issue by detecting and rewriting leaked samples without altering their difficulties. ITD reduces inflated accuracy by 22.9% on GSM8K and 19.0% on MMLU.

The search results did not contain specific information about IRT (item response theory) applications in this context. If you're looking for research that specifically combines IRT with these decontamination methods, you might want to search more specifically for that combination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dec3083-3177-4971-8a2d-d7735c6c08b5",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "1b174062-42a6-4d61-ad4b-298de2a7acaf",
  "sourceToolAssistantUUID": "7dec3083-3177-4971-8a2d-d7735c6c08b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T12:40:53.749Z_

<details><summary>↩ Tool result · `toolu_01Mod2Zfp8Rk4Gtv9DfdeYk5`</summary>

```text
Web search results for query: "RIDE "Difficulty Evolving Perturbation" IRT mathematical reasoning adversarial contamination 2025 2026"

Links: [{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/html/2511.04120"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...","url":"https://openreview.net/pdf?id=PPkzchpdNK"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ITEM ...","url":"https://openreview.net/pdf/d5ed0f963c21d7ed1a8a3c452c9d81b161061351.pdf"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists","url":"https://arxiv.org/pdf/2511.07112"}]

Based on the search results, I found relevant information about RIDE:

RIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical questions.

The research addresses a critical problem: strong performance in mathematical reasoning may result from data contamination during pretraining that leads to memorization-based answers, or from the model relying primarily on superficial pattern matching without understanding mathematical knowledge.

**How RIDE Works:**

The method constructs a difficulty ranker for math questions using IRT-based difficulty estimation with LLMs acting as students, and this ranker serves as a reward model by providing difficulty reward signals, which are used to guide reinforcement learning on existing high-difficulty datasets.

The approach employs 35 LLMs to simulate students and build a difficulty ranker from their responses, which provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions across difficulty levels.

**Results:**

Applying RIDE to competition-level mathematical benchmarks yields perturbed versions that degrade advanced LLM performance, with experiments showing an average 21.73% drop across 26 models.

The paper appears to have been published in early 2026 based on the metadata from the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e71bfcf-d7c0-49ec-914d-fbd3b8fa9b49",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "e2d89a1c-ad92-4436-9652-bb6390278a81",
  "sourceToolAssistantUUID": "5e71bfcf-d7c0-49ec-914d-fbd3b8fa9b49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-28T12:40:55.899Z_

<details><summary>↩ Tool result · `toolu_01JXyCMerZWVZeAt4rthPifr`</summary>

```text
Web search results for query: ""LLM Benchmark Datasets Should Be Contamination-Resistant" 2026 arxiv"

Links: [{"title":"Towards Contamination Resistant Benchmarks","url":"https://arxiv.org/pdf/2505.08389"},{"title":"LLM Benchmark Datasets Should Be Contamination-Resistant","url":"https://arxiv.org/html/2605.19999v1"},{"title":"Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v1"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation","url":"https://arxiv.org/pdf/2502.17521"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge","url":"https://arxiv.org/pdf/2412.13670"}]

I found relevant papers on this topic. Here are the search results:

## Key Papers Found:

1. **"LLM Benchmark Datasets Should Be Contamination-Resistant"** - This paper evaluates how well contamination resistance definitions are realized through different methods, and notes that inversion attacks can recover input information directly from KV cache representations.

2. **"Towards Contamination Resistant Benchmarks"** - This work contributes to the development of contamination resistant benchmarks, enabling more rigorous LLM evaluation and offering insights into the true capabilities and limitations of LLMs. A key strategy to address contamination is to create a dynamic benchmark that receives continuous updates, with new test instances added after a model's training cutoff.

3. **"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation"** - Data contamination occurs when benchmark data is inadvertently included in the training phase of language models, leading to an inflated and misleading assessment of their performance.

The search results show an active research area focused on ensuring LLM benchmarks are resistant to data contamination through both static methods like encryption and dynamic approaches with continuously updated benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8145493c-32b1-4dae-a1af-9823eb4b1488",
  "isSidechain": true,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "agentId": "af89ed972f0b00e1c",
  "type": "user",
  "uuid": "3b7684b4-a0e8-4883-8c02-56f375455b91",
  "sourceToolAssistantUUID": "8145493c-32b1-4dae-a1af-9823eb4b1488",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-28T12:42:11.839Z_

Now I have comprehensive results from all searches. Here is my full analysis.

---

## Adversarial Literature Search Report: CRADE (IRT + Contamination Detection + Adversarial Robustness)

I conducted 10 specified searches plus 7 follow-up targeted searches. Below are the findings organized by search query, followed by an overall competitive threat assessment.

---

### Search 1: "contamination-aware IRT" OR "contamination item response theory" LLM 2025 2026

**Found:** No paper uses the exact phrase "contamination-aware IRT." However, several papers apply IRT to LLM benchmarking:
- **PSN-IRT** (Zhou et al., AAAI 2026 Oral) -- uses IRT to audit benchmark quality and explicitly flags contaminated items as a quality problem. Does NOT model contamination as a latent variable or correct for it within the IRT framework.
- **IRT-Router** (Song et al., ACL 2025) -- uses IRT for LLM routing, no contamination angle.
- **Diagnosing LLM-as-a-Judge via IRT** (2026) -- applies IRT-GRM to judge reliability, no contamination.

**Three-way intersection?** No. PSN-IRT is closest (IRT + contamination awareness) but has no adversarial robustness component.

---

### Search 2: "benchmark contamination correction" "item response theory" 2026

**Found:** PSN-IRT again dominates. It identifies contaminated items and removes them to create cleaner benchmarks, but does not perform contamination *correction* within the IRT model itself (e.g., jointly estimating ability and contamination parameters). No adversarial component.

**Three-way intersection?** No.

---

### Search 3: "decontamination" "IRT" "large language model" 2026

**Found:** Two separate threads that do NOT intersect:
- **Inference-Time Decontamination (ITD)** and **DeconIEP** -- decontamination methods that operate at inference time by rewriting or perturbing leaked samples. No IRT component.
- **PSN-IRT** -- IRT-based benchmark analysis. No decontamination mechanism.

**Three-way intersection?** No.

---

### Search 4: "gated IRT" language model

**Found:** Only results for gated recurrent/convolutional language models from 2016-2019. No paper proposes a "gated IRT" model where a contamination gate modulates item parameters. This specific architectural idea appears novel.

**Three-way intersection?** No results at all.

---

### Search 5: site:arxiv.org "contamination" "adversarial" "IRT" LLM evaluation 2026

**Found:** No single paper addressing all three terms together. The results split into:
- Contamination detection surveys (Min-K%, ConStat, canary GUIDs)
- Adversarial evaluation (perturbation-based)
- IRT for benchmarking (PSN-IRT)

A critical find here: **"LLM Benchmark Datasets Should Be Contamination-Resistant"** (arxiv 2605.19999, May 2026) -- very recent, evaluates contamination resistance methods. No IRT component.

**Three-way intersection?** No.

---

### Search 6: site:openreview.net contamination IRT LLM evaluation 2026

**Found:** Multiple contamination-focused papers at ICLR 2026 and in review:
- **Auditing Test Data Contamination with Error Rate Control** (ICLR 2026)
- **The Emperor's New Clothes in Benchmarking** -- tests 20 mitigation strategies and finds none effectively balances fidelity and contamination resistance
- **Detecting Benchmark Contamination Through Watermarking**
- **Knowledge Distillation as Decontamination** (ICLR 2026)
- **LiveBench** -- contamination-limited benchmark

None of these use IRT. None combine IRT with contamination or adversarial robustness.

**Three-way intersection?** No.

---

### Search 7: "joint contamination ability" OR "contamination-adjusted scoring" LLM 2026

**Found:** The closest competitor in the contamination-adjustment space:
- **DCR: Data Contamination Rating** (EMNLP 2025) -- uses a fuzzy inference system to produce a contamination factor that adjusts raw accuracy. Validated on 9 LLMs. This is a contamination-adjusted scoring system, but it does NOT use IRT. It uses heuristic fuzzy logic, not psychometric measurement theory. No adversarial component.
- **"Silicon Bureaucracy and AI Test-Oriented Education"** (arxiv 2603.21636, March 2026) -- proposes an audit framework that compares clean vs. noisy conditions (where benchmark problems are deleted, rewritten, perturbed). This has contamination sensitivity + adversarial perturbation but NO IRT.

**Three-way intersection?** No, but these are the two most relevant partial competitors:
- DCR covers contamination-adjusted scoring (without IRT)
- Silicon Bureaucracy covers contamination + adversarial perturbation (without IRT)

---

### Search 8: "benchmark integrity" "measurement theory" LLM 2025 2026

**Found:**
- **Benchmark Health Index (BHI)** (Feb 2026) -- meta-analyzes 106 benchmarks across discrimination, saturation, and impact. Uses measurement concepts but NOT formal IRT. No contamination correction or adversarial robustness.
- **Quantifying Construct Validity in LLM Evaluations** (Feb 2026) -- applies validity theory to LLM benchmarks. Addresses measurement rigor but not contamination or adversarial robustness.

**Three-way intersection?** No.

---

### Search 9: "paired item" contamination LLM evaluation

**Found:**
- **PaCoST (Paired Confidence Significance Testing)** -- constructs paired counterparts to detect benchmark contamination via statistical confidence analysis. This is a contamination detection method using paired items but has NO IRT and NO adversarial robustness component.
- **"Quantifying Data Contamination in Psychometric Evaluations of LLMs"** (Han et al., EACL 2026 Findings) -- measures memorization and contamination in psychometric inventories (BFI-44, PVQ-40). Uses psychometric instruments but NOT IRT for ability estimation. Focuses on personality/values questionnaires, not capability benchmarks. No adversarial component.

**Three-way intersection?** No.

---

### Search 10: site:arxiv.org "psychometric" "contamination" "language model" 2026

**Found:** The Han et al. EACL 2026 paper again. This is the closest to combining psychometrics with contamination, but it studies contamination OF psychometric tests (whether LLMs have memorized personality questionnaires), not contamination-aware psychometric scoring of LLM ability. No IRT model is used; no adversarial component.

**Three-way intersection?** No.

---

### Follow-up: RIDE (IRT + Adversarial, most relevant partial overlap)

**RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning** (late 2025 / early 2026, OpenReview)

This is a significant find. RIDE uses IRT to measure question difficulty, then uses IRT-derived difficulty as a reward signal to train an adversarial question rewriter via reinforcement learning. It explicitly notes that strong benchmark performance may stem from contamination/memorization, and generates adversarial variants to test robustness. Average performance drops 21.73% across 26 models.

**RIDE covers two of the three legs: IRT + adversarial perturbation.** It mentions contamination as a motivation but does NOT model contamination as a latent variable, does NOT jointly estimate contamination and ability, and does NOT propose contamination-aware IRT parameters. It is an adversarial benchmark construction tool, not a contamination-correcting measurement framework.

---

## Overall Assessment

### Papers occupying partial intersections (ranked by threat level):

| Paper | IRT | Contamination | Adversarial | Threat to CRADE |
|-------|-----|---------------|-------------|-----------------|
| **RIDE** (2025-2026) | Yes (difficulty estimation) | Motivation only | Yes (adversarial rewriting) | **MODERATE** -- covers IRT + adversarial but not contamination modeling |
| **PSN-IRT** (AAAI 2026 Oral) | Yes (full IRT framework) | Identifies contaminated items | No | **MODERATE** -- covers IRT + contamination detection but not adversarial |
| **Silicon Bureaucracy** (Mar 2026) | No | Yes (sensitivity auditing) | Yes (perturbation-based) | **LOW-MODERATE** -- covers contamination + adversarial without IRT |
| **DCR** (EMNLP 2025) | No | Yes (contamination-adjusted scoring) | No | **LOW** -- contamination correction without IRT |
| **Han et al.** (EACL 2026) | No (psychometric but not IRT) | Yes (psychometric contamination) | No | **LOW** -- different domain (personality, not capability) |
| **BHI** (Feb 2026) | No (measurement-inspired but not IRT) | No | No | **NEGLIGIBLE** |

### Key Conclusion

**No paper was found that occupies the three-way intersection of IRT + contamination detection/correction + adversarial robustness.** The CRADE proposal's claim of novelty at this intersection appears to hold as of late May 2026.

However, the authors should be aware of and cite these partial competitors:

1. **RIDE** is the most dangerous near-miss -- it uses IRT-guided adversarial perturbation and is motivated by contamination concerns. A reviewer could argue RIDE is "close enough." CRADE must clearly differentiate by emphasizing its contamination-as-latent-variable modeling within IRT, which RIDE entirely lacks.

2. **PSN-IRT** (AAAI 2026 Oral) is a high-visibility paper that uses IRT and explicitly addresses contamination in benchmarks. CRADE must differentiate by showing that PSN-IRT only *detects and removes* contaminated items rather than *correcting for contamination within the model*.

3. **Silicon Bureaucracy** (March 2026) combines contamination auditing with adversarial perturbation. It lacks IRT but is conceptually adjacent. The CRADE authors should cite it.

4. **DCR** provides contamination-adjusted scoring, which is conceptually similar to what CRADE presumably does, but uses fuzzy logic rather than IRT. CRADE should position itself as the principled psychometric alternative.

---

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://arxiv.org/abs/2505.15055)
- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [IRT-Router (ACL 2025)](https://arxiv.org/abs/2506.01048)
- [Diagnosing LLM-as-a-Judge via IRT (2026)](https://arxiv.org/pdf/2602.00521)
- [RIDE: Difficulty Evolving Perturbation with IRT](https://arxiv.org/pdf/2511.04120)
- [Silicon Bureaucracy and AI Test-Oriented Education (2026)](https://arxiv.org/abs/2603.21636)
- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://arxiv.org/abs/2507.11405)
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026)](https://arxiv.org/abs/2510.07175)
- [Benchmark Health Index (2026)](https://arxiv.org/pdf/2602.11674)
- [LLM Benchmark Datasets Should Be Contamination-Resistant (May 2026)](https://arxiv.org/html/2605.19999v1)
- [When Benchmarks Leak: Inference-Time Decontamination (2026)](https://arxiv.org/abs/2601.19334)
- [The Emperor's New Clothes in Benchmarking (OpenReview)](https://openreview.net/forum?id=TuvDxubEfE)
- [Auditing Test Data Contamination with Error Rate Control (OpenReview)](https://openreview.net/forum?id=YsoabhpS7z)
- [Detecting Benchmark Contamination Through Watermarking (OpenReview)](https://openreview.net/forum?id=WFGxFzFDmQ)
- [LiveBench (OpenReview)](https://openreview.net/forum?id=sKYHBTAxVa)
- [Towards Contamination Resistant Benchmarks](https://arxiv.org/pdf/2505.08389)
- [Quantifying Construct Validity in LLM Evaluations](https://arxiv.org/pdf/2602.15532)
- [Lifting the Benchmark Iceberg with IRT (OpenReview)](https://openreview.net/forum?id=ZyVQqK7mcP)
- [Knowledge Distillation as Decontamination (ICLR 2026)](https://openreview.net/pdf?id=W8VCH9x1HZ)
- [A Survey on Data Contamination for LLMs](https://arxiv.org/html/2502.14425v2)
- [Benchmarking LLMs Under Data Contamination: Static to Dynamic Evaluation](https://arxiv.org/html/2502.17521v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b7684b4-a0e8-4883-8c02-56f375455b91",
  "isSidechain": true,
  "agentId": "af89ed972f0b00e1c",
  "requestId": "req_011CbUyzFVLdGqCg87KGzF2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e60954e3-bb42-44ff-8ade-c80cc038e1dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018K4cXQyhZW8LuyMCp97J6r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2778,
      "cache_read_input_tokens": 22500,
      "output_tokens": 3392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2778
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3392,
          "cache_read_input_tokens": 22500,
          "cache_creation_input_tokens": 2778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2778,
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
