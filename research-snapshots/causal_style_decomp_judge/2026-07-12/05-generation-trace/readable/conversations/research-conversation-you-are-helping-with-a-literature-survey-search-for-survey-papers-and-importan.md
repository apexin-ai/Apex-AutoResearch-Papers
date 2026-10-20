# Research conversation: You are helping with a literature survey. Search for survey papers and important benchmarks related to visual document r

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 171
- **Recorded user turns:** 1
- **Tool calls:** 78
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0dd57a49da85eaac.jsonl`
- **Structured JSON:** [`c4f2c5c58cb522c37a9a.json`](../../sessions/c4/c4f2c5c58cb522c37a9a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

171 recorded events

### User

_source line 1 · 2026-05-30T06:14:02.182Z_

You are helping with a literature survey. Search for survey papers and important benchmarks related to visual document retrieval, document understanding with VLMs, and multimodal information retrieval.

Execute these searches:

1. Search: "visual document retrieval survey 2025 2026"
2. Search: "document understanding vision language model survey 2025"
3. Search: "multimodal information retrieval survey 2024 2025"
4. Search: "ViDoRe benchmark visual document retrieval 2025 2026"
5. Search: "document retrieval benchmark evaluation 2025 2026"
6. Search: "site:paperswithcode.com visual document retrieval SOTA"
7. Search: "most cited visual document retrieval 2024 2025"

For each paper you find, use WebFetch on its arxiv page to read the abstract. Report back with:
- Full title
- Authors (first author et al.)
- Venue or arXiv date
- URL
- What the paper does (2-3 sentences)
- Why it's important

Exclude these seed papers: ColPali, MMDocIR, Snappy, AGREE, ColParse, MURE, ViDoRe V3, RegionGPT.

Find as many relevant papers as possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "5e91f631-8a14-420d-aa8f-f4cf26e58ed0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:14:02.186Z_

```json
{
  "parentUuid": "5e91f631-8a14-420d-aa8f-f4cf26e58ed0",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
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
      "TaskStop",
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
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "db433711-45df-4c35-bab5-6103750b4481",
  "timestamp": "2026-05-30T06:14:02.186Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:14:02.188Z_

```json
{
  "parentUuid": "db433711-45df-4c35-bab5-6103750b4481",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c6189f83-b124-4d36-9b47-6b5515bd309a",
  "timestamp": "2026-05-30T06:14:02.188Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:14:04.699Z_



I'll start by loading the WebSearch and WebFetch tools, then execute the searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6189f83-b124-4d36-9b47-6b5515bd309a",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG6uBH39X7zQY2nKspJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71906bd7-cbf2-4af9-9540-ca5de5d8f9a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QJmKDQJJpXdX7J7yeUS6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 7413,
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

_source line 5 · 2026-05-30T06:14:05.324Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GiTpt9vQs3CifqbmVB5z9j`</summary>

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
  "parentUuid": "71906bd7-cbf2-4af9-9540-ca5de5d8f9a8",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG6uBH39X7zQY2nKspJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6497d58d-244f-4bea-969e-5a7785098c9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QJmKDQJJpXdX7J7yeUS6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 7413,
      "output_tokens": 102,
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
          "output_tokens": 102,
          "cache_read_input_tokens": 7413,
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

_source line 6 · 2026-05-30T06:14:05.327Z_

<details><summary>↩ Tool result · `toolu_01GiTpt9vQs3CifqbmVB5z9j`</summary>

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
  "parentUuid": "6497d58d-244f-4bea-969e-5a7785098c9e",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "99028545-9cb3-40ef-b699-67fad33ce873",
  "sourceToolAssistantUUID": "6497d58d-244f-4bea-969e-5a7785098c9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:14:07.825Z_



Now let me execute all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99028545-9cb3-40ef-b699-67fad33ce873",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8132c32-b88d-4c1f-970f-ddfe0accf564",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 8 · 2026-05-30T06:14:08.299Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BBMSdFV2FyiaHnapmQeB2F`</summary>

```json
{
  "query": "visual document retrieval survey 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8132c32-b88d-4c1f-970f-ddfe0accf564",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab8adf45-525d-4ed1-be50-291b1819e7b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 9 · 2026-05-30T06:14:08.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPjnFmjTkWkbCucUngJSJ5`</summary>

```json
{
  "query": "document understanding vision language model survey 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab8adf45-525d-4ed1-be50-291b1819e7b4",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2db5f201-f4d4-4ed1-8e9c-2e950adc8189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 10 · 2026-05-30T06:14:09.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LpiD3TfgXF57ZFpg3tyRgU`</summary>

```json
{
  "query": "multimodal information retrieval survey 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2db5f201-f4d4-4ed1-8e9c-2e950adc8189",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2083629-8078-4897-af77-347d642e3b59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 11 · 2026-05-30T06:14:10.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014avJWqBrYavuFUXzrr5DJD`</summary>

```json
{
  "query": "ViDoRe benchmark visual document retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2083629-8078-4897-af77-347d642e3b59",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ec00828-7f37-4e94-ad63-4fd6cf0b7a78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 12 · 2026-05-30T06:14:10.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QKwv97dyqULjD3Vbn7V9QX`</summary>

```json
{
  "query": "document retrieval benchmark evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec00828-7f37-4e94-ad63-4fd6cf0b7a78",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2aad36b-cf56-4771-ba0d-fd187760e203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 13 · 2026-05-30T06:14:11.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P3uqLJ3MzHfRDGwyXur6BM`</summary>

```json
{
  "query": "site:paperswithcode.com visual document retrieval SOTA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2aad36b-cf56-4771-ba0d-fd187760e203",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5ae4b0f-2ada-4ad3-a911-f49d62cbb5a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
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

_source line 14 · 2026-05-30T06:14:11.471Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PAZTrHw3NeGtq4rRYCoETV`</summary>

```json
{
  "query": "most cited visual document retrieval 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ae4b0f-2ada-4ad3-a911-f49d62cbb5a6",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG78q4WesRYaSWj262r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4fde79a-2c5b-4fd1-a537-d75970456c67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCoAvvixYQPkbQ3trgGG2F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9043,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 355,
          "cache_read_input_tokens": 9043,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1124,
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

_source line 15 · 2026-05-30T06:14:16.145Z_

<details><summary>↩ Tool result · `toolu_01BBMSdFV2FyiaHnapmQeB2F`</summary>

```text
Web search results for query: "visual document retrieval survey 2025 2026"

Links: [{"title":"A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends","url":"https://arxiv.org/html/2507.09861v2"},{"title":"Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding","url":"https://arxiv.org/html/2510.15253v3"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.19961"},{"title":"Roles of MLLMs in Visually Rich Document Retrieval for RAG: A Survey","url":"https://arxiv.org/pdf/2601.03262"},{"title":"A Survey of Cross-Modal Image-Text Retrieval","url":"https://www.icck.org/filebob/uploads/storage/CJIF_k8UiIafD4xkk4zR.pdf"},{"title":"DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning","url":"https://arxiv.org/pdf/2509.23883"}]

Based on the web search results, here are the key findings about visual document retrieval surveys from 2025-2026:

## Recent Surveys on Visual Document Retrieval

Multimodal retrieval, the task of retrieving relevant multimodal information using queries spanning multiple modalities like text and vision, has become a cornerstone of modern information retrieval. 

Several comprehensive surveys have emerged in this period:

1. **MLLM-Based Document Understanding**: Research has shifted from early single-page, text-centric retrieval to more complex benchmarks, with work like Docs2Synth providing a synthetic data trained retriever framework for scanned visually rich documents.

2. **Multimodal RAG Approaches**: MoLoRAG (2025) bootstraps document understanding via multi-modal logic-aware retrieval, representing advances in integrating visual document understanding with retrieval-augmented generation.

3. **Dedicated VDR Survey**: A dedicated comprehensive analysis of Visual Document Retrieval (VDR) in the LLM era has been notably absent from previous research, though this gap appears to be filling with recent publications.

4. **Key Methodological Shift**: The methodology for VDR has undergone significant paradigm shift from early OCR-based approaches to LVLM-based methods, which have demonstrated state-of-the-art retrieval performance.

5. **Emerging Frameworks**: New methods like Document Screenshot Embedding (DSE) treat page screenshots as the unit of indexing, avoiding preprocessing steps that introduce error.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab8adf45-525d-4ed1-be50-291b1819e7b4",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "9ad89b2d-7342-403e-b061-7cdf997b3c07",
  "sourceToolAssistantUUID": "ab8adf45-525d-4ed1-be50-291b1819e7b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-30T06:14:16.274Z_

<details><summary>↩ Tool result · `toolu_01LpiD3TfgXF57ZFpg3tyRgU`</summary>

```text
Web search results for query: "multimodal information retrieval survey 2024 2025"

Links: [{"title":"A Survey on Multimodal Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.08748v1"},{"title":"A survey of multimodal recommender systems: methods, challenges, and future directions | International Journal of Multimedia Information Retrieval | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13735-026-00406-x"},{"title":"Retrieving Multimodal Information for Augmented Generation: A Survey","url":"https://arxiv.org/pdf/2303.10868"},{"title":"[2504.08748] A Survey of Multimodal Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2504.08748"},{"title":"Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation [Quick Review]","url":"https://liner.com/review/ask-in-any-modality-comprehensive-survey-on-multimodal-retrievalaugmented-generation"},{"title":"GitHub - llm-lab-org/Multimodal-RAG-Survey: A Survey on Multimodal Retrieval-Augmented Generation · GitHub","url":"https://github.com/llm-lab-org/Multimodal-RAG-Survey"},{"title":"A Review on Retrieval-Augmented Generation","url":"https://faith.futuretechsci.org/index.php/FAITH/article/download/297/75/1689"},{"title":"The 1st EReL@MIR Workshop on Efficient Representation Learning for   Multimodal Information Retrieval","url":"https://arxiv.org/pdf/2504.14788"}]

Based on the search results, here are several recent surveys on multimodal information retrieval from 2024-2025:

## Key Surveys

**1. Multimodal Retrieval-Augmented Generation (MRAG) Survey**

A survey reviews MRAG's essential components, datasets, evaluation methods, and limitations, and identifies challenges and future research directions, highlighting MRAG's potential to revolutionize multimodal information retrieval and generation. Recent studies show MRAG outperforms traditional RAG, especially in scenarios requiring both visual and textual understanding.

This is an ACL 2025 paper that summarizes a comprehensive survey on Multimodal RAG, detailing its taxonomy and research trends. The authors provide a comprehensive review of Multimodal RAG, covering its task formulation, datasets, benchmarks, evaluation metrics, and key innovations.

**2. Multimodal Recommender Systems Survey**

A survey synthesizes over 127 recent publications (2016–2025) and organizes the MMRS landscape through a novel pipeline-based taxonomy comprising six stages: modality extraction, filtration, bridging, fusion, augmentation, and optimization.

**3. Workshop on Efficient Representation Learning**

The first EReL@MIR workshop was proposed at the Web Conference 2025, inviting participants to explore novel solutions, emerging problems, challenges, efficiency evaluation metrics and benchmarks.

These surveys cover various aspects of multimodal information retrieval, from retrieval-augmented generation to recommendation systems and efficient representation learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2083629-8078-4897-af77-347d642e3b59",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "bfc94332-a936-46d9-b5c7-e74f34974d40",
  "sourceToolAssistantUUID": "b2083629-8078-4897-af77-347d642e3b59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:14:17.895Z_

<details><summary>↩ Tool result · `toolu_01QKwv97dyqULjD3Vbn7V9QX`</summary>

```text
Web search results for query: "document retrieval benchmark evaluation 2025 2026"

Links: [{"title":"From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents","url":"https://arxiv.org/html/2604.01733v1"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/html/2602.19961v1"},{"title":"BEIR Benchmark Leaderboard 2025 & 2026: NDCG@10 Scores & Rankings | Ailog RAG","url":"https://app.ailog.fr/en/blog/news/beir-benchmark-update"},{"title":"Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG","url":"https://arxiv.org/html/2603.04238v1"},{"title":"RAG Benchmarks Leaderboard: Retrieval Rankings 2026 | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/rag-benchmarks-leaderboard/"},{"title":"Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks","url":"https://arxiv.org/pdf/2603.04532"},{"title":"Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?","url":"https://arxiv.org/pdf/2508.03644"}]

Based on the search results, here's what I found about document retrieval benchmark evaluation in 2025-2026:

## Recent Benchmarks and Leaderboards

As of April 2026, Gemini Embedding 2 leads retrieval benchmarks with 67.71 on the MTEB retrieval subset, followed by Voyage 4 Large and NV-Embed-v2.

BEIR (Benchmarking Information Retrieval) is a heterogeneous benchmark for zero-shot evaluation of retrieval models created in 2021, testing models across 18 diverse datasets and measuring how well models generalize to unseen domains without fine-tuning.

## Specialized Benchmarks

Several domain-specific and specialized benchmarks have emerged:

- T2-RAGBench, a financial QA benchmark, was accepted at EACL 2026.

- VisR-Bench is a benchmark for retrieval-augmented question answering over long, visually rich documents.

- DOUBLE-BENCH is a new benchmark consisting of 5,168 human-validated single- and multi-hop queries and 3,276 documents in 6 languages and 4 types of document data.

## Multilingual Focus

In May 2025, MIRACL-VISION extended the benchmark to visual document retrieval across 18 languages.

## Temporal Evaluation

Research on temporal drift examined test collections using two independent corpus snapshots of ten GitHub repositories providing documentation for RAG frameworks, with snapshots from October 2024 and October 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2aad36b-cf56-4771-ba0d-fd187760e203",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "af2aa1d3-4cb1-4465-9f6d-020834bdae94",
  "sourceToolAssistantUUID": "b2aad36b-cf56-4771-ba0d-fd187760e203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T06:14:17.900Z_

<details><summary>↩ Tool result · `toolu_01NPjnFmjTkWkbCucUngJSJ5`</summary>

```text
Web search results for query: "document understanding vision language model survey 2025"

Links: [{"title":"Vision Language Models Survey 2025 | Libertify","url":"https://www.libertify.com/interactive-library/vision-language-models-survey/"},{"title":"A Survey of Multimodal Models on Language and Vision: A Unified Modeling Perspective","url":"https://www.sciltp.com/journals/dmml/articles/2510001963"},{"title":"Vision Language Models: A Survey of 26K Papers","url":"https://arxiv.org/pdf/2510.09586"},{"title":"Vision Encoders in Vision-Language Models: A Survey Han Xiao Jina AI by Elastic","url":"https://jina.ai/vision-encoder-survey.pdf"},{"title":"A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends","url":"https://arxiv.org/pdf/2507.09861"},{"title":"From Perception to Cognition: A Survey of Vision-Language Interactive Reasoning in Multimodal Large Language Models","url":"https://arxiv.org/html/2509.25373v1"},{"title":"A comprehensive survey of Vision–Language Models: Pretrained models, fine-tuning, prompt engineering, adapters, and benchmark datasets - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1566253525006955"},{"title":"[2510.09586] Vision Language Models: A Survey of 26K Papers","url":"https://arxiv.org/abs/2510.09586"}]

I've found several highly relevant resources for document understanding and vision-language models from 2025:

## Key Surveys on Vision-Language Models (2025)

A comprehensive survey analyzed 26,104 accepted papers from CVPR, ICLR, and NeurIPS spanning 2023–2025. This survey provides insight into major research trends in the field.

## Major Research Trends

Multimodal vision-language-LLM work has become the dominant research paradigm, consuming 40% of all accepted papers by 2025. Additionally, by 2025, the community has pivoted decisively toward instruction following and reasoning, reflecting the influence of ChatGPT-style interaction paradigms on visual understanding research.

## Document Understanding Specifically

Multimodal Large Language Models (MLLMs) trained on massive visual and linguistic datasets have demonstrated powerful representational capabilities for understanding text-rich images, and MLLM-based frameworks have shown prominent performances on diverse document structure recognition and information extraction.

## Model Development

LLaVA demonstrates the fastest growth trajectory—from 0.1% in 2023 to 2.7% in 2025, while ALIGN remains the most frequently cited VLM family.

The search results include several specialized surveys covering vision encoders, comprehensive VLM components (fine-tuning, prompt engineering), and MLLM-based visually rich document understanding frameworks from 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2db5f201-f4d4-4ed1-8e9c-2e950adc8189",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "a7e5a63f-be9a-4445-bf4c-7b8acc2145d9",
  "sourceToolAssistantUUID": "2db5f201-f4d4-4ed1-8e9c-2e950adc8189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:14:17.985Z_

<details><summary>↩ Tool result · `toolu_014avJWqBrYavuFUXzrr5DJD`</summary>

```text
Web search results for query: "ViDoRe benchmark visual document retrieval 2025 2026"

Links: [{"title":"ViDoRe Benchmarks for Visual Retrieval","url":"https://www.emergentmind.com/topics/vidore-benchmarks"},{"title":"GitHub - illuin-tech/vidore-benchmark: Vision Document Retrieval (ViDoRe): Benchmark. Evaluation code for the ColPali paper. · GitHub","url":"https://github.com/illuin-tech/vidore-benchmark"},{"title":"vidore (Vidore)","url":"https://huggingface.co/vidore"},{"title":"Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/pdf/2407.01449"},{"title":"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models","url":"https://arxiv.org/pdf/2509.15432"},{"title":"[2505.17166] ViDoRe Benchmark V2: Raising the Bar for Visual Retrieval","url":"https://arxiv.org/abs/2505.17166"},{"title":"[2601.08620] ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios","url":"https://arxiv.org/abs/2601.08620"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.03992"},{"title":"ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios","url":"https://arxiv.org/pdf/2601.08620"},{"title":"VIDORE BENCHMARK V2: Raising the Bar for Visual Retrieval Quentin Mac´e1","url":"https://arxiv.org/pdf/2505.17166"}]

Based on the search results, here's what I found about the ViDoRe benchmark for visual document retrieval in 2025-2026:

## Overview

ViDoRe is a comprehensive benchmark to evaluate systems on page-level document retrieval with wide coverage of domains, visual elements, and languages.

## Recent Versions

ViDoRe Benchmark V2 was released in 2025, with the title "Raising the Bar for Visual Retrieval", and ViDoRe V3 followed in 2026, focusing on "A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios".

## Key Features

**Document Coverage:** The benchmark covers scientific publications, charts, forms, tables, industry reports, regulatory documents, financial/HR/energy/pharma/maintenance records, and ESG reports.

**Multilingual Support:** Queries and corpora are in English, French, and up to six languages for V3, with training data typically monolingual and evaluation multilingual.

**Query Types:** Queries include open-ended, extractive, numerical, multi-hop, compare/contrast, boolean, and enumerative types.

## ViDoRe V3 Enhancements

Through 12,000 hours of human annotation effort, V3 provides high-quality annotations for retrieval relevance, bounding box localization, and verified reference answers. Evaluation of state-of-the-art RAG pipelines reveals that visual retrievers outperform textual ones, late-interaction models and textual reranking substantially improve performance, and hybrid or purely visual contexts enhance answer generation quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ec00828-7f37-4e94-ad63-4fd6cf0b7a78",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "3cfdc671-3c05-4f56-a742-17898f3c9360",
  "sourceToolAssistantUUID": "2ec00828-7f37-4e94-ad63-4fd6cf0b7a78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:14:18.110Z_

<details><summary>↩ Tool result · `toolu_01P3uqLJ3MzHfRDGwyXur6BM`</summary>

```text
Web search results for query: "site:paperswithcode.com visual document retrieval SOTA"

Links: [{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.19961"},{"title":"DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning","url":"https://arxiv.org/pdf/2509.23883"},{"title":"Papers with Code - Fine-grained Late-interaction Multi-modal Retrieval for Retrieval Augmented Visual Question Answering","url":"https://paperswithcode.com/paper/fine-grained-late-interaction-multi-modal-1"},{"title":"Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"https://arxiv.org/pdf/2505.07730"},{"title":"Attention Grounded Enhancement for Visual Document Retrieval","url":"https://arxiv.org/pdf/2511.13415"},{"title":"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models","url":"https://arxiv.org/pdf/2509.15432"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/pdf/2506.04997"},{"title":"Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework","url":"https://arxiv.org/pdf/2602.19549"},{"title":"Index Light, Reason Deep: Deferred Visual Ingestion for Visual-Dense Document Question Answering","url":"https://arxiv.org/pdf/2602.14162"}]

Based on the search results, here's what I found about Visual Document Retrieval (VDR) and the current state-of-the-art:

## Overview of Visual Document Retrieval

Visual Document Retrieval (VDR) is the task of retrieving relevant document pages based on a query that leverages both visual and textual cues, with importance in applications from e-commerce product searches to educational resource discovery. VDR is an emerging research area that focuses on encoding and retrieving document images directly, bypassing the dependence on Optical Character Recognition (OCR) for document search.

## Current State-of-the-Art

The state-of-the-art visualized document retriever is ColPali/ColQwen2. ColPali introduced a recent advance in VDR that significantly improved retrieval effectiveness through a late interaction mechanism and demonstrated substantial performance gains over existing baselines.

Additionally, SERVAL reaches 63.4% nDCG@5 on the ViDoRe-v2 benchmark, surpassing the strongest specialised multi-vector visual document encoder.

## Key Characteristics

VDR presents greater challenges than traditional text retrieval as it must interpret not only textual content but also complex layouts, tables, figures, and other visual elements that convey critical information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5ae4b0f-2ada-4ad3-a911-f49d62cbb5a6",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "a6875d98-8a09-45fb-ba9d-463bda36ee46",
  "sourceToolAssistantUUID": "f5ae4b0f-2ada-4ad3-a911-f49d62cbb5a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:14:18.745Z_

<details><summary>↩ Tool result · `toolu_01PAZTrHw3NeGtq4rRYCoETV`</summary>

```text
Web search results for query: "most cited visual document retrieval 2024 2025"

Links: [{"title":"ViDoRAG: Visual Document Retrieval-Augmented ...","url":"https://aclanthology.org/2025.emnlp-main.464.pdf"},{"title":"Published as a conference paper at ICLR 2025 VISRAG: VISION-BASED","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf"},{"title":"Visual Document Retrieval: Concepts & Advances","url":"https://www.emergentmind.com/topics/visual-document-retrieval-vdr"},{"title":"[2407.01449] ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/abs/2407.01449"},{"title":"VISR-BENCH: A VISUAL RETRIEVAL BENCHMARK FOR ...","url":"https://openreview.net/pdf?id=No8PAJEyeG"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.19961"},{"title":"Sitemap - 2024 - Top Information Retrieval Papers of the Week","url":"https://recsys.substack.com/sitemap/2024"}]

Based on the search results, here are the key findings about most cited visual document retrieval work in 2024-2025:

## Recent Notable Work and Benchmarks

**ColPali** is a prominent framework for efficient document retrieval with vision language models, submitted in June 2024 and last revised in February 2025, that addresses how documents convey information through text, figures, layouts, and tables.

The **ViDoRe Benchmark V1/V2** provides a multilingual, multi-domain evaluation environment incorporating realistic, complex query scenarios.

**MIRACL-VISION** is a multilingual visual benchmark covering 18 languages with human-generated queries designed to stress VLM multilingual generalization.

**Jina-VDR** is a 30-task, multi-domain, multi-modal benchmark specifically designed for visually-rich image/document retrieval.

## Recent Conference Publications

**ViDoRAG** was presented at EMNLP 2025 (November 4-9, 2025) on Visual Document Retrieval-Augmented Generation.

Recent work includes notable advancements in high-resolution visual understanding and OCR capabilities.

## Core Problem Being Addressed

Modern VDR aims to capture both textual and non-textual cues such as layout, tables, figures, and other visual structures, overcoming limitations of OCR-based systems that often discard layout and visual information essential for reliable evidence localization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4fde79a-2c5b-4fd1-a537-d75970456c67",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "6e437926-f287-4145-ad06-22303bd6099a",
  "sourceToolAssistantUUID": "a4fde79a-2c5b-4fd1-a537-d75970456c67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-30T06:14:22.234Z_

Good, I have a rich set of results. Now let me fetch the abstracts of the most relevant papers. Let me start with the first batch of unique, non-excluded papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e437926-f287-4145-ad06-22303bd6099a",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c9008ff-cd86-4ed4-a993-3b57dbfadb83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 23 · 2026-05-30T06:14:23.190Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ErA59F6WLdNga3T82GNBma`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.19961",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c9008ff-cd86-4ed4-a993-3b57dbfadb83",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e0ac0a9-a4cd-49ca-b046-62cb869c0ccb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 24 · 2026-05-30T06:14:23.662Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NnKiLX7qGqzs53x8xjbtUn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03262",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e0ac0a9-a4cd-49ca-b046-62cb869c0ccb",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6ca7483-41c6-4189-824f-f599fbc81a0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 25 · 2026-05-30T06:14:24.614Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014dsXnVaYgAvFrK5yA9mtTf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.15253",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ca7483-41c6-4189-824f-f599fbc81a0c",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e02685c7-f601-494e-aa12-4eb2d88fe100",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 26 · 2026-05-30T06:14:25.066Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RRCnLzXqqbq9szFMfNqF5N`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.09861",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e02685c7-f601-494e-aa12-4eb2d88fe100",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c81741b-b9a1-4264-9b40-58c7f89e559e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 27 · 2026-05-30T06:14:25.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PhwkCRNHL8kiYDtuNSQH5N`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.15432",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c81741b-b9a1-4264-9b40-58c7f89e559e",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "408f01aa-d98f-412a-b458-45cac91304d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 28 · 2026-05-30T06:14:26.456Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YXFKjWnmgaWudqqmLopREp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.08748",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "408f01aa-d98f-412a-b458-45cac91304d3",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2811908e-4b80-4dc5-ba11-03768c909ab5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5816,
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

_source line 29 · 2026-05-30T06:14:26.821Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014W9DW9daPikhoDweMToz4q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.17166",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2811908e-4b80-4dc5-ba11-03768c909ab5",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG87xkfezChMTXdzoPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4d14061-0b0f-45e6-a91f-c4f61de9a1c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjQX2Bjgt964gqk8onmYs7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5816,
      "cache_read_input_tokens": 10167,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 616,
          "cache_read_input_tokens": 10167,
          "cache_creation_input_tokens": 5816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5816,
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

_source line 30 · 2026-05-30T06:14:27.460Z_

<details><summary>↩ Tool result · `toolu_01NnKiLX7qGqzs53x8xjbtUn`</summary>

```text
# Paper Details

**Full Title:** "Roles of MLLMs in Visually Rich Document Retrieval for RAG: A Survey"

**Author:** Xiantao Zhang

**Submission Date:** December 16, 2025

**Abstract:**
The paper addresses challenges that visually rich documents present to retrieval-augmented generation systems, specifically "layout-dependent semantics, brittle OCR, and evidence spread across complex figures and structured tables." The survey categorizes how multimodal language models tackle these issues into three approaches: Modality-Unifying Captioners, Multimodal Embedders, and End-to-End Representers. The author compares these methods across dimensions including retrieval granularity, information preservation, performance efficiency, and compatibility with additional processing techniques. The work concludes by highlighting emerging research opportunities such as adaptive retrieval strategies, model optimization, and assessment frameworks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6ca7483-41c6-4189-824f-f599fbc81a0c",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "4fd6ea1d-510e-41fa-aadb-234bfa8603f4",
  "sourceToolAssistantUUID": "c6ca7483-41c6-4189-824f-f599fbc81a0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T06:14:27.506Z_

<details><summary>↩ Tool result · `toolu_01ErA59F6WLdNga3T82GNBma`</summary>

```text
# Paper Details

**Full Title:** "Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval"

**Authors:** Yibo Yan, Jiahao Huo, Guanbo Feng, Mingdong Ou, Yi Cao, Xin Zou, Shuliang Liu, Yuanhuiyi Lyu, Yu Huang, Jungang Li, Kening Zheng, Xu Zheng, Philip S. Yu, James Kwok, and Xuming Hu

**Submission Date:** February 23, 2026 (Version 1); last revised March 23, 2026 (Version 2)

**Abstract:** This comprehensive survey examines visual document retrieval through the lens of multimodal large language models. The work distinguishes documents from natural images by their characteristic "dense textual content, intricate layouts, and fine-grained semantic dependencies." The authors categorize methodological approaches into three areas: multimodal embedding models, multimodal reranker models, and integration of retrieval-augmented generation with agentic systems. The paper concludes by identifying challenges and proposing future research directions for advancing multimodal document intelligence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e0ac0a9-a4cd-49ca-b046-62cb869c0ccb",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "bea525b1-601f-4c29-a88f-4f592fab96c0",
  "sourceToolAssistantUUID": "7e0ac0a9-a4cd-49ca-b046-62cb869c0ccb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T06:14:28.993Z_

<details><summary>↩ Tool result · `toolu_01RRCnLzXqqbq9szFMfNqF5N`</summary>

```text
# Paper Information

**Full Title:** "A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends"

**Authors:** Yihao Ding, Siwen Luo, Yue Dai, Yanbei Jiang, Zechuan Li, Qiang Sun, Geoffrey Martin, Wei Liu, and Yifan Peng

**Submission Date:** July 14, 2025 (v1); Last revised April 21, 2026 (v2)

**Abstract:** The paper addresses how multimodal large language models can interpret documents containing "intricate visual, textual, and structural elements." It examines both OCR-based and OCR-free approaches for extracting information from document images. The survey focuses on two primary areas: techniques for combining textual, visual, and layout information, plus training approaches including pretraining and instruction tuning. The authors also discuss obstacles like limited training data, multi-page document handling, and multilingual content, while exploring emerging technologies such as retrieval-augmented generation and agent-based systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c81741b-b9a1-4264-9b40-58c7f89e559e",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "d2ed7e0f-356b-4c41-9c31-81685bd7d86a",
  "sourceToolAssistantUUID": "4c81741b-b9a1-4264-9b40-58c7f89e559e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T06:14:29.375Z_

<details><summary>↩ Tool result · `toolu_014dsXnVaYgAvFrK5yA9mtTf`</summary>

```text
# Paper Details

**Full Title:** "Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding"

**Authors:** Sensen Gao, Shanshan Zhao, Xu Jiang, Lunhao Duan, Yong Xien Chng, Qing-Guo Chen, Weihua Luo, Kaifu Zhang, Jia-Wang Bian, and Mingming Gong

**Submission Date:** October 17, 2025 (v1); last revised April 20, 2026 (v3)

**Abstract:**
The paper addresses document understanding challenges in applications ranging from financial analysis to scientific discovery. Current methods—whether OCR-based or multimodal—have limitations in handling documents' combined text, tables, charts, and layout. The authors propose that "Multimodal RAG" enables "holistic retrieval and reasoning across all modalities" for comprehensive document intelligence. The survey presents a taxonomy organized by domain, retrieval modality, and granularity, reviews advances using graph structures and agentic systems, and discusses datasets, benchmarks, applications, and industry implementation. It identifies open challenges in efficiency, fine-grained representation, and robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e02685c7-f601-494e-aa12-4eb2d88fe100",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "df676515-7f5a-4fe4-a222-bcc72766005d",
  "sourceToolAssistantUUID": "e02685c7-f601-494e-aa12-4eb2d88fe100",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:14:29.655Z_

<details><summary>↩ Tool result · `toolu_01PhwkCRNHL8kiYDtuNSQH5N`</summary>

```text
# SERVAL Paper Details

**Full Title:**
"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models"

**Authors:**
Thong Nguyen, Yibin Lei, Jia-Huei Ju, Andrew Yates

**Submission Date:**
September 18, 2025

**Abstract:**
The researchers present a novel approach to visual document retrieval that generates "detailed textual description[s] of each document image" using a vision-language model, then applies standard text encoding. Their method achieves 63.4% nDCG@5 on the ViDoRe-v2 benchmark, outperforming specialized encoders. The technique offers advantages including better scalability for large collections and improved multilingual support. The authors demonstrate that modern vision-language models effectively capture "complex textual and visual cues with sufficient granularity" to serve as a semantic bridge, eliminating the need for intensive contrastive training and establishing a strong zero-shot baseline for future systems in this domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "408f01aa-d98f-412a-b458-45cac91304d3",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "76611e37-6b21-40d4-b52b-c8a65837b9b7",
  "sourceToolAssistantUUID": "408f01aa-d98f-412a-b458-45cac91304d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-30T06:14:29.739Z_

<details><summary>↩ Tool result · `toolu_01YXFKjWnmgaWudqqmLopREp`</summary>

```text
# Paper Details

**Full Title:** "A Survey of Multimodal Retrieval-Augmented Generation"

**Authors:** Lang Mei, Siyu Mo, Zhihan Yang, Chong Chen

**Submission Date:** March 26, 2025

**Abstract:** The paper examines how MRAG enhances language models by incorporating diverse data types (text, images, videos) into retrieval and generation processes. Unlike text-focused approaches, this framework "reduces hallucinations and enhances question-answering systems by grounding responses in factual, multimodal knowledge." Research indicates MRAG surpasses traditional methods in scenarios requiring both visual and textual comprehension. The survey covers essential components, datasets, evaluation techniques, and current limitations while exploring future research opportunities in multimodal information systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2811908e-4b80-4dc5-ba11-03768c909ab5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "115842e2-08ed-481d-b580-4fc31e257266",
  "sourceToolAssistantUUID": "2811908e-4b80-4dc5-ba11-03768c909ab5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T06:14:30.761Z_

<details><summary>↩ Tool result · `toolu_014W9DW9daPikhoDweMToz4q`</summary>

```text
# ViDoRe Benchmark V2 Paper Details

**Full Title:** "ViDoRe Benchmark V2: Raising the Bar for Visual Retrieval"

**Authors:** Quentin Macé, António Loison, Manuel Faysse

**Submission Date:** May 22, 2025 (v1); revised September 19, 2025 (v2)

**Abstract:** 
The paper addresses saturation issues in the original ViDoRe Benchmark, where "top models exceeding 90% nDCG@5" limited meaningful differentiation. Version 2 introduces more demanding evaluation scenarios including contextual blind querying, extended cross-document queries, and a mixed approach combining synthetic and human-validated question generation. The benchmark encompasses four multilingual datasets with explicit evaluation guidance. Early findings reveal "substantial room for advancement" and provide insights regarding model generalization and multilingual performance. The authors present this as an evolving community resource.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d14061-0b0f-45e6-a91f-c4f61de9a1c5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "ffab227a-63c5-4afb-b55f-ebd3c4652077",
  "sourceToolAssistantUUID": "a4d14061-0b0f-45e6-a91f-c4f61de9a1c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-30T06:14:33.308Z_

Now let me fetch more papers from the search results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffab227a-63c5-4afb-b55f-ebd3c4652077",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b91d07a-ef04-49ce-b02a-5307e4128bc7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 38 · 2026-05-30T06:14:34.795Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DENMkuYVPJt6zUQu7S8ZUr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.23883",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b91d07a-ef04-49ce-b02a-5307e4128bc7",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b073e0c4-3d0c-4e00-b557-bda05536e160",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 39 · 2026-05-30T06:14:35.269Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016J3ViA1D5DXekDi1fjTexv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.09586",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b073e0c4-3d0c-4e00-b557-bda05536e160",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be206482-fe6e-4286-bf27-5f185bd8fbe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 40 · 2026-05-30T06:14:36.213Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JYH9Q1RJkGmmGoMUsHtUhT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03992",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be206482-fe6e-4286-bf27-5f185bd8fbe1",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "778b6e2c-55e9-4ab2-b943-c6753043f27e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 41 · 2026-05-30T06:14:36.686Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0148Q7RhqwvWWzo5Uo3MWRiW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.19549",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "778b6e2c-55e9-4ab2-b943-c6753043f27e",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7f5068c-c2b5-4337-a7bb-520dc92c51a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 42 · 2026-05-30T06:14:37.157Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BPnnVwHBC8wPNzgowRX48W`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.14162",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f5068c-c2b5-4337-a7bb-520dc92c51a5",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dafb683-dba8-4aa3-a74f-248e2cc1f9f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 43 · 2026-05-30T06:14:38.096Z_

<details><summary>↩ Tool result · `toolu_01DENMkuYVPJt6zUQu7S8ZUr`</summary>

```text
# DocPruner Paper Details

**Full Title:**
"DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning"

**Authors:**
Yibo Yan, Guangwei Xu, Xin Zou, Shuliang Liu, James Kwok, and Xuming Hu

**Submission Date:**
September 28, 2025

**Abstract:**
The paper introduces a framework addressing storage limitations in visual document retrieval systems. The researchers explain that while "multi-vector paradigm" approaches using patch-level embeddings are effective, they require substantial storage. DocPruner tackles this by employing "adaptive patch-level embedding pruning" that identifies and removes redundant embeddings based on attention patterns. The framework achieves "a significant 50-60% reduction in storage" while maintaining retrieval performance across multiple datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b073e0c4-3d0c-4e00-b557-bda05536e160",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "12903acb-e6a9-4cf9-801a-69323cec9b56",
  "sourceToolAssistantUUID": "b073e0c4-3d0c-4e00-b557-bda05536e160",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-30T06:14:38.104Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HQNbst9oKL4oyKw6hxtuG9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.07730",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12903acb-e6a9-4cf9-801a-69323cec9b56",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f70fa4c1-c8df-447d-b195-95d2008820b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
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

_source line 45 · 2026-05-30T06:14:38.567Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013crqCKHfFpR61GagKSQCtN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.04997",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f70fa4c1-c8df-447d-b195-95d2008820b7",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG91Pe7epXFuY7DbyHN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f96953a-633c-4750-9703-20943bfd22a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W19G7HFth6H4gpcpBixXwT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 15983,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 15983,
          "cache_creation_input_tokens": 2432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2432,
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

_source line 46 · 2026-05-30T06:14:39.923Z_

<details><summary>↩ Tool result · `toolu_016J3ViA1D5DXekDi1fjTexv`</summary>

```text
# Paper Details

**Full Title:** "Vision Language Models: A Survey of 26K Papers"

**Author:** Fengming Lin

**Submission Date:** Friday, October 10, 2025

**Abstract Summary:**

This comprehensive analysis examines 26,104 papers accepted at CVPR, ICLR, and NeurIPS between 2023-2025. The research employs normalized titles and abstracts matched against a custom lexicon to assign topical labels and extract details about tasks, architectures, training approaches, and datasets.

The study identifies three major trends: (1) rapid expansion of multimodal vision-language-LLM research reframing traditional perception tasks as instruction-following problems; (2) generative methods growing steadily, with diffusion research focusing on "controllability, distillation, and speed"; and (3) sustained 3D and video research, with composition techniques shifting from NeRFs to Gaussian splatting.

Within vision-language models specifically, the authors find parameter-efficient methods like prompting and LoRA are dominant, while training practices have shifted toward instruction tuning of existing backbones rather than building encoders from scratch. The researchers make their methodology and lexicon publicly available for community auditing and extension.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be206482-fe6e-4286-bf27-5f185bd8fbe1",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "16b2a3a5-bb73-436d-be99-3512e9d16b2c",
  "sourceToolAssistantUUID": "be206482-fe6e-4286-bf27-5f185bd8fbe1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-30T06:14:40.401Z_

<details><summary>↩ Tool result · `toolu_0148Q7RhqwvWWzo5Uo3MWRiW`</summary>

```text
# Paper Summary

**Full Title:** "Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework"

**Authors:** Yibo Yan, Mingdong Ou, Yi Cao, Xin Zou, Jiahao Huo, Shuliang Liu, James Kwok, and Xuming Hu

**Submission Date:** February 23, 2026 (v1); revised April 20, 2026 (v2)

**Abstract:** The paper addresses challenges in Visual Document Retrieval by proposing a two-stage framework. The authors note that while current multi-vector approaches perform well, they face "prohibitive overhead" that existing methods inadequately resolve. Their solution combines "adaptive pruning" to eliminate low-value patches with "hierarchical merging" to compress embeddings, aiming to preserve semantic information while reducing storage requirements. Testing across 29 datasets demonstrates improved performance and extended compression capabilities compared to existing alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7f5068c-c2b5-4337-a7bb-520dc92c51a5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "de723e17-20ce-4661-bd37-0093c8c52a25",
  "sourceToolAssistantUUID": "e7f5068c-c2b5-4337-a7bb-520dc92c51a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-30T06:14:40.918Z_

<details><summary>↩ Tool result · `toolu_01JYH9Q1RJkGmmGoMUsHtUhT`</summary>

```text
# Paper Information

**Full Title:** 
"Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval"

**Authors:** 
Gabriel de Souza P. Moreira, Ronay Ak, Mengyao Xu, Oliver Holworthy, Benedikt Schifferer, Zhiding Yu, Yauhen Babakhin, Radek Osmulski, Jiarui Cai, Ryan Chesler, Bo Liu, and Even Oldridge

**Submission Date:** 
February 3, 2026 (v1); last revised April 1, 2026 (v2)

**Abstract:**
The authors present embedding models designed for visual document retrieval in Retrieval-Augmented Generation systems. They introduce three model variants (3B, 4B, and 8B parameters) built on Vision Language Models. Their 8B model achieved first place on the ViDoRe V3 leaderboard with "an average NDCG@10 of 63.42." Key techniques discussed include "cluster-based sampling, hard-negative mining, bidirectional attention, late interaction, and model merging," along with engineering considerations for balancing accuracy and storage efficiency with reduced-dimension embeddings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "778b6e2c-55e9-4ab2-b943-c6753043f27e",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "9b073577-feb5-4003-b646-196828854698",
  "sourceToolAssistantUUID": "778b6e2c-55e9-4ab2-b943-c6753043f27e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-30T06:14:42.553Z_

<details><summary>↩ Tool result · `toolu_01HQNbst9oKL4oyKw6hxtuG9`</summary>

```text
# Research Paper Summary

**Title:** "Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction"

**Authors:** Jingfen Qiao, Jia-Huei Ju, Xinyu Ma, Evangelos Kanoulas, Andrew Yates

**Submission Date:** May 12, 2025

**Abstract:** The researchers examine visual document retrieval (VDR) methods that work directly with document images rather than relying on OCR. They evaluate whether "late interaction mechanisms" improve performance across different vision-language models. While confirming that late interaction enhances retrieval effectiveness, they note it creates computational challenges during inference. The study also explores how VDR models handle text inputs and assesses their robustness with text-heavy datasets. A key finding reveals that query tokens "tend to match the patch contains visually similar tokens or their surrounding patches," even though they cannot explicitly match image patches as in traditional text retrieval scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f70fa4c1-c8df-447d-b195-95d2008820b7",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "907160ba-5eb3-4b21-a9c2-8f53f4bc4194",
  "sourceToolAssistantUUID": "f70fa4c1-c8df-447d-b195-95d2008820b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-30T06:14:42.782Z_

<details><summary>↩ Tool result · `toolu_013crqCKHfFpR61GagKSQCtN`</summary>

```text
# Paper Summary

**Full Title:**
"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings"

**Authors:**
Yubo Ma, Jinsong Li, Yuhang Zang, Xiaobao Wu, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Haodong Duan, Jiaqi Wang, Yixin Cao, and Aixin Sun

**Submission Date:**
June 5, 2025

**Abstract:**
The researchers address excessive memory consumption in ColPali/ColQwen2 visual document retrieval systems by examining token-reduction approaches. They compare token pruning and token merging strategies, finding that while random pruning surprisingly outperforms complex methods, it remains inadequate for this task. The team concludes merging is better suited to the problem and introduces "Light-ColPali/ColQwen2," which achieves "98.2% of retrieval performance with only 11.8% of original memory usage" and maintains "94.6% effectiveness at 2.8% memory footprint."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f96953a-633c-4750-9703-20943bfd22a4",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "13e1adbe-4494-4786-a99b-ed05917fbdd6",
  "sourceToolAssistantUUID": "6f96953a-633c-4750-9703-20943bfd22a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-30T06:14:42.902Z_

<details><summary>↩ Tool result · `toolu_01BPnnVwHBC8wPNzgowRX48W`</summary>

```text
# Paper Summary

**Full Title:** "Index Light, Reason Deep: Deferred Visual Ingestion for Visual-Dense Document Question Answering"

**Author:** Tao Xu

**Submission Date:** February 15, 2026 (v1); revised February 26, 2026 (v2)

**Abstract Summary:**

The research addresses limitations in multimodal document question answering systems. Traditional approaches process document pages through Vision Language Models during indexing, converting visual content to text descriptions that are then vectorized for retrieval. However, this strategy struggles with engineering documents because descriptions lose visual nuances and embedding similarity fails on homogeneous content.

The proposed framework eliminates VLM processing at the indexing stage. Instead, it builds a hierarchical index using only structural elements (table of contents, drawing numbers) via a novel clustering algorithm. During questioning, the system retrieves candidate pages through BM25 and sends original images directly to a VLM for analysis.

Experimental validation shows substantial improvements: on Bridge engineering drawings, accuracy reached "65.6% vs. PI's 24.3% (+41.3pp)"; on Steel catalogs, "30.6% vs. 16.1% (+14.5pp)"; and on CircuitVQA benchmarks, retrieval performance achieved "31.2% vs. 0.7%".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dafb683-dba8-4aa3-a74f-248e2cc1f9f3",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "b46947d7-7ca9-4785-96e7-26706603cfec",
  "sourceToolAssistantUUID": "4dafb683-dba8-4aa3-a74f-248e2cc1f9f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-30T06:14:45.054Z_

Let me fetch more papers from the search results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b46947d7-7ca9-4785-96e7-26706603cfec",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff4ef706-6a59-4823-945d-382d80fc3035",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 53 · 2026-05-30T06:14:46.085Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RPKBLURU8nDdyopHHisXmW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.14788",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff4ef706-6a59-4823-945d-382d80fc3035",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e3c2040-f837-4256-9aa0-967c1c189efd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 54 · 2026-05-30T06:14:46.979Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HW4ei4uJuybNQDt71jcSoq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01733",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e3c2040-f837-4256-9aa0-967c1c189efd",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ad1c0e6-a355-42ca-9279-b63f2e587cf9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 55 · 2026-05-30T06:14:47.429Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011UsK4x1zstiTF4dp9KnCmd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.04238",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ad1c0e6-a355-42ca-9279-b63f2e587cf9",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d62f199-dc93-40bc-b641-30aa089b07fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 56 · 2026-05-30T06:14:48.362Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qh5RkNj8wjj5b9WXgyykLS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.03644",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d62f199-dc93-40bc-b641-30aa089b07fe",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27cf6dff-2b10-4272-a418-9350d6125f01",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 57 · 2026-05-30T06:14:48.834Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KsKTyqZJqokhmHcG8PHidF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.04532",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27cf6dff-2b10-4272-a418-9350d6125f01",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cdfcdc0-db41-4c43-9344-13781d1f3a34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 58 · 2026-05-30T06:14:49.997Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M3cKfKBaiFJCn2tYHcY5F6`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.464/",
  "prompt": "Extract the full title, authors, submission/publication date, and abstract of this paper (ViDoRAG)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cdfcdc0-db41-4c43-9344-13781d1f3a34",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYG9uBcMRzzQi72Gd8ic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a93a47d-20cf-4cfe-873f-8c81a403440e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2BGLzNH1PYJycbo5x15uj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 528,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 18415,
      "output_tokens": 524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 528,
          "output_tokens": 524,
          "cache_read_input_tokens": 18415,
          "cache_creation_input_tokens": 2016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2016,
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

_source line 59 · 2026-05-30T06:14:50.424Z_

<details><summary>↩ Tool result · `toolu_01RPKBLURU8nDdyopHHisXmW`</summary>

```text
# Paper Summary

**Full Title:** "The 1st EReL@MIR Workshop on Efficient Representation Learning for Multimodal Information Retrieval"

**Authors:** Junchen Fu, Xuri Ge, Xin Xin, Haitao Yu, Yue Feng, Alexandros Karatzoglou, Ioannis Arapakis, and Joemon M. Jose

**Submission Date:** April 21, 2025

**Abstract:** The paper describes a workshop addressing efficiency challenges in multimodal representation learning. Large foundation models like LLaMA, GPT, and CLIP have achieved strong performance in multimodal information retrieval tasks, yet their size creates "substantial obstacles to the practical adaptation" when deployed for IR applications. The workshop, held at Web Conference 2025, aims to bring together academic and industry researchers to "explore novel solutions, emerging problems, challenges, efficiency evaluation metrics and benchmarks" for achieving efficient multimodal representation learning in the era of foundation models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e3c2040-f837-4256-9aa0-967c1c189efd",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "99c86d6c-dc70-4792-a7db-c80dfd61f65a",
  "sourceToolAssistantUUID": "1e3c2040-f837-4256-9aa0-967c1c189efd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-30T06:14:50.764Z_

<details><summary>↩ Tool result · `toolu_01HW4ei4uJuybNQDt71jcSoq`</summary>

```text
# Paper Information

**Full Title:** "From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents"

**Authors:** Meftun Akarsu, Recep Kaan Karaman, Christopher Mierbach

**Submission Date:** April 2, 2026

**Abstract Summary:**

This research evaluates ten different retrieval methods for documents containing both text and tabular content. The authors tested their approaches on a financial question-answering dataset with over 23,000 queries. Their key finding reveals that "a two-stage pipeline combining hybrid retrieval with neural reranking achieves Recall@5 of 0.816 and MRR@3 of 0.605." Notably, the study challenges conventional wisdom by demonstrating that traditional BM25 keyword-based retrieval outperforms modern semantic search methods for financial documents. The researchers also determined that query expansion techniques provide minimal value for numerical precision tasks, while contextual retrieval consistently improves performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ad1c0e6-a355-42ca-9279-b63f2e587cf9",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "1f95b688-0dd8-4d27-b43d-8a1e0b6bc98a",
  "sourceToolAssistantUUID": "6ad1c0e6-a355-42ca-9279-b63f2e587cf9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-30T06:14:51.766Z_

<details><summary>↩ Tool result · `toolu_011UsK4x1zstiTF4dp9KnCmd`</summary>

```text
# Paper Summary

**Full Title:** "Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG"

**Authors:** Martin Asenov, Kenza Benkirane, Dan Goldwater, Aneiss Ghodsi

**Submission Date:** March 4, 2026

**Abstract:**

The researchers investigate retrieval-augmented generation (RAG) systems, comparing traditional lexical methods like BM25 against modern multimodal retrievers. They demonstrate that "better document representation is the primary driver of benchmark improvements" rather than superior retrieval mechanisms. By systematically adjusting transcription and preprocessing while keeping retrieval constant, they show BM25 can close performance gaps on multilingual and visual benchmarks. The authors conclude that evaluation frameworks should separately measure transcription and retrieval capabilities to accurately identify where progress genuinely occurs and where resources should be directed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d62f199-dc93-40bc-b641-30aa089b07fe",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "19013fc8-bfe4-4f8b-a3dd-677466443056",
  "sourceToolAssistantUUID": "9d62f199-dc93-40bc-b641-30aa089b07fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-30T06:14:52.734Z_

<details><summary>↩ Tool result · `toolu_01KsKTyqZJqokhmHcG8PHidF`</summary>

```text
# Paper Details

**Title:** "Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks"

**Authors:** Nathan Kuissi, Suraj Subrahmanyan, Nandan Thakur, Jimmy Lin

**Submission Date:** March 4, 2026

**Abstract Summary:**

The researchers investigated how temporal changes affect FreshStack, a retrieval benchmark for technical domains. By comparing corpus snapshots from October 2024 and October 2025, they found that nearly all queries from 2024 remained supported in 2025, with relevant documents migrating to competitor repositories. When evaluating retrieval models across both snapshots, they observed "only minor shifts in model rankings, with overall strong correlation of up to 0.978 Kendall τ at Recall@50." This suggests that retrieval benchmarks can maintain reliability even as their underlying corpora evolve over time. The team released all research artifacts publicly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cdfcdc0-db41-4c43-9344-13781d1f3a34",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "cead467b-e9e5-4415-ad25-ceedb83a8b00",
  "sourceToolAssistantUUID": "7cdfcdc0-db41-4c43-9344-13781d1f3a34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-30T06:14:53.022Z_

<details><summary>↩ Tool result · `toolu_01Qh5RkNj8wjj5b9WXgyykLS`</summary>

```text
# Paper Information

**Full Title:** "Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?"

**Authors:** Wenxuan Shen, Mingjia Wang, Yaochen Wang, Dongping Chen, Junjie Yang, Yao Wan, and Weiwei Lin

**Submission Date:** August 5, 2025

**Abstract:**

The researchers address evaluation gaps in Retrieval-Augmented Generation systems that employ Multimodal Large Language Models for document analysis. They present Double-Bench, "a new large-scale, multilingual, and multimodal evaluation system" comprising over 3,000 documents and 5,000 queries across six languages.

Key findings include: the performance gap between text and visual embedding models is shrinking, revealing a need for more robust document retrieval approaches. The study also identifies an "over-confidence dilemma within current document RAG frameworks that tend to provide answer even without evidence support."

The benchmark includes comprehensive testing of nine embedding models, four MLLMs, and four end-to-end frameworks, with plans for annual updates to maintain currency and prevent data contamination issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27cf6dff-2b10-4272-a418-9350d6125f01",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "d07475f2-ed48-45be-84d9-901f90dbc7b5",
  "sourceToolAssistantUUID": "27cf6dff-2b10-4272-a418-9350d6125f01",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-30T06:14:53.419Z_

<details><summary>↩ Tool result · `toolu_01M3cKfKBaiFJCn2tYHcY5F6`</summary>

```text
# ViDoRAG Paper Information

**Full Title:**
"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents"

**Authors:**
Qiuchen Wang, Ruixue Ding, Zehui Chen, Weiqi Wu, Shihang Wang, Pengjun Xie, and Feng Zhao

**Publication Date:**
November 2025

**Abstract Summary:**
The paper addresses challenges in applying RAG methods to visually rich documents. The researchers introduced ViDoSeek, a benchmark dataset for evaluating RAG on complex visual documents. They identified two key limitations in existing approaches: difficulty integrating textual and visual features, and insufficient reasoning token allocation. Their proposed ViDoRAG framework uses a "Gaussian Mixture Model (GMM)-based hybrid strategy" for multimodal retrieval and implements an iterative agent workflow with exploration, summarization, and reflection stages. The method achieved "over 10% improvement on the competitive ViDoSeek benchmark" compared to existing techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a93a47d-20cf-4cfe-873f-8c81a403440e",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "1302bf62-8370-4432-abbf-e16265a03ca9",
  "sourceToolAssistantUUID": "7a93a47d-20cf-4cfe-873f-8c81a403440e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-30T06:14:56.878Z_

Now let me search for more papers I haven't found yet - specifically VisRAG, DSE, and other important systems.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1302bf62-8370-4432-abbf-e16265a03ca9",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGAgE2aFP2o2EnaG6oV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "094f3ea1-ba3a-4a32-8b9f-b5cd188c3f45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjF4TA7TuLT47sTnAqTGBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 20431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 66 · 2026-05-30T06:14:57.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TahYK9zhQAmwzumSn21AH7`</summary>

```json
{
  "query": "VisRAG vision-based retrieval augmented generation ICLR 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "094f3ea1-ba3a-4a32-8b9f-b5cd188c3f45",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGAgE2aFP2o2EnaG6oV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dce0b15c-a929-499f-a3a5-2acbe664b98b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjF4TA7TuLT47sTnAqTGBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 20431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 67 · 2026-05-30T06:14:58.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014St3cfRRho2ZVuceKnYaBg`</summary>

```json
{
  "query": "Document Screenshot Embedding DSE visual document retrieval arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce0b15c-a929-499f-a3a5-2acbe664b98b",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGAgE2aFP2o2EnaG6oV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b977bd7a-6430-4770-8f8e-8b9bc7d588d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjF4TA7TuLT47sTnAqTGBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 20431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 68 · 2026-05-30T06:14:58.849Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KgqeAhnA4EmUpicp2LxvGc`</summary>

```json
{
  "query": "MIRACL-VISION multilingual visual document retrieval benchmark arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b977bd7a-6430-4770-8f8e-8b9bc7d588d9",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGAgE2aFP2o2EnaG6oV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "718c8237-8afb-4c4f-b8ef-6dfd8cc10e9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjF4TA7TuLT47sTnAqTGBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 20431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 69 · 2026-05-30T06:14:59.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WaXMWVwisDuLbB5rJsVvKH`</summary>

```json
{
  "query": "Jina-VDR visual document retrieval benchmark arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718c8237-8afb-4c4f-b8ef-6dfd8cc10e9d",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGAgE2aFP2o2EnaG6oV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ada3b8ce-4b16-447c-a6d8-f244a5699e88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjF4TA7TuLT47sTnAqTGBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 20431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 70 · 2026-05-30T06:15:04.545Z_

<details><summary>↩ Tool result · `toolu_01TahYK9zhQAmwzumSn21AH7`</summary>

```text
Web search results for query: "VisRAG vision-based retrieval augmented generation ICLR 2025 arxiv"

Links: [{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents | OpenReview","url":"https://openreview.net/forum?id=zG459X3Xge"},{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents","url":"https://arxiv.org/html/2410.10594v2"},{"title":"Published as a conference paper at ICLR 2025 VISRAG: VISION-BASED","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf"},{"title":"VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.09733"},{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality   Documents","url":"https://arxiv.org/pdf/2410.10594"},{"title":"Published as a conference paper at ICLR 2025 VISRAG: VISION-BASED","url":"https://openreview.net/pdf/b13eed287ec8fb31700414fded06f07db85891cd.pdf"},{"title":"Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook","url":"https://arxiv.org/html/2503.18016v1"},{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents | Request PDF","url":"https://www.researchgate.net/publication/384929416_VisRAG_Vision-based_Retrieval-augmented_Generation_on_Multi-modality_Documents"}]

Based on the search results, I found information about VisRAG. Here's what I found:

## VisRAG Overview

VisRAG presents Vision-based Retrieval-augmented Generation (VisRAG), which studies the feasibility of building a pure-vision RAG pipeline using VLMs. VisRAG is built with a VLM-based retriever VisRAG-Ret and generator VisRAG-Gen.

## Problem It Addresses

Current RAG systems are solely based on text, rendering it impossible to utilize vision information like layout and images that play crucial roles in real-world multi-modality documents. VisRAG tackles this issue by establishing a vision-language model (VLM)-based RAG pipeline where instead of first parsing the document to obtain text, the document is directly embedded using a VLM as an image and then retrieved to enhance the generation of a VLM.

## ICLR 2025 Publication

VisRAG was published as "Vision-based retrieval-augmented generation on multi-modality documents" at The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025.

## Performance Results

VisRAG outperforms traditional RAG in both the retrieval and generation stages, achieving a 20–40% end-to-end performance gain over traditional text-based RAG pipeline.

The paper is available on arXiv (2410.10594) and has been accepted as a conference paper at ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dce0b15c-a929-499f-a3a5-2acbe664b98b",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "79ef3c13-d826-475d-b4e0-0de1a27dcf36",
  "sourceToolAssistantUUID": "dce0b15c-a929-499f-a3a5-2acbe664b98b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-30T06:15:05.305Z_

<details><summary>↩ Tool result · `toolu_01KgqeAhnA4EmUpicp2LxvGc`</summary>

```text
Web search results for query: "MIRACL-VISION multilingual visual document retrieval benchmark arxiv 2025"

Links: [{"title":"MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250511651O/abstract"},{"title":"[2505.11651v2] MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark","url":"http://arxiv.org/abs/2505.11651v2"},{"title":"[2505.11651] MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark","url":"https://arxiv.org/abs/2505.11651"},{"title":"Paper page - MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark","url":"https://huggingface.co/papers/2505.11651"},{"title":"MIRACL-VISION: A Large, multilingual, visual document retrieval ...","url":"https://bytez.com/docs/arxiv/2505.11651/paper"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/html/2602.19961v1"},{"title":"nvidia/miracl-vision · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nvidia/miracl-vision"},{"title":"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models","url":"https://arxiv.org/html/2509.15432"}]

Based on the search results, here's what I found about MIRACL-VISION:

## Overview

MIRACL-VISION is a challenging, representative, multilingual evaluation benchmark for visual retrieval pipelines. MIRACL-VISION covers 18 languages, and is an extension of the MIRACL dataset, a popular benchmark to evaluate text-based multilingual retrieval pipelines.

## Purpose and Context

Document retrieval is an important task for search and Retrieval-Augmented Generation (RAG) applications. Large Language Models (LLMs) have contributed to improving the accuracy of text-based document retrieval. However, documents with complex layout and visual elements like tables, charts and infographics are not perfectly represented in textual format. Recently, image-based document retrieval pipelines have become popular, which use visual large language models (VLMs) to retrieve relevant page images given a query.

## Key Findings

The research reveals significant performance gaps: a gap in state-of-the-art VLM-based embedding models on multilingual capabilities, with up to 59.7% lower retrieval accuracy than text-based retrieval models. Even for the English language, the visual models retrieval accuracy is 12.1% lower compared to text-based models.

The paper was published on arXiv in May 2025 (arxiv:2505.11651).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "718c8237-8afb-4c4f-b8ef-6dfd8cc10e9d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "0f7e6266-4a2a-44a9-b325-778d1681bd76",
  "sourceToolAssistantUUID": "718c8237-8afb-4c4f-b8ef-6dfd8cc10e9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-30T06:15:05.443Z_

<details><summary>↩ Tool result · `toolu_014St3cfRRho2ZVuceKnYaBg`</summary>

```text
Web search results for query: "Document Screenshot Embedding DSE visual document retrieval arxiv"

Links: [{"title":"[2406.11251] Unifying Multimodal Retrieval via Document Screenshot Embedding","url":"https://arxiv.org/abs/2406.11251"},{"title":"Unifying Multimodal Retrieval via Document Screenshot Embedding","url":"https://arxiv.org/pdf/2406.11251"},{"title":"Unifying Multimodal Retrieval via Document Screenshot Embedding","url":"https://arxiv.org/html/2406.11251v1"},{"title":"Papers Explained 313: Document Screenshot Embedding | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-313-document-screenshot-embedding-792cb286643c"},{"title":"Unifying Multimodal Retrieval via Document Screenshot ...","url":"https://aclanthology.org/2024.emnlp-main.373.pdf"},{"title":"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/html/2501.16902"},{"title":"Xueguang Ma on X: \"Introducing Document Screenshot Embedding (DSE): a new retrieval paradigm that unifies various formats and modalities into a single form for direct document encoding. paper: https://t.co/wLptH9zzOr work done with amazing co-authors: @jacklin_64 @alexlimh23 @WenhuChen @lintool https://t.co/uVtnHzx7fv\" / X","url":"https://x.com/xueguang_ma/status/1803093148589318508"},{"title":"Roles of MLLMs in Visually Rich Document Retrieval for RAG: A Survey","url":"https://arxiv.org/pdf/2601.03262"}]

I found the research paper you're looking for. Here's what I found:

## Document Screenshot Embedding (DSE)

Document Screenshot Embedding (DSE) is a novel retrieval paradigm that regards document screenshots as a unified input format, which does not require any content extraction preprocess and preserves all the information in a document (e.g., text, image and layout). DSE leverages a large vision-language model to directly encode document screenshots into dense representations for retrieval.

### Key Features

Unlike the texts and images extracted from a document, screenshots are easy to obtain. More importantly, screenshots naturally preserve all the information in a document.

### Performance

DSE outperforms BM25 by 17 points in top-1 retrieval accuracy. Additionally, in a mixed-modality task of slide retrieval, DSE significantly outperforms OCR text retrieval methods by over 15 points in nDCG@10.

### Paper Details

The paper is available on arXiv at **arxiv.org/abs/2406.11251** and was authored by Xueguang Ma, Sheng-Chieh Lin, Minghan Li, Wenhu Chen, and Jimmy Lin from the University of Waterloo. The researchers crafted the Wiki-SS dataset, a 1.3M Wikipedia web page screenshots as the corpus to answer the questions from the Natural Questions dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b977bd7a-6430-4770-8f8e-8b9bc7d588d9",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "2fb4631f-dda0-4c6c-8061-efea871965a1",
  "sourceToolAssistantUUID": "b977bd7a-6430-4770-8f8e-8b9bc7d588d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-30T06:15:06.124Z_

<details><summary>↩ Tool result · `toolu_01WaXMWVwisDuLbB5rJsVvKH`</summary>

```text
Web search results for query: "Jina-VDR visual document retrieval benchmark arxiv 2025"

Links: [{"title":"JinaVDR: New Visual Document Retrieval Benchmark with 95 Tasks in 20 Languages","url":"https://jina.ai/news/jinavdr-new-visual-document-retrieval-benchmark-with-95-tasks-in-20-languages/"},{"title":"[2506.18902v3] jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://arxiv.org/abs/2506.18902v3"},{"title":"[2506.18902] jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://arxiv.org/abs/2506.18902"},{"title":"GitHub - jina-ai/jina-vdr: Jina VDR is a multilingual, multi-domain benchmark for visual document retrieval · GitHub","url":"https://github.com/jina-ai/jina-vdr"},{"title":"Unlocking Multimodal Document Intelligence:","url":"https://arxiv.org/pdf/2602.19961"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/html/2602.19961v1"},{"title":"arXiv:2506.18902v2 [cs.AI] 24 Jun 2025","url":"https://www.arxiv.org/pdf/2506.18902v2"},{"title":"jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://arxiv.org/html/2506.18902v2"},{"title":"NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval","url":"https://arxiv.org/html/2603.12824"}]

Based on the search results, here's what I found about Jina-VDR:

## Overview

JinaVDR is a benchmark providing an evaluation framework spanning 95 tasks across 20 languages, including domain-diverse and layout-rich documents like charts, maps, traditional scanned documents, Markdown files, and complex tables.

## Key Features

JinaVDR encompasses multilingual documents with intricate layouts—combining graphs, charts, tables, text, and images alongside scanned copies and screenshots, and pairs these diverse visual documents with targeted text queries for comprehensive evaluation of retrieval performance.

Jina-VDR utilizes over 70k documents, reflecting a trend toward scaling both query volume and corpus diversity.

## ArXiv Connection

The Jina-VDR benchmark was introduced to facilitate evaluation of visual document retrieval capabilities and is specifically designed for visually rich image retrieval. The benchmark is described in the arXiv paper "jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval" (arXiv:2506.18902).

## Significance

Jina-VDR represents a significant shift in supporting 20 languages, addressing the gap in multilingual visual document retrieval benchmarks that were previously predominantly English-centric.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada3b8ce-4b16-447c-a6d8-f244a5699e88",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "0b8f6028-6df4-47ac-b99a-dd85b3bb968b",
  "sourceToolAssistantUUID": "ada3b8ce-4b16-447c-a6d8-f244a5699e88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-30T06:15:09.224Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L8eH1pBc5rRXURoVXCYXsV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.10594",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8f6028-6df4-47ac-b99a-dd85b3bb968b",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGBcXJrA4kVYYSrsbkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d2083bc-9215-43de-91ef-d9f692f34421",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvbAFeSdqF8th2g18Pt4UL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3521,
      "cache_read_input_tokens": 23005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3521,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-30T06:15:09.703Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JuqQc6yynkbSGx5bVi6TVa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.11251",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d2083bc-9215-43de-91ef-d9f692f34421",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGBcXJrA4kVYYSrsbkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cbab782-c7f9-4df3-9c36-c13295593518",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvbAFeSdqF8th2g18Pt4UL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3521,
      "cache_read_input_tokens": 23005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3521,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-30T06:15:10.716Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S9UpuU5yv4XTU4kggWgt3c`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11651",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbab782-c7f9-4df3-9c36-c13295593518",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGBcXJrA4kVYYSrsbkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "041b3374-6c79-4e94-bffd-9982c8b425c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvbAFeSdqF8th2g18Pt4UL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3521,
      "cache_read_input_tokens": 23005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3521,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-30T06:15:11.186Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TWmdyhBvK6PbMMwNm6nZs8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18902",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "041b3374-6c79-4e94-bffd-9982c8b425c4",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGBcXJrA4kVYYSrsbkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d94352fb-d252-46a3-8d92-edfcc0aa2ca5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvbAFeSdqF8th2g18Pt4UL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3521,
      "cache_read_input_tokens": 23005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3521,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-30T06:15:12.273Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PjzaHeRhQw9CvH47QN1M6W`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.09733",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (VisRAG 2.0)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94352fb-d252-46a3-8d92-edfcc0aa2ca5",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGBcXJrA4kVYYSrsbkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93d33ce4-e944-4b62-bc87-7abc7b716950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvbAFeSdqF8th2g18Pt4UL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3521,
      "cache_read_input_tokens": 23005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3521,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-30T06:15:12.763Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PCnHY28kfbg7aL3SGeDf5x`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.12824",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (NanoVDR)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93d33ce4-e944-4b62-bc87-7abc7b716950",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGBcXJrA4kVYYSrsbkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa31679e-9c58-4beb-b3cb-91c8c1b98bcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvbAFeSdqF8th2g18Pt4UL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3521,
      "cache_read_input_tokens": 23005,
      "output_tokens": 514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3521
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 514,
          "cache_read_input_tokens": 23005,
          "cache_creation_input_tokens": 3521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3521,
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

_source line 80 · 2026-05-30T06:15:13.216Z_

<details><summary>↩ Tool result · `toolu_01L8eH1pBc5rRXURoVXCYXsV`</summary>

```text
# VisRAG Paper Summary

**Full Title:** "VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents"

**Authors:** Shi Yu, Chaoyue Tang, Bokai Xu, Junbo Cui, Junhao Ran, Yukun Yan, Zhenghao Liu, Shuo Wang, Xu Han, Zhiyuan Liu, and Maosong Sun

**Submission Date:** October 14, 2024 (with revision on March 2, 2025)

**Abstract Summary:**
The researchers present VisRAG, a system that enhances retrieval-augmented generation by leveraging vision capabilities. Rather than converting documents to text first, their approach directly embeds documents as images using vision-language models. This technique preserves layout and visual information that traditional text-based systems lose during parsing. Testing showed the method achieved "20--40% end-to-end performance gain over traditional text-based RAG pipeline." The team has released their code and training data publicly to support further research in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d2083bc-9215-43de-91ef-d9f692f34421",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "32d9ca30-8cac-4ed3-8888-f83746b3137d",
  "sourceToolAssistantUUID": "8d2083bc-9215-43de-91ef-d9f692f34421",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-30T06:15:13.564Z_

<details><summary>↩ Tool result · `toolu_01JuqQc6yynkbSGx5bVi6TVa`</summary>

```text
# Paper Information

**Title:** "Unifying Multimodal Retrieval via Document Screenshot Embedding"

**Authors:** Xueguang Ma, Sheng-Chieh Lin, Minghan Li, Wenhu Chen, Jimmy Lin

**Submission Date:** June 17, 2024 (v1); December 2, 2024 (v2)

**Abstract:** 
The researchers introduce Document Screenshot Embedding (DSE), a retrieval approach that treats document screenshots as unified input rather than requiring separate parsing for different formats. This method employs a large vision-language model to encode document screenshots into dense representations. The team evaluated DSE using Wiki-SS, a dataset of 1.3M Wikipedia web page screenshots paired with Natural Questions queries. Results show DSE outperformed BM25 by 17 points in top-1 accuracy for text-heavy documents and exceeded OCR-based methods by over 15 points in nDCG@10 for mixed-modality slide retrieval tasks. The approach preserves all document information including text, images, and layout without preprocessing loss.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cbab782-c7f9-4df3-9c36-c13295593518",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "c58a1e3b-2855-46f3-8127-6533720808ac",
  "sourceToolAssistantUUID": "1cbab782-c7f9-4df3-9c36-c13295593518",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-30T06:15:14.771Z_

<details><summary>↩ Tool result · `toolu_01S9UpuU5yv4XTU4kggWgt3c`</summary>

```text
# MIRACL-VISION Paper Summary

**Full Title:** "MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark"

**Authors:** Radek Osmulski, Gabriel de Souza P. Moreira, Ronay Ak, Mengyao Xu, Benedikt Schifferer, Even Oldridge

**Submission Date:** May 16, 2025 (v1); revised May 21, 2025 (v2)

**Abstract:**
This research introduces a multilingual evaluation resource for visual document retrieval, covering 18 languages. The work extends the existing MIRACL dataset by incorporating document images alongside traditional text-based retrieval methods. The authors employed techniques to reduce corpus size while maintaining challenge level by filtering out "easy" negative examples. Their experiments revealed significant performance gaps: visual language models underperformed text-based systems by approximately 60% on non-English tasks and 12% on English content. The benchmark aims to support development of more effective image-based document retrieval systems, particularly for handling complex layouts and visual elements like tables and charts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "041b3374-6c79-4e94-bffd-9982c8b425c4",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "4493678f-6c6b-46cc-b301-6049456ab559",
  "sourceToolAssistantUUID": "041b3374-6c79-4e94-bffd-9982c8b425c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-30T06:15:16.989Z_

<details><summary>↩ Tool result · `toolu_01PjzaHeRhQw9CvH47QN1M6W`</summary>

```text
# VisRAG 2.0 Paper Information

**Full Title:** "VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation"

**Authors:** Yubo Sun, Chunyi Peng, Yukun Yan, Shi Yu, Zhenghao Liu, Chi Chen, Zhiyuan Liu, and Maosong Sun

**Submission Date:** October 10, 2025

**Abstract Summary:**

This research introduces a framework designed to enhance vision-language models by incorporating external visual knowledge. The system addresses limitations in current approaches through an evidence-focused methodology. The paper describes a model that "first observes retrieved images and records per-image evidence, then derives the final answer from the aggregated evidence." 

The researchers also present a novel training technique called Reward-Scoped Group Relative Policy Optimization that connects granular rewards to specific tokens. Testing across multiple visual question-answering benchmarks revealed substantial improvements, with "27% improvements on average" compared to baseline performance. The work demonstrates that the approach excels at identifying and integrating relevant visual information across multiple images to generate accurate responses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93d33ce4-e944-4b62-bc87-7abc7b716950",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "24c0ef90-752b-471e-bebe-e3cfbe09c87b",
  "sourceToolAssistantUUID": "93d33ce4-e944-4b62-bc87-7abc7b716950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-30T06:15:17.020Z_

<details><summary>↩ Tool result · `toolu_01TWmdyhBvK6PbMMwNm6nZs8`</summary>

```text
# Paper Summary

**Full Title:** "jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval"

**Authors:** Michael Günther, Saba Sturua, Mohammad Kalim Akram, Isabelle Mohr, Andrei Ungureanu, Bo Wang, Sedigheh Eslami, Scott Martens, Maximilian Werk, Nan Wang, and Han Xiao

**Submission Date:** June 23, 2025 (v1); last revised July 7, 2025 (v3)

**Abstract:**

The researchers introduce a 3.8 billion parameter multimodal embedding model that "unifies text and image representations through a novel architecture" supporting both single and multi-vector embeddings. The system incorporates task-specific Low-Rank Adaptation adapters to enhance performance across retrieval scenarios including query-document matching, semantic similarity, and code search. The model demonstrates strong capabilities in processing "visually rich content such as tables, charts, diagrams, and mixed-media formats." The team also created a new benchmark called Jina-VDR designed specifically for evaluating visually rich image retrieval tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d94352fb-d252-46a3-8d92-edfcc0aa2ca5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "51ec72a2-53d4-4216-99c8-b6b201fd2a95",
  "sourceToolAssistantUUID": "d94352fb-d252-46a3-8d92-edfcc0aa2ca5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-30T06:15:17.432Z_

<details><summary>↩ Tool result · `toolu_01PCnHY28kfbg7aL3SGeDf5x`</summary>

```text
# NanoVDR Paper Details

**Full Title:** "NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval"

**Authors:** Zhuchenyang Liu, Yao Zhang, Yu Xiao

**Submission Date:** March 13, 2026 (v1); Last revised May 27, 2026 (v2)

**Abstract Summary:**
The research addresses inefficiencies in vision-language model-based document retrieval systems. Rather than using identical multi-billion parameter encoders for both documents and queries, the team proposes an asymmetric approach. A frozen 2-billion parameter vision-language model indexes documents offline, while a significantly smaller 69-million parameter text-only model encodes search queries during inference. 

Key findings include that pointwise cosine alignment on query text consistently outperforms alternative training objectives. The team also identified and resolved cross-lingual transfer challenges through machine translation data augmentation. The final NanoVDR-S-Multi model achieves "95.1% of teacher quality" while delivering "32× fewer parameters and 50× lower CPU query latency," using minimal training resources under 13 GPU-hours.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa31679e-9c58-4beb-b3cb-91c8c1b98bcb",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "f163dc9e-7a81-469f-a6a0-55930ab66128",
  "sourceToolAssistantUUID": "fa31679e-9c58-4beb-b3cb-91c8c1b98bcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-30T06:15:19.653Z_

Let me search for additional relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f163dc9e-7a81-469f-a6a0-55930ab66128",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGCSt9z9B9mtF8uCFiV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b966cf3-421e-4dfe-8e8e-d79ddd129dec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016efJB4CVQhsge2sHA1eNq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 26526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2207,
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

_source line 87 · 2026-05-30T06:15:20.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01588WkL5mDMsqPpZYAs5K6r`</summary>

```json
{
  "query": "ColQwen2 visual document retrieval late interaction arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b966cf3-421e-4dfe-8e8e-d79ddd129dec",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGCSt9z9B9mtF8uCFiV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd5eab83-c09f-4f70-99e6-48b9ecbfab4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016efJB4CVQhsge2sHA1eNq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 26526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2207,
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

_source line 88 · 2026-05-30T06:15:21.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01To5gdeoUQHw3f5k4gkzAfQ`</summary>

```json
{
  "query": "MoLoRAG multi-modal logic-aware retrieval document understanding arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd5eab83-c09f-4f70-99e6-48b9ecbfab4f",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGCSt9z9B9mtF8uCFiV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa9d4d5d-8189-4b20-baf6-72110854f4d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016efJB4CVQhsge2sHA1eNq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 26526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2207,
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

_source line 89 · 2026-05-30T06:15:22.118Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015x317zJ6oGKaxWwK6RX4aE`</summary>

```json
{
  "query": "VisR-Bench visual retrieval benchmark long visually rich documents arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa9d4d5d-8189-4b20-baf6-72110854f4d1",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGCSt9z9B9mtF8uCFiV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2aefd60-29d9-44b6-9603-cabf0e2a7602",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016efJB4CVQhsge2sHA1eNq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 26526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2207,
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

_source line 90 · 2026-05-30T06:15:22.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GwBkjgFfHDKseGzVwcCmTZ`</summary>

```json
{
  "query": "Docs2Synth synthetic data document retrieval arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2aefd60-29d9-44b6-9603-cabf0e2a7602",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGCSt9z9B9mtF8uCFiV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e8c870d-4f68-4a9c-8d8f-6450db0dc33a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016efJB4CVQhsge2sHA1eNq7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 26526,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2207
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 26526,
          "cache_creation_input_tokens": 2207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2207,
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

_source line 91 · 2026-05-30T06:15:28.392Z_

<details><summary>↩ Tool result · `toolu_015x317zJ6oGKaxWwK6RX4aE`</summary>

```text
Web search results for query: "VisR-Bench visual retrieval benchmark long visually rich documents arxiv"

Links: [{"title":"VisR-Bench: A Visual Retrieval Benchmark for Visually-Rich Documents | OpenReview","url":"https://openreview.net/forum?id=No8PAJEyeG"},{"title":"VisR-Bench: An Empirical Study on Visual Retrieval-Augmented Generation for Multilingual Long Document Understanding","url":"https://arxiv.org/html/2508.07493v2"},{"title":"[2508.07493] VisR-Bench: An Empirical Study on Visual Retrieval-Augmented Generation for Multilingual Long Document Understanding","url":"https://arxiv.org/abs/2508.07493"},{"title":"Paper page - VisR-Bench: An Empirical Study on Visual Retrieval-Augmented Generation for Multilingual Long Document Understanding","url":"https://huggingface.co/papers/2508.07493"},{"title":"VISR-BENCH: A VISUAL RETRIEVAL BENCHMARK FOR ...","url":"https://openreview.net/pdf?id=No8PAJEyeG"},{"title":"Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG","url":"https://arxiv.org/html/2603.04238"},{"title":"GitHub - puar-playground/VisR-Bench: VisR-Bench: A Multilingual Visual Retrieval Benchmark for Long Documents · GitHub","url":"https://github.com/puar-playground/VisR-Bench"},{"title":"Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy","url":"https://arxiv.org/html/2510.22215"}]

Based on the search results, here's what I found about VisR-Bench:

## Overview

VisR-Bench is the first question-driven multilingual Visual Retrieval benchmark designed to evaluate MLLM retrieval performance in visually rich document images.

## Dataset Details

VisR-Bench consists of 53K high-quality synthetic QA pairs and 1,286 documents (373 English and 913 multilingual), with an average length of about eighteen pages. The benchmark spans sixteen languages with three question types (figures, text, and tables), offering diverse linguistic and question coverage.

## Key Features

By generating QA pairs for different evidence types, tables, figures, and visual text, the benchmark enables granular performance analysis in multimodal reasoning, OCR robustness, and table understanding. Additionally, queries do not contain explicit answers, preventing models from relying on superficial keyword matching.

## Evaluation Results

Results show that while MLLMs significantly outperform text-based and multimodal encoder models, they still struggle with structured tables and low-resource languages, highlighting key challenges in multilingual visual retrieval.

The paper is available on arXiv (2508.07493) and the code is available on GitHub at the repository referenced in the results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2aefd60-29d9-44b6-9603-cabf0e2a7602",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "31481c68-f560-4266-99fb-17646ccf620e",
  "sourceToolAssistantUUID": "c2aefd60-29d9-44b6-9603-cabf0e2a7602",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-30T06:15:30.315Z_

<details><summary>↩ Tool result · `toolu_01588WkL5mDMsqPpZYAs5K6r`</summary>

```text
Web search results for query: "ColQwen2 visual document retrieval late interaction arxiv 2024 2025"

Links: [{"title":"Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"https://arxiv.org/html/2505.07730v1"},{"title":"An Overview of Late Interaction Retrieval Models: ColBERT, ColPali, and ColQwen | Weaviate","url":"https://weaviate.io/blog/late-interaction-overview"},{"title":"[2602.03992] Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval","url":"https://arxiv.org/abs/2602.03992"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.03992"},{"title":"Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model","url":"https://arxiv.org/html/2603.28554v2"},{"title":"Exploration of Augmentation Strategies in Multi-modal ...","url":"https://arxiv.org/pdf/2512.16802"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction embedding models for Visual Document Retrieval","url":"https://arxiv.org/html/2602.03992v1"}]

Based on the search results, here's what I found about ColQwen2 visual document retrieval with late interaction:

## ColQwen2 Overview

ColQwen stands for Contextualized Late Interaction over Qwen2 (also called ColQwen2). ColQwen is a multimodal late interaction retrieval model that uses vision language models (VLMs) instead of text-only models.

## Key Characteristics

Unlike conventional approaches to PDF retrieval that require Optical Character Recognition (OCR) and advanced chunking, ColQwen treats the entire PDF as an image. ColQwen2 leverages the Qwen2-VL-2B backbone and adopts a multi-vector retrieval scheme with adapters.

## Late Interaction Mechanism

Late interaction involves dynamically selecting and weighting fine-grained vectors based on the query context, substantially enhancing VDR effectiveness on the ViDoRe benchmark.

## Recent Research

A recent reproducibility study from May 2025 found that ColQwen2's performance drops by 85.1% on larger token datasets when using only non-lexical query token matching, and 39.9% on lexical query token matching, demonstrating the importance of both matching types for effective retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd5eab83-c09f-4f70-99e6-48b9ecbfab4f",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "3f54e2a2-e750-427e-b600-cc4cecac2944",
  "sourceToolAssistantUUID": "fd5eab83-c09f-4f70-99e6-48b9ecbfab4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-30T06:15:30.347Z_

<details><summary>↩ Tool result · `toolu_01GwBkjgFfHDKseGzVwcCmTZ`</summary>

```text
Web search results for query: "Docs2Synth synthetic data document retrieval arxiv 2025"

Links: [{"title":"[2601.12260] Docs2Synth: A Synthetic Data Trained Retriever Framework for Scanned Visually Rich Documents Understanding","url":"https://arxiv.org/abs/2601.12260"},{"title":"Docs2Synth: A Synthetic Data Trained Retriever Framework for Scanned Visually Rich Documents Understanding","url":"https://arxiv.org/html/2601.12260"},{"title":"Docs2Synth: A Synthetic Data Trained Retriever Framework for Scanned Visually Rich Documents Understanding","url":"https://arxiv.org/pdf/2601.12260"},{"title":"[2502.17957] On Synthetic Data Strategies for Domain-Specific Generative Retrieval","url":"https://arxiv.org/abs/2502.17957"},{"title":"Source2Synth: Synthetic Data Generation and Curation Grounded in Real Data Sources","url":"https://arxiv.org/html/2409.08239v2"},{"title":"Information Retrieval Feb 2025","url":"https://www.arxiv.org/list/cs.IR/2025-02?skip=300&show=50"}]

Based on the search results, here's what I found:

Docs2Synth is a synthetic-supervision framework that enables retrieval-guided inference for private and low-resource domains. It automatically processes raw document collections, generates and verifies diverse QA pairs via an agent-based system, and trains a lightweight visual retriever to extract domain-relevant evidence.

The framework addresses challenges in document understanding for regulated domains, where scanned documents often contain sensitive, evolving, and domain-specific knowledge, leading to a lack of manual annotations for model adaptation and difficulty for pretrained models to stay up-to-date with domain-specific facts.

During inference, the retriever collaborates with a multimodal large language model through an iterative retrieval-generation loop, reducing hallucination and improving response consistency. Experiments on multiple visually rich document understanding benchmarks show that Docs2Synth substantially enhances grounding and domain generalization without requiring human annotations.

The paper was published on arXiv in January 2026 (arxiv ID: 2601.12260) and includes an open-source implementation available at their project website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e8c870d-4f68-4a9c-8d8f-6450db0dc33a",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "1917b85c-c109-4063-a61c-13d0b4f5e7ed",
  "sourceToolAssistantUUID": "3e8c870d-4f68-4a9c-8d8f-6450db0dc33a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-30T06:15:33.056Z_

<details><summary>↩ Tool result · `toolu_01To5gdeoUQHw3f5k4gkzAfQ`</summary>

```text
Web search results for query: "MoLoRAG multi-modal logic-aware retrieval document understanding arxiv"

Links: [{"title":"[2509.07666] MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval","url":"https://arxiv.org/abs/2509.07666"},{"title":"MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval","url":"https://arxiv.org/html/2509.07666v1"},{"title":"Paper page - MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval","url":"https://huggingface.co/papers/2510.09510"},{"title":"MoLoRAG: Bootstrapping Document Understanding via ...","url":"https://aclanthology.org/2025.emnlp-main.708.pdf"},{"title":"MoLoRAG: Bootstrapping Document Understanding","url":"https://arxiv.org/pdf/2509.07666"},{"title":"[2602.10271] MLDocRAG: Multimodal Long-Context Document Retrieval Augmented Generation","url":"https://arxiv.org/abs/2602.10271"}]

Based on the search results, here's what I found about MoLoRAG:

## Overview

MoLoRAG is a logic-aware retrieval framework for multi-modal, multi-page document understanding. The paper was published on arXiv in September 2025 (arxiv ID: 2509.07666).

## Problem and Motivation

Traditional methods convert documents into text for processing by Large Language Models (LLMs), but this process strips away critical multi-modal information like figures. While Large Vision-Language Models (LVLMs) address this limitation, their constrained input size makes multi-page document comprehension infeasible. Retrieval-augmented generation (RAG) methods mitigate this by selecting relevant pages, but they rely solely on semantic relevance, ignoring logical connections between pages and the query, which is essential for reasoning.

## Approach

MoLoRAG is a graph-based retrieval framework that first constructs a page graph to represent the dependencies between pages, and a lightweight VLM serves as the retrieval engine, reasoning over this graph through traversal to identify logically relevant pages. Both semantic and logical relevance are combined into a unified similarity score to re-rank pages, enabling a more comprehensive retrieval process.

## Performance

MoLoRAG demonstrates superior ability to assess logical relevance. The framework shows effectiveness in handling both Document Question Answering (DocQA) tasks across multiple multi-modal document benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa9d4d5d-8189-4b20-baf6-72110854f4d1",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "38fc1863-9b88-4af0-bcd1-e49178e42cec",
  "sourceToolAssistantUUID": "fa9d4d5d-8189-4b20-baf6-72110854f4d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-30T06:15:36.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ErCuMQ4RyGUyMoqAdtqtgY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.07666",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38fc1863-9b88-4af0-bcd1-e49178e42cec",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGDbhzkcpJW32LCRKuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f7f0ec9-ff6f-4e02-8f7b-fcdcec434aad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feSv6hTeGs3fpsS9Drr68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1376,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 96 · 2026-05-30T06:15:37.258Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ST2nWTnVzL6iC6mswvPZuZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.07493",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f7f0ec9-ff6f-4e02-8f7b-fcdcec434aad",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGDbhzkcpJW32LCRKuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baf126fc-38cc-472f-905e-319c011d003f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feSv6hTeGs3fpsS9Drr68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1376,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 97 · 2026-05-30T06:15:37.733Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PnA8PzUFMbH6Stcqt4NyKX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.12260",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baf126fc-38cc-472f-905e-319c011d003f",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGDbhzkcpJW32LCRKuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffef1c26-b307-4ece-995f-0f0e17b69545",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feSv6hTeGs3fpsS9Drr68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1376,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 98 · 2026-05-30T06:15:38.729Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Tkbqamstd7wzXe8FFX82Ee`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.28554",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (Hydra)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffef1c26-b307-4ece-995f-0f0e17b69545",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGDbhzkcpJW32LCRKuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29add9b8-c277-466c-9686-ea5ff063dac3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feSv6hTeGs3fpsS9Drr68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1376,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 99 · 2026-05-30T06:15:39.673Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012cY2dTMJyc1SBVuZTuoRZJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.10271",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (MLDocRAG)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29add9b8-c277-466c-9686-ea5ff063dac3",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGDbhzkcpJW32LCRKuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34674bb0-635a-4967-a597-0128ebdcb26c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feSv6hTeGs3fpsS9Drr68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1376,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 100 · 2026-05-30T06:15:40.136Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016VThjsN1TpdiyKqyLAPW7D`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.22215",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (Hybrid-Vector Retrieval)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34674bb0-635a-4967-a597-0128ebdcb26c",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGDbhzkcpJW32LCRKuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c350eec-bf2c-489c-ab9e-889fcd6cc929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013feSv6hTeGs3fpsS9Drr68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1376,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 28733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 101 · 2026-05-30T06:15:40.818Z_

<details><summary>↩ Tool result · `toolu_01ErCuMQ4RyGUyMoqAdtqtgY`</summary>

```text
# MoLoRAG Paper Details

**Title:** "MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval"

**Authors:** Xixi Wu, Yanchao Tan, Nan Hou, Ruiyang Zhang, Hong Cheng

**Submission Date:** September 6, 2025

**Abstract Summary:**

The paper addresses limitations in multi-page document comprehension by proposing a retrieval system that combines semantic and logical relevance. The researchers note that while Large Vision-Language Models can process multi-modal information, their input constraints make handling lengthy documents impractical.

The proposed framework constructs a page graph capturing contextual relationships, enabling a lightweight vision model to traverse and identify relevant pages including those with logical connections. The authors report results showing "average improvements of 9.68% in accuracy over LVLM direct inference and 7.44% in retrieval precision over baselines" across four document question-answering datasets.

The work offers both training-free and fine-tuned variants for flexibility, with implementations made publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f7f0ec9-ff6f-4e02-8f7b-fcdcec434aad",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "0e2677a1-2145-4887-9747-43dbe2196b0f",
  "sourceToolAssistantUUID": "5f7f0ec9-ff6f-4e02-8f7b-fcdcec434aad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-30T06:15:41.404Z_

<details><summary>↩ Tool result · `toolu_01ST2nWTnVzL6iC6mswvPZuZ`</summary>

```text
# VisR-Bench Paper Details

**Full Title:** VisR-Bench: An Empirical Study on Visual Retrieval-Augmented Generation for Multilingual Long Document Understanding

**Authors:** Jian Chen, Ming Li, Jihyung Kil, Chenguang Wang, Tong Yu, Ryan Rossi, Tianyi Zhou, Changyou Chen, Ruiyi Zhang

**Submission Date:** August 10, 2025 (v1); last revised August 25, 2025 (v2)

**Abstract Summary:**
The paper addresses a gap in existing benchmarks by introducing VisR-Bench, which focuses on "question-driven multimodal retrieval in long documents" across multiple languages. The benchmark contains approximately 35,000 question-answer pairs from 1,200 documents, covering sixteen languages and three question types (figures, text, and tables). A key innovation involves queries designed to prevent "models from relying on superficial keyword matching." The evaluation reveals that multimodal language models substantially outperform text-based approaches, though they demonstrate limitations when handling "structured tables and low-resource languages."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf126fc-38cc-472f-905e-319c011d003f",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "86c20966-ffee-4c99-90e2-cec7e85d2cee",
  "sourceToolAssistantUUID": "baf126fc-38cc-472f-905e-319c011d003f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-30T06:15:42.852Z_

<details><summary>↩ Tool result · `toolu_01PnA8PzUFMbH6Stcqt4NyKX`</summary>

```text
# Paper Information

**Full Title:** "Docs2Synth: A Synthetic Data Trained Retriever Framework for Scanned Visually Rich Documents Understanding"

**Authors:** Yihao Ding, Qiang Sun, Puzhen Wu, Sirui Li, Siwen Luo, Wei Liu

**Submission Date:** January 18, 2026

**Abstract:**

The paper addresses document understanding challenges in regulated sectors where scanned materials contain sensitive, changing, and specialized knowledge. The framework tackles two core problems: insufficient annotated training data and outdated domain knowledge in pretrained models.

The proposed approach combines strengths from different model types. While multimodal language models excel at zero-shot tasks, they tend to generate false information; vision-language models offer accuracy but demand expensive manual labeling for new domains.

Docs2Synth solves this through an automated pipeline that processes document collections, creates and validates question-answer pairs using agents, and trains a compact visual retriever to identify relevant evidence. At inference time, the retriever works alongside a language model through iterative back-and-forth interactions, minimizing errors and improving reliability. The authors package this as accessible Python software for practical deployment across varied applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffef1c26-b307-4ece-995f-0f0e17b69545",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "a831e79f-09e3-4730-a559-5049293184a4",
  "sourceToolAssistantUUID": "ffef1c26-b307-4ece-995f-0f0e17b69545",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-30T06:15:42.910Z_

<details><summary>↩ Tool result · `toolu_01Tkbqamstd7wzXe8FFX82Ee`</summary>

```text
# Hydra Paper Details

**Full Title:** "Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model"

**Author:** Athos Georgiou

**Submission Date:** March 30, 2026 (v1); latest revision April 19, 2026 (v3)

**Abstract Summary:**
The paper addresses inefficiency in visual document processing by proposing a unified architecture. Rather than deploying separate retrieval and generation systems, Hydra combines both capabilities through a dual-head design. The approach uses a LoRA adapter that toggles between modes: enabling it generates multi-vector embeddings for retrieval tasks, while disabling it restores the base model's generation performance. The authors identify and resolve technical challenges that typically cause generation degradation in retrieval-optimized models. The single-model approach significantly reduces memory requirements—"peak GPU memory from 28.85 GB to 10.77 GB at 4B (62.7% reduction)" and enables the release of two model variants (Hydra-4B and Hydra-0.8B).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29add9b8-c277-466c-9686-ea5ff063dac3",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "0fbbeb7b-fba0-4c09-bc84-3a2c2efdb937",
  "sourceToolAssistantUUID": "29add9b8-c277-466c-9686-ea5ff063dac3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-30T06:15:43.735Z_

<details><summary>↩ Tool result · `toolu_016VThjsN1TpdiyKqyLAPW7D`</summary>

```text
# Hybrid-Vector Retrieval for Visually Rich Documents

**Full Title:** "Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy"

**Authors:** Juyeon Kim, Geon Lee, Dongwon Choi, Taeuk Kim, and Kijung Shin

**Submission Date:** October 25, 2025 (v1); revised April 20, 2026 (v2)

**Abstract Summary:**
The paper addresses document retrieval challenges by proposing HEAVEN, a framework that balances computational efficiency with retrieval accuracy. The system uses a two-stage approach: first retrieving candidates through single-vector methods on summarized pages, then reranking with multi-vector methods while filtering less important query terms. The authors also introduce ViMDoc, a benchmark for evaluating retrieval on visually complex, multi-document collections. Results demonstrate the method achieves "99.87% of the Recall@1 performance of multi-vector models on average" while reducing computational costs by 99.82%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c350eec-bf2c-489c-ab9e-889fcd6cc929",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "50445961-6b4f-4f06-a5a3-7b3524019382",
  "sourceToolAssistantUUID": "8c350eec-bf2c-489c-ab9e-889fcd6cc929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-30T06:15:44.039Z_

<details><summary>↩ Tool result · `toolu_012cY2dTMJyc1SBVuZTuoRZJ`</summary>

```text
# MLDocRAG Paper Information

**Full Title:** MLDocRAG: Multimodal Long-Context Document Retrieval Augmented Generation

**Authors:** Yongyue Zhang and Yaxiong Wu

**Submission Date:** February 10, 2026 (v1); last revised February 13, 2026 (v3)

**Abstract Summary:**

The paper addresses challenges in comprehending multimodal long-context documents containing mixed content like text, figures, and tables. The researchers propose organizing diverse document elements through a query-centric approach, treating queries as semantic representations for heterogeneous materials.

Their framework, MLDocRAG, employs a Multimodal Chunk-Query Graph structure. This graph is built by generating detailed questions from various document sections and connecting them across different modalities and pages. This enables more effective retrieval and evidence gathering for multimodal question-answering tasks.

Testing on MMLongBench-Doc and LongDocURL datasets demonstrates that MLDocRAG "consistently improves retrieval quality and answer accuracy," showing its utility in handling complex multimodal documents that span multiple pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34674bb0-635a-4967-a597-0128ebdcb26c",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "1edb367e-602e-4240-afee-08fd3bf75a5e",
  "sourceToolAssistantUUID": "34674bb0-635a-4967-a597-0128ebdcb26c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-30T06:15:46.780Z_

Let me search for more important papers in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1edb367e-602e-4240-afee-08fd3bf75a5e",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGEQeGXv44DE9JrXKiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0627fd51-1001-4455-9588-87d300ff98d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcG5ppfad3FkoeD4CmGSaj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 30316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3281,
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

_source line 108 · 2026-05-30T06:15:47.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017zzF7okHJqreRCk2DBW5Di`</summary>

```json
{
  "query": "pixel poisoning attack document screenshot retrieval arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0627fd51-1001-4455-9588-87d300ff98d3",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGEQeGXv44DE9JrXKiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f21f1b8d-8526-4bc9-8f79-e133da66d517",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcG5ppfad3FkoeD4CmGSaj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 30316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3281,
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

_source line 109 · 2026-05-30T06:15:48.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TW8ap6raLwr19sGYwhFHUc`</summary>

```json
{
  "query": "MRMR reasoning-intensive multimodal retrieval benchmark arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f21f1b8d-8526-4bc9-8f79-e133da66d517",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGEQeGXv44DE9JrXKiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "436c9580-1192-4043-a200-a20c7bb241af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcG5ppfad3FkoeD4CmGSaj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 30316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3281,
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

_source line 110 · 2026-05-30T06:15:48.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NuWxuGJp9NVPYSxxLBc7CP`</summary>

```json
{
  "query": "retrieval augmented generation visual understanding survey arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "436c9580-1192-4043-a200-a20c7bb241af",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGEQeGXv44DE9JrXKiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6517250-1b54-4169-a178-95b80c1807f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcG5ppfad3FkoeD4CmGSaj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 30316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3281,
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

_source line 111 · 2026-05-30T06:15:49.269Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKNKGhhvxsZSYdUzKyieCo`</summary>

```json
{
  "query": "BiVLC BM25 visual document retrieval ColPali alternative arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6517250-1b54-4169-a178-95b80c1807f5",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGEQeGXv44DE9JrXKiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "745411a2-fac3-45f0-ba2b-6d01e57ec08f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcG5ppfad3FkoeD4CmGSaj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 279,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 30316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3281,
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

_source line 112 · 2026-05-30T06:15:54.970Z_

<details><summary>↩ Tool result · `toolu_01NuWxuGJp9NVPYSxxLBc7CP`</summary>

```text
Web search results for query: "retrieval augmented generation visual understanding survey arxiv 2025"

Links: [{"title":"Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250318016Z/abstract"},{"title":"[2503.18016v1] Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook","url":"http://arxiv.org/abs/2503.18016v1"},{"title":"[2503.18016] Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook","url":"https://arxiv.org/abs/2503.18016"},{"title":"Retrieval Augmented Generation and Understanding in ...","url":"https://arxiv.org/pdf/2503.18016"},{"title":"Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook | Request PDF","url":"https://www.researchgate.net/publication/390143171_Retrieval_Augmented_Generation_and_Understanding_in_Vision_A_Survey_and_New_Outlook"},{"title":"Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding","url":"https://arxiv.org/html/2510.15253v2"},{"title":"Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook","url":"https://arxiv.org/html/2503.18016v1"},{"title":"[2504.08748] A Survey of Multimodal Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2504.08748"},{"title":"Multimodal Adaptive Retrieval Augmented Generation ...","url":"https://arxiv.org/pdf/2603.00511"}]

I found the paper you're looking for! Here are the results:

## "Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook"

This survey was published on arXiv in March 2025 (arXiv:2503.18016). The paper is authored by Xu Zheng and colleagues.

### Main Focus

The survey provides a comprehensive review of the current state of retrieval-augmented techniques in computer vision, focusing on two main areas: visual understanding and visual generation.

### Scope

In the realm of visual understanding, the survey systematically reviews tasks ranging from basic image recognition to complex applications such as medical report generation and multimodal question answering. For visual content generation, it examines the application of RAG in tasks related to image, video, and 3D generation.

The survey also explores recent advancements in RAG for embodied AI, with a particular focus on applications in planning, task execution, multimodal perception, interaction, and specialized domains.

### Key Insight

Given that the integration of retrieval-augmented techniques in CV is still in its early stages, the authors highlight the key limitations of current approaches and propose future research directions to drive the development of this promising area.

You can access the paper directly on arXiv at: https://arxiv.org/abs/2503.18016


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6517250-1b54-4169-a178-95b80c1807f5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "e0ae0cbb-77ed-4238-98d5-ebb211632f6d",
  "sourceToolAssistantUUID": "e6517250-1b54-4169-a178-95b80c1807f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-30T06:15:56.395Z_

<details><summary>↩ Tool result · `toolu_01TW8ap6raLwr19sGYwhFHUc`</summary>

```text
Web search results for query: "MRMR reasoning-intensive multimodal retrieval benchmark arxiv 2025"

Links: [{"title":"MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.09510v1"},{"title":"MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval","url":"https://arxiv.org/pdf/2510.09510"},{"title":"Paper page - MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval","url":"https://huggingface.co/papers/2510.09510"},{"title":"[2510.09510] MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval","url":"https://arxiv.org/abs/2510.09510"},{"title":"MRMR","url":"https://openreview.net/pdf/4b90e6cb883a3d5058db987f962e14835415f9cb.pdf"},{"title":"ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge","url":"https://arxiv.org/html/2602.09839"},{"title":"Multimodal Reasoning Benchmarks","url":"https://www.emergentmind.com/topics/multimodal-reasoning-benchmarks"}]

Based on the search results, here's what I found about the MRMR benchmark:

## MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval

MRMR is the first expert-level multidisciplinary multimodal retrieval benchmark requiring intensive reasoning, containing 1,502 queries spanning 23 domains, with positive documents carefully verified by human experts.

### Key Advancements

The benchmark challenges retrieval systems across diverse areas of expertise, enabling fine-grained model comparison across domains. Queries are reasoning-intensive, with images requiring deeper interpretation such as diagnosing microscopic slides. 

The benchmark introduces Contradiction Retrieval, a novel task requiring models to identify conflicting concepts. Queries and documents are constructed as image-text interleaved sequences, offering a realistic setting with multi-image queries and mixed-modality corpus documents, unlike earlier benchmarks restricted to single images or unimodal documents.

The paper was published on arXiv in October 2025 (arXiv:2510.09510), and the dataset is available on Hugging Face at https://huggingface.co/datasets/MRMRbenchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "436c9580-1192-4043-a200-a20c7bb241af",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "7440615f-a284-4f3c-98c8-35fcfb0cb3a9",
  "sourceToolAssistantUUID": "436c9580-1192-4043-a200-a20c7bb241af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-30T06:15:56.446Z_

<details><summary>↩ Tool result · `toolu_01BKNKGhhvxsZSYdUzKyieCo`</summary>

```text
Web search results for query: "BiVLC BM25 visual document retrieval ColPali alternative arxiv 2025 2026"

Links: [{"title":"Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/pdf/2407.01449"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/html/2407.01449v2"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models 👀","url":"https://huggingface.co/blog/manu/colpali"},{"title":"ColPali: EFFICIENT DOCUMENT RETRIEVAL WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf"},{"title":"[2407.01449] ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/abs/2407.01449"},{"title":"LensVLM: Selective Context Expansion for Compressed Visual Representation of Text","url":"https://arxiv.org/html/2605.07019v1"},{"title":"Visual Words Meet BM25: Sparse Auto-Encoder Visual Word Scoring for Image Retrieval","url":"https://arxiv.org/pdf/2603.05781"},{"title":"Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/pdf/2512.02660"}]

Based on the web search results, I found information related to your query about visual document retrieval systems. Here's what I found:

## ColPali and Related Systems

ColPali is a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages, enabling document retrieval by directly embedding the images of document pages.

### Comparison with BM25

Little difference is seen between BM25 and BGE-M3 embeddings, highlighting the visual information bottleneck. This suggests that traditional text-based retrieval methods like BM25 struggle with visually rich documents compared to vision-based approaches.

### Performance and Alternative Approaches

ColQwen3-4B combines the ColPali framework with a Qwen3-based language model, achieving state-of-the-art performance on ViDoRe, while ColModernVBERT is a 250M-parameter variant achieving performance within 0.6 points of ColPali on NDCG@5 with 10× fewer parameters.

Additionally, BM25-V is a sparse retriever that adopts SAE-derived visual words with BM25 and enables efficient inverted-index retrieval by representing each image as a compact set of active visual words.

**Note:** The search results did not specifically return information about a system called "BiVLC" from 2025 or 2026, though they do contain relevant information about ColPali alternatives and BM25-based visual retrieval approaches from recent arXiv papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "745411a2-fac3-45f0-ba2b-6d01e57ec08f",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "aaaf803e-b5a5-4de8-92e9-8db3ba11883b",
  "sourceToolAssistantUUID": "745411a2-fac3-45f0-ba2b-6d01e57ec08f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-30T06:15:57.288Z_

<details><summary>↩ Tool result · `toolu_017zzF7okHJqreRCk2DBW5Di`</summary>

```text
Web search results for query: "pixel poisoning attack document screenshot retrieval arxiv 2025"

Links: [{"title":"[2501.16902] Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/abs/2501.16902"},{"title":"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/html/2501.16902v1"},{"title":"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/pdf/2501.16902"},{"title":"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/abs/10.1145/3726302.3730056"},{"title":"GitHub - ielab/dsr-poisoning: Document Screenshot Retrievers Poisoning","url":"https://github.com/ielab/dsr-poisoning"},{"title":"One Pic is All it Takes: Poisoning Visual Document Retrieval Augmented Generation with a Single Image","url":"https://arxiv.org/html/2504.02132"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** "Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks"

**Key Findings:**
The research focuses on vision-language model (VLM)-based retrievers, such as DSE and ColPali, which leverage document screenshots embedded as vectors to enable effective search. 

The study proposes three pixel poisoning attack methods designed to compromise VLM-based retrievers. The results are significant: injecting even a single adversarial screenshot into the retrieval corpus can significantly disrupt search results, poisoning the top-10 retrieved documents for 41.9% of queries in the case of DSE and 26.4% for ColPali.

These vulnerability rates notably exceed those observed with equivalent attacks on text-only retrievers, and when targeting a small set of known queries, the attack success rate raises, achieving complete success in certain cases.

**Availability:**
- The paper has been accepted at SIGIR 2025
- The paper is available on arXiv: https://arxiv.org/abs/2501.16902
- The official code repository is available on GitHub: https://github.com/ielab/dsr-poisoning


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f21f1b8d-8526-4bc9-8f79-e133da66d517",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "8c120554-e98d-4836-8bf1-b09a4635050d",
  "sourceToolAssistantUUID": "f21f1b8d-8526-4bc9-8f79-e133da66d517",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-30T06:16:03.829Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012gxrnAdqQ3naWzSbb5yRyn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.16902",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c120554-e98d-4836-8bf1-b09a4635050d",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGFPJBeWAZL8ghSQxou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "768a53a2-4506-4d92-aeff-0eaac907d1b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Kci6DvSfcqupxDaq6iCAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2274,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 33597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 117 · 2026-05-30T06:16:04.282Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019iH9FmqxZEpb5pdFiWMfVb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.09510",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "768a53a2-4506-4d92-aeff-0eaac907d1b7",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGFPJBeWAZL8ghSQxou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60e7a84c-c781-496c-86b7-9e67aa5a2178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Kci6DvSfcqupxDaq6iCAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2274,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 33597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 118 · 2026-05-30T06:16:05.256Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YEjxVvtzskM6CMPyr3am6r`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.18016",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e7a84c-c781-496c-86b7-9e67aa5a2178",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGFPJBeWAZL8ghSQxou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "880343fa-2850-482f-9f93-1ee498a4a6fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Kci6DvSfcqupxDaq6iCAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2274,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 33597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 119 · 2026-05-30T06:16:06.175Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FoV4kcppvu67hr9defFppk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05781",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (BM25-V / visual words)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "880343fa-2850-482f-9f93-1ee498a4a6fc",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGFPJBeWAZL8ghSQxou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbfc2428-bb36-400d-9c3a-bce45881a8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Kci6DvSfcqupxDaq6iCAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2274,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 33597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 120 · 2026-05-30T06:16:06.653Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F7mcPLud3YjShpdMGW7vsB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.02660",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbfc2428-bb36-400d-9c3a-bce45881a8e2",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGFPJBeWAZL8ghSQxou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d02a1c40-875d-46ca-8daa-0e4b1dfc02ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Kci6DvSfcqupxDaq6iCAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2274,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 33597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 121 · 2026-05-30T06:16:07.292Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017Epg4WMy8Yn3ETELsRAYqm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.09839",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (ARK benchmark)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02a1c40-875d-46ca-8daa-0e4b1dfc02ee",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGFPJBeWAZL8ghSQxou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f870a427-96ed-47ad-9b39-064c2cba6655",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Kci6DvSfcqupxDaq6iCAP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2274,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 33597,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1143
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2274,
          "output_tokens": 512,
          "cache_read_input_tokens": 33597,
          "cache_creation_input_tokens": 1143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1143,
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

_source line 122 · 2026-05-30T06:16:08.428Z_

<details><summary>↩ Tool result · `toolu_012gxrnAdqQ3naWzSbb5yRyn`</summary>

```text
# Paper Summary

**Full Title:** "Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks"

**Authors:** Shengyao Zhuang, Ekaterina Khramtsova, Xueguang Ma, Bevan Koopman, Jimmy Lin, and Guido Zuccon

**Submission Date:** January 28, 2025

**Abstract:** This research examines security vulnerabilities in vision-language model-based document retrievers like DSE and ColPali. The authors introduce three adversarial attack methods targeting these systems. Their findings reveal that inserting just one malicious screenshot into a retrieval corpus can severely compromise search performance, disrupting the top-10 results for roughly 42% of queries in DSE and 26% in ColPali. These disruption rates substantially exceed those seen in attacks on traditional text-based systems. When attackers focus on specific known queries, success rates improve dramatically, reaching complete effectiveness in some scenarios. The work underscores significant security risks associated with deploying vision-language models in retrieval systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "768a53a2-4506-4d92-aeff-0eaac907d1b7",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "346d8c71-d4be-47b3-86fa-3fc45e455d0d",
  "sourceToolAssistantUUID": "768a53a2-4506-4d92-aeff-0eaac907d1b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-30T06:16:08.865Z_

<details><summary>↩ Tool result · `toolu_01YEjxVvtzskM6CMPyr3am6r`</summary>

```text
# Paper Information

**Full Title:**
"Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook"

**Authors:**
Xu Zheng, Ziqiao Weng, Yuanhuiyi Lyu, Lutao Jiang, Haiwei Xue, Bin Ren, Danda Paudel, Nicu Sebe, Luc Van Gool, and Xuming Hu

**Submission Date:**
March 23, 2025

**Abstract:**
This survey examines how retrieval-augmented generation (RAG) extends beyond language models into computer vision. The authors explore RAG applications across two primary domains: visual understanding (covering tasks from image recognition to medical report generation) and visual generation (addressing image, video, and 3D creation). They also investigate RAG's role in embodied AI systems, including planning and multimodal perception. The paper identifies current limitations and proposes future research directions for advancing retrieval-augmented techniques in vision systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "880343fa-2850-482f-9f93-1ee498a4a6fc",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "ae98f67c-42cb-4979-b759-a44edcb78747",
  "sourceToolAssistantUUID": "880343fa-2850-482f-9f93-1ee498a4a6fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-30T06:16:08.954Z_

<details><summary>↩ Tool result · `toolu_019iH9FmqxZEpb5pdFiWMfVb`</summary>

```text
# MRMR Paper Details

**Full Title:** MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval

**Authors:** Siyue Zhang, Yuan Gao, Xiao Zhou, Yilun Zhao, Tingyu Song, Arman Cohan, Anh Tuan Luu, Chen Zhao

**Submission Date:** October 10, 2025 (with revision on February 14, 2026)

**Abstract Summary:**

The researchers present a new benchmark containing 1,502 queries across 23 domains with "positive documents carefully verified by human experts." The dataset distinguishes itself through three main innovations: it enables evaluation across diverse expertise areas, incorporates "reasoning-intensive" queries requiring detailed image analysis, and introduces a novel task focused on identifying contradictory concepts. 

The benchmark features a realistic multimodal environment where "queries and documents are constructed as image-text interleaved sequences," moving beyond earlier systems that used single images or uniform document types.

Their evaluation of 14 frontier models revealed that text embedding models paired with caption generation outperformed specialized multimodal systems on reasoning tasks, suggesting considerable room for advancement in this field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60e7a84c-c781-496c-86b7-9e67aa5a2178",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "2c673620-fd3a-4b51-8a75-ed3e179dcc17",
  "sourceToolAssistantUUID": "60e7a84c-c781-496c-86b7-9e67aa5a2178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-30T06:16:11.229Z_

<details><summary>↩ Tool result · `toolu_01F7mcPLud3YjShpdMGW7vsB`</summary>

```text
# Paper Information

**Full Title:** Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation

**Author:** Athos Georgiou

**Submission Date:** December 2, 2025 (v1); Last revised January 1, 2026 (v3)

**Abstract Summary:**

This work addresses limitations in document retrieval by combining two existing approaches. The researchers propose bridging multimodal retrieval models like ColPali—which compute fine-grained similarity between query tokens and image patches—with OCR-based systems that extract structured text with spatial coordinates.

Their hybrid method formalizes the mapping between vision transformer patch grids and OCR bounding boxes, using patch-level similarity scores to filter relevant regions. On the BBox-DocVQA benchmark, their approach achieves 59.7% hit rate at IoU@0.5 for within-page localization. The technique reduces context tokens by approximately 29% compared to including all OCR regions and 52% versus full-page image tokens. Notably, it requires no additional training and operates entirely at inference time. The authors released "Snappy," an open-source implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d02a1c40-875d-46ca-8daa-0e4b1dfc02ee",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "beab1dc6-6df7-422a-b57c-00e92cd3acd0",
  "sourceToolAssistantUUID": "d02a1c40-875d-46ca-8daa-0e4b1dfc02ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-30T06:16:11.392Z_

<details><summary>↩ Tool result · `toolu_01FoV4kcppvu67hr9defFppk`</summary>

```text
# Paper Information: BM25-V

**Full Title:**
"Visual Words Meet BM25: Sparse Auto-Encoder Visual Word Scoring for Image Retrieval"

**Authors:**
- Donghoon Han
- Eunhwan Park
- Seunghyeon Seo

**Submission Date:**
March 6, 2026

**Abstract Summary:**
The researchers present BM25-V, a method that applies Okapi BM25 scoring to sparse visual-word activations derived from a Sparse Auto-Encoder operating on Vision Transformer patch features. The approach leverages the Zipfian-like distribution of visual-word document frequencies to suppress common, uninformative words while emphasizing rare, discriminative ones. As a first-stage retriever using sparse inverted-index operations, it achieves "Recall@200 ≥ 0.993" across seven benchmarks. When paired with dense reranking of only 200 candidates per query, the two-stage pipeline maintains near-dense accuracy within 0.2% on average. The method demonstrates zero-shot transferability from ImageNet-1K training to seven fine-grained benchmarks and provides explainability through quantified IDF contributions to retrieval decisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbfc2428-bb36-400d-9c3a-bce45881a8e2",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "4918c779-3ec1-4262-b545-4606b18cf320",
  "sourceToolAssistantUUID": "fbfc2428-bb36-400d-9c3a-bce45881a8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-30T06:16:11.828Z_

<details><summary>↩ Tool result · `toolu_017Epg4WMy8Yn3ETELsRAYqm`</summary>

```text
# ARK Benchmark Paper Details

**Full Title:** "ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge"

**Authors:** Yijie Lin, Guofeng Ding, Haochen Zhou, Haobin Li, Mouxing Yang, and Xi Peng

**Submission Date:** February 10, 2026

**Abstract Summary:**

The researchers created a benchmark to evaluate how systems retrieve information across different modalities. Their framework analyzes retrieval through two dimensions: knowledge domains (covering five areas with 17 subcategories) and reasoning skills (six types). 

The benchmark tests systems using various query and candidate formats with 16 different visual data types. According to the authors, "most queries are paired with targeted hard negatives that require multi-step reasoning" to prevent simple matching shortcuts.

Testing 23 different retrievers revealed significant performance gaps, particularly in "fine-grained visual and spatial reasoning" tasks. While techniques like re-ranking and rewriting showed promise, the researchers note that "substantial headroom remains" for improvement in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f870a427-96ed-47ad-9b39-064c2cba6655",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "9d4ab176-c845-4185-8831-2878739fd227",
  "sourceToolAssistantUUID": "f870a427-96ed-47ad-9b39-064c2cba6655",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 128 · 2026-05-30T06:16:15.424Z_

Let me search for a few more important papers I've seen referenced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d4ab176-c845-4185-8831-2878739fd227",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGGTSVsWjAfxwmsbXHd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc11e614-7537-4e14-b7ae-bf4d492d1df8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PQSn6vzronNGgxwe21sqB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4481,
      "cache_read_input_tokens": 34740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4481,
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

_source line 129 · 2026-05-30T06:16:16.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014SXiPWQbSWsoJ42bWuArGJ`</summary>

```json
{
  "query": "ColModernVBERT small efficient visual document retrieval arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc11e614-7537-4e14-b7ae-bf4d492d1df8",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGGTSVsWjAfxwmsbXHd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dd780fa-9b4e-4610-8c0a-ff943e701cd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PQSn6vzronNGgxwe21sqB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4481,
      "cache_read_input_tokens": 34740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4481,
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

_source line 130 · 2026-05-30T06:16:17.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFFQ2ELZcP1a2xxSDy48AP`</summary>

```json
{
  "query": "\"multi-page document understanding\" VLM benchmark arxiv 2025 2026 MP-DocVQA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dd780fa-9b4e-4610-8c0a-ff943e701cd1",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGGTSVsWjAfxwmsbXHd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f8a13d7-d58a-42f6-94c9-80001ca82a47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PQSn6vzronNGgxwe21sqB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4481,
      "cache_read_input_tokens": 34740,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 34740,
          "cache_creation_input_tokens": 4481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4481,
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

_source line 131 · 2026-05-30T06:16:17.790Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SzewvRbAj99cPBdqzqtHg8`</summary>

```json
{
  "query": "document retrieval reranking visual language model arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f8a13d7-d58a-42f6-94c9-80001ca82a47",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGGTSVsWjAfxwmsbXHd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea3fc2e4-1ef1-42e8-8cd5-138accfe0c98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PQSn6vzronNGgxwe21sqB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4481,
      "cache_read_input_tokens": 34740,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 34740,
          "cache_creation_input_tokens": 4481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4481,
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

_source line 132 · 2026-05-30T06:16:22.945Z_

<details><summary>↩ Tool result · `toolu_014SXiPWQbSWsoJ42bWuArGJ`</summary>

```text
Web search results for query: "ColModernVBERT small efficient visual document retrieval arxiv 2025 2026"

Links: [{"title":"Small is Mighty: How ModernVBERT Redefines Visual Document Retrieval | Deep Paper","url":"https://deep-paper.org/en/paper/2510.01149/"},{"title":"ModernVBERT: Towards Smaller Visual Document Retrievers","url":"https://arxiv.org/html/2510.01149v1"},{"title":"[Quick Review] ModernVBERT: Towards Smaller Visual Document Retrievers","url":"https://liner.com/review/modernvbert-towards-smaller-visual-document-retrievers"},{"title":"[2510.01149] ModernVBERT: Towards Smaller Visual Document Retrievers","url":"https://arxiv.org/abs/2510.01149"},{"title":"Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/pdf/2512.02660"},{"title":"ModernVBERT: TOWARDS SMALLER VISUAL DOCU- MENT RETRIEVERS Paul Teiletche1,2","url":"https://arxiv.org/pdf/2510.01149"},{"title":"[2510.01149v1] ModernVBERT: Towards Smaller Visual Document Retrievers","url":"https://arxiv.org/abs/2510.01149v1"},{"title":"irpapers: A Visual Document Benchmark for Scientific Retrieval and Question Answering","url":"https://arxiv.org/html/2602.17687"},{"title":"Fantastic (small) Retrievers and How to Train","url":"https://arxiv.org/pdf/2510.14880"}]

Based on the search results, I found comprehensive information about ColModernVBERT and the ModernVBERT paper:

## Overview

ColModernVBERT is a lean 250M parameter model designed for visual document retrieval. ModernVBERT is a compact 250M-parameter vision-language encoder that outperforms models up to 10 times larger when fine-tuned on document retrieval tasks.

## Key Design Features

The training recipe for ModernVBERT combines a 150M text bidirectional encoder with a 100M vision encoder, using a Masked Language Modeling objective and an augmented input image resolution during a cooldown stage.

There is a tight synergy between bidirectional attention and late-interaction retrieval, which underscores a fundamental limitation of repurposing decoder-style generative VLMs for retrieval.

## Performance

ColModernVBERT tops all sub-1B models and matches models up to 10× larger, while being CPU-friendly. ColModernVBERT achieved strong performance on visual document retrieval benchmarks, matching larger models while significantly reducing inference latency and costs on CPU hardware.

## Publication

Models and code are made available at https://huggingface.co/ModernVBERT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dd780fa-9b4e-4610-8c0a-ff943e701cd1",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "7484399b-4203-48a0-b4d8-251148988622",
  "sourceToolAssistantUUID": "1dd780fa-9b4e-4610-8c0a-ff943e701cd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-30T06:16:24.419Z_

<details><summary>↩ Tool result · `toolu_01SzewvRbAj99cPBdqzqtHg8`</summary>

```text
Web search results for query: "document retrieval reranking visual language model arxiv 2025 2026"

Links: [{"title":"When Vision Meets Texts in Listwise Reranking","url":"https://arxiv.org/html/2601.20623"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/html/2602.19961v1"},{"title":"When Vision Meets Texts in Listwise Reranking Hongyi Cai xcloudfance@gmail.com","url":"https://arxiv.org/pdf/2601.20623"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.19961"},{"title":"arXiv:2506.12364v2 [cs.AI] 22 Jun 2025","url":"https://www.arxiv.org/pdf/2506.12364"},{"title":"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models","url":"https://arxiv.org/pdf/2509.15432"},{"title":"[2601.20623] When Vision Meets Texts in Listwise Reranking","url":"https://arxiv.org/abs/2601.20623"}]

Based on the search results, I found several relevant papers from arxiv in 2025-2026 about document retrieval reranking with visual language models:

## Key Papers Found:

**1. "When Vision Meets Texts in Listwise Reranking"** (January 2026)
This paper addresses multimodal reranking in document retrieval using visual-language models and listwise ranking approaches with knowledge distillation. The proposed Rank-Nexus approach extends listwise reranking to multimodal scenarios, jointly processing both textual passages and images to generate comprehensive rankings.

**2. "Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval"** (February 2026)
This survey discusses FreeRet, which introduces a plug-and-play framework that uses off-the-shelf multimodal large language models (MLLMs) for both embedding-based search and multiple-choice question based reranking without parameter updates. The paper also covers the development of MLLM-based embedding and reranker models to enhance semantic matching.

**3. "SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval"** (2025)
This work addresses Visual Document Retrieval (VDR) by jointly encoding textual and visual elements rendered as images.

These papers represent recent advances in combining visual language models with document retrieval and reranking tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea3fc2e4-1ef1-42e8-8cd5-138accfe0c98",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "cbed6f09-09e6-469b-9d4b-6aa74b3bcf62",
  "sourceToolAssistantUUID": "ea3fc2e4-1ef1-42e8-8cd5-138accfe0c98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-30T06:16:25.226Z_

<details><summary>↩ Tool result · `toolu_01QFFQ2ELZcP1a2xxSDy48AP`</summary>

```text
Web search results for query: ""multi-page document understanding" VLM benchmark arxiv 2025 2026 MP-DocVQA"

Links: [{"title":"DocVLM: Make Your VLM an Efficient Reader","url":"https://arxiv.org/html/2412.08746v1"},{"title":"Hierarchical multimodal transformers for Multipage DocVQA | Request PDF","url":"https://www.researchgate.net/publication/372639409_Hierarchical_multimodal_transformers_for_Multipage_DocVQA"},{"title":"Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark","url":"https://arxiv.org/pdf/2507.15882"},{"title":"Enhancing Document VQA Models via Retrieval-Augmented Generation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-09368-4_6"},{"title":"Hierarchical multimodal transformers for Multi-Page DocVQA","url":"https://arxiv.org/pdf/2212.05935"},{"title":"Doc-𝑉^∗: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA","url":"https://arxiv.org/html/2604.13731v1"},{"title":"AVIR: Adaptive Visual In-Document Retrieval for Efficient Multi-Page Document Question Answering","url":"https://arxiv.org/pdf/2601.11976"}]

I found several relevant results about multi-page document understanding and VLM benchmarks. Here's what the search revealed:

## Key Benchmarks

MP-DocVQA is a multi-page document VQA dataset with 46K samples, 6K unique documents, and 60K questions. Document Haystack is a novel benchmark designed to evaluate VLM performance in retrieving key multimodal information from long documents, featuring 400 document variants ranging from 5 to 200 pages.

## Recent Research (2025-2026)

DocVLM achieves state-of-the-art results on MP-DocVQA (86.3% vs. 80.3%), despite not being trained on multipage data. DocVLM was tested on the MP-DocVQA dataset with documents up to 20 pages long – a scale that most other state-of-the-art methods struggle to handle due to token limitations.

Doc-V* jointly optimizes answer accuracy and evidence-seeking efficiency and is trained on data sourced from MP-DocVQA and DUDE. AVIR, a retrieval-guided MP-VQA pipeline, achieves superior performance on MP-DocVQA, SlideVQA, and DUDE.

## Related Benchmarks

Recent benchmarks such as DUDE, Loong, SlideVQA, and MMLongBench-Doc attempted to tackle multi-page document comprehension.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f8a13d7-d58a-42f6-94c9-80001ca82a47",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "f3e2f815-e63b-4c5c-8bfd-e9359f1c5044",
  "sourceToolAssistantUUID": "8f8a13d7-d58a-42f6-94c9-80001ca82a47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-30T06:16:28.371Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F45N9nPJ3VdaAja1cx9Nmo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01149",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3e2f815-e63b-4c5c-8bfd-e9359f1c5044",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGHSkbpvGNij28BdLCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffafc0e0-be7e-4dbb-adb9-037566fc2812",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbQwLnwnp71eWMBwZFpM7D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 39221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1715,
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

_source line 136 · 2026-05-30T06:16:28.828Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RZj6eUTpk9YtSQyCQRrJgN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20623",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffafc0e0-be7e-4dbb-adb9-037566fc2812",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGHSkbpvGNij28BdLCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7799e04-761a-45d5-ae11-1ad4c69ad5cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbQwLnwnp71eWMBwZFpM7D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 39221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1715,
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

_source line 137 · 2026-05-30T06:16:29.900Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BUedZLkPqyiiBmHWbXAaFD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.11976",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (AVIR)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7799e04-761a-45d5-ae11-1ad4c69ad5cb",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGHSkbpvGNij28BdLCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2e23721-7393-46c9-b517-c25bb3202749",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbQwLnwnp71eWMBwZFpM7D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 39221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1715,
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

_source line 138 · 2026-05-30T06:16:30.794Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014kdq4h6esUF2Nm5T9Dv8TF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.17687",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (irpapers benchmark)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e23721-7393-46c9-b517-c25bb3202749",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGHSkbpvGNij28BdLCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab185a50-7a91-4b83-8806-ab678626bc1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbQwLnwnp71eWMBwZFpM7D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 39221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1715,
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

_source line 139 · 2026-05-30T06:16:31.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MtgkqrTyFYVojRN39RuAFr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.15882",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (Document Haystack)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab185a50-7a91-4b83-8806-ab678626bc1d",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGHSkbpvGNij28BdLCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c907f04c-bd5b-44db-8455-0d396c67c272",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbQwLnwnp71eWMBwZFpM7D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 1715,
      "cache_read_input_tokens": 39221,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 723,
          "output_tokens": 434,
          "cache_read_input_tokens": 39221,
          "cache_creation_input_tokens": 1715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1715,
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

_source line 140 · 2026-05-30T06:16:32.267Z_

<details><summary>↩ Tool result · `toolu_01F45N9nPJ3VdaAja1cx9Nmo`</summary>

```text
# Paper Summary

**Full Title:** ModernVBERT: Towards Smaller Visual Document Retrievers

**Authors:** Paul Teiletche, Quentin Macé, Max Conti, Antonio Loison, Gautier Viaud, Pierre Colombo, Manuel Faysse

**Submission Date:** October 1, 2025 (with revisions through December 16, 2025)

**Abstract:**
This research addresses visual document retrieval through systematic optimization of training approaches. The authors demonstrate that repurposing large generative vision-language models creates performance constraints. Through controlled experimentation, they identify critical factors including "attention masking, image resolution, modality alignment data regimes, and late interaction centered contrastive objectives." The resulting ModernVBERT model, a 250-million parameter encoder, achieves superior performance compared to significantly larger competitors while enabling efficient CPU-based deployment, reducing operational costs without sacrificing retrieval effectiveness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffafc0e0-be7e-4dbb-adb9-037566fc2812",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "e1dfc7c8-6606-41c9-b124-b225213f347e",
  "sourceToolAssistantUUID": "ffafc0e0-be7e-4dbb-adb9-037566fc2812",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-30T06:16:32.550Z_

<details><summary>↩ Tool result · `toolu_01RZj6eUTpk9YtSQyCQRrJgN`</summary>

```text
# Paper Summary

**Full Title:** "When Vision Meets Texts in Listwise Reranking"

**Author:** Hongyi Cai

**Submission Date:** January 28, 2026

**Abstract Summary:**

The paper introduces Rank-Nexus, a system designed to improve document ranking by combining visual and textual information. The researchers developed a training approach that handles images and text separately before combining them, addressing challenges in multimodal learning where aligned datasets are limited.

Key contributions include using a lightweight 2-billion-parameter model (rather than larger alternatives requiring 7-32B parameters) and creating training data through multimodal language model captions. The system achieves competitive results on standard benchmarks like TREC and BEIR for text-based tasks, as well as image-focused challenges including INQUIRE and MMDocIR, while maintaining computational efficiency without requiring complex reasoning-based approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7799e04-761a-45d5-ae11-1ad4c69ad5cb",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "51951b43-f274-4eed-a94c-7ad9e49baa50",
  "sourceToolAssistantUUID": "f7799e04-761a-45d5-ae11-1ad4c69ad5cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-30T06:16:34.229Z_

<details><summary>↩ Tool result · `toolu_01BUedZLkPqyiiBmHWbXAaFD`</summary>

```text
# AVIR Paper Information

**Full Title:** "AVIR: Adaptive Visual In-Document Retrieval for Efficient Multi-Page Document Question Answering"

**Authors:** Zongmin Li, Yachuan Li, Lei Kang, Dimosthenis Karatzas, Wenkang Ma

**Submission Date:** January 17, 2026

**Abstract:** The research addresses challenges in multi-page document visual question answering by proposing a lightweight retrieval system that scores pages for relevance. "Pages are then clustered according to the score distribution to adaptively select relevant content." The framework uses Top-K filtering and relevance thresholds to maintain context quality. Rather than fine-tuning models, the selected pages feed directly into a frozen large vision-language model for answer generation. The approach achieves significant computational efficiency, "reducing the average page count required for question answering by 70%" while attaining strong performance metrics (84.58% ANLS) on the MP-DocVQA benchmark, with additional validation on SlideVQA and DUDE datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2e23721-7393-46c9-b517-c25bb3202749",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "c996eb30-249b-44ca-af4d-979c7d0d9347",
  "sourceToolAssistantUUID": "e2e23721-7393-46c9-b517-c25bb3202749",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-30T06:16:35.156Z_

<details><summary>↩ Tool result · `toolu_014kdq4h6esUF2Nm5T9Dv8TF`</summary>

```text
# IRPAPERS Paper Information

**Full Title:**
"IRPAPERS: A Visual Document Benchmark for Scientific Retrieval and Question Answering"

**Authors:**
Connor Shorten, Augustas Skaburskas, Daniel M. Jones, Charles Pierse, Roberto Esposito, John Trengrove, Etienne Dilocker, Bob van Luijt

**Submission Date:**
February 5, 2026

**Abstract Summary:**
The paper addresses how image-based document processing compares to traditional text-based methods. The researchers created a benchmark comprising 3,230 pages from 166 scientific papers, with both image and OCR versions available. Using 180 test questions, they evaluated retrieval and question-answering systems across both modalities. Key findings indicate that "text retrieval using Arctic 2.0 embeddings, BM25, and hybrid text search achieved 46% Recall@1, 78% Recall@5, and 91% Recall@20," while combining both modalities improved performance to 49%, 81%, and 95% respectively. The study demonstrates that text and image representations have complementary strengths, with multimodal approaches outperforming single-modality systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab185a50-7a91-4b83-8806-ab678626bc1d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "84d87a28-03f1-4aeb-bfe0-087c79b3e838",
  "sourceToolAssistantUUID": "ab185a50-7a91-4b83-8806-ab678626bc1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-30T06:16:35.409Z_

<details><summary>↩ Tool result · `toolu_01MtgkqrTyFYVojRN39RuAFr`</summary>

```text
# Document Haystack Paper Details

**Full Title:** Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark

**Authors:** Goeric Huybrechts, Srikanth Ronanki, Sai Muralidhar Jayanthi, Jack Fitzgerald, Srinivasan Veeravanallur

**Submission Date:** July 18, 2025 (v1); Last revised August 4, 2025 (v2)

**Abstract:** The researchers created a benchmark to evaluate how well Vision Language Models handle extensive documents. "Document Haystack features documents ranging from 5 to 200 pages and strategically inserts pure text or multimodal text+image 'needles' at various depths" to test retrieval capabilities. The dataset contains 400 document variants and 8,250 questions, supported by automated evaluation methods. The team presents findings from prominent VLMs and outlines potential future research directions in this domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c907f04c-bd5b-44db-8455-0d396c67c272",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "1aa18691-b8c6-483c-8b3e-3a207ac0478c",
  "sourceToolAssistantUUID": "c907f04c-bd5b-44db-8455-0d396c67c272",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 145 · 2026-05-30T06:16:38.158Z_

Let me search for a few more important papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa18691-b8c6-483c-8b3e-3a207ac0478c",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGJCGVPnRsBg8DnJpkC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eafac0f-8359-4303-be79-203fb533e591",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvqJNTWP87uEiNxAguDYzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 40936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
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

_source line 146 · 2026-05-30T06:16:39.160Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UzGbRiD6KXfiLXFc9PxK3w`</summary>

```json
{
  "query": "FreeRet training-free visual document retrieval reranking MLLM arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eafac0f-8359-4303-be79-203fb533e591",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGJCGVPnRsBg8DnJpkC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7395cf4-26bf-4cbb-82ec-30a133c87b38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvqJNTWP87uEiNxAguDYzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 40936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
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

_source line 147 · 2026-05-30T06:16:39.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PykM1U1NSk1spe4GjgGV21`</summary>

```json
{
  "query": "ColQwen3 visual document retrieval 2026 arxiv state-of-the-art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7395cf4-26bf-4cbb-82ec-30a133c87b38",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGJCGVPnRsBg8DnJpkC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f4365ab-a8db-4fd1-8c9e-f61704f4a31d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvqJNTWP87uEiNxAguDYzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 40936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
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

_source line 148 · 2026-05-30T06:16:40.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012CU8o9cJRqEkjFd5LQTFBa`</summary>

```json
{
  "query": "\"visual document retrieval\" efficient token compression embedding reduction arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f4365ab-a8db-4fd1-8c9e-f61704f4a31d",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGJCGVPnRsBg8DnJpkC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cdc33ff-69f8-4e47-b3b8-5ee12a7c9279",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvqJNTWP87uEiNxAguDYzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 40936,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 40936,
          "cache_creation_input_tokens": 2442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2442,
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

_source line 149 · 2026-05-30T06:16:44.653Z_

<details><summary>↩ Tool result · `toolu_01UzGbRiD6KXfiLXFc9PxK3w`</summary>

```text
Web search results for query: "FreeRet training-free visual document retrieval reranking MLLM arxiv 2025"

Links: [{"title":"[2509.24621] FreeRet: MLLMs as Training-Free Retrievers","url":"https://arxiv.org/abs/2509.24621"},{"title":"FreeRet: MLLMs as Training-Free Retrievers","url":"https://arxiv.org/pdf/2509.24621"},{"title":"FREERET: MLLMS AS TRAINING-FREE RETRIEVERS","url":"https://openreview.net/pdf/286fbf50a0b598c7f85d4e9b4c3c5dd18b483251.pdf"},{"title":"[Literature Review] FreeRet: MLLMs as Training-Free Retrievers","url":"https://www.themoonlight.io/en/review/freeret-mllms-as-training-free-retrievers"},{"title":"RETLLM: TRAINING AND DATA-FREE MLLMS FOR MULTIMODAL INFORMATION RETRIEVAL","url":"https://arxiv.org/html/2602.22278"}]

I found the paper you're looking for! Here's what I discovered:

FreeRet is a plug-and-play framework that turns any MLLM into a two-stage retriever, first deriving semantically grounded embeddings directly from the model for fast candidate search, and then exploiting its reasoning ability for precise reranking.

On the MMEB and MMEB-V2 benchmarks spanning 46 datasets, FreeRet substantially outperforms models trained on millions of pairs.

FreeRet is model-agnostic and scales seamlessly across MLLM families and sizes, preserves their generative abilities, supports arbitrary modality combinations, and unifies retrieval, reranking, and generation into end-to-end RAG within a single model.

The paper appears to have been published on September 29, 2025, and is available on arXiv as paper 2509.24621.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7395cf4-26bf-4cbb-82ec-30a133c87b38",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "03c39df4-8d23-425d-95fe-f5ea4bcc3a9b",
  "sourceToolAssistantUUID": "d7395cf4-26bf-4cbb-82ec-30a133c87b38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-30T06:16:46.227Z_

<details><summary>↩ Tool result · `toolu_01PykM1U1NSk1spe4GjgGV21`</summary>

```text
Web search results for query: "ColQwen3 visual document retrieval 2026 arxiv state-of-the-art"

Links: [{"title":"Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model","url":"https://arxiv.org/html/2603.28554v2"},{"title":"Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/html/2512.02660v3"},{"title":"CausalEmbed: Auto-Regressive Multi-Vector Generation in Latent Space for Visual Document Embedding","url":"https://arxiv.org/html/2601.21262"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction embedding models for Visual Document Retrieval","url":"https://arxiv.org/html/2602.03992v1"},{"title":"[2512.02660] Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/abs/2512.02660"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/pdf/2506.04997"},{"title":"Visual Late Chunking: An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval","url":"https://arxiv.org/html/2604.10167"}]

Based on the search results, here's what I found about ColQwen3 and visual document retrieval in 2026:

## ColQwen3 Overview

ColQwen3-4B combines the ColPali framework with a Qwen3-based language model, achieving state-of-the-art performance on ViDoRe while maintaining the patch-level embeddings essential for visual document retrieval tasks.

## State-of-the-Art Performance

Nemotron ColEmbed V2 achieves state-of-the-art performance on the ViDoRe benchmarks, with the 8B model ranking first on the ViDoRe V3 leaderboard as of February 03, 2026, achieving an average NDCG@10 of 63.42.

Additionally, Ops-ColQwen3 is described as a State-of-the-Art Multimodal Embedding Model for Visual Document Retrieval.

## Technical Approach

The ColPali architecture has spawned a family of late-interaction visual retrievers sharing the core patch-embedding approach, with ColQwen3-4B combining the ColPali framework with a Qwen3-based language model.

The search results show active development in visual document retrieval with multiple ColQwen3 variants being evaluated and deployed across the 2025-2026 period on standardized benchmarks like ViDoRe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f4365ab-a8db-4fd1-8c9e-f61704f4a31d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "605f5d86-8c66-4777-a0fa-b888e90df4ff",
  "sourceToolAssistantUUID": "5f4365ab-a8db-4fd1-8c9e-f61704f4a31d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-30T06:16:47.303Z_

<details><summary>↩ Tool result · `toolu_012CU8o9cJRqEkjFd5LQTFBa`</summary>

```text
Web search results for query: ""visual document retrieval" efficient token compression embedding reduction arxiv 2025 2026"

Links: [{"title":"Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/pdf/2407.01449"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/html/2506.04997v1"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/pdf/2506.04997"},{"title":"CausalEmbed: Auto-Regressive Multi-Vector Generation in Latent Space for Visual Document Embedding","url":"https://arxiv.org/pdf/2601.21262"},{"title":"[2506.04997] Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/abs/2506.04997"},{"title":"Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework","url":"https://arxiv.org/pdf/2602.19549"},{"title":"Structural Anchor Pruning: Training-Free Multi-Vector Compression for Visual Document Retrieval","url":"https://arxiv.org/html/2601.20107"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1003/"}]

I've completed the web search for "visual document retrieval" with focus on efficient token compression and embedding reduction from recent arxiv papers (2025-2026). Here are the key findings:

## Recent Research on Efficient Visual Document Retrieval

Several recent papers address the challenge of reducing patch-level embeddings while maintaining retrieval performance:

**Light-ColPali/ColQwen2 (2025)**
A token-reduction approach that integrates semantic clustering at the latest stage of the pipeline, combined with fine-tuning, to achieve efficient and accurate visualized document retrieval. It retains 98.2% of NDCG@5 scores with only 11.8% of original memory footprint and maintains 94.6% effectiveness at just 2.8% memory footprint.

**CausalEmbed (2026)**
An auto-regressive method that enables efficient VDR tasks using only dozens of visual tokens, achieving a 30–155× reduction in token count while maintaining highly competitive performance.

**Token Reduction Approaches**
Two common token-reduction approaches are token pruning and token merging. However, random pruning performs better than other carefully designed strategies.

**Recent Framework (2026)**
A Prune-then-Merge framework addresses information loss of pure pruning with a two-stage pipeline: adaptive pruning is followed by hierarchical merging that aggregates the discarded patches into summary representations.

These papers demonstrate significant progress in making visual document retrieval more storage and computationally efficient.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cdc33ff-69f8-4e47-b3b8-5ee12a7c9279",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "9f7a5643-7d3c-4ad6-a115-24f134e0e95b",
  "sourceToolAssistantUUID": "0cdc33ff-69f8-4e47-b3b8-5ee12a7c9279",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-30T06:16:51.040Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017jQYTSzsaTNa7nZ74yuzGH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.24621",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f7a5643-7d3c-4ad6-a115-24f134e0e95b",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGK56fgnaMFhBF6k8zY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "882c707f-c72b-4f87-b939-1426423d4741",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjFnRkWAjt2nLmLDpLm593",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2259,
      "cache_read_input_tokens": 43378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2259,
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

_source line 153 · 2026-05-30T06:16:51.984Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V4bm7cVUoB89z2xqRQdJJv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21262",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (CausalEmbed)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "882c707f-c72b-4f87-b939-1426423d4741",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGK56fgnaMFhBF6k8zY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a35f00c2-f607-47ee-b95c-4594de346799",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjFnRkWAjt2nLmLDpLm593",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2259,
      "cache_read_input_tokens": 43378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2259,
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

_source line 154 · 2026-05-30T06:16:52.452Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GbwFFuToXqVbkmgppVC9gJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20107",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (Structural Anchor Pruning)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a35f00c2-f607-47ee-b95c-4594de346799",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGK56fgnaMFhBF6k8zY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9322e86d-1ec8-4eca-9458-c39821987b1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjFnRkWAjt2nLmLDpLm593",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2259,
      "cache_read_input_tokens": 43378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2259,
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

_source line 155 · 2026-05-30T06:16:53.403Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BJmGd8vPkT3EHGhFn8y8iw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10167",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (Visual Late Chunking)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9322e86d-1ec8-4eca-9458-c39821987b1d",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGK56fgnaMFhBF6k8zY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27966c00-827f-4fb2-8061-ccf3066ff619",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjFnRkWAjt2nLmLDpLm593",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2259,
      "cache_read_input_tokens": 43378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2259,
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

_source line 156 · 2026-05-30T06:16:54.332Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MxYotoDDhQQ2cgP74cxkme`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.22278",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (RetLLM)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27966c00-827f-4fb2-8061-ccf3066ff619",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGK56fgnaMFhBF6k8zY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f354d9e0-e5c1-4871-8373-566b1931b290",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjFnRkWAjt2nLmLDpLm593",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2259,
      "cache_read_input_tokens": 43378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2259,
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

_source line 157 · 2026-05-30T06:16:55.387Z_

<details><summary>↩ Tool result · `toolu_017jQYTSzsaTNa7nZ74yuzGH`</summary>

```text
# Paper Information

**Full Title:** "FreeRet: MLLMs as Training-Free Retrievers"

**Authors:** Yuhan Zhu, Xiangyu Zeng, Chenting Wang, Xinhao Li, Chunxu Liu, Yicheng Xu, Ziang Yan, Yi Wang, and Limin Wang

**Submission Date:** September 29, 2025 (v1); last revised May 25, 2026 (v3)

**Abstract Summary:**

The paper proposes that multimodal large language models can function as effective retrievers without requiring additional training. The framework accomplishes this through a two-stage approach: first extracting semantically meaningful embeddings for candidate retrieval, then leveraging the model's reasoning capabilities for refined ranking. Key innovations include "bypassing lexical alignment layers to obtain semantically faithful embeddings, conditioning representation generation with explicit priors, and mitigating framing effect in reranking via neutral choice framing." Testing across 46 datasets showed the method significantly surpassed trained baseline models while remaining compatible with various MLLM architectures and maintaining their generative functions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "882c707f-c72b-4f87-b939-1426423d4741",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "4a29df32-9304-4e9f-8f4e-248581be1691",
  "sourceToolAssistantUUID": "882c707f-c72b-4f87-b939-1426423d4741",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-30T06:16:56.471Z_

<details><summary>↩ Tool result · `toolu_01V4bm7cVUoB89z2xqRQdJJv`</summary>

```text
# CausalEmbed Paper Details

**Full Title:** "CausalEmbed: Auto-Regressive Multi-Vector Generation in Latent Space for Visual Document Embedding"

**Authors:** Jiahao Huo, Yu Huang, Yibo Yan, Ye Pan, Kening Zheng, Wei-Chieh Huang, Yi Cao, Mingdong Ou, Philip S. Yu, and Xuming Hu

**Submission Date:** January 29, 2026 (last revised April 16, 2026)

**Abstract Summary:**

The paper addresses storage challenges in Visual Document Retrieval systems using Multimodal Large Language Models. The authors propose an auto-regressive generation method that "encourages the embedding models to learn compact and well-structured representations." 

Key achievements include:
- Reduces token count by 30-155x compared to traditional approaches
- Maintains competitive performance across various benchmarks
- Uses only dozens of visual tokens instead of thousands
- Provides flexible test-time scaling strategies for multi-vector representations

The research contributes to making document retrieval more practical for real-world deployment by substantially lowering computational and storage requirements while preserving effectiveness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a35f00c2-f607-47ee-b95c-4594de346799",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "85344d37-7440-47b1-9d81-cc453267564e",
  "sourceToolAssistantUUID": "a35f00c2-f607-47ee-b95c-4594de346799",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-30T06:16:56.883Z_

<details><summary>↩ Tool result · `toolu_01BJmGd8vPkT3EHGhFn8y8iw`</summary>

```text
# Visual Late Chunking Paper Details

**Full Title:** "Visual Late Chunking: An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval"

**Authors:** Yibo Yan, Mingdong Ou, Yi Cao, Jiahao Huo, Xin Zou, Shuliang Liu, James Kwok, Xuming Hu

**Submission Date:** April 11, 2026

**Abstract:** The researchers propose ColChunk, a framework addressing efficiency challenges in Visual Document Retrieval. They employ "hierarchical clustering on patch-level embeddings, fused with a 2D position prior" to create contextualized multi-vector representations. Their approach achieves "over a 90% reduction in storage requirements while simultaneously delivering a 9-point average improvement in nDCG@5" across representative single-vector models. The method balances retrieval accuracy with computational efficiency in visual document systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27966c00-827f-4fb2-8061-ccf3066ff619",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "990cef76-5b9b-4797-92ec-0f1de3d80979",
  "sourceToolAssistantUUID": "27966c00-827f-4fb2-8061-ccf3066ff619",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-30T06:16:57.069Z_

<details><summary>↩ Tool result · `toolu_01GbwFFuToXqVbkmgppVC9gJ`</summary>

```text
# Structural Anchor Pruning Paper Details

**Full Title:** "Structural Anchor Pruning: Training-Free Multi-Vector Compression for Visual Document Retrieval"

**Authors:** Zhuchenyang Liu, Ziyu Hu, Yao Zhang, Yu Xiao

**Submission Date:** January 27, 2026 (v1); Last revised May 21, 2026 (v2)

**Abstract Summary:**

The paper addresses storage challenges in Vision-Language Models used for document retrieval. The authors propose SAP, a framework that eliminates the need for model training while compressing visual token data. Their method includes three key components: a diagnostic tool for evaluating per-layer compression, an automated procedure for identifying optimal pruning regions, and a scoring mechanism to select important image patches.

The research demonstrates that SAP "retains over 90% of NDCG@5 while pruning more than 90% of visual tokens" across multiple architectures without requiring model-specific adjustments. A notable discovery is the identification of an "Alignment-Aggregation Divergence" showing that document visual structure remains stable through intermediate network layers but becomes sparse and query-specific in final layers, explaining why previous pruning approaches focusing on final layers proved ineffective.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9322e86d-1ec8-4eca-9458-c39821987b1d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "b48cfeef-a207-4337-9b21-ac58855e9d78",
  "sourceToolAssistantUUID": "9322e86d-1ec8-4eca-9458-c39821987b1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-30T06:16:57.532Z_

<details><summary>↩ Tool result · `toolu_01MxYotoDDhQQ2cgP74cxkme`</summary>

```text
# RetLLM Paper Details

**Full Title:**
"RETLLM: Training and Data-Free MLLMs for Multimodal Information Retrieval"

**Authors:**
Dawei Su and Dongsheng Wang

**Submission Date:**
February 25, 2026

**Abstract:**
The paper introduces a novel framework that enables multimodal large language models to perform retrieval tasks without requiring training or large datasets. The approach formulates retrieval as a scoring task and uses a two-stage pipeline: an initial filtering stage that creates a high-quality candidate set, followed by a scoring stage that predicts relevance. The researchers also propose a visual enhancement module to help the models better utilize image information. According to the abstract, "extensive experiments on MMIR benchmarks show that RetLLM outperforms fine-tuned models," and the work "demonstrates that MLLMs can achieve strong MMIR performance without any training."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f354d9e0-e5c1-4871-8373-566b1931b290",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "2f929181-169b-46ac-a1a0-d4a1ed7092e5",
  "sourceToolAssistantUUID": "f354d9e0-e5c1-4871-8373-566b1931b290",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 162 · 2026-05-30T06:17:02.173Z_

Let me do a final round of searches to find a few more unique papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f929181-169b-46ac-a1a0-d4a1ed7092e5",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGKpuR71vYtsX1LwoCs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f9b35b4-4bef-4a95-b6ab-4cba12aeb3e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxH8AjvytSaFgqAX3wz49s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 45637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
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

_source line 163 · 2026-05-30T06:17:02.710Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TTrTTrgVJq7RwaJapnT1Rx`</summary>

```json
{
  "query": "MMEB multimodal embedding benchmark arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f9b35b4-4bef-4a95-b6ab-4cba12aeb3e7",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGKpuR71vYtsX1LwoCs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bf99bff-c9ff-4b73-b73c-e1d4bd052ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxH8AjvytSaFgqAX3wz49s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 45637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
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

_source line 164 · 2026-05-30T06:17:03.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qe9Zfm1yVrSXXXJA6J9Tfv`</summary>

```json
{
  "query": "VLM document OCR-free retrieval table chart understanding arxiv 2025 2026 new methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bf99bff-c9ff-4b73-b73c-e1d4bd052ace",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGKpuR71vYtsX1LwoCs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "728c3993-3c73-42b5-8f22-b9fb83c13ff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxH8AjvytSaFgqAX3wz49s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 45637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
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

_source line 165 · 2026-05-30T06:17:08.481Z_

<details><summary>↩ Tool result · `toolu_01TTrTTrgVJq7RwaJapnT1Rx`</summary>

```text
Web search results for query: "MMEB multimodal embedding benchmark arxiv 2024 2025"

Links: [{"title":"MetaEmbed: Scaling Multimodal Retrieval at Test-Time ...","url":"https://arxiv.org/pdf/2509.18095"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=TE0KOzWYAF"},{"title":"Explore More, Learn Better: Parallel MLLM Embeddings under Mutual Information Minimization","url":"https://arxiv.org/pdf/2511.01588"},{"title":"VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks","url":"https://tiger-ai-lab.github.io/VLM2Vec/"},{"title":"Breaking the Modality Barrier: Universal Embedding Learning with Multimodal LLMs","url":"https://arxiv.org/html/2504.17432"},{"title":"GitHub - TIGER-AI-Lab/VLM2Vec: This repo contains the code for \"VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks\" [ICLR 2025] · GitHub","url":"https://github.com/TIGER-AI-Lab/VLM2Vec"},{"title":"VLM2Vec: Training Vision-Language Models for Massive Multimodal   Embedding Tasks","url":"https://arxiv.org/pdf/2410.05160"}]

Based on the search results, here's information about MMEB (Massive Multimodal Embedding Benchmark):

## Overview

MMEB (Massive Multimodal Embedding Benchmark) includes 36 datasets spanning four meta-task categories: classification, visual question answering, retrieval, and visual grounding. MMEB provides a comprehensive framework for training and evaluating embedding models across various combinations of text and image modalities, with all tasks reformulated as ranking tasks.

## Key Details

MMEB is divided into 20 in-distribution datasets for training, and 16 out-of-distribution datasets reserved for evaluation. MMEB was introduced in the context of VLM2Vec (published at ICLR 2025), a contrastive training framework that transforms vision-language models into embedding models through training on MMEB.

## Recent Developments

An extended version called MMEB-V2 includes 78 tasks total and extends the benchmark with videos and visual documents for systematically evaluating embedding models across multiple modalities.

The benchmark has become a standard for evaluating multimodal embedding models, with various recent works using it to evaluate their approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bf99bff-c9ff-4b73-b73c-e1d4bd052ace",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "a62ee573-423f-4103-aacd-43d1eb58b18a",
  "sourceToolAssistantUUID": "4bf99bff-c9ff-4b73-b73c-e1d4bd052ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-30T06:17:11.110Z_

<details><summary>↩ Tool result · `toolu_01Qe9Zfm1yVrSXXXJA6J9Tfv`</summary>

```text
Web search results for query: "VLM document OCR-free retrieval table chart understanding arxiv 2025 2026 new methods"

Links: [{"title":"MMDocBench: Benchmarking Large Vision-Language Models for Fine-Grained   Visual Document Understanding","url":"https://arxiv.org/pdf/2410.21311"},{"title":"Enhanced Chart Understanding in Vision and Language Task via Cross-modal   Pre-training on Plot Table Pairs","url":"https://arxiv.org/pdf/2305.18641"},{"title":"Hierarchical Visual Feature Aggregation for OCR-Free Document   Understanding","url":"https://arxiv.org/pdf/2411.05254"},{"title":"mPLUG-DocOwl 1.5: Unified Structure Learning for OCR-free Document   Understanding","url":"https://arxiv.org/pdf/2403.12895"},{"title":"Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding","url":"https://arxiv.org/html/2510.15253v3"}]

I found relevant research on VLM document understanding with OCR-free methods. Here are the key findings:

## OCR-Free Document Understanding Methods

Recent approaches design OCR-free document understanding tasks from perspectives of fine-grained visual perception and reasoning, where understanding partial and fine-grained details in images is crucial.

## Notable Recent Approaches

Donut and Pix2Struct propose OCR-free pre-training frameworks, where the pre-trained model directly generates text output from raw image input. Recent work emphasizes the importance of structure information in Visual Document Understanding and proposes Unified Structure Learning comprising structure-aware parsing tasks and multi-grained text localization tasks across 5 domains: document, webpage, table, chart, and natural image.

## OCR-Free Retrieval Methods

Recent methods such as DSE and ColPali leverage vision-language models (VLMs) to encode document pages directly into image embeddings, achieving significant efficiency gains. Light-ColPali and HPC-ColPali improve efficiency of ColPali-style multi-vector retrieval by compressing patch-level representations.

## Handling Complex Elements

Document understanding frameworks without external OCR engines face significant challenges in considering multiple scales of document images, as text and visual elements often vary in size and style, and complex graphical elements such as charts and diagrams pose additional difficulties.

These recent works (2024-2026) show a clear trend toward efficient, OCR-free approaches using visual language models for document, table, and chart understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "728c3993-3c73-42b5-8f22-b9fb83c13ff3",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "e321765f-f43b-4973-adb2-841a08acd77d",
  "sourceToolAssistantUUID": "728c3993-3c73-42b5-8f22-b9fb83c13ff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-30T06:17:14.309Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K1xJZzyFHwbrs7vekA9J4w`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.05160",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (VLM2Vec)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e321765f-f43b-4973-adb2-841a08acd77d",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGLpuCS4NgFy9BrVLBK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d4a2402-ff63-4585-bc21-16fe797c21a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoihM7srZUWH2Gyx1XdFX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 47438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-30T06:17:15.000Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Tv7QLyr883Bs73EYyxXwrU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.21311",
  "prompt": "Extract the full title, authors, submission date, and abstract of this paper (MMDocBench)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d4a2402-ff63-4585-bc21-16fe797c21a0",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGLpuCS4NgFy9BrVLBK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57d8ad88-f2cc-41c4-b8c8-eb02f3e22432",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoihM7srZUWH2Gyx1XdFX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 47438,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1455
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 47438,
          "cache_creation_input_tokens": 1455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1455,
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

_source line 169 · 2026-05-30T06:17:18.501Z_

<details><summary>↩ Tool result · `toolu_01K1xJZzyFHwbrs7vekA9J4w`</summary>

```text
# VLM2Vec Paper Details

**Full Title:**
"VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks"

**Authors:**
Ziyan Jiang, Rui Meng, Xinyi Yang, Semih Yavuz, Yingbo Zhou, Wenhu Chen

**Submission Date:**
October 7, 2024 (with revisions on October 11, 2024 and January 2, 2025)

**Abstract Summary:**
The work introduces two key contributions to multimodal embedding research. First, the authors developed MMEB, a benchmark spanning four meta-task categories and 36 datasets for evaluating embedding models. Second, they present VLM2Vec, a framework that transforms state-of-the-art vision-language models into embedding systems. Unlike earlier approaches such as CLIP and BLIP, this method can "process any combination of images and text to generate a fixed-dimensional vector based on task instructions." Testing on models like Phi-3.5-V and LLaVA-1.6 demonstrates significant performance gains, with "an absolute average improvement of 10% to 20% over existing multimodal embedding models."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d4a2402-ff63-4585-bc21-16fe797c21a0",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "7437c25f-2ec3-4ac3-9c75-4281038d6900",
  "sourceToolAssistantUUID": "3d4a2402-ff63-4585-bc21-16fe797c21a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-30T06:17:20.062Z_

<details><summary>↩ Tool result · `toolu_01Tv7QLyr883Bs73EYyxXwrU`</summary>

```text
# MMDocBench Paper Information

**Full Title:** "MMDocBench: Benchmarking Large Vision-Language Models for Fine-Grained Visual Document Understanding"

**Authors:** Fengbin Zhu, Ziyang Liu, Xiang Yao Ng, Haohui Wu, Wenjie Wang, Fuli Feng, Chao Wang, Huanbo Luan, and Tat Seng Chua

**Submission Date:** October 25, 2024

**Abstract Summary:**

The researchers address gaps in evaluating how well advanced vision-language models handle detailed visual analysis. They introduce MMDocBench, a new assessment tool using document images to test fine-grained perception and reasoning. The benchmark comprises "15 main tasks with 4,338 QA pairs and 11,353 supporting regions," encompassing diverse materials like academic papers, receipts, financial records, tables, charts, and infographics. Testing covered sixteen models—both openly available and proprietary versions—to identify their capabilities and limitations across different document types and task categories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d8ad88-f2cc-41c4-b8c8-eb02f3e22432",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "a0dd57a49da85eaac",
  "type": "user",
  "uuid": "184154e5-8315-4d37-ae54-4b2e91e85468",
  "sourceToolAssistantUUID": "57d8ad88-f2cc-41c4-b8c8-eb02f3e22432",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 171 · 2026-05-30T06:20:37.536Z_

Now I have a comprehensive collection. Let me compile the final report.

---

Here is the literature survey. I have excluded the seed papers (ColPali, MMDocIR, Snappy, AGREE, ColParse, MURE, ViDoRe V3, RegionGPT) as requested.

---

## SURVEYS

**1. Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval**
- **Authors:** Yibo Yan et al.
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.19961
- **What it does:** A comprehensive survey of visual document retrieval in the MLLM era. Categorizes methods into multimodal embedding models, multimodal reranker models, and RAG+agentic integration. Covers the full pipeline from OCR-based to VLM-based retrieval approaches.
- **Why important:** The most dedicated and recent survey specifically focused on VDR. Provides a complete taxonomy of the field and identifies key challenges and future directions.

**2. Roles of MLLMs in Visually Rich Document Retrieval for RAG: A Survey**
- **Authors:** Xiantao Zhang
- **Date:** arXiv, December 2025
- **URL:** https://arxiv.org/abs/2601.03262
- **What it does:** Surveys how MLLMs address challenges in visually rich document retrieval for RAG, including layout-dependent semantics, brittle OCR, and evidence spread across tables/figures. Categorizes approaches into Modality-Unifying Captioners, Multimodal Embedders, and End-to-End Representers.
- **Why important:** Provides a focused analysis of the retrieval component specifically for visually rich documents in RAG pipelines, comparing approaches across granularity, preservation, efficiency, and compatibility.

**3. Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding**
- **Authors:** Sensen Gao et al.
- **Date:** arXiv, October 2025 (revised April 2026)
- **URL:** https://arxiv.org/abs/2510.15253
- **What it does:** Surveys multimodal RAG for document understanding across financial analysis, scientific discovery, and other domains. Proposes a taxonomy by domain, retrieval modality, and granularity, and reviews advances using graph structures and agentic systems.
- **Why important:** Bridges the gap between document understanding and RAG, covering datasets, benchmarks, applications, and industry implementation with a focus on holistic retrieval across all modalities.

**4. A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends**
- **Authors:** Yihao Ding et al.
- **Date:** arXiv, July 2025 (revised April 2026)
- **URL:** https://arxiv.org/abs/2507.09861
- **What it does:** Surveys how MLLMs interpret documents containing intricate visual, textual, and structural elements. Covers both OCR-based and OCR-free approaches, pretraining and instruction tuning methods, and emerging technologies like RAG and agent-based systems.
- **Why important:** Provides the most detailed treatment of the document understanding side (as opposed to retrieval), which is the upstream capability that visual retrieval systems rely on.

**5. A Survey of Multimodal Retrieval-Augmented Generation**
- **Authors:** Lang Mei et al.
- **Date:** arXiv, March 2025
- **URL:** https://arxiv.org/abs/2504.08748
- **What it does:** Reviews MRAG's essential components, datasets, and evaluation methods for incorporating diverse data types (text, images, videos) into retrieval and generation. Demonstrates MRAG outperforms traditional RAG in scenarios requiring both visual and textual understanding.
- **Why important:** An ACL 2025 paper providing a comprehensive taxonomy of multimodal RAG, establishing the field's foundations and evaluation standards.

**6. Retrieval Augmented Generation and Understanding in Vision: A Survey and New Outlook**
- **Authors:** Xu Zheng et al.
- **Date:** arXiv, March 2025
- **URL:** https://arxiv.org/abs/2503.18016
- **What it does:** Surveys retrieval-augmented techniques in computer vision across visual understanding (image recognition to medical report generation) and visual generation (image, video, 3D creation). Also explores RAG for embodied AI.
- **Why important:** Broadens the RAG discussion beyond documents to the full scope of computer vision, identifying how retrieval augmentation is transforming diverse vision tasks.

**7. Vision Language Models: A Survey of 26K Papers**
- **Authors:** Fengming Lin
- **Date:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.09586
- **What it does:** Analyzes 26,104 papers accepted at CVPR, ICLR, and NeurIPS (2023-2025) using automated topic labeling. Identifies that multimodal VLM work consumes 40% of accepted papers by 2025, with a decisive pivot toward instruction following and reasoning.
- **Why important:** Provides macro-level evidence of the massive growth of VLM research and the dominance of instruction tuning over encoder-from-scratch approaches, contextualizing the VDR subfield within the broader landscape.

---

## BENCHMARKS

**8. ViDoRe Benchmark V2: Raising the Bar for Visual Retrieval**
- **Authors:** Quentin Mace et al.
- **Date:** arXiv, May 2025
- **URL:** https://arxiv.org/abs/2505.17166
- **What it does:** Addresses saturation of the original ViDoRe benchmark (top models exceeding 90% nDCG@5) by introducing harder scenarios including contextual blind querying, extended cross-document queries, and mixed synthetic/human-validated questions across four multilingual datasets.
- **Why important:** The standard benchmark for visual document retrieval. V2 restores discriminative power and reveals substantial room for advancement, making it the primary evaluation target for new VDR methods.

**9. MIRACL-VISION: A Large, Multilingual, Visual Document Retrieval Benchmark**
- **Authors:** Radek Osmulski et al.
- **Date:** arXiv, May 2025
- **URL:** https://arxiv.org/abs/2505.11651
- **What it does:** Extends the MIRACL text retrieval benchmark to visual document retrieval across 18 languages. Reveals that VLM-based retrieval models underperform text-based models by up to 59.7% on non-English tasks and 12.1% on English.
- **Why important:** Exposes a critical multilingual gap in visual retrieval, demonstrating that current VDR models are far behind text-based systems for non-English content. Essential for driving multilingual VDR research.

**10. jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval (incl. Jina-VDR Benchmark)**
- **Authors:** Michael Gunther et al.
- **Date:** arXiv, June 2025
- **URL:** https://arxiv.org/abs/2506.18902
- **What it does:** Introduces a 3.8B parameter multimodal embedding model supporting both single and multi-vector embeddings with task-specific LoRA adapters. Also introduces Jina-VDR, a 95-task, 20-language benchmark for visually rich document retrieval with 70K+ documents.
- **Why important:** Both a strong baseline model and a major benchmark. Jina-VDR's 95-task scope across 20 languages makes it one of the most comprehensive VDR evaluation resources available.

**11. MRMR: A Realistic and Expert-Level Multidisciplinary Benchmark for Reasoning-Intensive Multimodal Retrieval**
- **Authors:** Siyue Zhang et al.
- **Date:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.09510
- **What it does:** Introduces 1,502 expert-verified queries across 23 domains requiring intensive reasoning (e.g., diagnosing microscopic slides). Introduces contradiction retrieval as a novel task and uses image-text interleaved sequences for realistic evaluation.
- **Why important:** Pushes multimodal retrieval evaluation beyond surface-level matching toward genuine reasoning. Reveals that text embedding models with captions outperform specialized multimodal systems, highlighting the reasoning gap.

**12. Double-Bench (Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?)**
- **Authors:** Wenxuan Shen et al.
- **Date:** arXiv, August 2025
- **URL:** https://arxiv.org/abs/2508.03644
- **What it does:** Introduces a large-scale, multilingual, multimodal evaluation system with 3,000+ documents and 5,000+ queries across six languages. Tests nine embedding models, four MLLMs, and four end-to-end frameworks. Identifies an "over-confidence dilemma" in current document RAG.
- **Why important:** Finds that the gap between text and visual embedding models is shrinking, while exposing a systemic problem where RAG systems provide answers even without supporting evidence. Plans annual updates to prevent data contamination.

**13. VisR-Bench: An Empirical Study on Visual Retrieval-Augmented Generation for Multilingual Long Document Understanding**
- **Authors:** Jian Chen et al.
- **Date:** arXiv, August 2025
- **URL:** https://arxiv.org/abs/2508.07493
- **What it does:** Introduces a question-driven multilingual benchmark with 35K QA pairs from 1,200 documents across 16 languages. Queries are designed to prevent superficial keyword matching. Evaluates retrieval across figures, text, and tables.
- **Why important:** First benchmark specifically targeting retrieval-augmented QA over long, visually rich documents with multilingual coverage. Reveals that MLLMs struggle with structured tables and low-resource languages.

**14. Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark**
- **Authors:** Goeric Huybrechts et al.
- **Date:** arXiv, July 2025
- **URL:** https://arxiv.org/abs/2507.15882
- **What it does:** Creates a "needle-in-a-haystack" style benchmark with documents ranging from 5 to 200 pages. Inserts text and multimodal text+image needles at various depths, generating 400 document variants and 8,250 questions.
- **Why important:** Directly tests VLMs' ability to retrieve specific information from very long document contexts, a critical capability for real-world document understanding applications.

**15. irpapers: A Visual Document Benchmark for Scientific Retrieval and Question Answering**
- **Authors:** Connor Shorten et al.
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.17687
- **What it does:** Creates a benchmark of 3,230 pages from 166 scientific papers with both image and OCR versions. Shows text retrieval achieves 46% Recall@1 while combining text+image reaches 49%, demonstrating complementary strengths.
- **Why important:** Provides direct, controlled comparison between text-based and image-based retrieval on scientific documents, demonstrating the value of multimodal fusion.

**16. ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge**
- **Authors:** Yijie Lin et al.
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.09839
- **What it does:** Evaluates retrieval along two axes: knowledge domains (5 areas, 17 subcategories) and reasoning skills (6 types). Tests 23 retrievers with 16 different visual data types and targeted hard negatives requiring multi-step reasoning.
- **Why important:** Reveals significant performance gaps in fine-grained visual and spatial reasoning, providing a structured framework for understanding where retrievers succeed and fail.

**17. VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks (incl. MMEB)**
- **Authors:** Ziyan Jiang et al.
- **Date:** arXiv, October 2024 (ICLR 2025)
- **URL:** https://arxiv.org/abs/2410.05160
- **What it does:** Introduces MMEB (Massive Multimodal Embedding Benchmark) with 36 datasets across classification, VQA, retrieval, and visual grounding. Presents VLM2Vec, a framework that transforms VLMs into embedding models, achieving 10-20% improvement over existing multimodal embedding models.
- **Why important:** Established the MMEB benchmark that has become a standard evaluation suite for multimodal embedding models, and demonstrated the paradigm of converting generative VLMs into embedding models.

**18. MMDocBench: Benchmarking Large Vision-Language Models for Fine-Grained Visual Document Understanding**
- **Authors:** Fengbin Zhu et al.
- **Date:** arXiv, October 2024
- **URL:** https://arxiv.org/abs/2410.21311
- **What it does:** Introduces a benchmark with 15 tasks, 4,338 QA pairs, and 11,353 supporting regions across academic papers, receipts, financial records, tables, charts, and infographics. Tests 16 models for fine-grained perception and reasoning.
- **Why important:** Focuses on fine-grained perception (not just page-level retrieval), testing whether models can identify specific regions within documents -- a capability needed for grounded retrieval.

---

## RETRIEVAL METHODS AND SYSTEMS

**19. VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents**
- **Authors:** Shi Yu et al.
- **Date:** arXiv, October 2024 (ICLR 2025)
- **URL:** https://arxiv.org/abs/2410.10594
- **What it does:** Establishes a pure-vision RAG pipeline by directly embedding document pages as images using VLMs, bypassing text extraction entirely. Achieves 20-40% end-to-end performance gain over traditional text-based RAG.
- **Why important:** A foundational ICLR 2025 paper that demonstrated the feasibility and superiority of vision-based RAG over text-based RAG, establishing the paradigm that many subsequent VDR works build upon.

**20. Unifying Multimodal Retrieval via Document Screenshot Embedding (DSE)**
- **Authors:** Xueguang Ma et al.
- **Date:** arXiv, June 2024 (EMNLP 2024)
- **URL:** https://arxiv.org/abs/2406.11251
- **What it does:** Treats document screenshots as unified input format, encoding them with a VLM into dense representations. Outperforms BM25 by 17 points in top-1 accuracy and OCR-based methods by 15+ points in nDCG@10 for slide retrieval.
- **Why important:** Pioneered the screenshot-as-retrieval-unit paradigm. Demonstrated that directly encoding document images preserves information that text extraction loses, influencing ColPali and many subsequent methods.

**21. SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models**
- **Authors:** Thong Nguyen et al.
- **Date:** arXiv, September 2025
- **URL:** https://arxiv.org/abs/2509.15432
- **What it does:** Generates detailed textual descriptions of document images using a VLM, then applies standard text encoding. Achieves 63.4% nDCG@5 on ViDoRe-v2, outperforming specialized multi-vector encoders. Zero-shot, with no contrastive training.
- **Why important:** Demonstrates that modern VLMs can serve as semantic bridges for VDR without any task-specific training, establishing a strong zero-shot baseline and challenging the necessity of specialized retrieval training.

**22. Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval**
- **Authors:** Gabriel de Souza P. Moreira et al.
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.03992
- **What it does:** Introduces 3B, 4B, and 8B late interaction models for VDR. The 8B model achieved first place on the ViDoRe V3 leaderboard (63.42 NDCG@10). Key techniques include cluster-based sampling, hard-negative mining, bidirectional attention, and model merging.
- **Why important:** Current SOTA on the primary VDR benchmark. Demonstrates the scaling recipe and engineering decisions needed to build top-performing visual document retrievers.

**23. ModernVBERT: Towards Smaller Visual Document Retrievers**
- **Authors:** Paul Teiletche et al.
- **Date:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.01149
- **What it does:** Builds a compact 250M-parameter vision-language encoder that outperforms models up to 10x larger. Identifies critical factors including attention masking, image resolution, and modality alignment. Enables CPU-based deployment.
- **Why important:** Demonstrates that purpose-built bidirectional encoders dramatically outperform repurposed generative VLMs for retrieval. Achieves near-SOTA performance at a fraction of the parameter count, making VDR practical for resource-constrained settings.

**24. NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval**
- **Authors:** Zhuchenyang Liu et al.
- **Date:** arXiv, March 2026
- **URL:** https://arxiv.org/abs/2603.12824
- **What it does:** Uses asymmetric architecture: a frozen 2B VLM indexes documents offline while a 69M text-only model encodes queries at inference. Achieves 95.1% of teacher quality with 32x fewer parameters and 50x lower CPU query latency.
- **Why important:** Pushes efficiency to the extreme by showing query encoding does not need vision capabilities. Enables practical deployment where query latency is critical.

**25. Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model**
- **Authors:** Athos Georgiou
- **Date:** arXiv, March 2026
- **URL:** https://arxiv.org/abs/2603.28554
- **What it does:** Combines retrieval and generation in a single VLM using a dual-head design with a LoRA adapter toggle. Reduces peak GPU memory by 62.7% (from 28.85GB to 10.77GB at 4B). Releases Hydra-4B and Hydra-0.8B models.
- **Why important:** Addresses the practical problem of deploying separate retrieval and generation models. Demonstrates that a single model can serve both purposes without degradation in either task.

**26. FreeRet: MLLMs as Training-Free Retrievers**
- **Authors:** Yuhan Zhu et al.
- **Date:** arXiv, September 2025
- **URL:** https://arxiv.org/abs/2509.24621
- **What it does:** Turns any MLLM into a two-stage retriever without additional training: extracts semantically grounded embeddings for candidate search, then uses reasoning for reranking. Outperforms models trained on millions of pairs across 46 MMEB datasets.
- **Why important:** Demonstrates that off-the-shelf MLLMs already contain strong retrieval capabilities that can be unlocked without training. Model-agnostic and supports arbitrary modality combinations.

**27. RetLLM: Training and Data-Free MLLMs for Multimodal Information Retrieval**
- **Authors:** Dawei Su and Dongsheng Wang
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.22278
- **What it does:** Formulates retrieval as a scoring task with a two-stage pipeline (filtering + scoring) and a visual enhancement module. Outperforms fine-tuned models on MMIR benchmarks without any training.
- **Why important:** Reinforces the finding that training-free approaches can match or exceed fine-tuned models, suggesting the community should reconsider the cost/benefit of specialized training for multimodal retrieval.

**28. ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents**
- **Authors:** Qiuchen Wang et al.
- **Date:** EMNLP 2025, November 2025
- **URL:** https://aclanthology.org/2025.emnlp-main.464/
- **What it does:** Introduces ViDoSeek benchmark for evaluating RAG on complex visual documents. Proposes a GMM-based hybrid strategy for multimodal retrieval with iterative agent workflow (exploration, summarization, reflection). Achieves 10%+ improvement on ViDoSeek.
- **Why important:** Published at EMNLP 2025, combines visual retrieval with agentic reasoning, advancing beyond single-pass retrieval to iterative evidence gathering.

**29. MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval**
- **Authors:** Xixi Wu et al.
- **Date:** arXiv, September 2025 (EMNLP 2025)
- **URL:** https://arxiv.org/abs/2509.07666
- **What it does:** Constructs page graphs representing logical dependencies between document pages, then traverses these graphs to find both semantically and logically relevant pages. Achieves 9.68% accuracy improvement over LVLM direct inference and 7.44% retrieval precision gain.
- **Why important:** Introduces the concept of logical (not just semantic) relevance in document retrieval, addressing multi-hop reasoning scenarios where relevant information is spread across logically connected pages.

**30. Docs2Synth: A Synthetic Data Trained Retriever Framework for Scanned Visually Rich Documents Understanding**
- **Authors:** Yihao Ding et al.
- **Date:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.12260
- **What it does:** Automatically processes raw document collections, generates and verifies QA pairs via agents, and trains a lightweight visual retriever. At inference, the retriever collaborates with an MLLM through iterative retrieval-generation loops.
- **Why important:** Solves the critical data scarcity problem for domain-specific VDR (especially regulated sectors) by enabling training without human annotations, making VDR practical for private and low-resource domains.

**31. VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation**
- **Authors:** Yubo Sun et al.
- **Date:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.09733
- **What it does:** Extends VisRAG with evidence-guided multi-image reasoning: first observes retrieved images and records per-image evidence, then derives answers from aggregated evidence. Introduces Reward-Scoped Group Relative Policy Optimization. Achieves 27% average improvement.
- **Why important:** Advances the vision-based RAG paradigm from single-image to multi-image reasoning with explicit evidence tracking, addressing a key limitation of the original VisRAG.

**32. When Vision Meets Texts in Listwise Reranking (Rank-Nexus)**
- **Authors:** Hongyi Cai
- **Date:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.20623
- **What it does:** Extends listwise reranking to multimodal scenarios using a lightweight 2B parameter model. Jointly processes textual passages and images through a decoupled training approach. Competitive on TREC, BEIR, INQUIRE, and MMDocIR benchmarks.
- **Why important:** Addresses the reranking stage of the retrieval pipeline for multimodal documents, an underexplored area compared to first-stage retrieval.

**33. MLDocRAG: Multimodal Long-Context Document Retrieval Augmented Generation**
- **Authors:** Yongyue Zhang and Yaxiong Wu
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.10271
- **What it does:** Proposes a Multimodal Chunk-Query Graph structure that generates detailed questions from document sections and connects them across modalities and pages. Consistently improves retrieval quality and answer accuracy on MMLongBench-Doc and LongDocURL.
- **Why important:** Introduces graph-based cross-modal linking for long document retrieval, enabling retrieval of evidence that spans modalities and pages.

**34. AVIR: Adaptive Visual In-Document Retrieval for Efficient Multi-Page Document Question Answering**
- **Authors:** Zongmin Li et al.
- **Date:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.11976
- **What it does:** Proposes a lightweight page-scoring system that adaptively selects relevant pages using clustering, Top-K filtering, and relevance thresholds. Reduces average page count by 70% while achieving 84.58% ANLS on MP-DocVQA.
- **Why important:** Demonstrates that efficient adaptive retrieval can dramatically reduce the number of pages a VLM must process without sacrificing answer quality, addressing a key scalability challenge.

**35. Index Light, Reason Deep: Deferred Visual Ingestion for Visual-Dense Document Question Answering**
- **Authors:** Tao Xu
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.14162
- **What it does:** Eliminates VLM processing at indexing time, instead building hierarchical indices from structural elements and sending original images to VLMs only at query time. Achieves 65.6% accuracy on bridge engineering drawings vs. 24.3% for baselines.
- **Why important:** Challenges the dominant paradigm of VLM-based indexing, showing that for specialized engineering documents, lightweight structural indexing plus deferred visual reasoning vastly outperforms pre-computed visual embeddings.

---

## EFFICIENCY AND COMPRESSION

**36. DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning**
- **Authors:** Yibo Yan et al.
- **Date:** arXiv, September 2025
- **URL:** https://arxiv.org/abs/2509.23883
- **What it does:** Addresses storage overhead in multi-vector VDR by using attention-based adaptive pruning to identify and remove redundant patch embeddings. Achieves 50-60% storage reduction while maintaining retrieval performance.
- **Why important:** One of the first works to systematically address the storage bottleneck of ColPali-style multi-vector representations.

**37. Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings (Light-ColPali/ColQwen2)**
- **Authors:** Yubo Ma et al.
- **Date:** arXiv, June 2025 (ACL 2025 Findings)
- **URL:** https://arxiv.org/abs/2506.04997
- **What it does:** Compares token pruning vs. merging strategies for ColPali/ColQwen2. Finds that random pruning surprisingly outperforms complex methods, but merging is better suited overall. Light-ColPali retains 98.2% performance at 11.8% memory and 94.6% at 2.8%.
- **Why important:** ACL 2025 Findings paper that provides systematic empirical evidence on compression strategies, establishing that token merging is the right approach and achieving extreme compression ratios.

**38. Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework**
- **Authors:** Yibo Yan et al.
- **Date:** arXiv, February 2026
- **URL:** https://arxiv.org/abs/2602.19549
- **What it does:** Proposes a two-stage framework combining adaptive pruning (remove low-value patches) with hierarchical merging (compress remaining embeddings). Tests across 29 datasets, demonstrating improved performance and extended compression over prior methods.
- **Why important:** Advances beyond pure pruning by recovering information from discarded patches through merging, achieving better accuracy-efficiency tradeoffs than pruning or merging alone.

**39. CausalEmbed: Auto-Regressive Multi-Vector Generation in Latent Space for Visual Document Embedding**
- **Authors:** Jiahao Huo et al.
- **Date:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.21262
- **What it does:** Uses auto-regressive generation to produce compact, well-structured multi-vector representations in latent space. Achieves 30-155x token count reduction while maintaining competitive performance.
- **Why important:** Fundamentally rethinks how multi-vector embeddings are generated, moving from direct patch encoding to learned compact representations with flexible test-time scaling.

**40. Structural Anchor Pruning (SAP): Training-Free Multi-Vector Compression for Visual Document Retrieval**
- **Authors:** Zhuchenyang Liu et al.
- **Date:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.20107
- **What it does:** Proposes training-free compression that retains 90%+ of NDCG@5 while pruning 90%+ of visual tokens. Discovers "Alignment-Aggregation Divergence" -- document structure is stable in intermediate layers but becomes sparse/query-specific in final layers, explaining why prior final-layer pruning failed.
- **Why important:** Provides theoretical insight into why compression works (and when it doesn't) through the lens of layer-wise representation analysis, and achieves strong compression without any training.

**41. Visual Late Chunking (ColChunk): An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval**
- **Authors:** Yibo Yan et al.
- **Date:** arXiv, April 2026
- **URL:** https://arxiv.org/abs/2604.10167
- **What it does:** Employs hierarchical clustering on patch-level embeddings fused with 2D position priors to create contextualized multi-vector representations. Achieves 90%+ storage reduction with a 9-point nDCG@5 improvement for single-vector models.
- **Why important:** Shows that contextual chunking of visual patches can simultaneously improve retrieval accuracy AND reduce storage, rather than trading one for the other.

**42. HEAVEN: Hybrid-Vector Retrieval for Visually Rich Documents**
- **Authors:** Juyeon Kim et al.
- **Date:** arXiv, October 2025
- **URL:** https://arxiv.org/abs/2510.22215
- **What it does:** Two-stage approach: retrieves candidates via single-vector methods on summarized pages, then reranks with multi-vector methods. Achieves 99.87% of multi-vector Recall@1 while reducing compute by 99.82%. Also introduces ViMDoc benchmark.
- **Why important:** Demonstrates that the efficiency/accuracy tradeoff can be nearly eliminated through intelligent cascading, making multi-vector retrieval practical at scale.

---

## ROBUSTNESS AND ANALYSIS

**43. Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction**
- **Authors:** Jingfen Qiao et al.
- **Date:** arXiv, May 2025
- **URL:** https://arxiv.org/abs/2505.07730
- **What it does:** Evaluates whether late interaction mechanisms improve VDR across different VLMs. Confirms effectiveness but notes computational challenges. Reveals that query tokens tend to match patches with visually similar tokens, even without explicit text matching capability.
- **Why important:** Provides critical reproducibility analysis of the ColPali family, revealing how late interaction actually works mechanically and identifying robustness concerns with text-heavy datasets.

**44. Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks**
- **Authors:** Shengyao Zhuang et al.
- **Date:** arXiv, January 2025 (SIGIR 2025)
- **URL:** https://arxiv.org/abs/2501.16902
- **What it does:** Introduces three adversarial pixel poisoning attacks against VLM-based retrievers. A single malicious screenshot can poison top-10 results for 41.9% of DSE queries and 26.4% of ColPali queries -- rates exceeding attacks on text-only systems.
- **Why important:** SIGIR 2025 paper revealing critical security vulnerabilities in visual document retrieval. Essential reading for anyone deploying VDR systems in production, as these attack surfaces are unique to the vision-based paradigm.

**45. Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG**
- **Authors:** Martin Asenov et al.
- **Date:** arXiv, March 2026
- **URL:** https://arxiv.org/abs/2603.04238
- **What it does:** Shows that BM25 can close performance gaps with multimodal retrievers on multilingual and visual benchmarks when document representation (transcription/preprocessing) is improved. Argues evaluation should separate transcription quality from retrieval quality.
- **Why important:** A cautionary finding that challenges whether VDR gains come from better retrieval or just better document representation. Calls for more rigorous evaluation methodology.

**46. BM25-V: Visual Words Meet BM25 -- Sparse Auto-Encoder Visual Word Scoring for Image Retrieval**
- **Authors:** Donghoon Han et al.
- **Date:** arXiv, March 2026
- **URL:** https://arxiv.org/abs/2603.05781
- **What it does:** Applies BM25 scoring to sparse visual-word activations from a Sparse Auto-Encoder on ViT patch features. Achieves Recall@200 >= 0.993 across seven benchmarks as a first-stage retriever. Provides explainability through IDF contributions.
- **Why important:** Bridges classic information retrieval (BM25) with modern vision models, offering an interpretable and efficient alternative to dense visual retrieval. Demonstrates that sparse retrieval principles transfer to visual domains.

**47. Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks**
- **Authors:** Nathan Kuissi et al.
- **Date:** arXiv, March 2026
- **URL:** https://arxiv.org/abs/2603.04532
- **What it does:** Investigates temporal stability of retrieval benchmarks by comparing corpus snapshots from October 2024 and October 2025. Finds strong ranking correlation (0.978 Kendall tau at Recall@50) despite corpus evolution.
- **Why important:** Provides empirical evidence that retrieval benchmarks maintain reliability over time, addressing concerns about benchmark staleness.

---

## WORKSHOPS AND COMMUNITY

**48. The 1st EReL@MIR Workshop on Efficient Representation Learning for Multimodal Information Retrieval**
- **Authors:** Junchen Fu et al.
- **Date:** arXiv, April 2025 (Web Conference 2025)
- **URL:** https://arxiv.org/abs/2504.14788
- **What it does:** Organizes a workshop at The Web Conference 2025 addressing efficiency challenges in multimodal representation learning for information retrieval. Focuses on bridging the gap between large foundation model capabilities and practical deployment constraints.
- **Why important:** Signals community recognition that efficiency is a first-class research challenge for multimodal IR, not just a deployment concern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "184154e5-8315-4d37-ae54-4b2e91e85468",
  "isSidechain": true,
  "agentId": "a0dd57a49da85eaac",
  "requestId": "req_011CbYGMVBp95izPhZo6Pb4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3513c0c-36a7-43d3-879e-8904146ab239",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ljq6pqJwSRyCPpy53F8tc1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 48893,
      "output_tokens": 8877,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8877,
          "cache_read_input_tokens": 48893,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 769,
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
