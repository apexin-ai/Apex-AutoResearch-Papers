# Research conversation: You are helping with a literature survey on robust conformal prediction, especially under data poisoning and distributio

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-adbfc87c1aba5efc3.jsonl`
- **Structured JSON:** [`19574bb0d2a6d2104f86.json`](../../sessions/19/19574bb0d2a6d2104f86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

78 recorded events

### User

_source line 1 · 2026-05-30T06:13:42.321Z_

You are helping with a literature survey on robust conformal prediction, especially under data poisoning and distribution shift. Execute these searches and for each promising paper, fetch its arXiv abstract.

Search queries to run:
1. "robust conformal prediction poisoning 2024 2025 2026"
2. "conformal prediction distribution shift 2024 2025 2026"
3. "conformal prediction adversarial robustness 2024 2025"
4. "Provably Reliable Conformal Prediction Sets Data Poisoning" (find citing papers)
5. "conformal prediction exchangeability violation 2024 2025 2026"

For each paper found, fetch its arXiv page and extract: title, authors, venue, year, and a one-line summary. Focus on papers from 2024-2026 that deal with making conformal prediction robust to various threats.

Return a structured list of all papers found with title, authors, venue, URL, and one-line summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "728d8e38-8d7f-41ed-aa56-fce4ff5c4823",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:13:42.324Z_

```json
{
  "parentUuid": "728d8e38-8d7f-41ed-aa56-fce4ff5c4823",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
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
  "uuid": "d664be6f-6b1b-4268-bc6c-a338b3fe01f8",
  "timestamp": "2026-05-30T06:13:42.324Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:13:42.325Z_

```json
{
  "parentUuid": "d664be6f-6b1b-4268-bc6c-a338b3fe01f8",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "feec3eb1-c80b-48ea-9216-9bb948f0a8a3",
  "timestamp": "2026-05-30T06:13:42.325Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:13:45.330Z_



I'll execute all five search queries in parallel to find relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feec3eb1-c80b-48ea-9216-9bb948f0a8a3",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5SCXndhistaDUCdu8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4e09dbc-3dc0-429c-908e-01af735cb290",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWxEBJiYDcT8GubpHcSyJx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 5 · 2026-05-30T06:13:45.895Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XMNWax5qgVkjuGbPfMM24D`</summary>

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
  "parentUuid": "b4e09dbc-3dc0-429c-908e-01af735cb290",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5SCXndhistaDUCdu8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "949c6208-5ddf-4ea8-a0cb-9f73adedb9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWxEBJiYDcT8GubpHcSyJx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 7413,
      "output_tokens": 95,
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
          "output_tokens": 95,
          "cache_read_input_tokens": 7413,
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

_source line 6 · 2026-05-30T06:13:45.898Z_

<details><summary>↩ Tool result · `toolu_01XMNWax5qgVkjuGbPfMM24D`</summary>

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
  "parentUuid": "949c6208-5ddf-4ea8-a0cb-9f73adedb9f1",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "f8b77d43-1319-4a65-a90e-8246603ee617",
  "sourceToolAssistantUUID": "949c6208-5ddf-4ea8-a0cb-9f73adedb9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:13:49.085Z_



Now let me run all five search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b77d43-1319-4a65-a90e-8246603ee617",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5hjvJqw1a6AuFhQvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b43dc728-b2fe-4ec2-8175-6a7d864328bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj7a7THYLCzNT1tr4cHZcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 8 · 2026-05-30T06:13:49.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015W2vV6rWd7Gp6hYhUR2Uhw`</summary>

```json
{
  "query": "robust conformal prediction poisoning 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b43dc728-b2fe-4ec2-8175-6a7d864328bd",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5hjvJqw1a6AuFhQvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69d05c4b-6d07-4f46-9cd8-5513bc3c1dfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj7a7THYLCzNT1tr4cHZcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 9 · 2026-05-30T06:13:49.993Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NySAcbaxBUmRN4rN1FMvJQ`</summary>

```json
{
  "query": "conformal prediction distribution shift 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d05c4b-6d07-4f46-9cd8-5513bc3c1dfe",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5hjvJqw1a6AuFhQvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c82d98cb-f41b-4a22-b1e5-39e6ea9b8afc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj7a7THYLCzNT1tr4cHZcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 10 · 2026-05-30T06:13:50.539Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U6jS1pNuWgzzMfFRCfn8XB`</summary>

```json
{
  "query": "conformal prediction adversarial robustness 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c82d98cb-f41b-4a22-b1e5-39e6ea9b8afc",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5hjvJqw1a6AuFhQvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31b24b4c-ba8d-4e18-b7d1-89fdde7896e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj7a7THYLCzNT1tr4cHZcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 11 · 2026-05-30T06:13:51.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RR1CfPuvPSSini9LizGSHM`</summary>

```json
{
  "query": "\"Provably Reliable Conformal Prediction Sets\" \"Data Poisoning\" citing papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31b24b4c-ba8d-4e18-b7d1-89fdde7896e3",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5hjvJqw1a6AuFhQvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88bcac86-dbd6-4772-a821-4e6a781c7012",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj7a7THYLCzNT1tr4cHZcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 12 · 2026-05-30T06:13:51.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N5y3KxaJg2VEnAxb2QZ9U5`</summary>

```json
{
  "query": "conformal prediction exchangeability violation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88bcac86-dbd6-4772-a821-4e6a781c7012",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG5hjvJqw1a6AuFhQvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d9edd66-99de-42d4-857a-0debafbb5f02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj7a7THYLCzNT1tr4cHZcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 13 · 2026-05-30T06:13:56.164Z_

<details><summary>↩ Tool result · `toolu_01RR1CfPuvPSSini9LizGSHM`</summary>

```text
Web search results for query: ""Provably Reliable Conformal Prediction Sets" "Data Poisoning" citing papers"

Links: [{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"}]

Based on the search results, here is the paper I found:

## Primary Paper

"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" by Yan Scholten and Stephan Günnemann was accepted at ICLR 2025 as a Spotlight paper.

### Key Contributions

The paper addresses how conformal prediction, which provides model-agnostic and distribution-free uncertainty quantification, is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, and proposes reliable prediction sets (RPS) as the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning.

### Methodology

To ensure reliability under training poisoning, the authors introduce smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data. For calibration poisoning, they construct multiple prediction sets each calibrated on distinct subsets of the calibration data, then aggregate them into a majority prediction set that includes a class only if it appears in a majority of the individual sets.

The paper is available on arXiv (2410.09878) and the authors have provided a GitHub implementation of the reliable conformal prediction sets approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88bcac86-dbd6-4772-a821-4e6a781c7012",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "ccfbeeef-6389-47a9-8e28-eb886c9015c1",
  "sourceToolAssistantUUID": "88bcac86-dbd6-4772-a821-4e6a781c7012",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-30T06:13:57.420Z_

<details><summary>↩ Tool result · `toolu_01U6jS1pNuWgzzMfFRCfn8XB`</summary>

```text
Web search results for query: "conformal prediction adversarial robustness 2024 2025"

Links: [{"title":"Adversarially Robust Conformal Prediction","url":"https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://proceedings.mlr.press/v267/bao25a.html"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/html/2511.18562"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"}]

Based on the search results, here's what's current in the field of conformal prediction and adversarial robustness:

## Recent Developments (2024-2025)

Recent approaches including probabilistic, two-quantile, and smoothing-based methods (aPRCP, CAS, RCP1, BinCP) offer set-size reductions of 2x–10x compared to prior robust conformal prediction methods, with negligible empirical coverage loss.

Training-time defenses (OPSA-AT, uncertainty-reducing AT) outperform PGD, TRADES, and vanilla adversarial training on set efficiency under calibration and test-time attacks.

## Key Applications and Frameworks

Recent research advances adversarial training by leveraging conformal prediction principles, developing methods like OPSA (OPtimal Size Attack) designed to reduce the efficiency of conformal prediction at any significance level by maximizing model uncertainty.

Reasoning-enhanced frameworks (COLEP) further tighten coverage and reduce set size via logical correction and exact marginalization using probabilistic circuits.

## Broader Context

Conformal Prediction has emerged as a promising paradigm distinguished by its distribution-free properties and robust uncertainty quantification capabilities, excelling in both regression and classification tasks by providing statistically rigorous confidence intervals and well-calibrated probability estimates.

Through the implementation of defensive mechanisms, conformal prediction substantially enhances model robustness against adversarial perturbations, highlighting its significant potential for deployment in safety-critical applications such as autonomous driving and medical diagnosis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31b24b4c-ba8d-4e18-b7d1-89fdde7896e3",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "78648d31-c61b-4c75-9ee2-1c63ac57903a",
  "sourceToolAssistantUUID": "31b24b4c-ba8d-4e18-b7d1-89fdde7896e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-30T06:13:57.641Z_

<details><summary>↩ Tool result · `toolu_01NySAcbaxBUmRN4rN1FMvJQ`</summary>

```text
Web search results for query: "conformal prediction distribution shift 2024 2025 2026"

Links: [{"title":"Conformal Prediction for Time-series Forecasting with Change Points","url":"https://arxiv.org/html/2509.02844v3"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Conformal Regression under Distribution Shift: A Reinforcement Learning Method for Adaptive Uncertainty Quantification | OpenReview","url":"https://openreview.net/forum?id=7puF5JOkKk"},{"title":"Conformal Inference under High-Dimensional Covariate Shifts via Likelihood-Ratio Regularization","url":"https://arxiv.org/html/2502.13030v5"},{"title":"Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift","url":"https://arxiv.org/pdf/2511.04275"},{"title":"Empirically Validating Conformal Prediction on Modern Vision   Architectures Under Distribution Shift and Long-tailed Data","url":"https://arxiv.org/pdf/2307.01088"}]

Based on the web search results, here are the key findings about conformal prediction and distribution shift research from 2024-2026:

## Recent Research on Conformal Prediction under Distribution Shift

**Theoretical and Methodological Advances:**

Recent work has focused on conformal inference for online prediction with arbitrary distribution shifts, published in the Journal of Machine Learning Research in 2024. A key research direction involves identifying approaches that yield the tightest worst-case conformal prediction sets while preserving the desired coverage under distribution shift.

**Addressing Time-Series and Temporal Challenges:**

In time-series settings, the exchangeability assumption underlying conformal prediction is often violated due to temporal dependencies, which recent adaptive conformal prediction methods address by dynamically calibrating intervals based on recent residuals and adaptive weighting strategies.

A 2025 approach proposes online conformal inference with retrospective adjustment, designed to achieve faster adaptation to distributional shifts. Existing methods typically adapt slowly to distribution shifts because they update predictions only in a forward manner.

**High-Dimensional Covariate Shifts:**

Several methods have been proposed to adapt conformal prediction to covariate shift, with approaches published between 2019 and 2024.

**Practical Challenges:**

Performance of conformal prediction methods degrades across neural architectures when tested on distribution-shifted datasets, with target coverage consistently violated and average confidence set size increasing under distribution shift.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c82d98cb-f41b-4a22-b1e5-39e6ea9b8afc",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "4868750b-1818-46e8-acc4-9161dc11690d",
  "sourceToolAssistantUUID": "c82d98cb-f41b-4a22-b1e5-39e6ea9b8afc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-30T06:13:59.012Z_

<details><summary>↩ Tool result · `toolu_015W2vV6rWd7Gp6hYhUR2Uhw`</summary>

```text
Web search results for query: "robust conformal prediction poisoning 2024 2025 2026"

Links: [{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Adversarially Robust Conformal Prediction","url":"https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"},{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"Verifiably Robust Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=5pJfDlaSxV"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"}]

Based on the search results, here's what I found on robust conformal prediction and poisoning attacks from 2024-2026:

## Key Research Areas

**Poisoning Attacks on Conformal Prediction:**
Recent work proposes methods to improve the reliability of conformal prediction under worst-case training and calibration poisoning. Data poisoning occurs when adversaries modify the training or calibration data (e.g., during data labeling) and can significantly alter the prediction sets, resulting in overly conservative or empty sets.

**Defense Methods:**

1. Multi-split conformal prediction is one approach, and to ensure reliability under calibration poisoning, researchers construct multiple prediction sets, each calibrated on distinct subsets of the calibration data.

2. VRCP (Verifiably Robust Conformal Prediction) is a framework that leverages neural network verification methods to recover coverage guarantees under adversarial attacks, and can be used to mitigate poisoning attacks. VRCP is also automatically robust to feature poisoning attacks.

3. Zargarbashi et al. (2024) derive robust prediction sets by bounding worst-case changes in conformity scores for adversarial evasion and poisoning attacks, using CDF-based bounds to compute conservative prediction sets.

**Robustness Frameworks:**
Beta-weighted and entropy-minimized adversarial training (AT-UR, TRADES-UR, MART-UR) further reduce the population prediction set size while maintaining nominal coverage.

The research shows significant progress in developing theoretically guaranteed robust conformal prediction methods that handle data poisoning attacks from 2024 onwards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69d05c4b-6d07-4f46-9cd8-5513bc3c1dfe",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "3cc78548-0fbf-4b2c-9b9e-c6d5f3baa17a",
  "sourceToolAssistantUUID": "69d05c4b-6d07-4f46-9cd8-5513bc3c1dfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:13:59.405Z_

<details><summary>↩ Tool result · `toolu_01N5y3KxaJg2VEnAxb2QZ9U5`</summary>

```text
Web search results for query: "conformal prediction exchangeability violation 2024 2025 2026"

Links: [{"title":"Conformal prediction beyond exchangeability","url":"https://www.researchgate.net/publication/371558117_Conformal_prediction_beyond_exchangeability"},{"title":"Conformal prediction beyond exchangeability","url":"https://arxiv.org/pdf/2202.13415"},{"title":"Conformal prediction beyond exchangeability","url":"https://projecteuclid.org/journals/annals-of-statistics/volume-51/issue-2/Conformal-prediction-beyond-exchangeability/10.1214/23-AOS2276.pdf"},{"title":"Federated Conformal Approach for Trustworthy ... - Authorea","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/302644/preprint_pdf/f1cf7a8a7efeed3a23ba7595624aaac6.pdf"},{"title":"Conformal Prediction Beyond Exchangeability","url":"https://arxiv.org/html/2202.13415v5"},{"title":"conformal-predictions-from-scratch/notebooks/regression/4-Conformal-Prediction-Beyond-Exchangeability.ipynb at main · joneswack/conformal-predictions-from-scratch","url":"https://github.com/joneswack/conformal-predictions-from-scratch/blob/main/notebooks/regression/4-Conformal-Prediction-Beyond-Exchangeability.ipynb"},{"title":"Predictive inference for time series: why is split conformal effective despite temporal dependence?","url":"https://arxiv.org/pdf/2510.02471"},{"title":"Conformal Prediction Beyond Exchangeability","url":"https://www.stat.cmu.edu/~ryantibs/papers/nexcp.pdf"},{"title":"Online Conformal Prediction: Enforcing monotonicity via Online Optimization","url":"https://arxiv.org/html/2605.12668"}]

Based on the search results, here's what recent research shows about conformal prediction and exchangeability violations:

## Key Findings

Exchangeability is often violated when predictive models are deployed in practice. For example, if the data distribution drifts over time, then the data points are no longer exchangeable; moreover, in such settings, we might want to use an algorithm that treats recent observations as more relevant, which would violate the assumption that data points are treated symmetrically.

## Recent Research (2023-2026)

Recent work clarifies what guarantees remain when exchangeability is violated. A significant contribution in this area is the work by Barber et al. (2023), titled "Conformal prediction beyond exchangeability," which demonstrates how to quantify the loss of coverage due to violations of exchangeability, and how to modify the conformal prediction methodology to regain predictive coverage even in the presence of distribution drift or other violations of exchangeability.

## Application Areas

Recent research has extended this work to specific domains:

- In graph-structured time series, inherent cross-node coupling can violate the exchangeability condition, making direct application of CP unreliable.

- Conformal prediction provides statistically rigorous uncertainty quantification but relies on the exchangeability assumption, which is violated in federated prognostics due to cross-fleet heterogeneity and within-unit degradation or progression patterns.

- Time series data clearly violate exchangeability assumptions, and a significant body of work has aimed to develop variants of conformal prediction methods that are adapted for the time series setting.

- Recent work has extended conformal prediction to the online setting without relying on exchangeability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d9edd66-99de-42d4-857a-0debafbb5f02",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "1ba23620-a28b-49b4-82ee-68b8aff1a526",
  "sourceToolAssistantUUID": "1d9edd66-99de-42d4-857a-0debafbb5f02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-30T06:14:03.935Z_

Good, I have a solid set of results. Now let me fetch the arXiv abstracts for all the promising papers I've identified. I'll fetch them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ba23620-a28b-49b4-82ee-68b8aff1a526",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b38a6525-4c5d-4d1f-9b7a-e080768bfee0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 19 · 2026-05-30T06:14:05.352Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014M7xYMMNMu1R1AJtjCttQZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.09878",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b38a6525-4c5d-4d1f-9b7a-e080768bfee0",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b649ea8-947b-4067-a718-c230331db3b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 20 · 2026-05-30T06:14:06.310Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EZLEER7RhEbLtDgTzN1hDD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.09165",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b649ea8-947b-4067-a718-c230331db3b8",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47d29530-9396-4713-8328-98c4a0950ee0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 21 · 2026-05-30T06:14:06.713Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Wm7ieqL6dMk4d6JvKtqBt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.14105",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d29530-9396-4713-8328-98c4a0950ee0",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e1e549a-4b04-418b-b6b8-cb607f683b47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 22 · 2026-05-30T06:14:07.719Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018BnLSJTgsMSDaBML2bJqUh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.13030",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e1e549a-4b04-418b-b6b8-cb607f683b47",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7405bc08-804f-4971-8f4f-0a332947f994",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 23 · 2026-05-30T06:14:09.339Z_

<details><summary>↩ Tool result · `toolu_014M7xYMMNMu1R1AJtjCttQZ`</summary>

```text
# Paper Extraction

**Title:** Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning

**Authors:** Yan Scholten, Stephan Günnemann

**Year:** 2024 (submitted October 13, 2024; accepted at ICLR 2025)

**Venue:** ICLR 2025 (Spotlight)

**Abstract:**

The paper addresses vulnerability in conformal prediction methods when training and calibration data are compromised through poisoning attacks. The authors introduce reliable prediction sets (RPS), which employs two key mechanisms: smoothed score functions that aggregate predictions from classifiers trained on distinct data partitions to handle training poisoning, and multiple calibrated prediction sets aggregated via majority voting to address calibration poisoning. This dual aggregation strategy reduces the influence of individual corrupted datapoints. The approach achieves "strong reliability while maintaining utility and preserving coverage on clean data," representing "an important step towards more trustworthy uncertainty quantification in the presence of data poisoning."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b649ea8-947b-4067-a718-c230331db3b8",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "9863446e-3923-4123-b564-498c4683ee9e",
  "sourceToolAssistantUUID": "8b649ea8-947b-4067-a718-c230331db3b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-30T06:14:09.565Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ltnnn8FPioViKkLZV6xMxi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.04275",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9863446e-3923-4123-b564-498c4683ee9e",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d9d0240-3fea-43e8-8c51-323cc007a285",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 25 · 2026-05-30T06:14:09.687Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015QTTvCGXQ1QgXwMWfzZnPv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.07804",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d9d0240-3fea-43e8-8c51-323cc007a285",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db70cdb0-8328-4bc8-aa61-85380a4eddf8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 26 · 2026-05-30T06:14:09.835Z_

<details><summary>↩ Tool result · `toolu_01EZLEER7RhEbLtDgTzN1hDD`</summary>

```text
# Paper Information

**Title:** "Robust Yet Efficient Conformal Prediction Sets"

**Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski

**Year:** 2024

**Venue:** Proceedings of the 41st International Conference on Machine Learning

**Abstract:**

The paper addresses vulnerabilities in conformal prediction methods by developing provably robust prediction sets. The authors derive bounds on worst-case changes in conformity scores to create sets that "include the true label with any user-specified probability." Their approach handles both continuous and discrete data types, with guarantees covering evasion attacks on test examples and poisoning attacks affecting calibration data (features and labels). The tighter bounds they establish enable more efficient prediction sets compared to existing methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47d29530-9396-4713-8328-98c4a0950ee0",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "77c54486-53e1-4ea4-b31f-7c9ba4c52419",
  "sourceToolAssistantUUID": "47d29530-9396-4713-8328-98c4a0950ee0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-30T06:14:10.180Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YTr4k6CeoHHEi15Myi6PAH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18562",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77c54486-53e1-4ea4-b31f-7c9ba4c52419",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45f3afc5-79b7-4ea8-9c27-04c1b32b2203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 28 · 2026-05-30T06:14:10.979Z_

<details><summary>↩ Tool result · `toolu_014Wm7ieqL6dMk4d6JvKtqBt`</summary>

```text
# Paper Summary

**Title:** "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations"

**Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk

**Year:** 2025 (submitted February 19, 2025; revised May 19, 2025)

**Venue:** arXiv (stat.ML category)

**Abstract:**

The paper addresses robustness challenges in conformal prediction when facing distribution shifts. The authors model these shifts using Levy-Prokhorov ambiguity sets to handle "both local and global perturbations." Their key contribution involves establishing connections between conformal prediction and these ambiguity sets. By "propagating the LP ambiguity set through the scoring function," they convert "complex high-dimensional distribution shifts to manageable one-dimensional" ones. This enables precise quantification of worst-case coverage guarantees. The researchers develop robust conformal prediction intervals that remain valid under distribution shifts, explicitly relating LP parameters to interval properties. Experimental validation on real-world datasets demonstrates the approach's practical effectiveness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e1e549a-4b04-418b-b6b8-cb607f683b47",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "c256c67c-0718-4af0-9519-a64ad1ae84b4",
  "sourceToolAssistantUUID": "8e1e549a-4b04-418b-b6b8-cb607f683b47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-30T06:14:11.044Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F2VrvtW3TjUDtPsuQdjD7W`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.02844",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c256c67c-0718-4af0-9519-a64ad1ae84b4",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe74315f-3d86-4c3c-8d9a-2a5e0995d3a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 30 · 2026-05-30T06:14:11.490Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013RiUeCZz7aeThCAeSvPSRA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2202.13415",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe74315f-3d86-4c3c-8d9a-2a5e0995d3a1",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac2a3a86-aaf3-4785-9338-4da8beb75ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 31 · 2026-05-30T06:14:11.951Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BfRRF7e6vjENMJFicujgrk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.02471",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac2a3a86-aaf3-4785-9338-4da8beb75ba5",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d93c5a2a-1d0a-406e-a77f-0c51f0106ada",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
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

_source line 32 · 2026-05-30T06:14:12.527Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RsuSfPdKZvYqdkGc6Jtbsc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.12668",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d93c5a2a-1d0a-406e-a77f-0c51f0106ada",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG6hN86b1aVHp2dj5Dk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ffc7821-2efe-4cb5-aec5-dd88d9c30520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J68KmDks83D5CGVJHs7kr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 10101,
      "output_tokens": 978,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 978,
          "cache_read_input_tokens": 10101,
          "cache_creation_input_tokens": 4036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4036,
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

_source line 33 · 2026-05-30T06:14:12.638Z_

<details><summary>↩ Tool result · `toolu_018BnLSJTgsMSDaBML2bJqUh`</summary>

```text
# Paper Summary

**Title:** "Conformal Inference under High-Dimensional Covariate Shifts via Likelihood-Ratio Regularization"

**Authors:** Sunay Joshi, Shayan Kiyani, George Pappas, Edgar Dobriban, Hamed Hassani

**Year:** 2025 (submitted February 18, 2025; last revised July 1, 2025)

**Venue:** Not explicitly mentioned; categorized as Statistics > Machine Learning on arXiv

**Abstract:**

The researchers address conformal prediction under covariate shift scenarios. They propose the likelihood ratio regularized quantile regression (LR-QR) algorithm, which "combines the pinball loss with a novel choice of regularization in order to construct a threshold function without directly estimating the unknown likelihood ratio." This approach proves advantageous for high-dimensional data like images. The method achieves valid marginal coverage in target domains with controllable error margins, utilizing stability bounds from learning theory. Testing demonstrates superiority over existing approaches across diverse applications: regression tasks on the Communities and Crime dataset, image classification via WILDS, and LLM question-answering on the MMLU benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7405bc08-804f-4971-8f4f-0a332947f994",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "ca3957d2-211c-4423-88df-694a270f3156",
  "sourceToolAssistantUUID": "7405bc08-804f-4971-8f4f-0a332947f994",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:14:13.454Z_

<details><summary>↩ Tool result · `toolu_01Ltnnn8FPioViKkLZV6xMxi`</summary>

```text
# Paper Summary

**Title:** "Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift"

**Authors:** Jungbin Jun, Ilsang Ohn

**Year:** 2025 (submitted November 6, 2025)

**Venue:** Not explicitly mentioned; posted to arXiv under Statistics > Machine Learning (stat.ML)

**Abstract:**

The researchers introduce a method for conformal prediction that adapts more quickly to distributional changes in online settings. While traditional conformal prediction guarantees coverage under exchangeability assumptions, this breaks down when data distributions shift over time. Rather than only generating predictions for new data points, their approach retroactively updates previous predictions using "regression approaches with efficient leave-one-out update formulas." This enables the full set of predictions to align with the most current distribution. According to their findings, the method delivers "faster coverage recalibration and improved statistical efficiency compared to existing online conformal prediction methods."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d9d0240-3fea-43e8-8c51-323cc007a285",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "9dac98ff-774b-47fa-b546-edc2c579840b",
  "sourceToolAssistantUUID": "4d9d0240-3fea-43e8-8c51-323cc007a285",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-30T06:14:13.707Z_

<details><summary>↩ Tool result · `toolu_015QTTvCGXQ1QgXwMWfzZnPv`</summary>

```text
# Paper Information

**Title:** "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability"

**Authors:** Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, Zhixin Zhou

**Year:** 2025 (submitted June 9, 2025)

**Venue:** Not specified as a conference or journal publication; posted on arXiv (cs.LG)

**Abstract:**

The researchers develop methods combining adversarial training with conformal prediction principles. They introduce OPSA (OPtimal Size Attack), an attack designed to "reduce the efficiency of conformal prediction at any significance level by maximizing model uncertainty." Correspondingly, they propose OPSA-AT, a defensive strategy integrating this attack within a conformal training framework. According to their findings, "our OPSA-AT defensive model significantly enhances robustness not only against OPSA but also other adversarial attacks, and maintains reliable prediction." The work targets safety-critical applications where both adversarial resilience and trustworthy uncertainty estimates are essential.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db70cdb0-8328-4bc8-aa61-85380a4eddf8",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "d0c9fd3b-7dc5-48d8-9872-7e72ecd5aeb2",
  "sourceToolAssistantUUID": "db70cdb0-8328-4bc8-aa61-85380a4eddf8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T06:14:14.491Z_

<details><summary>↩ Tool result · `toolu_01F2VrvtW3TjUDtPsuQdjD7W`</summary>

```text
# Paper Information

**Title:** "Conformal Prediction for Time-series Forecasting with Change Points"

**Authors:** Sophia Sun, Rose Yu

**Year:** 2025 (submitted September 2, 2025; latest revision December 1, 2025)

**Venue:** Not explicitly mentioned in the document

**Abstract:**

The authors propose addressing a gap in uncertainty quantification for time series by developing a novel algorithm that handles sudden shifts in data patterns. Their approach "integrat[es] a model to predict the underlying state with online conformal prediction to model uncertainties in non-stationary time series." They demonstrate theoretical validity and improved adaptivity under minimal assumptions, with empirical validation on six datasets showing performance improvements over comparable methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe74315f-3d86-4c3c-8d9a-2a5e0995d3a1",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "06e98d05-bd64-4d4b-8353-7cf9e5fb707e",
  "sourceToolAssistantUUID": "fe74315f-3d86-4c3c-8d9a-2a5e0995d3a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-30T06:14:14.641Z_

<details><summary>↩ Tool result · `toolu_01YTr4k6CeoHHEi15Myi6PAH`</summary>

```text
# Paper Details

**Title:** "Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks"

**Authors:** Xunlei Qian, Yue Xing

**Year:** 2025

**Venue:** AISTATS 2026 (submitted)

**Abstract:**

Conformal prediction methods offer distribution-free coverage guarantees but depend critically on exchangeability assumptions that may fail under distribution shift. This work examines how split conformal prediction performs when facing adversarial perturbations during testing, analyzing both coverage validity and prediction set dimensions.

The researchers characterize theoretically how adversarial perturbations during calibration influence coverage guarantees under adversarial test scenarios, and evaluate adversarial training's effects at the model-training stage.

Experimental findings show: (i) coverage varies monotonically with calibration-time attack intensity, allowing practitioners to control test-time coverage predictably; (ii) appropriately chosen calibration attacks maintain target coverage across a range of perturbation levels; and (iii) adversarial training produces more informative prediction sets while preserving high coverage rates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f3afc5-79b7-4ea8-9c27-04c1b32b2203",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "db022724-fdab-4290-9c7b-148550d8c5dd",
  "sourceToolAssistantUUID": "45f3afc5-79b7-4ea8-9c27-04c1b32b2203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T06:14:15.118Z_

<details><summary>↩ Tool result · `toolu_013RiUeCZz7aeThCAeSvPSRA`</summary>

```text
# Paper Details

**Title:** Conformal prediction beyond exchangeability

**Authors:** Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani

**Year:** 2022 (submitted February 27, 2022; revised March 17, 2023)

**Venue:** arXiv (Statistics > Methodology category)

**Abstract:**

The paper addresses limitations in conformal prediction when data violates standard assumptions. The authors note that "Conformal prediction is a popular, modern technique for providing valid predictive inference" yet typically requires exchangeability. The authors develop extensions using weighted quantiles and a novel randomization technique to handle distribution drift and asymmetric algorithms. Their approach maintains coverage guarantees under exchangeability while showing "substantially less loss of coverage when exchangeability is violated due to distribution drift." The methods are validated through simulations and applications to electricity and election forecasting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac2a3a86-aaf3-4785-9338-4da8beb75ba5",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "2e07af9d-cea5-4ab8-b0ec-42ff5a8eeae8",
  "sourceToolAssistantUUID": "ac2a3a86-aaf3-4785-9338-4da8beb75ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-30T06:14:15.903Z_

<details><summary>↩ Tool result · `toolu_01BfRRF7e6vjENMJFicujgrk`</summary>

```text
# Paper Summary

**Title:** "Predictive inference for time series: why is split conformal effective despite temporal dependence?"

**Authors:** Rina Foygel Barber and Ashwin Pananjady

**Year:** 2025 (submitted October 2, 2025; revised January 10, 2026)

**Venue:** Not specified (arXiv preprint in Statistics/Machine Learning)

**Abstract:**

The paper investigates uncertainty quantification for time series forecasting using conformal prediction methods. The authors examine why split conformal prediction performs well empirically despite violating the exchangeability assumption required by the method—a violation caused by temporal dependence in the data.

Key contributions include: introducing a "switch coefficient" to measure how temporal dependence creates exchangeability violations; providing coverage probability bounds for split conformal prediction in time series settings, including cases with memory-based predictors like autoregressive models; and establishing sharp characterizations "over the class of stationary, β-mixing processes." The work also provides analytical tools potentially applicable to other dependent data inference methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d93c5a2a-1d0a-406e-a77f-0c51f0106ada",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "bcb7fd9d-4bb2-457b-98a0-eb6eaf396b6c",
  "sourceToolAssistantUUID": "d93c5a2a-1d0a-406e-a77f-0c51f0106ada",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-30T06:14:16.731Z_

<details><summary>↩ Tool result · `toolu_01RsuSfPdKZvYqdkGc6Jtbsc`</summary>

```text
# Paper Extraction

**Title:** "Online Conformal Prediction: Enforcing monotonicity via Online Optimization"

**Authors:** Eduardo Ochoa Rivera, Ambuj Tewari

**Year:** 2026 (submitted May 12, 2026)

**Venue:** Not explicitly mentioned

**Abstract:**

The authors present methods for uncertainty quantification that produce nested prediction sets across multiple confidence levels. Their approach addresses a gap in existing online conformal prediction by ensuring "consistency across multiple confidence levels" rather than focusing on a single coverage level. 

The framework is motivated by practical applications where "different users operate under heterogeneous risk tolerances." By jointly estimating multiple coverage levels with non-crossing constraints, the methods improve statistical efficiency similar to quantile regression approaches.

The authors leverage "an online optimization perspective with small regret" to maintain coverage guarantees while enforcing nestedness. Their empirical evaluation demonstrates that the proposed approach achieves "stable coverage across all levels, strictly nested prediction sets, and improved efficiency compared to existing online conformal baselines" on both synthetic and real-world forecasting tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ffc7821-2efe-4cb5-aec5-dd88d9c30520",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "dcd70f0d-c219-4b36-a6cc-9c25e9f6ad12",
  "sourceToolAssistantUUID": "6ffc7821-2efe-4cb5-aec5-dd88d9c30520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-30T06:14:21.603Z_

Now let me search for a few more papers that were referenced in the results, plus look for additional papers citing the Scholten & Gunnemann work and the Verifiably Robust CP paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd70f0d-c219-4b36-a6cc-9c25e9f6ad12",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG7yLaymMFegihNmAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c8c596d-9a4d-40a5-a78f-77edb177d1b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4EsgBMPisRmSvLDRbEfoY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10597,
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

_source line 42 · 2026-05-30T06:14:22.141Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0178QAKizvQYFEjkvkdVztH6`</summary>

```json
{
  "query": "Verifiably Robust Conformal Prediction arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c8c596d-9a4d-40a5-a78f-77edb177d1b1",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG7yLaymMFegihNmAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5ee9ae5-799b-493f-8537-4ee12a051b71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4EsgBMPisRmSvLDRbEfoY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10597,
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

_source line 43 · 2026-05-30T06:14:23.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H34G6jh96KRF5ZqTpn81Up`</summary>

```json
{
  "query": "COLEP conformal prediction logical reasoning robustness 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5ee9ae5-799b-493f-8537-4ee12a051b71",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG7yLaymMFegihNmAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dc03bf0-63a2-4071-af1b-1f0f5fe032be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4EsgBMPisRmSvLDRbEfoY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10597,
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

_source line 44 · 2026-05-30T06:14:23.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VjrEu8jcEDxrUxin52NXx`</summary>

```json
{
  "query": "site:arxiv.org conformal prediction robust coverage poisoning calibration 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dc03bf0-63a2-4071-af1b-1f0f5fe032be",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG7yLaymMFegihNmAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2606a749-1906-46a3-9083-d5a51b4f19dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4EsgBMPisRmSvLDRbEfoY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10597,
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

_source line 45 · 2026-05-30T06:14:24.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WVXZoTjzmzVhjtmL9hwr7B`</summary>

```json
{
  "query": "conformal prediction adversarial examples certified robustness 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2606a749-1906-46a3-9083-d5a51b4f19dd",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG7yLaymMFegihNmAcm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8851a358-8fdf-473e-a86f-3bc710ed79d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4EsgBMPisRmSvLDRbEfoY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10597,
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

_source line 46 · 2026-05-30T06:14:28.337Z_

<details><summary>↩ Tool result · `toolu_0178QAKizvQYFEjkvkdVztH6`</summary>

```text
Web search results for query: "Verifiably Robust Conformal Prediction arXiv 2024 2025"

Links: [{"title":"Verifiably Robust Conformal Prediction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/verifiably-robust-conformal-prediction"},{"title":"Verifiably Robust Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=5pJfDlaSxV"},{"title":"[2405.18942] Verifiably Robust Conformal Prediction","url":"https://arxiv.org/abs/2405.18942"},{"title":"Verifiably Robust Conformal Prediction","url":"https://arxiv.org/html/2405.18942v3"},{"title":"Verifiably Robust Conformal Prediction","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/0814a342597d65e0832fc7ec9b42c317-Abstract-Conference.html"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"}]

Based on the search results, here's what I found about "Verifiably Robust Conformal Prediction":

## Overview

VRCP (Verifiably Robust Conformal Prediction) is a new framework that leverages recent neural network verification methods to recover coverage guarantees under adversarial attacks.

## Key Features

The paper introduces a novel conformal prediction algorithm called "verifiably robust conformal prediction" (VRCP) that constructs prediction sets guaranteed to contain the true outcome with a pre-specified probability (e.g. 95% of the time).

## Problem It Addresses

The guarantee is violated when the data is subjected to adversarial attacks, which often result in a significant loss of coverage. Previous approaches leverage variations of randomised smoothing to produce conservative sets, but are limited in that they only support ℓ²-bounded perturbations and classification tasks.

## Innovations

The VRCP method is the first to support perturbations bounded by arbitrary norms including ℓ¹, ℓ², and ℓ∞, as well as regression tasks.

## Publication

The paper was published on September 25, 2024 and was presented as a NeurIPS 2024 poster. The arXiv paper is numbered 2405.18942.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5ee9ae5-799b-493f-8537-4ee12a051b71",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "72380964-3daf-4be6-a90a-e6ee5ca99b77",
  "sourceToolAssistantUUID": "c5ee9ae5-799b-493f-8537-4ee12a051b71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-30T06:14:28.429Z_

<details><summary>↩ Tool result · `toolu_01H34G6jh96KRF5ZqTpn81Up`</summary>

```text
Web search results for query: "COLEP conformal prediction logical reasoning robustness 2024 2025"

Links: [{"title":"[Literature Review] COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits","url":"https://www.themoonlight.io/en/review/colep-certifiably-robust-learning-reasoning-conformal-prediction-via-probabilistic-circuits"},{"title":"COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via   Probabilistic Circuits","url":"https://arxiv.org/pdf/2403.11348"},{"title":"COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits","url":"https://arxiv.org/html/2403.11348v1"},{"title":"COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits | OpenReview","url":"https://openreview.net/forum?id=XN6ZPINdSg&noteId=dp9iei4nRp"},{"title":"[2403.11348] COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits","url":"https://arxiv.org/abs/2403.11348"},{"title":"COLEP: Certifiably Robust Learning- Reasoning Conformal Prediction via","url":"https://iclr.cc/media/iclr-2024/Slides/18452_hMRSXz4.pdf"},{"title":"GitHub - kangmintong/COLEP: [ICLR 2024] Codes for COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits · GitHub","url":"https://github.com/kangmintong/COLEP"}]

Based on the search results, here's what I found about COLEP:

## Overview
COLEP is a certifiably robust learning-reasoning conformal prediction framework via probabilistic circuits, which comprises a data-driven learning component that trains statistical models to learn different semantic concepts, and a reasoning component that encodes knowledge and characterizes the relationships among the statistical knowledge models for logic reasoning.

## Problem It Addresses
Even small adversarial perturbations during the inference can violate the exchangeability assumption, challenge the coverage guarantees, and result in a subsequent decline in prediction coverage. The framework provides end-to-end certification of prediction coverage for COLEP under ℓ₂ bounded adversarial perturbations, and also provides certified coverage considering the finite size of the calibration set.

## Key Contributions
COLEP achieves higher prediction coverage and accuracy over a single model as long as the utilities of knowledge models are non-trivial.

## Publication
The paper was presented at the ICLR 2024 conference. Code for COLEP is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc03bf0-63a2-4071-af1b-1f0f5fe032be",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "fb25f669-8dab-410b-ba2b-90cd3450bc4d",
  "sourceToolAssistantUUID": "0dc03bf0-63a2-4071-af1b-1f0f5fe032be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-30T06:14:30.581Z_

<details><summary>↩ Tool result · `toolu_019VjrEu8jcEDxrUxin52NXx`</summary>

```text
Web search results for query: "site:arxiv.org conformal prediction robust coverage poisoning calibration 2024 2025"

Links: [{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/html/2511.18562"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Another Fit Bites the Dust: Conformal Prediction as a Calibration Standard for Machine Learning in High-Energy Physics","url":"https://arxiv.org/html/2512.17048v1"},{"title":"Conformal prediction without knowledge of labeled calibration data","url":"https://arxiv.org/pdf/2509.10321"},{"title":"[2407.07700] Split Conformal Prediction under Data Contamination","url":"https://arxiv.org/abs/2407.07700"}]

I found several highly relevant papers on arxiv.org about conformal prediction with robustness, coverage, poisoning, and calibration from 2024-2025. Here are the key results:

1. **Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning** - Submitted on 13 Oct 2024 (v1), last revised 16 Mar 2025 (this version, v4). This paper proposes reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning.

2. **Robust Yet Efficient Conformal Prediction Sets** - This paper presents results about conformal prediction robust to feature poisoning with nominal coverage guarantees, tested on CIFAR-10 dataset.

3. **Enhancing Adversarial Robustness with Conformal Prediction** - A recent paper from June 2025 that presents a framework addressing how Conformal Prediction offers distribution-free coverage guarantees but encounters difficulties when subjected to data poisoning and adversarial attacks.

4. **Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks** - A December 2025 paper addressing calibration robustness in conformal prediction.

5. **Split Conformal Prediction under Data Contamination** - This paper proposes Contamination Robust Conformal Prediction as an adjustment in the classification setting.

6. **Conformal Prediction without Knowledge of Labeled Calibration Data** - A September 2024 paper exploring conformal prediction when calibration data is not available.

7. **Another Fit Bites the Dust: Conformal Prediction as a Calibration Standard for Machine Learning in High-Energy Physics** - A December 2025 paper exploring applications of conformal prediction in physics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2606a749-1906-46a3-9083-d5a51b4f19dd",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "ea7e0d8d-f64e-409e-8cfa-d8e47ee29d89",
  "sourceToolAssistantUUID": "2606a749-1906-46a3-9083-d5a51b4f19dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-30T06:14:32.849Z_

<details><summary>↩ Tool result · `toolu_01WVXZoTjzmzVhjtmL9hwr7B`</summary>

```text
Web search results for query: "conformal prediction adversarial examples certified robustness 2024 2025 arXiv"

Links: [{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"(PDF) Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://www.researchgate.net/publication/397934771_Ensuring_Calibration_Robustness_in_Split_Conformal_Prediction_Under_Adversarial_Attacks"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/html/2511.18562"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"},{"title":"Provably Robust Conformal Prediction with Improved Efficiency","url":"https://arxiv.org/pdf/2404.19651"},{"title":"[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/abs/2506.07804"}]

I've found several recent papers on the intersection of conformal prediction, adversarial examples, and certified robustness from 2024-2025. Here are the key findings:

## Recent Papers (2024-2025)

**1. Conformal Prediction under Lévy–Prokhorov Distribution Shifts**
Clarkson et al. (2024) addressed split conformal prediction under data contamination, with a focus on balancing robustness and informativeness while identifying parameters that yield the tightest worst-case conformal prediction sets under distribution shift.

**2. Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks**
Recent complementary developments include probabilistic robustness via quantile-of-quantiles, adversarially valid guarantees for sequential settings, certifiable reasoning with probabilistic circuits, Lipschitz-bounded models for scalable certification, and conformal training/attack frameworks that directly optimize set size under threat, collectively advancing provably robust conformal prediction in adversarial scenarios by addressing both validity and efficiency.

**3. Enhancing Adversarial Robustness with Conformal Prediction (2025)**
Researchers developed OPSA (OPtimal Size Attack), an adversarial attack method designed to reduce conformal prediction efficiency by maximizing model uncertainty, and OPSA-AT (Adversarial Training), a defense strategy that integrates OPSA within a novel conformal training paradigm. The OPSA-AT defensive model significantly enhances robustness against OPSA and other adversarial attacks while maintaining reliable prediction.

**4. Provably Robust Conformal Prediction with Improved Efficiency**
Gendler et al. (2021) proposed Randomized Smoothed Conformal Prediction (RSCP), which constructs prediction sets robust to adversarial examples with coverage guarantees even under perturbations.

These papers represent active research at the intersection of these three areas on arXiv, with significant work published in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8851a358-8fdf-473e-a86f-3bc710ed79d9",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "e7433a85-132a-402f-b644-a071119adca0",
  "sourceToolAssistantUUID": "8851a358-8fdf-473e-a86f-3bc710ed79d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-30T06:14:35.395Z_

Let me fetch the remaining key papers I've discovered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7433a85-132a-402f-b644-a071119adca0",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56f814b4-909b-40fb-8428-02ccde8a1301",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 51 · 2026-05-30T06:14:36.782Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018iNc5uJK1dERqfzSBhpwbu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.18942",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f814b4-909b-40fb-8428-02ccde8a1301",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "915cd234-d01a-4425-a9a4-8c09b51b3e8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 52 · 2026-05-30T06:14:37.252Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CACtaiZYz7W85JMpCEv2Lb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.11348",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "915cd234-d01a-4425-a9a4-8c09b51b3e8e",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f089e22-1af7-4230-b395-692f5e4e96d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 53 · 2026-05-30T06:14:38.205Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013WDGEqbD8e9zWUrtJBAqDf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.07700",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f089e22-1af7-4230-b395-692f5e4e96d2",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3de78b8-7376-4dca-9fe8-091349186609",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 54 · 2026-05-30T06:14:38.668Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013REmDnq5cgchQsYVe9Zky1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.19651",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3de78b8-7376-4dca-9fe8-091349186609",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc52e3f7-fd20-4624-8494-99657731813a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 55 · 2026-05-30T06:14:39.610Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X7q46DT711NLjRubB6c9V1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.05239",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc52e3f7-fd20-4624-8494-99657731813a",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cbf463a-abec-4519-9464-0705bbeac555",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 56 · 2026-05-30T06:14:40.597Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012fSZhLVqjvtsvyRd9qGsQM`</summary>

```json
{
  "url": "https://openreview.net/forum?id=7puF5JOkKk",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the abstract or summary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cbf463a-abec-4519-9464-0705bbeac555",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9AKfFvMHXB4UKERgk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03d7ece2-8f2e-46dd-b747-8cb5f9dc91ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLVhQxoxQ8Kj5thzMtg77",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3454,
      "cache_read_input_tokens": 18010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3454,
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

_source line 57 · 2026-05-30T06:14:42.169Z_

<details><summary>↩ Tool result · `toolu_01CACtaiZYz7W85JMpCEv2Lb`</summary>

```text
# Paper Details

**Title:** COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits

**Authors:** Mintong Kang, Nezihe Merve Gürel, Linyi Li, Bo Li

**Year:** 2024

**Venue:** ICLR 2024

**Abstract:**

The paper addresses a vulnerability in conformal prediction: adversarial perturbations can undermine the exchangeability assumption and compromise coverage guarantees. The authors propose COLEP, a framework combining "a data-driven learning component that trains statistical models to learn different semantic concepts, and a reasoning component that encodes knowledge and characterizes the relationships among the trained models for logic reasoning." Probabilistic circuits enable efficient exact reasoning.

Theoretically, the work provides certification of prediction coverage under bounded adversarial perturbations and accounts for finite calibration sets. The authors demonstrate that their approach surpasses single-model performance when knowledge models have non-trivial utility. Empirically, COLEP achieves improvements in certified coverage: up to 12% on GTSRB, 9% on CIFAR-10, and 14% on AwA2 datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f089e22-1af7-4230-b395-692f5e4e96d2",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "1af913fd-4a28-4dbe-b786-3fafd30ffe39",
  "sourceToolAssistantUUID": "8f089e22-1af7-4230-b395-692f5e4e96d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-30T06:14:42.415Z_

<details><summary>↩ Tool result · `toolu_018iNc5uJK1dERqfzSBhpwbu`</summary>

```text
# Paper Summary

**Title:** "Verifiably Robust Conformal Prediction"

**Authors:** Linus Jeary, Tom Kuipers, Mehran Hosseini, Nicola Paoletti

**Year:** 2024

**Venue:** NeurIPS 2024

**Abstract:**

The researchers address a vulnerability in Conformal Prediction (CP), a method for generating statistically valid prediction sets. While CP normally guarantees coverage of true test outputs, this breaks down under adversarial attacks. Previous solutions using randomized smoothing only handled ℓ₂-bounded perturbations and classification tasks.

The authors present VRCP, a framework leveraging neural network verification methods to recover coverage guarantees. Their approach supports "perturbations bounded by arbitrary norms including ℓ¹, ℓ², and ℓ∞, as well as regression tasks." Testing on CIFAR10, CIFAR100, TinyImageNet, and deep reinforcement learning environments shows VRCP achieves nominal coverage while producing more efficient prediction regions than existing methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "915cd234-d01a-4425-a9a4-8c09b51b3e8e",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "81f78490-7f80-4487-b009-e692c1fe0a30",
  "sourceToolAssistantUUID": "915cd234-d01a-4425-a9a4-8c09b51b3e8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-30T06:14:42.457Z_

<details><summary>↩ Tool result · `toolu_013WDGEqbD8e9zWUrtJBAqDf`</summary>

```text
# Paper Summary

**Title:** Split Conformal Prediction under Data Contamination

**Authors:** Jase Clarkson, Wenkai Xu, Mihai Cucuringu, Yvik Swan, Gesine Reinert

**Year:** 2024 (submitted July 10, 2024; latest revision November 28, 2025)

**Venue:** Not explicitly mentioned; classified under Statistics > Machine Learning

**Abstract:** 

The researchers investigate how split conformal prediction—a computationally efficient non-parametric approach for building prediction intervals—performs when calibration data contains contamination. They examine scenarios where "a small fraction of the calibration scores are drawn from a different distribution than the bulk." The study quantifies how such corrupted data affects coverage guarantees and prediction set efficiency on clean test data. Additionally, the authors introduce an enhancement called Contamination Robust Conformal Prediction for classification tasks and validate their theoretical findings through numerical and real-world experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3de78b8-7376-4dca-9fe8-091349186609",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "68edeb98-1277-42c1-8425-8caf0a9f534f",
  "sourceToolAssistantUUID": "a3de78b8-7376-4dca-9fe8-091349186609",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-30T06:14:42.619Z_

<details><summary>↩ Tool result · `toolu_013REmDnq5cgchQsYVe9Zky1`</summary>

```text
# Paper Information

**Title:** "Provably Robust Conformal Prediction with Improved Efficiency"

**Authors:** Ge Yan, Yaniv Romano, Tsui-Wei Weng

**Year:** 2024

**Venue:** Not explicitly mentioned (arXiv preprint, cs.LG category)

**Abstract:**

The authors address vulnerabilities in conformal prediction methods when facing adversarial examples. They introduce RSCP+, a framework providing "provable robustness guarantee in evaluation," fixing limitations in the earlier RSCP approach. Additionally, they propose two techniques—Post-Training Transformation and Robust Conformal Training—to reduce prediction set sizes while maintaining robustness guarantees.

Results across CIFAR10, CIFAR100, and ImageNet demonstrate efficiency improvements of up to 4.36×, 5.46×, and 16.9× respectively, where baseline methods "only yield trivial predictions including full label set." The authors provide code availability for reproducibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc52e3f7-fd20-4624-8494-99657731813a",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "0eaf0bc0-da50-4cb9-b771-9c9acb6afe98",
  "sourceToolAssistantUUID": "bc52e3f7-fd20-4624-8494-99657731813a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-30T06:14:43.299Z_

<details><summary>↩ Tool result · `toolu_01X7q46DT711NLjRubB6c9V1`</summary>

```text
# Paper Details

**Title:** Robust Conformal Prediction with a Single Binary Certificate

**Authors:** Soroush H. Zargarbashi, Aleksandar Bojchevski

**Year:** 2025

**Venue:** ICLR 2025

**Abstract:**

This work addresses conformal prediction (CP) under adversarial conditions. CP typically converts model outputs into prediction sets with probabilistic coverage guarantees. The authors' method enhances robustness through "binarizing samples with an adjustable threshold selected to preserve the coverage guarantee."

A key innovation is that robustness is achieved "by computing only one binary certificate, unlike previous methods that certify each calibration (or test) point." This approach yields smaller prediction sets while requiring significantly fewer Monte Carlo samples—approximately 150 for CIFAR10 compared to the ~10,000 samples needed by existing baselines. Additionally, the method eliminates the previous constraint requiring bounded score functions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cbf463a-abec-4519-9464-0705bbeac555",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "d77de1d2-b7f2-4d3f-bf69-9d657f2b458d",
  "sourceToolAssistantUUID": "3cbf463a-abec-4519-9464-0705bbeac555",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-30T06:14:44.089Z_

<details><summary>↩ Tool result · `toolu_012fSZhLVqjvtsvyRd9qGsQM`</summary>

```text
# Paper Extraction

**Title:** "Conformal Regression under Distribution Shift: A Reinforcement Learning Method for Adaptive Uncertainty Quantification"

**Authors:** Yilei Zhao, Wentao Zhang, Miguel R. Pebes-Trujillo, Junxian Liu, Hongxin Wei, Wei Yang Bryan Lim

**Year:** 2025 (submitted); modified February 2026

**Venue:** ICLR 2026 Conference (Desk Rejected Submission)

**Summary:** 

This work introduces CORE, a method combining reinforcement learning with conformal prediction for time-series forecasting. The authors address limitations in existing adaptive conformal prediction approaches by creating "a mutual feedback loop between reinforcement learning and conformal prediction." The system uses exploration to better handle uncertain regions and outliers while dynamically calibrating prediction intervals through uncertainty-guided rewards.

The experimental evaluation across 8 standard time-series datasets shows the approach achieves approximately "1.36% improvement in coverage rate and 5.03% in interval length" compared to six baseline methods, demonstrating gains in both prediction accuracy and interval quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03d7ece2-8f2e-46dd-b747-8cb5f9dc91ab",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "81385eed-e177-4505-a62f-774aeed62902",
  "sourceToolAssistantUUID": "03d7ece2-8f2e-46dd-b747-8cb5f9dc91ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-30T06:14:46.525Z_

Let me also search for a couple more recent papers in this space that may have been missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81385eed-e177-4505-a62f-774aeed62902",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9zKRqr6pV4Hw4vxZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1c370e4-e9e5-4bdd-9e88-b7fbb4a24af1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyMgDK2kddxaz5y5JdBFUP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2214,
      "cache_read_input_tokens": 21464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2214,
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

_source line 64 · 2026-05-30T06:14:47.781Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JhtGypMGw667MMqAjzkq8r`</summary>

```json
{
  "query": "arXiv \"robust conformal prediction\" \"backdoor\" OR \"Byzantine\" OR \"corruption\" 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1c370e4-e9e5-4bdd-9e88-b7fbb4a24af1",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9zKRqr6pV4Hw4vxZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "004c53ec-1ce2-4bd4-bcd6-0821c64abfe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyMgDK2kddxaz5y5JdBFUP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2214,
      "cache_read_input_tokens": 21464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2214,
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

_source line 65 · 2026-05-30T06:14:48.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QYVviQR2eMZD2H1k9FKdzX`</summary>

```json
{
  "query": "arXiv conformal prediction \"label noise\" OR \"data corruption\" robust coverage guarantee 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "004c53ec-1ce2-4bd4-bcd6-0821c64abfe1",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYG9zKRqr6pV4Hw4vxZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49e34d30-4fe7-489a-a368-43c7b1d1261c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyMgDK2kddxaz5y5JdBFUP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2214,
      "cache_read_input_tokens": 21464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2214,
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

_source line 66 · 2026-05-30T06:14:55.284Z_

<details><summary>↩ Tool result · `toolu_01JhtGypMGw667MMqAjzkq8r`</summary>

```text
Web search results for query: "arXiv "robust conformal prediction" "backdoor" OR "Byzantine" OR "corruption" 2024 2025"

Links: [{"title":"[2406.01960] Certifiably Byzantine-Robust Federated Conformal Prediction","url":"https://arxiv.org/abs/2406.01960"},{"title":"Certifiably Byzantine-Robust Federated Conformal Prediction","url":"https://arxiv.org/pdf/2406.01960"},{"title":"Certiﬁably Byzantine-Robust Federated Conformal Prediction","url":"https://par.nsf.gov/servlets/purl/10524900"},{"title":"Certifiably Byzantine-Robust Federated Conformal Prediction","url":"https://arxiv.org/html/2406.01960v1"},{"title":"(PDF) Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://www.researchgate.net/publication/397934771_Ensuring_Calibration_Robustness_in_Split_Conformal_Prediction_Under_Adversarial_Attacks"},{"title":"[2405.18942] Verifiably Robust Conformal Prediction","url":"https://arxiv.org/abs/2405.18942"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/html/2503.05239v1"}]

I've found several relevant research papers on arXiv related to robust conformal prediction with Byzantine, backdoor, and corruption threats in 2024-2025:

## Key Papers Found:

1. **Certifiably Byzantine-Robust Federated Conformal Prediction** (June 2024)
   - Introduces Rob-FCP framework which executes robust federated conformal prediction, effectively countering malicious clients capable of reporting arbitrary statistics with the conformal calibration process
   - Demonstrates robustness against diverse proportions of malicious clients under a variety of Byzantine attacks on five standard benchmark and real-world healthcare datasets

2. **Verifiably Robust Conformal Prediction** (May-November 2024)
   - Introduces VRCP (Verifiably Robust Conformal Prediction), a framework that leverages recent neural network verification methods to recover coverage guarantees under adversarial attacks

3. **Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning** (October 2024)
   - Addresses reliability of prediction sets under data poisoning threats where adversaries can modify, add or remove datapoints

4. **Robust Conformal Prediction with a Single Binary Certificate** (March 2025)
   - Recent robust CP baselines use a conservative score at test time that is a certified bound on the conformity score of the clean unseen input

5. **Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks** (November 2025)
   - Recent work on adversarial robustness in conformal prediction calibration

These papers represent active research in making conformal prediction methods robust against various attack vectors including Byzantine failures, data poisoning/corruption, and adversarial perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "004c53ec-1ce2-4bd4-bcd6-0821c64abfe1",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "cfe0eb1a-2501-48a0-a25f-ba31bbc25308",
  "sourceToolAssistantUUID": "004c53ec-1ce2-4bd4-bcd6-0821c64abfe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-30T06:14:56.917Z_

<details><summary>↩ Tool result · `toolu_01QYVviQR2eMZD2H1k9FKdzX`</summary>

```text
Web search results for query: "arXiv conformal prediction "label noise" OR "data corruption" robust coverage guarantee 2024 2025"

Links: [{"title":"Conformal Prediction with Corrupted Labels:","url":"https://arxiv.org/pdf/2505.04733"},{"title":"Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting","url":"https://arxiv.org/html/2505.04733v1"},{"title":"Label Noise Robustness of Conformal Prediction","url":"https://www.jmlr.org/papers/volume25/23-1549/23-1549.pdf"},{"title":"[2501.18363v3] Exploring the Noise Robustness of Online Conformal Prediction","url":"https://arxiv.org/abs/2501.18363v3"},{"title":"Conformal Prediction of Classifiers with Many Classes based on Noisy Labels","url":"https://arxiv.org/html/2501.12749v2"},{"title":"Exploring the Noise Robustness of Online Conformal Prediction","url":"https://arxiv.org/html/2501.18363"},{"title":"[2501.18363] Robust Online Conformal Prediction under Uniform Label Noise","url":"https://ar5iv.labs.arxiv.org/html/2501.18363"},{"title":"Robust Online Conformal Prediction under Uniform Label ...","url":"https://arxiv.org/abs/2501.18363"},{"title":"Online Conformal Prediction with Corrupted Feedback","url":"https://arxiv.org/html/2605.20515"},{"title":"Robust Online Conformal Prediction under Uniform Label Noise","url":"https://arxiv.org/html/2501.18363v2"}]

I found several highly relevant papers on arXiv about conformal prediction with label noise and data corruption from 2024-2025:

## Key Recent Papers

1. **"Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting"** (arXiv:2505.04733, May 2025)
   - Leverages recent results on label-noise robustness of conformal prediction, with related work on robust conformal outlier detection under contaminated reference data

2. **"Robust Online Conformal Prediction under Uniform Label Noise"** (arXiv:2501.18363, January-October 2025)
   - Label noise causes a persistent gap between the actual mis-coverage rate and the desired rate, leading to either overestimated or underestimated coverage guarantees
   - Proposes Noise Robust Online Conformal Prediction (NR-OCP) by updating the threshold with a novel robust pinball loss, which provides an unbiased estimate of clean pinball loss
   - Achieves a convergence rate of O(T^-1/2) for both empirical and expected coverage errors under uniform label noise

3. **"Conformal Prediction of Classifiers with Many Classes based on Noisy Labels"** (arXiv:2501.12749, 2025)
   - Addresses estimating the conformal prediction threshold from noisy labels

4. **"Online Conformal Prediction with Corrupted Feedback"** (arXiv:2605.20515, recent 2026)
   - Addresses conformal prediction in online settings with corrupted feedback

These papers provide both theoretical analysis and practical methods for maintaining robust coverage guarantees when training data contains label noise or corruption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49e34d30-4fe7-489a-a368-43c7b1d1261c",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "8f87ffc7-de37-4153-b826-e0ab616e45cd",
  "sourceToolAssistantUUID": "49e34d30-4fe7-489a-a368-43c7b1d1261c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-30T06:15:00.990Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KnY8RY8P23kTLLnZwuDpK8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.01960",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f87ffc7-de37-4153-b826-e0ab616e45cd",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYGAw7UNGFRCztEEQ6Xz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8aaae87-8b3e-4e51-8a77-fdd7e7a6cf7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqA8kVkR7GMSKu9FW32PBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 23678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 69 · 2026-05-30T06:15:01.461Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HxgDUzQK2hTg4k6J8mbXD9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.04733",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8aaae87-8b3e-4e51-8a77-fdd7e7a6cf7d",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYGAw7UNGFRCztEEQ6Xz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdd91816-ce3c-4ff8-9907-e7c3c598ff98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqA8kVkR7GMSKu9FW32PBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 23678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 70 · 2026-05-30T06:15:02.416Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JZk68Z2HZZYyXGd8oSgwz2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.18363",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdd91816-ce3c-4ff8-9907-e7c3c598ff98",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYGAw7UNGFRCztEEQ6Xz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "743d0ca4-7e2e-40b6-bc27-8bd0f5555d5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqA8kVkR7GMSKu9FW32PBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 23678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 71 · 2026-05-30T06:15:02.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VD82vLQoV91rkfnCmcWNmn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.12749",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "743d0ca4-7e2e-40b6-bc27-8bd0f5555d5f",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYGAw7UNGFRCztEEQ6Xz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "081447ce-485d-45f4-8b6d-53f92ac37273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqA8kVkR7GMSKu9FW32PBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 23678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 72 · 2026-05-30T06:15:03.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013wskU9QgPVFA35QrD2oCFH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.20515",
  "prompt": "Extract the paper title, full author list, year, venue if mentioned, and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "081447ce-485d-45f4-8b6d-53f92ac37273",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYGAw7UNGFRCztEEQ6Xz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf793f44-46bd-4566-9860-38ad7bf2f8e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqA8kVkR7GMSKu9FW32PBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 23678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 73 · 2026-05-30T06:15:04.982Z_

<details><summary>↩ Tool result · `toolu_01KnY8RY8P23kTLLnZwuDpK8`</summary>

```text
# Paper Details

**Title:** "Certifiably Byzantine-Robust Federated Conformal Prediction"

**Authors:** Mintong Kang, Zhen Lin, Jimeng Sun, Cao Xiao, Bo Li

**Year:** 2024

**Venue:** ICML 2024 (International Conference on Machine Learning)

**Abstract:**

The paper addresses vulnerabilities in federated conformal prediction systems where malicious clients can compromise uncertainty quantification. The researchers introduce Rob-FCP, a framework that maintains coverage guarantees despite Byzantine failures. Key contributions include:

- A novel approach to "robust federated conformal prediction, effectively countering malicious clients capable of reporting arbitrary statistics with the conformal calibration process"
- Theoretical analysis proving "the coverage of Rob-FCP is asymptotically close to the desired coverage level"
- A method to estimate the number of malicious clients when unknown
- Empirical validation across benchmark and healthcare datasets

The work combines conformal prediction's statistical rigor with federated learning's distributed architecture while defending against adversarial attacks from compromised nodes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8aaae87-8b3e-4e51-8a77-fdd7e7a6cf7d",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "a0dcb5fa-866a-4fb0-9973-820ea0482190",
  "sourceToolAssistantUUID": "c8aaae87-8b3e-4e51-8a77-fdd7e7a6cf7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-30T06:15:06.136Z_

<details><summary>↩ Tool result · `toolu_01HxgDUzQK2hTg4k6J8mbXD9`</summary>

```text
# Paper Details

**Title:** "Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting"

**Authors:** Shai Feldman, Stephen Bates, Yaniv Romano

**Year:** 2025 (submitted May 7, 2025; latest revision February 26, 2026)

**Venue:** Not explicitly mentioned; categorized under Computer Science > Machine Learning (cs.LG)

**Abstract:**

The researchers present a framework addressing uncertainty quantification when training data contain corrupted labels. Building on conformal prediction methodology, they develop techniques to generate prediction sets with guaranteed coverage despite noisy or missing labels. Their approach extends privileged conformal prediction by analyzing its robustness to weight estimation errors. Additionally, they introduce uncertain imputation—a new method that avoids weight estimation by preserving label uncertainty during imputation. The framework provides theoretical guarantees and includes a triply robust variant ensuring valid predictions when at least one underlying component functions correctly. They validate their methods through experiments on synthetic and real datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdd91816-ce3c-4ff8-9907-e7c3c598ff98",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "c7ef7f25-b86d-4630-9ebd-b3fef514adb8",
  "sourceToolAssistantUUID": "fdd91816-ce3c-4ff8-9907-e7c3c598ff98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-30T06:15:06.193Z_

<details><summary>↩ Tool result · `toolu_01VD82vLQoV91rkfnCmcWNmn`</summary>

```text
# Paper Details

**Title:** Conformal Prediction of Classifiers with Many Classes based on Noisy Labels

**Authors:** Coby Penso, Jacob Goldberger, Ethan Fetaya

**Year:** 2025

**Venue:** COPA 2025 (Conformal and Probabilistic Prediction with Applications), Proceedings of Machine Learning Research 26

**Abstract:**

The paper addresses calibration of conformal prediction systems when only noisy training labels are available. The authors present "Noise-Aware Conformal Prediction (NACP)," which estimates proper prediction thresholds despite label corruption. Their method "controls the prediction uncertainty of classification systems by producing a small prediction set" with guaranteed coverage probability. The approach offers theoretical finite-sample guarantees for uniform noise that scale well to multiclass scenarios, demonstrated on image classification benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "081447ce-485d-45f4-8b6d-53f92ac37273",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "80e9ebb1-6902-4010-8dc0-ab3313cb7ba7",
  "sourceToolAssistantUUID": "081447ce-485d-45f4-8b6d-53f92ac37273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-30T06:15:06.848Z_

<details><summary>↩ Tool result · `toolu_01JZk68Z2HZZYyXGd8oSgwz2`</summary>

```text
# Paper Information

**Title:** "Exploring the Noise Robustness of Online Conformal Prediction"

**Authors:** Huajun Xi, Kangdao Liu, Hao Zeng, Wenguang Sun, Hongxin Wei

**Year:** 2025

**Venue:** NIPS 2025

**Abstract:**

Conformal prediction enables uncertainty quantification by generating prediction sets that reliably contain true labels with predetermined probability. The researchers examine how uniform label noise impacts online conformal prediction—methods designed to adjust predictions amid distribution shifts. Their key finding reveals that "label noise causes a persistent gap between the actual mis-coverage rate and the desired rate α." They introduce Noise Robust Online Conformal Prediction (NR-OCP), which employs robust pinball loss for threshold updates without requiring clean labels. Theoretically, their approach "achieves a convergence rate of O(T^{-1/2})" for coverage errors under uniform noise across constant and dynamic learning schedules. Experimental results demonstrate effectiveness in maintaining both accurate coverage and computational efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "743d0ca4-7e2e-40b6-bc27-8bd0f5555d5f",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "cb249ed4-9a89-49d4-8c0d-2442d836b0c0",
  "sourceToolAssistantUUID": "743d0ca4-7e2e-40b6-bc27-8bd0f5555d5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-30T06:15:07.463Z_

<details><summary>↩ Tool result · `toolu_013wskU9QgPVFA35QrD2oCFH`</summary>

```text
# Paper Details

**Title:** "Online Conformal Prediction with Corrupted Feedback"

**Authors:** Bowen Wang, Matteo Zecchin, Osvaldo Simeone

**Year:** 2026 (submitted May 19, 2026)

**Venue:** Not explicitly mentioned; categorized under Computer Science > Machine Learning (cs.LG) and Signal Processing (eess.SP) on arXiv

**Abstract:**

The paper addresses the challenge of maintaining reliable uncertainty estimates in sequential, non-stationary settings. While online conformal prediction typically assumes perfect feedback, this work examines what happens when feedback becomes corrupted through noise, communication failures, or adversarial interference. 

The researchers propose two robust approaches: one leveraging structural properties of predicted thresholds to filter corrupted feedback, and another using active compensation mechanisms. Both methods provide explicit miscoverage guarantees, with specialized analysis for independent stochastic and arbitrary error models with memory constraints. Experimental validation on real-world datasets demonstrates that these approaches achieve "markedly improved calibration and significantly smaller prediction sets" compared to baseline methods under corrupted feedback conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf793f44-46bd-4566-9860-38ad7bf2f8e5",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "adbfc87c1aba5efc3",
  "type": "user",
  "uuid": "510d23b7-3097-4b37-98aa-c6233626a584",
  "sourceToolAssistantUUID": "cf793f44-46bd-4566-9860-38ad7bf2f8e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-30T06:16:20.467Z_

Now I have a comprehensive collection. Here is the structured literature survey:

---

## Literature Survey: Robust Conformal Prediction (2024--2026)

### CATEGORY A: Robustness to Data Poisoning

**1. Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning**
- **Authors:** Yan Scholten, Stephan Gunnemann
- **Venue:** ICLR 2025 (Spotlight)
- **Year:** 2024 (arXiv), 2025 (published)
- **URL:** https://arxiv.org/abs/2410.09878
- **Summary:** Introduces Reliable Prediction Sets (RPS) -- the first efficient method for conformal prediction with provable reliability guarantees under both training and calibration data poisoning, using smoothed score functions over data partitions and majority-vote aggregation of calibration subsets.

**2. Robust Yet Efficient Conformal Prediction Sets**
- **Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski
- **Venue:** ICML 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.09165
- **Summary:** Derives tight CDF-based bounds on worst-case conformity score changes to construct provably robust prediction sets against evasion attacks on test data and poisoning attacks on calibration data (both features and labels), achieving 2-10x set-size reductions over prior methods.

**3. Split Conformal Prediction under Data Contamination**
- **Authors:** Jase Clarkson, Wenkai Xu, Mihai Cucuringu, Yvik Swan, Gesine Reinert
- **Venue:** arXiv preprint (stat.ML)
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.07700
- **Summary:** Quantifies the impact of calibration data contamination on coverage and prediction set efficiency, and proposes Contamination Robust Conformal Prediction (CRCP) as an adjustment for classification that restores coverage guarantees under a small fraction of corrupted calibration scores.

---

### CATEGORY B: Adversarial Robustness (Test-Time Evasion Attacks)

**4. Verifiably Robust Conformal Prediction (VRCP)**
- **Authors:** Linus Jeary, Tom Kuipers, Mehran Hosseini, Nicola Paoletti
- **Venue:** NeurIPS 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2405.18942
- **Summary:** Leverages neural network verification to recover CP coverage guarantees under adversarial attacks; the first method supporting arbitrary norms (l1, l2, l-infinity) and both classification and regression tasks, outperforming randomized-smoothing baselines in prediction set efficiency.

**5. COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits**
- **Authors:** Mintong Kang, Nezihe Merve Gurel, Linyi Li, Bo Li
- **Venue:** ICLR 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.11348
- **Summary:** Combines data-driven learning with logic reasoning via probabilistic circuits to provide end-to-end certified coverage under l2-bounded adversarial perturbations, achieving up to 14% improvement in certified coverage on standard benchmarks (GTSRB, CIFAR-10, AwA2).

**6. Provably Robust Conformal Prediction with Improved Efficiency (RSCP+)**
- **Authors:** Ge Yan, Yaniv Romano, Tsui-Wei Weng
- **Venue:** arXiv preprint (cs.LG)
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2404.19651
- **Summary:** Fixes theoretical limitations in the original RSCP framework and introduces Post-Training Transformation and Robust Conformal Training techniques, achieving 4-17x efficiency improvements on CIFAR10/CIFAR100/ImageNet while maintaining provable robustness guarantees.

**7. Robust Conformal Prediction with a Single Binary Certificate**
- **Authors:** Soroush H. Zargarbashi, Aleksandar Bojchevski
- **Venue:** ICLR 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2503.05239
- **Summary:** Achieves adversarial robustness in CP by binarizing samples with an adjustable threshold, requiring only one binary certificate instead of certifying each calibration/test point individually -- reducing Monte Carlo samples from ~10,000 to ~150 on CIFAR10 while producing smaller prediction sets.

**8. Enhancing Adversarial Robustness with Conformal Prediction (OPSA / OPSA-AT)**
- **Authors:** Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, Zhixin Zhou
- **Venue:** arXiv preprint (cs.LG)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2506.07804
- **Summary:** Introduces OPSA (Optimal Size Attack) that maximizes model uncertainty to reduce CP efficiency at any significance level, and OPSA-AT, a defensive adversarial training strategy that significantly enhances robustness against OPSA and other attacks while maintaining reliable prediction.

**9. Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks**
- **Authors:** Xunlei Qian, Yue Xing
- **Venue:** AISTATS 2026 (submitted)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2511.18562
- **Summary:** Theoretically characterizes how adversarial perturbations at calibration time influence test-time coverage, showing coverage varies monotonically with calibration attack intensity, and demonstrates that appropriately chosen calibration-time attacks can maintain target coverage across a range of test-time perturbation levels.

**10. Verifiably Robust Conformal Prediction for Probabilistic Guarantees under Adversarial Attacks**
- **Authors:** (Jeary et al., extended version)
- **Venue:** Pattern Recognition (journal), 2025
- **Year:** 2025
- **URL:** https://www.sciencedirect.com/science/article/pii/S0031320325007113
- **Summary:** Journal extension of the NeurIPS 2024 VRCP paper with additional analysis and experiments on probabilistic guarantees under adversarial attacks.

---

### CATEGORY C: Distribution Shift

**11. Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations**
- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk
- **Venue:** arXiv preprint (stat.ML)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2502.14105
- **Summary:** Models distribution shifts via Levy-Prokhorov ambiguity sets, propagates them through scoring functions to reduce high-dimensional shifts to one-dimensional problems, enabling precise worst-case coverage quantification and robust conformal prediction intervals.

**12. Conformal Inference under High-Dimensional Covariate Shifts via Likelihood-Ratio Regularization (LR-QR)**
- **Authors:** Sunay Joshi, Shayan Kiyani, George Pappas, Edgar Dobriban, Hamed Hassani
- **Venue:** arXiv preprint (stat.ML)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2502.13030
- **Summary:** Proposes likelihood-ratio regularized quantile regression that avoids direct estimation of unknown likelihood ratios for conformal prediction under covariate shift, achieving valid marginal coverage in target domains on high-dimensional tasks including image classification (WILDS) and LLM QA (MMLU).

**13. Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift**
- **Authors:** Jungbin Jun, Ilsang Ohn
- **Venue:** arXiv preprint (stat.ML)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2511.04275
- **Summary:** Introduces retrospective adjustment of previous predictions using efficient leave-one-out update formulas in online conformal prediction, enabling faster coverage recalibration and improved statistical efficiency under distribution shift compared to forward-only approaches.

**14. Conformal Prediction for Time-series Forecasting with Change Points**
- **Authors:** Sophia Sun, Rose Yu
- **Venue:** arXiv preprint
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2509.02844
- **Summary:** Integrates a latent state prediction model with online conformal prediction to handle sudden distributional shifts (change points) in non-stationary time series, with theoretical validity guarantees and empirical improvements on six datasets.

---

### CATEGORY D: Exchangeability Violations

**15. Conformal Prediction Beyond Exchangeability**
- **Authors:** Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani
- **Venue:** Annals of Statistics, 2023
- **Year:** 2023 (foundational; still highly cited through 2025-2026)
- **URL:** https://arxiv.org/abs/2202.13415
- **Summary:** Foundational work extending CP using weighted quantiles and a novel randomization technique to handle distribution drift and asymmetric algorithms, quantifying coverage loss from exchangeability violations and recovering coverage guarantees under non-exchangeable settings.

**16. Predictive Inference for Time Series: Why is Split Conformal Effective Despite Temporal Dependence?**
- **Authors:** Rina Foygel Barber, Ashwin Pananjady
- **Venue:** arXiv preprint (stat.ML)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2510.02471
- **Summary:** Introduces a "switch coefficient" to measure exchangeability violations caused by temporal dependence, provides coverage bounds for split CP in time series including autoregressive predictors, and establishes sharp characterizations over stationary beta-mixing processes.

**17. Online Conformal Prediction: Enforcing Monotonicity via Online Optimization**
- **Authors:** Eduardo Ochoa Rivera, Ambuj Tewari
- **Venue:** arXiv preprint
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2605.12668
- **Summary:** Enforces nested (monotone) prediction sets across multiple confidence levels in online CP without exchangeability, using online optimization with small regret to achieve stable coverage across all levels with improved efficiency over existing online CP baselines.

---

### CATEGORY E: Label Noise / Corrupted Feedback

**18. Exploring the Noise Robustness of Online Conformal Prediction (NR-OCP)**
- **Authors:** Huajun Xi, Kangdao Liu, Hao Zeng, Wenguang Sun, Hongxin Wei
- **Venue:** NeurIPS 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2501.18363
- **Summary:** Shows that uniform label noise causes a persistent gap between actual and desired miscoverage rate in online CP, and proposes NR-OCP using a robust pinball loss that provides an unbiased estimate of clean pinball loss, achieving O(T^{-1/2}) convergence for coverage errors.

**19. Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting**
- **Authors:** Shai Feldman, Stephen Bates, Yaniv Romano
- **Venue:** arXiv preprint (cs.LG)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2505.04733
- **Summary:** Develops uncertain imputation (avoiding weight estimation by preserving label uncertainty) and a triply robust variant for conformal prediction with corrupted labels, providing coverage guarantees when at least one underlying component functions correctly.

**20. Conformal Prediction of Classifiers with Many Classes based on Noisy Labels (NACP)**
- **Authors:** Coby Penso, Jacob Goldberger, Ethan Fetaya
- **Venue:** COPA 2025 (PMLR vol. 26)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2501.12749
- **Summary:** Proposes Noise-Aware Conformal Prediction for estimating proper prediction thresholds under label corruption in multiclass settings, with finite-sample coverage guarantees for uniform noise that scale well to many classes.

**21. Online Conformal Prediction with Corrupted Feedback**
- **Authors:** Bowen Wang, Matteo Zecchin, Osvaldo Simeone
- **Venue:** arXiv preprint (cs.LG)
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2605.20515
- **Summary:** Addresses online CP when feedback is corrupted through noise, communication failures, or adversarial interference; proposes structural filtering and active compensation mechanisms with explicit miscoverage guarantees under both stochastic and adversarial error models.

---

### CATEGORY F: Federated / Distributed Robustness

**22. Certifiably Byzantine-Robust Federated Conformal Prediction (Rob-FCP)**
- **Authors:** Mintong Kang, Zhen Lin, Jimeng Sun, Cao Xiao, Bo Li
- **Venue:** ICML 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2406.01960
- **Summary:** Introduces Rob-FCP for federated conformal prediction that maintains coverage guarantees despite Byzantine (arbitrarily malicious) clients, with theoretical proof that coverage is asymptotically close to the desired level and a method to estimate the number of malicious clients when unknown.

---

This survey covers 22 papers across six threat categories. The field is rapidly developing, with the core tension being between **robustness** (maintaining coverage guarantees under adversarial conditions) and **efficiency** (keeping prediction sets small enough to be informative). Key trends include: (1) moving from randomized smoothing to neural network verification for tighter certified sets; (2) addressing calibration-time vs. training-time vs. test-time threats separately and jointly; (3) extending robustness to online/streaming and federated settings; and (4) handling label noise as a specific form of data corruption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "510d23b7-3097-4b37-98aa-c6233626a584",
  "isSidechain": true,
  "agentId": "adbfc87c1aba5efc3",
  "requestId": "req_011CbYGBiEMZS1HSN12bdFcH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50a1ac5b-a037-4d27-9ac0-50bc7eab1562",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199XUykePi82cSbEMBPsXXx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 25577,
      "output_tokens": 3675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3675,
          "cache_read_input_tokens": 25577,
          "cache_creation_input_tokens": 1717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1717,
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
