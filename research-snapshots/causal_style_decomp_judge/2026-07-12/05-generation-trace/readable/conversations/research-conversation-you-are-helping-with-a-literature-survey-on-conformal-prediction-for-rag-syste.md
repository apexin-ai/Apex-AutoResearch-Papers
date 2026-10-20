# Research conversation: You are helping with a literature survey on conformal prediction for RAG systems. Search for and analyze papers from 202

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a38362145d53a1294.jsonl`
- **Structured JSON:** [`847202d144770c58ad68.json`](../../sessions/84/847202d144770c58ad68.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-30T06:12:49.813Z_

You are helping with a literature survey on conformal prediction for RAG systems. Search for and analyze papers from 2024-2026.

Execute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:

1. Search: "conformal prediction retrieval augmented generation 2024 2025 2026"
2. Search: "TRAQ conformal prediction RAG trustworthy"
3. Search: "C-RAG certified generation risks retrieval augmented language models"
4. Search: "conformal prediction LLM factuality 2025 2026"
5. Search: "conformal prediction natural language generation abstention"

For each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.

Return a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers that combine conformal prediction with RAG or LLM systems.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "b1ba3c90-17f1-4a99-bb4a-5a323a5fbff9",
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

_source line 2 · 2026-05-30T06:12:49.818Z_

```json
{
  "parentUuid": "b1ba3c90-17f1-4a99-bb4a-5a323a5fbff9",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
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
  "uuid": "2ca7263b-a3de-4f41-b55e-52e609ad534b",
  "timestamp": "2026-05-30T06:12:49.818Z",
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

_source line 3 · 2026-05-30T06:12:49.819Z_

```json
{
  "parentUuid": "2ca7263b-a3de-4f41-b55e-52e609ad534b",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0bd81830-eca3-4edd-a789-0bce8f7f02c2",
  "timestamp": "2026-05-30T06:12:49.819Z",
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

_source line 4 · 2026-05-30T06:12:52.869Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd81830-eca3-4edd-a789-0bce8f7f02c2",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1ZtXS7tNLPpwUpFA2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ad167c5-d98c-41e5-b0d6-b325d9afd201",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLF5F3wudgywdp5qMRaDKx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8977,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8977,
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

_source line 5 · 2026-05-30T06:12:53.525Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NRgbSFC1HiPx8zKKFv6TB8`</summary>

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
  "parentUuid": "3ad167c5-d98c-41e5-b0d6-b325d9afd201",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1ZtXS7tNLPpwUpFA2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3ccccfb-7428-407c-8e55-b9b251ad6be8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLF5F3wudgywdp5qMRaDKx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8977,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8977,
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

_source line 6 · 2026-05-30T06:12:53.535Z_

<details><summary>↩ Tool result · `toolu_01NRgbSFC1HiPx8zKKFv6TB8`</summary>

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
  "parentUuid": "f3ccccfb-7428-407c-8e55-b9b251ad6be8",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "7f8bc8d5-a63a-4fa2-bf9c-2c10d632e52f",
  "sourceToolAssistantUUID": "f3ccccfb-7428-407c-8e55-b9b251ad6be8",
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

_source line 7 · 2026-05-30T06:12:56.011Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f8bc8d5-a63a-4fa2-bf9c-2c10d632e52f",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1rKFPqciWffKSYvJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3758f6b-ff68-45cd-9858-b4bba35d4af2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9cX1uxpsrpZfcBMtbzycZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 8 · 2026-05-30T06:12:56.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mg7amz2MushL683tiU542g`</summary>

```json
{
  "query": "conformal prediction retrieval augmented generation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3758f6b-ff68-45cd-9858-b4bba35d4af2",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1rKFPqciWffKSYvJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddf6be61-f3c0-47d6-be93-35f0b665d59d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9cX1uxpsrpZfcBMtbzycZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 9 · 2026-05-30T06:12:57.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MYvKukyUaGHUcW3D6NQvix`</summary>

```json
{
  "query": "TRAQ conformal prediction RAG trustworthy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddf6be61-f3c0-47d6-be93-35f0b665d59d",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1rKFPqciWffKSYvJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a2680c7-af68-4bc7-a27f-094cfaa7dfc7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9cX1uxpsrpZfcBMtbzycZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 10 · 2026-05-30T06:12:57.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRoFfjYSTCL3Zx1kzwABhV`</summary>

```json
{
  "query": "C-RAG certified generation risks retrieval augmented language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a2680c7-af68-4bc7-a27f-094cfaa7dfc7",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1rKFPqciWffKSYvJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf24ed02-0f73-45f7-a839-c8ed5d97305a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9cX1uxpsrpZfcBMtbzycZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 11 · 2026-05-30T06:12:58.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014egE5LarbM4bNGuUThFrKZ`</summary>

```json
{
  "query": "conformal prediction LLM factuality 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf24ed02-0f73-45f7-a839-c8ed5d97305a",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1rKFPqciWffKSYvJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a123b8a2-71bc-44cc-8b8a-585bc889e1c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9cX1uxpsrpZfcBMtbzycZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8977,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 8977,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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

_source line 12 · 2026-05-30T06:12:58.841Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FJkmr8vfUcNCU7XAqdsHzw`</summary>

```json
{
  "query": "conformal prediction natural language generation abstention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a123b8a2-71bc-44cc-8b8a-585bc889e1c7",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG1rKFPqciWffKSYvJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "711e03e5-ef72-4d46-966d-eeede44fba2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9cX1uxpsrpZfcBMtbzycZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8977,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 8977,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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

_source line 13 · 2026-05-30T06:13:03.635Z_

<details><summary>↩ Tool result · `toolu_01MYvKukyUaGHUcW3D6NQvix`</summary>

```text
Web search results for query: "TRAQ conformal prediction RAG trustworthy"

Links: [{"title":"[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/abs/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/28e078b52a761cf3fe5941d3428acb7bbf608f21"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=N-FM_cf9BBXM"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"}]

Here are the search results for "TRAQ conformal prediction RAG trustworthy":

## Overview

TRAQ (Trustworthy Retrieval Augmented Question Answering) provides the first end-to-end statistical correctness guarantee for RAG.

## The Problem It Addresses

Large language models frequently generate incorrect responses based on made-up facts (hallucinations), and while Retrieval Augmented Generation is a promising strategy to avoid hallucinations, it does not provide guarantees on its correctness.

## How It Works

TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.

TRAQ introduces a novel nonconformity measure based on semantic uncertainty, clustering semantically equivalent answers and measuring uncertainty by the number of non-equivalent clusters.

## Results

In experimental evaluation, TRAQ provides the desired correctness guarantee while reducing prediction set size by 16.2% on average compared to an ablation.

The paper was published at NAACL 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a2680c7-af68-4bc7-a27f-094cfaa7dfc7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "b030ed34-a045-4f06-97ba-4994f9c668a9",
  "sourceToolAssistantUUID": "8a2680c7-af68-4bc7-a27f-094cfaa7dfc7",
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

_source line 14 · 2026-05-30T06:13:03.816Z_

<details><summary>↩ Tool result · `toolu_01KRoFfjYSTCL3Zx1kzwABhV`</summary>

```text
Web search results for query: "C-RAG certified generation risks retrieval augmented language models"

Links: [{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240203181K/abstract"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models","url":"https://arxiv.org/pdf/2402.03181"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://proceedings.mlr.press/v235/kang24a.html"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/c-rag-certified-generation-risks-retrieval-augmented"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2402.03181v5"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/c-rag-certified-generation-risks-for-retrieval-augmented-language/"},{"title":"[2402.03181] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2402.03181"}]

Based on the search results, here's what I found about C-RAG:

## Overview

C-RAG is the first framework to certify generation risks for RAG models. The research addresses a key gap in understanding how retrieval-augmented language models (RAG) handle trustworthiness issues.

## The Problem

Despite the impressive capabilities of large language models, they still suffer from trustworthiness issues such as hallucinations and misalignments, and while retrieval-augmented language models have been proposed to enhance the credibility of generations by grounding external knowledge, the theoretical understandings of their generation risks remains unexplored.

## The Approach

The framework provides conformal risk analysis for RAG models and certifies an upper confidence bound of generation risks (called conformal generation risk), and also provides theoretical guarantees on conformal generation risks for general bounded risk functions under test distribution shifts.

## Key Findings

RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial. Additionally, intensive empirical results demonstrate the soundness and tightness of the conformal generation risk guarantees across four widely-used NLP datasets on four state-of-the-art retrieval models.

The research was published in the Proceedings of the 41st International Conference on Machine Learning in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf24ed02-0f73-45f7-a839-c8ed5d97305a",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "323e2e65-1226-454a-bc6f-5247b1f2ca11",
  "sourceToolAssistantUUID": "cf24ed02-0f73-45f7-a839-c8ed5d97305a",
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

_source line 15 · 2026-05-30T06:13:04.723Z_

<details><summary>↩ Tool result · `toolu_01Mg7amz2MushL683tiU542g`</summary>

```text
Web search results for query: "conformal prediction retrieval augmented generation 2024 2025 2026"

Links: [{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730244"},{"title":"Towards Trustworthy Retrieval Augmented Generation for ...","url":"https://arxiv.org/pdf/2502.06872"},{"title":"Conformal Prediction in the Age of Multimodal Foundation Models: A Survey | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-15120-9_13"},{"title":"RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium","url":"https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"CONFLARE: CONFormal LArge language model REtrieval","url":"https://arxiv.org/pdf/2404.04287"},{"title":"Enhancing RAG and Knowledge Graphs with Discourse Boris Galitsky","url":"https://dialogue-conf.org/wp-content/uploads/2025/04/GalitskyBIlvovskyDMorkovkinA.110.pdf"}]

Based on the search results, here's what I found on conformal prediction and retrieval augmented generation from 2024-2026:

## Recent Research Developments

Existing research in Retrieval-Augmented Generation (RAG) mostly focuses on improving overall question-answering accuracy, but often overlooks the quality of sub-claims within generated responses.

### Key Applications and Methods

Conformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees in RAG systems. Several frameworks have emerged:

1. **Conformal-RAG**: By leveraging information from the RAG system, Conformal-RAG retains up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee.

2. **TRAQ (Trustworthy Retrieval Augmented Question Answering)**: TRAQ expanded the conformal prediction framework to include a Bayesian optimization module that minimizes the prediction set during the multi-step calibration. By leveraging Bayesian optimization, the framework efficiently searches for the optimal parameters that reduce the size of the prediction set while maintaining the desired confidence level. TRAQ ensures that the retrieval process remains both accurate and computationally feasible, enhancing the overall reliability and performance of RAG systems.

3. **CONFLARE**: Recent work has focused on conformal prediction, which introduces a straightforward approach to uncertainty quantification, providing uncertainty levels with statistical guarantees. For any given input, conformal prediction estimates a prediction interval in regression tasks and a set of classes in classification tasks. These estimates are guaranteed to encompass the ground-truth value with a probability defined by the user.

Recent innovations span generative modeling, predictive pipelines, reasoning and control, and retrieval-augmented generation, highlighting techniques such as sampling-aware calibration, trust-score conditioning and input-adaptive error control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddf6be61-f3c0-47d6-be93-35f0b665d59d",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "c5afc2fb-d2f1-4419-9980-e2e976e99af2",
  "sourceToolAssistantUUID": "ddf6be61-f3c0-47d6-be93-35f0b665d59d",
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

_source line 16 · 2026-05-30T06:13:06.141Z_

<details><summary>↩ Tool result · `toolu_01FJkmr8vfUcNCU7XAqdsHzw`</summary>

```text
Web search results for query: "conformal prediction natural language generation abstention"

Links: [{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"[2604.27914] Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/abs/2604.27914"},{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/html/2502.19110v4"},{"title":"Conformal Prediction Sets for Deep Generative Models via Reduction to Conformal Regression","url":"https://arxiv.org/html/2503.10512v2"},{"title":"ConU: Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees","url":"https://arxiv.org/html/2407.00499v1"},{"title":"Conformal Language Modeling","url":"https://axi.lims.ac.uk/paper/2306.10193"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/html/2502.06884v1"}]

Based on the search results, here's what I found about conformal prediction, natural language generation, and abstention:

## Overview

Conformal abstention (CA) is a post-hoc framework adapted from conformal prediction (CP) to determine whether to abstain from answering a query. CA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct.

## Key Applications and Challenges

When language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Conformal prediction offers a potential solution to this problem.

The application of CP to language generation faces two big challenges: (i) the combinatorially large size of output sets and (ii) the conditional (recursive) nature of language generation, which violates the exchangeability assumption underlying standard CP.

## Recent Developments

Recent research has explored various approaches:

- Yadkori et al. (2024) use conformal risk control to obtain an upper bound on the hallucination risk, developing an abstention procedure.

- The conformalized abstention policy (CAP) allows three possible outcomes per query: a single prediction, a set of plausible predictions, or abstention, balancing informativeness and risk based on prediction confidence.

- Linguistic calibration can be seen as a form of soft abstention, whereas traditional abstention corresponds to committing to the universal set of all possible worlds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "711e03e5-ef72-4d46-966d-eeede44fba2d",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "a020a53d-16f4-4d2b-b18c-2ddf639d638b",
  "sourceToolAssistantUUID": "711e03e5-ef72-4d46-966d-eeede44fba2d",
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

_source line 17 · 2026-05-30T06:13:07.813Z_

<details><summary>↩ Tool result · `toolu_014egE5LarbM4bNGuUThFrKZ`</summary>

```text
Web search results for query: "conformal prediction LLM factuality 2025 2026"

Links: [{"title":"[2604.13991] Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/abs/2604.13991"},{"title":"Differentiable Conformal Training for LLM Reasoning Factuality","url":"https://arxiv.org/pdf/2604.20098"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217v1"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://www.researchgate.net/publication/397200904_Large_language_model_validity_via_enhanced_conformal_prediction_methods"},{"title":"Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/html/2604.13991"},{"title":"Conformal Language Model Reasoning with Coherent Factuality","url":"https://arxiv.org/pdf/2505.17126"},{"title":"Language Models with Conformal Factuality Guarantees","url":"https://arxiv.org/pdf/2402.10978"}]

I've completed the web search for "conformal prediction LLM factuality 2025 2026". Here's a summary of the recent research in this area:

## Key Findings

Conformal prediction is being used as a distribution-free method for constructing prediction sets with guaranteed error rates to provide statistical factuality guarantees for LLMs.

### Recent Developments

Several important papers from 2025-2026 have advanced this field:

1. **Adaptive Conformal Prediction**: Recent work shows approaches that significantly outperform existing baselines in terms of conditional coverage.

2. **Differentiable Conformal Training**: Conformal factuality methods decompose LLM outputs into atomic claims and filter based on calibrated risk thresholds. More recent work has extended conformal prediction to multi-step reasoning through approximate deducibility graphs.

3. **RAG-Based LLMs**: Research integrates conformal factuality filtering with retrieval-augmented generation and introduces new factuality metrics, showing that standard measures miss key trade-offs between correctness and informativeness.

4. **Robust Conformal Prediction**: These approaches have been adapted to LLMs and language generation, from early work on closed-ended QA to open-ended generation and correctness-oriented uncertainty sets for free-form QA.

### Core Motivation

Despite LLMs' impressive performance, they are still susceptible to hallucinations, producing fluent but factually incorrect outputs. Conformal prediction methods aim to address this by providing statistical guarantees for factuality while maintaining model usefulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a123b8a2-71bc-44cc-8b8a-585bc889e1c7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "f280849a-3a3c-4abe-aa01-e1dfd58057f4",
  "sourceToolAssistantUUID": "a123b8a2-71bc-44cc-8b8a-585bc889e1c7",
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

_source line 18 · 2026-05-30T06:13:11.127Z_

Excellent. Now let me fetch the abstracts from the key papers identified. I'll fetch them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f280849a-3a3c-4abe-aa01-e1dfd58057f4",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6993d9a2-d556-4054-8bdf-f177a797900c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 19 · 2026-05-30T06:13:12.084Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VUZMsxXZUyGLQDpPYNusA5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2307.04642",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6993d9a2-d556-4054-8bdf-f177a797900c",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b9245f4-b5b2-449f-b15a-c5066549d571",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 20 · 2026-05-30T06:13:13.065Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JfLkDMydHkPDNyAxDvkRpF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.03181",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b9245f4-b5b2-449f-b15a-c5066549d571",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e9b15e5-e353-481f-99dd-c5e306c2fc82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 21 · 2026-05-30T06:13:14.017Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RxGX8pn55KDk1SEM3qW3xq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.04287",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. CONFLARE conformal large language model retrieval."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e9b15e5-e353-481f-99dd-c5e306c2fc82",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8e2faf0-9b51-4318-a91e-d8869a6a4fd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 22 · 2026-05-30T06:13:14.967Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QP7nsapVNqFQjZHFAT7vqe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.10978",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Language models with conformal factuality guarantees."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e2faf0-9b51-4318-a91e-d8869a6a4fd7",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41dd2b1c-d2dd-46e1-b17e-b53404c05000",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 23 · 2026-05-30T06:13:15.903Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q7fgtj6rUdjYTiC81o11Me`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13991",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Adaptive conformal prediction factuality LLM."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41dd2b1c-d2dd-46e1-b17e-b53404c05000",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "983ac98a-8b73-454d-8619-257213102dbc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 24 · 2026-05-30T06:13:16.052Z_

<details><summary>↩ Tool result · `toolu_01VUZMsxXZUyGLQDpPYNusA5`</summary>

```text
# TRAQ Paper Details

**Full Title:** "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction"

**Authors:**
- Shuo Li
- Sangdon Park
- Insup Lee
- Osbert Bastani

**Publication Date:** Submitted July 7, 2023; last revised April 5, 2024

**Abstract:**

The paper addresses a significant challenge with large language models in open-domain question answering: their tendency to produce fabricated information. The researchers propose TRAQ, which delivers "the first end-to-end statistical correctness guarantee for RAG." The method employs conformal prediction to construct sets of responses guaranteed to contain semantically correct answers with high probability. Additionally, it uses Bayesian optimization to reduce prediction set sizes. Experimental results demonstrate the approach achieves the desired correctness guarantee while reducing average prediction set size by 16.2% compared to baseline ablations. The implementation is publicly available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b9245f4-b5b2-449f-b15a-c5066549d571",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "7c2ab851-b75f-4572-8abc-7b4d36e6a384",
  "sourceToolAssistantUUID": "6b9245f4-b5b2-449f-b15a-c5066549d571",
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

_source line 25 · 2026-05-30T06:13:16.847Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016ZAjpmA3miDUzXGD2apbgX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.20098",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Differentiable conformal training LLM reasoning factuality."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c2ab851-b75f-4572-8abc-7b4d36e6a384",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ac9433e-9473-4cf3-9666-5ad7c5778c03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 26 · 2026-05-30T06:13:17.046Z_

<details><summary>↩ Tool result · `toolu_01JfLkDMydHkPDNyAxDvkRpF`</summary>

```text
# C-RAG Paper Details

**Full Title:**
"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models"

**Authors:**
Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, and Bo Li

**Publication Date:**
Submitted February 5, 2024; accepted to ICML 2024; final version July 30, 2024

**Abstract:**
The researchers address trustworthiness challenges in large language models, particularly "hallucinations and misalignments." They present C-RAG, a framework providing "conformal risk analysis for RAG models and certif[ying] an upper confidence bound of generation risks." The work establishes that retrieval-augmented approaches can achieve lower risk than standalone language models when retrieval and transformer quality are sufficient. Their findings are validated across four NLP datasets using multiple state-of-the-art retrieval systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e9b15e5-e353-481f-99dd-c5e306c2fc82",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "c261d339-71d8-41f1-9626-a83a9853f045",
  "sourceToolAssistantUUID": "8e9b15e5-e353-481f-99dd-c5e306c2fc82",
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

_source line 27 · 2026-05-30T06:13:18.257Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MKESvSZWU1zTbz7cYHk5Eh`</summary>

```json
{
  "url": "https://openreview.net/forum?id=OKnM5rEUbg",
  "prompt": "Extract the full title, all authors, venue, and the complete abstract of this paper. Understanding conformal factuality RAG-based LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c261d339-71d8-41f1-9626-a83a9853f045",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c125642-ba26-4f46-bc40-0a7b01b84c67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3530,
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

_source line 28 · 2026-05-30T06:13:18.935Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NyqVLvfYZL45e1CkshwQfo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.27914",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Geometry-calibrated conformal abstention language models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c125642-ba26-4f46-bc40-0a7b01b84c67",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG2tfuTsbCyhNhK9MzV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72d30b9a-b9ff-4864-970a-c626330bcb20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TDEE5vkjBX5ATGCmt46Wm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 769,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 10099,
      "output_tokens": 783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 769,
          "output_tokens": 783,
          "cache_read_input_tokens": 10099,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3530,
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

_source line 29 · 2026-05-30T06:13:19.325Z_

<details><summary>↩ Tool result · `toolu_01RxGX8pn55KDk1SEM3qW3xq`</summary>

```text
# CONFLARE Paper Details

**Full Title:** "CONFLARE: CONFormal LArge language model REtrieval"

**Authors:**
- Pouria Rouzrokh
- Shahriar Faghani
- Cooper U. Gamble
- Moein Shariatnia
- Bradley J. Erickson

**Publication Date:** April 4, 2024

**Abstract:**

The research addresses a critical vulnerability in retrieval-augmented generation (RAG) systems: "RAG does not guarantee valid responses if retrieval fails to identify the necessary information." The authors propose applying conformal prediction to quantify uncertainty in the retrieval process through a four-step framework.

The methodology involves creating a calibration dataset, comparing question embeddings against document embeddings to identify relevant chunks and record similarity scores, then analyzing these scores to establish a threshold based on a user-specified error rate (α). During inference, all chunks exceeding this similarity threshold are retrieved as context, theoretically ensuring the true answer appears with (1-α) confidence. The team provides a Python implementation requiring only LLMs without human intervention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8e2faf0-9b51-4318-a91e-d8869a6a4fd7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "15503f00-8e9b-4368-9548-fba770a08949",
  "sourceToolAssistantUUID": "c8e2faf0-9b51-4318-a91e-d8869a6a4fd7",
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

_source line 30 · 2026-05-30T06:13:19.348Z_

<details><summary>↩ Tool result · `toolu_01QP7nsapVNqFQjZHFAT7vqe`</summary>

```text
# Paper Information

**Title:** "Language Models with Conformal Factuality Guarantees"

**Authors:** Christopher Mohri, Tatsunori Hashimoto

**Publication Date:** February 15, 2024 (submitted)

**Abstract:**

The researchers propose conformal factuality, which merges language modeling with conformal prediction to provide high-probability correctness guarantees for LM outputs. They frame output correctness as an uncertainty quantification challenge, where uncertainty sets align with what an LM's output logically entails. The method functions as a progressive back-off algorithm that makes outputs progressively less specific to expand uncertainty sets and ensure correctness. It works with any black-box language model and requires minimal human annotation. Testing on closed-book QA benchmarks and mathematical reasoning tasks demonstrated the approach could deliver "80-90% correctness guarantees while retaining the majority of the LM's original output."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41dd2b1c-d2dd-46e1-b17e-b53404c05000",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "552b7a0c-a908-4a0e-8047-7ae5eae367ae",
  "sourceToolAssistantUUID": "41dd2b1c-d2dd-46e1-b17e-b53404c05000",
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

_source line 31 · 2026-05-30T06:13:20.275Z_

<details><summary>↩ Tool result · `toolu_01Q7fgtj6rUdjYTiC81o11Me`</summary>

```text
# Paper Summary

**Title:** "Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models"

**Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, Maxim Panov

**Publication Date:** April 15, 2026 (arXiv submission)

**Abstract:**
The researchers address how large language models frequently produce factually incorrect content. Their work introduces an adaptive conformal prediction methodology that "extends conformal score transformation methods to LLMs, with applications to long-form generation and multiple-choice question answering." Unlike previous approaches, this technique enables "prompt-dependent calibration, retaining marginal coverage guarantees while improving conditional coverage." The method supports selective prediction capabilities, allowing unreliable information to be filtered during downstream use. Testing across multiple white-box models demonstrated significant improvements in conditional coverage compared to existing alternatives.

**Key Innovation:** The approach is prompt-adaptive rather than one-size-fits-all, better capturing how reliability varies across different inputs and tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "983ac98a-8b73-454d-8619-257213102dbc",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "a230a386-820b-4f2e-b006-fa07568335a5",
  "sourceToolAssistantUUID": "983ac98a-8b73-454d-8619-257213102dbc",
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

_source line 32 · 2026-05-30T06:13:20.370Z_

<details><summary>↩ Tool result · `toolu_016ZAjpmA3miDUzXGD2apbgX`</summary>

```text
# Paper Details

**Full Title:** "Differentiable Conformal Training for LLM Reasoning Factuality"

**Authors:** Nathan Hittesdorf, Marco Salzetta, Lu Cheng

**Publication Date:** Submitted April 22, 2026

**Abstract Summary:**

The research addresses hallucination problems in large language models through a novel approach. The authors explain that "Conformal Prediction (CP) addresses this by calibrating error rates on held-out data to provide statistically valid confidence guarantees." Their key innovation, Differentiable Coherent Factuality (DCF), improves upon existing methods by making the system fully differentiable.

The method enables learning better scoring mechanisms while maintaining reliability assurances. According to the abstract, their approach "achieves up to 141% improvement in claim retention while maintaining reliability guarantees," representing meaningful progress toward dependable conformal systems for language model outputs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac9433e-9473-4cf3-9666-5ad7c5778c03",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "52fb69fe-4d66-44dc-b12e-c9cba6cf813b",
  "sourceToolAssistantUUID": "5ac9433e-9473-4cf3-9666-5ad7c5778c03",
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

_source line 33 · 2026-05-30T06:13:22.823Z_

<details><summary>↩ Tool result · `toolu_01NyqVLvfYZL45e1CkshwQfo`</summary>

```text
# Paper Information

**Full Title:** Geometry-Calibrated Conformal Abstention for Language Models

**Authors:** Rui Xu, Yi Chen, Sihong Xie, Hui Xiong

**Publication Date:** April 30, 2026 (submitted)

**Complete Abstract:**

The research addresses how language models frequently produce plausible but inaccurate responses when lacking relevant knowledge, rather than acknowledging uncertainty. The team proposes a post hoc framework called Conformal Abstention (CA), drawing from conformal prediction methodology, to determine when a model should decline answering. This approach offers finite-sample guarantees regarding both participation probability and response correctness likelihood.

A key innovation involves using prediction confidence instead of non-conformity scores, which are impractical for open-ended generation tasks. The authors introduce a calibration method leveraging representation geometry to assess how much the model's actual knowledge contributes to its response. Their experimental results demonstrate "75 percent conditional correctness" when implementing selective answering strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72d30b9a-b9ff-4864-970a-c626330bcb20",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "ac96f19a-52a4-43c3-b330-ac5152336c62",
  "sourceToolAssistantUUID": "72d30b9a-b9ff-4864-970a-c626330bcb20",
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

_source line 34 · 2026-05-30T06:13:23.148Z_

<details><summary>↩ Tool result · `toolu_01MKESvSZWU1zTbz7cYHk5Eh`</summary>

```text
# Paper Details

**Title:** "Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights"

**Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak

**Venue:** ICLR 2026 Conference

**Abstract Summary:**

The research addresses how to reduce "hallucinations" in large language models by combining two techniques. The authors unite conformal factuality filtering (which offers statistical guarantees) with retrieval-augmented generation (which uses trusted knowledge bases). 

Key contributions include investigating components like reference sources and scoring functions, plus introducing three novel evaluation metrics: non-empty rate, non-vacuous empirical factuality, and sufficient correctness. The team conducted experiments across three datasets and multiple model sizes.

The findings reveal that "standard metrics fail to capture" meaningful trade-offs between accuracy and usefulness, demonstrating the need to reconsider how we evaluate factual correctness in LLM outputs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c125642-ba26-4f46-bc40-0a7b01b84c67",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "12981ae3-2c13-4f46-aaa2-50edf0d9026d",
  "sourceToolAssistantUUID": "6c125642-ba26-4f46-bc40-0a7b01b84c67",
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

_source line 35 · 2026-05-30T06:13:25.241Z_

Now let me fetch a few more papers that appeared in the results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12981ae3-2c13-4f46-aaa2-50edf0d9026d",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3ed5cd1-4ec7-45be-972c-bb09be5b50ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 36 · 2026-05-30T06:13:27.188Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X9NnZPS1dBwPhf2DrBE2Qs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19110",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Conformal linguistic calibration factuality specificity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3ed5cd1-4ec7-45be-972c-bb09be5b50ac",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a6d5645-023f-49be-872d-f85e980857da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 37 · 2026-05-30T06:13:28.129Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JVozKFRMoiZq3r3VaEwR3T`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.00499",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. ConU conformal uncertainty large language models correctness coverage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a6d5645-023f-49be-872d-f85e980857da",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c30606f4-b240-416d-8a6b-5de0ee144389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 38 · 2026-05-30T06:13:29.540Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RQe7ZcbeJ518GGPbM4VCNy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06884",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Learning conformal abstention policies adaptive risk management LLM."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c30606f4-b240-416d-8a6b-5de0ee144389",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "037fdbc1-9eef-4757-8fb7-6cd153aba2a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 39 · 2026-05-30T06:13:30.479Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KZyanzu1JpfmJtLH2KnmpR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.17126",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Conformal language model reasoning coherent factuality."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "037fdbc1-9eef-4757-8fb7-6cd153aba2a1",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "439cdd5f-9fd9-4490-96d4-cf365b0c7500",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 40 · 2026-05-30T06:13:31.429Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EVbxRUSDrAZ8RyihPDwHT5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.16217",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Beyond surface statistics robust conformal prediction LLMs internal representations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "439cdd5f-9fd9-4490-96d4-cf365b0c7500",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2fd091e-c7c6-4fe1-91db-0a8bd4396d6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

### Tool result

_source line 41 · 2026-05-30T06:13:31.834Z_

<details><summary>↩ Tool result · `toolu_01X9NnZPS1dBwPhf2DrBE2Qs`</summary>

```text
# Paper Information

**Title:** "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity"

**Authors:** Zhengping Jiang, Anqi Liu, Benjamin Van Durme

**Publication Date:** Submitted February 26, 2025; last revised August 11, 2025 (version 4)

**Abstract:**

The researchers address reliability issues in language model outputs by proposing a method called Conformal Linguistic Calibration (CLC). This approach reinterprets linguistic calibration as answer set prediction, connecting abstention (withholding responses) and linguistic calibration (hedging statements with uncertainty markers) through pragmatics principles.

Their framework enables controlled imprecision levels in model responses while maintaining "conformal guarantees on factual accuracy." The method allows fine-tuning models to perform uncertainty-aware adaptive claim rewriting, creating "a controllable balance between factuality and specificity." This addresses limitations of existing approaches: abstention loses valuable information, while calibrated responses prove difficult to use in downstream applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a6d5645-023f-49be-872d-f85e980857da",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "87047c4e-b945-4d78-8509-a90f0a456799",
  "sourceToolAssistantUUID": "0a6d5645-023f-49be-872d-f85e980857da",
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

_source line 42 · 2026-05-30T06:13:32.814Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JQKW1SrKQEsqaFkjzpfDbk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.20978",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Response quality assessment retrieval augmented generation conditional conformal factuality."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87047c4e-b945-4d78-8509-a90f0a456799",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6a2d5f8-56f9-4cdf-b81f-85db495c2620",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

### Tool result

_source line 43 · 2026-05-30T06:13:32.836Z_

<details><summary>↩ Tool result · `toolu_01JVozKFRMoiZq3r3VaEwR3T`</summary>

```text
# Paper Details: ConU

**Full Title:** "ConU: Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees"

**Authors:** Zhiyuan Wang, Jinhao Duan, Lu Cheng, Yue Zhang, Qingni Wang, Xiaoshuang Shi, Kaidi Xu, Hengtao Shen, Xiaofeng Zhu

**Publication Date:** November 18, 2024 (v3); originally submitted June 29, 2024

**Abstract Summary:**
The research addresses uncertainty quantification in natural language generation using black-box LLMs. The team introduces "a novel uncertainty measure based on self-consistency theory" and develops a conformal uncertainty criterion integrated with correctness alignment. Testing across 7 popular LLMs and 4 datasets spanning general and medical domains, the method achieves "strict control over the correctness coverage rate." The approach generates calibrated prediction sets that balance both rigor and practical efficiency for open-ended generation tasks.

**Status:** Accepted by EMNLP 2024 Findings
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c30606f4-b240-416d-8a6b-5de0ee144389",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "1f525021-f959-49df-a494-384927569621",
  "sourceToolAssistantUUID": "c30606f4-b240-416d-8a6b-5de0ee144389",
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

_source line 44 · 2026-05-30T06:13:33.417Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015gyKphx23eGjAwQQCL4kya`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06872",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Towards trustworthy retrieval augmented generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f525021-f959-49df-a494-384927569621",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG42N3M89169mZh656a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a95574bd-520b-4400-a1c9-243569e6c18f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GHnFscR3uUU9og9bEQkDP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 256,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 13629,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 256,
          "output_tokens": 698,
          "cache_read_input_tokens": 13629,
          "cache_creation_input_tokens": 3391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3391,
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

_source line 45 · 2026-05-30T06:13:34.162Z_

<details><summary>↩ Tool result · `toolu_01RQe7ZcbeJ518GGPbM4VCNy`</summary>

```text
# Paper Summary

**Full Title:** "Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models"

**Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, and Amit Ranjan Trivedi

**Publication Date:** February 8, 2025

**Complete Abstract:**

The research addresses reliability challenges in LLMs and VLMs by combining reinforcement learning with conformal prediction. Rather than using fixed uncertainty thresholds, the team developed a method to dynamically optimize decision boundaries. 

Their approach treats prediction thresholds as learnable parameters, balancing competing goals like reducing prediction set size while preserving statistical coverage guarantees. Testing across multiple models and datasets demonstrated notable improvements: accuracy gains up to 3.2%, hallucination detection AUROC improvements of 22.19%, uncertainty-guided generation metrics enhanced by 21.17%, and calibration error reductions between 70-85%. The method consistently achieved the 90% coverage target while outperforming comparison baselines like Least Ambiguous Classifiers and Adaptive Prediction Sets, offering a more flexible solution for safety-critical deployment scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "037fdbc1-9eef-4757-8fb7-6cd153aba2a1",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "9ca80b93-f448-416e-9c42-4bc9ff815d84",
  "sourceToolAssistantUUID": "037fdbc1-9eef-4757-8fb7-6cd153aba2a1",
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

_source line 46 · 2026-05-30T06:13:34.906Z_

<details><summary>↩ Tool result · `toolu_01KZyanzu1JpfmJtLH2KnmpR`</summary>

```text
# Paper Summary

**Title:** "Conformal Language Model Reasoning with Coherent Factuality"

**Authors:** Maxon Rubin-Toles, Maya Gambhir, Keshav Ramji, Aaron Roth, Surbhi Goel

**Publication Date:** Submitted May 21, 2025

**Abstract:**

The researchers address a critical challenge in deploying language models for decision-making: ensuring output reliability. While existing approaches evaluate isolated claims for factuality, they fall short for logical reasoning tasks where each step depends on preceding ones. 

The team introduces "coherent factuality"—a framework that considers claims within their logical context. Their solution employs split conformal prediction on "deducibility graphs" that map reasoning steps. Testing on mathematical datasets (MATH and FELM), the method maintains consistent correctness across coverage targets, achieving "90% factuality on our stricter definition while retaining 80% or more of the original claims," demonstrating the effectiveness of their graph-guided strategy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "439cdd5f-9fd9-4490-96d4-cf365b0c7500",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "8dce765e-bd85-4242-bc10-02dd998ba7b6",
  "sourceToolAssistantUUID": "439cdd5f-9fd9-4490-96d4-cf365b0c7500",
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

_source line 47 · 2026-05-30T06:13:35.695Z_

<details><summary>↩ Tool result · `toolu_01EVbxRUSDrAZ8RyihPDwHT5`</summary>

```text
# Paper Details

**Full Title:** "Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations"

**Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang

**Publication Date:** Submitted on 17 April 2026

**Complete Abstract:**

The research addresses reliability concerns in deployed language models by proposing an alternative to conventional uncertainty measures. Rather than relying on output-level signals like token probabilities or entropy, the authors introduce a conformal prediction framework leveraging internal model representations. Their key contribution involves Layer-Wise Information scores that "measure how conditioning on the input reshapes predictive entropy across model depth." 

When tested on question-answering benchmarks, particularly under distribution shifts, their method demonstrated superior validity-efficiency trade-offs compared to text-level alternatives while preserving competitive performance on in-domain tasks. The findings suggest that "internal representations can provide more informative conformal scores when surface-level uncertainty is unstable under distribution shift," offering practitioners a more robust approach to uncertainty quantification in language model applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2fd091e-c7c6-4fe1-91db-0a8bd4396d6d",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "015b6eaa-5cc9-400a-b003-60800a21b6e3",
  "sourceToolAssistantUUID": "b2fd091e-c7c6-4fe1-91db-0a8bd4396d6d",
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

_source line 48 · 2026-05-30T06:13:37.237Z_

<details><summary>↩ Tool result · `toolu_01JQKW1SrKQEsqaFkjzpfDbk`</summary>

```text
# Paper Information

**Full Title:** Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality

**Authors:** 
- Naihe Feng
- Yi Sui
- Shiyi Hou
- Jesse C. Cresswell
- Ga Wu

**Publication Date:** June 26, 2025 (submitted)

**Complete Abstract:**

The research introduces Conformal-RAG, a framework addressing quality evaluation of sub-claims in RAG systems. The work employs conformal prediction methodology combined with RAG mechanisms to deliver "statistical guarantees on response quality." This approach provides "group-conditional coverage spanning multiple sub-domains without requiring manual labelling," distinguishing it from existing auto-evaluation approaches that lack probabilistic assurances or demand ground truth answers.

A key finding shows the method preserves "up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee." The paper was accepted as a short paper at SIGIR 2025 and includes publicly available code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6a2d5f8-56f9-4cdf-b81f-85db495c2620",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "bec928bb-4e12-4930-a828-1cb6d5642dea",
  "sourceToolAssistantUUID": "a6a2d5f8-56f9-4cdf-b81f-85db495c2620",
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

_source line 49 · 2026-05-30T06:13:38.423Z_

<details><summary>↩ Tool result · `toolu_015gyKphx23eGjAwQQCL4kya`</summary>

```text
# Paper Information

**Title:** "Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey"

**Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, Yongjia Lei, Yuying Zhao, Xueqi Cheng, Qingkai Zeng, Luna Dong, Yinglong Xia, Krishnaram Kenthapadi, Ryan Rossi, Franck Dernoncourt, Md Mehrab Tanjim, Nesreen Ahmed, Xiaorui Liu, Wenqi Fan, Erik Blasch, Yu Wang, Meng Jiang, and Tyler Derr

**Publication Date:** February 8, 2025 (submitted)

**Abstract:** 

This comprehensive survey examines how Retrieval-Augmented Generation techniques can be made more trustworthy when applied to large language models. The authors identify that while RAG successfully reduces hallucinations and incorporates current knowledge, it introduces new challenges including robustness vulnerabilities, privacy exposure, susceptibility to adversarial manipulation, and accountability gaps. The paper organizes trustworthiness concerns around six dimensions: "reliability, privacy, safety, fairness, explainability, and accountability." For each area, the authors present frameworks and taxonomies to evaluate current approaches and suggest future research opportunities, with emphasis on real-world applications benefiting from these improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a95574bd-520b-4400-a1c9-243569e6c18f",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "a203aec0-97a3-415e-ba8d-79cc2dc2c656",
  "sourceToolAssistantUUID": "a95574bd-520b-4400-a1c9-243569e6c18f",
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

_source line 50 · 2026-05-30T06:13:40.965Z_

Now let me do one more targeted search to make sure I haven't missed any key papers specifically at the intersection of conformal prediction and RAG.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a203aec0-97a3-415e-ba8d-79cc2dc2c656",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG59YfkkyZgGx5iec3Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9493d0fa-2eb4-4142-9d27-1ad31a82c3e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE5aKp1avFCJkjr6MEGwNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2922,
      "cache_read_input_tokens": 17020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2922,
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

_source line 51 · 2026-05-30T06:13:41.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcHJJs1yFW2qmpeGWMypbR`</summary>

```json
{
  "query": "conformal prediction retrieval augmented generation uncertainty quantification arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9493d0fa-2eb4-4142-9d27-1ad31a82c3e7",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG59YfkkyZgGx5iec3Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7963fae-855f-48a0-a61b-8461eaf93174",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE5aKp1avFCJkjr6MEGwNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2922,
      "cache_read_input_tokens": 17020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2922,
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

_source line 52 · 2026-05-30T06:13:42.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BtSgw1cL3xCueWZtZwEcnN`</summary>

```json
{
  "query": "\"conformal RAG\" OR \"conformal factuality\" OR \"conformal prediction RAG\" paper 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7963fae-855f-48a0-a61b-8461eaf93174",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG59YfkkyZgGx5iec3Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f187a1b9-d320-4ac6-ad94-ffbc5face6fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE5aKp1avFCJkjr6MEGwNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2922,
      "cache_read_input_tokens": 17020,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2922
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 17020,
          "cache_creation_input_tokens": 2922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2922,
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

_source line 53 · 2026-05-30T06:13:49.851Z_

<details><summary>↩ Tool result · `toolu_01BtSgw1cL3xCueWZtZwEcnN`</summary>

```text
Web search results for query: ""conformal RAG" OR "conformal factuality" OR "conformal prediction RAG" paper 2025 2026"

Links: [{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"},{"title":"UNDERSTANDING CONFORMAL FACTUALITY FOR RAG- ...","url":"https://openreview.net/pdf/5ecf9d6dffd4601271be6f538997ee5bf9b9c5be.pdf"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"}]

Based on the search results, I found several recent papers on conformal RAG and conformal factuality from 2025-2026:

## Key Papers Found:

1. **Conformal-RAG (June 2025)**: Conformal-RAG is a novel framework inspired by recent applications of conformal prediction on large language models that leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality. By leveraging information from the RAG system, Conformal-RAG retains up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee. Paper: arXiv:2506.20978

2. **Understanding Conformal Factuality for RAG-based LLMs (September 2025)**: This paper integrates conformal factuality filtering with retrieval-augmented generation, introduces new factuality metrics, and shows through large-scale experiments that standard measures miss key trade-offs between correctness and informativeness. Submitted to ICLR 2026, OpenReview ID: OKnM5rEUbg

3. **Principled Context Engineering for RAG via Conformal Prediction (January 2026)**: Conformal prediction enables reliable, coverage-controlled context reduction in RAG, offering a model-agnostic and principled approach to context engineering, reducing retained context by 2-3x relative to unfiltered retrieval. arXiv:2511.17908, published in ECIR 2026

4. **Is Conformal Factuality for RAG-based LLMs Robust? (March 2026)**: This work exposes factuality-informativeness trade-offs and fragility of conformal filtering framework under distribution shifts and distractors, highlighting the need for new approaches for reliability with robustness and usefulness as key metrics. arXiv:2603.16817


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f187a1b9-d320-4ac6-ad94-ffbc5face6fb",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "5bccb010-46ad-428f-8be7-e47a307decb7",
  "sourceToolAssistantUUID": "f187a1b9-d320-4ac6-ad94-ffbc5face6fb",
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

_source line 54 · 2026-05-30T06:13:50.180Z_

<details><summary>↩ Tool result · `toolu_01LcHJJs1yFW2qmpeGWMypbR`</summary>

```text
Web search results for query: "conformal prediction retrieval augmented generation uncertainty quantification arxiv 2025 2026"

Links: [{"title":"URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models","url":"https://arxiv.org/pdf/2603.19281"},{"title":"Towards Trustworthy Retrieval Augmented Generation for ...","url":"https://arxiv.org/pdf/2502.06872"},{"title":"CONFLARE: CONFormal LArge language model REtrieval","url":"https://arxiv.org/pdf/2404.04287"},{"title":"URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models","url":"https://arxiv.org/html/2603.19281"},{"title":"CONFLARE: CONFormal LArge language model REtrieval","url":"https://arxiv.org/html/2404.04287v1"},{"title":"[2605.28920] Conf-Gen: Conformal Uncertainty Quantification for Generative Models","url":"https://arxiv.org/abs/2605.28920"},{"title":"[2506.05497] Conformal Prediction Beyond the Seen: A Missing Mass Perspective for Uncertainty Quantification in Generative Models","url":"https://arxiv.org/abs/2506.05497"},{"title":"QuCo-RAG: Quantifying Uncertainty from the Pre-training Corpus for Dynamic Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.19134"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"}]

I found several relevant papers at the intersection of conformal prediction, retrieval-augmented generation (RAG), and uncertainty quantification from 2024-2026. Here are the key findings:

## Recent Research Papers

**URAG: A Benchmark for Uncertainty Quantification in RAG (March 2026)**
This recent preprint from March 2026 reformulates open-ended tasks into multiple-choice question answering and leverages conformal prediction to obtain statistically valid uncertainty scores. The paper applies the evaluation pipeline to 8 standard RAG methods, measuring their performance through both accuracy and prediction-set sizes.

**Conformal-RAG: Response Quality Assessment (June 2025)**
Conformal-RAG leverages conformal prediction and internal information from the RAG mechanism to offer statistical guarantees on response quality, ensuring group-conditional coverage spanning multiple sub-domains.

**CONFLARE: Conformal Retrieval Framework (April 2024)**
This framework applies uncertainty quantification to question-answering RAG by enhancing the retrieval process with conformal prediction, enabling users to retrieve document chunks necessary to ensure the context contains the true answer with tolerable uncertainty levels.

**TRAQ: Trustworthy RAG via Conformal Prediction**
TRAQ leverages conformal prediction to ensure that the retrieved set includes the relevant passage with high probability and that the LLM set contains a semantically correct answer, providing a guarantee that a semantically correct answer is contained in its set with high probability.

**QuCo-RAG: Uncertainty from Pre-training Corpus (December 2025)**
QuCo-RAG determines when to retrieve by quantifying uncertainty via pre-training corpus statistics, shifting from subjective internal confidence to objective external evidence.

**Conf-Gen: Conformal UQ for Generative Models (May 2026)**
This very recent paper demonstrates conformal uncertainty quantification applications including image generators producing non-memorized images and conversational AI systems.

These papers show an active research area combining conformal prediction theory with RAG systems to provide statistical guarantees on uncertainty quantification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7963fae-855f-48a0-a61b-8461eaf93174",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "54fc6b54-676e-4c20-af78-76729f8544bd",
  "sourceToolAssistantUUID": "c7963fae-855f-48a0-a61b-8461eaf93174",
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

_source line 55 · 2026-05-30T06:13:52.820Z_

Let me fetch the remaining papers I haven't read yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54fc6b54-676e-4c20-af78-76729f8544bd",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG61rLXVfRieTg7y95a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e06ef468-c79e-4f76-b0e2-ad43bd434a12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4TGtwZGGhzi8a481wUvQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 891,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 19942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1256,
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

_source line 56 · 2026-05-30T06:13:54.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FFCjUrZLspWs7fm6b1fquC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.17908",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Principled context engineering RAG conformal prediction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e06ef468-c79e-4f76-b0e2-ad43bd434a12",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG61rLXVfRieTg7y95a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "710a57bd-62c6-455d-8500-3d0f10e2aa76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4TGtwZGGhzi8a481wUvQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 891,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 19942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1256,
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

_source line 57 · 2026-05-30T06:13:54.707Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VSyKFxDq1wefcHPtdWDkuR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16817",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. Is conformal factuality for RAG-based LLMs robust?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "710a57bd-62c6-455d-8500-3d0f10e2aa76",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG61rLXVfRieTg7y95a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "881272b8-3efe-4a93-9b0d-8d7c398b0ca3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4TGtwZGGhzi8a481wUvQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 891,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 19942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1256,
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

_source line 58 · 2026-05-30T06:13:55.877Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pmgw6MNCmmKyjxYdsiLB7M`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19281",
  "prompt": "Extract the full title, all authors, publication date, and the complete abstract of this paper. URAG benchmark uncertainty quantification retrieval augmented."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "881272b8-3efe-4a93-9b0d-8d7c398b0ca3",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG61rLXVfRieTg7y95a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "114d985d-92c3-4e2f-85c8-aaeae8c9ffb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4TGtwZGGhzi8a481wUvQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 891,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 19942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1256,
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

_source line 59 · 2026-05-30T06:13:58.428Z_

<details><summary>↩ Tool result · `toolu_01FFCjUrZLspWs7fm6b1fquC`</summary>

```text
# Paper Information

**Full Title:**
"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction"

**Authors:**
- Debashish Chakraborty
- Eugene Yang
- Daniel Khashabi
- Dawn Lawrie
- Kevin Duh

**Publication Date:**
Submitted November 22, 2025; revised January 19, 2026 (accepted at ECIR 2026)

**Abstract:**
The researchers address a challenge in retrieval-augmented generation where "LLM accuracy declines when long or noisy contexts exceed the model's effective attention span." Their method applies conformal prediction to filter retrieved evidence while maintaining statistical control. Testing on NeuCLIR and RAGTIME datasets, the approach "meets its target coverage, ensuring that a specified fraction of relevant snippets are retained" while reducing context size by 2-3x. Results indicate that "most discarded material is redundant or irrelevant," demonstrating improved factual accuracy through principled, model-agnostic context filtering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "710a57bd-62c6-455d-8500-3d0f10e2aa76",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "d1c142ee-5391-4dde-a4cf-1598479d1213",
  "sourceToolAssistantUUID": "710a57bd-62c6-455d-8500-3d0f10e2aa76",
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

_source line 60 · 2026-05-30T06:14:00.419Z_

<details><summary>↩ Tool result · `toolu_01VSyKFxDq1wefcHPtdWDkuR`</summary>

```text
# Paper Summary

**Full Title:** "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"

**Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak

**Publication Date:** March 17, 2026

**Complete Abstract:**

The research examines whether large language models can reliably avoid generating false information when using retrieval-augmented generation (RAG) with conformal factuality methods. While RAG grounds responses in retrieved evidence and conformal filtering offers statistical reliability guarantees, the authors question whether these approaches remain effective in practice.

Their findings reveal three critical limitations: First, "conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs." Second, the statistical guarantees break down when facing distribution shifts and distractors, requiring calibration data to match deployment conditions precisely. Third, simpler entailment-based verification systems outperform LLM-based confidence scorers while using "over 100× fewer FLOPs."

**Direct Answer:** No—the research demonstrates that conformal factuality guarantees are not robust to real-world conditions, exposing critical fragility in the framework that demands new approaches prioritizing both reliability and usefulness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "881272b8-3efe-4a93-9b0d-8d7c398b0ca3",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "ac3a6c30-3e47-47b5-a0b5-3828db6022b7",
  "sourceToolAssistantUUID": "881272b8-3efe-4a93-9b0d-8d7c398b0ca3",
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

_source line 61 · 2026-05-30T06:14:01.715Z_

<details><summary>↩ Tool result · `toolu_01Pmgw6MNCmmKyjxYdsiLB7M`</summary>

```text
# URAG Paper Details

**Full Title:** "URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models"

**Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang

**Publication Date:** March 2, 2026

**Complete Abstract:**

This research introduces a comprehensive evaluation framework examining how retrieval systems affect the trustworthiness of large language models. The work reformats open-ended tasks into multiple-choice questions to systematically measure confidence levels using conformal prediction methods. Testing eight established RAG approaches across domains including healthcare, programming, and mathematics, the researchers discovered that: improved accuracy frequently correlates with lower uncertainty, though this connection breaks down when retrieval contains errors; simpler modular methods generally outperform complex reasoning-based approaches in balancing accuracy and uncertainty; and no single technique performs consistently well across all domains. The study also identifies how retrieval parameters, foundational knowledge reliance, and confidence signals can increase overconfident mistakes and false generation. The authors provide their implementation code publicly for community access.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "114d985d-92c3-4e2f-85c8-aaeae8c9ffb8",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "a38362145d53a1294",
  "type": "user",
  "uuid": "4b7faed6-ee21-453c-b481-c7ce4a1a2426",
  "sourceToolAssistantUUID": "114d985d-92c3-4e2f-85c8-aaeae8c9ffb8",
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

_source line 62 · 2026-05-30T06:15:25.991Z_

I now have comprehensive information on all the key papers. Here is the structured literature survey.

---

## Literature Survey: Conformal Prediction for RAG and LLM Systems (2024--2026)

### TIER 1: Papers directly combining Conformal Prediction with RAG

---

**1. TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction**

- **Authors:** Shuo Li, Sangdon Park, Insup Lee, Osbert Bastani
- **Venue:** NAACL 2024
- **URL:** https://arxiv.org/abs/2307.04642
- **Summary:** First end-to-end statistical correctness guarantee for RAG; constructs prediction sets guaranteed to contain a semantically correct answer using conformal prediction, and uses Bayesian optimization to minimize set size (16.2% reduction).
- **Why important:** Foundational paper -- the first to apply conformal prediction end-to-end across both retrieval and generation in RAG, establishing the paradigm for the field.

---

**2. C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models**

- **Authors:** Mintong Kang, Nezihe Merve Gurel, Ning Yu, Dawn Song, Bo Li
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2402.03181
- **Summary:** First framework to certify generation risks for RAG via conformal risk analysis; proves RAG achieves lower conformal generation risk than standalone LLMs when retrieval quality is non-trivial; provides guarantees under distribution shift.
- **Why important:** Provides the theoretical backbone -- certified upper confidence bounds on generation risk -- that underpins formal safety analysis of RAG systems.

---

**3. CONFLARE: CONFormal LArge language model REtrieval**

- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson
- **Venue:** arXiv preprint, April 2024
- **URL:** https://arxiv.org/abs/2404.04287
- **Summary:** Applies conformal prediction to the retrieval step of RAG, establishing a similarity-score threshold at a user-specified error rate alpha so that the retrieved chunks are guaranteed to contain the true answer with (1-alpha) confidence.
- **Why important:** Focuses specifically on making the retrieval component conformally valid, complementing approaches that target generation. Provides a lightweight, practical Python implementation.

---

**4. Conformal-RAG: Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality**

- **Authors:** Naihe Feng, Yi Sui, Shiyi Hou, Jesse C. Cresswell, Ga Wu
- **Venue:** SIGIR 2025 (short paper)
- **URL:** https://arxiv.org/abs/2506.20978
- **Summary:** Combines conformal prediction with RAG-internal information to assess sub-claim quality; retains up to 60% more high-quality sub-claims than naive CP applied to LLMs, with group-conditional coverage across sub-domains and no manual labeling.
- **Why important:** Moves beyond whole-answer guarantees to sub-claim-level factuality assessment within RAG, which is essential for long-form generation where individual claims may be independently correct or incorrect.

---

**5. Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights**

- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=OKnM5rEUbg
- **Summary:** Integrates conformal factuality filtering with RAG and introduces three new evaluation metrics (non-empty rate, non-vacuous empirical factuality, sufficient correctness) that reveal trade-offs standard metrics miss between correctness and informativeness.
- **Why important:** Provides the first rigorous empirical analysis showing that standard factuality metrics are inadequate for evaluating conformal-RAG systems; the new metrics have become a reference framework for subsequent work.

---

**6. Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights**

- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak
- **Venue:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2603.16817
- **Summary:** Stress-tests conformal factuality for RAG under distribution shifts and distractors; finds guarantees break down, vacuous outputs dominate at high factuality levels, and simpler entailment-based verifiers outperform LLM scorers at 100x fewer FLOPs.
- **Why important:** Critical "reality check" paper -- exposes fragility in conformal-RAG guarantees under realistic deployment conditions, setting the agenda for more robust methods.

---

**7. Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction**

- **Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh
- **Venue:** ECIR 2026
- **URL:** https://arxiv.org/abs/2511.17908
- **Summary:** Uses conformal prediction to filter retrieved evidence in RAG, reducing context length by 2--3x while maintaining statistical coverage guarantees that a target fraction of relevant snippets are retained; improves factual accuracy by removing noise.
- **Why important:** Addresses the practical problem of context window overload in RAG via a principled, model-agnostic filtering approach with formal coverage control.

---

**8. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**

- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang
- **Venue:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2603.19281
- **Summary:** Comprehensive benchmark evaluating 8 RAG methods across healthcare, programming, and math using conformal prediction to obtain statistically valid uncertainty scores; finds accuracy-uncertainty correlation breaks under retrieval errors and simpler modular methods often outperform complex reasoning approaches.
- **Why important:** First standardized benchmark for uncertainty quantification in RAG, enabling systematic comparison of methods and identifying failure modes.

---

### TIER 2: Conformal Prediction for LLM Factuality and Abstention (directly applicable to RAG)

---

**9. Language Models with Conformal Factuality Guarantees**

- **Authors:** Christopher Mohri, Tatsunori Hashimoto
- **Venue:** arXiv preprint, February 2024
- **URL:** https://arxiv.org/abs/2402.10978
- **Summary:** Introduces "conformal factuality" -- a back-off algorithm that makes LLM outputs progressively less specific to expand uncertainty sets until correctness is guaranteed; achieves 80--90% correctness guarantees on QA and math reasoning with any black-box LLM.
- **Why important:** Seminal paper defining the conformal factuality framework that most subsequent RAG+CP papers build upon; the back-off mechanism is now a standard technique in the field.

---

**10. Conformal Linguistic Calibration: Trading-off between Factuality and Specificity**

- **Authors:** Zhengping Jiang, Anqi Liu, Benjamin Van Durme
- **Venue:** arXiv preprint, February 2025 (revised August 2025)
- **URL:** https://arxiv.org/abs/2502.19110
- **Summary:** Reframes linguistic calibration as answer set prediction; connects abstention and hedging through pragmatics; enables fine-tuned models to do uncertainty-aware adaptive claim rewriting with conformal guarantees on factual accuracy.
- **Why important:** Bridges the gap between hard abstention (refuse to answer) and soft calibration (hedge the answer), offering a nuanced middle ground particularly relevant for RAG systems that should communicate uncertainty rather than simply abstain.

---

**11. ConU: Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees**

- **Authors:** Zhiyuan Wang, Jinhao Duan, Lu Cheng, Yue Zhang, Qingni Wang, Xiaoshuang Shi, Kaidi Xu, Hengtao Shen, Xiaofeng Zhu
- **Venue:** EMNLP 2024 Findings
- **URL:** https://arxiv.org/abs/2407.00499
- **Summary:** Proposes a self-consistency-based uncertainty measure for black-box LLMs with conformal prediction to achieve strict correctness coverage control; evaluated on 7 LLMs across 4 datasets in general and medical domains.
- **Why important:** Provides a practical, model-agnostic uncertainty measure that can be directly plugged into RAG pipelines to decide when to trust or reject generated answers.

---

**12. Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models**

- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi
- **Venue:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06884
- **Summary:** Uses reinforcement learning to dynamically optimize conformal abstention thresholds rather than using fixed ones; achieves up to 3.2% accuracy gain, 22.19% hallucination detection improvement, and 70--85% calibration error reduction while meeting 90% coverage targets.
- **Why important:** Moves beyond static thresholds to learned, adaptive abstention policies -- directly applicable to RAG systems that must decide when to abstain vs. answer in varying deployment conditions.

---

**13. Geometry-Calibrated Conformal Abstention for Language Models**

- **Authors:** Rui Xu, Yi Chen, Sihong Xie, Hui Xiong
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.27914
- **Summary:** Post-hoc conformal abstention framework that uses representation geometry (how much the model's actual knowledge contributes to a response) instead of non-conformity scores; achieves 75% conditional correctness with selective answering.
- **Why important:** Novel use of internal representation geometry for conformal calibration, addressing the fundamental challenge that non-conformity scores are impractical for open-ended generation.

---

**14. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models**

- **Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, Maxim Panov
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.13991
- **Summary:** Prompt-adaptive conformal prediction that enables prompt-dependent calibration for LLMs; improves conditional coverage over existing methods while retaining marginal coverage guarantees; supports selective prediction for filtering unreliable claims.
- **Why important:** Addresses a key limitation of prior work (uniform calibration across all inputs) by making conformal thresholds adapt to each prompt, which is critical for RAG where query difficulty varies enormously.

---

**15. Differentiable Conformal Training for LLM Reasoning Factuality**

- **Authors:** Nathan Hittesdorf, Marco Salzetta, Lu Cheng
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.20098
- **Summary:** Makes conformal factuality fully differentiable (Differentiable Coherent Factuality -- DCF), enabling learning of better scoring mechanisms during training; achieves up to 141% improvement in claim retention while maintaining reliability guarantees.
- **Why important:** First paper to make conformal factuality end-to-end differentiable, enabling joint optimization of scoring and filtering rather than treating them as separate post-hoc steps.

---

**16. Conformal Language Model Reasoning with Coherent Factuality**

- **Authors:** Maxon Rubin-Toles, Maya Gambhir, Keshav Ramji, Aaron Roth, Surbhi Goel
- **Venue:** arXiv preprint, May 2025
- **URL:** https://arxiv.org/abs/2505.17126
- **Summary:** Introduces "coherent factuality" -- evaluating claims within their logical reasoning context rather than in isolation using deducibility graphs; achieves 90% factuality while retaining 80%+ of original claims on math reasoning tasks.
- **Why important:** Extends conformal factuality from isolated claim checking to multi-step reasoning chains, which is essential for RAG systems used in complex reasoning tasks where claim dependencies matter.

---

**17. Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations**

- **Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.16217
- **Summary:** Uses layer-wise information scores from internal model representations as conformal scores instead of output-level signals (token probabilities, entropy); shows superior validity-efficiency trade-offs especially under distribution shift.
- **Why important:** Demonstrates that internal representations provide more robust conformal scores than surface-level uncertainty, which is particularly relevant for RAG systems where distribution shift between calibration and deployment data is common.

---

### TIER 3: Survey

---

**18. Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey**

- **Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, et al. (20+ authors)
- **Venue:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06872
- **Summary:** Comprehensive survey organizing RAG trustworthiness around six dimensions (reliability, privacy, safety, fairness, explainability, accountability); covers conformal prediction methods among other approaches.
- **Why important:** Provides the broader context for where conformal prediction fits within the full landscape of trustworthy RAG research; useful for positioning any new work in the area.

---

### Key Takeaways for the Field

1. **The pipeline has two natural CP injection points:** the retrieval step (CONFLARE, Principled Context Engineering) and the generation step (conformal factuality, TRAQ). The best systems address both (TRAQ, Conformal-RAG).

2. **The factuality-informativeness trade-off is the central challenge:** Conformal guarantees can be achieved, but often at the cost of vacuous or overly hedged outputs (Chen et al., 2026). New metrics beyond simple coverage are needed.

3. **Robustness under distribution shift remains unsolved:** C-RAG provides theoretical bounds under shift, but empirical work (Chen et al., March 2026) shows practical fragility.

4. **The frontier is moving toward:** (a) adaptive/prompt-dependent calibration (Rubashevskii et al., 2026), (b) differentiable conformal training (Hittesdorf et al., 2026), (c) internal-representation-based scores (Wang et al., 2026), and (d) coherent multi-step reasoning guarantees (Rubin-Toles et al., 2025).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b7faed6-ee21-453c-b481-c7ce4a1a2426",
  "isSidechain": true,
  "agentId": "a38362145d53a1294",
  "requestId": "req_011CbYG6sAjMBgXJ9ZBgsPno",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "989d8847-bab2-4e9e-8486-e91321fcfa07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDde1v1vh8D4kWMG3KPcvE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2103,
      "cache_read_input_tokens": 21198,
      "output_tokens": 3896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3896,
          "cache_read_input_tokens": 21198,
          "cache_creation_input_tokens": 2103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2103,
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
