# Research conversation: You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustne

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 1
- **Tool calls:** 38
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab1852e2a938e1f06.jsonl`
- **Structured JSON:** [`eaf24552451c6405712f.json`](../../sessions/ea/eaf24552451c6405712f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

87 recorded events

### User

_source line 1 · 2026-05-29T05:16:15.821Z_

You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation using Item Response Theory.

Search for the most important recent papers (2024-2026) on Item Response Theory applied to LLM evaluation. Execute these searches:

1. WebSearch: "item response theory LLM evaluation 2025 2026"
2. WebSearch: "ATLAS IRT adaptive testing large language models 2025"
3. WebSearch: "PSN-IRT LLM benchmark evaluation 2024 2025"
4. WebSearch: "computerized adaptive testing LLM ability estimation 2025"
5. WebSearch: "measurement theory psychometrics LLM evaluation calibration 2025"

For each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.

Focus on papers that:
- Apply IRT or other psychometric models to LLM evaluation
- Propose adaptive testing for efficient LLM benchmarking
- Use measurement theory to produce calibrated ability scores
- Study item difficulty and discrimination for LLM test items

For each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.

Return a structured list of ALL papers found with these details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "4b06ab07-4e9a-4f0e-8ed0-42397006efa4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:16:15.825Z_

```json
{
  "parentUuid": "4b06ab07-4e9a-4f0e-8ed0-42397006efa4",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
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
  "uuid": "0d43ced8-71be-4a25-87fc-b06a57ab41bc",
  "timestamp": "2026-05-29T05:16:15.825Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:16:15.826Z_

```json
{
  "parentUuid": "0d43ced8-71be-4a25-87fc-b06a57ab41bc",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "51adc626-685f-4808-9bd7-c1a7d04b767c",
  "timestamp": "2026-05-29T05:16:15.826Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:16:18.513Z_



I'll start by loading the WebSearch and WebFetch tools, then execute all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51adc626-685f-4808-9bd7-c1a7d04b767c",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtTqRRY5qFf7QfmC9t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "205fad71-2f0b-47fc-947e-e19719000657",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZTmg8iimp7TkxFhXUToq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1647,
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

_source line 5 · 2026-05-29T05:16:18.684Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014Abj7aJT8DNHfMucwkjTYw`</summary>

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
  "parentUuid": "205fad71-2f0b-47fc-947e-e19719000657",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtTqRRY5qFf7QfmC9t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74a33a00-6ef2-415b-8e2e-1f6a0a5daaaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZTmg8iimp7TkxFhXUToq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 7413,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1647
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1647,
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

_source line 6 · 2026-05-29T05:16:18.689Z_

<details><summary>↩ Tool result · `toolu_014Abj7aJT8DNHfMucwkjTYw`</summary>

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
  "parentUuid": "74a33a00-6ef2-415b-8e2e-1f6a0a5daaaf",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "0c4c47ce-12a3-4309-b157-c26cc045b28e",
  "sourceToolAssistantUUID": "74a33a00-6ef2-415b-8e2e-1f6a0a5daaaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:16:21.265Z_



Now let me execute all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c4c47ce-12a3-4309-b157-c26cc045b28e",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtgHmrdu3hxaoiNjhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2365786-a5e9-424f-96eb-d220035d76a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch3MJ7DV1zQW2Tm4kvAD9K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 8 · 2026-05-29T05:16:21.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GxDPxFB8pfDAieKCABqiZd`</summary>

```json
{
  "query": "item response theory LLM evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2365786-a5e9-424f-96eb-d220035d76a6",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtgHmrdu3hxaoiNjhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "584e6104-9b53-4239-855b-b157b38347a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch3MJ7DV1zQW2Tm4kvAD9K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 9 · 2026-05-29T05:16:22.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A54nqwffdbyEsiXv1xVLAF`</summary>

```json
{
  "query": "ATLAS IRT adaptive testing large language models 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "584e6104-9b53-4239-855b-b157b38347a4",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtgHmrdu3hxaoiNjhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4141880-da87-4c70-977a-3c22ec1650c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch3MJ7DV1zQW2Tm4kvAD9K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 10 · 2026-05-29T05:16:22.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ULk358ZbbiKXkhjnasdcKQ`</summary>

```json
{
  "query": "PSN-IRT LLM benchmark evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4141880-da87-4c70-977a-3c22ec1650c0",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtgHmrdu3hxaoiNjhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85de9c1b-c247-4c66-ac25-cd0eed64ceda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch3MJ7DV1zQW2Tm4kvAD9K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 11 · 2026-05-29T05:16:22.654Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016PHeN4E2c1StEfRNa2Gc1e`</summary>

```json
{
  "query": "computerized adaptive testing LLM ability estimation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85de9c1b-c247-4c66-ac25-cd0eed64ceda",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtgHmrdu3hxaoiNjhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29e182c2-e619-41d4-bad1-858143dba676",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch3MJ7DV1zQW2Tm4kvAD9K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 12 · 2026-05-29T05:16:22.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJ49YGVnBZZqK8BjEVxPmc`</summary>

```json
{
  "query": "measurement theory psychometrics LLM evaluation calibration 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e182c2-e619-41d4-bad1-858143dba676",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHtgHmrdu3hxaoiNjhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "915a2379-7a5a-414f-b032-fa88caab03ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch3MJ7DV1zQW2Tm4kvAD9K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9060,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1125
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 9060,
          "cache_creation_input_tokens": 1125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1125,
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

_source line 13 · 2026-05-29T05:16:29.115Z_

<details><summary>↩ Tool result · `toolu_01GxDPxFB8pfDAieKCABqiZd`</summary>

```text
Web search results for query: "item response theory LLM evaluation 2025 2026"

Links: [{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://www.arxiv.org/pdf/2602.00521"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/html/2605.00238"},{"title":"Lifting the benchmark iceberg with item-response theory | OpenReview","url":"https://openreview.net/forum?id=ZyVQqK7mcP"},{"title":"[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/abs/2602.00521"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/pdf/2510.00844"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://arxiv.org/pdf/2509.22888"},{"title":"IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.761/"}]

Based on the search results, here are the key findings on item response theory (IRT) and LLM evaluation from 2025-2026:

## Recent Applications of IRT to LLM Evaluation

Recent work has applied IRT to LLM evaluation in several ways, including diagnosing the reliability of LLM-as-a-judge systems and modeling latent LLM abilities together with query difficulty and discrimination for routing and performance prediction.

## Key Research Areas

**LLM-as-a-Judge Reliability**: A two-phase diagnostic framework for assessing reliability of LLM-as-a-Judge has been introduced, grounded in Item Response Theory (IRT) and using the Graded Response Model (GRM) of IRT.

**Benchmark Analysis**: The Pseudo-Siamese Network for Item Response Theory (PSN-IRT) is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture, and analysis on 11 LLM benchmarks comprising 41,871 items has revealed significant shortcomings in their measurement quality.

**Model Routing**: IRT-Router explicitly models the relationship between LLM capabilities and user query attributes, enabling accurate prediction of response performance while providing interpretable insights such as LLM abilities and query difficulty.

**Compact Model Representations**: IrtNet pioneers the application of item response theory to formally model LLM abilities through an IRT-based framework that learns compact representations of LLM abilities.

**Geometric Modeling**: JE-IRT establishes a unified and interpretable geometric lens that connects LLM abilities with the structure of questions, offering a distinctive perspective on model evaluation and generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "584e6104-9b53-4239-855b-b157b38347a4",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "6ab33b68-466f-48b2-80f3-ac20b2b16daf",
  "sourceToolAssistantUUID": "584e6104-9b53-4239-855b-b157b38347a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T05:16:29.496Z_

<details><summary>↩ Tool result · `toolu_01ULk358ZbbiKXkhjnasdcKQ`</summary>

```text
Web search results for query: "PSN-IRT LLM benchmark evaluation 2024 2025"

Links: [{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"LLM Benchmarks","url":"https://www.emergentmind.com/topics/large-language-model-benchmarks"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Published as a conference paper at ICLR 2025 ME TABENCH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs","url":"https://arxiv.org/pdf/2602.11674"},{"title":"(PDF) Evaluation and Benchmarking of LLM Agents: A Survey","url":"https://www.researchgate.net/publication/394100858_Evaluation_and_Benchmarking_of_LLM_Agents_A_Survey"},{"title":"LLM evaluation benchmarks and safety datasets for 2025 | RAIL Score Knowledge Hub","url":"https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025"}]

Based on the search results, here's what I found about PSN-IRT LLM benchmark evaluation:

## Overview

PSN-IRT is a proposed method where separate neural networks estimate model-ability, which are then combined via the IRT formula to predict the probability of a correct response.

## Key Features

PSN-IRT is a multi-dimensional, compositional, or item-level psychometric model that models item discriminability, guessing rates, and difficulty. PSN-IRT diagnostic frameworks have shown that current benchmarks often lack items with the right combination of difficulty and discriminative power, leading to poor alignment with human preferences and real-world distinctions.

## Research Findings

PSN-IRT analysis of mainstream benchmarks found that current LLM benchmarks present deficiencies in many aspects. Additionally, selecting items with PSN-IRT leads to model rankings that better align with human preference.

## Efficiency Benefits

PSN-IRT can facilitate more efficient benchmarking by investigating whether strategically curating smaller, highly informative item sets can yield model comparisons that maintain or even surpass the accuracy and reliability of larger, undifferentiated collections.

The research appears to be from a recent ArXiv paper titled "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" published in January 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85de9c1b-c247-4c66-ac25-cd0eed64ceda",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "86480cc5-e0f0-4245-a832-99a3ded07666",
  "sourceToolAssistantUUID": "85de9c1b-c247-4c66-ac25-cd0eed64ceda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-29T05:16:29.789Z_

<details><summary>↩ Tool result · `toolu_016PHeN4E2c1StEfRNa2Gc1e`</summary>

```text
Web search results for query: "computerized adaptive testing LLM ability estimation 2025"

Links: [{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | OpenReview","url":"https://openreview.net/forum?id=iX39LhePyd"},{"title":"[2511.04689] Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/abs/2511.04689"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/html/2601.13885"},{"title":"[2306.10512] Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective","url":"https://ar5iv.labs.arxiv.org/html/2306.10512"},{"title":"ADAPTIVE TESTING FOR LLM EVALUATION: A","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective | OpenReview","url":"https://openreview.net/forum?id=s6X3s3rBPW"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"}]

Based on the search results, here's what I found on computerized adaptive testing for LLM ability estimation in 2025:

## Recent Developments

ATLAS is an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information-guided item selection, reducing the number of required items by up to 90% while maintaining measurement precision.

Computerized Adaptive Testing (CAT) dynamically selects informative test items to estimate model capabilities with far fewer evaluations than exhaustive benchmarking, and has emerged as a promising approach for efficient evaluation of large language models.

## Key Technical Approach

ATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability, terminating when precision thresholds are reached.

## Performance Results

On HellaSwag (5,600 items), the framework matches whole-bank ability estimates using only 41 items with 0.157 mean absolute error. Additionally, among more than 3,000 evaluated models, 23-31% shift by more than 10 rank positions, and models with identical accuracies receive meaningfully different ability estimates.

This represents a significant advancement in making LLM evaluation more efficient and psychometrically sound by borrowing methodology from educational assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29e182c2-e619-41d4-bad1-858143dba676",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "cd9ca6a4-f4ac-4a83-928b-026cfce7580c",
  "sourceToolAssistantUUID": "29e182c2-e619-41d4-bad1-858143dba676",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T05:16:30.508Z_

<details><summary>↩ Tool result · `toolu_01A54nqwffdbyEsiXv1xVLAF`</summary>

```text
Web search results for query: "ATLAS IRT adaptive testing large language models 2025"

Links: [{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | OpenReview","url":"https://openreview.net/forum?id=iX39LhePyd"},{"title":"[2511.04689] Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/abs/2511.04689"},{"title":"ATLAS: Adaptive Test-Time Latent Steering with External Verifiers for Enhancing LLMs’ Reasoning","url":"https://arxiv.org/html/2601.03093v1"},{"title":"ADAPTIVE TESTING FOR LLM EVALUATION: A","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"(PDF) ATLAS: Adaptive Test-Time Latent Steering with External Verifiers for Enhancing LLMs Reasoning","url":"https://www.researchgate.net/publication/399522278_ATLAS_Adaptive_Test-Time_Latent_Steering_with_External_Verifiers_for_Enhancing_LLMs_Reasoning"},{"title":"Latency-Response Theory Model: Evaluating Large Language","url":"https://www.arxiv.org/pdf/2512.07019"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length","url":"https://arxiv.org/html/2512.07019"}]

Based on the search results, here's what I found about ATLAS and IRT adaptive testing for large language models in 2025:

## Overview

ATLAS is an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information–guided item selection. Evaluating large language models (LLMs) typically requires thousands of benchmark items, making the process expensive, slow, and increasingly impractical at scale.

## Key Performance Benefits

ATLAS reduces the number of required items by up to 90% while maintaining measurement precision. More specifically, it matches whole-bank ability estimates using only 41 items (0.157 MAE) on HellaSwag (5,600 items).

## How It Works

ATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters. Then, rather than administering fixed item sets, ATLAS dynamically selects items with maximum Fisher information for each model's current estimated ability, terminating when precision thresholds are reached.

## Validation and Scope

The framework was validated across five major benchmarks (WinoGrande, TruthfulQA, HellaSwag, GSM8K, ARC). ATLAS uses a substantially larger and more diverse pool of 3,000+ LMs for IRT calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4141880-da87-4c70-977a-3c22ec1650c0",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "ef98275e-3829-44eb-8118-b91a8fe88229",
  "sourceToolAssistantUUID": "c4141880-da87-4c70-977a-3c22ec1650c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T05:16:30.694Z_

<details><summary>↩ Tool result · `toolu_01DJ49YGVnBZZqK8BjEVxPmc`</summary>

```text
Web search results for query: "measurement theory psychometrics LLM evaluation calibration 2025"

Links: [{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689v2"},{"title":"Rethinking psychometrics through LLMs: how item semantics shape measurement and prediction in psychological questionnaires | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-21289-8"},{"title":"Leveraging LLM respondents for item evaluation: A psychometric analysis - Liu - 2025 - British Journal of Educational Technology - Wiley Online Library","url":"https://bera-journals.onlinelibrary.wiley.com/doi/pdf/10.1111/bjet.13570"},{"title":"Psychometric Benchmarks for AI Evaluation","url":"https://www.emergentmind.com/topics/psychometrically-informed-benchmarks"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"https://llm-psychometrics.com/"},{"title":"LLM Psychometrics Review","url":"https://www.emergentmind.com/papers/2505.08245"},{"title":"[2505.08245] Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"https://arxiv.org/abs/2505.08245"}]

Based on the search results, here's what I found about measurement theory, psychometrics, LLM evaluation, and calibration in 2025:

## Emerging Field of LLM Psychometrics

LLM Psychometrics is an emerging interdisciplinary field that leverages psychometric instruments, theories, and principles to evaluate, understand, and enhance LLMs. This addresses novel challenges such as measuring human-like psychological constructs, moving beyond static and task-specific benchmarks, and establishing human-centered evaluation through psychometrics—the science of quantifying the intangible aspects of human psychology.

## Calibration and Validation

Recent IRT-based LLM benchmarks perform explicit psychometric validation to ensure calibration quality, with approaches like ATLAS demonstrating the importance of rigorous model-fit diagnostics. Psychometric validation ensures reliability and fairness, where reliability measures the consistency of the model's outputs, while validity ensures the accuracy of the constructs being measured.

## Methodological Approaches

Test formats can range from tightly controlled structured items to open-ended conversations and full agentic simulations, with data sources from established inventories or synthetic prompts, and prompting strategies including perturbing questions and injecting performance-enhancing instructions.

## Key Challenges

LLM responses may be unstable under surface changes to prompt or context, and construct labels like "reasoning" must be underpinned by explicit psychological taxonomies to support validity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "915a2379-7a5a-414f-b032-fa88caab03ec",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "1287a7c7-4e89-4dba-91ec-643872fee39a",
  "sourceToolAssistantUUID": "915a2379-7a5a-414f-b032-fa88caab03ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-29T05:16:34.035Z_

Excellent. I've found a rich set of papers. Now let me fetch the arXiv pages for all the unique promising papers to get detailed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1287a7c7-4e89-4dba-91ec-643872fee39a",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3e16ade-5624-493e-ba21-6e951af4d063",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 19 · 2026-05-29T05:16:34.514Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Km8NLHN5KGsLKMPh7MfvJi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15055",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e16ade-5624-493e-ba21-6e951af4d063",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "729a90ab-bf1a-42ce-b729-d688059fa6ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 20 · 2026-05-29T05:16:35.439Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BttVNajGNiUhbArthhbDQV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.00521",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729a90ab-bf1a-42ce-b729-d688059fa6ad",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3048da0b-68bb-46ed-8e74-29d7e35e1108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 21 · 2026-05-29T05:16:35.933Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SB9kjjVtXKdrm15x9m5RX1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.04689",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3048da0b-68bb-46ed-8e74-29d7e35e1108",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de624e87-4d29-49b9-8f73-804e50c07ec5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 22 · 2026-05-29T05:16:36.406Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DydbeVm2AfKQ9yNsH5riWM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.00844",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de624e87-4d29-49b9-8f73-804e50c07ec5",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4a4d363-7be7-4312-840b-b79bf9ec25a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 23 · 2026-05-29T05:16:36.891Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LS4qnxfCmkd4GBBM7p9EQA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22888",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4a4d363-7be7-4312-840b-b79bf9ec25a8",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "184f3b30-7ac0-4db6-b923-4dfe329bbf35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 24 · 2026-05-29T05:16:37.877Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SmHTi19KXL7uB1R1NosVSN`</summary>

```json
{
  "url": "https://aclanthology.org/2025.acl-long.761/",
  "prompt": "Extract the full title, all authors, venue, and abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "184f3b30-7ac0-4db6-b923-4dfe329bbf35",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b43bef1-dba3-44ad-a923-9a9c0ff0c0bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 25 · 2026-05-29T05:16:38.321Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T81ejL6SGXTQqMeGHFRnFf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.07019",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b43bef1-dba3-44ad-a923-9a9c0ff0c0bf",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fae8e449-5fcd-4300-9e93-d7290703ac54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 26 · 2026-05-29T05:16:39.268Z_

<details><summary>↩ Tool result · `toolu_01Km8NLHN5KGsLKMPh7MfvJi`</summary>

```text
# Paper Details

**Full Title:**
"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"

**Authors:**
Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao

**Submission Date:**
May 21, 2025 (v1)

**Abstract:**
The research addresses inconsistencies in LLM benchmark evaluations by proposing Pseudo-Siamese Network for Item Response Theory (PSN-IRT). This framework enhances traditional IRT approaches and enables "accurate and reliable estimations of item characteristics and model abilities." The team analyzed 11 benchmarks containing 41,871 test items, uncovering "significant and varied shortcomings in their measurement quality." The findings demonstrate that using PSN-IRT can produce smaller, more effective benchmarks that better correlate with human preferences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "729a90ab-bf1a-42ce-b729-d688059fa6ad",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "87e969b7-36cc-4904-a4eb-6c20c1c096d6",
  "sourceToolAssistantUUID": "729a90ab-bf1a-42ce-b729-d688059fa6ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-29T05:16:38.911Z_

<details><summary>↩ Tool result · `toolu_01BttVNajGNiUhbArthhbDQV`</summary>

```text
# Paper Details

**Full Title:** "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory"

**Authors:** Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim

**Submission Date:** January 31, 2026

**Complete Abstract:**

The researchers introduce a diagnostic framework for evaluating LLM judges' dependability, grounded in Item Response Theory. Their approach employs the Graded Response Model and examines reliability across two dimensions: "(1) intrinsic consistency, defined as the stability of measurement behavior under prompt variations, and (2) human alignment, capturing correspondence with human quality assessments." The empirical analysis of multiple LLM judges demonstrates that applying IRT-GRM produces interpretable diagnostic information. The findings offer practical guidance for verifying LLM judge reliability and pinpointing sources of measurement instability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3048da0b-68bb-46ed-8e74-29d7e35e1108",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "901d9e5b-e85d-4027-b2df-09ef595b19f6",
  "sourceToolAssistantUUID": "3048da0b-68bb-46ed-8e74-29d7e35e1108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-29T05:16:39.301Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019JpLxsH35Spozy776dpNHr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00238",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901d9e5b-e85d-4027-b2df-09ef595b19f6",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa16624e-3933-40fc-8740-17e5d79fdb74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 29 · 2026-05-29T05:16:39.760Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WrpxqH39vdLky5MRqpy6dh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.08245",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa16624e-3933-40fc-8740-17e5d79fdb74",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef323cb0-8144-4bd7-b3aa-a441f9c835c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 30 · 2026-05-29T05:16:40.422Z_

<details><summary>↩ Tool result · `toolu_01SB9kjjVtXKdrm15x9m5RX1`</summary>

```text
# Paper Summary

**Full Title:** "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"

**Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, and Nitesh V. Chawla

**Submission Date:** October 26, 2025 (v1); February 2, 2026 (v2)

**Abstract:**

The researchers introduce ATLAS, a framework that applies psychometric principles to streamline LLM assessment. Rather than relying on thousands of benchmark items, their method uses "Fisher information-guided item selection" to identify the most informative test questions. Key findings include reducing required test items by up to 90% while preserving measurement reliability. On HellaSwag specifically, the approach matched full-bank estimates using only 41 items. The authors demonstrate that ability estimates derived from their method align with standard accuracy metrics across benchmarks, yet provide finer-grained differentiation among models—roughly 23-31% of the 3,000+ tested models shifted significantly in ranking despite having identical accuracy scores.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de624e87-4d29-49b9-8f73-804e50c07ec5",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "9b5dbf9a-bd89-4e14-8a96-52aa4f4efb2c",
  "sourceToolAssistantUUID": "de624e87-4d29-49b9-8f73-804e50c07ec5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T05:16:40.302Z_

<details><summary>↩ Tool result · `toolu_01DydbeVm2AfKQ9yNsH5riWM`</summary>

```text
# Paper Information

**Title:** "Learning Compact Representations of LLM Abilities via Item Response Theory"

**Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu

**Submission Date:** October 1, 2025

**Abstract:** The paper addresses efficient management of numerous large language models by developing compact ability representations to support downstream applications like model routing and performance forecasting. The researchers propose an approach grounded in psychometric item response theory that estimates answer correctness likelihood based on three components: a model's skill vector, a query's discrimination vector, and query difficulty. They employ a Mixture-of-Experts network linking model and query embeddings to jointly learn these parameters. Experimental results demonstrate the method achieves leading performance in model routing and benchmark prediction tasks, with learned parameters providing interpretable insights into model capabilities and query properties.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4a4d363-7be7-4312-840b-b79bf9ec25a8",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "86bb61ad-2a86-48f3-a37f-332d06f4c9d6",
  "sourceToolAssistantUUID": "b4a4d363-7be7-4312-840b-b79bf9ec25a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-29T05:16:40.718Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017ED8m6CcnTgEptNoxqhpB4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.13885",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86bb61ad-2a86-48f3-a37f-332d06f4c9d6",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3a47e53-d0b9-4d0b-963c-3f7bd5d99639",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 33 · 2026-05-29T05:16:41.176Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CTfTSk6oGBg5DTJ4usP6v6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11674",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3a47e53-d0b9-4d0b-963c-3f7bd5d99639",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3af5611-c018-4241-9fa6-9111b2218afa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4101,
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

_source line 34 · 2026-05-29T05:16:41.463Z_

<details><summary>↩ Tool result · `toolu_01LS4qnxfCmkd4GBBM7p9EQA`</summary>

```text
# Paper Details

**Full Title:** JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory

**Authors:** Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang

**Submission Date:** September 26, 2025

**Abstract:** 

The paper introduces a framework that moves beyond traditional LLM evaluation by using geometric embeddings. Rather than compressing model capabilities into single scores, the approach places both language models and test questions in a shared geometric space. In this space, question embeddings encode semantic meaning through direction and difficulty through magnitude, while model performance depends on the geometric relationship between model and question vectors. The framework reveals how out-of-distribution performance connects to directional alignment, demonstrates that larger magnitudes indicate more challenging questions, and enables efficient addition of new models through single embedding fitting. The learned space further uncovers an internal LLM taxonomy that partially diverges from conventional subject classifications, providing what the authors describe as "a unified and interpretable geometric lens" for understanding model evaluation and generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "184f3b30-7ac0-4db6-b923-4dfe329bbf35",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "22338006-aa88-4d20-b2a5-c0c14d417074",
  "sourceToolAssistantUUID": "184f3b30-7ac0-4db6-b923-4dfe329bbf35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-29T05:16:41.401Z_

<details><summary>↩ Tool result · `toolu_01SmHTi19KXL7uB1R1NosVSN`</summary>

```text
# Paper Information

**Title:** "IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory"

**Authors:** Wei Song, Zhenya Huang, Cheng Cheng, Weibo Gao, Bihan Xu, GuanHao Zhao, Fei Wang, and Runze Wu

**Venue:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), July 2025, Vienna, Austria

**Abstract:** The research addresses the challenge of selecting the most appropriate language model for specific user queries while balancing performance gains against computational costs. The team developed IRT-Router, "a multi-LLM routing framework that efficiently routes user queries to the most suitable LLM." Drawing from Item Response Theory—a psychological measurement approach—the system models relationships between model capabilities and query characteristics. Testing across 20 language models and 12 datasets demonstrated superior effectiveness compared to baseline methods, with particularly strong results in cold-start scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b43bef1-dba3-44ad-a923-9a9c0ff0c0bf",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "c1dd6b63-fead-41f2-bfa9-b4ee3fe7e096",
  "sourceToolAssistantUUID": "6b43bef1-dba3-44ad-a923-9a9c0ff0c0bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-29T05:16:41.584Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GfFUZCJEMbu41KLmoEDkA8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.23506",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1dd6b63-fead-41f2-bfa9-b4ee3fe7e096",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHuZSYUxgEWfHXUWZP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df11eeb2-2fa9-46ec-b2cc-20ac75006228",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C42QzcrgL274LrUCH1BgjY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 10185,
      "output_tokens": 1037,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1037,
          "cache_read_input_tokens": 10185,
          "cache_creation_input_tokens": 4101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4101,
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

_source line 37 · 2026-05-29T05:16:42.621Z_

<details><summary>↩ Tool result · `toolu_01T81ejL6SGXTQqMeGHFRnFf`</summary>

```text
# Paper Details

**Full Title:** "Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length"

**Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu

**Submission Date:** December 7, 2025 (v1); Last revised December 11, 2025 (v2)

**Abstract:**

The paper introduces a new statistical framework called Latency-Response Theory (LaRT) for assessing LLMs. The researchers explain that their approach extends beyond traditional Item Response Theory by "jointly model[ing] the response accuracy and CoT length by introducing the latent ability, latent speed, and a key correlation parameter between them."

Key findings include that LaRT provides more accurate estimates of model abilities compared to existing methods. The empirical analysis across benchmark datasets revealed "a strong negative correlation between the latent ability and latent speed in all benchmarks," suggesting that more capable models tend to generate lengthier reasoning chains. The framework demonstrates improvements in "predictive power, item efficiency, ranking validity, and LLM evaluation efficiency" compared to conventional evaluation approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fae8e449-5fcd-4300-9e93-d7290703ac54",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "c82613bb-23d5-4594-9f95-399d16bb340b",
  "sourceToolAssistantUUID": "fae8e449-5fcd-4300-9e93-d7290703ac54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-29T05:16:43.504Z_

<details><summary>↩ Tool result · `toolu_019JpLxsH35Spozy776dpNHr`</summary>

```text
# Paper Information

**Full Title:** "Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory"

**Authors:** Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, Ulf Kroehne

**Submission Date:** April 30, 2026 (v1); Last revised May 13, 2026 (v2)

**Abstract:** The researchers propose an evaluation framework for LLM-based automated short answer grading using item response theory, which "models grading correctness as a function of latent grader ability and response grading difficulty." Their analysis of 17 open-weight LLMs reveals that models with comparable overall performance show substantial differences in accuracy decline as responses become more difficult. Key findings indicate that errors concentrate on partially correct incomplete labels, and difficult responses correlate with "weaker semantic alignment to the reference answer, stronger contradiction signals, and greater semantic isolation." The framework offers insights beyond traditional aggregate metrics like macro-F1 and Cohen's kappa, accepted at BEA 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa16624e-3933-40fc-8740-17e5d79fdb74",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "98b88e12-2bd0-4855-b3fe-fb99191107f2",
  "sourceToolAssistantUUID": "fa16624e-3933-40fc-8740-17e5d79fdb74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-29T05:16:43.857Z_

<details><summary>↩ Tool result · `toolu_01WrpxqH39vdLky5MRqpy6dh`</summary>

```text
# Paper Details

**Full Title:** "Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement"

**Authors:**
- Haoran Ye
- Jing Jin
- Yuhang Xie
- Xin Zhang
- Guojie Song

**Submission Date:** May 13, 2025 (v1); most recent revision March 11, 2026 (v3)

**Abstract:**

The authors explore how LLM evaluation has become increasingly complex, requiring methods beyond traditional benchmarks. They introduce the emerging field of LLM Psychometrics, which applies psychological measurement principles to assess AI systems. The review synthesizes literature on using "psychometric instruments, theories, and principles to evaluate, understand, and enhance LLMs." Key contributions include establishing benchmarking frameworks, expanding evaluation methodologies, validating findings, and improving LLM capabilities. The work integrates perspectives across disciplines to provide guidance for developing human-centered evaluation approaches that support advanced AI systems. A curated resource repository is available on GitHub for researchers in this interdisciplinary domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef323cb0-8144-4bd7-b3aa-a441f9c835c1",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "cf251f96-07e5-42e8-bde1-5ae1c538d51a",
  "sourceToolAssistantUUID": "ef323cb0-8144-4bd7-b3aa-a441f9c835c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-29T05:16:44.564Z_

<details><summary>↩ Tool result · `toolu_017ED8m6CcnTgEptNoxqhpB4`</summary>

```text
# Paper Information

**Full Title:**
"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores"

**Authors:**
- Esma Balkır
- Alice Pernthaller
- Marco Basaldella
- José Hernández-Orallo
- Nigel Collier

**Submission Date:**
January 20, 2026

**Complete Abstract:**
The researchers extend Computerized Adaptive Testing (CAT) methodology to handle continuous scoring metrics rather than binary correct/incorrect classifications. Their approach replaces the traditional Bernoulli distribution with a heteroskedastic normal distribution, enabling application to generation tasks evaluated with metrics like ROUGE, BLEU, and LLM-as-a-Judge. The method incorporates uncertainty-aware ranking with adaptive stopping rules to identify reliable model rankings while "testing as few items and as cheaply as possible." Validation across five benchmarks demonstrates the approach uses minimal items while achieving improved ranking correlation and maintaining high accuracy on confident predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3a47e53-d0b9-4d0b-963c-3f7bd5d99639",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "c9d9d859-91b5-4629-a2ad-c762603c33b2",
  "sourceToolAssistantUUID": "c3a47e53-d0b9-4d0b-963c-3f7bd5d99639",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-29T05:16:45.221Z_

<details><summary>↩ Tool result · `toolu_01CTfTSk6oGBg5DTJ4usP6v6`</summary>

```text
# Paper Information

**Full Title:** "Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs"

**Authors:** Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao

**Submission Date:** February 12, 2026

**Abstract:**

The paper addresses concerns about the reliability of LLM evaluation benchmarks, which face issues like "score inflation and selective reporting." The authors propose the Benchmark Health Index (BHI), a data-driven auditing framework that evaluates benchmarks across three dimensions:

1. **Capability Discrimination** – assessing how effectively benchmarks differentiate model performance
2. **Anti-Saturation** – evaluating remaining capacity before performance ceilings limit usefulness
3. **Impact** – measuring influence through adoption and influence on research and industry practices

The research synthesizes 106 validated benchmarks from 91 representative models (2025) to characterize the evaluation landscape. The framework enables principled benchmark selection and supports lifecycle management for future evaluation protocols.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3af5611-c018-4241-9fa6-9111b2218afa",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "5946828f-2541-47c3-92e6-d84e55a0fb7a",
  "sourceToolAssistantUUID": "b3af5611-c018-4241-9fa6-9111b2218afa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-29T05:16:46.739Z_

<details><summary>↩ Tool result · `toolu_01GfFUZCJEMbu41KLmoEDkA8`</summary>

```text
# Paper Information

**Full Title:** "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking"

**Authors:** Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng

**Submission Date:** February 28, 2026

**Complete Abstract:**

The researchers propose a computerized adaptive testing framework based on item response theory to efficiently evaluate medical knowledge in LLMs. Their study involved two phases: Monte Carlo simulations to optimize CAT settings, and empirical testing of 38 models using a calibrated medical item bank. 

The adaptive approach achieved "near-perfect correlation with full-bank estimates (r = 0.988) while using only 1.3 percent of the items." Notably, the method reduced evaluation time from hours to minutes per model while maintaining inter-model performance rankings. The authors characterize this as "a psychometric framework for rapid, low-cost benchmarking" of foundational medical knowledge, emphasizing it serves as a screening tool rather than a replacement for clinical validation studies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df11eeb2-2fa9-46ec-b2cc-20ac75006228",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "b01e054c-88e2-4fe2-94af-59f9915b1206",
  "sourceToolAssistantUUID": "df11eeb2-2fa9-46ec-b2cc-20ac75006228",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-29T05:16:49.369Z_

Good. Now let me fetch a few more papers that appeared in the results and do some additional searches to make sure I have comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b01e054c-88e2-4fe2-94af-59f9915b1206",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHvk1KifBpnaHyT43NG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f10d7d72-3277-4a9d-8ea5-c89163e93c3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwqvG9rzQawqVHVeJMieqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11197,
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

_source line 44 · 2026-05-29T05:16:51.252Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014BWaj1CciQ6V59i7WBJVaS`</summary>

```json
{
  "url": "https://openreview.net/forum?id=ZyVQqK7mcP",
  "prompt": "Extract the full title, all authors, venue, and abstract of this paper about lifting the benchmark iceberg with item-response theory."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f10d7d72-3277-4a9d-8ea5-c89163e93c3d",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHvk1KifBpnaHyT43NG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca0e0c31-2f38-4acf-ab66-82607e8ff428",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwqvG9rzQawqVHVeJMieqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11197,
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

_source line 45 · 2026-05-29T05:16:52.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018tye2ix9yw6yWa5upwqGj2`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2306.10512",
  "prompt": "Extract the full title, all authors, submission date, venue, and abstract of this paper about efficiently measuring cognitive ability of LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca0e0c31-2f38-4acf-ab66-82607e8ff428",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHvk1KifBpnaHyT43NG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c89da953-0013-4259-86f8-8a46f84c67d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwqvG9rzQawqVHVeJMieqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11197,
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

_source line 46 · 2026-05-29T05:16:53.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QcZsLVTkvowFDMnkJp8u1B`</summary>

```json
{
  "query": "IRT item response theory benchmark contamination LLM data leakage detection 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c89da953-0013-4259-86f8-8a46f84c67d0",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHvk1KifBpnaHyT43NG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc13828d-11e6-43e0-aa14-88065c749c39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwqvG9rzQawqVHVeJMieqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11197,
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

_source line 47 · 2026-05-29T05:16:53.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXvGmwNB9kdp3W8QxT2k85`</summary>

```json
{
  "query": "\"item response theory\" robustness adversarial evaluation language models 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc13828d-11e6-43e0-aa14-88065c749c39",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHvk1KifBpnaHyT43NG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20f2c49e-653d-4ab1-82a7-e6e2196649d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwqvG9rzQawqVHVeJMieqM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11197,
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

_source line 48 · 2026-05-29T05:16:53.684Z_

<details><summary>↩ Tool result · `toolu_014BWaj1CciQ6V59i7WBJVaS`</summary>

```text
# Paper Information

**Title:** "Lifting the benchmark iceberg with item-response theory"

**Authors:** Mara Schilling-Wilhelmi, Nawaf Alampara, Kevin Maik Jablonka

**Venue:** ICLR 2025 Workshop AI4MAT

**Abstract:** The authors investigate how hidden implementation choices in LLM benchmarks distort model rankings, introducing what they call a "benchmark iceberg" phenomenon. Rather than reflecting genuine capability differences, much variability in rankings stems from these obscured choices. Their proposal adapts item response theory—established psychometric principles from educational assessment—to make benchmarks more transparent and reliable evaluation instruments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca0e0c31-2f38-4acf-ab66-82607e8ff428",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "aa10b2d0-29d0-4478-9cfe-d484460fbc43",
  "sourceToolAssistantUUID": "ca0e0c31-2f38-4acf-ab66-82607e8ff428",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-29T05:16:54.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S3yyTDs5tn4ZGiwYzwJDtU`</summary>

```json
{
  "query": "multidimensional IRT MIRT large language model evaluation benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa10b2d0-29d0-4478-9cfe-d484460fbc43",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHvk1KifBpnaHyT43NG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "228382cf-ee98-4375-ae40-7b757947d576",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwqvG9rzQawqVHVeJMieqM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 7413,
      "output_tokens": 406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 406,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 11197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11197,
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

_source line 50 · 2026-05-29T05:16:57.564Z_

<details><summary>↩ Tool result · `toolu_018tye2ix9yw6yWa5upwqGj2`</summary>

```text
# Paper Information

**Full Title:** "Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective"

**Authors:** Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Rui Lv, Zhenya Huang, Guanhao Zhao, Zheng Zhang, Qingyang Mao, Shijin Wang, Enhong Chen

**Submission Date:** Not explicitly stated in the document (arxiv ID: 2306.10512 suggests June 2023)

**Venue:** arXiv (preprint server)

**Abstract:** The paper proposes applying Computerized Adaptive Testing (CAT) to evaluate large language models more efficiently. Rather than administering fixed test sets, this framework dynamically adjusts question difficulty based on model performance, enabling accurate ability estimation using fewer questions. The authors benchmark six instruction-tuned LLMs across three domains—subject knowledge, mathematical reasoning, and programming—finding that ChatGPT exhibits "careless student" behavior with tendency to slip and guess, while GPT-4 demonstrates significantly superior cognitive abilities reaching middle-level student performance in mathematical reasoning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c89da953-0013-4259-86f8-8a46f84c67d0",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "309fe1f9-17b5-457e-90b0-36712f7ec672",
  "sourceToolAssistantUUID": "c89da953-0013-4259-86f8-8a46f84c67d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-29T05:17:00.702Z_

<details><summary>↩ Tool result · `toolu_01QcZsLVTkvowFDMnkJp8u1B`</summary>

```text
Web search results for query: "IRT item response theory benchmark contamination LLM data leakage detection 2024 2025"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"LLM Benchmark Datasets Should Be Contamination-Resistant","url":"https://arxiv.org/html/2605.19999v1"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v1"},{"title":"When Benchmarks Lie: Why Contamination Breaks LLM Evaluation | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/when-benchmarks-lie-why-contamination-breaks-llm-evaluation-1fa335706f32"},{"title":"Benchmark Leakage Trap: Can We Trust LLM-based Recommendation?","url":"https://arxiv.org/pdf/2602.13626"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/pdf/2408.14352"}]

I found several relevant research papers and resources about benchmark contamination and data leakage detection in LLMs. Here's what the search results show:

## Key Research Findings

**Benchmark Contamination as a Critical Issue:**
Benchmark contamination is a significant obstacle to fair LLM evaluation and can quickly render benchmarks obsolete. Recent studies have detected widespread contamination across popular LLMs, with levels reaching up to 45% on commonly used benchmarks.

**Detection Methods (2024-2025):**
Several researchers have proposed methods to detect and mitigate data contamination, including a retrieval-based approach to assess the degree of overlap between pre-training text and benchmark data. Dong et al. (2024b) proposed the CDD method to identify peaks in the output distribution to detect data contamination.

**Item Response Theory Applications:**
Selecting items with PSN-IRT leads to model rankings that better align with human preference, and recent studies have introduced quantitative metrics to assess benchmark behavior post-deployment.

**Mitigation Strategies:**
A new study by Sun et al. (2025) provides a rigorous assessment of how current mitigation strategies perform, evaluating each strategy on five benchmarks including ARC-Challenge, GSM8K, TruthfulQA, MMLU, and RepliQA.

The search results include recent arxiv papers from 2024-2025 that directly address these interconnected topics of IRT, benchmark contamination, and data leakage detection methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc13828d-11e6-43e0-aa14-88065c749c39",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "690079e8-1096-4a35-9193-e2638675093b",
  "sourceToolAssistantUUID": "fc13828d-11e6-43e0-aa14-88065c749c39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-29T05:17:01.267Z_

<details><summary>↩ Tool result · `toolu_01WXvGmwNB9kdp3W8QxT2k85`</summary>

```text
Web search results for query: ""item response theory" robustness adversarial evaluation language models 2024 2025"

Links: [{"title":"RIDE: Difficulty Evolving Perturbation with Item Response ...","url":"https://arxiv.org/pdf/2511.04120"},{"title":"NanoFlux: Adversarial Dual‑LLM Evaluation and Distillation for Multi‑Domain Reasoning","url":"https://arxiv.org/html/2509.23252v2"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Large Language Model Evaluation in 2025: Smarter Metrics That ...","url":"https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"},{"title":"Adversarial Defense without Adversarial Defense: Enhancing Language Model Robustness via Instance-level Principal Component Removal - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12617998/"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Chain-of-Thought Driven Adversarial Scenario Extrapolation for Robust Language Models","url":"https://arxiv.org/pdf/2505.17089"}]

I found several relevant research papers on this topic. Here are the key findings:

## Item Response Theory Applied to Adversarial Evaluation

Item Response Theory (IRT) is widely applied in AI for automated item difficulty estimation and efficient evaluation. Recent research has extended this framework to adversarial evaluation of language models.

A 2025 framework evaluates adversarial question quality with Item Response Theory (IRT), showing that "good" adversarial questions stump models but not humans, with high discriminative power.

## Recent Developments (2024-2025)

Existing LLM robustness evaluations often use controlled perturbations to test whether models truly understand tasks rather than memorize surface patterns, revealing substantial degradation in many LLMs. Unlike rule-based methods, reinforcement learning-based rewriting approaches are used to generate perturbations, producing better-formed data and avoiding unsolvable or multiple-solution problems.

Item Response Theory has recently been applied to LLM evaluation, providing item parameters such as difficulty, discrimination, and guessing, as well as latent ability estimates for models.

## Emerging Frameworks

As of June 2025, the ecosystem has matured significantly, with dozens of metrics targeting diverse dimensions such as factual grounding, explainability, robustness, and ethical compliance. Emerging trends—including green metrics, adversarial robustness, and continuous evaluation pipelines—are shaping the next phase of trustworthy LLM development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20f2c49e-653d-4ab1-82a7-e6e2196649d6",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "36bc5a92-9932-4dad-a5da-62d67510e294",
  "sourceToolAssistantUUID": "20f2c49e-653d-4ab1-82a7-e6e2196649d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-29T05:17:02.386Z_

<details><summary>↩ Tool result · `toolu_01S3yyTDs5tn4ZGiwYzwJDtU`</summary>

```text
Web search results for query: "multidimensional IRT MIRT large language model evaluation benchmark 2024 2025"

Links: [{"title":"Latency-Response Theory Model: Evaluating Large Language","url":"https://www.arxiv.org/pdf/2512.07019"},{"title":"Toward a unified framework for data-efficient evaluation of large language models","url":"https://arxiv.org/html/2510.04051"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Large Language Model Evaluation in 2025: Smarter Metrics That ...","url":"https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"},{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory","url":"https://arxiv.org/pdf/2603.02663"},{"title":"(PDF) Large Language Model Evaluation in 2025: Smarter Metrics That Separate Hype from Trust","url":"https://www.researchgate.net/publication/392654652_Large_Language_Model_Evaluation_in_2025_Smarter_Metrics_That_Separate_Hype_from_Trust"}]

Based on the search results, here are the key findings about multidimensional IRT (MIRT) and large language model evaluation benchmarks from 2024-2025:

## Recent Developments in IRT-Based LLM Evaluation

Recent developments (Polo et al., 2024; Truong et al., 2025; Zhou et al., 2025) utilize ideas from item response theory (IRT) to produce robust performance estimations that are stable across subsets. IRT approaches disentangle the influences of model capability and evaluation item difficulty, thereby producing invariant estimates of model capabilities.

## Multidimensional IRT Applications

Maia Polo et al. (2024) applies Multidimensional Item Response Theory models to predict the responses of future question items. Through a novel factorized design, LEGO-IRT incorporates structural knowledge by jointly modeling multiple metrics and benchmarks.

## Benefits and Challenges

IRT explicitly models variation in item difficulty and discrimination and therefore provides a latent ability estimate that is comparable across models and datasets. However, the application of IRT on LLM benchmarks is still underexplored due to the complexity and scale of modern datasets and its assumption of normally distributed abilities.

## Practical Impact

Polo et al. (2024) used IRT methods to reduce the evaluation effort over MMLU by 99% while leaving the evaluation quality almost intact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "228382cf-ee98-4375-ae40-7b757947d576",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "dae803ef-81ea-423e-9ac8-501b81852693",
  "sourceToolAssistantUUID": "228382cf-ee98-4375-ae40-7b757947d576",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-29T05:17:04.737Z_

Let me fetch the remaining papers I found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dae803ef-81ea-423e-9ac8-501b81852693",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHwtyrLuMcefNu5JCDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23380a0a-1f7c-4be1-a095-1fc2b013d8b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1j1ChZ4AgpVCuc45kmwhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 18610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3204,
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

_source line 55 · 2026-05-29T05:17:05.678Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FUPrnDaMsrAk18VNyFf4fZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.04120",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper about RIDE difficulty evolving perturbation with IRT."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23380a0a-1f7c-4be1-a095-1fc2b013d8b6",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHwtyrLuMcefNu5JCDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff6c1ed8-64d5-4f71-a696-7123e9cea3fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1j1ChZ4AgpVCuc45kmwhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 18610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3204,
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

_source line 56 · 2026-05-29T05:17:06.620Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BS5LxXXVynX5kxwFKaiYDq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.04051",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper about unified framework for data-efficient evaluation of LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff6c1ed8-64d5-4f71-a696-7123e9cea3fa",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHwtyrLuMcefNu5JCDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df6ac54d-49ec-44b9-8770-b678afb0606e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1j1ChZ4AgpVCuc45kmwhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 18610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3204,
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

_source line 57 · 2026-05-29T05:17:09.712Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017k7ro5PG6QP8gix58Sk4a8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.02663",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper about multimodal item response theory."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df6ac54d-49ec-44b9-8770-b678afb0606e",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHwtyrLuMcefNu5JCDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd44a0ff-6bf2-4894-8063-1ff5a675624e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1j1ChZ4AgpVCuc45kmwhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 18610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3204,
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

_source line 58 · 2026-05-29T05:17:09.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015iGu5F3M4Hrujt6WPyaN2B`</summary>

```json
{
  "query": "LEGO-IRT multidimensional item response theory LLM benchmark Polo 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd44a0ff-6bf2-4894-8063-1ff5a675624e",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHwtyrLuMcefNu5JCDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63a98ce4-2e4b-4ee6-b8a8-4977ee8dc7d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1j1ChZ4AgpVCuc45kmwhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 18610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3204,
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

_source line 59 · 2026-05-29T05:17:09.801Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D5opBJ3a7zhsjrXXAw732T`</summary>

```json
{
  "query": "IRT item parameters difficulty discrimination guessing LLM evaluation efficient benchmark 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63a98ce4-2e4b-4ee6-b8a8-4977ee8dc7d6",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHwtyrLuMcefNu5JCDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43830e54-7c9b-4128-81aa-eaf1b6326bad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1j1ChZ4AgpVCuc45kmwhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 18610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3204,
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

_source line 60 · 2026-05-29T05:17:10.404Z_

<details><summary>↩ Tool result · `toolu_01FUPrnDaMsrAk18VNyFf4fZ`</summary>

```text
# RIDE Paper Details

**Full Title:** "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning"

**Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan

**Submission Date:** November 6, 2025 (v1); Last revised January 31, 2026 (v2)

**Abstract:**

The research addresses concerns that large language models may achieve inflated mathematical reasoning results through training data leakage or pattern matching rather than genuine understanding. The authors propose RIDE, a framework combining adversarial question rewriting with Item Response Theory to systematically measure question difficulty and generate more challenging mathematical problems.

The methodology involves using 35 language models as simulated test-takers to build a difficulty ranker from their responses. This ranker provides reward signals for reinforcement learning that guides a question-rewriting model to create reformulated versions across difficulty levels. When applied to competition-level mathematics benchmarks, the resulting perturbed questions caused "an average 21.73% drop across 26 models," revealing limitations in mathematical reasoning robustness and validating their evaluation approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff6c1ed8-64d5-4f71-a696-7123e9cea3fa",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "2496012d-8acd-42b6-a21e-9ff74d3c52f8",
  "sourceToolAssistantUUID": "ff6c1ed8-64d5-4f71-a696-7123e9cea3fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-29T05:17:10.811Z_

<details><summary>↩ Tool result · `toolu_01BS5LxXXVynX5kxwFKaiYDq`</summary>

```text
# Paper Summary

**Full Title:** "Toward a unified framework for data-efficient evaluation of large language models"

**Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang

**Submission Date:** October 5, 2025

**Abstract Summary:**

The research addresses computational costs in LLM evaluation through a novel approach called LEGO-IRT. The framework leverages Item Response Theory to distinguish model capabilities from task difficulty while handling both discrete and continuous scoring metrics—a significant improvement over existing methods. 

Key capabilities include: supporting diverse evaluation metrics natively, decomposing ability estimates into general and context-specific components, and incorporating structural relationships across multiple benchmarks. Testing involved 70 language models evaluated on 5 benchmarks. Results demonstrate that "stable capability estimates using just 3% of the total evaluation items" are achievable, with structural knowledge reducing error margins substantially. The authors further suggest their latent ability measurements may "align more closely with human preferences" than conventional metrics.

**Code Availability:** The authors have made implementation code publicly available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6ac54d-49ec-44b9-8770-b678afb0606e",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "a0f2eac7-430e-4263-9a93-b871ee9efc04",
  "sourceToolAssistantUUID": "df6ac54d-49ec-44b9-8770-b678afb0606e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-29T05:17:14.623Z_

<details><summary>↩ Tool result · `toolu_017k7ro5PG6QP8gix58Sk4a8`</summary>

```text
# Paper Summary

**Full Title:** "Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory"

**Authors:** Shunki Uebayashi, Kento Masui, Kyohei Atarashi, Han Bao, Hisashi Kashima, Naoto Inoue, Mayu Otani, Koh Takeuchi

**Submission Date:** March 3, 2026

**Abstract:**

The researchers address a critical issue with current multimodal benchmarks: they contain "shortcut questions, which can be solved using only a single modality." They propose M3IRT, a framework extending classical Item Response Theory to decompose model capability and question difficulty into three components: image-only, text-only, and cross-modal elements.

Their approach evaluates vision-language models across 24 systems on three benchmarks, demonstrating that M3IRT effectively identifies genuinely cross-modal questions while filtering low-quality items. Notably, the method "preserves ranking fidelity even when 50% of items are artificially generated low-quality questions," thereby enabling more efficient and reliable multimodal assessment tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd44a0ff-6bf2-4894-8063-1ff5a675624e",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "0c956e3c-e574-4240-8037-702dd1e4dddd",
  "sourceToolAssistantUUID": "dd44a0ff-6bf2-4894-8063-1ff5a675624e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-29T05:17:18.566Z_

<details><summary>↩ Tool result · `toolu_01D5opBJ3a7zhsjrXXAw732T`</summary>

```text
Web search results for query: "IRT item parameters difficulty discrimination guessing LLM evaluation efficient benchmark 2024 2025 arXiv"

Links: [{"title":"An Interpretable and Scalable Framework for Evaluating Large Language Models","url":"https://arxiv.org/html/2605.07046"},{"title":"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/html/2605.00238"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689v2"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations","url":"https://arxiv.org/html/2601.09953v2"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/html/2510.00844v1"},{"title":"Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length","url":"https://arxiv.org/html/2512.07019v2"},{"title":"Latency-Response Theory Model: Evaluating Large Language","url":"https://www.arxiv.org/pdf/2512.07019"}]

I found several highly relevant papers on arXiv from 2024-2025 that discuss IRT (Item Response Theory) parameters for evaluating Large Language Models. Here are the key findings:

## Recent IRT-Based LLM Evaluation Papers:

**1. An Interpretable and Scalable Framework for Evaluating Large Language Models**
This approach reformulates the problem as a sequence of constrained matrix factorization subproblems, enabling stable and efficient parameter estimation with theoretical guarantees for identifiability and convergence. It delivers orders-of-magnitude speedups over competing methods while maintaining comparable or even higher estimation accuracy.

**2. Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory**
This proposes the Pseudo-Siamese Network for IRT (PSN-IRT), designed to diagnose benchmark item quality by analyzing LLM responses, inferring model-ability and four properties for benchmark items: discriminability, difficulty, guessing-rate and feasibility.

**3. Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks**
IRT provides item parameters such as difficulty, discrimination, and guessing, as well as latent ability estimates for models.

**4. Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration**
Predictive approaches use IRT, amortized modeling, and multi-prompt estimators to infer full-benchmark performance from limited observations.

**5. Learning Compact Representations of LLM Abilities via Item Response Theory**
This work applies IRT to model LLM abilities and introduces an MoE-based method to explicitly learn query characteristics (discrimination and difficulty).

These papers collectively demonstrate the emerging use of psychometric IRT frameworks for efficient and interpretable LLM evaluation in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43830e54-7c9b-4128-81aa-eaf1b6326bad",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "c6c78612-039c-4b09-96a0-2d18704b1fbf",
  "sourceToolAssistantUUID": "43830e54-7c9b-4128-81aa-eaf1b6326bad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-29T05:17:24.160Z_

<details><summary>↩ Tool result · `toolu_015iGu5F3M4Hrujt6WPyaN2B`</summary>

```text
Web search results for query: "LEGO-IRT multidimensional item response theory LLM benchmark Polo 2024"

Links: [{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/5cc488ae1b2fca02ccf35d8a46821e982bd149f1.pdf"},{"title":"Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length","url":"https://arxiv.org/html/2512.07019v1"},{"title":"[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/html/2510.00844v1"},{"title":"Latency-Response Theory Model: Evaluating Large Language","url":"https://www.arxiv.org/pdf/2512.07019"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"[2510.04051] Toward a unified framework for data-efficient evaluation of large language models","url":"https://arxiv.org/abs/2510.04051"},{"title":"Toward a unified framework for data-efficient evaluation of large language models","url":"https://arxiv.org/html/2510.04051"},{"title":"METABENCH A SPARSE BENCHMARK OF REASONING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"}]

Based on the search results, here's what I found about LEGO-IRT and the 2024 Polo work:

## LEGO-IRT Framework

LEGO-IRT is a unified and flexible framework for data-efficient LLM evaluation. Through extensive experiments involving 70 LLMs across 5 benchmarks, LEGO-IRT achieves stable capability estimates using just 3% of the total evaluation items.

## Addressing IRT Limitations

While Item Response Theory (IRT) offers a promising path toward data-efficient evaluation by disentangling model capability from item difficulty, existing IRT-based methods are hampered by significant limitations, such as being restricted to binary correctness metrics and failing to handle continuous scores used in generative tasks.

## Polo et al. 2024

Recent developments including Polo et al. (2024) utilize ideas from item response theory (IRT) to produce robust performance estimations that are stable across subsets. Polo's work applies Multidimensional Item Response Theory models to predict the responses of future question items.

The search results indicate that Polo et al. 2024 was influential in applying IRT methods to LLM evaluation, and LEGO-IRT represents a more recent advancement that extends these ideas to handle more complex evaluation scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63a98ce4-2e4b-4ee6-b8a8-4977ee8dc7d6",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "8a1a1d20-d7ee-422a-922d-ef6f1761e329",
  "sourceToolAssistantUUID": "63a98ce4-2e4b-4ee6-b8a8-4977ee8dc7d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-29T05:17:26.981Z_

Let me fetch the remaining new papers I haven't seen yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a1a1d20-d7ee-422a-922d-ef6f1761e329",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHyW3GZsKwM7iS9wDzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a0fd89b-3d17-418d-85e8-97c9ec8c33a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1RtRGMH8WNZAcHhNZ8AfB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 895,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 21814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 66 · 2026-05-29T05:17:27.928Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M9aqhn3RfMZNB4Rue1MSxS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.07046",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper about interpretable and scalable framework for evaluating LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a0fd89b-3d17-418d-85e8-97c9ec8c33a1",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHyW3GZsKwM7iS9wDzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4836a56f-0c97-4049-9a59-04686d1d4b3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1RtRGMH8WNZAcHhNZ8AfB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 895,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 21814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 67 · 2026-05-29T05:17:28.865Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016dT22G1A1ULQBodSBAoJ1C`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12843",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper about Growing Pains extensible LLM benchmarking via fixed parameter calibration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4836a56f-0c97-4049-9a59-04686d1d4b3c",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHyW3GZsKwM7iS9wDzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8de0308-ddb3-4129-aaa8-37ae7f31fa5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1RtRGMH8WNZAcHhNZ8AfB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 895,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 21814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 68 · 2026-05-29T05:17:29.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YC4cHsNuW8Y8oD6cSjBnhA`</summary>

```json
{
  "query": "tinyBenchmarks Polo IRT efficient LLM evaluation MMLU 2024 NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8de0308-ddb3-4129-aaa8-37ae7f31fa5d",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHyW3GZsKwM7iS9wDzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e2027e3-cacd-43d1-a928-c8a2433cc219",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1RtRGMH8WNZAcHhNZ8AfB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 895,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 21814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 69 · 2026-05-29T05:17:30.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011PbfyccGKnsy7g2srcRT5S`</summary>

```json
{
  "query": "MetaBench IRT sparse benchmark reasoning LLM ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e2027e3-cacd-43d1-a928-c8a2433cc219",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHyW3GZsKwM7iS9wDzz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fe05fff-b549-4a4d-bcdc-271488e90b6b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1RtRGMH8WNZAcHhNZ8AfB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 895,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 21814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 70 · 2026-05-29T05:17:31.094Z_

<details><summary>↩ Tool result · `toolu_01M9aqhn3RfMZNB4Rue1MSxS`</summary>

```text
# Paper Summary

**Full Title:** "An Interpretable and Scalable Framework for Evaluating Large Language Models"

**Authors:** Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu

**Submission Date:** May 7, 2026

**Abstract:** The authors address LLM evaluation challenges by proposing a framework based on Item Response Theory and the majorization-minimization principle. Their approach "reformulates the problem as a sequence of constrained matrix factorization subproblems, enabling stable and efficient parameter estimation" with theoretical guarantees. Testing on synthetic and real datasets, including MATH-500 and Open LLM Leaderboard benchmarks, demonstrates significant computational speedups while maintaining or improving accuracy. The method provides interpretable insights into item difficulty and discrimination patterns that can guide benchmark development.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4836a56f-0c97-4049-9a59-04686d1d4b3c",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "a6e3e9d5-646b-49c8-95ff-fb34978aefa4",
  "sourceToolAssistantUUID": "4836a56f-0c97-4049-9a59-04686d1d4b3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-29T05:17:36.600Z_

<details><summary>↩ Tool result · `toolu_016dT22G1A1ULQBodSBAoJ1C`</summary>

```text
# Paper Details

**Full Title:** "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"

**Authors:**
- Eliya Habba
- Itay Itzhak
- Asaf Yehudai
- Yotam Perlitz
- Elron Bandel
- Michal Shmueli-Scheuer
- Leshem Choshen
- Gabriel Stanovsky

**Submission Date:** April 14, 2026 (v1); revised April 15, 2026 (v2)

**Abstract:**

The research addresses the challenge of evaluating numerous language models against multiple datasets by proposing "a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks." The methodology maintains fixed parameters for previously evaluated items while introducing new datasets sequentially. This enables direct comparison of results across different evaluation periods despite models being assessed on varying sample sets.

Testing across over 400 models demonstrated the approach achieves "within 2-3 percentage points" accuracy in predicting complete evaluations using only 100 anchor questions per dataset. The ranking preservation capability reaches "Spearman ρ ≥ 0.9," confirming the framework sustains "score comparability, at a constant evaluation cost per new dataset."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8de0308-ddb3-4129-aaa8-37ae7f31fa5d",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "390a2225-efec-42cc-9713-954fae244155",
  "sourceToolAssistantUUID": "d8de0308-ddb3-4129-aaa8-37ae7f31fa5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-29T05:17:37.417Z_

<details><summary>↩ Tool result · `toolu_011PbfyccGKnsy7g2srcRT5S`</summary>

```text
Web search results for query: "MetaBench IRT sparse benchmark reasoning LLM ICLR 2025"

Links: [{"title":"metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ebc26584810a189ef1e4f173aba4319-Abstract-Conference.html"},{"title":"metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=4T33izzFpK"},{"title":"GitHub - adkipnis/metabench: A principled reduction of six benchmarks from the Open LLM Leaderboard to a single sparse benchmark. · GitHub","url":"https://github.com/adkipnis/metabench"},{"title":"metabench A Sparse Benchmark to Measure General Ability in Large Language Models","url":"https://arxiv.org/html/2407.12844v1"},{"title":"[Literature Review] metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://www.themoonlight.io/en/review/metabench-a-sparse-benchmark-of-reasoning-and-knowledge-in-large-language-models"},{"title":"metabench A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/html/2407.12844v2"},{"title":"METABENCH A SPARSE BENCHMARK OF REASONING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"[2407.12844] metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/abs/2407.12844"}]

Based on the search results, here's what I found about MetaBench at ICLR 2025:

## Overview

MetaBench is part of the International Conference on Representation Learning 2025 (ICLR 2025) Conference. It is the data-driven distilled version of six popular LLM benchmarks, drastically reducing their size with minimal information loss.

## Methodology

The researchers used data from more than 5000 LLMs to identify the most informative items of six benchmarks: ARC, GSM8K, HellaSwag, MMLU, TruthfulQA and WinoGrande (with 28,632 items in total).

The construction process involved fitting variants of IRT (Item Response Theory) models to the remaining items, inferring item information from the item parameters and selecting the most informative items to construct metabench.

## Results

The sparse benchmark, metabench, has less than 3% of the original size of all six benchmarks combined. More specifically, the distilled metabench benchmark comprises less than 3% of the original datasets (858 items from 28,632 combined items), yet is able to reconstruct original benchmark scores with high fidelity (1.24% RMSE for individual scores and 0.58% for total scores).

A single factor is sufficient to capture 79.3% of the total variability across latent abilities, with this meta-ability having a Pearson correlation of r = 0.938 with the original grand average score.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fe05fff-b549-4a4d-bcdc-271488e90b6b",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "7825d84a-12b5-4b4f-ba3d-be85a8ca88ed",
  "sourceToolAssistantUUID": "7fe05fff-b549-4a4d-bcdc-271488e90b6b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-29T05:17:38.765Z_

<details><summary>↩ Tool result · `toolu_01YC4cHsNuW8Y8oD6cSjBnhA`</summary>

```text
Web search results for query: "tinyBenchmarks Polo IRT efficient LLM evaluation MMLU 2024 NeurIPS"

Links: [{"title":"(PDF) tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples [Quick Review]","url":"https://liner.com/review/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/pdf/2402.14992"},{"title":"GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub","url":"https://github.com/felipemaiapolo/tinyBenchmarks"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"tinyBenchmarks/README.md at main · felipemaiapolo/tinyBenchmarks","url":"https://github.com/felipemaiapolo/tinyBenchmarks/blob/main/README.md"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://proceedings.mlr.press/v235/maia-polo24a.html"},{"title":"[PDF] tinyBenchmarks: evaluating LLMs with fewer examples | Semantic Scholar","url":"https://www.semanticscholar.org/paper/tinyBenchmarks:-evaluating-LLMs-with-fewer-examples-Polo-Weber/4c0f88e80320885e8289a9af781a1101717104f2"},{"title":"Efficient multi-prompt evaluation of LLMs","url":"https://arxiv.org/pdf/2405.17202"}]

Based on the search results, here's what I found about tinyBenchmarks:

## Overview

tinyBenchmarks proposes a novel evaluation framework using Item Response Theory (IRT) to efficiently estimate LLM performance on benchmarks with substantially fewer examples, demonstrating that 100 curated examples can suffice for MMLU.

## Key Features

The method introduces the generalized p-IRT (gp-IRT) estimator, which combines direct sampling-based estimation with IRT model predictions to enhance accuracy and robustness, particularly when probabilities are inaccurate. Strategies for selecting evaluation examples include stratified random sampling, correctness-based clustering, and a robust IRT-based clustering of example representations.

## Results and Efficiency Gains

The study demonstrates that evaluating LLMs on a small, curated subset of examples achieves an average estimation error of approximately 2% with as few as 100 examples per scenario, significantly reducing evaluation costs by a factor of 140 for MMLU (from 14K to 100 examples) and 160 for the Open LLM Leaderboard (from 29K to 180 examples across 6 scenarios).

## Published Work and Resources

The work was published in the Proceedings of the 41st International Conference on Machine Learning, PMLR 235:34303-34326, 2024. Note: The search results reference ICLR 2024 publication, not NeurIPS 2024. The researchers released "tinyBenchmarks," comprising pre-selected subsets of 100 examples per scenario for popular benchmarks, along with an IRT-based tool for efficient performance estimation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e2027e3-cacd-43d1-a928-c8a2433cc219",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "f93f0ee6-2702-4328-8178-19c593a2d409",
  "sourceToolAssistantUUID": "8e2027e3-cacd-43d1-a928-c8a2433cc219",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-29T05:17:41.508Z_

Let me fetch the last few papers and do one more targeted search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f93f0ee6-2702-4328-8178-19c593a2d409",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHzaUwhLt84ffmYRxEq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fd5dc4a-b4da-4cd6-bae0-9f2afe7026a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJTG8MppTq33pDg4eUqZhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 75 · 2026-05-29T05:17:42.472Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DqQcHt6fMgB5SxC8jQ3wWQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.14992",
  "prompt": "Extract the full title, all authors, submission date, venue, and complete abstract of this tinyBenchmarks paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fd5dc4a-b4da-4cd6-bae0-9f2afe7026a7",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHzaUwhLt84ffmYRxEq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7def34ac-9b9c-40a4-abac-62abca0e5e90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJTG8MppTq33pDg4eUqZhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 76 · 2026-05-29T05:17:43.009Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q6Rynd79N71rmmVEAK93xY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.12844",
  "prompt": "Extract the full title, all authors, submission date, venue, and complete abstract of this metabench paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7def34ac-9b9c-40a4-abac-62abca0e5e90",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHzaUwhLt84ffmYRxEq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09ac9d97-0c18-4211-9bc7-1acb1f48c6fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJTG8MppTq33pDg4eUqZhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 77 · 2026-05-29T05:17:44.805Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018PKtztgbetgXdga5RgXhuM`</summary>

```json
{
  "url": "https://openreview.net/forum?id=s6X3s3rBPW",
  "prompt": "Extract the full title, all authors, venue, and abstract of this paper about efficiently measuring cognitive ability of LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09ac9d97-0c18-4211-9bc7-1acb1f48c6fc",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHzaUwhLt84ffmYRxEq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23bac2a2-cb37-4a12-93dd-38e6be703c64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJTG8MppTq33pDg4eUqZhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 78 · 2026-05-29T05:17:45.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kpgiyan6oMwwKWYVEhoEiu`</summary>

```json
{
  "query": "\"Rasch model\" OR \"2PL\" OR \"3PL\" LLM evaluation benchmark ability estimation 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23bac2a2-cb37-4a12-93dd-38e6be703c64",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWHzaUwhLt84ffmYRxEq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "691e5c0d-fc93-4c7a-8042-ede268edf0ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJTG8MppTq33pDg4eUqZhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

### Tool result

_source line 79 · 2026-05-29T05:17:46.359Z_

<details><summary>↩ Tool result · `toolu_01DqQcHt6fMgB5SxC8jQ3wWQ`</summary>

```text
# tinyBenchmarks Paper Details

**Full Title:** "tinyBenchmarks: evaluating LLMs with fewer examples"

**Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin

**Submission Date:** February 22, 2024 (v1); revised May 26, 2024 (v2)

**Venue:** Proceedings of the 41st International Conference on Machine Learning (ICML)

**Abstract:** 

The researchers investigate methods to reduce evaluation costs for large language models by demonstrating that "to accurately estimate the performance of an LLM on MMLU, a popular multiple-choice QA benchmark consisting of 14K examples, it is sufficient to evaluate this LLM on 100 curated examples." They release evaluation tools and condensed versions of major benchmarks including Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Their work shows these "tiny benchmarks are sufficient to reliably and efficiently reproduce the original evaluation results."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7def34ac-9b9c-40a4-abac-62abca0e5e90",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "f7596022-1b83-43ba-9a59-8a8f6011da35",
  "sourceToolAssistantUUID": "7def34ac-9b9c-40a4-abac-62abca0e5e90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-29T05:17:47.079Z_

<details><summary>↩ Tool result · `toolu_01Q6Rynd79N71rmmVEAK93xY`</summary>

```text
# metabench Paper Information

**Full Title:** "metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models"

**Authors:** Alex Kipnis, Konstantinos Voudouris, Luca M. Schulze Buschoff, Eric Schulz

**Submission Date:** July 4, 2024 (v1); Last revised February 20, 2025 (v2)

**Venue:** ICLR 2025

**Abstract Summary:**

The researchers analyzed over 5,000 large language models to identify redundancies across six major benchmarks totaling 28,632 test items. They created "metabench," a compressed version containing less than 3% of the original combined size. This sparse benchmark effectively reconstructs individual benchmark scores with an average root mean square error of 1.24%, total scores with 0.58% error, and reveals "a single underlying common factor whose Spearman correlation with the total score is r = 0.94." The work demonstrates that substantial item overlap exists across these evaluation frameworks, suggesting they measure overlapping underlying capabilities rather than distinct abilities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09ac9d97-0c18-4211-9bc7-1acb1f48c6fc",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "d6aec9de-d652-42eb-a191-ae90fe24ada6",
  "sourceToolAssistantUUID": "09ac9d97-0c18-4211-9bc7-1acb1f48c6fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-29T05:17:49.324Z_

<details><summary>↩ Tool result · `toolu_018PKtztgbetgXdga5RgXhuM`</summary>

```text
# Paper Information

**Full Title:** "Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective"

**Authors:** Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Rui Lv, Zhenya Huang, GuanHao Zhao, Zheng Zhang, Qingyang Mao, Shijin Wang, and Enhong Chen

**Venue:** ICLR 2024 Conference

**Abstract Summary:**

The researchers present an adaptive testing framework inspired by psychometric methods to evaluate large language models more effectively. Rather than administering standardized tests, their approach dynamically adjusts question characteristics—particularly difficulty—based on model performance, enabling "more accurate estimation of the model's abilities, using fewer questions."

The study analyzes six commercial instruction-tuned LLMs across three domains: Subject Knowledge, Mathematical Reasoning, and Programming. Key findings indicate that ChatGPT exhibits careless behavior patterns, while "GPT4 can outperform other models significantly and reach the cognitive ability of middle-level students." The authors propose that adaptive testing will become standard practice in LLM evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23bac2a2-cb37-4a12-93dd-38e6be703c64",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "1716e557-0a42-4f55-b1be-e152dd55d5d2",
  "sourceToolAssistantUUID": "23bac2a2-cb37-4a12-93dd-38e6be703c64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-29T05:17:51.618Z_

<details><summary>↩ Tool result · `toolu_01Kpgiyan6oMwwKWYVEhoEiu`</summary>

```text
Web search results for query: ""Rasch model" OR "2PL" OR "3PL" LLM evaluation benchmark ability estimation 2024 2025 arXiv"

Links: [{"title":"Reliable and Efficient Amortized Model-based Evaluation","url":"https://arxiv.org/html/2503.13335"},{"title":"Reliable and Efficient Amortized Model-Based Evaluation","url":"https://crfm.stanford.edu/2025/06/04/reliable-and-efficient-evaluation.html"},{"title":"(PDF) Evaluation and Benchmarking of LLM Agents: A Survey","url":"https://www.researchgate.net/publication/394100858_Evaluation_and_Benchmarking_of_LLM_Agents_A_Survey"},{"title":"Assessing the Performance of Chatbots on the Taiwan Psychiatry Licensing Examination Using the Rasch Model","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11594248/"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"}]

Based on the search results, here are the key findings related to your query:

## Recent Research on IRT Models for LLM Evaluation

Recent work has compared the one-parameter logistic model (Rasch model), the two-parameter logistic (2PL) model, and the three-parameter logistic (3PL) model for evaluating large language models. The Rasch model captures how LLM ability and question difficulty affect the correctness at the resolution of each (LLM, question) pair.

### Rasch Model Performance

The Rasch model achieves an AUC-ROC of 0.85 on the training set and 0.83 on the test set on average, indicating that the Rasch model reliably reflects the LLMs' performance across a wide range of questions. The LLM's ability estimated via the Rasch calibration phase is effectively identical to widely used metrics on the AI leaderboards, such as average scores, with the two metrics perfectly correlated and yielding the same model ranking.

### Advanced IRT Applications (2024-2025)

More recent work has developed adaptive testing approaches. One approach called ATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability.

These developments show that Item Response Theory (IRT) has recently been applied to LLM evaluation, with researchers exploring how classical psychometric models can improve the efficiency and reliability of LLM benchmarking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "691e5c0d-fc93-4c7a-8042-ede268edf0ed",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "f3cad15a-a442-499b-a37a-75c33ebd4efe",
  "sourceToolAssistantUUID": "691e5c0d-fc93-4c7a-8042-ede268edf0ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-29T05:17:54.785Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T76GPiRCTge3cMgdGy5jbp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.13335",
  "prompt": "Extract the full title, all authors, submission date, and complete abstract of this paper about reliable and efficient amortized model-based evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3cad15a-a442-499b-a37a-75c33ebd4efe",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWJ1XV8znTXV4no3r6kr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea749139-12ef-4d8f-b1a0-3a51c295c650",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyZ4cw5H6PMAQCxUswWbMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2885,
      "cache_read_input_tokens": 26803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-29T05:17:55.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ChCyHL9pCMCAcaTbZjL9Hg`</summary>

```json
{
  "query": "Elo rating IRT comparison LLM leaderboard ranking calibration score 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea749139-12ef-4d8f-b1a0-3a51c295c650",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWJ1XV8znTXV4no3r6kr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a23d6bd-69d9-4ed1-95e9-ea5592205ce4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyZ4cw5H6PMAQCxUswWbMR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2885,
      "cache_read_input_tokens": 26803,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 26803,
          "cache_creation_input_tokens": 2885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2885,
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

_source line 85 · 2026-05-29T05:17:58.487Z_

<details><summary>↩ Tool result · `toolu_01T76GPiRCTge3cMgdGy5jbp`</summary>

```text
# Paper Summary

**Title:** "Reliable and Efficient Amortized Model-based Evaluation"

**Authors:** Sang Truong, Yuheng Tu, Percy Liang, Bo Li, Sanmi Koyejo

**Submission Date:** March 17, 2025

**Abstract:**

The research addresses the high cost of comprehensive language model evaluations across multiple benchmarks. Rather than assessing all questions, practitioners often use random subsets, which produces unreliable results due to question difficulty variations. The authors apply item response theory (IRT) principles, training a model to predict question difficulty from content alone. This enables reliable measurement at lower cost. Additionally, they develop a question generator that creates items at specified difficulty levels, supporting adaptive testing where questions are selected strategically based on evolving performance estimates. Testing across 22 natural language benchmarks and 172 language models demonstrates their approach provides "more reliable and efficient" results compared to standard practices.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea749139-12ef-4d8f-b1a0-3a51c295c650",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "63b41174-2e6d-4609-a40a-a7996e968533",
  "sourceToolAssistantUUID": "ea749139-12ef-4d8f-b1a0-3a51c295c650",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-29T05:18:02.270Z_

<details><summary>↩ Tool result · `toolu_01ChCyHL9pCMCAcaTbZjL9Hg`</summary>

```text
Web search results for query: "Elo rating IRT comparison LLM leaderboard ranking calibration score 2024 2025"

Links: [{"title":"Chatbot Arena (LMSYS) Review 2025: Is the LLM Leaderboard Reliable?","url":"https://skywork.ai/blog/chatbot-arena-lmsys-review-2025/"},{"title":"LLM Chess Leaderboard","url":"https://maxim-saplin.github.io/llm_chess/"},{"title":"Tournament-Style ELO Ranking","url":"https://www.emergentmind.com/topics/tournament-style-elo-ranking"},{"title":"How to Read Elo Ratings and Arena Scores for LLMs","url":"https://www.statology.org/how-to-read-elo-ratings-and-arena-scores-for-llms/"},{"title":"Elo Uncovered: Robustness and Best Practices in Language Model Evaluation | OpenReview","url":"https://openreview.net/forum?id=Pc9LLjTL5f"},{"title":"Metrics for evaluating LLMs. ELO Rating, BLEU, Perplexity and Cross… | by Jaideep Ray | Better ML | Medium","url":"https://medium.com/better-ml/metrics-for-evaluating-llms-2c9d86acdbf6"},{"title":"LMSYS Chatbot Arena ELO Ratings: The Ultimate AI Showdown (2024) 🤖 - ChatBench","url":"https://www.chatbench.org/lmsys-chatbot-arena-elo-ratings/"},{"title":"Model Consistency as a Cheap yet Predictive Proxy for LLM Elo Scores","url":"https://arxiv.org/pdf/2509.23510"}]

I found comprehensive information about Elo ratings, IRT, and LLM leaderboard rankings. Here are the key findings:

## Elo Ratings in LLM Leaderboards

LLM leaderboards like LMSYS Chatbot Arena use a Bradley–Terry model to estimate latent "strength" parameters for each model, then present these on an Elo-like scale with uncertainty intervals. The Elo system uses a mathematical formula to update ratings: New Rating = Old Rating + K × (Actual Result – Expected Result), where higher K values make ratings more responsive to recent results but also more volatile.

## IRT Methodology

HELM references IRT (Item Response Theory) methodology in its capabilities evaluation framework, offering an alternative approach to Elo-based scoring.

## 2024-2025 Developments

A paper published in September 2024 (revised January 2025) examines the Elo rating system in LLM evaluations, revealing its inherent volatility and providing empirical guidelines for robust model ranking. Despite alternatives, the Elo score method remains the gold standard because it captures both stylistic preferences and diverse task capabilities.

## Leaderboard Calibration

LMSYS maintains centralized leaderboards for multiple arenas and highlights confidence intervals directly in the interface. When examining Elo leaderboards, models with similar scores (within 20-30 points) should be considered roughly equivalent in performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a23d6bd-69d9-4ed1-95e9-ea5592205ce4",
  "isSidechain": true,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "agentId": "ab1852e2a938e1f06",
  "type": "user",
  "uuid": "6350e7b4-58ea-4680-a702-84ed2b5a0aa0",
  "sourceToolAssistantUUID": "0a23d6bd-69d9-4ed1-95e9-ea5592205ce4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-29T05:20:06.042Z_

Now I have comprehensive coverage. Here is the structured list of all papers found:

---

## Literature Survey: Item Response Theory Applied to LLM Evaluation (2024--2026)

### Paper 1: ATLAS -- Adaptive Testing for LLM Evaluation
- **Title:** Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks
- **Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
- **Date:** October 2025 (v1); February 2026 (v2)
- **Venue:** arXiv preprint (under review at ICML 2026 per OpenReview)
- **URL:** https://arxiv.org/abs/2511.04689
- **Summary:** Introduces ATLAS, a computerized adaptive testing framework using 3PL IRT with Fisher information-guided item selection that reduces required test items by up to 90% (e.g., 41 items instead of 5,600 on HellaSwag) while maintaining measurement precision.
- **Why important:** The most direct application of psychometric adaptive testing to LLM benchmarking. Demonstrates that IRT-based CAT can produce finer-grained ability estimates than raw accuracy, with 23--31% of 3,000+ models shifting significantly in rank. Directly relevant to the paper's goal of efficient, calibrated ability estimation.

---

### Paper 2: PSN-IRT -- Lost in Benchmarks?
- **Title:** Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory
- **Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao
- **Date:** May 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2505.15055
- **Summary:** Proposes Pseudo-Siamese Network for IRT (PSN-IRT) that models four item parameters (discriminability, difficulty, guessing-rate, feasibility) and analyzes 11 benchmarks with 41,871 items, revealing significant shortcomings in measurement quality.
- **Why important:** Core related work for jointly modeling item parameters and model ability. Demonstrates that IRT-selected item subsets produce rankings better aligned with human preferences, directly supporting the thesis that current benchmarks are psychometrically flawed.

---

### Paper 3: IrtNet -- Compact Representations of LLM Abilities
- **Title:** Learning Compact Representations of LLM Abilities via Item Response Theory
- **Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu
- **Date:** October 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2510.00844
- **Summary:** Proposes IrtNet, an IRT-based framework using Mixture-of-Experts networks to learn compact multidimensional ability vectors for LLMs alongside query discrimination vectors and difficulty parameters, enabling model routing and performance forecasting.
- **Why important:** Extends IRT from scalar ability to multidimensional latent representations. Shows how IRT parameters can be learned jointly via neural networks, bridging classical psychometrics with deep learning -- a methodological precedent for neural IRT in LLM evaluation.

---

### Paper 4: JE-IRT -- Joint Embedding Item Response Theory
- **Title:** JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory
- **Authors:** Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang
- **Date:** September 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2509.22888
- **Summary:** Places LLMs and test items in a shared geometric embedding space where question direction encodes semantics, magnitude encodes difficulty, and model-question alignment determines performance. Reveals an internal LLM taxonomy that diverges from conventional subject classifications.
- **Why important:** Novel geometric/embedding-based extension of IRT that provides interpretable visualizations of model abilities. The geometric framework could complement contamination detection by revealing anomalous ability patterns.

---

### Paper 5: IRT-Router
- **Title:** IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory
- **Authors:** Wei Song, Zhenya Huang, Cheng Cheng, Weibo Gao, Bihan Xu, GuanHao Zhao, Fei Wang, Runze Wu
- **Date:** July 2025
- **Venue:** ACL 2025 (Long Papers), Vienna, Austria
- **URL:** https://aclanthology.org/2025.acl-long.761/
- **Summary:** Uses IRT to model LLM ability and query difficulty/discrimination for routing user queries to the most suitable model among 20 LLMs across 12 datasets, with strong cold-start performance.
- **Why important:** Demonstrates practical downstream use of IRT-estimated ability parameters. Published at a top venue (ACL 2025), validating the IRT-for-LLM-evaluation paradigm in the NLP community.

---

### Paper 6: LaRT -- Latency-Response Theory
- **Title:** Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length
- **Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu
- **Date:** December 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2512.07019
- **Summary:** Extends IRT by jointly modeling response accuracy and chain-of-thought length, introducing latent ability, latent speed, and a correlation parameter between them. Finds strong negative correlation between ability and speed (more capable models produce longer reasoning chains).
- **Why important:** Extends classical IRT to incorporate process data (CoT length) alongside correctness, a novel psychometric direction. The joint modeling approach is conceptually parallel to jointly modeling contamination and robustness, offering methodological inspiration.

---

### Paper 7: Diagnosing LLM-as-a-Judge Reliability via IRT
- **Title:** Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
- **Authors:** Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim
- **Date:** January 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2602.00521
- **Summary:** Applies the Graded Response Model (GRM) from IRT to diagnose LLM judge reliability across two dimensions: intrinsic consistency (stability under prompt variations) and human alignment (correspondence with human assessments).
- **Why important:** Applies IRT not to evaluate LLM test-takers but LLM judges, broadening the psychometric framework to evaluation reliability. The GRM approach is relevant to modeling graded/partial responses in benchmark evaluation.

---

### Paper 8: IRT for Automatic Short Answer Grading
- **Title:** Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory
- **Authors:** Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, Ulf Kroehne
- **Date:** April 2026
- **Venue:** BEA 2026
- **URL:** https://arxiv.org/abs/2605.00238
- **Summary:** Models grading correctness as a function of latent grader ability and response difficulty using IRT. Analysis of 17 open-weight LLMs reveals that models with comparable aggregate performance differ substantially on difficult responses.
- **Why important:** Demonstrates IRT's ability to reveal performance differences invisible to aggregate metrics, supporting the argument that IRT-based evaluation is more informative than simple accuracy.

---

### Paper 9: LEGO-IRT -- Unified Framework for Data-Efficient Evaluation
- **Title:** Toward a unified framework for data-efficient evaluation of large language models
- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang
- **Date:** October 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2510.04051
- **Summary:** Proposes LEGO-IRT, a multidimensional IRT framework that handles both discrete and continuous scoring metrics, decomposes ability into general and context-specific components, and achieves stable estimates with only 3% of evaluation items across 70 LLMs and 5 benchmarks.
- **Why important:** Addresses a key limitation of prior IRT-for-LLM work (restriction to binary correctness). The ability decomposition and structural modeling across benchmarks is directly relevant to jointly modeling multiple evaluation dimensions.

---

### Paper 10: tinyBenchmarks
- **Title:** tinyBenchmarks: evaluating LLMs with fewer examples
- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- **Date:** February 2024
- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)
- **URL:** https://arxiv.org/abs/2402.14992
- **Summary:** Demonstrates that 100 IRT-curated examples suffice to estimate LLM performance on MMLU (14K items), achieving ~2% estimation error. Introduces the gp-IRT estimator combining direct sampling with IRT predictions, reducing evaluation cost by 140x.
- **Why important:** Foundational work establishing IRT-based benchmark reduction for LLMs at a top venue (ICML). The gp-IRT estimator and item selection strategies set the baseline that subsequent work (ATLAS, PSN-IRT, LEGO-IRT) builds upon.

---

### Paper 11: metabench
- **Title:** metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models
- **Authors:** Alex Kipnis, Konstantinos Voudouris, Luca M. Schulze Buschoff, Eric Schulz
- **Date:** July 2024 (v1); February 2025 (v2)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2407.12844
- **Summary:** Uses IRT to distill six major LLM benchmarks (28,632 items) into 858 items (<3%) while reconstructing scores with 1.24% RMSE. Reveals a single latent factor capturing 79.3% of cross-benchmark variability (Spearman r=0.94 with total score).
- **Why important:** Published at ICLR 2025, demonstrating IRT-based benchmark compression at scale. The finding that a single factor dominates has implications for understanding what LLM benchmarks actually measure -- relevant to contamination analysis.

---

### Paper 12: Efficiently Measuring Cognitive Ability of LLMs
- **Title:** Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective
- **Authors:** Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Rui Lv, Zhenya Huang, GuanHao Zhao, Zheng Zhang, Qingyang Mao, Shijin Wang, Enhong Chen
- **Date:** June 2023 (v1); published 2024
- **Venue:** ICLR 2024
- **URL:** https://ar5iv.labs.arxiv.org/html/2306.10512
- **Summary:** Pioneering work applying CAT to LLM evaluation across subject knowledge, math reasoning, and programming. Finds ChatGPT exhibits "careless student" behavior (high slip/guess rates) while GPT-4 reaches middle-level student ability.
- **Why important:** One of the earliest papers applying psychometric adaptive testing to LLMs, published at ICLR 2024. The "careless student" finding for ChatGPT is an early signal that IRT reveals qualitative behavioral patterns, not just scores.

---

### Paper 13: RIDE -- Adversarial Perturbation with IRT
- **Title:** RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning
- **Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan
- **Date:** November 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2511.04120
- **Summary:** Combines IRT with RL-based adversarial question rewriting to generate difficulty-calibrated perturbations of math benchmarks. Uses 35 LLMs as simulated test-takers to build a difficulty ranker, causing an average 21.73% accuracy drop across 26 models.
- **Why important:** Directly bridges IRT and adversarial robustness evaluation -- the closest existing work to jointly modeling difficulty and robustness. The IRT-guided perturbation framework is a key methodological precedent for the proposed AAAI paper.

---

### Paper 14: Confident Rankings with Fewer Items (Continuous CAT)
- **Title:** Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores
- **Authors:** Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier
- **Date:** January 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2601.13885
- **Summary:** Extends CAT from binary IRT to continuous scores using a heteroskedastic normal distribution, enabling adaptive testing with ROUGE, BLEU, and LLM-as-a-Judge metrics. Incorporates uncertainty-aware ranking with adaptive stopping.
- **Why important:** Generalizes IRT-based adaptive testing beyond multiple-choice to generation tasks, broadening the applicability of psychometric evaluation. The uncertainty-aware ranking methodology is relevant to producing calibrated ability estimates.

---

### Paper 15: CAT for Medical LLM Benchmarking
- **Title:** Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking
- **Authors:** Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng
- **Date:** February 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2603.23506
- **Summary:** Applies IRT-based CAT to medical LLM evaluation, achieving near-perfect correlation with full-bank estimates (r=0.988) using only 1.3% of items, reducing evaluation from hours to minutes per model across 38 models.
- **Why important:** Domain-specific validation of IRT-CAT for LLM evaluation in a high-stakes setting (medicine). The 1.3% item usage with r=0.988 is the strongest efficiency result reported, demonstrating the power of psychometric methods.

---

### Paper 16: Growing Pains -- Fixed Parameter Calibration
- **Title:** Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration
- **Authors:** Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky
- **Date:** April 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2604.12843
- **Summary:** Uses multidimensional IRT with anchor items to enable extensible benchmarking where new datasets are calibrated against fixed parameters, achieving score prediction within 2--3 percentage points and Spearman rho >= 0.9 across 400+ models.
- **Why important:** Addresses the practical challenge of benchmark extensibility -- new items and models can be added without re-evaluating everything. The anchor-item approach from educational testing is a mature psychometric technique newly applied to LLMs.

---

### Paper 17: Reliable and Efficient Amortized Model-Based Evaluation
- **Title:** Reliable and Efficient Amortized Model-based Evaluation
- **Authors:** Sang Truong, Yuheng Tu, Percy Liang, Bo Li, Sanmi Koyejo
- **Date:** March 2025
- **Venue:** arXiv preprint (Stanford CRFM)
- **URL:** https://arxiv.org/abs/2503.13335
- **Summary:** Trains a model to predict question difficulty from content alone using IRT, enabling reliable measurement at lower cost. Also develops a question generator that creates items at specified difficulty levels for adaptive testing. Validated across 22 benchmarks and 172 LLMs.
- **Why important:** From Stanford CRFM (HELM team), this work amortizes IRT calibration by predicting item parameters from question text, removing the need for large response matrices. The difficulty-controlled item generation capability is relevant to both contamination testing and adaptive evaluation.

---

### Paper 18: Scalable IRT via Matrix Factorization
- **Title:** An Interpretable and Scalable Framework for Evaluating Large Language Models
- **Authors:** Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu
- **Date:** May 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2605.07046
- **Summary:** Reformulates IRT parameter estimation as constrained matrix factorization using the majorization-minimization principle, achieving orders-of-magnitude speedups with theoretical guarantees for identifiability and convergence.
- **Why important:** Addresses scalability of IRT estimation for large LLM evaluation matrices (many models x many items), providing the computational infrastructure needed for practical deployment of IRT-based evaluation.

---

### Paper 19: Benchmark Health Index
- **Title:** Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs
- **Authors:** Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao
- **Date:** February 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2602.11674
- **Summary:** Proposes BHI, a data-driven framework evaluating benchmark quality across capability discrimination, anti-saturation, and impact dimensions, synthesizing 106 benchmarks from 91 models.
- **Why important:** While not strictly IRT-based, addresses benchmark quality assessment from a measurement perspective. The discrimination and saturation metrics are closely related to IRT item parameters, and the meta-evaluation approach complements IRT-based item analysis.

---

### Paper 20: M3IRT -- Multimodal Item Response Theory
- **Title:** Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory
- **Authors:** Shunki Uebayashi, Kento Masui, Kyohei Atarashi, Han Bao, Hisashi Kashima, Naoto Inoue, Mayu Otani, Koh Takeuchi
- **Date:** March 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2603.02663
- **Summary:** Extends IRT to multimodal evaluation by decomposing model ability and question difficulty into image-only, text-only, and cross-modal components. Identifies shortcut questions and preserves ranking fidelity even when 50% of items are low-quality.
- **Why important:** Demonstrates IRT's extensibility to multimodal settings and shows robustness to low-quality items -- a property relevant to contamination-robust evaluation.

---

### Paper 21: LLM Psychometrics Survey
- **Title:** Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement
- **Authors:** Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song
- **Date:** May 2025 (v1); March 2026 (v3)
- **Venue:** arXiv preprint (survey)
- **URL:** https://arxiv.org/abs/2505.08245
- **Summary:** Comprehensive survey of "LLM Psychometrics" as an emerging field, synthesizing work on applying psychometric instruments, theories, and principles to evaluate, understand, and enhance LLMs. Covers benchmarking frameworks, validation methodologies, and enhancement techniques.
- **Why important:** The key survey paper positioning IRT-for-LLM-evaluation within the broader psychometrics landscape. Essential citation for framing the related work section and understanding the field's trajectory.

---

### Paper 22: Lifting the Benchmark Iceberg with IRT
- **Title:** Lifting the benchmark iceberg with item-response theory
- **Authors:** Mara Schilling-Wilhelmi, Nawaf Alampara, Kevin Maik Jablonka
- **Date:** 2025
- **Venue:** ICLR 2025 Workshop on AI4MAT
- **URL:** https://openreview.net/forum?id=ZyVQqK7mcP
- **Summary:** Investigates how hidden implementation choices in LLM benchmarks distort model rankings (the "benchmark iceberg" phenomenon) and proposes IRT as a transparency tool.
- **Why important:** Highlights a complementary angle -- IRT as a diagnostic tool for benchmark transparency rather than just efficiency. The "benchmark iceberg" framing connects to contamination concerns where hidden factors distort evaluation.

---

### Summary of Coverage by Theme

**Adaptive Testing / Efficient Evaluation:** Papers 1 (ATLAS), 10 (tinyBenchmarks), 11 (metabench), 12 (Cognitive Ability CAT), 14 (Continuous CAT), 15 (Medical CAT), 17 (Amortized Evaluation)

**IRT Model Extensions for LLMs:** Papers 2 (PSN-IRT), 3 (IrtNet), 4 (JE-IRT), 6 (LaRT), 9 (LEGO-IRT), 18 (Matrix Factorization IRT), 20 (M3IRT)

**IRT for Robustness/Adversarial Evaluation:** Paper 13 (RIDE) -- the most directly relevant to the proposed AAAI paper's joint contamination-robustness modeling

**Benchmark Quality / Meta-Evaluation:** Papers 11 (metabench), 19 (BHI), 22 (Benchmark Iceberg)

**Applied IRT for LLM Evaluation:** Papers 5 (IRT-Router), 7 (LLM-as-Judge), 8 (Short Answer Grading), 16 (Fixed Parameter Calibration)

**Survey:** Paper 21 (LLM Psychometrics)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6350e7b4-58ea-4680-a702-84ed2b5a0aa0",
  "isSidechain": true,
  "agentId": "ab1852e2a938e1f06",
  "requestId": "req_011CbWJ2KHwXJfNTYRYdxvxr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f3e0f93-a340-4c39-9d19-3092634e7a96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrxVqh316T6knM52Jnirjg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 29688,
      "output_tokens": 5777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5777,
          "cache_read_input_tokens": 29688,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1226,
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
