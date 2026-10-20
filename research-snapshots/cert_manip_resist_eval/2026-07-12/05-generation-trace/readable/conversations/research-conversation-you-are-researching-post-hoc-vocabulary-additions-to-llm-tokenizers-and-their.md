# Research conversation: You are researching post-hoc vocabulary additions to LLM tokenizers and their effects on downstream reasoning tasks. Con

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 1
- **Tool calls:** 39
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a750ba1644a9199d8.jsonl`
- **Structured JSON:** [`8c4c18baf68b747049cd.json`](../../sessions/8c/8c4c18baf68b747049cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

92 recorded events

### User

_source line 1 · 2026-05-19T23:31:30.268Z_

You are researching post-hoc vocabulary additions to LLM tokenizers and their effects on downstream reasoning tasks.

Context: Churchill & Skiena (2026) "Reducing Tokenization Premiums for Low-Resource Languages" showed that post-hoc vocabulary additions produce similar hidden states in LLaMA 3.2 1B. A reviewer noted this has ONLY been validated via hidden state similarity on a 1B model, never on downstream reasoning tasks on 235B-scale models.

Research deeply:
1. The Churchill & Skiena 2026 paper - what exactly did they do? What was validated?
2. Other work on modifying tokenizer vocabularies post-training
3. Has anyone shown vocabulary additions help on downstream reasoning benchmarks (MGSM, MMLU, etc.)?
4. What happens when you add tokens to a tokenizer without retraining the model? Does it break reasoning?
5. "Token healing" or "token merging" approaches
6. Any work on tokenizer swapping or adaptation for multilingual models

Search for:
- "Reducing Tokenization Premiums Low-Resource Languages" Churchill Skiena 2026
- "post-hoc vocabulary addition language model reasoning"
- "tokenizer adaptation without retraining downstream tasks"
- "vocabulary expansion multilingual LLM benchmark performance"
- "One Tokenizer To Rule Them All" ICLR 2026

Use WebFetch to read relevant papers. Report with specific details about what has and hasn't been validated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "a8464977-e95f-4de7-a4f9-d18315d849ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T23:31:30.273Z_

```json
{
  "parentUuid": "a8464977-e95f-4de7-a4f9-d18315d849ca",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
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
  "uuid": "3d07847f-d3f2-4ead-b02c-caca75fb453b",
  "timestamp": "2026-05-19T23:31:30.273Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T23:31:30.275Z_

```json
{
  "parentUuid": "3d07847f-d3f2-4ead-b02c-caca75fb453b",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d76f5373-95bf-46dd-9347-8ebc1ef7180e",
  "timestamp": "2026-05-19T23:31:30.275Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T23:31:33.285Z_



I'll research this topic thoroughly. Let me start by loading the WebSearch and WebFetch tools, then conduct multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d76f5373-95bf-46dd-9347-8ebc1ef7180e",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKQLaq2igMsaZTxWF9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681d0e75-8886-4b5f-9944-4f3bd58e8130",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZUmLxeY5ojEWyMZjBApxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1652,
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

_source line 5 · 2026-05-19T23:31:33.496Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R9QChThtjRTF3PhbxNecmH`</summary>

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
  "parentUuid": "681d0e75-8886-4b5f-9944-4f3bd58e8130",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKQLaq2igMsaZTxWF9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99c0f038-073b-449c-895c-49b56b520f19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZUmLxeY5ojEWyMZjBApxB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 7409,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1652
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 7409,
          "cache_creation_input_tokens": 1652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1652,
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

_source line 6 · 2026-05-19T23:31:33.499Z_

<details><summary>↩ Tool result · `toolu_01R9QChThtjRTF3PhbxNecmH`</summary>

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
  "parentUuid": "99c0f038-073b-449c-895c-49b56b520f19",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "5350eac1-ecd3-472c-a859-0a17e525bc92",
  "sourceToolAssistantUUID": "99c0f038-073b-449c-895c-49b56b520f19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T23:31:36.502Z_



Now let me launch multiple searches in parallel to cover all the research angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5350eac1-ecd3-472c-a859-0a17e525bc92",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKeFk4Qd5XrqEzBkRv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f628f6ef-ec9a-4164-8067-6711d7519f61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CovszF6rJQaaJiommTtMKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 8 · 2026-05-19T23:31:36.858Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CbUFKmiYG92sgBLZLdn4vF`</summary>

```json
{
  "query": "\"Reducing Tokenization Premiums\" Churchill Skiena 2026 low-resource languages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f628f6ef-ec9a-4164-8067-6711d7519f61",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKeFk4Qd5XrqEzBkRv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0416e8f0-e48a-4b51-98a9-d15197f2492f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CovszF6rJQaaJiommTtMKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 9 · 2026-05-19T23:31:37.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014uUjAwCjhyJsmp1R5ehEBs`</summary>

```json
{
  "query": "post-hoc vocabulary addition language model tokenizer reasoning downstream tasks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0416e8f0-e48a-4b51-98a9-d15197f2492f",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKeFk4Qd5XrqEzBkRv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5459019f-f14c-4dbf-bd0b-a24a70ac5124",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CovszF6rJQaaJiommTtMKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 10 · 2026-05-19T23:31:37.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019DTCAihEBDzHYh799KgxPp`</summary>

```json
{
  "query": "\"One Tokenizer To Rule Them All\" ICLR 2026 multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5459019f-f14c-4dbf-bd0b-a24a70ac5124",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKeFk4Qd5XrqEzBkRv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6acaf5a5-96c0-4b5f-8913-43d6f3af4b5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CovszF6rJQaaJiommTtMKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 11 · 2026-05-19T23:31:38.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019jqodQdYajApzYdoH7h3zV`</summary>

```json
{
  "query": "tokenizer vocabulary expansion without retraining LLM benchmark performance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6acaf5a5-96c0-4b5f-8913-43d6f3af4b5b",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKeFk4Qd5XrqEzBkRv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "031bf1a4-a84e-4ab5-879c-503e1f62671a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CovszF6rJQaaJiommTtMKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 12 · 2026-05-19T23:31:38.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YJd9VQxKYZ2gDpP7PwYjjv`</summary>

```json
{
  "query": "token healing token merging language model inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "031bf1a4-a84e-4ab5-879c-503e1f62671a",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoKeFk4Qd5XrqEzBkRv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11f51b54-5980-4ef1-b34e-927a793a328c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CovszF6rJQaaJiommTtMKi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 9061,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 9061,
          "cache_creation_input_tokens": 1131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1131,
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

_source line 13 · 2026-05-19T23:31:43.577Z_

<details><summary>↩ Tool result · `toolu_019DTCAihEBDzHYh799KgxPp`</summary>

```text
Web search results for query: ""One Tokenizer To Rule Them All" ICLR 2026 multilingual"

Links: [{"title":"One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers | OpenReview","url":"https://openreview.net/forum?id=RMT6CZquly"},{"title":"One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers","url":"https://arxiv.org/html/2506.10766v1"},{"title":"[Literature Review] One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers","url":"https://www.themoonlight.io/en/review/one-tokenizer-to-rule-them-all-emergent-language-plasticity-via-multilingual-tokenizers"},{"title":"(PDF) One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers","url":"https://www.researchgate.net/publication/392629744_One_Tokenizer_To_Rule_Them_All_Emergent_Language_Plasticity_via_Multilingual_Tokenizers"},{"title":"[2506.10766] One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers","url":"https://arxiv.org/abs/2506.10766"}]

I found the paper! Here's what I found about "One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers":

The paper was submitted to ICLR 2026 on September 18, 2025 (modified February 11, 2026).

**Overview:**
The paper addresses the challenge of pretraining massively multilingual Large Language Models (LLMs) on corpora from many languages at once due to limited model capacity, scarce high-quality data in many languages, and compute constraints.

**Main Contribution:**
The authors propose using a universal tokenizer that is trained for more languages than the primary pretraining languages to enable nimble and efficient adaptation in expanding language coverage after pretraining.

**Key Results:**
The universal tokenizer enables significantly higher language adaptation, with up to 20.2% increase in win rates compared to tokenizers specific to pretraining languages. Additionally, the universal tokenizer exhibits 2x higher plasticity with 8x faster adaptation compared to the cluster-specific baseline tokenizer.

**Scale of Experiments:**
The authors conducted systematic experiments across 63 languages belonging to diverse typological and lexicographic language groups.

The paper is available on OpenReview and arXiv (2506.10766).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6acaf5a5-96c0-4b5f-8913-43d6f3af4b5b",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "314b074f-e847-40dc-8251-b0e91c096eec",
  "sourceToolAssistantUUID": "6acaf5a5-96c0-4b5f-8913-43d6f3af4b5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T23:31:44.637Z_

<details><summary>↩ Tool result · `toolu_014uUjAwCjhyJsmp1R5ehEBs`</summary>

```text
Web search results for query: "post-hoc vocabulary addition language model tokenizer reasoning downstream tasks"

Links: [{"title":"From Tokens to Words: On the Inner Lexicon of LLMs","url":"https://arxiv.org/html/2410.05864v4"},{"title":"Vocabulary Expansion of Chat Models with Unlabeled Target Language Data","url":"https://arxiv.org/html/2412.11704v1"},{"title":"Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/pdf/2506.06607"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/pdf/2601.13328"},{"title":"Length-MAX Tokenizer for Language Models","url":"https://arxiv.org/pdf/2511.20849"},{"title":"Vocabulary Customization for Efficient Domain-Specific LLM Deployment","url":"https://arxiv.org/pdf/2509.26124"},{"title":"Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models","url":"https://arxiv.org/pdf/2512.03989"},{"title":"From Tokens to Words: On the Inner Lexicon of LLMs","url":"https://arxiv.org/pdf/2410.05864"},{"title":"Multilingual Tokenizer Advances","url":"https://www.emergentmind.com/topics/multilingual-tokenizer"}]

I found relevant research on post-hoc vocabulary addition for language models. Here are the key findings:

## Research Overview

Recent work explores expanding a model's vocabulary with new input and output embeddings for originally multi-token words, without updates to model parameters. This approach is particularly important for low-resource languages and domains, as even multilingual tokenizers can produce substantially longer token sequences for non-English languages—up to 13 times longer than equivalent English texts.

## Key Techniques

Several post-hoc approaches have been developed to address tokenizer vocabulary limitations:

- Prior attempts to expand tokenizer vocabulary post-hoc are limited in number, and require substantial additional training
- Recent work introduces methods for vocabulary extension based on continued BPE training, showing more efficient tokenization than adding tokens from independently trained domain-specific tokenizers
- Some techniques enable direct reuse of pretrained model weights with new tokenizers, facilitating cross-tokenizer knowledge distillation, speculative decoding, ensembling, merging, and domain-specific vocabulary adaptations

## Impact on Downstream Tasks

Tokenization quality is tied to model performance, with language-specific tokenizers providing advantages over multilingual ones, and more efficient compression associated with better downstream results. Adapted models show substantial inference speedups, ranging from 1.9x to 5.7x across various tasks.

The research demonstrates that post-hoc vocabulary addition can improve efficiency and performance without requiring full model retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5459019f-f14c-4dbf-bd0b-a24a70ac5124",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "6b35194b-637f-46d8-9576-ca38b1ecb9b5",
  "sourceToolAssistantUUID": "5459019f-f14c-4dbf-bd0b-a24a70ac5124",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T23:31:45.895Z_

<details><summary>↩ Tool result · `toolu_019jqodQdYajApzYdoH7h3zV`</summary>

```text
Web search results for query: "tokenizer vocabulary expansion without retraining LLM benchmark performance 2025 2026"

Links: [{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2402.14714"},{"title":"Balancing Vocabulary Size in Modern LLMs (GPT-4, LLaMA, Mistral)","url":"https://www.rohan-paul.com/p/tutorial-balancing-vocabulary-size"},{"title":"Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://www.arxiv.org/pdf/2504.15120"},{"title":"Tokenization is Killing our Multilingual LLM Dream","url":"https://huggingface.co/blog/omarkamali/tokenization"},{"title":"Achieving Tokenizer Flexibility in Language Models through Heuristic","url":"https://arxiv.org/pdf/2505.09738"},{"title":"Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/pdf/2506.06607"},{"title":"Vocabulary Expansion of Large Language Models via Kullback-Leibler-Based Self-Distillation","url":"https://arxiv.org/pdf/2508.15807"},{"title":"Vocabulary Customization for Efficient Domain-Specific LLM Deployment","url":"https://arxiv.org/pdf/2509.26124"},{"title":"Stop Taking Tokenizers for Granted: They Are Core Design Decisions in","url":"https://www.arxiv.org/pdf/2601.13260"},{"title":"TokAlign: Efficient Vocabulary Adaptation via Token Alignment","url":"https://arxiv.org/pdf/2506.03523"}]

Based on the search results, here's what I found about tokenizer vocabulary expansion without retraining LLM benchmark performance in 2025-2026:

## Recent Research on Training-Free Tokenizer Expansion

Several methods now achieve effective vocabulary expansion without gradient updates, with approaches like OMP consistently outperforming baselines including WECHSEL and FOCUS. These techniques enable direct reuse of pretrained model weights with new tokenizers, facilitating cross-tokenizer knowledge distillation and domain-specific vocabulary adaptations.

## Key Performance Findings

Methods like TokenAdapt are designed for high zero-shot semantic preservation, minimizing adaptation costs while avoiding significant retraining requirements. In real-world evaluations, augmented tokenizers have significantly shortened input sequences by up to 20% and reduced inference latency on downstream tasks while preserving predictive quality.

## Practical Applications

Recent work demonstrates significant improvements in non-English language performance with an average 8% improvement across benchmarks, while retaining the model's existing knowledge and eliminating the need for extensive retraining to maintain original English capabilities.

## Emerging Approaches in 2025-2026

Researchers are exploring whether a continuous pre-tokenization layer trained contrastively can recover performance gaps without retraining the LLM itself. Cutting-edge models released in 2025, such as Mistral-Nemo-Instruct and Ministral-8B-Instruct, now employ tokenizers with extended vocabularies of approximately 131k tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "031bf1a4-a84e-4ab5-879c-503e1f62671a",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "2f4fa351-4770-40fc-a58c-575b55b27966",
  "sourceToolAssistantUUID": "031bf1a4-a84e-4ab5-879c-503e1f62671a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T23:31:46.627Z_

<details><summary>↩ Tool result · `toolu_01YJd9VQxKYZ2gDpP7PwYjjv`</summary>

```text
Web search results for query: "token healing token merging language model inference"

Links: [{"title":"Token Efficiency and Compression Techniques in Large Language Models: Navigating Context-Length Limits | by Arash Nicoomanesh | Medium","url":"https://medium.com/@anicomanesh/token-efficiency-and-compression-techniques-in-large-language-models-navigating-context-length-05a61283412b"},{"title":"Token healing — Guidance latest documentation","url":"https://guidance.readthedocs.io/en/latest/example_notebooks/tutorials/token_healing.html"},{"title":"Token Merging for fast LLM inference : Background and first trials with Mistral","url":"https://huggingface.co/blog/samchain/token-merging-fast-inference"},{"title":"GitHub - samchaineau/llm_slerp_generation: Repo hosting codes and materials related to speeding LLMs' inference using token merging. · GitHub","url":"https://github.com/samchaineau/llm_slerp_generation"},{"title":"PuMer: Pruning and Merging Tokens for Efficient Vision Language Models","url":"https://arxiv.org/pdf/2305.17530"},{"title":"Token Merging. The Smart Shortcut Making Transformers… | by Zaina Haider | Medium","url":"https://medium.com/@thekzgroupllc/token-merging-5681afc4ff36"},{"title":"AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhong_AIM_Adaptive_Inference_of_Multi-Modal_LLMs_via_Token_Merging_and_ICCV_2025_paper.pdf"},{"title":"MrT5: Dynamic Token Merging for Efficient Byte-level Language Models","url":"https://arxiv.org/pdf/2410.20771"},{"title":"AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning","url":"https://arxiv.org/html/2412.03248v1"}]

Based on the search results, here's what I found about token healing and token merging in language model inference:

## Token Merging (ToMe)

Token Merging (TOME) introduces the idea of progressively merging tokens based on redundancy, where similar or repetitive tokens are merged during different stages of model inference, reducing the overall number of tokens processed. Tokens with similar embeddings or minimal differences are combined as the model progresses through layers of attention.

ToMe identifies which tokens are semantically similar and fuses them mid-inference instead of pushing all tokens through every layer. Token merging can be a powerful method for improving efficiency, especially in cases where many tokens contain redundant or repeated information.

## Token Healing

Token healing addresses issues that arise with byte-pair encoding (BPE) and similar tokenization schemes used by GPT-style models, which can lead to subtle issues during prompting and inference because token boundaries often don't line up with the end of the prompt. This is why ending a prompt with a space is usually a bad idea in GPT models, since most word-based tokens have the space before the word, not after it.

## Applications

Token merging has been applied in models like CLIP, Flamingo, and Segment Anything to merge text and image tokens to control memory usage and latency, with ongoing work to apply it to language models dealing with long sequences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11f51b54-5980-4ef1-b34e-927a793a328c",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "66090408-fef8-4d10-af74-074401e3026e",
  "sourceToolAssistantUUID": "11f51b54-5980-4ef1-b34e-927a793a328c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T23:31:46.857Z_

<details><summary>↩ Tool result · `toolu_01CbUFKmiYG92sgBLZLdn4vF`</summary>

```text
Web search results for query: ""Reducing Tokenization Premiums" Churchill Skiena 2026 low-resource languages"

Links: [{"title":"[2601.13328] Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/abs/2601.13328"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/html/2601.13328v1"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/pdf/2601.13328"},{"title":"Explaining and Mitigating Crosslingual Tokenizer Inequities","url":"https://arxiv.org/pdf/2510.21909"},{"title":"When Every Token Counts: Optimal Segmentation for Low-Resource Language   Models","url":"https://arxiv.org/pdf/2412.06926"}]

I found the paper you're looking for! Here are the key details:

The paper "Reducing Tokenization Premiums for Low-Resource Languages" was authored by Geoffrey Churchill and Steven Skiena, and it was published on January 19, 2026.

**Summary of the research:**

Low-resource languages suffer from substantial tokenization premiums in modern language models, requiring several times as many tokens to encode a sentence compared to English. This results in increased API and energy costs and reduced effective context windows for these languages.

The paper analyzes the tokenizers of ten popular language models to understand their designs and per-language tokenization premiums, and proposes a mechanism to reduce tokenization premiums in pre-trained models by post-hoc additions to the token vocabulary that coalesce multi-token characters into single tokens.

The methodology was applied to 12 low-resource languages, demonstrating that the original and compressed inputs often have similar last hidden states when run through the Llama 3.2 1B model.

The paper is available on arXiv at https://arxiv.org/abs/2601.13328.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0416e8f0-e48a-4b51-98a9-d15197f2492f",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "11c9193e-7fee-4d15-a0b1-758298fdf649",
  "sourceToolAssistantUUID": "0416e8f0-e48a-4b51-98a9-d15197f2492f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T23:31:49.687Z_

Good, I have initial results. Now let me fetch the actual papers and do more targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11c9193e-7fee-4d15-a0b1-758298fdf649",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe651a6a-9b7e-4726-97d6-2fc330aca158",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 19 · 2026-05-19T23:31:53.542Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01An4S3DbVqLv9qPXYRSwMEr`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.13328v1",
  "prompt": "Extract ALL details about: 1) What exactly was their methodology for post-hoc vocabulary additions? 2) How did they validate it - what metrics did they use? 3) What model(s) did they test on and at what scale? 4) Did they test on ANY downstream reasoning benchmarks (like MGSM, MMLU, etc.)? 5) What are the specific limitations they acknowledge? 6) What exactly do they mean by \"similar hidden states\"? How was similarity measured? 7) What languages were tested? 8) What specific results/numbers do they report?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe651a6a-9b7e-4726-97d6-2fc330aca158",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9198b299-3f21-42d7-972a-f39f7924ba88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 20 · 2026-05-19T23:31:55.388Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019eP8ckP2yVdKjBc4pnck6q`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.10766v1",
  "prompt": "Extract ALL details about: 1) What is the methodology? 2) What scale models were tested? 3) What downstream benchmarks were used? 4) How does this relate to post-hoc vocabulary expansion? 5) Did they test reasoning tasks specifically (MGSM, MMLU, etc.)? 6) What are the key results and limitations? 7) How does the universal tokenizer work vs language-specific ones?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9198b299-3f21-42d7-972a-f39f7924ba88",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76567510-5691-4e50-8136-f92e5172a835",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 21 · 2026-05-19T23:31:57.271Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WDURrwzwr8KiseyNbkko38`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2506.06607",
  "prompt": "Extract ALL details about: 1) What is the training-free tokenizer transplantation method? 2) What models and scales were tested? 3) Were any downstream reasoning benchmarks tested (MGSM, MMLU, etc.)? 4) How does it handle vocabulary mismatches? 5) Key results and limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76567510-5691-4e50-8136-f92e5172a835",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "707d3ab6-3263-4e66-b57c-7745edb315ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 22 · 2026-05-19T23:31:59.140Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PQoQXWHktSYMD96qphpQPU`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.11704v1",
  "prompt": "Extract ALL details about: 1) What is the method for vocabulary expansion of chat models? 2) What scale models were tested? 3) Were downstream benchmarks tested (MGSM, MMLU, ARC, etc.)? 4) What specific results were achieved? 5) Did they test reasoning tasks? 6) Limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "707d3ab6-3263-4e66-b57c-7745edb315ee",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b965bda-05c9-43d2-88e9-d72f74120a5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 23 · 2026-05-19T23:31:59.801Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RdNivDc1NrTgYeWcwTcswR`</summary>

```json
{
  "query": "vocabulary expansion multilingual LLM MGSM MMLU benchmark results 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b965bda-05c9-43d2-88e9-d72f74120a5c",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7810186-6efd-4280-a00e-634c41d2c2c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 24 · 2026-05-19T23:32:00.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0161X8uU1gTeZpoxTXeZ4DJo`</summary>

```json
{
  "query": "tokenizer swapping adaptation pretrained model without retraining FOCUS WECHSEL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7810186-6efd-4280-a00e-634c41d2c2c7",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoLdB2sctZobmVTwSCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5159929-1fe3-48b5-964b-269298afa251",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYXuQfvriDQkcaHGZER8xw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 10192,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 810
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3104,
          "output_tokens": 791,
          "cache_read_input_tokens": 10192,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 810,
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

_source line 25 · 2026-05-19T23:32:03.490Z_

<details><summary>↩ Tool result · `toolu_01WDURrwzwr8KiseyNbkko38`</summary>

```text
# Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit

## 1. Method Overview
The paper proposes a training-free approach using **Orthogonal Matching Pursuit (OMP)** to transplant tokenizers between language models without requiring additional training. The technique maps vocabulary embeddings from a source tokenizer to a target model's embedding space by finding optimal sparse linear combinations of existing embeddings.

## 2. Models and Scales Tested
The study evaluated the method on:
- **Llama 3.2-1B** (source and target)
- **Qwen2.5-7B** 
- **Mistral-Nemo-Base-2407**

Testing involved transplanting tokenizers across these architectures at different model scales to assess generalization.

## 3. Downstream Reasoning Benchmarks
The paper primarily focuses on language modeling and general evaluation tasks through "the EleutherAI eval-harness," though specific mention of MGSM, MMLU, or similar advanced reasoning benchmarks is not explicitly detailed in the available abstract/introduction content. The evaluation emphasizes practical transplantation effectiveness rather than specialized reasoning tasks.

## 4. Vocabulary Mismatch Handling
The OMP-based approach handles mismatches by using sparse decomposition: new vocabulary tokens are reconstructed as weighted combinations of existing embeddings, effectively bridging the gap between different tokenizer vocabularies without retraining.

## 5. Key Results and Limitations
- **Advantage**: Eliminates training overhead while maintaining model performance
- **Results**: Successfully transplanted tokenizers across model scales with minimal degradation
- **Limitation**: Reconstruction quality depends on finding appropriate sparse combinations; some vocabulary coverage gaps may persist

[Binary content (application/pdf, 717.6KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/ec50337c-efb0-4976-b822-6e64218d6124/tool-results/webfetch-1779233517283-t7mrzh.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "707d3ab6-3263-4e66-b57c-7745edb315ee",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "61350bda-4c3c-4c23-8cab-78a4bc5f02b4",
  "sourceToolAssistantUUID": "707d3ab6-3263-4e66-b57c-7745edb315ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T23:32:04.057Z_

<details><summary>↩ Tool result · `toolu_01An4S3DbVqLv9qPXYRSwMEr`</summary>

```text
# Analysis of Post-Hoc Vocabulary Addition Methodology

## 1) Methodology for Post-Hoc Vocabulary Additions

The researchers added missing Unicode characters as individual tokens to a frozen model's vocabulary. For each new character, they:

1. Tokenized the character using the original tokenizer (yielding multiple tokens)
2. Ran the Llama model on these token embeddings through a specified layer
3. Averaged the resulting hidden states into a single vector
4. Used prediction methods to derive an embedding that would produce similar hidden state when run independently

## 2) Validation Metrics

They measured "cosine similarity between averaged last hidden states" before and after augmentation. Specifically: "the cosine similarity between these two vectors to be a per-sentence similarity measure, which is averaged over all sentences."

However, they acknowledged significant limitations with this approach in their Limitations section.

## 3) Model(s) and Scale

They tested exclusively on **Llama 3.2 1B** (1 billion parameters). This was a deliberate choice for a preliminary study on a smaller, more manageable model.

## 4) Downstream Reasoning Benchmarks

**No.** They did not test on MGSM, MMLU, or any downstream tasks. This represents a major gap—their validation was purely embedding-based, not task-based.

## 5) Specific Limitations Acknowledged

The authors identified three critical validation issues:

- Cosine similarity scores are "meaningless in isolation"
- "Cosine similarity is not necessarily aligned with performance on real downstream tasks"
- Averaging hidden states is "a fairly aggressive operation"

They also flagged a "vote-splitting problem" where augmenting (rather than replacing) vocabulary could cause probability mass splitting between original sub-tokens and new combined tokens, potentially degrading performance.

## 6) "Similar Hidden States" Definition

Similarity was measured as **cosine similarity** of the final layer (layer 16) averaged last hidden states. They extracted layer-16 representations from both compressed and uncompressed inputs, averaged each into 2,048-dimensional vectors, then computed cosine similarity across all test sentences per language.

## 7) Languages Tested

12 languages with predominantly non-Latin scripts:
Amharic (amh), Bangla (ben), Hebrew (heb), Hindi (hin), Armenian (hye), Shan (shn), Tamil (tam), Telugu (tel), Urdu (urd), Vietnamese (vie), Yiddish (ydd), Chinese traditional script (zho)

## 8) Specific Results/Numbers

Key findings from Table 4:

- **Linear regression at layer 0** performed best overall
- Shan language: ~0.68-0.72 similarity (worst-tokenized language)
- Traditional Chinese: ~0.92-0.98 similarity (highest preservation)
- Amharic at layer 0: extreme difficulty (~0.05-0.36 similarity)
- Vietnamese: 0.85+ similarity but only 26% new tokens needed

The authors reduced tokenization premiums substantially (from 5-10x penalties to lower ratios) but provided no downstream task performance metrics validating practical utility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9198b299-3f21-42d7-972a-f39f7924ba88",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "863b3c94-6a0f-4c99-865c-c87a4d182594",
  "sourceToolAssistantUUID": "9198b299-3f21-42d7-972a-f39f7924ba88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T23:32:06.829Z_

<details><summary>↩ Tool result · `toolu_01RdNivDc1NrTgYeWcwTcswR`</summary>

```text
Web search results for query: "vocabulary expansion multilingual LLM MGSM MMLU benchmark results 2025 2026"

Links: [{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2402.14714"},{"title":"Multilingual Benchmarks 2026: MGSM, MMLU-ProX LLM Scores | BenchLM.ai","url":"https://benchlm.ai/multilingual"},{"title":"MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.79/"},{"title":"[2503.10497] MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation","url":"https://arxiv.org/abs/2503.10497"},{"title":"MMLU-ProX: A Multilingual Benchmark for Advanced LLM Evaluation","url":"https://mmluprox.github.io/"},{"title":"MGSM Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/mgsm"},{"title":"MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation","url":"https://arxiv.org/pdf/2503.10497"}]

Based on the search results, here's what I found regarding vocabulary expansion, multilingual LLMs, and MGSM/MMLU benchmark results:

## Vocabulary Expansion and Multilingual LLMs

Open source models such as LLaMA, MPT, Falcon, Mistral, and Phi-1.5 have predominantly favored English, leading to a performance gap in non-English languages. Non-English languages like Korean require significantly more tokens than English even for equivalent semantic content. To address this, EEVE Korean LLMs were built on recent English-centric LLMs with further Korean-centric pre-training.

## MGSM Benchmark Results

MGSM tests mathematical reasoning across 10 languages, using the same 250 grade school math problems translated into Bengali, Chinese, French, German, Japanese, Russian, Spanish, Swahili, Telugu, and Thai. GPT-5.3 Codex scores 96% on MGSM.

## MMLU-ProX Multilingual Benchmark (2025)

A new benchmark called MMLU-ProX was introduced in 2025. MMLU-ProX covers 29 languages with each language version consisting of 11,829 identical questions, enabling direct cross-linguistic comparisons. 

The results reveal significant disparities in the multilingual capabilities of LLMs: While they perform well in high-resource languages, their performance declines markedly in low-resource languages, with gaps of up to 24.3%. The best models achieve over 70% accuracy on English but drop to around 40% for languages like Swahili, highlighting persistent gaps in multilingual capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7810186-6efd-4280-a00e-634c41d2c2c7",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "fa769952-9040-45b2-9221-f1e5aa72c0b9",
  "sourceToolAssistantUUID": "e7810186-6efd-4280-a00e-634c41d2c2c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T23:32:07.384Z_

<details><summary>↩ Tool result · `toolu_0161X8uU1gTeZpoxTXeZ4DJo`</summary>

```text
Web search results for query: "tokenizer swapping adaptation pretrained model without retraining FOCUS WECHSEL 2025"

Links: [{"title":"[2506.06607] Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/abs/2506.06607"},{"title":"Achieving Tokenizer Flexibility in Language Models through Heuristic Adaptation and Supertoken Learning","url":"https://arxiv.org/html/2505.09738"},{"title":"Language Adaptation on a Tight Academic Compute Budget: Tokenizer   Swapping Works and Pure bfloat16 Is Enough","url":"https://arxiv.org/pdf/2408.15793"},{"title":"Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/pdf/2506.06607"},{"title":"FOCUS: Effective Embedding Initialization for Monolingual Specialization   of Multilingual Models","url":"https://arxiv.org/pdf/2305.14481"},{"title":"Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models","url":"https://arxiv.org/pdf/2512.03989"},{"title":"Achieving Tokenizer Flexibility in Language Models through Heuristic Adaptation and Supertoken Learning","url":"https://arxiv.org/pdf/2505.09738"},{"title":"[2512.03989] Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models","url":"https://arxiv.org/abs/2512.03989"}]

Based on the search results, I found relevant information about tokenizer swapping and adaptation for pretrained models. Here are the key findings:

## FOCUS and WECHSEL Methods

FOCUS uses fastText to weight combinations of existing embeddings based on similarities calculated in external spaces, while WECHSEL identifies semantically similar source tokens using static multilingual embeddings and combines their vectors.

FOCUS is an embedding initialization method that allows transfer of information from a source model's pretrained embedding matrix to a new embedding matrix for a target language's tokenizer, using overlapping tokens between both tokenizers as anchor points and representing new target language tokens as a weighted mean of overlapping tokens' embeddings.

## Recent Advances (2025)

A recent Orthogonal Matching Pursuit (OMP) approach achieves better overall performance compared to baselines like WECHSEL, FOCUS, and ZETT, effectively bridging large tokenizer discrepancies without gradient updates. This technique enables direct reuse of pretrained model weights with new tokenizers, facilitating cross-tokenizer knowledge distillation, speculative decoding, ensembling, merging, and domain-specific vocabulary adaptations.

## Practical Application

Swapping the tokenizer for a specialized one yields more efficient tokenization and is competitive with the original tokenizer in language adaptation scenarios.

These methods represent the state-of-the-art approaches for adapting pretrained models to new tokenizers without requiring full retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5159929-1fe3-48b5-964b-269298afa251",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "6c70e14b-44f6-4684-b582-88114e61b0b1",
  "sourceToolAssistantUUID": "a5159929-1fe3-48b5-964b-269298afa251",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T23:32:07.425Z_

<details><summary>↩ Tool result · `toolu_019eP8ckP2yVdKjBc4pnck6q`</summary>

```text
# Research Summary: Universal Tokenizers for Multilingual LLMs

## 1) Methodology

The researchers trained language models using a **universal tokenizer** (covering 62 languages) versus **cluster-specific tokenizers** (limited to primary pretraining languages). They evaluated three adaptation strategies:

- Continued pretraining with both primary and expanded language data
- Targeted adaptation to expanded languages only
- Targeted adaptation to fully unseen languages

The study manipulated tokenizer design while keeping model architecture constant across ablations.

## 2) Model Scale

"We focus on only 3.3 billion parameter language models for ablations" trained for "100 billion tokens using a total of 25,000 steps." The researchers acknowledged this limitation, noting they required "a large amount of compute" and this represented "the edge of what is computationally feasible."

## 3) Downstream Benchmarks

**Open-ended evaluation:** LLM-as-a-Judge win rates using the Aya Evaluation Dataset (200 examples translated from Dolly-15k across 15 languages)

**Task-specific multilingual:** Belebele (122-language reading comprehension) and M-MMLU (machine-translated MMLU)

**English-only tasks:** ARC-C/E, BoolQ, CommonsenseQA, Hellaswag, MMLU, OpenBookQA, PIQA, SIQA, TruthfulQA, WinoGrande

## 4) Relation to Post-hoc Vocabulary Expansion

The work explicitly contrasts with Cross-Lingual Vocabulary Adaptation (CVA). "When randomly initializing the new tokens, CVA (tokenizer replacement) fails to achieve comparable performance even against the Cluster tokenizer, and significantly lags behind the Universal tokenizer by 15.4% and 35.2% win rates." The universal approach embedded at pretraining outperforms post-hoc vocabulary replacement strategies.

## 5) Reasoning Task Coverage

The study included **MMLU** (general knowledge reasoning) but did not specifically evaluate dedicated multilingual reasoning benchmarks like MGSM (Multilingual Grade School Math). The evaluation emphasized open-ended generation quality rather than systematic reasoning performance.

## 6) Key Results & Limitations

**Primary findings:**
- Universal tokenizer achieved "an average of 19% higher win rate in continued pretraining experiments" on expanded languages
- Performance on primary languages showed "no more than 2% difference" versus baselines
- "Universal tokenizer enables +8x faster adaptation in terms of sample efficiency"
- Improvements persisted even for "7 heavily under-resourced languages" unseen during tokenizer training (5% gain)

**Acknowledged limitations:**
- "All of our pretraining experiments were conducted on 3.3B parameter models with a 100B token budget"
- "We focused only on the BPE algorithm" due to computational constraints
- Limited to 69 languages despite "many more languages in the world"

## 7) Universal vs. Language-Specific Tokenizers

**Universal tokenizer:** Trained on all 62 languages using specialized weighting that balances language family/script buckets against data distribution proportions

**Cluster tokenizer:** Trained only on primary pretraining languages for each geographic region

The universal approach employed a 250k vocabulary (larger than typical) and required "5% of the training mixture from English data...uniformly distributed...among all the expanded languages, to avoid undertrained tokens."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76567510-5691-4e50-8136-f92e5172a835",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "f42bc05d-85fa-40fd-a12b-2ae05d1f5b88",
  "sourceToolAssistantUUID": "76567510-5691-4e50-8136-f92e5172a835",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T23:32:08.828Z_

<details><summary>↩ Tool result · `toolu_01PQoQXWHktSYMD96qphpQPU`</summary>

```text
# Vocabulary Expansion of Chat Models: Key Details

## 1) Vocabulary Expansion Method

The approach involves three main steps:

- **Tokenizer creation**: Train an auxiliary target language tokenizer on unlabeled data, then select the top-k frequent tokens not already in the source vocabulary
- **Model initialization**: Expand embedding and language modeling head matrices using "mean initialization" (averaging source token embeddings)
- **Continual pre-training**: Train only the embedding layer, language modeling head, and top/bottom two layers on target language data (500M tokens)

Additionally, three post-hoc techniques inject source model information: applying the source chat template, copying special token weights, and merging model weights via linear interpolation or SLERP.

## 2) Model Scale Tested

The study evaluated three chat models: "Qwen2.5 7B," "Llama 3.1 8B," and "Gemma 2 9B." All experiments used models in the 7-9 billion parameter range.

## 3) Downstream Benchmarks Tested

The evaluation covered diverse tasks but **not** the specific benchmarks you mentioned (MGSM, ARC). Instead, they tested:

- Generative: summarization (XL-SUM), machine translation (FLORES-200)
- Discriminative: multiple-choice classification (Belebele)
- English benchmarks: MMLU, BBH, IFEval

## 4) Specific Results Achieved

Key findings include:

- "off-the-shelf VE generally performs well across target language tasks and models in 71% of cases"
- Up to "5.7x inference speedup" for adapted models
- Post-hoc techniques improved performance in "87% of cases with up to 6.0x faster inference"
- "adapted chat models with the post-hoc techniques outperform adapted base counterparts in 88.9% of the settings"

## 5) Reasoning Tasks

**No**, the study did not test reasoning-specific tasks. They focused on practical NLP applications (translation, summarization, classification) rather than complex reasoning benchmarks.

## 6) Limitations

The authors acknowledged five key constraints:

- **Initialization methods**: Only tested mean initialization; other methods (W2CV, WECHSEL) were not evaluated
- **Training approaches**: Limited to one continual pre-training strategy; LoRA and full fine-tuning not explored
- **Merging methods**: Used only linear and SLERP; newer methods like TIES unexplored
- **Model sizes**: Restricted to 7-9B models due to computational constraints
- **Language coverage**: Only seven languages tested despite acknowledging "experimenting with more languages is an interesting avenue"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b965bda-05c9-43d2-88e9-d72f74120a5c",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "b637bebb-3f7f-4482-8348-79c581796548",
  "sourceToolAssistantUUID": "5b965bda-05c9-43d2-88e9-d72f74120a5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T23:32:12.388Z_

Excellent. Let me now dig deeper into specific papers and search for any work specifically validating vocabulary additions on downstream reasoning at scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b637bebb-3f7f-4482-8348-79c581796548",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoNFHD1LnPiJEnWUjQS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f623adc-b120-4d26-b792-3dd3d70081fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ADKxfosMVZY2E5kPVLMT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1570,
      "cache_creation_input_tokens": 6613,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6613,
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

_source line 32 · 2026-05-19T23:32:14.387Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DJz5fR48x151rvCb4QMCKr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.14714",
  "prompt": "Extract details about: 1) What is EEVE and the vocabulary expansion method? 2) What scale models were tested? 3) Were MGSM, MMLU, or other reasoning benchmarks tested? 4) What were the specific results? 5) Did vocabulary expansion help or hurt reasoning? 6) Was this post-hoc or did it require retraining?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f623adc-b120-4d26-b792-3dd3d70081fe",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoNFHD1LnPiJEnWUjQS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66649969-04f6-437b-b559-4fea15d8ceda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ADKxfosMVZY2E5kPVLMT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1570,
      "cache_creation_input_tokens": 6613,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6613,
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

_source line 33 · 2026-05-19T23:32:16.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TGXt1jFSMpPPjohck8urTb`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09738",
  "prompt": "Extract ALL details about: 1) What is the heuristic adaptation and supertoken learning method? 2) What models and scales tested? 3) Were downstream reasoning benchmarks used (MGSM, MMLU)? 4) Does this work without retraining? 5) Key results about whether tokenizer changes preserve reasoning ability?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66649969-04f6-437b-b559-4fea15d8ceda",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoNFHD1LnPiJEnWUjQS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d206b64-9226-4f08-8979-5dfadbd40807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ADKxfosMVZY2E5kPVLMT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1570,
      "cache_creation_input_tokens": 6613,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6613,
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

_source line 34 · 2026-05-19T23:32:18.156Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01985AMiM5AfHb1bN1W5y7k8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.03989",
  "prompt": "Extract ALL details about: 1) What is the method for teaching old tokenizers new words? 2) What models and scales tested? 3) Were downstream benchmarks tested? 4) How much retraining is needed? 5) Does it preserve model reasoning capabilities? 6) Key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d206b64-9226-4f08-8979-5dfadbd40807",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoNFHD1LnPiJEnWUjQS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77580690-34ed-4740-867d-43df209085b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ADKxfosMVZY2E5kPVLMT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1570,
      "cache_creation_input_tokens": 6613,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6613,
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

_source line 35 · 2026-05-19T23:32:18.857Z_

<details><summary>↩ Tool result · `toolu_01DJz5fR48x151rvCb4QMCKr`</summary>

```text
# Summary of EEVE Paper Details

Based on the provided arXiv page content, here's what can be extracted:

## 1) EEVE and Vocabulary Expansion Method
EEVE (Efficient and Effective Vocabulary Expansion) encompasses "parameter freezing and subword initialization" to adapt English-centric LLMs for non-English languages.

## 2) Scale of Models Tested
The paper tested vocabulary expansion on models including SOLAR-10.7B and Phi-2, with their resulting model labeled "EEVE-Korean-10.8B-v1.0."

## 3) Reasoning Benchmarks
The abstract does not mention MGSM, MMLU, or other reasoning benchmarks. Evaluation appears limited to "the Open Ko-LLM Leaderboard" for Korean language tasks.

## 4) Specific Results
The model "ranks as the leading Korean pre-trained model in the open-source community, according to Hugging Face's leaderboard" as of January 2024, outperforming most instruction-tuned LLMs.

## 5) Impact on Reasoning
The abstract provides no information on whether vocabulary expansion affected reasoning capabilities.

## 6) Post-hoc vs. Retraining
The method achieved improvements "within just 2 billion tokens," suggesting efficient adaptation rather than full retraining from scratch, though the exact training methodology isn't detailed in this abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66649969-04f6-437b-b559-4fea15d8ceda",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "061f192f-2a34-4236-ade7-5cc0ca896be9",
  "sourceToolAssistantUUID": "66649969-04f6-437b-b559-4fea15d8ceda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T23:32:19.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MqeVVpHXqup3vbGDB9TQaJ`</summary>

```json
{
  "query": "\"vocabulary expansion\" OR \"tokenizer adaptation\" large language model reasoning MGSM benchmark downstream performance degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "061f192f-2a34-4236-ade7-5cc0ca896be9",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoNFHD1LnPiJEnWUjQS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7db129a4-c623-4db5-9ed9-800fc0e72fb3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ADKxfosMVZY2E5kPVLMT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1570,
      "cache_creation_input_tokens": 6613,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6613,
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

_source line 37 · 2026-05-19T23:32:19.951Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BgBoCoeTi8pjjmgai9FF1M`</summary>

```json
{
  "query": "Churchill Skiena tokenization premium hidden state similarity limitations LLaMA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db129a4-c623-4db5-9ed9-800fc0e72fb3",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoNFHD1LnPiJEnWUjQS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe926df5-beba-4c41-8aa3-fd63155cdb5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ADKxfosMVZY2E5kPVLMT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1570,
      "cache_creation_input_tokens": 6613,
      "cache_read_input_tokens": 11002,
      "output_tokens": 573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6613
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1570,
          "output_tokens": 573,
          "cache_read_input_tokens": 11002,
          "cache_creation_input_tokens": 6613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6613,
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

_source line 38 · 2026-05-19T23:32:22.825Z_

<details><summary>↩ Tool result · `toolu_01985AMiM5AfHb1bN1W5y7k8`</summary>

```text
# Analysis of "Teaching Old Tokenizers New Words"

Based on the provided arXiv page, here's what can be extracted:

## 1) Method for Teaching Old Tokenizers New Words
The paper proposes **"continued BPE training"** that extends pre-trained tokenizers by continuing the BPE merge learning process on new data, rather than simply appending non-overlapping tokens from a newly trained tokenizer.

## 2) Models and Scales Tested
The abstract mentions **"multiple languages and model families"** but does not specify particular model names or scale details on this page.

## 3) Downstream Benchmarks
No downstream benchmark testing information is disclosed in the available abstract or metadata.

## 4) Retraining Requirements
The page does not specify how much retraining is needed for the adaptation process.

## 5) Model Reasoning Capabilities
No information about preservation of reasoning capabilities is mentioned in the provided content.

## 6) Key Results
The paper reports that continued BPE training:
- **"improves tokenization efficiency"**
- Leads to **"better utilization of added vocabulary"**
- Introduces "leaf-based vocabulary pruning" to remove redundant tokens while maintaining model quality

The work was accepted to **EACL 2026 Findings** and includes an open-source toolkit release.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77580690-34ed-4740-867d-43df209085b8",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "075ef19c-721f-492c-81ad-947609a1fdd8",
  "sourceToolAssistantUUID": "77580690-34ed-4740-867d-43df209085b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T23:32:25.376Z_

<details><summary>↩ Tool result · `toolu_01TGXt1jFSMpPPjohck8urTb`</summary>

```text
# TokenAdapt: Heuristic Adaptation and Supertoken Learning Analysis

## 1) Method Overview

The framework introduces two core innovations:

**TokenAdapt (Heuristic Transplantation):** A hybrid initialization strategy combining:
- *Local heuristic*: Decomposes new tokens using the original tokenizer, then weights sub-token embeddings based on "semantic similarity and relative length"
- *Global heuristic*: Identifies k-nearest semantically similar tokens from the original vocabulary via auxiliary embeddings and averages their vectors

The final embedding blends both estimates: `(1-w_glob)·e_local + w_glob·e_glob`

**Supertokens:** Learned multi-word units through probabilistic pre-tokenization before BPE training, designed to "enhance compression and reduce fragmentation."

## 2) Models and Scales Tested

- **Base models**: Meta-Llama 3.2-3B and Qwen 2.5-3B
- **Target tokenizers**: QTK-81K (standard) and Adi-Bun-128K (supertoken variant)
- **Evaluation domains**: English, Hindi, Code, Math, Hinglish

No large-scale models evaluated; testing limited to 3B parameter range.

## 3) Downstream Reasoning Benchmarks

**No reasoning benchmarks were used.** Evaluation relied exclusively on zero-shot perplexity measurements across domain-specific subsets of the tinycompany/ppl dataset. MGSM, MMLU, and comparable reasoning tasks were absent.

## 4) Retraining Requirements

The method claims near-zero-shot viability. While technically initialization occurs without retraining, the abstract acknowledges that existing methods "still may not fully preserve semantic nuances," and comparative baselines included "residual fine-tuning." TokenAdapt itself appears **retraining-free for initialization**, though downstream adaptation performance depends on auxiliary embedding quality.

## 5) Reasoning Preservation

**This critical aspect remains unaddressed.** The paper provides no direct evidence regarding whether tokenizer transplantation preserves reasoning capabilities. Perplexity ratios (Table 1) showed TokenAdapt achieved "up to approximately a 2-fold improvement" versus ReTok, but perplexity ≠ reasoning fidelity. No analysis of whether complex logical, mathematical, or multi-step reasoning survives tokenizer changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d206b64-9226-4f08-8979-5dfadbd40807",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "9f41888e-efe6-4bde-8479-1d56dbe79177",
  "sourceToolAssistantUUID": "3d206b64-9226-4f08-8979-5dfadbd40807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T23:32:26.583Z_

<details><summary>↩ Tool result · `toolu_01BgBoCoeTi8pjjmgai9FF1M`</summary>

```text
Web search results for query: "Churchill Skiena tokenization premium hidden state similarity limitations LLaMA 2026"

Links: [{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/html/2601.13328"},{"title":"[2601.13328] Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/abs/2601.13328"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/pdf/2601.13328"},{"title":"Where is the signal in tokenization space?","url":"https://arxiv.org/pdf/2408.08541"},{"title":"Tokenization Multiplicity Leads to Arbitrary Price Variation in LLM-as-a-service","url":"https://arxiv.org/pdf/2506.06446"}]

Based on the search results, I found a recent paper by Geoffrey Churchill and Steven Skiena that directly addresses your query.

The paper "Reducing Tokenization Premiums for Low-Resource Languages" by Geoffrey Churchill and Steven Skiena addresses how low-resource languages suffer from substantial tokenization premiums in modern language models, requiring several times as many tokens to encode a sentence compared to English.

This tokenization premium results in increased API and energy costs and reduced effective context windows for these languages. The authors analyze the tokenizers of ten popular language models to understand their designs and per-language tokenization premiums, and propose a mechanism to reduce tokenization premiums in pre-trained models by post-hoc additions to the token vocabulary that coalesce multi-token characters into single tokens.

Regarding the hidden state similarity aspect: The authors apply this methodology to 12 low-resource languages, demonstrating that the original and compressed inputs often have similar last hidden states when run through the Llama 3.2 1B model.

The paper was published in January 2026 (arXiv ID: 2601.13328) and represents recent research on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe926df5-beba-4c41-8aa3-fd63155cdb5d",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "0ae67c43-2a57-44c1-9a4b-f00bbe4c515d",
  "sourceToolAssistantUUID": "fe926df5-beba-4c41-8aa3-fd63155cdb5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T23:32:37.226Z_

<details><summary>↩ Tool result · `toolu_01MqeVVpHXqup3vbGDB9TQaJ`</summary>

```text
Web search results for query: ""vocabulary expansion" OR "tokenizer adaptation" large language model reasoning MGSM benchmark downstream performance degradation"

Links: [{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2402.14714"},{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models","url":"https://arxiv.org/html/2402.14714v1"},{"title":"Vocabulary Expansion of Large Language Models via Kullback-Leibler-Based Self-Distillation","url":"https://arxiv.org/pdf/2508.15807"},{"title":"An Empirical Comparison of Vocabulary Expansion and Initialization   Approaches for Language Models","url":"https://arxiv.org/pdf/2407.05841"},{"title":"How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?","url":"https://arxiv.org/pdf/2406.11477"},{"title":"TokAlign: Efficient Vocabulary Adaptation via Token Alignment","url":"https://arxiv.org/html/2506.03523v1"}]

Now let me search specifically for information about downstream performance degradation and reasoning with MGSM benchmark:

Links: [{"title":"MGSM Benchmark: Multilingual Grade School Math","url":"https://www.emergentmind.com/topics/multilingual-grade-school-math-mgsm-benchmark"},{"title":"MGSM (Multilingual Grade School Math) | AI Wiki","url":"https://aiwiki.ai/wiki/mgsm"},{"title":"MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation","url":"https://arxiv.org/html/2601.21225"},{"title":"(PDF) MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation","url":"https://www.researchgate.net/publication/400237352_MGSM-Pro_A_Simple_Strategy_for_Robust_Multilingual_Mathematical_Reasoning_Evaluation"},{"title":"MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260121225X/abstract"},{"title":"MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation","url":"https://arxiv.org/pdf/2601.21225"},{"title":"MGSM problem distribution with respect to the number of reasoning steps... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/MGSM-problem-distribution-with-respect-to-the-number-of-reasoning-steps-in-the-standard_fig1_364222723"},{"title":"[2601.21225] MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation","url":"https://arxiv.org/abs/2601.21225"}]

Let me search for more specific information about how vocabulary expansion affects downstream tasks and reasoning:

Links: [{"title":"Tokenizer Choice For LLM Training: Negligible or Crucial? | Continuum Labs","url":"https://training.continuumlabs.ai/training/the-fine-tuning-process/tokenization/tokenizer-choice-for-llm-training-negligible-or-crucial"},{"title":"How does a Language-Specific Tokenizer affect LLMs?","url":"https://arxiv.org/html/2502.12560v1"},{"title":"(PDF) How does a Language-Specific Tokenizer affect LLMs?","url":"https://www.researchgate.net/publication/389130085_How_does_a_Language-Specific_Tokenizer_affect_LLMs"},{"title":"Tokenizer Choice For LLM Training: Negligible or Crucial?","url":"https://arxiv.org/pdf/2310.08754"},{"title":"One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers","url":"https://arxiv.org/html/2506.10766v1"},{"title":"Tokenization Impacts Multilingual Language Modeling: Assessing   Vocabulary Allocation and Overlap Across Languages","url":"https://arxiv.org/pdf/2305.17179"},{"title":"Vocabulary Customization for Efficient Domain-Specific LLM Deployment","url":"https://arxiv.org/pdf/2509.26124"},{"title":"IndicSuperTokenizer: An Optimized Tokenizer for Indic Multilingual LLMs","url":"https://arxiv.org/html/2511.03237v1"},{"title":"Tokenization is Sensitive to Language Variation","url":"https://arxiv.org/pdf/2502.15343"}]

Based on my web search results, I've found comprehensive information about vocabulary expansion, tokenizer adaptation, their impact on multilingual LLMs, and performance on reasoning benchmarks like MGSM. Here's what I found:

## Vocabulary Expansion and Tokenizer Adaptation in Multilingual LLMs

### Overview of Vocabulary Expansion Methods

Vocabulary expansion methods address the challenge of English-centric tokenizers inefficiently processing non-English texts by using parameter freezing and subword initialization techniques. These approaches can significantly boost non-English proficiency within just 2 billion tokens, which is more efficient than previous efforts requiring trillions of tokens.

One major challenge for LLM adaptation is the lack of vocabulary coverage in the original model's tokenizer for new languages, which results in inefficient tokenization with high fertility.

### Downstream Performance Impact

Tokenizer choice can significantly affect the model's downstream performance and training costs. More specifically, English-centric tokenizers applied to multilingual LLMs result in severe downstream performance degradation and additional training costs of up to 68% due to inefficient tokenization vocabulary.

However, extended tokenizers decrease confidence in incorrect predictions during generation and reduce cross-entropy in complex tasks, potentially leading to higher performance in downstream tasks.

### MGSM Benchmark and Reasoning Performance

MGSM is a benchmark that assesses multilingual mathematical reasoning using 250 grade-school word problems across 10 diverse languages. Research on this benchmark reveals important issues about robustness:

Many low-resource languages suffer large performance drops when tested on digit instantiations different from those in the original test set. Low-resource languages suffer the most in terms of huge drop in performance, in some cases losing more than -20.0 drop in performance.

Evaluations across nine languages reveal that many low-resource languages suffer large performance drops when tested on digit instantiations different from the original test set, and model robustness in high-resource language settings does not necessarily translate to low-resource language settings.

The research indicates that while vocabulary expansion and tokenizer adaptation are essential for improving multilingual LLM efficiency and capability, careful attention must be paid to downstream task robustness, particularly for low-resource languages in reasoning benchmarks like MGSM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7db129a4-c623-4db5-9ed9-800fc0e72fb3",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "ef2bc43d-e735-4926-b43d-c52de398bd10",
  "sourceToolAssistantUUID": "7db129a4-c623-4db5-9ed9-800fc0e72fb3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-19T23:32:40.119Z_

Let me fetch more papers and do additional targeted searches on the specific gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef2bc43d-e735-4926-b43d-c52de398bd10",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoQLV45rbhvhULG4M1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23a7076e-dade-4fa6-aa60-0f0ed5756056",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StdMuHuDCTTYq68KTniD95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 518,
      "cache_creation_input_tokens": 5113,
      "cache_read_input_tokens": 17615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5113,
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

_source line 43 · 2026-05-19T23:32:42.557Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018PbGpozp57fC5DTLbAcYyo`</summary>

```json
{
  "url": "https://arxiv.org/html/2402.14714v1",
  "prompt": "Extract ALL details about: 1) What is EEVE's exact method for vocabulary expansion? 2) What models and scales? 3) Which downstream benchmarks including reasoning tasks were tested? Specifically list all benchmarks. 4) Was MGSM tested? 5) How much continued pretraining was needed? 6) Did vocabulary expansion help or hurt reasoning benchmarks specifically? 7) What were the specific numbers on reasoning benchmarks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23a7076e-dade-4fa6-aa60-0f0ed5756056",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoQLV45rbhvhULG4M1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c718519f-f5c2-4268-87b2-795a39eaaca8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StdMuHuDCTTYq68KTniD95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 518,
      "cache_creation_input_tokens": 5113,
      "cache_read_input_tokens": 17615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5113,
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

_source line 44 · 2026-05-19T23:32:44.483Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018YWya8GaB72XGeD975AynQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.12560v1",
  "prompt": "Extract ALL details about: 1) How does a language-specific tokenizer affect LLMs? 2) What downstream reasoning benchmarks were tested? 3) What scale models? 4) What specific results on reasoning tasks? 5) Does changing the tokenizer degrade reasoning? 6) Key findings about tokenizer vs reasoning performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c718519f-f5c2-4268-87b2-795a39eaaca8",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoQLV45rbhvhULG4M1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b63ded-6574-405b-a949-6a31679c5f3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StdMuHuDCTTYq68KTniD95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 518,
      "cache_creation_input_tokens": 5113,
      "cache_read_input_tokens": 17615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5113,
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

_source line 45 · 2026-05-19T23:32:45.895Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017dmQ1AASHHhRA2ko25DHs2`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.03523v1",
  "prompt": "Extract ALL details about TokAlign: 1) What is the method? 2) What models and scales tested? 3) Were downstream reasoning benchmarks tested (MGSM, MMLU, etc.)? 4) How much retraining needed? 5) Key results on whether vocabulary adaptation preserves reasoning? 6) Specific benchmark numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11b63ded-6574-405b-a949-6a31679c5f3d",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoQLV45rbhvhULG4M1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6c383d1-d1f1-49c6-ba38-cb80d9418e57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StdMuHuDCTTYq68KTniD95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 518,
      "cache_creation_input_tokens": 5113,
      "cache_read_input_tokens": 17615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5113,
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

_source line 46 · 2026-05-19T23:32:46.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01289eEUSSUjQ2SCvoUDydZB`</summary>

```json
{
  "query": "vocabulary expansion LLM 70B 235B scale model downstream reasoning benchmark evaluation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c383d1-d1f1-49c6-ba38-cb80d9418e57",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoQLV45rbhvhULG4M1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8faea7e2-55b2-42d3-a6c3-0c4253106ba7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StdMuHuDCTTYq68KTniD95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 518,
      "cache_creation_input_tokens": 5113,
      "cache_read_input_tokens": 17615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5113,
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

_source line 47 · 2026-05-19T23:32:47.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T4x5rVa8iovi5B6EDz7we1`</summary>

```json
{
  "query": "\"tokenizer replacement\" OR \"vocabulary addition\" breaks reasoning chain-of-thought language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8faea7e2-55b2-42d3-a6c3-0c4253106ba7",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoQLV45rbhvhULG4M1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bec1b086-7fe3-4919-b675-a8a6a476eaca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StdMuHuDCTTYq68KTniD95",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 518,
      "cache_creation_input_tokens": 5113,
      "cache_read_input_tokens": 17615,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 518,
          "output_tokens": 589,
          "cache_read_input_tokens": 17615,
          "cache_creation_input_tokens": 5113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5113,
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

_source line 48 · 2026-05-19T23:32:50.317Z_

<details><summary>↩ Tool result · `toolu_018PbGpozp57fC5DTLbAcYyo`</summary>

```text
# EEVE Vocabulary Expansion Analysis

## 1) EEVE's Exact Method

EEVE combines three key components:

- **Tokenizer Training**: Added 8,960 new Korean tokens (appearing ≥6,000 times) to the base vocabulary, expanding it to 40,960 tokens total
- **Subword-based Embedding Initialization**: New input embeddings initialized as averages of constituent subword embeddings; output embeddings initialized from the first subword token
- **Multi-stage Training**: Seven sequential training stages with progressive parameter freezing, starting with only input embeddings, then output embeddings, then both, gradually unfreezing base model parameters

## 2) Models and Scales

Two model variants were released:
- EEVE-Korean-10.8B-v1.0 (based on SOLAR-10.7B)
- EEVE-Korean-2.8B-v1.0 (based on Phi-2)

## 3) Downstream Benchmarks

The evaluation tested **five specific benchmarks**:
- BoolQ (Boolean Question Answering)
- COPA (Commonsense Causal Reasoning)
- HellaSwag (Commonsense Reasoning)
- WiC (Context-sensitive Word Understanding)
- SentiNeg (Sentiment Negation Recognition)

**Notably, no reasoning tasks like GSM8K or mathematical reasoning were included in the main evaluation**, though the authors mention this as future work.

## 4) MGSM Testing

**No, MGSM was not tested.** The paper makes no mention of MGSM benchmarks.

## 5) Continued Pretraining Required

The method required "just 2 billion tokens" of Korean pre-training across the seven stages, contrasting with claims that "new embeddings require trillions of training tokens."

## 6) Vocabulary Expansion Impact on Reasoning

**This cannot be answered from the paper.** No explicit reasoning benchmarks were evaluated in the main results, making direct assessment impossible.

## 7) Specific Reasoning Benchmark Numbers

**No reasoning benchmark scores are provided.** The evaluation focused exclusively on language understanding tasks, not reasoning capabilities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c718519f-f5c2-4268-87b2-795a39eaaca8",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "f7c39f1e-4ea4-4a59-9f0a-529430d4ad33",
  "sourceToolAssistantUUID": "c718519f-f5c2-4268-87b2-795a39eaaca8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T23:32:50.761Z_

<details><summary>↩ Tool result · `toolu_018YWya8GaB72XGeD975AynQ`</summary>

```text
# Analysis of Language-Specific Tokenizers and LLM Performance

## 1) How Language-Specific Tokenizers Affect LLMs

The research demonstrates that language-specific tokenizers significantly impact LLM behavior. The extended Korean tokenizer reduces byte-level segmentation (0.96% unknown tokens vs. 48.61% for base Llama-2), resulting in shorter average token sequences (125.91 vs. 325.27 tokens). The study found that "the extended tokenizer decreases confidence in incorrect predictions during generation" and produces more semantically coherent outputs.

## 2) Downstream Reasoning Benchmarks Tested

**None were tested.** This study explicitly uses only intrinsic evaluation through Next Token Prediction (NTP) tasks, not downstream benchmarks. The authors note: "we opt for a pretrained model instead of instruction-tuned model" and focus on understanding tokenizer effects through controlled NTP experiments rather than downstream task performance.

## 3) Model Scale

The research uses **TinyLlama with 1.1 billion parameters**—a deliberately small model. The authors acknowledge this limitation: "the results cannot be directly generalized to larger models" and suggest future work should explore varying model sizes.

## 4) Specific Results on Reasoning Tasks

No reasoning task results exist in this paper, as reasoning benchmarks were not evaluated.

## 5) Does Tokenizer Change Degrade Reasoning?

This question cannot be answered from this research, which doesn't assess reasoning capabilities.

## 6) Key Findings About Tokenizer vs. Reasoning Performance

The study found that extended tokenizers demonstrate:
- **Lower confidence on incorrect predictions** (character/word-level tasks)
- **Reduced cross-entropy loss on complex tasks**
- **Greater generation stability**, though not necessarily higher accuracy on granular predictions
- The authors hypothesize these factors "potentially lead to higher performance in downstream tasks"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11b63ded-6574-405b-a949-6a31679c5f3d",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "7ca3627b-dcd0-4628-b57a-d7bfe57b66b6",
  "sourceToolAssistantUUID": "11b63ded-6574-405b-a949-6a31679c5f3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T23:32:53.639Z_

<details><summary>↩ Tool result · `toolu_017dmQ1AASHHhRA2ko25DHs2`</summary>

```text
# TokAlign: Efficient Vocabulary Adaptation Analysis

## 1) What is the method?

TokAlign aligns token vocabularies between LLMs using token co-occurrence information. The approach involves three steps: tokenizing a mixed corpus, learning token representations via GloVe, and creating a one-to-one mapping matrix based on cosine similarity. The system then rearranges model parameters and applies progressive two-stage fine-tuning for stability.

## 2) Models and scales tested

The research evaluated Pythia models (1B, 2.8B, 6.9B parameters) as base models. Target vocabularies came from Gemma, Qwen2, LLaMA2, and LLaMA3. Cross-model distillation used teacher models including "Gemma 7B, Qwen2 7B, and LLaMA3 8B."

## 3) Downstream reasoning benchmarks tested

**Not tested.** The paper evaluated only general language understanding tasks: XNLI, PAWS-X, XCOPA, XStoryCloze for cross-lingual transfer, and ARC-E, BoolQ, HellaSwag, OpenbookQA, PIQA, WinoGrande for downstream evaluation. No reasoning-specific benchmarks like MGSM or MMLU appear in the results.

## 4) Retraining needed

"As few as 5k steps are needed for our method to recover the performance of vanilla models." The paper states that "after only 2k steps of Language Adaptation Tuning," the method achieved improvements on multilingual tasks.

## 5) Key reasoning preservation results

No reasoning-specific evaluation exists. However, general capability preservation reached "97.6% performance of the base model" on average after vocabulary replacement, recovering to "98.0% performance" with only 5k steps.

## 6) Specific benchmark numbers

**Perplexity (cross-lingual):** Decreased from 3.4e² to 1.2e² after TokAlign initialization across 13 languages, improving compression rates by 29.2% average.

**Token-level distillation gains:** "4.4% better than sentence-level distillation" using Qwen2 7B as teacher with only 235M tokens.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6c383d1-d1f1-49c6-ba38-cb80d9418e57",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "24a14a3d-661f-41b1-ad85-5da8618d68d8",
  "sourceToolAssistantUUID": "c6c383d1-d1f1-49c6-ba38-cb80d9418e57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T23:32:53.907Z_

<details><summary>↩ Tool result · `toolu_01T4x5rVa8iovi5B6EDz7we1`</summary>

```text
Web search results for query: ""tokenizer replacement" OR "vocabulary addition" breaks reasoning chain-of-thought language model"

Links: [{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/html/2601.14658v1"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.14658"},{"title":"Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning","url":"https://arxiv.org/pdf/2502.03275"},{"title":"Break the Chain: Large Language Models Can be Shortcut Reasoners","url":"https://arxiv.org/pdf/2406.06580"},{"title":"Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning","url":"https://arxiv.org/html/2502.03275v1"},{"title":"Tokenization Demystified: Building Tokenizers for Language Models | by Suvradeep | Medium","url":"https://medium.com/@suvraadeep/tokenization-demystified-building-tokenizers-for-language-models-9cd18cb26dab"}]

Here are the key findings from my web search:

## Main Research Finding

A significant paper titled "Say Anything but This: When Tokenizer Betrays Reasoning in LLMs" demonstrates that tokenizer failures persist across open-source LLM families even as model parameters increase, and provides a systematic taxonomy of mechanisms underlying these failures, including whitespace-boundary manipulations and intra-word resegmentation patterns that systematically compromise LLM reasoning.

## How Tokenization Affects Reasoning

The tokenizer imposes structural artifacts on the model's internal representation of language by defining how text is segmented, and the availability of numerous subtoken units enables different subtoken combinations to concatenate into the same word, establishing representational non-uniqueness.

## Vocabulary Extension Challenges

Another relevant study on vocabulary expansion found that one technical challenge posed for fine-tuning is that the vocabulary is now extended and contains unseen latent tokens. The research addresses this by introducing a simple training procedure that randomly mixes latent and text tokens, which enables fast adaptation to new latent tokens.

These findings suggest that both tokenizer replacement and vocabulary addition can create representational mismatches that negatively impact the chain-of-thought reasoning capabilities of language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bec1b086-7fe3-4919-b675-a8a6a476eaca",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "79c96e18-6369-41dc-982f-23eb44cad1d3",
  "sourceToolAssistantUUID": "bec1b086-7fe3-4919-b675-a8a6a476eaca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T23:32:54.267Z_

<details><summary>↩ Tool result · `toolu_01289eEUSSUjQ2SCvoUDydZB`</summary>

```text
Web search results for query: "vocabulary expansion LLM 70B 235B scale model downstream reasoning benchmark evaluation 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"Is GPT-OSS Good? A Comprehensive Evaluation of OpenAI’s Latest Open Source Models ∗: Equal contribution. †: Corresponding author: Junhao Song (junhao.song23@imperial.ac.uk)","url":"https://arxiv.org/html/2508.12461v1"},{"title":"evaluation of reasoning in language models","url":"https://arxiv.org/pdf/2509.24210"},{"title":"The 2025 Planning Performance of Frontier Large Language Models","url":"https://arxiv.org/pdf/2511.09378"},{"title":"Challenging the Boundaries of Reasoning: An Olympiad-Level Math Benchmark for Large Language Models","url":"https://arxiv.org/html/2503.21380v2"},{"title":"Vocabulary Expansion of Large Language Models via Kullback-Leibler-Based Self-Distillation","url":"https://arxiv.org/pdf/2508.15807"},{"title":"Revisiting the Scaling Properties of Downstream Metrics in Large Language Model Training","url":"https://arxiv.org/pdf/2512.08894"},{"title":"Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies","url":"https://arxiv.org/pdf/2407.13623"},{"title":"Reasoning Effort and Problem Complexity: A Scaling Analysis in LLMs","url":"https://arxiv.org/pdf/2503.15113"}]

Based on the search results, I found relevant information about your query. Here are the key findings:

## Model Scale and Evaluation

Recent comprehensive evaluations have tested models ranging from 14.7B to 235B parameters, including both dense and sparse designs, across ten benchmarks covering general knowledge, mathematical reasoning, code generation, multilingual understanding, and conversational ability. 70B parameter models such as Llama 3.3 70B and DeepSeek-R1 70B represent competitive alternatives in their size category.

## Vocabulary and Scaling

The optimal vocabulary size depends on the available compute budget and larger models deserve larger vocabularies; for example, the optimal vocabulary size of Llama2-70B is predicted to have been at least 216K, 7 times larger than its actual vocabulary of 32K. Adopting predicted optimal vocabulary sizes consistently improves downstream performance over commonly used vocabulary sizes.

## Downstream Reasoning Benchmarks

Important research directions track the behavior of interpretable indicators of model capabilities, like accuracy on downstream benchmarks measuring performance on general knowledge, reasoning, math and coding tasks. Notable reasoning benchmarks include GSM8K, ARC-AGI, GPQA, MMLU, SWE-bench and NPhard-eval.

## Vocabulary Expansion Methods

Recent work addresses vocabulary expansion in LLMs by introducing mathematically grounded methods for knowledge distillation via KL divergence, allowing student models to inherit distributional knowledge from teachers despite differing vocabularies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8faea7e2-55b2-42d3-a6c3-0c4253106ba7",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "e407d7af-1b29-49dc-959b-589d60c62028",
  "sourceToolAssistantUUID": "8faea7e2-55b2-42d3-a6c3-0c4253106ba7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-19T23:32:57.334Z_

This is very interesting -- let me fetch that critical paper about tokenizer betraying reasoning, plus a few more targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e407d7af-1b29-49dc-959b-589d60c62028",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoRbP2C49KDDGPcQNS6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc8583d3-79de-43a4-ba65-4a3b42bc9593",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTiQ7hHprFeSrCai1QaFmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 22728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 54 · 2026-05-19T23:33:00.159Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019iMXStHfmDhxoWcB7g6jR2`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.14658v1",
  "prompt": "Extract ALL details about: 1) How does the tokenizer betray reasoning in LLMs? 2) What specific reasoning failures are caused by tokenization? 3) What models and scales were tested? 4) What benchmarks were used? 5) What is the taxonomy of tokenizer-induced reasoning failures? 6) Does this apply to vocabulary expansion specifically? 7) Key results and numbers? 8) How do these failures scale with model size?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc8583d3-79de-43a4-ba65-4a3b42bc9593",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoRbP2C49KDDGPcQNS6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6326b983-2e72-41b2-bf46-af2a920d7e83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTiQ7hHprFeSrCai1QaFmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 22728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 55 · 2026-05-19T23:33:02.570Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KCRb3GC5aSvVhHmtF8RMmF`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.15807",
  "prompt": "Extract ALL details about: 1) What is the KL-based self-distillation method for vocabulary expansion? 2) What models and scales tested? 3) Were downstream reasoning benchmarks tested (MGSM, MMLU, GSM8K)? 4) Key results about reasoning preservation? 5) What specific benchmark numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6326b983-2e72-41b2-bf46-af2a920d7e83",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoRbP2C49KDDGPcQNS6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d01f6b1c-87f9-4bb3-b928-36a54a6b9e5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTiQ7hHprFeSrCai1QaFmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 22728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 56 · 2026-05-19T23:33:03.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LbJ3mxJYXEHzjYnuyRKVaj`</summary>

```json
{
  "query": "\"post-hoc\" tokenizer vocabulary modification frozen model weights embedding initialization downstream evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01f6b1c-87f9-4bb3-b928-36a54a6b9e5c",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoRbP2C49KDDGPcQNS6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f14fcc0-1cb5-4a3c-b575-62f8d2776fed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTiQ7hHprFeSrCai1QaFmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 22728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 57 · 2026-05-19T23:33:04.378Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wuq2xUuDVXbuZ82yNVR8Ub`</summary>

```json
{
  "query": "Kuwain Arabic language injection vocabulary expansion reasoning benchmark evaluation LLaMA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f14fcc0-1cb5-4a3c-b575-62f8d2776fed",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoRbP2C49KDDGPcQNS6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf8bcd5a-29cc-45bb-9e4e-7d4d8058be48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTiQ7hHprFeSrCai1QaFmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 621,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 22728,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3438
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 621,
          "output_tokens": 453,
          "cache_read_input_tokens": 22728,
          "cache_creation_input_tokens": 3438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3438,
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

_source line 58 · 2026-05-19T23:33:07.448Z_

<details><summary>↩ Tool result · `toolu_01KCRb3GC5aSvVhHmtF8RMmF`</summary>

```text
# KL-Based Self-Distillation for Vocabulary Expansion

## 1) Method Overview
The paper proposes a Kullback-Leibler (KL) divergence-based self-distillation approach to expand language model vocabularies. This technique enables models to incorporate new tokens while preserving reasoning capabilities through careful knowledge transfer from the original model to an expanded version.

## 2) Models and Scales Tested
The research evaluated vocabulary expansion across multiple model architectures and sizes, examining how the method scales across different configurations to ensure practical applicability.

## 3) Downstream Reasoning Benchmarks
Yes, the study specifically tested reasoning preservation on several important benchmarks:
- **MGSM** (Multilingual Grade School Math)
- **MMLU** (Massive Multitask Language Understanding)
- **GSM8K** (Grade School Math)

These benchmarks were critical for validating that expanded vocabularies maintain reasoning performance.

## 4) Key Results on Reasoning Preservation
The KL-based self-distillation method successfully preserved reasoning capabilities during vocabulary expansion, demonstrating that "expanded models maintained performance on downstream reasoning tasks" through careful probability distribution alignment.

## 5) Specific Benchmark Numbers
The document structure indicates benchmark results were included, though the exact numerical scores require accessing the results sections within the paper's content pages (the PDF metadata shows 58 pages of detailed experimental results).

[Binary content (application/pdf, 860.6KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/ec50337c-efb0-4976-b822-6e64218d6124/tool-results/webfetch-1779233582582-jk9gwc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d01f6b1c-87f9-4bb3-b928-36a54a6b9e5c",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "08bfda9d-0e0e-41d1-a872-7a541c2a46cb",
  "sourceToolAssistantUUID": "d01f6b1c-87f9-4bb3-b928-36a54a6b9e5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T23:33:11.018Z_

<details><summary>↩ Tool result · `toolu_01Wuq2xUuDVXbuZ82yNVR8Ub`</summary>

```text
Web search results for query: "Kuwain Arabic language injection vocabulary expansion reasoning benchmark evaluation LLaMA 2025"

Links: [{"title":"Paper page - Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://huggingface.co/papers/2504.15120"},{"title":"Kuwain 1.5B: An Arabic SLM via Language Injection | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/kuwain-15b-arabic-slm-via-language-injection"},{"title":"[PDF] Kuwain 1.5B: An Arabic SLM via Language Injection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/91a18fd8558f752e8dc51e6ca5a323eb234fe634"},{"title":"Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://www.arxiv.org/pdf/2504.15120"},{"title":"[2504.15120] Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://arxiv.org/abs/2504.15120"},{"title":"Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://arxiv.org/html/2504.15120v1"},{"title":"[Literature Review] Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://www.themoonlight.io/en/review/kuwain-15b-an-arabic-slm-via-language-injection"},{"title":"[2504.15120v1] Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://arxiv.org/abs/2504.15120v1"},{"title":"(PDF) Kuwain 1.5B: An Arabic SLM via Language Injection","url":"https://www.researchgate.net/publication/390990787_Kuwain_15B_An_Arabic_SLM_via_Language_Injection"}]

Based on the search results, here's what I found about Kuwain:

## Kuwain 1.5B: An Arabic SLM via Language Injection

Kuwain is a 1.5 billion parameter model created by injecting the Arabic language into a small open-source model mainly trained in English. The paper was published on April 22, 2025.

**Key Features:**
- The paper introduces a novel method for integrating a new language into an LLM while successfully incorporating a previously unseen target language into an existing LLM without compromising its prior knowledge.
- The approach focuses on expanding the TinyLlama 1.1B model's capabilities by injecting Arabic language understanding and generation through strategic layer extension and vocabulary expansion.

**Performance Results:**
- The method demonstrates significant improvements in Arabic language performance, with an average 8% improvement across various benchmarks, while retaining the model's existing knowledge with a minimum amount of the original model's data.
- The vocabulary was expanded with additional 26K Arabic tokens, and Kuwain achieves an expansion ratio of 2.30—very close to Jais's performance despite using 41% fewer tokens.

**Significance:**
This offers a cost-effective alternative to training a comprehensive model in both English and Arabic, highlighting the potential for efficient, targeted language model expansion without extensive retraining or resource-intensive processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf8bcd5a-29cc-45bb-9e4e-7d4d8058be48",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "db2edfae-819d-4608-a02d-4e86f498df8a",
  "sourceToolAssistantUUID": "cf8bcd5a-29cc-45bb-9e4e-7d4d8058be48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T23:33:12.298Z_

<details><summary>↩ Tool result · `toolu_019iMXStHfmDhxoWcB7g6jR2`</summary>

```text
# How Tokenizers Betray LLM Reasoning: Key Findings

## 1) Core Mechanism of Tokenizer Betrayal

The fundamental issue stems from tokenizers producing **non-unique encodings**—"multiple token ID sequences can detokenize to identical surface strings." This one-to-many mapping creates a representational mismatch where models treat different internal token sequences as distinct despite encoding semantically identical text.

## 2) Specific Reasoning Failures from Tokenization

Models exhibit "phantom edits"—cases where they output different token IDs that decode to the same word. The paper demonstrates that models internally "believe" they've successfully executed substitutions when no actual content change occurred at the text level, even though token-level representations differ.

## 3) Models and Scales Tested

The study evaluated **ten state-of-the-art open-source LLMs** across four families:
- **Gemma**: 270M, 1B, 4B, 12B parameters
- **Llama**: 1B, 3B, 8B parameters  
- **Mistral**: 8B, 24B parameters
- **Qwen**: 4B, 30B parameters

## 4) Benchmark/Task Used

A custom **tokenization-consistency probe** requiring models to replace bracketed words in context while preserving all other text unchanged. Testing used 5% of non-stop words from XSUM dataset articles (100-600 word range), totaling over 11,000 replacement trials.

## 5) Taxonomy of Eight Tokenizer-Induced Artifacts

1. **Whitespace-boundary shift**: swapping space-prefixed with non-prefixed token variants
2. **Whitespace detachment/reattachment**: splitting or combining explicit space tokens
3. **Newline/whitespace substitution**: replacing spaces with newline tokens
4. **Intra-word resegmentation**: decomposing atomic tokens into constituent subtokens
5. **Proper-noun segmentation ambiguity**: alternative decompositions of rare words
6. **Morphological boundary surfacing**: resegmenting along morphemic boundaries
7. **Acronym splitting**: alternative tokenizations of capital-letter sequences
8. **Plural/possessive tail tokens**: resegmenting words like "rights" as ["right", "s"]

## 6) Vocabulary Expansion Application

The paper emphasizes that "duplicate single-token variants causes systematic model failures," particularly regarding whitespace variants (Error Type 1). This directly relates to vocabulary design redundancies enabling problematic token-space edits without surface-level changes.

## 7) Key Results and Numbers

- **Non-trivial failure rates persist across all model sizes**
- Approximately **72.2% of phantom edits** preserve subtoken count while altering token ID identity alone
- About **78% of cases** maintain identical subtoken counts (1→1 transitions)
- **19.7%** increase token count through splitting; only **2.3%** decrease through merging
- Token ID masking intervention reduced phantom edit rates to **0-5%** across models

## 8) Failure Scaling with Model Size

Contrary to expectations, **model size is not the primary bottleneck**. The paper found that "within the Qwen3 and Gemma3 families, some larger variants achieve replacement success that is comparable to or even lower than that of smaller counterparts." The "Different" failure category persists across all parameter scales, indicating tokenization artifacts represent a fundamental architectural constraint rather than a capacity limitation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6326b983-2e72-41b2-bf46-af2a920d7e83",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "3e91d8a7-81b5-42be-8acb-b23611ef7452",
  "sourceToolAssistantUUID": "6326b983-2e72-41b2-bf46-af2a920d7e83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T23:33:13.652Z_

<details><summary>↩ Tool result · `toolu_01LbJ3mxJYXEHzjYnuyRKVaj`</summary>

```text
Web search results for query: ""post-hoc" tokenizer vocabulary modification frozen model weights embedding initialization downstream evaluation"

Links: [{"title":"Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/html/2506.06607v1"},{"title":"Reducing Tokenization Premiums for Low-Resource Languages","url":"https://arxiv.org/html/2601.13328v1"},{"title":"Getting the most out of your tokenizer for pre-training and domain adaptation","url":"https://arxiv.org/html/2402.01035v2"},{"title":"Vocabulary Expansion of Chat Models with Unlabeled Target Language Data","url":"https://arxiv.org/html/2412.11704v1"},{"title":"[2506.06607] Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/abs/2506.06607"},{"title":"How to bring my tokenizer and set vocabulary size accordingly for training a model with loaded weights · Issue #2087 · Lightning-AI/litgpt","url":"https://github.com/Lightning-AI/litgpt/issues/2087"},{"title":"Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit","url":"https://arxiv.org/pdf/2506.06607"},{"title":"Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models","url":"https://arxiv.org/html/2512.03989v2"},{"title":"Model-Aware Tokenizer Transfer","url":"https://arxiv.org/html/2510.21954v1"}]

Based on the web search results, I found several relevant papers addressing post-hoc tokenizer vocabulary modification, frozen model weights, embedding initialization, and downstream evaluation:

## Key Research Areas

### Post-Hoc Vocabulary Modification with Frozen Weights

A training-free approach using Orthogonal Matching Pursuit (OMP) on shared-token embeddings preserves perplexity and classification accuracy far better than naive heuristics. This method reconstructs unseen token embeddings by approximating each out-of-vocabulary token as a sparse linear combination of shared tokens.

Post-hoc vocabulary modifications can reduce tokenization premiums in pre-trained models by adding tokens that coalesce multi-token characters into single tokens.

### Embedding Initialization Strategies

Fast Vocabulary Transfer (FVT) is applied to initialize the weights of new embeddings when changing tokenizers. WECHSEL uses FastText embeddings and a translation vocabulary to identify the closest source tokens, with new embeddings initialized as weighted averages of source embeddings.

Methods like OMP, when compared to baselines (zero-init, mean-init, and existing approaches like WECHSEL, FOCUS, ZETT), consistently achieve the best overall performance without gradient updates.

### Downstream Evaluation

Downstream performance is evaluated on tasks like code generation after tokenizer fine-tuning, while translation quality is assessed using benchmarks like Belebele, Global MMLU, and Long FLORES.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f14fcc0-1cb5-4a3c-b575-62f8d2776fed",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "61b36ced-7487-40c8-8a56-31381033dadb",
  "sourceToolAssistantUUID": "5f14fcc0-1cb5-4a3c-b575-62f8d2776fed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-19T23:33:17.995Z_

Let me fetch the OMP paper for more details on downstream evaluation, and dig into the KL-distillation paper's actual benchmark numbers, plus the Kuwain paper's benchmark details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61b36ced-7487-40c8-8a56-31381033dadb",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoT2TB2EnY8T9QpYSLW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5db9408a-e248-4189-8a31-b7f8f98185a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMzUAsQPxbvZwTZ8m5cREj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 3099,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3099,
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

_source line 63 · 2026-05-19T23:33:21.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BHasEzNxdp1vwfx4pYN8qB`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.06607v1",
  "prompt": "Extract ALL details about: 1) What exactly are the downstream benchmarks used? List every benchmark. 2) What models and scales? 3) What are the specific numerical results on each benchmark? 4) Does the method preserve reasoning? 5) How does OMP compare to WECHSEL, FOCUS on downstream tasks? 6) Was this tested with completely frozen model weights (no retraining at all)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5db9408a-e248-4189-8a31-b7f8f98185a7",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoT2TB2EnY8T9QpYSLW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d24b1dd6-0c02-43ee-832a-10d3007b3886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMzUAsQPxbvZwTZ8m5cREj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 3099,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3099,
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

_source line 64 · 2026-05-19T23:33:24.144Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01389NpcNhrNEz6sSUmsfLuM`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15120v1",
  "prompt": "Extract ALL details about: 1) What is the exact vocabulary expansion method? 2) What benchmarks were tested - list ALL benchmarks? 3) Were reasoning benchmarks tested (MGSM, GSM8K, MMLU, ARC)? 4) What are the specific numerical results? 5) How much retraining was needed? 6) Did vocabulary expansion help or hurt reasoning specifically?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d24b1dd6-0c02-43ee-832a-10d3007b3886",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoT2TB2EnY8T9QpYSLW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "728c40ed-dec6-431b-9b37-1b24c3f920c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMzUAsQPxbvZwTZ8m5cREj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 3099,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3099,
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

_source line 65 · 2026-05-19T23:33:25.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GL7Vjr4BaB5FW8n73KNqer`</summary>

```json
{
  "query": "tokenizer vocabulary expansion 70B parameter model LLaMA Qwen reasoning benchmark MMLU GSM8K 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "728c40ed-dec6-431b-9b37-1b24c3f920c8",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoT2TB2EnY8T9QpYSLW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f33d75dd-fadd-42e2-8864-c74456393016",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMzUAsQPxbvZwTZ8m5cREj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 3099,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3099,
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

_source line 66 · 2026-05-19T23:33:25.892Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SqkeHrxwA5d7rsGqeCdiCx`</summary>

```json
{
  "query": "\"stop taking tokenizers for granted\" core design decisions 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f33d75dd-fadd-42e2-8864-c74456393016",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoT2TB2EnY8T9QpYSLW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9529cc1a-9ef8-40ac-8a63-b962905d4fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMzUAsQPxbvZwTZ8m5cREj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 3099,
      "cache_read_input_tokens": 26166,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 864,
          "output_tokens": 488,
          "cache_read_input_tokens": 26166,
          "cache_creation_input_tokens": 3099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3099,
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

_source line 67 · 2026-05-19T23:33:31.069Z_

<details><summary>↩ Tool result · `toolu_01SqkeHrxwA5d7rsGqeCdiCx`</summary>

```text
Web search results for query: ""stop taking tokenizers for granted" core design decisions 2026 arxiv"

Links: [{"title":"[2601.13260] Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models","url":"https://arxiv.org/abs/2601.13260"},{"title":"Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models","url":"https://arxiv.org/pdf/2601.13260"},{"title":"Stop Taking Tokenizers for Granted: They Are Core Design Decisions in","url":"https://www.arxiv.org/pdf/2601.13260"},{"title":"[Literature Review] Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models","url":"https://www.themoonlight.io/en/review/stop-taking-tokenizers-for-granted-they-are-core-design-decisions-in-large-language-models"},{"title":"Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models","url":"https://arxiv.org/html/2601.13260v2"}]

I found the paper you're looking for! Here's what the search revealed:

The paper "Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models" was authored by Sawsan Alqahtani and 4 other authors, published on arXiv on January 19, 2026 (with an updated version on January 24, 2026).

**Key arguments from the paper:**

The paper argues that tokenization underlies every large language model, yet it remains an under-theorized and inconsistently designed component. Common subword approaches such as Byte Pair Encoding (BPE) offer scalability but often misalign with linguistic structure, amplify bias, and waste capacity across languages and domains.

The paper reframes tokenization as a core modeling decision rather than a preprocessing step, and argues for a context-aware framework that integrates tokenizer and model co-design, guided by linguistic, domain, and deployment considerations.

The paper's arXiv identifier is **2601.13260**, and you can access it at https://arxiv.org/abs/2601.13260.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9529cc1a-9ef8-40ac-8a63-b962905d4fa2",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "d5d20f3b-524c-4b06-be80-455ca647d701",
  "sourceToolAssistantUUID": "9529cc1a-9ef8-40ac-8a63-b962905d4fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T23:33:31.524Z_

<details><summary>↩ Tool result · `toolu_01389NpcNhrNEz6sSUmsfLuM`</summary>

```text
# Kuwain 1.5B: Vocabulary Expansion and Evaluation Details

## 1) Vocabulary Expansion Method

The expansion employed SentencePiece tokenization trained on their Arabic dataset, resulting in "a vocabulary of 26K tokens" that extended the base model's tokenizer to "54K tokens" total. They analyzed gaps where the existing tokenizer failed for Arabic representation, noting that many English-centric models contained "only 28 Arabic tokens" versus their expanded coverage.

## 2) ALL Benchmarks Tested

**English benchmarks:** HellaSwag, Obqa, ARC-c, ARC-e, BoolQ, PIQA, WinoGrande

**Arabic benchmarks:** HellaSwag, Obqa, ARC-c, ARC-e, BoolQ, PIQA, Copa

**Leaderboard evaluation:** Arabic NLP benchmark comparisons against 50+ models

## 3) Reasoning Benchmarks Tested

**No.** Strict reasoning benchmarks (MGSM, GSM8K, MMLU) were not included. The evaluation used commonsense reasoning tasks like ARC (multiple-choice) and COPA (causal reasoning), but not specialized mathematical or comprehensive knowledge reasoning benchmarks.

## 4) Specific Numerical Results

- **Arabic improvement:** "8% improvement across various benchmarks"
- **English preservation:** "1%" slight improvement
- **Training cost reduction:** "70%" reduction
- **Average Arabic score:** 44.49 (Kuwain vs. 36.95 for base TinyLlama)
- **English benchmark average:** 53.28 maintained (vs. 52.99 baseline)

## 5) Retraining Requirements

Training occurred "on 8 A100 GPUs for 3 epochs" with "1M tokens" effective batch size, targeting "only the newly added layers" while keeping original layers frozen—a 70% cost reduction approach.

## 6) Vocabulary Expansion Impact on Reasoning

**Unaddressed in paper.** The study does not isolate vocabulary expansion's specific effect on reasoning tasks separately. Improvements reported are aggregate across all benchmarks without disaggregated analysis of reasoning performance specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "728c40ed-dec6-431b-9b37-1b24c3f920c8",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "790098ad-984a-4784-b0b5-d2a78b3090a7",
  "sourceToolAssistantUUID": "728c40ed-dec6-431b-9b37-1b24c3f920c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-19T23:33:32.481Z_

<details><summary>↩ Tool result · `toolu_01GL7Vjr4BaB5FW8n73KNqer`</summary>

```text
Web search results for query: "tokenizer vocabulary expansion 70B parameter model LLaMA Qwen reasoning benchmark MMLU GSM8K 2025 2026"

Links: [{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Think-at-Hard: Selective Latent Iterations to Improve Reasoning Language Models","url":"https://arxiv.org/html/2511.08577v2"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"LLM Reasoning Does Not Protect Against Clinical Cognitive Biases - An Evaluation Using BiasMedQA","url":"https://www.medrxiv.org/content/10.1101/2025.06.22.25330078.full.pdf"},{"title":"Qwen2 Technical Report","url":"https://arxiv.org/pdf/2407.10671"}]

Based on the search results, I found relevant information about tokenizer, vocabulary, LLaMA, Qwen models, and benchmarks mentioned in your query. Here are the key findings:

## Tokenizer and Vocabulary Expansion

LLaMA 3 introduced a 128K vocabulary tokenizer (vs 32K) reducing sequence length by 30%, which represents a significant vocabulary expansion compared to earlier models. In contrast, Qwen2 models employ a common vocabulary consisting of 151,643 regular tokens and 3 control tokens.

## 70B Parameter Models and Benchmarks

For 70B parameter models, there's substantial benchmark data available:

- **Qwen2-72B Performance**: The flagship model, Qwen2-72B, showcases remarkable performance: 84.2 on MMLU, 37.9 on GPQA, 64.6 on HumanEval, 89.5 on GSM8K, and 82.4 on BBH as a base language model.

## Recent 2025-2026 Benchmark Trends

Frontier models now reach 99% on GSM8K (GPT-5.3 Codex), making GSM8K useless for top-tier comparisons. Additionally, MMLU is saturated (88-94% for top models) and no longer differentiates frontier models. Instead, use: GPQA Diamond for scientific reasoning, SWE-bench Verified or SWE-bench Pro for coding, AIME 2025 for mathematical reasoning.

The search results show that newer reasoning benchmarks have become more important than GSM8K and MMLU for evaluating frontier models in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f33d75dd-fadd-42e2-8864-c74456393016",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "dab9028e-35e9-4da2-8240-3369efe32899",
  "sourceToolAssistantUUID": "f33d75dd-fadd-42e2-8864-c74456393016",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T23:33:34.715Z_

<details><summary>↩ Tool result · `toolu_01BHasEzNxdp1vwfx4pYN8qB`</summary>

```text
# Analysis of OMP Tokenizer Transplantation Paper

## 1) Downstream Benchmarks Used

The paper evaluates on the following benchmarks:

- **Language Understanding**: MMLU, ARC Challenge, XNLI, AGIEval, Lambada (EN)
- **Mathematical Reasoning**: GSM8K
- **Cross-lingual**: Belebele, Paws-X
- **Perplexity**: WikiText

As stated: "We evaluate perplexity on WikiText, plus classification or QA accuracy on MMLU, ARC, GSM8K, LAMBADA, XNLI, and Paws-X."

## 2) Models and Scales Tested

Two primary experiments:
- **Llama→Mistral NeMo**: 12B parameter transplantation (~128k to ~131k vocabulary, 54% overlap)
- **Qwen→Llama**: 1B parameter transplantation (~152k to ~128k vocabulary, 86% overlap)
- **Additional validation**: Mistral NeMo→Qwen (7B) for testing numeric tokenization hypothesis

## 3) Specific Numerical Results

**Llama→Mistral NeMo (Table 2)**:
- MMLU: 62.2% (baseline 64.5%, -3.6%)
- ARC-C: 52.7% (baseline 58.1%, -9.25%)
- GSM8K: 14.6% (baseline 55.9%, -73.81%)

**Qwen→Llama (Table 3)**:
- MMLU: 36.4% (baseline 36.7%, -0.89%)
- ARC-C: 36.26% (baseline 36.26%, 0%)
- GSM8K: 1.44% (baseline 6.75%, -78.65%)

**Mistral NeMo→Qwen (Table 4)**:
- GSM8K: 78.0% (baseline 82.6%, -5.6%)

## 4) Does It Preserve Reasoning?

**No, significantly degraded**. The paper states: "all zero-shot transplants dramatically degrade mathematical tasks." GSM8K performance drops 73-78% in mismatched numeric schemes. The authors identify this as stemming from "fundamental differences in numerical tokenization schemes" between models.

## 5) OMP vs. Competing Methods

Comparative performance on Qwen→Llama (Table 3):

| Method | MMLU | WikiText |
|--------|------|----------|
| OMP-K64 | 36.40% | 0.7159 |
| FOCUS | 26.95% | 0.8870 |
| WECHSEL | 23.14% | 3.1852 |
| ZeTT | 26.34% | 1.1426 |

OMP substantially outperforms all baselines. For instance, "OMP achieves best zero-shot preservation of the base model's performance across multiple benchmarks, while other zero-shot approaches degrade significantly."

## 6) Completely Frozen Weights Testing

**Yes, confirmed training-free**. The approach is explicitly "training-free" with zero gradient updates. Section 4.5 explores continued pre-training as optional enhancement but confirms the core method requires no retraining: "our approach does not require additional training." The base experiments use strictly "frozen model weights," establishing that transplantation operates entirely at the embedding initialization level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d24b1dd6-0c02-43ee-832a-10d3007b3886",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "93de19ce-a100-4680-8997-8a008051ae7d",
  "sourceToolAssistantUUID": "d24b1dd6-0c02-43ee-832a-10d3007b3886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-19T23:33:37.636Z_

Let me fetch this important survey paper and do a final round of targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93de19ce-a100-4680-8997-8a008051ae7d",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoUaGPQfKvu9X5kgyy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd2a56c-afa4-48cd-86e4-d8b6bad7f9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8pFuUatND3aUdSk3JMEZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1945,
      "cache_creation_input_tokens": 2211,
      "cache_read_input_tokens": 29265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2211,
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

_source line 72 · 2026-05-19T23:33:41.856Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KcRNPUeyif5hvNUb8cfVnf`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.13260v2",
  "prompt": "Extract details about: 1) What does this paper say about post-hoc vocabulary modifications? 2) What does it say about tokenizer changes affecting downstream reasoning? 3) Does it reference Churchill & Skiena? 4) What are their recommendations for vocabulary expansion? 5) What evidence do they cite about tokenizer changes helping or hurting reasoning benchmarks? 6) Any discussion of scale (does tokenizer impact differ at 1B vs 70B+ scales)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd2a56c-afa4-48cd-86e4-d8b6bad7f9f1",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoUaGPQfKvu9X5kgyy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "715542c0-1fb6-4387-943f-71e198acd0f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8pFuUatND3aUdSk3JMEZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1945,
      "cache_creation_input_tokens": 2211,
      "cache_read_input_tokens": 29265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2211,
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

_source line 73 · 2026-05-19T23:33:43.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PW5PJimAct7YsNbesqMq15`</summary>

```json
{
  "query": "vocabulary expansion continued pretraining 70B LLaMA multilingual MMLU MGSM results Korean Japanese Chinese 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "715542c0-1fb6-4387-943f-71e198acd0f7",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoUaGPQfKvu9X5kgyy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5ff8580-81ed-41cd-b764-51f5e1eb42ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8pFuUatND3aUdSk3JMEZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1945,
      "cache_creation_input_tokens": 2211,
      "cache_read_input_tokens": 29265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2211,
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

_source line 74 · 2026-05-19T23:33:43.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DppHoJYZ4xWMXocXQiafS4`</summary>

```json
{
  "query": "\"An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models\" downstream benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ff8580-81ed-41cd-b764-51f5e1eb42ef",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoUaGPQfKvu9X5kgyy8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f69b484b-67bb-4c4a-8649-a5479c346e16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8pFuUatND3aUdSk3JMEZH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1945,
      "cache_creation_input_tokens": 2211,
      "cache_read_input_tokens": 29265,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2211
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1945,
          "output_tokens": 326,
          "cache_read_input_tokens": 29265,
          "cache_creation_input_tokens": 2211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2211,
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

_source line 75 · 2026-05-19T23:33:47.414Z_

<details><summary>↩ Tool result · `toolu_01KcRNPUeyif5hvNUb8cfVnf`</summary>

```text
# Analysis of Paper: "Stop Taking Tokenizers for Granted"

## 1) Post-hoc Vocabulary Modifications

The paper discusses vocabulary expansion as a practical adaptation strategy. It notes that "targeted additions (e.g., 5–10K tokens) yield better returns than aggressive scaling" when extending existing tokenizers. However, the authors emphasize that such modifications require systematic evaluation and initialization strategies rather than ad hoc approaches.

## 2) Tokenizer Changes Affecting Downstream Reasoning

The paper mentions that poor tokenization undermines "model performance on compositional tasks such as code generation, multi-step reasoning, and multi-hop question answering." However, it does not provide detailed empirical evidence quantifying how specific tokenizer modifications affect reasoning capabilities.

## 3) Churchill & Skiena Reference

No, this paper does not reference Churchill & Skiena.

## 4) Vocabulary Expansion Recommendations

The authors recommend:
- Targeted, corpus-aligned expansions rather than uniform scaling
- Careful embedding initialization (subtoken averaging, external vectors)
- Embedding warm-up training before full model unfreezing
- Verification against linguistic fidelity and task alignment metrics before deployment

## 5) Evidence on Reasoning Benchmarks

The paper identifies reasoning as vulnerable to tokenization issues but does **not cite specific benchmark results** showing how tokenizer changes help or hurt reasoning performance. This remains an acknowledged gap in evaluation practices.

## 6) Scale Considerations

The paper does **not discuss** whether tokenizer impact varies across model scales (1B vs. 70B+). This dimension of analysis is absent from their treatment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "715542c0-1fb6-4387-943f-71e198acd0f7",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "2cd7bdae-2ccc-4e88-b163-4f2077e6cc51",
  "sourceToolAssistantUUID": "715542c0-1fb6-4387-943f-71e198acd0f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T23:33:49.416Z_

<details><summary>↩ Tool result · `toolu_01DppHoJYZ4xWMXocXQiafS4`</summary>

```text
Web search results for query: ""An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models" downstream benchmark"

Links: [{"title":"An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models","url":"https://arxiv.org/html/2407.05841v1"},{"title":"An Empirical Comparison of Vocabulary Expansion and Initialization   Approaches for Language Models","url":"https://arxiv.org/pdf/2407.05841"},{"title":"[2407.05841] An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models","url":"https://arxiv.org/abs/2407.05841"},{"title":"HyperOfa: Expanding LLM Vocabulary to New Languages via Hypernetwork-Based Embedding Initialization","url":"https://arxiv.org/html/2504.21018v2"},{"title":"An Empirical Comparison of Vocabulary Expansion and Initialization Approaches For Language Models - ACL Anthology","url":"https://aclanthology.org/2024.conll-1.8/"},{"title":"An Empirical Comparison of Vocabulary Expansion and ...","url":"https://aclanthology.org/2024.conll-1.8.pdf"},{"title":"An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2407.05841v1"}]

Based on the search results, I found the paper you're looking for. Here's information about the downstream benchmarks used in this research:

## Study Overview

The study evaluates different initialization methods for expanding RoBERTa and LLaMA 2 across four languages and five tasks.

## Downstream Tasks/Benchmarks

The paper evaluates performance on several downstream tasks:

**For RoBERTa:** The expanded RoBERTa model was evaluated across three downstream tasks: XNLI, NER, and QA.

**For LLaMA 2:** The paper evaluates 5 checkpoints from one epoch of continued pre-training (plus the initial checkpoint) on 4 downstream tasks. These tasks include MT (Machine Translation), QA (Question Answering), and XLSUM (cross-lingual summarization).

## Key Findings

The paper proposes Constrained Word2Vec (CW2V), a novel approach which does not require cross-lingual embeddings and initializes embeddings within the convex hull of existing embeddings. The results show that CW2V performs equally well or even better than more advanced techniques.

The paper was published at CoNLL 2024 and is available through the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f69b484b-67bb-4c4a-8649-a5479c346e16",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "4f71a4af-8df7-424c-aae0-a6af715d8084",
  "sourceToolAssistantUUID": "f69b484b-67bb-4c4a-8649-a5479c346e16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-19T23:33:50.566Z_

<details><summary>↩ Tool result · `toolu_01PW5PJimAct7YsNbesqMq15`</summary>

```text
Web search results for query: "vocabulary expansion continued pretraining 70B LLaMA multilingual MMLU MGSM results Korean Japanese Chinese 2024 2025"

Links: [{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/pdf/2509.11414"},{"title":"Effective vocabulary expanding of multilingual language models for extremely low-resource languages","url":"https://arxiv.org/pdf/2602.09388"},{"title":"Efficient and Effective Vocabulary Expansion Towards Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2402.14714"},{"title":"An Empirical Comparison of Vocabulary Expansion and Initialization   Approaches for Language Models","url":"https://arxiv.org/pdf/2407.05841"},{"title":"Enhancing LLM Language Adaption through Cross-lingual ...","url":"https://aclanthology.org/2025.emnlp-main.1380.pdf"},{"title":"How Vocabulary Sharing Facilitates Multilingualism in LLaMA?","url":"https://arxiv.org/pdf/2311.09071"},{"title":"Llama 3 Swallow – Swallow LLM","url":"https://swallow-llm.github.io/llama3-swallow.en.html"}]

Based on the web search results, I found several relevant papers and projects related to vocabulary expansion and continued pretraining of multilingual LLMs:

## Key Research and Projects

**Vocabulary Expansion for Multilingual LLMs:**

EEVE is a novel approach for efficient and effective vocabulary expansion that can better train the embeddings of newly added tokens. The EEVE-Korean-10.8B-v1.0 model ranks as the leading Korean pre-trained model in the open-source community as of January 2024.

Vocabulary expansion introduces frequently used yet long words as additional tokens, but is challenging because new embeddings require trillions of training tokens.

**Continued Pretraining Approaches:**

Practitioners typically adopt an incremental continued pretraining (CPT) strategy to incorporate new languages. However, it often results in catastrophic forgetting of previously supported languages. The most common solution to avoid forgetting is experience replay—reintroducing data in previously supported languages during CPT.

**Llama 3 Swallow (Japanese Adaptation):**

Swallow used continual pre-training to improve Japanese language proficiency of Meta Llama 3 8B and 70B, which improves performance on tasks related to knowledge. There is also a slight improvement in performance for mathematics (MGSM) and machine translation (WMT20).

The search results contain various studies on multilingual LLM expansion, though specific 70B LLaMA results across Korean, Japanese, and Chinese with detailed MMLU/MGSM scores from 2024-2025 were not fully detailed in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5ff8580-81ed-41cd-b764-51f5e1eb42ef",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "079098c4-730c-40f0-93f6-31461e2608b5",
  "sourceToolAssistantUUID": "f5ff8580-81ed-41cd-b764-51f5e1eb42ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-19T23:33:53.665Z_

Let me get the Llama 3 Swallow results (which are at 70B scale with vocabulary expansion) and the empirical comparison paper's details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "079098c4-730c-40f0-93f6-31461e2608b5",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoVk4XHFhPja6VjNB4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b214cb7a-8c37-4234-8301-3092a2bb7588",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkyaPa6WRTawRYMXLekELz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 686,
      "cache_creation_input_tokens": 3389,
      "cache_read_input_tokens": 31476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3389,
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

_source line 79 · 2026-05-19T23:33:57.497Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UMGjkH8eC8LBtwGEgPyDS9`</summary>

```json
{
  "url": "https://swallow-llm.github.io/llama3-swallow.en.html",
  "prompt": "Extract ALL details about: 1) What vocabulary expansion was done for LLaMA 3? 2) What scale models were tested (8B, 70B)? 3) What were the specific MGSM results? 4) What were the MMLU results? 5) Did vocabulary expansion help or hurt reasoning? 6) How much continued pretraining was needed? 7) Any other downstream benchmark results? Give me all specific numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b214cb7a-8c37-4234-8301-3092a2bb7588",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoVk4XHFhPja6VjNB4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "523b3700-a9c9-40f2-8a72-0a0f89ff5c29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkyaPa6WRTawRYMXLekELz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 686,
      "cache_creation_input_tokens": 3389,
      "cache_read_input_tokens": 31476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3389,
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

_source line 80 · 2026-05-19T23:33:59.381Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SenkXbwFiBCLRW4qg99kcz`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.05841v1",
  "prompt": "Extract ALL details about: 1) What vocabulary expansion methods were compared? 2) What models and scales? 3) What downstream benchmarks? 4) Specific results on reasoning tasks? 5) What initialization approaches work best? 6) Does vocabulary expansion hurt reasoning? 7) Key conclusions about best practices?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "523b3700-a9c9-40f2-8a72-0a0f89ff5c29",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoVk4XHFhPja6VjNB4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9699239c-4bb6-43a3-87e0-e93d200132d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkyaPa6WRTawRYMXLekELz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 686,
      "cache_creation_input_tokens": 3389,
      "cache_read_input_tokens": 31476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3389,
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

_source line 81 · 2026-05-19T23:33:59.823Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017bqo3sVfaiEmGzeUzLMCFt`</summary>

```json
{
  "query": "vocabulary expansion WITHOUT continued pretraining zero-shot frozen weights downstream task performance degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9699239c-4bb6-43a3-87e0-e93d200132d4",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoVk4XHFhPja6VjNB4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2071b26-3e55-4177-9889-03483d60ce4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkyaPa6WRTawRYMXLekELz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 686,
      "cache_creation_input_tokens": 3389,
      "cache_read_input_tokens": 31476,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3389
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 686,
          "output_tokens": 411,
          "cache_read_input_tokens": 31476,
          "cache_creation_input_tokens": 3389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3389,
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

_source line 82 · 2026-05-19T23:34:03.267Z_

<details><summary>↩ Tool result · `toolu_01UMGjkH8eC8LBtwGEgPyDS9`</summary>

```text
# Llama 3 Swallow Details

## 1) Vocabulary Expansion for Llama 3
**None was performed.** The document explicitly states: "the Llama 3 Swallow series does not perform vocabulary expansion." While a preliminary experiment added 48,000 Japanese subwords, they "decided not to expand the vocabulary" because the effect was limited (20% sequence length reduction vs. 42% for Llama 2).

## 2) Scale Models Tested
Both 8B and 70B models were developed, with versions for:
- Base models (pre-training only)
- Instruct models (instruction-tuned)

## 3) MGSM Results
No specific numerical scores provided. The text only notes that continual pre-training showed "slight improvement in performance for mathematics (MGSM)" and that "Qwen2 7B outperforms Llama 3 Swallow 8B in...mathematics (MGSM and GSM8K)."

## 4) MMLU Results
No specific scores reported. Only mentioned that Qwen2 7B outperformed in "examinations (JMMLU and MMLU)."

## 5) Vocabulary Expansion and Reasoning
Not applicable—no expansion was done for Llama 3. However, the analysis showed vocabulary expansion's "disadvantages such as task performance degradation."

## 6) Continued Pre-training Duration
No specific duration/step counts disclosed in this document.

## 7) Other Benchmark Results
Performance metrics were evaluated on multiple tasks (Japanese MT-Bench, JHumanEval, HumanEval, WMT20, NIILC), but exact numerical results aren't provided in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "523b3700-a9c9-40f2-8a72-0a0f89ff5c29",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "05cd7829-9054-42b7-a2f0-807921367b79",
  "sourceToolAssistantUUID": "523b3700-a9c9-40f2-8a72-0a0f89ff5c29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-19T23:34:05.693Z_

<details><summary>↩ Tool result · `toolu_017bqo3sVfaiEmGzeUzLMCFt`</summary>

```text
Web search results for query: "vocabulary expansion WITHOUT continued pretraining zero-shot frozen weights downstream task performance degradation"

Links: [{"title":"(PDF) Zero-Shot Video Question Answering via Frozen Bidirectional Language Models","url":"https://www.researchgate.net/publication/361359119_Zero-Shot_Video_Question_Answering_via_Frozen_Bidirectional_Language_Models"},{"title":"CoLeCLIP: Open-Domain Continual Learning via Joint Task Prompt and Vocabulary Learning","url":"https://arxiv.org/html/2403.10245"},{"title":"Decoupled Vocabulary Learning Enables Zero-Shot Translation from Unseen Languages","url":"https://arxiv.org/html/2408.02290v1"},{"title":"Patching open-vocabulary models by interpolating weights Gabriel Ilharco∗1","url":"https://openreview.net/pdf?id=CZZFRxbOLC"},{"title":"A Simple Framework for Open-Vocabulary Zero-Shot Segmentation","url":"https://arxiv.org/html/2406.16085v3"},{"title":"(PDF) A Simple Framework for Open-Vocabulary Zero-Shot Segmentation","url":"https://www.researchgate.net/publication/381666840_A_Simple_Framework_for_Open-Vocabulary_Zero-Shot_Segmentation"}]

The search returned several relevant results related to zero-shot learning, frozen weights, and vocabulary in downstream tasks. Here are the key findings:

It is possible to expand the set of tasks on which models achieve high accuracy without introducing new parameters, without re-training them from scratch, and without catastrophic forgetting.

To alleviate the forgetting of zero-shot knowledge, class vocabulary learning incorporates Parameter-Efficient Fine-Tuning (PEFT) modules into the frozen text encoder rather than fully fine-tuning the entire model.

By decoupling the image representation learning process from the vision-language alignment process, this methodology enhances both computational and data efficiency while improving performance in zero-shot classification tasks.

One approach showed that given enough modeling capacity one can add new languages without loss in quality on existing ones, though they only considered new languages sufficiently represented in the base model vocabulary and left the original vocabulary unmodified.

These findings suggest that vocabulary expansion and downstream task performance can be maintained with careful approaches that preserve frozen weights and use efficient fine-tuning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2071b26-3e55-4177-9889-03483d60ce4f",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "22895b71-81c5-44e9-bb17-a0303b853043",
  "sourceToolAssistantUUID": "d2071b26-3e55-4177-9889-03483d60ce4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T23:34:08.833Z_

<details><summary>↩ Tool result · `toolu_01SenkXbwFiBCLRW4qg99kcz`</summary>

```text
# Vocabulary Expansion and Initialization: Research Summary

## 1) Vocabulary Expansion Methods Compared

The study evaluated **six initialization approaches**:
- **Constrained Word2Vec (CW2V)** - the novel proposed method
- **OFA** (One For All Framework)
- **Multivariate** - samples from multivariate Gaussian distribution
- **Univariate** - draws from 1-D Gaussian distributions per dimension
- **Mean** - averages pre-expansion embeddings
- **Random** - standard Gaussian sampling

## 2) Models and Scales

Two architectures were tested:
- **RoBERTa** (125M parameters, encoder-based)
- **LLaMA2-7B** (7 billion parameters, decoder-based)

## 3) Downstream Benchmarks

**For RoBERTa:**
- XNLI (sentence classification)
- NER (token classification)
- QA (question answering)

**For LLaMA2:**
- XNLI
- Machine Translation (FLORES)
- QA
- XLSUM (summarization)

Evaluation covered **four target languages**: German, Russian, Hindi, Tamil

## 4) Results on Reasoning Tasks

The paper does not specifically address reasoning tasks. XNLI is a natural language inference task, but the results showed "all models perform almost equally poorly," suggesting "neither vocabulary expansion nor CPT is sufficient" for improvement.

## 5) Best-Performing Initialization Approaches

**Key finding:** Simpler methods matched sophisticated ones. Results showed "simpler approaches like multivariate initialization perform on par with these advanced methods."

**Performance hierarchy:**
- Without continued pretraining (CPT): CW2V excelled, especially for LLaMA2
- With CPT: "CW2V quickly converges with OFA" and even simpler baselines catch up within a few checkpoints
- Mean and Multivariate achieved "comparable performance to OFA and CW2V shortly thereafter"

## 6) Does Vocabulary Expansion Hurt Reasoning?

The paper reveals a **critical concern**: during CPT, "an initial drop in English performance" occurred. However, "performance drops, after which it begins to improve with prolonged training." This suggests temporary disruption rather than permanent harm, though the study provides limited reasoning task analysis.

## 7) Key Conclusions About Best Practices

**Theoretical foundation:** The authors established that initializing embeddings "within the convex hull of existing embeddings is a good initialization," preserving pre-expansion model behavior.

**Primary conclusion:** "Efficient large-scale multilingual continued pretraining can be achieved even with simpler initialization methods" provided they satisfy the convex hull constraint.

**Practical takeaway:** Organizations need not invest in complex methods like OFA when mean or multivariate initialization suffices, significantly reducing computational overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9699239c-4bb6-43a3-87e0-e93d200132d4",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "6df46249-97ba-4248-9ddc-0fdb4e2fe5fd",
  "sourceToolAssistantUUID": "9699239c-4bb6-43a3-87e0-e93d200132d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-19T23:34:12.476Z_

Let me do a final round of critical searches to complete the picture -- specifically on whether anyone has tested post-hoc vocabulary additions (without any continued pretraining) on large-scale model reasoning tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6df46249-97ba-4248-9ddc-0fdb4e2fe5fd",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoX6AXdry9xKCVsyLtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "511fbf84-f2c0-4c60-80c0-089cabb55f43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLCNwiv9vqvhp6KPW7wVi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 605,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 34865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2206,
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

_source line 86 · 2026-05-19T23:34:13.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DwovnSYc4zNcaHx25AE6PK`</summary>

```json
{
  "query": "\"vocabulary expansion\" OR \"tokenizer modification\" zero-shot NO retraining reasoning degradation GSM8K math benchmark LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "511fbf84-f2c0-4c60-80c0-089cabb55f43",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoX6AXdry9xKCVsyLtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4582fbcc-7576-4acf-b7bf-4a28719d4ccd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLCNwiv9vqvhp6KPW7wVi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 605,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 34865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2206,
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

_source line 87 · 2026-05-19T23:34:14.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rm84LvJfkDh49v9A2yLAxc`</summary>

```json
{
  "query": "token healing guidance library LLM tokenizer boundary prompt completion 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4582fbcc-7576-4acf-b7bf-4a28719d4ccd",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoX6AXdry9xKCVsyLtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4b7d15c-77d7-44f9-b6e5-48938f349b38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLCNwiv9vqvhp6KPW7wVi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 605,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 34865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2206,
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

_source line 88 · 2026-05-19T23:34:15.560Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wp4NDauYxikbzGEbz2h3pb`</summary>

```json
{
  "url": "https://guidance.readthedocs.io/en/latest/example_notebooks/tutorials/token_healing.html",
  "prompt": "Extract ALL details about: 1) What is token healing exactly? 2) How does it work? 3) What problems does it solve? 4) Is this related to vocabulary expansion? 5) Does it affect model reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4b7d15c-77d7-44f9-b6e5-48938f349b38",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoX6AXdry9xKCVsyLtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c41bf2e2-b37c-4b06-8023-b00e3b113fc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPLCNwiv9vqvhp6KPW7wVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 605,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 34865,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2206
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 605,
          "output_tokens": 302,
          "cache_read_input_tokens": 34865,
          "cache_creation_input_tokens": 2206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2206,
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

_source line 89 · 2026-05-19T23:34:20.432Z_

<details><summary>↩ Tool result · `toolu_01Wp4NDauYxikbzGEbz2h3pb`</summary>

```text
# Token Healing: Key Details

## 1) What is Token Healing?

Token healing is a technique that corrects tokenization misalignments occurring at prompt-completion boundaries. The process "backs up the generation process by one or more tokens before the end of the prompt, then constrains the first tokens generated to have a prefix that matches the last token in the prompt."

## 2) How Does It Work?

Rather than allowing tokenization to break naturally at the prompt boundary, guidance retroactively adjusts encoding by:
- Stepping back in the generation sequence
- Forcing initial generated tokens to share prefixes with the final prompt token
- Ensuring the resulting text uses the joint tokenization the model learned during training

The example demonstrates this: "This is a " followed by "fine day." produces suboptimal tokens when split at the boundary, but optimal tokens when considered as a unified string.

## 3) What Problems Does It Solve?

Token healing addresses tokenization artifacts from misaligned boundaries. Without it, models receive unusual token sequences that don't match training data patterns. This causes generation quality issues—the documentation shows GPT2 generating "http: //" (with space) instead of "http://" because the boundary forces poor token selection.

## 4) Related to Vocabulary Expansion?

No connection is mentioned. Token healing operates within existing tokenization schemes without expanding vocabularies.

## 5) Does It Affect Model Reasoning?

The documentation suggests it improves alignment with training data but doesn't explicitly address reasoning capabilities. It primarily concerns output quality through proper tokenization alignment, not cognitive processes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c41bf2e2-b37c-4b06-8023-b00e3b113fc8",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "92881578-fc38-4cf1-9560-7e580364c666",
  "sourceToolAssistantUUID": "c41bf2e2-b37c-4b06-8023-b00e3b113fc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-19T23:34:20.914Z_

<details><summary>↩ Tool result · `toolu_01Rm84LvJfkDh49v9A2yLAxc`</summary>

```text
Web search results for query: "token healing guidance library LLM tokenizer boundary prompt completion 2024 2025"

Links: [{"title":"Token healing — Guidance latest documentation","url":"https://guidance.readthedocs.io/en/latest/example_notebooks/tutorials/token_healing.html"},{"title":"guidance/notebooks/tutorials/token_healing.ipynb at main · guidance-ai/guidance","url":"https://github.com/guidance-ai/guidance/blob/main/notebooks/tutorials/token_healing.ipynb"},{"title":"Prompt Boundaries and Token Healing — Guidance latest documentation","url":"https://guidance.readthedocs.io/en/latest/example_notebooks/art_of_prompt_design/prompt_boundaries_and_token_healing.html"},{"title":"Token healing (under 40 LOC) · Issue #4778 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/4778"},{"title":"guidance/notebooks/art_of_prompt_design/prompt_boundaries_and_token_healing.ipynb at main · guidance-ai/guidance","url":"https://github.com/guidance-ai/guidance/blob/main/notebooks/art_of_prompt_design/prompt_boundaries_and_token_healing.ipynb"},{"title":"The Art of Prompt Design: Prompt Boundaries and Token Healing | by Scott Lundberg | TDS Archive | Medium","url":"https://medium.com/data-science/the-art-of-prompt-design-prompt-boundaries-and-token-healing-3b2448b0be38"},{"title":"Getting the most out of your tokenizer for pre-training and domain adaptation","url":"https://arxiv.org/html/2402.01035v1"},{"title":"Token healing (under 40 LOC) · Issue #28346 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/28346"}]

Based on the search results, here's what I found about token healing in LLM guidance libraries:

## Overview of Token Healing

Token healing rectifies the token boundary bias in greedy tokenization by trimming and regrowing the prompt to better align with the model's tokenizer, thus enhancing generation quality.

## The Problem It Solves

Token boundaries often don't line up with the end of the prompt if we consider the generated tokens that will also come next. While the end of a prompt will always align with a token boundary in practice, as the prompt is tokenized before being extended by the model, there may be instances where the first characters of the completion are part of a longer token that would span the prompt boundary. The inability to use tokens that span prompt boundaries can lead to subtle yet important biases in the model's output.

A concrete example: Given a completion prompt with a partial url ending with :, the model might have seen the expected completion :// as a single token in training. However, the prompt's tail token : tells it that the next token is not //, and so it generates a wrong completion.

## Implementation

Token healing requires direct endpoint integration to run efficiently, so it is currently supported only for the guidance.models.LlamaCpp and guidance.models.Transformers LLM backends. The Guidance library (guidance-ai) provides documentation and examples of token healing functionality.

Token healing is a technique used to address biases introduced by tokenization at prompt boundaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4b7d15c-77d7-44f9-b6e5-48938f349b38",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "d20c675a-cf22-40db-9280-4b90c3f0ec34",
  "sourceToolAssistantUUID": "d4b7d15c-77d7-44f9-b6e5-48938f349b38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-19T23:34:21.051Z_

<details><summary>↩ Tool result · `toolu_01DwovnSYc4zNcaHx25AE6PK`</summary>

```text
Web search results for query: ""vocabulary expansion" OR "tokenizer modification" zero-shot NO retraining reasoning degradation GSM8K math benchmark LLM"

Links: [{"title":"Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching","url":"https://openreview.net/pdf?id=DxKP2E0xK2"},{"title":"An Adaptive Method for Vocabulary Expansion of Domain- ...","url":"https://aclanthology.org/2024.emnlp-main.424.pdf"},{"title":"Masked Thought: Simply Masking Partial Reasoning Steps Can Improve   Mathematical Reasoning Learning of Language Models","url":"https://arxiv.org/pdf/2403.02178"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/html/2601.14658v1"},{"title":"GitHub - JIA-Lab-research/MR-GSM8K: Challenge LLMs to Reason About Reasoning: A Benchmark to Unveil Cognitive Depth in LLMs · GitHub","url":"https://github.com/JIA-Lab-research/MR-GSM8K"},{"title":"Efficient Vocabulary Reduction for Small Language Models","url":"https://aclanthology.org/2025.coling-industry.64.pdf"},{"title":"Achieving Tokenizer Flexibility in Language Models through Heuristic","url":"https://arxiv.org/pdf/2505.09738"},{"title":"Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models","url":"https://arxiv.org/html/2512.03989v2"}]

I found several relevant research papers addressing your query about vocabulary expansion, tokenizer modification, zero-shot performance, and reasoning degradation on the GSM8K math benchmark for LLMs.

## Key Findings:

**Performance Degradation with Tokenizer Modification:**

Simply swapping token IDs or altering merge rules without re-optimization typically disrupts the learned mapping between subword units and semantics, leading to broad performance degradation. In practice, rectifying tokenizer deficiencies would require modifying tokenization rules and vocabulary, followed by re-training model so it can internalize the revised token-ID mappings.

**Vocabulary Changes and GSM8K Performance:**

Tasks such as GSM8K, which require precise linguistic or logical structures, exhibited more performance degradation when vocabulary was modified. Additionally, when vocabulary size constantly increases, the vanilla tokenization could be broken, with more unseen tokens appearing within one instance.

**Zero-Shot Tokenizer Transfer:**

Recent work addresses zero-shot tokenizer transfer approaches. Zero-shot perplexity evaluations reveal advantages for the TokenAdapt initialization method, which consistently yielded the lowest overall perplexity ratios, indicating significantly better preservation of the original model's capabilities immediately following the tokenizer swap.

**Vocabulary Expansion Methods:**

Methods for controlled vocabulary modification of pre-trained language models have been developed through improved tokenizer extension and pruning.

These findings indicate that tokenizer modification without retraining leads to reasoning degradation, particularly on tasks requiring precise logic like GSM8K.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4582fbcc-7576-4acf-b7bf-4a28719d4ccd",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a750ba1644a9199d8",
  "type": "user",
  "uuid": "71421244-09e0-469d-adac-1f772fab486c",
  "sourceToolAssistantUUID": "4582fbcc-7576-4acf-b7bf-4a28719d4ccd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 92 · 2026-05-19T23:35:56.151Z_

Now I have a comprehensive picture. Let me compile the final research report.

---

## Research Report: Post-Hoc Vocabulary Additions to LLM Tokenizers and Effects on Downstream Reasoning

### 1. Churchill & Skiena (2026) -- What They Did and What Was Validated

**Paper**: "Reducing Tokenization Premiums for Low-Resource Languages" ([arXiv:2601.13328](https://arxiv.org/abs/2601.13328))

**Method**: They added missing Unicode characters as individual tokens to a frozen model's vocabulary. For each new character, they: (a) tokenized it with the original tokenizer (yielding multiple tokens), (b) ran the multi-token embeddings through the model to a specified layer, (c) averaged the resulting hidden states, and (d) used prediction methods (linear regression at layer 0 performed best) to derive a single embedding that would produce a similar hidden state.

**What was validated**: Exclusively **cosine similarity of averaged last hidden states at layer 16** of **LLaMA 3.2 1B** (1 billion parameters). They tested 12 low-resource languages with predominantly non-Latin scripts: Amharic, Bangla, Hebrew, Hindi, Armenian, Shan, Tamil, Telugu, Urdu, Vietnamese, Yiddish, and Traditional Chinese.

**Specific numbers**: Similarity ranged widely -- Traditional Chinese achieved ~0.92-0.98 cosine similarity, while Amharic at layer 0 was as low as ~0.05-0.36. Shan (worst-tokenized language) achieved ~0.68-0.72.

**What was NOT validated**: 
- No downstream task evaluation whatsoever -- no MGSM, MMLU, GSM8K, or any other benchmark
- No testing at scales beyond 1B parameters
- No evaluation of generation quality or text output

**Limitations the authors themselves acknowledge**:
- Cosine similarity scores are "meaningless in isolation"
- "Cosine similarity is not necessarily aligned with performance on real downstream tasks"
- Averaging hidden states is "a fairly aggressive operation"
- They flag a "vote-splitting problem" where augmenting (rather than replacing) vocabulary could cause probability mass splitting between original sub-tokens and new combined tokens, potentially degrading performance

**The reviewer's critique is entirely valid**: This has ONLY been validated via hidden state similarity on a 1B model. There is zero evidence it works on downstream reasoning at any scale, let alone 235B-scale models.

---

### 2. Other Work on Modifying Tokenizer Vocabularies Post-Training

Several approaches exist along a spectrum from fully training-free to requiring light continued pretraining:

**Fully Training-Free Methods (Zero Gradient Updates)**:

- **OMP (Orthogonal Matching Pursuit)** ([arXiv:2506.06607](https://arxiv.org/abs/2506.06607)): Reconstructs new token embeddings as sparse linear combinations of existing embeddings. Tested on LLaMA 3.2-1B, Qwen2.5-7B, and Mistral-Nemo. On MMLU, it preserves ~96% of baseline performance (62.2% vs 64.5% on LLaMA-to-Mistral NeMo). But **GSM8K drops catastrophically**: from 55.9% to 14.6% on LLaMA-to-Mistral NeMo (73.8% degradation), and from 6.75% to 1.44% on Qwen-to-LLaMA (78.6% degradation). The authors attribute this to "fundamental differences in numerical tokenization schemes."

- **FOCUS** ([arXiv:2305.14481](https://arxiv.org/abs/2305.14481)): Uses fastText to weight combinations of existing embeddings. Performs worse than OMP across benchmarks (26.95% vs 36.40% MMLU on Qwen-to-LLaMA).

- **WECHSEL**: Uses static multilingual embeddings to identify similar source tokens. Also inferior to OMP (23.14% MMLU on Qwen-to-LLaMA).

- **TokenAdapt** ([arXiv:2505.09738](https://arxiv.org/abs/2505.09738)): Hybrid local+global heuristic initialization. Tested only on 3B models. Evaluated only on perplexity, no downstream reasoning benchmarks at all.

**Methods Requiring Light Continued Pretraining**:

- **EEVE** ([arXiv:2402.14714](https://arxiv.org/abs/2402.14714)): Added 8,960 Korean tokens to SOLAR-10.7B with multi-stage progressive unfreezing over 2B tokens. Evaluated on BoolQ, COPA, HellaSwag, WiC, SentiNeg. **No reasoning benchmarks (MGSM, GSM8K, MMLU) were tested**.

- **Vocabulary Expansion of Chat Models** ([arXiv:2412.11704](https://arxiv.org/abs/2412.11704)): Tested on Qwen2.5-7B, LLaMA 3.1-8B, Gemma 2-9B with 500M tokens of continued pretraining. Evaluated on summarization, translation, Belebele, MMLU, BBH, IFEval. Up to 5.7x inference speedup. **No MGSM or math reasoning tested**.

- **TokAlign** ([arXiv:2506.03523](https://arxiv.org/abs/2506.03523)): Uses GloVe-based token alignment + progressive fine-tuning. Tested on Pythia models (1B-6.9B). Recovers 97.6% of base model performance after vocabulary replacement with just 5k steps. **No reasoning-specific benchmarks**.

- **Continued BPE Training** ([arXiv:2512.03989](https://arxiv.org/abs/2512.03989)): "Teaching Old Tokenizers New Words" -- extends tokenizers by continuing BPE merge learning. Accepted at EACL 2026 Findings. No downstream benchmark details available.

- **CW2V (Constrained Word2Vec)** ([arXiv:2407.05841](https://arxiv.org/abs/2407.05841), CoNLL 2024): Compared 6 initialization methods for RoBERTa-125M and LLaMA2-7B. Key finding: simpler initialization methods (mean, multivariate Gaussian) perform comparably to sophisticated ones after continued pretraining. Initializing within the "convex hull of existing embeddings" is the key principle. Tested on XNLI, MT, QA, XLSUM. **No math reasoning benchmarks**.

- **KL-Based Self-Distillation** ([arXiv:2508.15807](https://arxiv.org/abs/2508.15807)): Claims to test on MGSM, MMLU, and GSM8K -- this appears to be the only vocabulary expansion paper to explicitly evaluate math reasoning benchmarks, though detailed numbers were not extractable from the PDF metadata.

- **Kuwain 1.5B** ([arXiv:2504.15120](https://arxiv.org/abs/2504.15120)): Added 26K Arabic tokens to TinyLlama 1.1B. Achieved 8% improvement on Arabic benchmarks, preserved English performance. Trained on 8 A100 GPUs for 3 epochs. **No MGSM, GSM8K, or MMLU tested**.

---

### 3. Has Anyone Shown Vocabulary Additions Help on Downstream Reasoning Benchmarks?

**The short answer is: almost nobody has properly tested this, and the evidence that does exist is concerning.**

- The OMP paper is the most rigorous on this point, and it shows **catastrophic degradation on GSM8K** (73-79% drops) for training-free tokenizer transplantation, even when MMLU is relatively preserved.

- Llama 3 Swallow (Japanese adaptation of LLaMA 3 at both 8B and 70B scale) **decided NOT to expand vocabulary** for LLaMA 3, noting only 20% sequence length reduction vs 42% for LLaMA 2, and explicitly flagging vocabulary expansion's "disadvantages such as task performance degradation." They observed only "slight improvement" on MGSM from continued pretraining without vocabulary changes.

- The "One Tokenizer To Rule Them All" paper ([arXiv:2506.10766](https://arxiv.org/abs/2506.10766), ICLR 2026) tested M-MMLU and Belebele on 3.3B models and showed universal tokenizers outperform cluster-specific ones by up to 20.2% win rate. However, this is about **pretraining with a better tokenizer from the start**, not post-hoc additions.

- No paper was found that demonstrates post-hoc vocabulary additions (without continued pretraining) helping on reasoning benchmarks at any scale, let alone 70B+.

---

### 4. What Happens When You Add Tokens Without Retraining?

The evidence is clear and concerning:

**Mathematical reasoning breaks badly**: OMP shows GSM8K dropping 73-79% with zero-shot tokenizer transplantation. The authors identify "fundamental differences in numerical tokenization schemes" as the root cause -- different models tokenize numbers differently (digit-by-digit vs multi-digit), and transplanting a tokenizer that handles numbers differently destroys math reasoning.

**General knowledge is more resilient**: MMLU drops only 3.6% in the best OMP transplant case (LLaMA-to-Mistral NeMo), suggesting factual recall is less sensitive to tokenization changes than multi-step reasoning.

**"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs"** ([arXiv:2601.14658](https://arxiv.org/abs/2601.14658)) provides a systematic taxonomy of 8 tokenizer-induced reasoning failure modes (whitespace-boundary shifts, intra-word resegmentation, morphological boundary surfacing, etc.). Key finding: **model size does NOT fix tokenizer-induced reasoning failures**. Across Gemma (270M-12B), LLaMA (1B-8B), Mistral (8B-24B), and Qwen (4B-30B), "some larger variants achieve replacement success that is comparable to or even lower than that of smaller counterparts." This is a fundamental architectural constraint.

**The vote-splitting problem** (flagged by Churchill & Skiena themselves): When you add tokens without removing the original sub-token sequences, the model must split probability mass between the original multi-token encoding and the new single-token encoding. This can degrade performance even if the new embedding is well-initialized.

---

### 5. Token Healing and Token Merging

**Token Healing** (from the [Guidance library](https://guidance.readthedocs.io/en/latest/example_notebooks/tutorials/token_healing.html)) is a fundamentally different concept. It addresses prompt-boundary misalignment during inference -- when the tokenization of a prompt doesn't align with what the model expects at token boundaries. For example, ending a prompt with "http:" means the model cannot generate "://" as a single token. Token healing backs up generation by one or more tokens and constrains initial generated tokens to match the prompt's tail. This operates within the existing vocabulary and does not expand it. It primarily affects generation quality at prompt boundaries, not reasoning.

**Token Merging (ToMe)** is also distinct -- it progressively merges redundant token representations during inference (primarily in vision transformers and multimodal models like CLIP, Segment Anything). It reduces computation by fusing semantically similar tokens mid-inference rather than modifying the vocabulary. **MrT5** ([arXiv:2410.20771](https://arxiv.org/abs/2410.20771)) explores dynamic token merging for byte-level language models, but this is an architectural innovation rather than post-hoc vocabulary modification.

Neither token healing nor token merging is directly relevant to the Churchill & Skiena vocabulary expansion approach.

---

### 6. Tokenizer Swapping/Adaptation for Multilingual Models

**"One Tokenizer To Rule Them All"** ([arXiv:2506.10766](https://arxiv.org/abs/2506.10766), ICLR 2026): The strongest evidence that tokenizer design matters, but it argues for **pre-training** with a universal 250K-vocabulary tokenizer covering 62 languages rather than post-hoc modification. Key result: 19% higher win rate on expanded languages, 8x faster adaptation, while primary language performance drops by no more than 2%. Tested at 3.3B scale only. Explicitly shows that Cross-Lingual Vocabulary Adaptation (post-hoc tokenizer replacement) "fails to achieve comparable performance" and "significantly lags behind the Universal tokenizer by 15.4% and 35.2% win rates."

**"Stop Taking Tokenizers for Granted"** ([arXiv:2601.13260](https://arxiv.org/abs/2601.13260), January 2026): A survey/position paper arguing tokenization is a "core modeling decision" rather than a preprocessing step. Recommends targeted corpus-aligned expansions (5-10K tokens), careful embedding initialization within the convex hull, and embedding warm-up before full model unfreezing. Does NOT discuss scale-dependent effects and does NOT reference Churchill & Skiena.

**"How does a Language-Specific Tokenizer affect LLMs?"** ([arXiv:2502.12560](https://arxiv.org/abs/2502.12560)): Found that extended Korean tokenizers "decrease confidence in incorrect predictions" and reduce cross-entropy on complex tasks. But tested only on TinyLlama 1.1B, with no downstream reasoning benchmarks, and the authors acknowledge "the results cannot be directly generalized to larger models."

---

### Summary of the Validation Gap

The reviewer's concern about Churchill & Skiena (2026) is well-founded and reflects a broader gap in the literature:

| What has been validated | What has NOT been validated |
|---|---|
| Hidden state cosine similarity at 1B scale (Churchill & Skiena) | Any downstream task performance for pure post-hoc additions without retraining |
| Perplexity preservation for training-free transplantation (OMP, TokenAdapt) | Reasoning benchmark performance at >10B scale for any vocabulary expansion method |
| MMLU rough preservation with training-free transplant at 7-12B (OMP) | Mathematical reasoning preservation without retraining (GSM8K drops 73-79% in OMP) |
| Vocabulary expansion + continued pretraining helps at 7-10B for translation/NLU tasks | Whether the hidden state similarity metric used by Churchill & Skiena predicts downstream performance at all |
| Universal tokenizers outperform post-hoc adaptation (ICLR 2026) | Post-hoc vocabulary additions at 70B+ or 235B scale |

**The critical finding**: The OMP paper ([arXiv:2506.06607](https://arxiv.org/abs/2506.06607)) is the closest anyone has come to testing training-free tokenizer modification on reasoning, and it shows **catastrophic failure on math reasoning** (GSM8K), even while MMLU is relatively preserved. This strongly suggests that Churchill & Skiena's hidden-state-similarity validation is insufficient evidence that their approach would preserve downstream reasoning capability.

**No paper in the literature has validated post-hoc vocabulary additions on downstream reasoning tasks at 70B+ scale**, let alone 235B. The largest models tested for any vocabulary expansion approach are 10.8B (EEVE) and 3.3B ("One Tokenizer To Rule Them All"), and even these either skip reasoning benchmarks or show that post-hoc approaches lag behind pre-training-integrated solutions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71421244-09e0-469d-adac-1f772fab486c",
  "isSidechain": true,
  "agentId": "a750ba1644a9199d8",
  "requestId": "req_011CbCoXzT1fCRsAbhyGsbXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "527c9f52-61ab-4e1a-9baf-9c467170d4f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LeUBUb1NiJWVvEY1kofqt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1215,
      "cache_creation_input_tokens": 1698,
      "cache_read_input_tokens": 37071,
      "output_tokens": 3810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1215,
          "output_tokens": 3810,
          "cache_read_input_tokens": 37071,
          "cache_creation_input_tokens": 1698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1698,
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
