# Research conversation: I'm reviewing a proposal about domain-adaptive autoformalization for mathematical theorem proving in Lean 4. I need to s

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac1b5fe532ebdaa7c.jsonl`
- **Structured JSON:** [`a4b99874c8b579868989.json`](../../sessions/a4/a4b99874c8b579868989.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

68 recorded events

### User

_source line 1 · 2026-05-28T14:50:57.192Z_

I'm reviewing a proposal about domain-adaptive autoformalization for mathematical theorem proving in Lean 4. I need to search for any NEW papers from March-May 2026 that might be concurrent work or that the proposal might have missed. Search specifically for:

1. "domain-adaptive autoformalization" OR "domain-specific autoformalization" 2026
2. "autoformalization" "domain" "lean" 2026 site:arxiv.org
3. "mathlib" "domain" "autoformalization" 2026
4. "subdomain" "formalization" "lean" 2026
5. "error taxonomy" "autoformalization" 2026
6. "domain-conditioned retrieval" "theorem proving" 2026
7. Any new autoformalization papers from April-May 2026 on arxiv

Focus on finding work that:
- Conditions autoformalization on mathematical subdomain
- Provides domain-stratified error analysis for formal math
- Uses domain-aware retrieval for formalization
- Any new benchmarks or datasets for domain-stratified autoformalization evaluation

Report everything you find, especially anything that might pre-empt the proposal's novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "23315335-86ea-4337-86f0-733a4f734c93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T14:50:57.194Z_

```json
{
  "parentUuid": "23315335-86ea-4337-86f0-733a4f734c93",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
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
  "uuid": "ed77b83a-0440-468d-a744-aaffbafe7912",
  "timestamp": "2026-05-28T14:50:57.194Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T14:50:57.195Z_

```json
{
  "parentUuid": "ed77b83a-0440-468d-a744-aaffbafe7912",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ba1a12e2-9e77-497f-aab1-2850cf93c40e",
  "timestamp": "2026-05-28T14:50:57.195Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T14:51:00.196Z_



I'll conduct a thorough search across multiple queries to find concurrent work. Let me start by loading the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba1a12e2-9e77-497f-aab1-2850cf93c40e",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9uKPXAJsVmyzhb2gNG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f423d227-b806-4e65-9884-1ca28c85c89c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZuJ5fZybHrV25eTvA7HN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1613,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1613,
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

_source line 5 · 2026-05-28T14:51:00.826Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016kLFHTVkXphGZYHEEmV5bx`</summary>

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
  "parentUuid": "f423d227-b806-4e65-9884-1ca28c85c89c",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9uKPXAJsVmyzhb2gNG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdbfb2ed-cfea-40f7-8c24-33c7c8b207bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZuJ5fZybHrV25eTvA7HN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1613,
      "cache_read_input_tokens": 7407,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1613
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 1613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1613,
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

_source line 6 · 2026-05-28T14:51:00.830Z_

<details><summary>↩ Tool result · `toolu_016kLFHTVkXphGZYHEEmV5bx`</summary>

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
  "parentUuid": "bdbfb2ed-cfea-40f7-8c24-33c7c8b207bb",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "703b2a39-8672-4e48-85c2-41e8e03fd494",
  "sourceToolAssistantUUID": "bdbfb2ed-cfea-40f7-8c24-33c7c8b207bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T14:51:03.157Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "703b2a39-8672-4e48-85c2-41e8e03fd494",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b9a6dfa-4876-41e2-9456-43606b5f7565",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 8 · 2026-05-28T14:51:03.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GoGQ4oT1LibC7dr9mNruNW`</summary>

```json
{
  "query": "\"domain-adaptive autoformalization\" OR \"domain-specific autoformalization\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9a6dfa-4876-41e2-9456-43606b5f7565",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9c0b531-ea0a-4d69-bf55-934b9db9c81d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 9 · 2026-05-28T14:51:04.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013LaHyDXAoKeSJvCuTRdVyK`</summary>

```json
{
  "query": "\"autoformalization\" \"domain\" \"lean\" 2026 site:arxiv.org",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9c0b531-ea0a-4d69-bf55-934b9db9c81d",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9feffb7-a055-40f5-bf87-2ca1a753505f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 10 · 2026-05-28T14:51:04.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F961rpzgJUsgf4GYdNLmkD`</summary>

```json
{
  "query": "\"mathlib\" \"domain\" \"autoformalization\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9feffb7-a055-40f5-bf87-2ca1a753505f",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bbf5211-0c88-4ad7-8cc8-80ab678aac9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 11 · 2026-05-28T14:51:04.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013KejhLzC7GtxN5DfKZoQ6y`</summary>

```json
{
  "query": "\"subdomain\" \"formalization\" \"lean\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bbf5211-0c88-4ad7-8cc8-80ab678aac9b",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ad753b0-8805-4e7e-b289-de9db765519e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 12 · 2026-05-28T14:51:05.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ToXwQs5JARDknPxts1cNL`</summary>

```json
{
  "query": "\"error taxonomy\" \"autoformalization\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ad753b0-8805-4e7e-b289-de9db765519e",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad861f8f-9fa4-4892-ac4f-b9bae9d8adcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 13 · 2026-05-28T14:51:05.646Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Ywt2ascLgdM2kRQMDF3EV`</summary>

```json
{
  "query": "\"domain-conditioned retrieval\" \"theorem proving\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad861f8f-9fa4-4892-ac4f-b9bae9d8adcc",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c07dc79-7226-426b-9354-0a7281bdd506",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
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

_source line 14 · 2026-05-28T14:51:06.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KJpNbnFikEzXKyA3ybFeap`</summary>

```json
{
  "query": "autoformalization arxiv 2026 April May new papers lean 4 theorem proving",
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
  "parentUuid": "4c07dc79-7226-426b-9354-0a7281bdd506",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9ubE1xfYuWQf1fQocG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50578059-7f0c-40df-90c2-28930f3a41ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbMBV8HYHphaWbpKUKh9Fg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9020,
      "output_tokens": 446,
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
          "output_tokens": 446,
          "cache_read_input_tokens": 9020,
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

_source line 15 · 2026-05-28T14:51:11.476Z_

<details><summary>↩ Tool result · `toolu_013LaHyDXAoKeSJvCuTRdVyK`</summary>

```text
Web search results for query: ""autoformalization" "domain" "lean" 2026 site:arxiv.org"

Links: [{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"[2604.16347] Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/abs/2604.16347"},{"title":"MerLean: An Agentic Framework For Autoformalization in Quantum Computation","url":"https://arxiv.org/html/2602.16554v1"},{"title":"[2602.16554] MerLean: An Agentic Framework for Autoformalization in Quantum Computation","url":"https://arxiv.org/abs/2602.16554"},{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"}]

I found several recent papers on arxiv.org related to autoformalization and Lean from 2026:

1. **"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning"** (March 25, 2026) - This paper focuses on automatically translating natural language mathematical texts into formal proof language such as Lean4, with fine-tuning of Qwen3.5-2B using LoRA for natural language to Lean4 formalization on FineLeanCorpus.

2. **"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings"** (March 29, 2026) - This presents a unified framework for automatically translating entire NL theorems and proofs into Lean 4.

3. **"Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization"** (March 16, 2026) - This paper addresses AI-driven autoformalization of mathematics and proposes a human-in-the-loop approach in which human scientists and AI collaboratively produce formal proofs.

4. **"MerLean: An Agentic Framework for Autoformalization in Quantum Computation"** (February 18, 2026) - This evaluates MerLean on three theoretical quantum computing papers producing 2,050 Lean declarations from 114 statements in total, achieving end-to-end formalization on all three papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9feffb7-a055-40f5-bf87-2ca1a753505f",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "3ccea634-8bda-42e2-b2f4-072492c9661a",
  "sourceToolAssistantUUID": "c9feffb7-a055-40f5-bf87-2ca1a753505f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T14:51:11.734Z_

<details><summary>↩ Tool result · `toolu_01F961rpzgJUsgf4GYdNLmkD`</summary>

```text
Web search results for query: ""mathlib" "domain" "autoformalization" 2026"

Links: [{"title":"MMFormalizer: Multimodal Autoformalization in the Wild","url":"https://arxiv.org/pdf/2601.03017"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"(PDF) MMFormalizer: Multimodal Autoformalization in the Wild","url":"https://www.researchgate.net/publication/399522332_MMFormalizer_Multimodal_Autoformalization_in_the_Wild"},{"title":"UW Math AI Lab · GitHub","url":"https://github.com/uw-math-ai"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"ATLAS: Autoformalizing Theorems through Lifting, ...","url":"https://openreview.net/pdf?id=MlJyAvQaxp"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"}]

Based on the search results, here are recent developments related to mathlib, domain-specific work, and autoformalization in 2026:

## Key Findings:

**Multimodal Autoformalization:** Multimodal autoformalization beyond the geometric domain remains largely underexplored, particularly in modeling complex phenomena that arise in the real physical world. Mathlib provides a robust foundation for integrating perceptual representations with formal reasoning.

**Domain-Specific Approaches:** Agents explore relevant library code and extract key definitions and formulas, forming a static context for each category in a one-time, category-specific process. IndiMathBench problems are traditionally sourced from a fixed set of topics: algebra, euclidean geometry, elementary number theory, and combinatorics.

**Expanding Mathematical Domains:** Most undergraduate mathematics is present in mathlib, but several big gaps remain: differential geometry, partial differential equations, numerical analysis, with plans to autoformalize undergraduate textbooks on numerical analysis of differential equations.

**Autoformalization Benchmarks:** MathAtlas is a large-scale benchmark for graduate-level autoformalization of mathematics in the wild. A concept repository comprises 13 domains, 55 topics, and 350 concepts following Mathlib's organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bbf5211-0c88-4ad7-8cc8-80ab678aac9b",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "fca989c7-18d7-4f5c-a96b-6683ad6a18c7",
  "sourceToolAssistantUUID": "7bbf5211-0c88-4ad7-8cc8-80ab678aac9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T14:51:11.991Z_

<details><summary>↩ Tool result · `toolu_012Ywt2ascLgdM2kRQMDF3EV`</summary>

```text
Web search results for query: ""domain-conditioned retrieval" "theorem proving" 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.22819"},{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137v2"},{"title":"REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://arxiv.org/html/2505.20613v3"},{"title":"AI-Driven Formal Theorem Proving in the Lean Ecosystem","url":"https://leandojo.org/"},{"title":"Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS","url":"https://arxiv.org/pdf/2510.10815"},{"title":"LeanDojo: Theorem Proving with Retrieval-Augmented Language Models","url":"https://arxiv.org/pdf/2306.15626"},{"title":"[2306.15626] LeanDojo: Theorem Proving with Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2306.15626"}]

I found search results related to theorem proving and retrieval in 2026. Here are the most relevant findings:

LeanSearch v2 is a staged system for premise retrieval in theorem proving that achieves state-of-the-art Mathlib search without domain-specific fine-tuning and includes a reasoning mode targeting set-valued premise retrieval through iterative sketch-retrieve-reflect cycles.

REAL-Prover (REtrieval-Augmented Lean Prover) is a retrieval-augmented and stepwise framework for automated theorem proving in Lean, where each model invocation is conditioned on the current proof state and enhanced through the retrieval of semantically relevant theorems from Mathlib.

Additionally, DeltaProver introduces a custom Domain-Specific Language to perform subgoal decomposition, and iteratively repairs the generated proof using verifier conditions.

The search results show several 2026 papers and preprints focused on improving retrieval mechanisms for theorem proving, with emphasis on domain-specific conditioning and proof state awareness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c07dc79-7226-426b-9354-0a7281bdd506",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "de8aeff2-8f08-422f-b80e-b650d32c7cc4",
  "sourceToolAssistantUUID": "4c07dc79-7226-426b-9354-0a7281bdd506",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T14:51:12.688Z_

<details><summary>↩ Tool result · `toolu_015ToXwQs5JARDknPxts1cNL`</summary>

```text
Web search results for query: ""error taxonomy" "autoformalization" 2026"

Links: [{"title":"Formal Error Taxonomy","url":"https://www.emergentmind.com/topics/formal-error-taxonomy"},{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"Error Taxonomy Generation with SKILL.md - Data Science x AI","url":"https://datasciencexai.substack.com/p/error-taxonomy-generation-with-skillmd"},{"title":"What is Error Taxonomy? Definition","url":"https://decodo.com/glossary/error-taxonomy"},{"title":"ErrorAtlas: Taxonomy of LLM Failure Modes","url":"https://www.emergentmind.com/topics/erroratlas"},{"title":"Autoformalization in the Wild: Assessing LLMs on","url":"https://arxiv.org/pdf/2502.12065"},{"title":"Systematic Taxonomy of Errors","url":"https://www.emergentmind.com/topics/systematic-taxonomy-of-errors"},{"title":"[2602.00997] Error Taxonomy-Guided Prompt Optimization","url":"https://arxiv.org/abs/2602.00997"}]

I found several relevant results connecting error taxonomy and autoformalization from 2026. Here's what I discovered:

## Key Findings

**Autoformalization and Error Taxonomy Integration:**

The AI for Math Workshop at ICML 2026 features a track evaluating whether autoformalization preserves mathematical intent using the FormalRx-Test dataset built on the SCI Error Taxonomy with 28 error categories.

**Formalization Faithfulness Analysis:**

Research presented at the VerifAI-2 Workshop (ICLR 2026) uses Claude Opus 4.5 to classify formalization faithfulness following an error taxonomy, where the judge performs axiom-premise correspondence analysis to identify fabrication, mistranslation, and omission errors.

In multi-statement formalization settings, models may fabricate axioms absent from premises, omit premises entirely, or induce contradictions.

**Formal Error Taxonomy Framework:**

Updated January 19, 2026, Formal Error Taxonomy is a rigorously defined hierarchical framework that categorizes and analyzes error phenomena across diverse technical fields. Practical applications include AI model evaluation, benchmark design, and error diagnosis in domains like EFL writing, spreadsheets, and quantum processes.

**Related Work:**

Error Taxonomy-Guided Prompt Optimization (ETGPO) collects model errors, categorizes them into a taxonomy, and augments the prompt with guidance targeting the most frequent failure modes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad861f8f-9fa4-4892-ac4f-b9bae9d8adcc",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "6d01f9e1-055c-4c56-b4f0-426a1f759399",
  "sourceToolAssistantUUID": "ad861f8f-9fa4-4892-ac4f-b9bae9d8adcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T14:51:13.235Z_

<details><summary>↩ Tool result · `toolu_01GoGQ4oT1LibC7dr9mNruNW`</summary>

```text
Web search results for query: ""domain-adaptive autoformalization" OR "domain-specific autoformalization" 2026"

Links: [{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/html/2509.09810v2"},{"title":"Neuro-Symbolic Autoformalization Framework","url":"https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"},{"title":"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/pdf/2603.19828"}]

Based on the search results, here's what I found about domain-adaptive and domain-specific autoformalization in 2026:

## Current State of Domain-Specific Autoformalization

Current autoformalization approaches are often domain-specific, with systems designed separately for areas such as mathematical reasoning, planning, logic, etc. This represents a key challenge in the field.

## Recent Developments

Several recent frameworks and approaches from 2025-2026 are addressing autoformalization across different domains:

1. **Adaptive Multi-Paradigm Frameworks**: Adaptive multi-paradigm frameworks generalize autoformalization by decomposing NL problems into subproblems, predicting optimal reasoning paradigms, and dynamically composing reasoning over solver pools.

2. **Neuro-Symbolic Systems**: Neuro-symbolic autoformalization frameworks aim to translate free-form natural language task descriptions or regulatory policy documents into fully executable neuro-symbolic programs or executable policy models.

3. **Domain Adaptation in Mathematical Tasks**: Fine-tuning approaches adapt pre-trained models to specialized domains (e.g., competition math) using smaller, task-specific datasets.

## Future Directions

There is a vision for autoformalization systems that can generalize compositionally, adapt to new domains with minimal supervision, and tightly integrate with formal verification frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9c0b531-ea0a-4d69-bf55-934b9db9c81d",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "a7ecf8f6-e378-452a-9a85-bc10f81c8b42",
  "sourceToolAssistantUUID": "c9c0b531-ea0a-4d69-bf55-934b9db9c81d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T14:51:14.108Z_

<details><summary>↩ Tool result · `toolu_013KejhLzC7GtxN5DfKZoQ6y`</summary>

```text
Web search results for query: ""subdomain" "formalization" "lean" 2026"

Links: [{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Mathematics in Lean Release v4.19.0 Jeremy Avigad Patrick Massot May 14, 2026","url":"https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf"},{"title":"Mathlib: A Foundation for Formal Mathematics Research and Verification — Lean Lang","url":"https://lean-lang.org/use-cases/mathlib/"},{"title":"Lean-related conferences and events","url":"https://leanprover-community.github.io/events.html"},{"title":"AI-Driven Formal Theorem Proving in the Lean Ecosystem","url":"https://leandojo.org/"},{"title":"Formalizing Theoretical Computer Science in Lean","url":"https://urapprojects.berkeley.edu/detail.php?id=20341-1"},{"title":"leanprover-community.github.io/data/events.yaml at lean4 · leanprover-community/leanprover-community.github.io","url":"https://github.com/leanprover-community/leanprover-community.github.io/blob/lean4/data/events.yaml"},{"title":"Lean Together 2026 | A meeting all about Lean","url":"https://leanprover-community.github.io/lt2026/"},{"title":"Formalizing Fermat's Last Theorem in Lean: A Landmark Mathematical Project — Lean Lang","url":"https://lean-lang.org/use-cases/flt/"},{"title":"ON THE FORMALIZATION OF IUT: A PRELIMINARY","url":"https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20(2026-04).pdf"}]

The search results provide information about Lean formalization in 2026, though the results don't specifically focus on "subdomain" formalization. Here's what I found:

## Recent Lean Formalization Activity in 2026

The goal of mathematical formalization using Lean 4 is to teach formal mathematics using the Lean 4 interactive proof assistant.

Several major formalization projects are underway in 2026:

- **Fermat's Last Theorem**: An ambitious project led by Professor Kevin Buzzard at Imperial College London aims to formalize Fermat's Last Theorem in the Lean proof assistant, which represents a significant milestone in formal verification.

- **Inter-Universal Teichmüller Theory (IUT)**: There is work on the formalization of IUT in Lean, referred to as "LeanForm" as a communication tool.

- **Theoretical Computer Science Library**: A project aims to formalize essential mathematical theorems in theoretical computer science, including asymptotic theorems, graph theory, and finite-dimensional field theory, and extend to advanced topics including coding theory, information theory, complexity theory, and cryptography.

## Events and Community Activity

Several 2026 workshops include the Formal Mathematics and Proof Systems Interoperability (FMPSI'26) in June-July in Orsay, France, the Bridging Lean and the LMFDB workshop in June-July in Norwich, UK, and the Summer School on Formalization in Lean in Pittsburgh, USA.

If you're looking for more specific information about subdomain formalization in Lean, the search results don't contain detailed coverage of that particular topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ad753b0-8805-4e7e-b289-de9db765519e",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "e2b1241e-acad-4bf8-a161-f431014cadc0",
  "sourceToolAssistantUUID": "1ad753b0-8805-4e7e-b289-de9db765519e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T14:51:14.900Z_

<details><summary>↩ Tool result · `toolu_01KJpNbnFikEzXKyA3ybFeap`</summary>

```text
Web search results for query: "autoformalization arxiv 2026 April May new papers lean 4 theorem proving"

Links: [{"title":"Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/html/2604.16347"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/html/2406.01940v1"},{"title":"Lean Meets Theoretical Computer Science: Scalable Synthesis of Theorem Proving Challenges in Formal-Informal Pairs","url":"https://arxiv.org/html/2508.15878"},{"title":"A New Approach Towards Autoformalization Nilay Patel","url":"https://arxiv.org/pdf/2310.07957"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"[2508.15878] Lean Meets Theoretical Computer Science: Scalable Synthesis of Theorem Proving Challenges in Formal-Informal Pairs","url":"https://arxiv.org/abs/2508.15878"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"}]

Based on the search results, here are some relevant recent papers on autoformalization with Lean 4 and theorem proving from April-May 2026 and surrounding periods:

## Recent Papers Found

**Formalizing the Stability of the Two Higgs Doublet Model Potential into Lean** by Joseph Tooby-Smith (2026) - This represents recent work in formalizing physics concepts into Lean.

**Autoformalizing Mathematical Statements by Symbolic Equivalence and Semantic Consistency** by Li et al. (2024), published in NeurIPS - This work addresses key challenges in the autoformalization task.

**Rethinking and Improving Autoformalization: Reliable Evaluation and Benchmarks for Statement Autoformalization** by Liu et al. (2025), published in EMNLP.

**DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition** by Ren et al. (2025).

**HepLean: Digitalising High Energy Physics** by Joseph Tooby-Smith (2025), published in Computer Physics Communications.

Additionally, **Process-Driven Autoformalization in Lean 4** by Lu et al. (2024) and **ProofBridge**, which addresses proof auto-formalization in Lean 4 by combining joint embedding models, LLMs, and Lean for verification.

More recently, **Lean Meets Theoretical Computer Science** automatically synthesizes problems with parallel formal (Lean4) and informal (Markdown) specifications, creating a scalable pipeline for generating verified problems, with an update in May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50578059-7f0c-40df-90c2-28930f3a41ca",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "0e32fee8-39f7-4b50-9a93-67e94fca9cb8",
  "sourceToolAssistantUUID": "50578059-7f0c-40df-90c2-28930f3a41ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-28T14:51:17.194Z_

Good, I have initial results. Let me now run deeper follow-up searches on the most promising leads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e32fee8-39f7-4b50-9a93-67e94fca9cb8",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "916712cf-d321-4253-a02a-c7b18655d260",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 23 · 2026-05-28T14:51:18.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J1A69VvwLHsVQ5y8ksGaLM`</summary>

```json
{
  "query": "arxiv 2604.19459 \"Do LLMs Game Formalization\" error taxonomy ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "916712cf-d321-4253-a02a-c7b18655d260",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8353e7d9-de38-440f-9f47-87dca9ccc863",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 24 · 2026-05-28T14:51:19.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TcFrG6bSMtFiJZJqyarsSA`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization domain-stratified 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8353e7d9-de38-440f-9f47-87dca9ccc863",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d624daa1-b3d3-4741-9dfd-390008a39fc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 25 · 2026-05-28T14:51:19.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MhHDzvMTJRF3piJzp21VJ6`</summary>

```json
{
  "query": "LeanSearch v2 premise retrieval domain-aware 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d624daa1-b3d3-4741-9dfd-390008a39fc3",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72308ef2-fedc-43b1-a4a2-1110ff8fcd79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 26 · 2026-05-28T14:51:20.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UBca1d2AV1cj61L4EHExqX`</summary>

```json
{
  "query": "FormalEvolve neuro-symbolic autoformalization 2603.19828 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72308ef2-fedc-43b1-a4a2-1110ff8fcd79",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66db17d3-71c0-4b9a-aedb-8a4540e797c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 27 · 2026-05-28T14:51:21.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GwyUZqMThwUUaPxUuxdcdA`</summary>

```json
{
  "query": "\"cycle consistency\" autoformalization lean 2603.24372 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66db17d3-71c0-4b9a-aedb-8a4540e797c3",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7258ba0c-119a-4e77-97c3-ad2e751398d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 28 · 2026-05-28T14:51:22.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UgFAMTkZLFacftZrGN8sRP`</summary>

```json
{
  "query": "REAL-Prover retrieval augmented lean prover 2505.20613 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7258ba0c-119a-4e77-97c3-ad2e751398d4",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccda6d51-7f8e-4ffe-865d-17a610a52e8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5634,
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

_source line 29 · 2026-05-28T14:51:22.829Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V3HvmmUBzFVT6aHyRsZKiP`</summary>

```json
{
  "query": "DRIFT decompose retrieve formalize theorems autoformalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccda6d51-7f8e-4ffe-865d-17a610a52e8e",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9vd7u6UxBoNtD1iqVP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d7a5b0f-12e5-4218-96e3-51d835d2ca41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwqQbUK9xVVe83qycg8noe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5634,
      "cache_read_input_tokens": 9652,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 417,
          "cache_read_input_tokens": 9652,
          "cache_creation_input_tokens": 5634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5634,
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

_source line 30 · 2026-05-28T14:51:26.693Z_

<details><summary>↩ Tool result · `toolu_01J1A69VvwLHsVQ5y8ksGaLM`</summary>

```text
Web search results for query: "arxiv 2604.19459 "Do LLMs Game Formalization" error taxonomy ICLR 2026"

Links: [{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Autoformalization of Game Descriptions using Large Language Models","url":"https://arxiv.org/pdf/2409.12300"},{"title":"ICLR 2026 Workshop on Logical Reasoning of Large Language Models","url":"https://arxiv.org/pdf/2603.17169"}]

Based on the search results, I found the paper you're looking for. Here's what the search revealed:

The paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" (arxiv 2604.19459) was written by Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut, and it was published at the VerifAI-2 Workshop at ICLR 2026.

**About the paper:**

The paper addresses how formal verification guarantees proof validity but not formalization faithfulness, and for natural-language logical reasoning where models construct axiom systems from scratch, this gap between valid proofs and faithful translations is especially acute.

**Error Taxonomy:**

The paper uses Claude Opus 4.5 to classify formalization faithfulness following a taxonomy that examines premises, conclusions, and Lean code through axiom-premise correspondence analysis to identify fabrication, mistranslation, and omission errors. The prompt expands the Fabrication category into four subtypes to distinguish severity: CONCLUSION AS AXIOM (clear gaming), FABRICATED CONTRADICTION (unsound), FABRICATED WORLD KNOWLEDGE (common-sense), and FABRICATED INVENTED.

**Key Findings:**

The two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation as a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8353e7d9-de38-440f-9f47-87dca9ccc863",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "a098a3ec-b043-4f1a-8f4c-821da22e62e1",
  "sourceToolAssistantUUID": "8353e7d9-de38-440f-9f47-87dca9ccc863",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T14:51:26.738Z_

<details><summary>↩ Tool result · `toolu_01MhHDzvMTJRF3piJzp21VJ6`</summary>

```text
Web search results for query: "LeanSearch v2 premise retrieval domain-aware 2026 arxiv"

Links: [{"title":"[2605.13137] LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/abs/2605.13137"},{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137"},{"title":"Lean Finder: Semantic Search for Mathlib That Understands User Intents","url":"https://openreview.net/pdf?id=5SF4fFRw7u"},{"title":"Lean Finder: Semantic Search for Mathlib That Understands User Intents","url":"https://arxiv.org/html/2510.15940v1"},{"title":"arXiv:2506.11085v1 [cs.SE] 4 Jun 2025","url":"https://arxiv.org/pdf/2506.11085"},{"title":"(PDF) REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://www.researchgate.net/publication/392133993_REAL-Prover_Retrieval_Augmented_Lean_Prover_for_Mathematical_Reasoning"}]

Based on the search results, I found relevant information about LeanSearch v2:

LeanSearch v2 is a system for global premise retrieval in Lean 4 theorem proving. It is a staged retrieval system whose standard mode achieves state-of-the-art Mathlib search without domain-specific fine-tuning.

The reasoning mode builds on standard mode as its retrieval substrate, targeting global premise retrieval through iterative sketch-retrieve-reflect cycles. On a 69-query benchmark of research-level Mathlib theorems, reasoning mode recovers 46.1% of ground-truth premise groups within 10 retrieved candidates, outperforming strong reasoning retrieval systems (38.0%) and premise-selection baselines (9.3%).

In a controlled downstream evaluation with a fixed prover loop, replacing alternative retrievers with LeanSearch v2 yields the highest proof success (20% vs. 16% for the next-best system and 4% without retrieval).

The paper (arXiv 2605.13137) was submitted in May 2026 and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72308ef2-fedc-43b1-a4a2-1110ff8fcd79",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "6b28e7dd-088c-490e-9e15-99d5d450c632",
  "sourceToolAssistantUUID": "72308ef2-fedc-43b1-a4a2-1110ff8fcd79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T14:51:26.840Z_

<details><summary>↩ Tool result · `toolu_01TcFrG6bSMtFiJZJqyarsSA`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization domain-stratified 2026 arxiv"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291v1"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"}]

Based on the search results, I found detailed information about the MathAtlas benchmark:

## MathAtlas: A Benchmark for Autoformalization in the Wild

MathAtlas is a benchmark set for large-scale autoformalization of graduate-level mathematics in the wild. It is the first large-scale autoformalization benchmark of in-the-wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

### Key Features

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.

### Performance Results

MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions.

The paper was published on arXiv in May 2026 (arxiv:2605.14061) and addresses the gap left by previous autoformalization benchmarks that focused mainly on olympiad or undergraduate mathematics rather than graduate and research-level mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d624daa1-b3d3-4741-9dfd-390008a39fc3",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "cbbca663-7a43-4397-913d-58766fe5bd6c",
  "sourceToolAssistantUUID": "d624daa1-b3d3-4741-9dfd-390008a39fc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T14:51:28.204Z_

<details><summary>↩ Tool result · `toolu_01UBca1d2AV1cj61L4EHExqX`</summary>

```text
Web search results for query: "FormalEvolve neuro-symbolic autoformalization 2603.19828 2026"

Links: [{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"},{"title":"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/pdf/2603.19828"},{"title":"Neuro-Symbolic Autoformalization Framework","url":"https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"},{"title":"Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2508.13678v1"},{"title":"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview","url":"https://openreview.net/forum?id=hUb2At2DsQ"}]

Based on the search results, here's what I found about FormalEvolve:

FormalEvolve is a compilation-gated neuro-symbolic evolutionary framework that formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires. Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements.

The framework addresses the challenge that semantic consistency does not imply prover effectiveness: even semantically consistent formalizations can differ substantially in proof-search cost and success rate.

FormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.

On CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes (lower Gini).

The paper (arXiv:2603.19828) was submitted on March 20, 2026, with the latest version on March 23, 2026, authored by Haijian Lu, Wei Wang, and Jing Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66db17d3-71c0-4b9a-aedb-8a4540e797c3",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "1db915dc-6b1f-4f17-bc65-f7b753257392",
  "sourceToolAssistantUUID": "66db17d3-71c0-4b9a-aedb-8a4540e797c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T14:51:29.527Z_

<details><summary>↩ Tool result · `toolu_01GwyUZqMThwUUaPxUuxdcdA`</summary>

```text
Web search results for query: ""cycle consistency" autoformalization lean 2603.24372 2026"

Links: [{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"NeurIPS Improving autoformalization via cycle consistency and incremental type-checking using language-model probabilistic programs","url":"https://neurips.cc/virtual/2025/131104"},{"title":"Improving autoformalization via cycle consistency and incremental type-checking using language-model probabilistic programs | OpenReview","url":"https://openreview.net/forum?id=ZGcDZ73Nb2"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"Improving autoformalization via cycle consistency and incremental type-checking","url":"https://openreview.net/attachment?id=ZGcDZ73Nb2&name=pdf"}]

Based on the search results, I found relevant information about the paper with ID 2603.24372:

## Paper: "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning"

The paper, submitted on March 25, 2026, addresses autoformalization—automatically translating natural language mathematical texts into formal proof language such as Lean4—which can help accelerate AI-assisted mathematical research through proof verification or proof search.

### Cycle Consistency Approach

Cycle consistency measures how well the meaning of a statement is preserved through a natural language to Lean4 to natural language loop, computed as cosine similarity of off-the-shelf sentence embeddings.

### Methodology

The author fine-tunes Qwen3.5-2B with LoRA for natural language to Lean4 formalization on FineLeanCorpus and considers three training regimes: supervised fine-tuning (SFT) with curriculum learning, SFT without curriculum ordering, and reinforcement learning using group relative policy optimization (GRPO) with a cycle consistency reward.

### Results

On an unseen subset of FineLeanCorpus and on PutnamBench, RL substantially outperforms both SFT variants (mean cycle consistency 0.669 vs. 0.513 on FLC; 0.561 vs. 0.422 on PutnamBench), while increasing cross-entropy loss by only 0.011 nats, with minimal impact on formalization quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7258ba0c-119a-4e77-97c3-ad2e751398d4",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "b9650b5a-879f-4e2c-908c-6ba4dafeebf9",
  "sourceToolAssistantUUID": "7258ba0c-119a-4e77-97c3-ad2e751398d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T14:51:30.920Z_

<details><summary>↩ Tool result · `toolu_01UgFAMTkZLFacftZrGN8sRP`</summary>

```text
Web search results for query: "REAL-Prover retrieval augmented lean prover 2505.20613 2026"

Links: [{"title":"FrenzyMath/REAL-Prover · Hugging Face","url":"https://huggingface.co/FrenzyMath/REAL-Prover"},{"title":"[2505.20613] REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://arxiv.org/abs/2505.20613"},{"title":"[Literature Review] REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://www.themoonlight.io/en/review/real-prover-retrieval-augmented-lean-prover-for-mathematical-reasoning"},{"title":"REAL-Prover: Retrieval Augmented Lean ...","url":"https://arxiv.org/pdf/2505.20613"},{"title":"FrenzyMath/LeanSearch-PS · Hugging Face","url":"https://huggingface.co/FrenzyMath/LeanSearch-PS"},{"title":"(PDF) REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://www.researchgate.net/publication/392133993_REAL-Prover_Retrieval_Augmented_Lean_Prover_for_Mathematical_Reasoning"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=10525&show=250"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=3775&show=1000"},{"title":"Prover Agent: An Agent-Based Framework for Formal Mathematical Proofs","url":"https://arxiv.org/html/2506.19923v4"}]

Based on the search results, here's information about REAL-Prover:

## Overview

REAL-Prover is a retrieval-augmented, stepwise large language model-based theorem prover for Lean 4. It is a new open-source stepwise theorem prover for Lean 4 that is based on a fine-tuned large language model (REAL-Prover-v1) and integrated with a retrieval system (Leansearch-PS), which notably boosts performance on solving college-level mathematics problems.

## Key Components

The model is built on top of Qwen2.5-Math-7B, and fine-tuned using a custom pipeline and dataset to support formal reasoning in Lean. The model is integrated with a retrieval module (Leansearch-PS) that fetches relevant theorems from the Lean math library to enhance generation quality.

## Development Methods

To train REAL-Prover-v1, the authors developed HERALD-AF, a data extraction pipeline that converts natural language math problems into formal statements, and a new open-source Lean 4 interactive environment (Jixia-interactive) to facilitate synthesis data collection.

## Performance

The prover using only supervised fine-tune achieves a 23.7% success rate (Pass@64) on the ProofNet dataset, which is comparable to state-of-the-art models.

The arXiv paper (2505.20613) was published in May 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccda6d51-7f8e-4ffe-865d-17a610a52e8e",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "d08cd1cf-8626-4fdb-9451-42c8b0b6fe94",
  "sourceToolAssistantUUID": "ccda6d51-7f8e-4ffe-865d-17a610a52e8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T14:51:34.977Z_

<details><summary>↩ Tool result · `toolu_01V3HvmmUBzFVT6aHyRsZKiP`</summary>

```text
Web search results for query: "DRIFT decompose retrieve formalize theorems autoformalization 2026"

Links: [{"title":"[2510.10815] DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/abs/2510.10815"},{"title":"DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN ...","url":"https://openreview.net/pdf?id=IGEs577RFz"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems | OpenReview","url":"https://openreview.net/forum?id=IGEs577RFz"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/html/2510.10815v2"},{"title":"(PDF) DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://www.researchgate.net/publication/396458949_DRIFT_Decompose_Retrieve_Illustrate_then_Formalize_Theorems"},{"title":"ICLR Poster DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://iclr.cc/virtual/2026/poster/10010321"},{"title":"Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS","url":"https://arxiv.org/pdf/2510.10815"}]

Based on the search results, here's what I found about DRIFT:

DRIFT is a novel framework that enables LLMs to decompose informal mathematical statements into smaller, more tractable sub-components, and facilitates targeted retrieval of premises from mathematical libraries such as Mathlib. Additionally, DRIFT retrieves illustrative theorems to help models use premises more effectively in formalization tasks.

**The Problem It Addresses:**
Automating the formalization of mathematical statements for theorem proving remains a major challenge for LLMs, which struggle to identify and utilize the prerequisite mathematical knowledge and its corresponding formal representation in languages like Lean.

**How DRIFT Works:**
DRIFT operates in stages: first, an LLM breaks down the statement into atomic, concept-focused sub-queries, and for each sub-query, a dense retriever identifies foundational dependent premises from a formal library.

**Performance Results:**
DRIFT was evaluated across diverse benchmarks (ProofNet, ConNF, and MiniF2F-test) and consistently improves premise retrieval, nearly doubling the F1 score compared to the DPR baseline on ProofNet, with notable performance improvements on the ConNF benchmark using GPT-4.1 and DeepSeek-V3.1.

The paper was under review as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d7a5b0f-12e5-4218-96e3-51d835d2ca41",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "23460d95-fa0f-4a32-b399-a6c949ad2852",
  "sourceToolAssistantUUID": "8d7a5b0f-12e5-4218-96e3-51d835d2ca41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-28T14:51:38.039Z_

Excellent findings. Let me search for a few more specific topics that could be directly relevant to the proposal's novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23460d95-fa0f-4a32-b399-a6c949ad2852",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9x7Hq8pmG3X2bwPUsM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96b8cc40-900b-4b9f-8f19-7868c3495efc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgmbgM54rhPfzNEbu26UBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 15286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5221,
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

_source line 38 · 2026-05-28T14:51:39.045Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012VhnFWFEBwjQrFS4UTAAck`</summary>

```json
{
  "query": "MathAtlas 2605.14061 domain stratified evaluation 87 areas mathematics autoformalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b8cc40-900b-4b9f-8f19-7868c3495efc",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9x7Hq8pmG3X2bwPUsM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f726149c-f4c2-4dda-a5d7-e294dd8dde91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgmbgM54rhPfzNEbu26UBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 15286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5221,
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

_source line 39 · 2026-05-28T14:51:40.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PGSm9LnwrKpSavF6AHExjb`</summary>

```json
{
  "query": "\"domain-stratified\" OR \"domain stratified\" autoformalization evaluation benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f726149c-f4c2-4dda-a5d7-e294dd8dde91",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9x7Hq8pmG3X2bwPUsM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32c6dae6-793e-4391-9c6c-493e9a4bccf4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgmbgM54rhPfzNEbu26UBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 15286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5221,
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

_source line 40 · 2026-05-28T14:51:40.983Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DLNWWrZQXK5zMb9oMrkdM6`</summary>

```json
{
  "query": "\"Lean Atlas\" 2604.16347 human-AI collaborative formalization domain 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32c6dae6-793e-4391-9c6c-493e9a4bccf4",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9x7Hq8pmG3X2bwPUsM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f4655ad-697c-48e0-acff-970620a5148f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgmbgM54rhPfzNEbu26UBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 15286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5221,
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

_source line 41 · 2026-05-28T14:51:41.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FZ9xRfpFQn1VFP6Kmajy4v`</summary>

```json
{
  "query": "\"autoformalization\" \"domain adaptation\" OR \"domain-adaptive\" fine-tuning lean 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f4655ad-697c-48e0-acff-970620a5148f",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9x7Hq8pmG3X2bwPUsM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06cc1105-02c6-4334-8230-f757d05afc27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgmbgM54rhPfzNEbu26UBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 15286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5221,
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

_source line 42 · 2026-05-28T14:51:42.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LUr5Hb6xF62rL1Hng9c5cq`</summary>

```json
{
  "query": "autoformalization survey 2505.23486 2026 domain"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06cc1105-02c6-4334-8230-f757d05afc27",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9x7Hq8pmG3X2bwPUsM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20088080-89ee-4eff-b3ae-69fce5a7dd3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgmbgM54rhPfzNEbu26UBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5221,
      "cache_read_input_tokens": 15286,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 15286,
          "cache_creation_input_tokens": 5221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5221,
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

_source line 43 · 2026-05-28T14:51:45.668Z_

<details><summary>↩ Tool result · `toolu_012VhnFWFEBwjQrFS4UTAAck`</summary>

```text
Web search results for query: "MathAtlas 2605.14061 domain stratified evaluation 87 areas mathematics autoformalization"

Links: [{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Autoformalization of Mathematics","url":"https://www.emergentmind.com/topics/autoformalization-of-mathematics"},{"title":"Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency","url":"https://arxiv.org/pdf/2410.20936"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions","url":"https://arxiv.org/pdf/2502.12065"}]

Based on the search results, I found detailed information about MathAtlas and the paper 2605.14061:

## MathAtlas: A Benchmark for Autoformalization in the Wild

MathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

### Domain Coverage and Scope

Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others. The math texts cover subfields of algebra, analysis, geometry, number theory, probability, quantum theory, category theory, topology, and others, spanning a total of 87 fields and subfields of mathematics.

### Enriched Dependencies

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

### Baseline Performance

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions, demonstrating that MathAtlas is high quality but extremely challenging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f726149c-f4c2-4dda-a5d7-e294dd8dde91",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "fd5599c7-b148-4fb2-93b9-871b28410739",
  "sourceToolAssistantUUID": "f726149c-f4c2-4dda-a5d7-e294dd8dde91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T14:51:46.210Z_

<details><summary>↩ Tool result · `toolu_01PGSm9LnwrKpSavF6AHExjb`</summary>

```text
Web search results for query: ""domain-stratified" OR "domain stratified" autoformalization evaluation benchmark 2026"

Links: [{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4 | OpenReview","url":"https://openreview.net/forum?id=22ITxc8y5p"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/html/2406.06555v1"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/pdf/2512.00997"}]

Based on the search results, I found several relevant autoformalization evaluation benchmarks and papers from 2024-2026:

An evaluation benchmark for autoformalization in Lean4 proposes a benchmark of 101 pairs of mathematical formal-informal statements across 17 different topics, with manual evaluation of three state-of-the-art LLMs (GPT-3.5, GPT-4, and Gemini Pro).

Another benchmark study releases new benchmarks including a research-level mathematics dataset RLM25, a corrected ProofNet, and ProofNetVerif with labeled correct and incorrect autoformalization pairs for evaluating metrics.

Additionally, IndiMathBench presents a systematic formalization pipeline employing category-based retrieval, self-debug loops, and ensemble LLMs, includes a VS Code Extension for human-AI collaboration, and evaluates frontier models on autoformalization and proving capabilities.

However, I did not find specific results directly mentioning "domain-stratified" or "domain stratified" in the context of these benchmarks in these search results. If you're looking for information about a specific domain-stratified benchmark, please let me know and I can perform an additional search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32c6dae6-793e-4391-9c6c-493e9a4bccf4",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "6a943f9f-1d17-4faf-824f-135a7af70132",
  "sourceToolAssistantUUID": "32c6dae6-793e-4391-9c6c-493e9a4bccf4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T14:51:48.413Z_

<details><summary>↩ Tool result · `toolu_01DLNWWrZQXK5zMb9oMrkdM6`</summary>

```text
Web search results for query: ""Lean Atlas" 2604.16347 human-AI collaborative formalization domain 2026"

Links: [{"title":"[2604.16347] Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/abs/2604.16347"},{"title":"Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization","url":"https://arxiv.org/html/2604.16347v1"},{"title":"Architecture of Lean Atlas. The Lean 4 backend extracts and classifies... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Architecture-of-Lean-Atlas-The-Lean-4-backend-extracts-and-classifies-the-dependency_fig1_404020517"},{"title":"Human-AI Collaborative Uncertainty Quantification","url":"https://arxiv.org/pdf/2510.23476"},{"title":"LeanArchitect: Automating Blueprint Generation for Humans and AI","url":"https://arxiv.org/pdf/2601.22554"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.22554"},{"title":"Automatic Textbook Formalization","url":"https://api.emergentmind.com/papers/2604.03071"},{"title":"Semi-Autonomous Formalization of the Vlasov-Maxwell-Landau Equilibrium","url":"https://arxiv.org/pdf/2603.15929"}]

Based on the search results, here's information about Lean Atlas (arXiv:2604.16347):

## Overview

Lean Atlas is an integrated proof environment for scalable human-AI collaborative formalization, authored by Banri Yanahama and Akiyoshi Sannai and submitted on March 16, 2026.

## Problem and Approach

While the type checker of a proof assistant guarantees only the logical correctness of proofs, it does not verify whether propositions and definitions faithfully capture their intended mathematical content, so AI-generated formal proofs can exhibit semantic hallucination—passing the type checker yet failing to express the intended mathematics.

The paper proposes a human-in-the-loop approach in which human scientists and AI collaboratively produce formal proofs, with humans responsible for the semantic verification of propositions and definitions.

## Key Feature

Lean Atlas is a Lean 4 tool that visualizes the dependency graph of a Lean 4 project as an interactive web viewer, enabling human scientists to engage in the verification process effectively.

This tool addresses a critical gap in AI-driven mathematical formalization by introducing human oversight to catch semantic errors that automated type checkers cannot detect.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f4655ad-697c-48e0-acff-970620a5148f",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "dd8193af-8c22-452a-8d9f-c943bec6cb08",
  "sourceToolAssistantUUID": "3f4655ad-697c-48e0-acff-970620a5148f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T14:51:49.296Z_

<details><summary>↩ Tool result · `toolu_01FZ9xRfpFQn1VFP6Kmajy4v`</summary>

```text
Web search results for query: ""autoformalization" "domain adaptation" OR "domain-adaptive" fine-tuning lean 2026 arxiv"

Links: [{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"Lean-ing on Quality: How High-Quality Data Beats Diverse Multilingual Data in AutoFormalization","url":"https://arxiv.org/html/2502.15795"}]

I found several relevant papers on autoformalization and Lean 2026 on arXiv. Here are the key results:

## Most Recent Result (March 2026):

A paper titled "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning" (arXiv:2603.24372, March 25, 2026) presents a GRPO-based RL fine-tuning using cycle consistency as a reward, showing a 0.156 improvement in mean cycle consistency over the SFT baseline on held-out FLC data with minimal cross-entropy deterioration. The work uses Qwen3.5-2B as the base model with LoRA adapters.

## Related Autoformalization Research:

Fine-tuning approaches adapt pre-trained models to specialized domains (e.g., competition math) using smaller, task-specific datasets. Early work on autoformalization used retrieval and rule-based methods, whereas approaches using LLMs have recently gained popularity driven by the increase in the number of openly available large corpora of NL/Lean4 pairs.

FineLeanCorpus provides 509k pairs with difficulty ratings and domain labels for training data.

The search results confirm active research in domain-adaptive fine-tuning approaches for Lean autoformalization in 2026, with the most recent paper focusing on cycle consistency as an effective training signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06cc1105-02c6-4334-8230-f757d05afc27",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "c02eb37f-c1f6-4d3e-9367-4b23f1a9f2aa",
  "sourceToolAssistantUUID": "06cc1105-02c6-4334-8230-f757d05afc27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T14:51:49.801Z_

<details><summary>↩ Tool result · `toolu_01LUr5Hb6xF62rL1Hng9c5cq`</summary>

```text
Web search results for query: "autoformalization survey 2505.23486 2026 domain"

Links: [{"title":"[2505.23486v1] Autoformalization in the Era of Large Language Models: A Survey","url":"http://arxiv.org/abs/2505.23486v1"},{"title":"[2505.23486] Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/abs/2505.23486"},{"title":"[2505.23486v2] Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/abs/2505.23486v2"},{"title":"Autoformalization in the Era of Large Language Models: A Survey | Request PDF","url":"https://www.researchgate.net/publication/392204482_Autoformalization_in_the_Era_of_Large_Language_Models_A_Survey"},{"title":"Autoformalization in the Era of Large Language Models","url":"https://arxiv.org/pdf/2505.23486"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/html/2509.09810v2"},{"title":"Towards a Common Framework for Autoformalization","url":"https://ojs.aaai.org/index.php/AAAI/article/view/42132/46093"}]

Based on the search results, I found information about the arxiv paper 2505.23486:

This is a survey paper titled "Autoformalization in the Era of Large Language Models" that covers autoformalization, the process of transforming informal mathematical propositions into verifiable formal representations, which is a foundational task in automated theorem proving.

The paper notes that this field has witnessed substantial growth driven by rapid progress in artificial intelligence, particularly large language models (LLMs), bringing both new opportunities and unique challenges.

The survey examines how autoformalization is applied across various mathematical domains and levels of difficulty, and analyzes the end-to-end workflow from data preprocessing to model design and evaluation.

It further explores the emerging role of autoformalization in enhancing the verifiability of LLM-generated outputs, highlighting its potential to improve both trustworthiness and related aspects.

The paper was submitted on May 29, 2025 and last revised on July 3, 2025, and was authored by Ke Weng, Lun Du, Sirui Li, Wangyue Lu, Haozhe Sun, Hengyu Liu, and Tiancheng Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20088080-89ee-4eff-b3ae-69fce5a7dd3b",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "8fe22a09-dc81-44ae-a489-bad6f299bdc6",
  "sourceToolAssistantUUID": "20088080-89ee-4eff-b3ae-69fce5a7dd3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-28T14:51:52.634Z_

Let me run a few more targeted searches to cover remaining angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fe22a09-dc81-44ae-a489-bad6f299bdc6",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9yCLiXTp6F3MiK3Fth",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a40891a-34b7-47dc-a531-1429e43e8f25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RasVECGb8S5SUEQSCFzciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3708,
      "cache_read_input_tokens": 20507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3708,
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

_source line 49 · 2026-05-28T14:51:53.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011A7514RgEm7YRokJSmu6zS`</summary>

```json
{
  "query": "Construction-Verification benchmark applied mathematics lean 4 2602.01291 domain 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a40891a-34b7-47dc-a531-1429e43e8f25",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9yCLiXTp6F3MiK3Fth",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebce563d-ca22-4bae-aaa0-a849dabff8c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RasVECGb8S5SUEQSCFzciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3708,
      "cache_read_input_tokens": 20507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3708,
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

_source line 50 · 2026-05-28T14:51:54.639Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015eaQVwyDqpb1ndw41HRBs6`</summary>

```json
{
  "query": "\"domain-aware\" OR \"domain-conditioned\" autoformalization retrieval formalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebce563d-ca22-4bae-aaa0-a849dabff8c3",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9yCLiXTp6F3MiK3Fth",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b0c2b83-4ab1-4bf3-afee-4c812f84293f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RasVECGb8S5SUEQSCFzciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3708,
      "cache_read_input_tokens": 20507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3708,
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

_source line 51 · 2026-05-28T14:51:55.643Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017dhvkAmmJ1CGeVutJTrSnT`</summary>

```json
{
  "query": "ProofBridge 2510.15681 autoformalization joint embeddings lean domain 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b0c2b83-4ab1-4bf3-afee-4c812f84293f",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9yCLiXTp6F3MiK3Fth",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3deea0a-5519-4de7-b4a9-7e3167e6a4d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RasVECGb8S5SUEQSCFzciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3708,
      "cache_read_input_tokens": 20507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3708,
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

_source line 52 · 2026-05-28T14:51:56.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vpcs3ATZhZCjAaDvVCcUn4`</summary>

```json
{
  "query": "\"error analysis\" \"mathematical domain\" autoformalization lean performance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3deea0a-5519-4de7-b4a9-7e3167e6a4d1",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9yCLiXTp6F3MiK3Fth",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46335b5d-d78b-46a9-bef2-a8119f1db1b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RasVECGb8S5SUEQSCFzciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3708,
      "cache_read_input_tokens": 20507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3708,
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

_source line 53 · 2026-05-28T14:51:56.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TBhCPZQdusu6jNH3Pc4DAc`</summary>

```json
{
  "query": "autoformalization \"per domain\" OR \"by domain\" OR \"across domains\" performance lean 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46335b5d-d78b-46a9-bef2-a8119f1db1b2",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9yCLiXTp6F3MiK3Fth",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d032a424-1c0b-40a1-bef0-8af2990a43d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RasVECGb8S5SUEQSCFzciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3708,
      "cache_read_input_tokens": 20507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3708,
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

_source line 54 · 2026-05-28T14:52:01.165Z_

<details><summary>↩ Tool result · `toolu_011A7514RgEm7YRokJSmu6zS`</summary>

```text
Web search results for query: "Construction-Verification benchmark applied mathematics lean 4 2602.01291 domain 2026"

Links: [{"title":"[2602.01291] Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/abs/2602.01291"},{"title":"A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/pdf/2602.01291"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291"},{"title":"[2605.17255] CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/abs/2605.17255"},{"title":"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/html/2605.17255"},{"title":"[2602.18307] VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean","url":"https://arxiv.org/abs/2602.18307"},{"title":"VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean","url":"https://arxiv.org/pdf/2602.18307"},{"title":"VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean","url":"https://arxiv.org/html/2602.18307v1"},{"title":"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language   Models","url":"https://arxiv.org/pdf/2505.02735"}]

Based on the search results, here's what I found about the paper with ID 2602.01291:

The paper is titled "Construction-Verification: A Benchmark for Applied Mathematics in Lean 4" and was authored by Bowen Yang and 7 other authors. The paper was submitted on February 1, 2026.

The paper introduces a Lean 4 framework that enforces a construction-verification workflow, compelling the agent to define explicit solutions before proving their correctness. Existing benchmarks focus on logical verification of declarative propositions, often neglecting the task of explicitly synthesizing solutions, which is particularly important in applied mathematics domains where the goal is to derive concrete values or executable algorithms rather than solely proving theorems.

The paper curates a comprehensive benchmark called AMBER (Applied Mathematics BEnchmark for Reasoning) spanning core domains of applied mathematics, including convex analysis, optimization, and numerical (the excerpt appears to be cut off).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebce563d-ca22-4bae-aaa0-a849dabff8c3",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "de302966-ce8a-4a6b-b4c8-fd480f429083",
  "sourceToolAssistantUUID": "ebce563d-ca22-4bae-aaa0-a849dabff8c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T14:52:01.460Z_

<details><summary>↩ Tool result · `toolu_015eaQVwyDqpb1ndw41HRBs6`</summary>

```text
Web search results for query: ""domain-aware" OR "domain-conditioned" autoformalization retrieval formalization 2026"

Links: [{"title":"AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...","url":"https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=09lmwhDqZ3"},{"title":"[2508.06931] Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/abs/2508.06931"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/html/2509.09810v1"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"}]

Based on the search results, here are the key findings related to domain-aware/domain-conditioned autoformalization and retrieval in 2026:

## Key Research Work

A framework introduces a concept-definition knowledge base from Mathlib4 for the Lean 4 theorem prover, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts, and proposes contextual query augmentation with domain- and application-level signals to address conceptual polymorphism.

The research designs a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval, achieving up to 62.1% and an average of 29.9% relative improvement when integrated into LLM-based autoformalizers.

## Specific Framework (CRAMF)

The Concept-driven Retrieval-Augmented Mathematical Formalization (CRAMF) framework retrieves precise formal definitions of core mathematical concepts to provide contextual grounding for LLM-based autoformalization.

The framework includes a module that provides domain knowledge and application contexts for mathematical concepts to effectively resolve definition ambiguity.

These appear to be recent developments under review for ICLR 2026, representing the state-of-the-art in domain-aware retrieval-augmented approaches to autoformalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b0c2b83-4ab1-4bf3-afee-4c812f84293f",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "cfc4e3aa-fde6-4a4b-a395-f5bafaf589a6",
  "sourceToolAssistantUUID": "9b0c2b83-4ab1-4bf3-afee-4c812f84293f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-28T14:52:03.086Z_

<details><summary>↩ Tool result · `toolu_01Vpcs3ATZhZCjAaDvVCcUn4`</summary>

```text
Web search results for query: ""error analysis" "mathematical domain" autoformalization lean performance 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/html/2406.06555v1"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/html/2511.03108v1"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"}]

I've found several relevant resources on autoformalization in Lean and error analysis in mathematical domains. Here's what the search results show:

## Key 2026 Developments

Recent autoformalization systems utilizing Lean 4 include AlphaProof, an AlphaZero-inspired agent that learns to find formal proofs through reinforcement learning by training on millions of auto-formalized problems.

## Error Analysis and Mathematical Domains

Research highlights the types of mathematical domains where current autoformalizers struggle the most, providing guidance for future work. More specifically, Olympiad-style geometry and combinatorics remain underrepresented across existing Lean 4 benchmarks, with these being among the hardest domains for both ATPs and LLM-guided provers.

## Evaluation Approaches

Autoformalizations are evaluated on a 0-4 scale based on correction effort—the amount of necessary adjustments or modifications required to transform the generated formalization output of an LLM into an accurate and fully correct Lean4 formalization.

## Performance Metrics

Through sampling, autoformalization accuracy can be substantially increased, with GPT-4 improving from 31.0% to 45.1% accuracy on the ProofNet benchmark using 50 samples.

The search results indicate active research into understanding error patterns across different mathematical domains and improving autoformalization performance in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46335b5d-d78b-46a9-bef2-a8119f1db1b2",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "5aec0b88-d925-4a13-a4a4-5486837d7c97",
  "sourceToolAssistantUUID": "46335b5d-d78b-46a9-bef2-a8119f1db1b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T14:52:03.584Z_

<details><summary>↩ Tool result · `toolu_017dhvkAmmJ1CGeVutJTrSnT`</summary>

```text
Web search results for query: "ProofBridge 2510.15681 autoformalization joint embeddings lean domain 2026"

Links: [{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | OpenReview","url":"https://openreview.net/forum?id=U2jxHXuOX9"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"Paper page - ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://huggingface.co/papers/2510.15681"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"José A. Alonso on X: \"ProofBridge: Auto-formalization of natural language proofs in Lean via joint embeddings. ~ Prithwish Jana et als. https://t.co/cXfy31wRup #ITP #LeanProver #Autoformalization #LLMs #Math\" / X","url":"https://x.com/Jose_A_Alonso/status/1980233551749808484"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | Request PDF","url":"https://www.researchgate.net/publication/396693100_ProofBridge_Auto-Formalization_of_Natural_Language_Proofs_in_Lean_via_Joint_Embeddings"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"GitHub - shreyascasturi/proofbridge-nesy-2026: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/shreyascasturi/proofbridge-nesy-2026"}]

I found comprehensive results for your search. Here's what ProofBridge 2510.15681 is about:

## Overview

ProofBridge is a unified framework for automatically translating entire NL theorems and proofs into Lean 4. In practice, auto-formalization of both theorem and proof still requires human intervention, as seen in AlphaProof's silver-medal performance at the 2024 IMO, where problem statements were manually translated before automated proof synthesis.

## Key Technical Components

At its core is a joint embedding model that aligns NL and FL (NL-FL) theorem-proof pairs in a shared semantic space, enabling cross-modal retrieval of semantically relevant FL examples to guide translation.

ProofBridge integrates retrieval-augmented fine-tuning with iterative proof repair, leveraging Lean's type checker and semantic equivalence feedback to ensure both syntactic correctness and semantic fidelity.

## Performance

Experiments show substantial improvements in proof auto-formalization over strong baselines (including GPT-5, Gemini-2.5, Kimina-Prover, DeepSeek-Prover), with their retrieval-augmented approach yielding significant gains in semantic correctness and type correctness across pass@k metrics.

The paper (arXiv:2510.15681) was published for the ICLR-2026 main track and is available on arxiv.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3deea0a-5519-4de7-b4a9-7e3167e6a4d1",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "c5308c25-032b-4a0b-8495-b1e57f45e0c0",
  "sourceToolAssistantUUID": "d3deea0a-5519-4de7-b4a9-7e3167e6a4d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T14:52:03.912Z_

<details><summary>↩ Tool result · `toolu_01TBhCPZQdusu6jNH3Pc4DAc`</summary>

```text
Web search results for query: "autoformalization "per domain" OR "by domain" OR "across domains" performance lean 2026"

Links: [{"title":"Lean for Science Formalization Przemyslaw Chojecki ulam.ai February 18, 2026","url":"https://www.ulam.ai/research/lean-science.pdf"},{"title":"Autoformalization with Large Language Models","url":"https://www.emergentmind.com/topics/autoformalization-with-large-language-models"},{"title":"Lean Workbook: Autoformalized Math Problems","url":"https://www.emergentmind.com/topics/lean-workbook"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

I found several relevant search results on autoformalization and Lean performance. Here are the key findings:

## Per-Domain Performance in Autoformalization

LLMs show subject-dependent performance disparities in autoformalization, with all models excelling in Information Theory and Logic, but struggling with category and model theory. The frequency of these subjects on the internet appears to be related to LLM performance.

In the Lean-Workbook dataset, per-tag sampled formalization accuracy varies by domain: inequality (10/10), algebra (9/10), and number theory (9/10), yielding a weighted average of 93.5%.

## Recent Autoformalization Research (2026)

A recent February 2026 paper synthesizes evidence across physics, chemistry, biology, and economics, proposing a mathematics-first transfer strategy for autoformalization beyond mathematics by training autoformalization agents on mathematics and then porting the same agents to other domains.

A proposed SciAF (Science Autoformalization) framework extends standard autoformalization with domain validity predicates and explicit trust accounting to reflect scientific needs like units, shapes, state invariants, and numeric boundaries.

## Cross-Domain Language Support

Target formal languages and encoding schemes vary by domain: Mathematics uses Higher-Order Logic (Lean, Isabelle, Coq), while Planning uses PDDL and temporal extensions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d032a424-1c0b-40a1-bef0-8af2990a43d2",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "265780dc-ce75-4b3b-a993-81be9a142618",
  "sourceToolAssistantUUID": "d032a424-1c0b-40a1-bef0-8af2990a43d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-28T14:52:07.522Z_

Let me run a final round of targeted searches on the most relevant leads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "265780dc-ce75-4b3b-a993-81be9a142618",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9zEf9WbUYNG7K79BaQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27d8f136-225c-493c-b28f-18a051bc5082",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ABGrNfAzZ8WfH1ZxRiMeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4039,
      "cache_read_input_tokens": 24215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4039,
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

_source line 60 · 2026-05-28T14:52:08.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DVt7R8UkV2NoJP9x1JQxnN`</summary>

```json
{
  "query": "CRAMF \"conceptual retrieval\" autoformalization domain signals lean mathlib ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27d8f136-225c-493c-b28f-18a051bc5082",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9zEf9WbUYNG7K79BaQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38feb147-f7b3-41e4-9c4d-6242db0f982e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ABGrNfAzZ8WfH1ZxRiMeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4039,
      "cache_read_input_tokens": 24215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4039,
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

_source line 61 · 2026-05-28T14:52:09.468Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FYnAf4NRr8XuFMnweRowhq`</summary>

```json
{
  "query": "CAM-Bench 2605.17255 computational applied mathematics lean benchmark domain 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38feb147-f7b3-41e4-9c4d-6242db0f982e",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9zEf9WbUYNG7K79BaQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e45b80eb-5130-41d0-af4b-b7fe8b8c9c19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ABGrNfAzZ8WfH1ZxRiMeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4039,
      "cache_read_input_tokens": 24215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4039,
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

_source line 62 · 2026-05-28T14:52:10.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWojskEV1VLy2EyTUkPLAL`</summary>

```json
{
  "query": "Aria dependency graph autoformalization retrieval 2510.04520 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e45b80eb-5130-41d0-af4b-b7fe8b8c9c19",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9zEf9WbUYNG7K79BaQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5f2623f-6d3b-417d-86a0-c2106431b25f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ABGrNfAzZ8WfH1ZxRiMeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4039,
      "cache_read_input_tokens": 24215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4039,
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

_source line 63 · 2026-05-28T14:52:11.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JHjG9XXB4TY7n8uU8jSURz`</summary>

```json
{
  "query": "\"domain-specific\" \"error\" \"formalization\" lean analysis taxonomy categories 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5f2623f-6d3b-417d-86a0-c2106431b25f",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbV9zEf9WbUYNG7K79BaQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31f834f3-c7c2-4afd-92de-284023e0de09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ABGrNfAzZ8WfH1ZxRiMeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4039,
      "cache_read_input_tokens": 24215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4039,
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

_source line 64 · 2026-05-28T14:52:15.332Z_

<details><summary>↩ Tool result · `toolu_01DVt7R8UkV2NoJP9x1JQxnN`</summary>

```text
Web search results for query: "CRAMF "conceptual retrieval" autoformalization domain signals lean mathlib ICLR 2026"

Links: [{"title":"AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...","url":"https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=09lmwhDqZ3"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/pdf/2508.06931"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"[2508.06931] Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/abs/2508.06931"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | Request PDF","url":"https://www.researchgate.net/publication/394440359_Automated_Formalization_via_Conceptual_Retrieval-Augmented_LLMs"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.15940"}]

Based on the search results, I found relevant information about CRAMF:

CRAMF is a Concept-driven Retrieval-Augmented Mathematical Formalization framework that enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation.

The framework automatically constructs a concept-definition knowledge base from Mathlib4, the standard mathematical library for the Lean 4 theorem prover, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts.

To address conceptual polymorphism, the framework proposes contextual query augmentation with domain- and application-level signals, and designs a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval.

Experiments on miniF2F, ProofNet, and a newly proposed AdvancedMath benchmark show that CRAMF can be seamlessly integrated into LLM-based autoformalizers, yielding consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement.

The paper appears to have been published at ICLR 2026 based on the search results from OpenReview and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38feb147-f7b3-41e4-9c4d-6242db0f982e",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "10e87474-6852-4426-8c36-b359dcd17e83",
  "sourceToolAssistantUUID": "38feb147-f7b3-41e4-9c4d-6242db0f982e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-28T14:52:15.905Z_

<details><summary>↩ Tool result · `toolu_01FYnAf4NRr8XuFMnweRowhq`</summary>

```text
Web search results for query: "CAM-Bench 2605.17255 computational applied mathematics lean benchmark domain 2026"

Links: [{"title":"[2605.17255] CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/abs/2605.17255"},{"title":"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/html/2605.17255"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291v1"},{"title":"Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/pdf/2602.01291"},{"title":"A Combinatorial Identities Benchmark for Theorem Proving via Automated   Theorem Generation","url":"https://arxiv.org/pdf/2502.17840"}]

Based on the search results, here's what I found about CAM-Bench 2605.17255:

CAM-Bench is a Lean 4 theorem-proving benchmark of 1,000 Lean proof targets in computational and applied mathematics, with coverage spanning optimization, numerical linear algebra, and numerical analysis.

Existing benchmarks mainly focus on Olympiad-style problems and algebraic domains, leaving computational and applied mathematics underrepresented, which is the gap this benchmark aims to address.

The problems are adapted from textbook exercises and often depend on locally introduced definitions, notation, algorithms, and elementary results. To construct CAM-Bench, the developers created a dependency-recovery pipeline that reconstructs the local textbook context needed to state each problem faithfully, then normalizes each problem into a standalone informal theorem and translates it into a Lean target.

The paper was submitted on May 17, 2026, with authors from Fudan University, Qingdao University, Peking University, and Huawei Technologies Ltd. The benchmark is open-sourced and available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e45b80eb-5130-41d0-af4b-b7fe8b8c9c19",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "a504843c-69b4-4770-9407-3a8914de6809",
  "sourceToolAssistantUUID": "e45b80eb-5130-41d0-af4b-b7fe8b8c9c19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T14:52:16.158Z_

<details><summary>↩ Tool result · `toolu_01GWojskEV1VLy2EyTUkPLAL`</summary>

```text
Web search results for query: "Aria dependency graph autoformalization retrieval 2510.04520 2026"

Links: [{"title":"[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520v1"},{"title":"[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251004520W/abstract"},{"title":"(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"},{"title":"Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/pdf/2511.11990"},{"title":"(PDF) Improving Autoformalization Using Direct Dependency Retrieval","url":"https://www.researchgate.net/publication/397701226_Improving_Autoformalization_Using_Direct_Dependency_Retrieval"},{"title":"[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"},{"title":"ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://iclr.cc/virtual/2026/poster/10010860"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE","url":"https://arxiv.org/pdf/2510.04520"}]

Based on the search results, I found detailed information about the paper 2510.04520:

## Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph

Aria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

**Problem Being Addressed:**
Accurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.

**Key Innovation:**
The system introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.

**Results:**
On ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.

**Paper Details:**
The paper was submitted on October 6, 2025 by authors Hanyu Wang, Ruohan Xie, Yutong Wang, Guoxiong Gao, Xintao Yu, and Bin Dong.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5f2623f-6d3b-417d-86a0-c2106431b25f",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "76805b55-730f-4025-b93a-e0307bf003e7",
  "sourceToolAssistantUUID": "d5f2623f-6d3b-417d-86a0-c2106431b25f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-28T14:52:18.212Z_

<details><summary>↩ Tool result · `toolu_01JHjG9XXB4TY7n8uU8jSURz`</summary>

```text
Web search results for query: ""domain-specific" "error" "formalization" lean analysis taxonomy categories 2026 arxiv"

Links: [{"title":"Formalization of De Giorgi--Nash--Moser Theory in Lean - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260405984A/abstract"},{"title":"Formal Error Taxonomy","url":"https://www.emergentmind.com/topics/formal-error-taxonomy"},{"title":"Lean Formalization of Generalization Error Bound by Rademacher Complexity and Dudley’s Entropy Integral","url":"https://arxiv.org/html/2503.19605"},{"title":"Lean Formalization of Generalization Error Bound by Rademacher Complexity","url":"https://arxiv.org/pdf/2503.19605"},{"title":"[2503.19605] Lean Formalization of Generalization Error Bound by Rademacher Complexity and Dudley's Entropy Integral","url":"https://arxiv.org/abs/2503.19605"},{"title":"Semi-Autonomous Formalization of the Vlasov-Maxwell-Landau Equilibrium","url":"https://arxiv.org/html/2603.15929v2"},{"title":"From Euler to Today: Universal Mathematical Fallibility A Large-Scale Computational Analysis of Errors in ArXiv Papers","url":"https://arxiv.org/pdf/2511.10543"}]

Based on the search results, I found several relevant arxiv papers from 2026 related to Lean formalization and error analysis:

## Key Results:

A formalization in Lean of the core interior De Giorgi--Nash--Moser theory for uniformly elliptic divergence-form equations with bounded measurable coefficients (arxiv 2604.05984, April 2026).

A formalization of the generalization error bound by Rademacher complexity in Lean 4, building on measure-theoretic probability theory available in the Mathlib library (arxiv 2503.19605). This paper addresses a key challenge: statistical learning theory contains many domain-specific terms that often cause confusion, such as "data," "model," "random," "error," "hypothesis," "concept," and "risk" which are defined differently than in neighboring fields.

Additionally, Formal error taxonomies are anchored in domain-specific theories and represent a rigorously defined hierarchical framework that categorizes and analyzes error phenomena, employing structured layers, formal definitions, and logical notations to ensure accurate classification and reproducibility.

The search results show active work in 2026 on Lean formalization projects dealing with error analysis, complexity bounds, and domain-specific terminology challenges in mathematical domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31f834f3-c7c2-4afd-92de-284023e0de09",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "ac1b5fe532ebdaa7c",
  "type": "user",
  "uuid": "14cf1d21-25e6-482c-a783-9cb374b0519c",
  "sourceToolAssistantUUID": "31f834f3-c7c2-4afd-92de-284023e0de09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-28T14:53:26.908Z_

I now have a comprehensive picture. Here is my full report.

---

## Concurrent Work Report: Domain-Adaptive Autoformalization for Lean 4 (March--May 2026)

I searched extensively across seven query categories and multiple follow-up queries. Below are the findings organized by relevance to your proposal's core novelty claims.

---

### 1. HIGHEST RELEVANCE -- Papers that directly overlap with or threaten novelty claims

#### CRAMF: Concept-driven Retrieval-Augmented Mathematical Formalization (ICLR 2026)
- [arXiv:2508.06931](https://arxiv.org/abs/2508.06931) / [OpenReview](https://openreview.net/forum?id=09lmwhDqZ3)
- **Published at ICLR 2026 (main conference).**
- Builds a concept-definition knowledge base from Mathlib4 (26,000+ formal definitions, 1,000+ core concepts). Proposes **contextual query augmentation with domain- and application-level signals** to resolve conceptual polymorphism. Uses a dual-channel hybrid retrieval strategy with reranking.
- **Threat to novelty:** This directly addresses domain-aware retrieval for autoformalization. If the proposal claims domain-conditioned retrieval as novel, CRAMF is strong prior/concurrent work that must be cited and differentiated from. CRAMF achieves up to 62.1% relative improvement on miniF2F, ProofNet, and an AdvancedMath benchmark.

#### MathAtlas: A Benchmark for Autoformalization in the Wild (May 2026)
- [arXiv:2605.14061](https://arxiv.org/abs/2605.14061)
- First large-scale benchmark of graduate-level math autoformalization: ~52k entities from 103 textbooks, spanning **87 areas of mathematics** (real analysis, differential geometry, category theory, topology, quantum groups, etc.). Includes a dependency graph with ~178k relations.
- **Threat to novelty:** If the proposal claims to introduce domain-stratified evaluation for autoformalization, MathAtlas already provides a benchmark organized across 87 mathematical subfields with dependency-aware structure. Strong baselines achieve only 9.8% on theorems and 16.7% on definitions, demonstrating domain-stratified difficulty variation.

#### "Do LLMs Game Formalization?" (VerifAI-2 Workshop, ICLR 2026, April 2026)
- [arXiv:2604.19459](https://arxiv.org/abs/2604.19459)
- Introduces an **error taxonomy for formalization faithfulness** with categories: CONCLUSION AS AXIOM, FABRICATED CONTRADICTION, FABRICATED WORLD KNOWLEDGE, FABRICATED INVENTED, plus mistranslation and omission categories.
- **Threat to novelty:** If the proposal claims a novel error taxonomy for autoformalization, this paper provides a structured taxonomy specifically for formalization faithfulness errors. The taxonomy is applied to GPT-5 and DeepSeek-R1, revealing distinct failure modes.

---

### 2. HIGH RELEVANCE -- Papers that partially overlap

#### DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)
- [arXiv:2510.10815](https://arxiv.org/abs/2510.10815) / [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010321)
- Decomposes informal statements into sub-queries, performs **targeted premise retrieval from Mathlib**, and retrieves illustrative theorems to guide formalization. Nearly doubles F1 score vs. DPR baseline on ProofNet.
- **Relevance:** Overlaps with any domain-aware retrieval-for-formalization claims, though DRIFT's decomposition is statement-level rather than domain-level.

#### Aria: Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)
- [arXiv:2510.04520](https://arxiv.org/abs/2510.04520) / [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010860)
- Uses a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and constructing formalizations from grounded concepts. AriaScorer retrieves definitions from Mathlib for term-level grounding. Achieves 91.6% compilation and 68.5% accuracy on ProofNet.
- **Relevance:** Dependency-graph-based retrieval for autoformalization is closely related to domain-aware retrieval approaches.

#### ProofBridge: Auto-Formalization of NL Proofs in Lean via Joint Embeddings (ICLR 2026 main track)
- [arXiv:2510.15681](https://arxiv.org/abs/2510.15681)
- Joint embedding model aligning NL and FL theorem-proof pairs; cross-modal retrieval of semantically relevant FL examples; iterative proof repair with Lean's type checker. Outperforms GPT-5, Gemini-2.5, Kimina-Prover, DeepSeek-Prover.
- **Relevance:** Retrieval-augmented autoformalization with semantic alignment, though not explicitly domain-conditioned.

#### LeanSearch v2: Global Premise Retrieval for Lean 4 (May 2026)
- [arXiv:2605.13137](https://arxiv.org/abs/2605.13137)
- State-of-the-art Mathlib premise retrieval **without domain-specific fine-tuning**. Reasoning mode uses iterative sketch-retrieve-reflect cycles. Recovers 46.1% of ground-truth premise groups within top-10.
- **Relevance:** Sets the retrieval baseline that any domain-conditioned retrieval approach must beat.

---

### 3. MODERATE RELEVANCE -- Domain-specific benchmarks and tools

#### CAM-Bench: Computational and Applied Mathematics in Lean (May 2026)
- [arXiv:2605.17255](https://arxiv.org/abs/2605.17255)
- 1,000 Lean proof targets in optimization, numerical linear algebra, and numerical analysis. Addresses underrepresentation of applied math in existing benchmarks. Uses a dependency-recovery pipeline.
- **Relevance:** Another domain-stratified benchmark, though focused on computational/applied math rather than broad domain coverage.

#### Construction-Verification / AMBER Benchmark (February 2026)
- [arXiv:2602.01291](https://arxiv.org/abs/2602.01291)
- Lean 4 framework for applied mathematics spanning convex analysis, optimization, numerical methods. Enforces construction-verification workflow.
- **Relevance:** Domain-specific benchmark for applied math formalization.

#### FormalEvolve: Neuro-Symbolic Evolutionary Search (March 2026)
- [arXiv:2603.19828](https://arxiv.org/abs/2603.19828)
- Evolutionary framework for autoformalization using LLM-driven mutation/crossover with AST rewrite operations. Achieves 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet.
- **Relevance:** Novel search-based autoformalization approach; not domain-adaptive but relevant as a concurrent method.

#### Cycle Consistency Fine-tuning for Lean4 Autoformalization (March 2026)
- [arXiv:2603.24372](https://arxiv.org/abs/2603.24372)
- RL fine-tuning (GRPO) with cycle consistency reward on Qwen3.5-2B/LoRA for NL-to-Lean4 translation. Notes that FineLeanCorpus provides 509k pairs **with domain labels**.
- **Relevance:** The existence of domain labels in FineLeanCorpus means domain-conditioned training is straightforward; if the proposal relies on creating domain-labeled data, this is prior art.

#### Lean Atlas: Human-AI Collaborative Formalization (March/April 2026)
- [arXiv:2604.16347](https://arxiv.org/abs/2604.16347)
- Lean 4 tool for visualizing dependency graphs as interactive web viewers; human-in-the-loop semantic verification to catch AI hallucinations.
- **Relevance:** Addresses semantic faithfulness in formalization through human oversight rather than domain adaptation.

#### MerLean: Autoformalization for Quantum Computation (February 2026)
- [arXiv:2602.16554](https://arxiv.org/abs/2602.16554)
- Domain-specific autoformalization agent for quantum computing; produced 2,050 Lean declarations from 114 statements across 3 papers.
- **Relevance:** A concrete example of domain-specific autoformalization, though for a single domain (quantum).

---

### 4. CONTEXTUAL -- Surveys and broader landscape

#### Autoformalization in the Era of LLMs: A Survey (May 2025, revised July 2025)
- [arXiv:2505.23486](https://arxiv.org/abs/2505.23486)
- Comprehensive survey covering data preprocessing, model design, and evaluation across domains and difficulty levels. Examines domain-specific performance disparities: models excel in Information Theory and Logic but struggle with category theory and model theory.
- **Relevance:** The survey already documents domain-dependent performance gaps, which is relevant context for any domain-adaptive proposal.

#### SciAF Framework / Lean for Science (February 2026)
- [PDF](https://www.ulam.ai/research/lean-science.pdf)
- Proposes mathematics-first transfer for autoformalization beyond math: train on math, then port to physics, chemistry, biology, economics. Includes domain validity predicates.
- **Relevance:** Cross-domain transfer for autoformalization is a related direction.

---

### Summary Assessment of Novelty Threats

| Proposal Claim | Concurrent Work | Severity |
|---|---|---|
| Domain-conditioned retrieval for autoformalization | **CRAMF (ICLR 2026)** -- domain/application-level query augmentation with Mathlib retrieval | **HIGH** -- must differentiate |
| Domain-stratified error analysis | **"Do LLMs Game Formalization?" (ICLR 2026 workshop)** -- formalization error taxonomy | **MEDIUM-HIGH** -- different angle (faithfulness vs. domain) but overlapping |
| Domain-stratified evaluation benchmark | **MathAtlas (May 2026)** -- 87 math areas, 52k entities | **HIGH** -- must cite and explain differentiation |
| Domain-adaptive fine-tuning | **Cycle Consistency (March 2026)** -- FineLeanCorpus already has domain labels | **MEDIUM** -- domain labels exist; what's novel in the adaptation method? |
| Dependency-aware retrieval for formalization | **Aria (ICLR 2026)**, **DRIFT (ICLR 2026)**, **LeanSearch v2 (May 2026)** | **MEDIUM** -- crowded space for retrieval-augmented formalization |

The most critical papers to address are **CRAMF**, **MathAtlas**, and the **"Do LLMs Game Formalization?"** error taxonomy paper. The proposal should clearly articulate how its domain-adaptive approach differs from CRAMF's domain-level query augmentation, how its evaluation strategy goes beyond MathAtlas's 87-area coverage, and how its error taxonomy is distinct from the faithfulness taxonomy in the ICLR 2026 workshop paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14cf1d21-25e6-482c-a783-9cb374b0519c",
  "isSidechain": true,
  "agentId": "ac1b5fe532ebdaa7c",
  "requestId": "req_011CbVA1HmTNVSVSZMz72vXm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9518ed26-c7d3-434f-a4dc-160136ae85e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjz2cdtzAXWZeb3sSmHN6f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3145,
      "cache_read_input_tokens": 28254,
      "output_tokens": 2831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3145
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2831,
          "cache_read_input_tokens": 28254,
          "cache_creation_input_tokens": 3145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3145,
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
