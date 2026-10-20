# Research conversation: I need to deeply understand the paper "Decoding Answers Before Chain-of-Thought" (arXiv 2603.01437) to differentiate a p

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4f75ce9cd4490ba2.jsonl`
- **Structured JSON:** [`1c123a187aedc3252be1.json`](../../sessions/1c/1c123a187aedc3252be1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-19T14:35:02.550Z_

I need to deeply understand the paper "Decoding Answers Before Chain-of-Thought" (arXiv 2603.01437) to differentiate a proposed research component from it.

Our proposal includes using linear probes on open-source model hidden states to test whether tool identity is encoded in activations BEFORE reasoning tokens are generated, in multi-turn agentic tool-selection settings.

The reviewer says this closely mirrors "Decoding Answers Before CoT" which already showed this for QA with 0.9 AUC.

I need to:
1. Search for and read this paper in detail (arXiv 2603.01437)
2. Search for "pre-CoT activation probing" or "answer encoded before chain of thought" to find related work
3. Search for "tool call hidden state probing LLM" to see if anyone has done probing specifically for tool calls
4. Search for "structured output probing LLM" — tool calls involve structured JSON output which is fundamentally different from text answers

Key questions I need answered:
- What exactly does "Decoding Answers Before CoT" show? What models, what tasks, what probe accuracy?
- What are the key methodological differences between probing for a text answer vs. probing for a tool call (structured JSON with function name + parameters)?
- Are there unique challenges in probing for tool identity? (e.g., tool calls are multi-dimensional: tool name + parameter values, tool calls happen in a conversation context with prior tool results, etc.)
- Has anyone specifically probed for tool call decisions in hidden states?

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "20e7c2ed-b631-4eed-b7d8-2a855fdd582b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T14:35:02.553Z_

```json
{
  "parentUuid": "20e7c2ed-b631-4eed-b7d8-2a855fdd582b",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
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
  "uuid": "059491ed-976c-40fb-bef4-f2d677ccdf22",
  "timestamp": "2026-05-19T14:35:02.553Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T14:35:02.554Z_

```json
{
  "parentUuid": "059491ed-976c-40fb-bef4-f2d677ccdf22",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "08f6a68a-e1bd-4abb-a486-e76640181a77",
  "timestamp": "2026-05-19T14:35:02.554Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T14:35:05.569Z_



I'll conduct a thorough search for this paper and related work across multiple sources. Let me start by fetching the paper and running several web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f6a68a-e1bd-4abb-a486-e76640181a77",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6Qhv8PLHMUQX7zJZND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69d42338-9c3f-44df-afdf-3ff3577acf81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01867qGi4DBMmios9VFZfq1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1712,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1712,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T14:35:05.917Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MsaXdpqjgVweshbnTZpQsN`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d42338-9c3f-44df-afdf-3ff3577acf81",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6Qhv8PLHMUQX7zJZND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b362fce-d3aa-470b-b31d-c10aca7f4aae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01867qGi4DBMmios9VFZfq1t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1712,
      "cache_read_input_tokens": 7773,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1712,
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

_source line 6 · 2026-05-19T14:35:05.921Z_

<details><summary>↩ Tool result · `toolu_01MsaXdpqjgVweshbnTZpQsN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "7b362fce-d3aa-470b-b31d-c10aca7f4aae",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "b47def25-302e-4b2a-929d-d4931ff9eb18",
  "sourceToolAssistantUUID": "7b362fce-d3aa-470b-b31d-c10aca7f4aae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T14:35:08.680Z_



Now let me fetch the paper directly and run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b47def25-302e-4b2a-929d-d4931ff9eb18",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6QxXCtd6b3KyYcqA1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f32f217-995e-401c-a19c-28506be4b257",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvkCvdDFbaafzHup58RV95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 8 · 2026-05-19T14:35:10.110Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012CugvwR8V44cPTcXvhVfZY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.01437",
  "prompt": "Extract the full paper details: title, authors, abstract, and all content available on this page. I need to understand exactly what this paper shows about decoding answers before chain-of-thought reasoning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f32f217-995e-401c-a19c-28506be4b257",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6QxXCtd6b3KyYcqA1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c061258-ea70-4b9d-a2d5-3650b5cddcd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvkCvdDFbaafzHup58RV95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 9 · 2026-05-19T14:35:10.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019tbp9spPwWf34xhdYBpHZd`</summary>

```json
{
  "query": "arXiv 2603.01437 \"Decoding Answers Before Chain-of-Thought\" paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c061258-ea70-4b9d-a2d5-3650b5cddcd1",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6QxXCtd6b3KyYcqA1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "883c10b4-9852-4bf8-8470-dc8ea9d2b0e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvkCvdDFbaafzHup58RV95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 10 · 2026-05-19T14:35:11.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GxjYu83oaPRb7d2aB9fgz9`</summary>

```json
{
  "query": "\"pre-CoT activation probing\" OR \"answer encoded before chain of thought\" LLM hidden states"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "883c10b4-9852-4bf8-8470-dc8ea9d2b0e8",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6QxXCtd6b3KyYcqA1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0085c301-d4fa-4cff-b6c4-90f5a62a9e67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvkCvdDFbaafzHup58RV95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 11 · 2026-05-19T14:35:11.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018WjpNDDvcUwYfs2CscteHp`</summary>

```json
{
  "query": "tool call hidden state probing LLM agent tool selection mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0085c301-d4fa-4cff-b6c4-90f5a62a9e67",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6QxXCtd6b3KyYcqA1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8e086fa-3e32-4f89-b2ea-be9ad74e0a85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvkCvdDFbaafzHup58RV95",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 12 · 2026-05-19T14:35:12.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KLXNzWY4vYU8HwqGGnCA1a`</summary>

```json
{
  "query": "structured output probing LLM hidden states JSON function calling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8e086fa-3e32-4f89-b2ea-be9ad74e0a85",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6QxXCtd6b3KyYcqA1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29e04a09-381f-4a83-a454-c7c600249114",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvkCvdDFbaafzHup58RV95",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9485,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 9485,
          "cache_creation_input_tokens": 1136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1136,
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

_source line 13 · 2026-05-19T14:35:14.798Z_

<details><summary>↩ Tool result · `toolu_012CugvwR8V44cPTcXvhVfZY`</summary>

```text
# Paper Details: Decoding Answers Before Chain-of-Thought

**Title:** "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering"

**Authors:** Kyle Cox, Darius Kianersi, Adrià Garriga-Alonso

**Submission Date:** March 2, 2026

**arXiv Identifier:** 2603.01437

## Key Findings

The research demonstrates that instruction-tuned language models often arrive at their final answer before generating chain-of-thought reasoning. The researchers trained linear probes on residual stream activations and achieved "0.9 AUC on most tasks" when predicting answers before reasoning appeared.

More significantly, they found these decision patterns were causal: "steering activations along the probe direction flips model answers in over 50% of cases."

## Failure Modes

When steering activated incorrect answers, the models exhibited two distinct behaviors:

1. **Non-entailment:** Stating correct premises but reaching unsupported conclusions
2. **Confabulation:** Fabricating false premises entirely

## Implications

The findings suggest chain-of-thought reasoning may not reflect the actual decision process. While this post-hoc reasoning works instrumentally when models hold correct beliefs initially, it becomes problematic when the underlying model conclusion is incorrect, potentially generating convincing but false justifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c061258-ea70-4b9d-a2d5-3650b5cddcd1",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "0cc1ad2d-1580-4b13-9ce5-53adde54a02a",
  "sourceToolAssistantUUID": "7c061258-ea70-4b9d-a2d5-3650b5cddcd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T14:35:17.595Z_

<details><summary>↩ Tool result · `toolu_019tbp9spPwWf34xhdYBpHZd`</summary>

```text
Web search results for query: "arXiv 2603.01437 "Decoding Answers Before Chain-of-Thought" paper"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"C3oT: Generating Shorter Chain-of-Thought without Compromising   Effectiveness","url":"https://arxiv.org/pdf/2412.11664"},{"title":"Fast Chain-of-Thought: A Glance of Future from Parallel Decoding Leads   to Answers Faster","url":"https://arxiv.org/pdf/2311.08263"}]

Based on the web search results, here's information about the arXiv paper 2603.01437:

## Title
"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering"

## Authors
Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso

## Main Finding
The paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT.

## Key Results
Training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks. Additionally, the directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

## Context and Significance
The utility of CoT toward interpretability depends upon its faithfulness -- whether the model's stated reasoning reflects the underlying decision process. This paper investigates that concern by demonstrating that models may generate CoT reasoning post-hoc after already determining their answer.

When steering induces incorrect answers, the study observes two distinct failure modes: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883c10b4-9852-4bf8-8470-dc8ea9d2b0e8",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "b6a9a38e-8659-4afe-b498-72900c6148db",
  "sourceToolAssistantUUID": "883c10b4-9852-4bf8-8470-dc8ea9d2b0e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T14:35:18.514Z_

<details><summary>↩ Tool result · `toolu_01KLXNzWY4vYU8HwqGGnCA1a`</summary>

```text
Web search results for query: "structured output probing LLM hidden states JSON function calling"

Links: [{"title":"The guide to structured outputs and function calling with LLMs","url":"https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms"},{"title":"llm-structured-output · PyPI","url":"https://pypi.org/project/llm-structured-output/"},{"title":"How to build function calling and JSON mode for open-source and fine-tuned LLMs","url":"https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/"},{"title":"How do Structured Outputs Work? | Cohere","url":"https://docs.cohere.com/docs/structured-outputs"},{"title":"JSON Mode vs Function Calling vs Structured Output: 2026 Guide","url":"https://www.buildmvpfast.com/blog/structured-output-llm-json-mode-function-calling-production-guide-2026"},{"title":"Structured Outputs | Developer Documentation","url":"https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"}]

Based on the search results, here's what I found related to structured output, probing LLM hidden states, JSON, and function calling:

## Structured Output and Function Calling

Reliable JSON from LLMs can be obtained using structured outputs, JSON mode, Pydantic, Instructor, and Outlines, with code examples available for OpenAI, Claude, and Gemini for consistent data extraction. Structured output enforces an output schema defined as part of the LLM input, with the LLM output guaranteed to adhere to the provided schema with full Pydantic support.

Function calling (also known as "tool use") lets you pass a set of defined tools to an LLM as part of the request body, and based on the prompt, the model selects and returns the most appropriate function/tool from the provided options.

## Technical Implementation

The technical approach uses logit manipulation: Logit biasing guarantees valid output structure by identifying every invalid token and setting its score to negative infinity, ensuring that invalid tokens cannot be generated.

## Probing Hidden States

Internal representations (residual stream, attention outputs, and MLP outputs) are extracted from any combination of layers from a frozen transformer, pooled, concatenated, and used to train lightweight probe networks that learn to map internal states to calibrated predictions. PING (Probing INternal states of Generative models) is a framework that leverages internal states for improved predictions directly at inference time, turning latent signals into calibrated, deployable predictions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29e04a09-381f-4a83-a454-c7c600249114",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "c5948778-63a7-44bf-8905-3c2ad55efe5a",
  "sourceToolAssistantUUID": "29e04a09-381f-4a83-a454-c7c600249114",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T14:35:19.087Z_

<details><summary>↩ Tool result · `toolu_01GxjYu83oaPRb7d2aB9fgz9`</summary>

```text
Web search results for query: ""pre-CoT activation probing" OR "answer encoded before chain of thought" LLM hidden states"

Links: [{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/pdf/2603.17199"},{"title":"Knowing Before Saying: LLM Representations Encode Information About Chain-of-Thought Success Before Completion","url":"https://arxiv.org/html/2505.24362v2"},{"title":"[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"},{"title":"Paper page - Knowing Before Saying: LLM Representations Encode Information About Chain-of-Thought Success Before Completion","url":"https://huggingface.co/papers/2505.24362"}]

I found relevant research on this topic. Here are the key findings:

## Pre-CoT Activation Probing Research

Recent research provides mechanistic evidence that instruction-tuned models often determine their answer before generating chain-of-thought, with linear probes trained on residual stream activations at the last token before CoT predicting the model's final answer with 0.9 AUC on most tasks.

These probe directions are not only predictive but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

### Key Findings:

1. **Answer Pre-commitment**: The model's final answer is encoded in pre-CoT activations in the residual stream and is linearly decodable by a simple probe.

2. **Causal Evidence**: The probe direction is not merely predictive but causal: steering activations along this direction shifts the model's answer far more than equally large orthogonal perturbations.

3. **Confabulation Patterns**: When steered in the direction of the incorrect response, the model's verbalized reasoning exhibits confabulation (stating false premises to support the steered answer) and non-entailment (stating true premises but giving a conclusion that does not follow).

### Related Work:

Other research shows that pre-generation probes applied before any CoT tokens are generated predict behaviors as well as monitoring full CoT traces, and can flag behavior early, potentially avoiding unnecessary generation.

The primary paper on this topic is "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" by Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso (March 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0085c301-d4fa-4cff-b6c4-90f5a62a9e67",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "d4ec1da1-4c83-47c6-94eb-581637fb7caf",
  "sourceToolAssistantUUID": "0085c301-d4fa-4cff-b6c4-90f5a62a9e67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T14:35:19.802Z_

<details><summary>↩ Tool result · `toolu_018WjpNDDvcUwYfs2CscteHp`</summary>

```text
Web search results for query: "tool call hidden state probing LLM agent tool selection mechanistic interpretability"

Links: [{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v1"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection","url":"https://arxiv.org/html/2601.05214v1"},{"title":"Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/html/2605.07990"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback","url":"https://arxiv.org/html/2605.17453"},{"title":"Towards eliciting latent knowledge from LLMs with mechanistic interpretability","url":"https://arxiv.org/pdf/2505.14352"},{"title":"How to Evaluate Tool-Calling Agents - Arize AI","url":"https://arize.com/blog/how-to-evaluate-tool-calling-agents/"},{"title":"AutoTool: Efficient Tool Selection for Large Language Model Agents","url":"https://arxiv.org/pdf/2511.14650"}]

I've completed the web search. Here are the key findings related to your query about tool call hidden state probing, LLM agents, tool selection, and mechanistic interpretability:

## Key Research Areas

**Hidden State Probing for Tool Selection:**

Tool necessity is linearly decodable from language models' pre-generation representations with high accuracy (AUROC 0.89–0.96), and a mechanistic approach using lightweight linear probes can leverage the model's encoded tool-call decisions with minimal inference cost.

**Tool Calling Hallucinations:**

LLMs exhibit tool-calling hallucinations where they generate structurally plausible but functionally incorrect tool calls, manifesting as inappropriate tool selection, malformed parameters, incorrect tool chaining, or semantically incorrect function invocations.

**Mechanistic Interpretability of Tool Calling:**

Per-tool mean activations can both enable steering and flag likely-wrong calls, providing mechanistic visibility into which components carry tool selection.

**Recent Work:**

The search results include several recent papers (from January-May 2026) on this topic:
- "LLM Agents Already Know When to Call Tools - Even Without Reasoning" (1 week ago)
- "Internal Representations as Indicators of Hallucinations in Agent Tool Selection" (January 2026)
- "Tool Calling is Linearly Readable and Steerable in Language Models" (2 weeks ago)

These papers collectively demonstrate that language models' hidden representations encode tool-selection decisions and that mechanistic interpretability techniques can be used to understand, probe, and improve tool calling behavior in LLM agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8e086fa-3e32-4f89-b2ea-be9ad74e0a85",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "84bc979a-d8fa-4455-a3da-676d4e322722",
  "sourceToolAssistantUUID": "a8e086fa-3e32-4f89-b2ea-be9ad74e0a85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T14:35:23.433Z_

Excellent -- I found highly relevant results, especially papers that appear to directly overlap with your proposal. Let me now fetch the full HTML version of the main paper, plus the critically important papers about tool-call probing that just appeared.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84bc979a-d8fa-4455-a3da-676d4e322722",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6RyfwjTSwFLLB4J9n4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a16a3fd-6369-4c01-a425-bf6252570cc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x1zpk9YNAw5EAvcVfjxRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 749,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 10621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
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

_source line 19 · 2026-05-19T14:35:26.723Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VuzYdcHh6DAAdT3jbRLcCJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01437",
  "prompt": "Extract ALL details from this paper: (1) exact models used, (2) exact tasks/benchmarks, (3) probe methodology (what type of probe, what layer, what token position, what features), (4) exact AUC numbers per task, (5) steering methodology and results, (6) failure modes observed, (7) limitations section, (8) what they say about future work, (9) whether they mention tool calling or structured outputs at all, (10) how many answer classes they probe for (binary vs multi-class). Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a16a3fd-6369-4c01-a425-bf6252570cc2",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6RyfwjTSwFLLB4J9n4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75f9fee3-8b27-4f8d-991d-8ce9d0501470",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x1zpk9YNAw5EAvcVfjxRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 749,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 10621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
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

_source line 20 · 2026-05-19T14:35:29.551Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TKqPbp1sHN1mDHi99brYwg`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.07990",
  "prompt": "Extract ALL details from this paper \"Tool Calling is Linearly Readable and Steerable in Language Models\": (1) exact models used, (2) what they probe for (tool name, parameters, both?), (3) probe methodology, (4) exact accuracy/AUC numbers, (5) what tasks/benchmarks, (6) whether they do multi-turn or single-turn, (7) whether they consider structured JSON output, (8) limitations, (9) how this differs from probing for text answers, (10) all key findings. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75f9fee3-8b27-4f8d-991d-8ce9d0501470",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6RyfwjTSwFLLB4J9n4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba1e1615-d008-4617-a0bd-6984de14cc4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x1zpk9YNAw5EAvcVfjxRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 749,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 10621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
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

_source line 21 · 2026-05-19T14:35:31.913Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WyPkasmBhP1KDcRib5stUo`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.09252v1",
  "prompt": "Extract ALL details from this paper \"LLM Agents Already Know When to Call Tools - Even Without Reasoning\": (1) exact models, (2) methodology, (3) key findings, (4) accuracy numbers, (5) whether they probe for tool identity or just tool-use-vs-no-tool-use, (6) whether multi-turn is considered, (7) how this relates to chain-of-thought probing, (8) limitations. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba1e1615-d008-4617-a0bd-6984de14cc4f",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6RyfwjTSwFLLB4J9n4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e8abbd4-9a2b-4044-9c43-691d6a240709",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x1zpk9YNAw5EAvcVfjxRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 749,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 10621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
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

_source line 22 · 2026-05-19T14:35:33.334Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016QQ3HXfEXC8kmqqiKJwNCH`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.05214v1",
  "prompt": "Extract ALL details from this paper \"Internal Representations as Indicators of Hallucinations in Agent Tool Selection\": (1) exact models, (2) methodology, (3) key findings, (4) accuracy numbers, (5) what they probe for, (6) whether they look at tool name vs parameters vs both, (7) multi-turn or single-turn, (8) limitations. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8abbd4-9a2b-4044-9c43-691d6a240709",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6RyfwjTSwFLLB4J9n4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4a07b9b-c0df-4da1-8dd7-4331f43fa025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x1zpk9YNAw5EAvcVfjxRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 749,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 10621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
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

_source line 23 · 2026-05-19T14:35:34.314Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BXGtnjtzaZbYqFJATEJJBN`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.17199",
  "prompt": "Extract ALL details from this paper about \"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing\": (1) methodology, (2) models, (3) key findings, (4) how it relates to pre-CoT probing, (5) accuracy numbers, (6) what they probe for. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a07b9b-c0df-4da1-8dd7-4331f43fa025",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6RyfwjTSwFLLB4J9n4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed41e2d4-b6d2-424c-9409-b724080f86c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x1zpk9YNAw5EAvcVfjxRh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 749,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 10621,
      "output_tokens": 910,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 749,
          "output_tokens": 910,
          "cache_read_input_tokens": 10621,
          "cache_creation_input_tokens": 2944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2944,
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

_source line 24 · 2026-05-19T14:35:40.839Z_

<details><summary>↩ Tool result · `toolu_01BXGtnjtzaZbYqFJATEJJBN`</summary>

```text
# Paper Analysis: Catching Rationalization in the Act

## Methodology
The researchers use **activation probing** to detect motivated reasoning in language models. They train classifiers on neural network activations to identify when models are engaging in rationalization—generating justifications for predetermined conclusions rather than genuine reasoning.

## Models Tested
The paper evaluates multiple large language models including Llama 3, Gemma 3, and Qwen 3, examining their behavior across different scales and architectures.

## Key Findings
The central discovery is that models exhibit detectable signal of motivated reasoning *before* generating Chain-of-Thought (CoT) outputs. The activation patterns reveal biased reasoning processes that precede the explicit reasoning text. This enables "catching rationalization in the act" by probing internal representations.

## Pre-CoT vs. Post-CoT Probing
Critically, the authors demonstrate activation patterns differ **before** versus **after** CoT generation. Pre-CoT probing reveals the model's initial reasoning bias, while post-CoT probing captures outputs after explicit justification generation. This temporal distinction is essential for detecting genuine versus motivated reasoning.

## Accuracy Metrics
While specific percentages aren't clearly extracted from this PDF excerpt, the paper shows classifiers trained on activations can reliably distinguish rationalization from authentic reasoning across the tested models.

## What They Probe For
The probes specifically target internal representations indicating:
- Predetermined conclusion commitment
- Bias toward particular answers
- Genuine versus post-hoc reasoning signals
- Decision-making processes occurring in neural activations

---
**Code availability**: The authors provide implementation at GitHub (https://github.com/seyedparsa/motivated-reasoning)

[Binary content (application/pdf, 728.8KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/826e68f0-f084-4703-baa7-eafff3ec0b55/tool-results/webfetch-1779201334500-y5194j.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed41e2d4-b6d2-424c-9409-b724080f86c0",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "817b757a-9b41-4b0d-ae31-a19757fd0c92",
  "sourceToolAssistantUUID": "ed41e2d4-b6d2-424c-9409-b724080f86c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T14:35:44.665Z_

<details><summary>↩ Tool result · `toolu_01VuzYdcHh6DAAdT3jbRLcCJ`</summary>

```text
# Paper Analysis: Decoding Answers Before Chain-of-Thought

## (1) Exact Models Used
- **Gemma 2**: 2B-it, 9B-it (instruction-tuned)
- **Qwen 2.5 Instruct**: 1.5B-it, 3B-it, 7B-it (instruction-tuned)
- **Reasoning model tested**: GPT-OSS 20B (limited experiments in Appendix F)

## (2) Exact Tasks/Benchmarks
Four binary classification tasks:
1. **Anachronisms**: Historical event anachronism detection
2. **Logical Deduction**: Conclusion validity from premises
3. **Sports Understanding**: Statement plausibility assessment
4. **Social Chemistry**: Social interaction appropriateness judgment

All formatted as binary (A/B) choice tasks with 500 train/500 test examples and four few-shot CoT demonstrations.

## (3) Probe Methodology
- **Type**: Difference-of-means linear probes on residual stream activations
- **Token position**: Last pre-CoT token (colon in "Let's think step by step:")
- **Layer**: The layer with highest AUC across residual stream
- **Features**: Difference between mean activations for "yes" vs "no" answers computed as: "𝐰(ℓ) = 𝝁yes(ℓ) − 𝝁no(ℓ)"
- **Scoring metric**: Cosine similarity between test activations and probe direction

## (4) Exact AUC Numbers Per Task

| Model | Anachronisms | Logic | Social | Sports |
|-------|-------------|-------|--------|--------|
| Gemma 2 2B | 0.997 | 0.688 | 0.996 | 0.924 |
| Gemma 2 9B | 0.999 | 0.878 | 0.996 | 0.956 |
| Qwen 2.5 1.5B | 0.988 | 0.707 | 0.993 | 0.808 |
| Qwen 2.5 3B | 0.996 | 0.690 | 0.998 | 0.903 |
| Qwen 2.5 7B | 1.000 | 0.778 | 0.998 | 0.961 |

Key observation: "Probes are generally quite strong on all datasets except Logical Deduction" where CoT is most beneficial.

## (5) Steering Methodology and Results

**Methodology**: Contrastive activation addition applied during token generation:
- Formula: "𝐱̃ₜ(ℓ*) = 𝐱ₜ(ℓ*) + α𝐰(ℓ*)"
- Applied at layer with highest probe AUC
- Steering coefficient sweeps: α ∈ {0, ±2, ±4, ..., ±20}
- Two test subsets: examples initially answered correctly as "yes" or "no"

**Results**: Steering with probe direction exceeded orthogonal baselines significantly:
- "Steering in the probe direction consistently dominates steering in an orthogonal direction"
- Larger models (Qwen 7B, Gemma 9B) showed pronounced differences versus orthogonal baseline
- At |α| = 20, answer flip rates exceeded 50% on most datasets except Logical Deduction

**Orthogonal baseline**: Per-example random directions orthogonal to probe direction with matched norm.

## (6) Failure Modes Observed

Framework developed (Table 1) classifying steered incorrect reasoning into:

1. **Confabulation**: "Fabricating false premises to support steered answer"
   - Model introduces one or more false premises early to justify predetermined answer
   - Example: Conflating "telling on people" with "whistleblowing"

2. **Non-entailment**: "Stating correct premises but giving conclusion that does not follow"
   - Model states accurate reasoning but contradicts it in final answer
   - Example: Correctly determining sports car is oldest, then concluding it's newest

3. **Hallucination**: "Incoherent reasoning" with false premises AND non-following conclusions
   - Increases with steering strength
   - Particularly prevalent on Logical Deduction tasks

Document states: "While post-hoc reasoning may be instrumentally useful when correct, these failure modes suggest undesirable behaviors when reasoning from false belief."

## (7) Limitations Section

Primary limitations acknowledged:

1. **Reasoning models**: "Experiments focus on instruction-tuned models rather than reasoning models" explicitly trained via reinforcement learning. Appendix F shows low steering effectiveness on GPT-OSS 20B despite detectable probes.

2. **Superposition uncertainty**: "The technical challenge of superposition—where multiple features are encoded in overlapping directions"

3. **Feature interpretation ambiguity**: Question whether "pre-committed answer" exists as discrete feature or represents task-relevant concepts (plausibility, validity) whose activation determines answer.

4. **Mechanistic interpretation limits**: Probes satisfy necessary conditions (predictive + causal) but authors acknowledge "remaining uncertainty" about whether probe direction constitutes true causal representation.

## (8) Future Work Suggestions

1. Extend experiments to reasoning models to determine post-hoc reasoning prevalence
2. Adapt steering to **mitigate** (not promote) post-hoc reasoning
3. Investigate post-hoc reasoning instances resulting in model failure versus overdependence on memorization
4. Compare probe similarity to Sparse Autoencoder (SAE) features and test SAE-based steering
5. Authors suggest: "comparing the similarity of probes to features from Sparse Autoencoders may shed light on feature interpretation"

## (9) Tool Calling or Structured Outputs

**No mention**: The paper contains zero discussion of tool calling, function calling, or structured output capabilities. Focus remains entirely on activation-level mechanistic interpretability.

## (10) Answer Classes for Probing

**Binary classification exclusively**: All four tasks are binary (yes/no, A/B, plausible/implausible, appropriate/inappropriate). The probe predicts between exactly two answer classes throughout experiments.

---

**Key Finding Summary**: Authors demonstrate that instruction-tuned models linearly encode final answers in pre-CoT activations at >0.9 AUC on most tasks, and these directions causally influence generation through activation steering, suggesting "post-hoc reasoning" where answers are pre-determined before verbalized explanation occurs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75f9fee3-8b27-4f8d-991d-8ce9d0501470",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "ef71ce17-e433-44da-b8f3-20a0407f82e4",
  "sourceToolAssistantUUID": "75f9fee3-8b27-4f8d-991d-8ce9d0501470",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T14:35:47.265Z_

<details><summary>↩ Tool result · `toolu_016QQ3HXfEXC8kmqqiKJwNCH`</summary>

```text
# Analysis of "Internal Representations as Indicators of Hallucinations in Agent Tool Selection"

## 1. EXACT MODELS EVALUATED

Three open-source LLMs were tested:
- **Qwen-7B**: 7-billion parameters with Group Query Attention and RMSNorm
- **GPT-OSS-20B**: 20-billion parameters using standard transformer with multi-head attention
- **Llama-3.1-8B**: 8-billion parameters featuring RoPE embeddings and SwiGLU activation

## 2. METHODOLOGY

The authors developed an unsupervised, single-pass training pipeline:

- **Data generation**: Masked ground-truth tool calls from prompts, asked the LLM to predict them again, then labeled by comparing predicted versus reference calls
- **Feature extraction**: Captured final-layer hidden states at three token positions—function name onset, argument region (mean-pooled), and closing delimiter
- **Classifier training**: Two-layer MLP with 512-unit hidden layer, ReLU activation, sigmoid output
- **Inference**: Operates inline during generation using representations from the identical forward pass that produces tool calls

The approach requires no external validation or multiple sampling passes.

## 3. KEY FINDINGS

Internal transformer representations contain discriminative information for detecting tool-calling errors. The method achieved competitive performance against consistency-based baselines while maintaining real-time inference capabilities. Simpler aggregation methods (mean pooling) proved as effective as sophisticated alternatives, suggesting hallucination signals are distributed throughout generated text rather than concentrated in specific tokens.

## 4. ACCURACY NUMBERS

**Main Results (Table 2):**
- GPT-OSS-20B: 86% accuracy, 86% precision, 53% recall for hallucinations
- Llama-3.1-8B: 73% accuracy, 71% precision, 61% recall
- Qwen-7B: 74% accuracy, 34% precision, 62% recall

**Baseline Comparison (Table 1):**
Against Non Contradiction Probability and Semantic Similarity baselines, the proposed method achieved comparable overall accuracy but superior recall across models, particularly excelling at 86% recall on GPT-OSS-20B versus 74% for baselines.

## 5. WHAT THEY PROBE FOR

The paper formally defines five hallucination categories:

1. **Function Selection Error**: Invoking non-existent functions
2. **Function Appropriateness Error**: Semantically inappropriate tool choice
3. **Parameter Error**: Arguments outside valid domain
4. **Completeness Error**: Missing required parameters
5. **Tool Bypass Error**: Generating output instead of invoking available tools

However, the authors note their current work focuses on "unified binary detection across all error categories" rather than distinguishing between specific error types.

## 6. TOOL NAME VS. PARAMETERS VS. BOTH

The methodology addresses **both dimensions**:

- **Tool name matching**: Compared predicted function names against references
- **Parameter validation**: Checked argument agreement after normalization
- **Unified detection**: The binary classifier learns general incorrectness patterns across both function selection and parameter errors simultaneously

The feature extraction explicitly captures argument information through mean-pooling across the argument token region (𝒯_args), so the classifier considers parameter information alongside function selection.

## 7. MULTI-TURN OR SINGLE-TURN

The evaluation focuses on **single-turn interactions**:

The dataset comprised 2,411 tool-calling instances extracted from multi-domain agent interactions. While the underlying Glaive dataset includes multi-turn conversations, the paper's experiments operate on individual tool calls isolated from their conversational context. No analysis of multi-turn reasoning chains or sequential tool dependencies was performed.

## 8. LIMITATIONS

The authors explicitly acknowledge several constraints:

- **Reference-agreement labeling**: "Determining function equivalence beyond string matching remains difficult without additional context"
- **Dataset standardization**: Label generation depends on proper tool name and parameter canonicalization
- **Feature design**: The three-point feature approach is intentionally simple; future work should explore "field-aware pooling or lightweight attention over argument spans"
- **Cross-model generalization**: Different classifiers required per model architecture; future work should develop unified detectors across model families
- **Evaluation scope**: Experiments limited to mathematical reasoning domains; robustness across diverse tool types unexplored

The authors note that "consistency-based detection [is] less reliable" for tool calling since solutions may be unique rather than repeated across samples.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a07b9b-c0df-4da1-8dd7-4331f43fa025",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "b253cf52-4a31-46cb-b9bc-0df5abf71d51",
  "sourceToolAssistantUUID": "c4a07b9b-c0df-4da1-8dd7-4331f43fa025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T14:35:59.545Z_

<details><summary>↩ Tool result · `toolu_01WyPkasmBhP1KDcRib5stUo`</summary>

```text
# Comprehensive Extraction: "LLM Agents Already Know When to Call Tools"

## (1) Exact Models Tested
- Qwen3-1.7B, Qwen3-4B-Instruct, Qwen3-14B, Qwen3-32B
- Llama-3.1-8B-Instruct, Llama-3.3-70B-Instruct

## (2) Methodology

**Benchmark Design (When2Tool):**
The authors constructed 18 environments (15 single-hop, 3 multi-hop) spanning three tool-necessity categories:
- **Category A** ("Can I compute this?"): Computational scale testing (CalculatorEnv, StatisticsEnv, CountingEnv, MatrixEnv, PrimeEnv, ChainedCalculatorEnv)
- **Category B** ("Do I know this?"): Knowledge boundary assessment (RetrieverEnv, HistoricalYearEnv, GameRuleEnv, HashEnv, DecodingEnv, ChainedRetrieverEnv)
- **Category C** ("Can I execute this reliably?"): Execution tracking (ListManipulationEnv, DateTimeEnv, CodeExecutorEnv, ScheduleEnv, RegexMatchEnv, ChainedCodeExecutorEnv)

Each environment contains three difficulty levels (easy, medium, hard) creating a decision boundary. Total: 1,080 training and 2,700 test tasks.

**Baseline Evaluation:**
1. Prompt-only: Five modes (Force, Default, Necessary, Sparse, No Tool)
2. Reason-then-Act: Same five modes with explicit reasoning about tool necessity first

**Probing Analysis:**
- Extract hidden states at last token position
- Train L2-regularized logistic regression on all-layer features
- Binary labels: tool-unnecessary (y=0) if model succeeds without tools; tool-necessary (y=1) if it fails
- Training on 900 examples, evaluation on 2,250 held-out tasks

**Probe&Prefill Method:**
1. Extract last hidden states from input tokens
2. Apply linear probe with threshold τ to generate probability
3. Prepend steering sentence: either "I can solve this directly without using a tool" or "I need to use a tool for this question"
4. Model continues generation from prefill

## (3) Key Findings

**Finding 1 - Default Tool Overuse:**
Under default settings, models made "2,100–4,400 total tool calls across the 2,250-task single-hop test set," with "even on easy tasks, Qwen3-1.7B makes 864 tool calls out of 750 easy tasks."

**Finding 2 - Indiscriminate Prompt Engineering:**
"Hard tasks pay a disproportionate price" when prompt engineering reduces tool calls. Accuracy cost per saved call (ΔAcc/−ΔTC) reaches −42.4 on hard tasks for Qwen3-4B-Instruct versus −17.3 on easy tasks.

**Finding 3 - Reason-then-Act Limitations:**
Reasoning "only partially helps, but with additional cost." On Llama-3.1-8B, accuracy dropped from "79.5% to 31.2%" with reasoning; on Llama-3.3-70B, from "83.1% to 47.9%."

**Finding 4 - Coarse Control:**
"Prompt engineering cannot precisely control the accuracy–tool-call tradeoff," offering "only a handful of discrete, fixed operating points."

**Finding 5 - Linear Decodability:**
"The probe achieves AUROC 0.89–0.96 across all six tested models," with "tool necessity is consistently encoded in pre-generation hidden states regardless of model family or size."

**Finding 6 - Signal Exists Despite Generation Failure:**
On Llama models where Reason-then-Act "completely breaks tool calling," the probe still achieves "AUROC above 0.9; the information about tool necessity is clearly present in the representation."

## (4) Accuracy Numbers

**Per-Model AUROC (Table 3):**
| Model | AUROC | Accuracy | Easy | Medium | Hard |
|-------|-------|----------|------|--------|------|
| Qwen3-1.7B | 0.894 | 0.847 | 0.864 | 0.831 | 0.904 |
| Qwen3-4B-Inst. | 0.948 | 0.877 | 0.933 | 0.906 | 0.948 |
| Llama-3.1-8B | 0.927 | 0.849 | 0.892 | 0.867 | 0.884 |
| Qwen3-14B | 0.957 | 0.892 | 0.955 | 0.907 | 0.941 |
| Qwen3-32B | 0.952 | 0.885 | 0.951 | 0.903 | 0.939 |
| Llama-3.3-70B | 0.936 | 0.872 | 0.906 | 0.849 | 0.956 |

**Probe&Prefill Performance:**
Reduces "tool calls by 48% with only 1.7% accuracy loss," while "the best baseline at comparable accuracy only reduces 6% of tool calls, or achieves a similar tool call reduction but incurs a 5× higher accuracy loss."

**Accuracy Cost Per Saved Call (Table 4):**
Probe&Prefill achieved "−1.6 easy, −3.4 hard" averaged across six models, substantially better than all baselines (−16.8 to −44.4 on hard tasks).

**Real-World Performance (Search-o1):**
"Probe&Prefill reduces API calls by 20–56% while matching or exceeding baseline accuracy."

## (5) Probe Type: Tool-Use Decision vs. Tool Identity

The authors probe for **tool-use-versus-no-tool-use decisions exclusively**, not tool identity. The binary classification is whether a tool call is necessary at all, independent of which specific tool to invoke. The paper states: "a binary label: we force the model to answer without tool access, and label tasks where it succeeds as tool-unnecessary (y=0) and tasks where it fails as tool-necessary (y=1)."

## (6) Multi-Turn Consideration

**Limited multi-turn analysis.**

The benchmark includes multi-hop tasks ("3 multi-hop environments requiring a chain of 3 dependent tool calls where each step's output is the next step's input"). However, these are still fundamentally single-turn in design—they test sequential tool invocation within one interaction, not conversational back-and-forth.

Appendix C reports multi-hop results showing "Probe&Prefill reduces tool calls by up to 75% on Qwen models while maintaining or improving accuracy," but the paper provides minimal qualitative discussion of how tool-decision dynamics differ across multi-hop sequences.

## (7) Relation to Chain-of-Thought Probing

The paper's probing approach differs fundamentally from chain-of-thought (CoT) work:

- **This work**: Probes **pre-generation hidden states** (before autoregressive decoding) using unambiguous binary labels (task success/failure without tools).
- **CoT tradition**: Typically probes or examines **verbalized reasoning steps** during generation.

The authors explicitly contrast their finding with CoT: reasoning about tool necessity "is largely superficial: it does not improve the model's underlying decision beyond what is already encoded in its hidden states before any reasoning takes place." The probe prediction from pre-generation representations outperforms the model's own verbalized reasoning, suggesting tool-necessity knowledge is encoded *before* the model articulates thoughts.

## (8) Limitations

**Acknowledged Limitations:**

1. **Synthetic environments:** All 18 environments are designed tasks with no API cost and deterministic tool responses. Real-world deployments involve messier tools, variable latency, and failure modes.

2. **Offline evaluation:** "All tool responses are simulated locally and deterministically." Real-world tool calling includes network failures, rate limits, and unpredictable behavior.

3. **Specific tool set:** Environments assume access to particular tools (calculator, retriever, code executor). Generalization to entirely different tool sets is untested.

4. **Probe training data efficiency:** Appendix E.4 addresses data efficiency, but the method requires labeled training data (900 examples per environment) for probe training.

5. **Model scope:** Evaluation limited to Qwen3 and Llama families. Generalization to other architectures (e.g., Claude, GPT-4) is not demonstrated.

6. **No comparison with retrieval-based calibration:** The paper does not compare against confidence-based filtering or uncertainty quantification methods from the broader literature.

7. **Prefill susceptibility:** Hard prefill mode (forcing output format) may be brittle; soft prefill is "partially ignored" by Llama models due to "bad instruction following."

8. **Limited error analysis:** The paper does not deeply analyze failure modes—e.g., when does the probe give incorrect predictions despite high AUROC? What characteristics distinguish these errors?

9. **Inference cost:** While "<1ms overhead" is reported, absolute latency and the cost of maintaining separate probes per environment class are not thoroughly analyzed.

10. **SFT comparison:** Appendix H notes "Full fine-tuning improves accuracy but does not reliably reduce tool calls, and is orders of magnitude more expensive than Probe&Prefill," but SFT results are relegated to appendix with minimal discussion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e8abbd4-9a2b-4044-9c43-691d6a240709",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "5659caa6-ea9b-45dc-ab83-28ce91f8a5e6",
  "sourceToolAssistantUUID": "7e8abbd4-9a2b-4044-9c43-691d6a240709",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T14:36:35.545Z_

<details><summary>↩ Tool result · `toolu_01TKqPbp1sHN1mDHi99brYwg`</summary>

```text
# Comprehensive Analysis: "Tool Calling is Linearly Readable and Steerable in Language Models"

## (1) EXACT MODELS USED

**Instruction-Tuned Models (12 total):**
- Gemma 3: 270M, 1B, 4B, 12B, 27B
- Qwen 3: 0.6B, 1.7B, 4B, 8B, 14B
- Qwen 2.5: 7B
- Llama 3.1: 8B

**Base Models Tested:**
- Gemma 3: 270M, 1B, 4B, 12B, 27B
- Llama 3.1: 8B
- Note: "No public Qwen base variants"

**Reference for Circuit Tracing:** Gemma 3 4B (34 layers, d_model=2560)

---

## (2) WHAT THEY PROBE FOR

The paper examines **tool identity selection only**, specifically:
- Which tool name the model chooses from a fixed menu
- NOT individual argument values or parameters
- The JSON schema structure that follows (not parameter injection)

As stated: "We measure tool identity _selection_ and JSON schema correctness in single-turn 
fixed-menu settings"

---

## (3) PROBE METHODOLOGY

**Primary Method: Mean-Difference Steering**
1. Collect n=2–3 queries per tool, extract residual stream activations at final token position in layer ℓ (ℓ=33 for Gemma 3 4B, ℓ=35 for Qwen 3 4B)
2. Compute mean activation per tool: h̄ᵢ = (1/n)Σⱼhᵢ⁽ʲ⁾
3. Calculate normalized direction: dₐ→ᵦ = (h̄ᵦ - h̄ₐ) / ||h̄ᵦ - h̄ₐ||
4. Scale by α·sepₐ→ᵦ where sepₐ→ᵦ = (h̄ᵦ - h̄ₐ)·dₐ→ᵦ (α selected from {0.5, 0.7, 1.0})
5. Add to residual at layer ℓ during generation: h'ℓ = hℓ + α·sepₐ→ᵦ·dₐ→ᵦ
6. Intervene only at final token position on first forward pass

**Supporting Methods:**
- **PCA Analysis:** Center 15 tool mean vectors, compute SVD, measure cumulative variance explained
- **Activation Patching:** Swap individual attention head/MLP outputs with different-tool queries, measure confidence drop
- **Sparse Autoencoders (SAEs):** Decompose residual stream into features, count tool-specific vs. shared features
- **Cross-Layer Transcoders:** Identify features lighting up at specific layers for tool-calling
- **Cosine Readout:** Measure cosine similarity between query activation and per-tool means
- **Logistic Regression Classifier:** Train on residual stream to predict tool from 14 same-domain airline tools

---

## (4) EXACT ACCURACY/AUC NUMBERS

**Steering Performance (Tool Selection):**

| Setting | Models | Accuracy |
|---------|--------|----------|
| 5-tool switching (synthetic) | Gemma 3 4B, Qwen 3 4B | 100% (60/60 trials) |
| 15-tool exact match | Qwen 3 4B | 93% (28/30) |
| 15-tool exact match | Gemma 3 4B | 80% (24/30) |
| τ-bench airline (14 tools) | Gemma 3 4B | 94% |
| τ-bench airline | Gemma 3 12B | 90% |
| τ-bench airline | Gemma 3 27B | 77% |
| τ-bench retail (16 tools) | Gemma 3 4B | 76% |
| ToolBench cross-domain (10 tools) | Gemma 3 4B | 100% |
| ToolBench cross-domain | Qwen 3 4B | 100% |
| ToolBench cross-domain | Llama 3.1 8B | 90% |
| Ambiguous queries (8 queries) | Gemma 3 4B | 100% |
| Ambiguous queries | Qwen 3 4B | 96% |

**By Model Scale (Sw-15 = 15-tool synthetic):**
- Gemma 3 270M: 27%
- Gemma 3 1B: 43%
- Gemma 3 4B: 96%
- Gemma 3 12B: 97%
- Gemma 3 27B: 100%
- Qwen 3 0.6B: 50%
- Qwen 3 1.7B: 80%
- Qwen 3 4B: 93%
- Qwen 3 8B: 100%
- Llama 3.1 8B: 83%

**Schema Correctness (Arguments Auto-Adapt):**
- Gemma 3 4B: 73% schema-correct rate
- Qwen 3 4B: 27% schema-correct rate
- Llama 3.1 8B: 43% steering / 57% prefilled

**PCA Dimensionality (k₉₀ = dimensions needed for 90% variance):**
- K=15 tools: 9–11 across all models (vs. 14 theoretical max)
- K=50 ToolBench APIs: 17 dimensions (35% compression)
- K=100: 26 dimensions (26% compression)
- K=200: 36 dimensions (18% compression)
- K=500: 57 dimensions (11% compression)

**Within-Topic Airline Probe (14 same-domain tools):**
- Top-1 accuracy: 61–89% across five 4B–14B models
- Top-5 accuracy: 96–100%

**Error Detection (Cosine Gap Analysis):**
- Gemma 3 12B: Smallest-gap quartile has 14% error rate vs. 0% largest-gap quartile
- Gemma 3 27B: Smallest gap = 17% error rate, largest gap = 1% error rate
- **21× concentration ratio** for errors in low-confidence queries

**BFCL v3 Readout Performance:**

| Model | Generation | Cosine Readout | Gap |
|-------|-----------|-----------------|-----|
| Gemma 3 1B base | 2% | 69% | +67pp |
| Gemma 3 4B base | 3% | 75% | +72pp |
| Gemma 3 4B IT | 92% | 74% | -17pp |
| Gemma 3 12B IT | 95% | 66% | -30pp |
| Llama 3.1 8B base | 10% | 82% | +72pp |
| Llama 3.1 8B IT | 90% | 53% | -37pp |

**Activation Patching (Importance by Depth):**
- Peak importance: 89–98% depth for 4B+ models
- Gemma 3 4B: L17 H0 (6.5 points drop), L17 H1 (3.7 points)
- Layer contributions: 17% (early) + 37% (mid) + 45% (late)
- Attention vs. MLP: 80% attention, 20% MLP (Gemma 3 4B); 88% attention, 12% MLP (Qwen 3 4B)
- Top-3 heads vs. top-3 MLPs: 2.7× gap on Gemma, essentially tied on Qwen

**Unembedding Alignment:**
- Instruction-tuned models: +0.26 to +0.29 mean cosine difference
- Base models: ~half the IT alignment
- Parallel component alone: 93–100% steering effectiveness at matched magnitude

**Random Vector Control:**
- 0% switch rate (baseline for demonstrating direction specificity)

---

## (5) TASKS/BENCHMARKS

1. **Synthetic Tools (Controlled):** 5–15 fictional tools (get_weather, search, translate, schedule, calculate, etc.)

2. **τ-bench (Yao et al., 2024):**
   - Airline domain: 14 tools (book reservation, cancel, update flights, search direct flights, transfer to agent, etc.)
   - Retail domain: 16 tools
   - Realistic multi-turn agent benchmark

3. **ToolBench (Qin et al., 2024):**
   - Up to 2,000 real APIs from 49 domains
   - Finance, health, sports, etc.
   - 6 domains tested with 10 tools each
   - Cross-domain evaluation

4. **BFCL v3 (Yan et al., 2024):**
   - 1,053 real-world function-calling queries
   - Leave-one-out evaluation (n=500 per model)
   - Real user queries

---

## (6) MULTI-TURN vs. SINGLE-TURN EVALUATION

**Single-Turn (Primary Focus):**
- All main results on single-turn, fixed-menu prompts
- Consistent 77–100% accuracy across 12 instruction-tuned models
- This is the strongest domain

**Multi-Turn (Mixed Results):**
- Synthetic two-turn setup with fixed menu at turn 2: 100% at 4B+
- Real agent benchmark (τ-bench airline): "mixed picture" and "model-dependent"
- Matched-vs-baseline delta ranges from **-30 to +10 percentage points** across five 4B–14B models
- Gemma 3 12B L47 drops 30 points below baseline
- Qwen 3 8B and 14B lose 20 and 10 points respectively
- Authors state: "no consistent direction" and note 95% confidence intervals overlap with zero

**Key Limitation:** "Multi-turn behaviour is mixed... steering signal being reliable in single-turn, fixed-menu settings but competing for residual-stream capacity, or interacting badly with accumulated tool outputs."

---

## (7) STRUCTURED JSON OUTPUT CONSIDERATION

**Direct Findings:**
- "JSON arguments that follow autoregressively match the new tool's schema"
- Table 5 shows schema adaptation: steering weather→search changes location→query parameter
- Schema correctness rates: 73% (Gemma 3 4B), 27% (Qwen), 43% (Llama)

**Mechanism for Schema Adaptation:**
- NOT encoded in the steering vector itself
- Schema follows through **ordinary autoregressive generation** once tool name is committed
- Prefilled tool name experiments (Table 6) show identical schema correctness rates as steering

**Key Discovery:** "Flipping the name is enough" – once the tool is selected, JSON structure follows from training distribution

**Argument Content NOT Steerable:**
- Steering fails on argument values: "redirecting 'Tokyo' to 'Paris' while keeping the same tool gives 0/30"
- Format steering (JSON vs. plain text) also fails (0/10)
- Authors note: "Picking a tool is choosing from a short, fixed list, so a few directions suffice. Argument values are pulled from the query on the fly, not from a fixed menu."

**Hallucination Risk:** "Steered outputs match the target schema but sometimes fabricate arguments (like 'Pizza Palace' for a restaurant name)"

---

## (8) LIMITATIONS

**Scale Dependency:**
- Sub-1B models lack exploitable structure
- Linear structure absent at 270M parameters
- Starts emerging at 1B, sharpens with instruction tuning
- "representation-based monitoring only works at 1B and above"

**Tool Similarity:**
- Fails on near-synonymous tools (0% on 10 similar Sports APIs)
- "If the model cannot distinguish two tools, neither can we"

**Argument Steering:**
- Cannot redirect argument values or formats
- Only tool _selection_ is linear, not argument _content_

**Schema Fabrication:**
- Models may produce non-existent argument values
- "A real API server would likely reject such inputs"
- Evaluation measures schema structure, not actual task completion

**Multi-Turn Degradation:**
- Consistent positive effects only in single-turn, fixed-menu settings
- "Multi-turn agentic transfer is more fragile"
- "Steering should be viewed as an analytical and routing tool, not as a standalone method for end-to-end API execution"

**Prompt Length Constraints:**
- At K=750 tools with descriptions (~16K tokens), representations blur (k₉₀ drops from 57 to 27)
- Without descriptions, handles K=1,500 tools
- Bottleneck is total prompt length, not tool count
- Smaller models (Gemma 3 4B) degrade faster with longer prompts

**Architecture Scope:**
- Only tested on dense transformers (Gemma 3, Qwen 3/2.5, Llama 3.1)
- "Do not know if this extends to mixture-of-experts or state-space models"

**Cross-Model Transfer:**
- "Cosine alignment does not transfer across model families"
- Gemma vectors fail on Qwen (0% cross-family steering)

**Geometric Interpretation Caveats:**
- PCA dimensionality at K=15 and K=200 "does not survive matched-prompt controls"
- Non-tool topic queries with same prompt prefix compress equally well or better
- Authors revise claim: "tool identity has a linear, intervenable representation" not "uniquely small subspace"
- Base model cosine geometry extremely tight (cos ~0.998, std ~0.001), works through "argmax over very small differences rather than over a geometrically separable subspace"

---

## (9) HOW THIS DIFFERS FROM PROBING FOR TEXT ANSWERS

**Key Differences:**

| Aspect | This Work | Typical Text Probing |
|--------|-----------|---------------------|
| **What's Probed** | Discrete tool selection from fixed menu (K tools) | Open-ended text generation/classification |
| **Output Space** | Combinatorially small (K choices + JSON schema) | Combinatorially large (unbounded tokens) |
| **Interventional Target** | Single linear direction sufficient | Usually requires multiple directions or training |
| **Schema Constraint** | Structured output with known parameters | Free-form text without constraints |
| **Causal Mechanism** | Route to output layer token (unembedding alignment) | Complex generation pathway |
| **Steering Scope** | Changes entire argument payload schema automatically | Text content requires separate steering |

**Specific Contrast:** While text-answer probing examines sentiment, truthfulness, or refusal (binary/continuous concepts), this work exploits the **discrete, finite nature of tool calling** where the output must match one of K predefined names and follow one of K schemas. The linear structure emerges because the final layer can afford to keep discrete options cleanly separated.

---

## (10) ALL KEY FINDINGS

### Finding 1: Linear Readability
"Tool identity is linearly readable and steerable inside the model" across 12 instruction-tuned models spanning three families (Gemma 3, Qwen 3/2.5, Llama 3.1) and 270M–27B parameters.

### Finding 2: Steering Effectiveness
Adding mean-difference vector between tool means switches tool selection at:
- **77–100% accuracy** on name-only single-turn prompts (12 IT models)
- **93–100%** at 4B+ models
- Descriptions offer "at most a small boost" for 4B+ (83–100% with descriptions vs. 93–100% without)

### Finding 3: Dimensionality Compression
- K=15 tools fit in ~10 principal components (k₉₀=9–11)
- K=200 real APIs need only 36 directions (18% of theoretical max)
- BUT: matched-prompt controls show non-tool queries compress equally well, so "tool-specific subspace" claim doesn't survive that test

### Finding 4: Schema Auto-Adaptation
"Flipping the name is enough" – JSON arguments automatically restructure to match target tool's schema through autoregressive generation, not steering-vector encoding.

### Finding 5: Three-Stage Circuit
Activation patching reveals:
- **Stage 1 (early layers L0–3):** 38 tool-specific features light up
- **Stage 2 (mid layers L16–30):** Attention heads lock onto tool-name and entity tokens
- **Stage 3 (late layers L30–33):** JSON formatting features (generic, not tool-specific)

### Finding 6: Component Importance
- Peak importance at 89–98% depth for 4B+ models
- Gemma 3 4B: Two specific heads (L17 H0 and H1) carry more than all others combined
- Attention dominates on Gemma (80%), roughly tied with MLPs on Qwen (88% vs. 12%)

### Finding 7: Unembedding Alignment
Steering vector's parallel component to target tool's first-token unembedding row is sufficient:
- "Unit vector along it at matched magnitude already reaches 93–100%"
- Instruction-tuned models show 2× higher alignment than base models (+0.26 to +0.29 vs. ~0.13)
- Orthogonal remainder leaves choice "almost untouched"

### Finding 8: Within-Topic Discrimination
Despite all 14 τ-bench airline tools sharing airline domain, logistic regression on residual stream reaches:
- **Top-1: 61–89%** across five 4B–14B models
- **Top-5: 96–100%**
- Rules out "we're just moving along a topic axis" interpretation

### Finding 9: Pretraining vs. Instruction Tuning
Base models encodethe right tool internally without outputting it:
- Gemma 3 4B base: 3% generation, but 75% cosine readout (+72pp gap)
- Llama 3.1 8B base: 10% generation, 82% readout (+72pp gap)
- Gap of 56–72 percentage points suggests "pretraining forms the representation and instruction tuning later wires it to the output"

### Finding 10: Feature Sharpening with Scale
SAE analysis shows:
- **270M-IT:** 0 tool-specific features at early layers, only 16 at L15
- **1B-IT:** Specific-to-shared ratio jumps to 10.4 at L17 (125 features, 65% depth)
- **12B-IT:** Sharpening spans full network (0.1 → 1.6 → 2.3 → 4.1)
- "Instruction tuning organizes scattered features into functional pathways"

### Finding 11: Error Detection via Cosine Gap
When top-2 tools have smallest internal gap:
- Gemma 3 12B: **14–21× more wrong calls** than largest-gap queries
- Quartile-based: 14% error (smallest gap) vs. 0% (largest gap)
- Practical use case: "flag likely errors before they happen"

### Finding 12: Emergence Across Scales
- 270M: No steering (27%, chance level)
- 1B: Partial structure (43% on 15 tools, 100% on 5 tools)
- 4B+: Robust (≥83% on 15 tools, up to 100%)

### Finding 13: Phase Transition in Steering Strength
Sharp transition at α≈0.6–0.7:
- Below: steering does nothing
- Above: "accuracy jumps to 95–100% and stays there even at α=3.0"

### Finding 14: Robustness to Distractors
- Adding distractor tools up to K=150 doesn't reduce accuracy on core 5 tools (~100%)
- Steering among randomly sampled tools from all K: every 4B+ model stays above 90%

### Finding 15: Cross-Domain Generalization
- Base models struggle on cross-domain ToolBench (30% Gemma base, 50% Llama base)
- Instruction-tuned models reach 100% on most cross-domain settings
- Suggests "instruction tuning is needed for cross-domain generalization"

### Finding 16: Ambiguous Query Handling
On 8 deliberately ambiguous queries like "Help me plan my trip to Paris":
- Gemma 3 4B: 100% can redirect to every plausible tool
- Qwen 3 4B: 96%

### Finding 17: No Format or Argument Steering
- Format steering (JSON vs. plain text): 0/10
- Argument value redirection: 0/30
- Cross-family transfer: 0% (Gemma vectors on Qwen fail)

### Finding 18: Tool Name Tokenization Bottleneck
Four tools sharing get\_ prefix (get_weather, get_stock, get_news, get_directions) are hardest to distinguish:
- Prefix-match: 73–87%
- Exact-match: Lower due to follow-up token ambiguity
- "Tokenizer granularity" is the constraint, not steering mechanism

### Finding 19: Scaling with Real APIs
ToolBench scaling shows:
- K=50: k₉₀=17 (43 dimensions vs. random 35% compression)
- K=200: k₉₀=36 (Δ from non-tool matched-prompt ranges -73 to +51)
- Growth slower than random but not strictly monotonic due to domain clustering

### Finding 20: Practical Limitations on Prompt Length
- K=750 tools with descriptions (~16K tokens): k₉₀ collapses (57→27 on Gemma 3 4B)
- K=1,500 without descriptions: stable (k₉₀ grows to 116 with no collapse, prompt ~8K tokens)
- Larger models (12B/27B) tolerate at least K=1,000 before degradation

---

## SUMMARY TABLE: Core Results

| Dimension | Finding |
|-----------|---------|
| **Models Tested** | 12 IT + 6 base models (270M–27B) across 3 families |
| **What Probed** | Tool selection only (name), not arguments |
| **Methodology** | Mean-difference steering + activation patching + SAEs + cosine readout |
| **Peak Accuracy** | 93–100% (4B+ models, 15-tool fixed menu) |
| **Dimensionality** | K=15 fits in ~10 PCA components; K=200 needs 36 directions |
| **Circuit Localization** | 3-stage pathway (early features → mid attention heads → late formatting) |
| **Strongest Evidence** | Steering works, activation patching identifies causality, within-topic probe rules out topic-only reading |
| **Weakest Claim** | PCA "tool-specific subspace" – fails matched-prompt controls |
| **Multi-Turn** | -30 to +10pp vs. baseline; unreliable |
| **Schema Adaptation** | Automatic via autoregression (NOT steering vector), 27–73% correctness |
| **Key Limitation** | Single-turn fixed-menu only; sub-1B fails; argument values not steerable; hallucination risk |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba1e1615-d008-4617-a0bd-6984de14cc4f",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "4dfed172-88f3-4abf-85a4-5d1ff0e2a21b",
  "sourceToolAssistantUUID": "ba1e1615-d008-4617-a0bd-6984de14cc4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T14:36:38.562Z_

Now let me fetch more details on a couple more related papers and search for additional related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dfed172-88f3-4abf-85a4-5d1ff0e2a21b",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6XZZ2iMYZgJbdfKTor",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d59dc5f-b6b6-40aa-9d3b-4f84e3870a9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9teSNMbM5cQ4icyq4DeVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3881,
      "cache_creation_input_tokens": 9205,
      "cache_read_input_tokens": 13565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T14:36:40.419Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GP972QvCzkmyN7mtu1Vi4E`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.24362",
  "prompt": "Extract key details from \"Knowing Before Saying: LLM Representations Encode Information About Chain-of-Thought Success Before Completion\" - what models, what tasks, what probe accuracy, how does it relate to pre-CoT probing?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d59dc5f-b6b6-40aa-9d3b-4f84e3870a9e",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6XZZ2iMYZgJbdfKTor",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fc62b85-5856-459c-a32c-fe12e7365403",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9teSNMbM5cQ4icyq4DeVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3881,
      "cache_creation_input_tokens": 9205,
      "cache_read_input_tokens": 13565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T14:36:41.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BPZa8fg83rktiSCE9kpwFw`</summary>

```json
{
  "query": "\"tool calling\" \"linear probe\" OR \"probing\" hidden states LLM \"function calling\" activation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fc62b85-5856-459c-a32c-fe12e7365403",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6XZZ2iMYZgJbdfKTor",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2759f21-dae5-4173-b65c-14c39a35d85a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9teSNMbM5cQ4icyq4DeVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3881,
      "cache_creation_input_tokens": 9205,
      "cache_read_input_tokens": 13565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9205,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T14:36:42.009Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X6QqMeXXTd4kbgHtY258UL`</summary>

```json
{
  "query": "multi-turn agent tool selection probing hidden representations LLM conversation context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2759f21-dae5-4173-b65c-14c39a35d85a",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6XZZ2iMYZgJbdfKTor",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8389c505-3627-4e5e-9c30-2c6ba64ab526",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9teSNMbM5cQ4icyq4DeVE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3881,
      "cache_creation_input_tokens": 9205,
      "cache_read_input_tokens": 13565,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9205
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3881,
          "output_tokens": 268,
          "cache_read_input_tokens": 13565,
          "cache_creation_input_tokens": 9205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9205,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T14:36:44.794Z_

<details><summary>↩ Tool result · `toolu_01GP972QvCzkmyN7mtu1Vi4E`</summary>

```text
# "Knowing Before Saying" - Key Details

## Models & Tasks
The paper doesn't specify particular LLM models in the abstract. It examines zero-shot Chain-of-Thought (CoT) reasoning across unspecified tasks, comparing an LLM-based probing classifier against a BERT baseline.

## Probe Accuracy
The abstract indicates the probing classifier "performs well even before a single token is generated," but exact accuracy metrics aren't provided in the excerpt.

## Pre-CoT Probing Insight
The research's central finding involves early prediction capability: "crucial information about the reasoning process is already present in the initial steps representations." This suggests the model encodes success signals before generating reasoning tokens.

## Practical Implication
The authors found that "truncating CoT reasoning still improves performance over not using CoT at all," indicating early stopping is viable when guided by their classifier—though performance gaps persist compared to full reasoning chains.

The work suggests LLMs may encode reasoning success signals internally before externalization, with potential applications in optimizing CoT efficiency through supervised or reinforcement learning approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fc62b85-5856-459c-a32c-fe12e7365403",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "59858346-ccec-449e-ae41-dc8f94c57587",
  "sourceToolAssistantUUID": "1fc62b85-5856-459c-a32c-fe12e7365403",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T14:36:48.576Z_

<details><summary>↩ Tool result · `toolu_01X6QqMeXXTd4kbgHtY258UL`</summary>

```text
Web search results for query: "multi-turn agent tool selection probing hidden representations LLM conversation context"

Links: [{"title":"Multi-Turn Tool-Calling LLMs","url":"https://www.emergentmind.com/topics/multi-turn-tool-calling-large-language-models-llms"},{"title":"How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations","url":"https://arxiv.org/pdf/2508.05625"},{"title":"Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey","url":"https://arxiv.org/html/2503.22458v1"},{"title":"Multi-Turn Tool-Calling LLMs: Advances & Challenges","url":"https://www.emergentmind.com/topics/multi-turn-tool-calling-llms"},{"title":"MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations","url":"https://arxiv.org/pdf/2507.21428"},{"title":"Evaluating LLM-based Agents for Multi-turn Conversations: A Survey | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3793671"}]

Based on the search results, here's what I found about multi-turn agent tool selection and probing hidden representations in LLM conversation contexts:

## Multi-Turn Tool-Calling Agents

Multi-turn tool-calling LLMs are agentic architectures that alternate between generating text and invoking external tools, enabling adaptive multi-step dialogues. Action and tool-use components are fundamental to LLM-based multi-turn conversation agents, as they dynamically identify and execute appropriate API calls while maintaining context through memory of previous interactions.

## Tool Selection and State Management

At every turn, the model can select a tool and generate its arguments or terminate with the answer, with state transitions including appending tool feedback to the context and updating the internal representation.

## Probing Hidden Representations

The search results include research on using linear probes to analyze LLM representations. Linear probes are applied to provide token-level insights across various abstract phenomena in LLMs, and by using probes, researchers can efficiently analyze multi-turn dialogue at finer granularities such as at the token and turn levels.

## Context and Memory Management

Memory in LLM-based agents operates across a temporal hierarchy: from immediate awareness (turn memory) that anchors the agent within a single exchange, to sustained context (conversational memory) that weaves coherence across extended dialogues.

This research area combines agent design, tool orchestration, and interpretability techniques to understand how LLMs make tool selection decisions and maintain conversational context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8389c505-3627-4e5e-9c30-2c6ba64ab526",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "f2dc5393-71cf-4873-8370-c2d27b77a655",
  "sourceToolAssistantUUID": "8389c505-3627-4e5e-9c30-2c6ba64ab526",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T14:36:48.615Z_

<details><summary>↩ Tool result · `toolu_01BPZa8fg83rktiSCE9kpwFw`</summary>

```text
Web search results for query: ""tool calling" "linear probe" OR "probing" hidden states LLM "function calling" activation 2025 2026"

Links: [{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v1"},{"title":"Probing LLM Hidden States","url":"https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"},{"title":"GitHub - jammastergirish/LLMProbe · GitHub","url":"https://github.com/jammastergirish/LLMProbe"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2503.15299"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"},{"title":"LUMIA: Linear probing for Unimodal and MultiModal Membership Inference   Attacks leveraging internal LLM states","url":"https://arxiv.org/pdf/2411.19876"}]

Based on the search results, here's what I found on the intersection of tool calling, linear probes, and LLM hidden states from 2025-2026:

## Recent Research on Probing Tool-Use Decisions

Recent work extends probing to agentic tool-use decisions, showing that models "mostly know" when they need tools but fail to act on it. This is demonstrated through linear probes, which are classifiers trained on intermediate representations to test whether a target concept is linearly recoverable from them.

## Internal Monitoring for Tool Calling

An internal monitoring framework reads model activations immediately before each action and estimates whether the model is internally preparing to delegate to a tool and whether that action is likely to be low, medium, or high risk. In tool-selection settings, internal representations have been shown to distinguish correct from hallucinated tool calls, with calibration playing an important role when such probes are intended for deployment.

## Key Finding on Hidden State Signals

Hidden states can contain useful same-pass signals for tool-call errors that are not visible from outputs alone. Additionally, activation-probing results show that internal representations can predict downstream behavior before it is externally visible.

These 2025-2026 studies demonstrate that linear probing of LLM hidden states is an effective approach for understanding and improving tool-calling behavior in agentic AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2759f21-dae5-4173-b65c-14c39a35d85a",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "8b0ec9ff-9d80-49e9-b311-7003ac48c4fd",
  "sourceToolAssistantUUID": "c2759f21-dae5-4173-b65c-14c39a35d85a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-19T14:36:52.070Z_

Let me fetch one more critical paper and do a final targeted search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b0ec9ff-9d80-49e9-b311-7003ac48c4fd",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6YXS4XG1ceo98JeTxA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16b56a55-9e16-4ce6-adbf-f290e52b4cdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS96ELGbdaX3owJ492zL1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 14319,
      "cache_read_input_tokens": 13565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14319,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T14:36:53.950Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JXJt2Zsu92Aja7h3Je5LQB`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06890",
  "prompt": "Extract ALL details from \"Beyond the Black Box: Interpretability of Agentic AI Tool Use\": (1) models, (2) methodology, (3) what they probe for, (4) key findings on tool-use interpretability, (5) whether they address multi-turn settings, (6) how tool-use probing differs from answer probing, (7) accuracy numbers. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b56a55-9e16-4ce6-adbf-f290e52b4cdd",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6YXS4XG1ceo98JeTxA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c08b97dd-9e86-46be-9933-dd3caa9084b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS96ELGbdaX3owJ492zL1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 14319,
      "cache_read_input_tokens": 13565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14319,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T14:36:54.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CowQBtz1XKB6UUYhVYJHHP`</summary>

```json
{
  "query": "probing tool parameters arguments hidden states LLM structured output JSON schema activation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08b97dd-9e86-46be-9933-dd3caa9084b1",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6YXS4XG1ceo98JeTxA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc21e354-fe88-42dc-b5a2-b45988668fe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS96ELGbdaX3owJ492zL1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 14319,
      "cache_read_input_tokens": 13565,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 693,
          "output_tokens": 233,
          "cache_read_input_tokens": 13565,
          "cache_creation_input_tokens": 14319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14319,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T14:37:01.537Z_

<details><summary>↩ Tool result · `toolu_01CowQBtz1XKB6UUYhVYJHHP`</summary>

```text
Web search results for query: "probing tool parameters arguments hidden states LLM structured output JSON schema activation"

Links: [{"title":"Stop Blaming the LLM: JSON Schema Is the Cheapest Fix for Flaky AI Agents | by Micheal Lanham | Medium","url":"https://medium.com/@Micheal-Lanham/stop-blaming-the-llm-json-schema-is-the-cheapest-fix-for-flaky-ai-agents-00ebcecefff8"},{"title":"How do Structured Outputs Work? | Cohere","url":"https://docs.cohere.com/docs/structured-outputs"},{"title":"Structured outputs | LLM Inference Handbook","url":"https://bentoml.com/llm/getting-started/tool-integration/structured-outputs"},{"title":"GitHub - otriscon/llm-structured-output · GitHub","url":"https://github.com/otriscon/llm-structured-output"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"},{"title":"How Good Are LLMs at Processing Tool Outputs?","url":"https://arxiv.org/pdf/2510.15955"}]

Based on the search results, here are the key findings related to your query:

## JSON Schema and Structured Output for Tool Parameters

A JSON Schema is a way to describe the structure of the JSON object you want the LLM to generate, and it forces the LLM to stick to this schema, giving you greater control over the output. JSON Schema checks structure, types, and required fields.

## Tool Arguments and Activation

The approach involves enforcing structured outputs validated against a JSON Schema for every tool. In production systems with strict schema enforcement, teams consistently report that tool-call failures drop to near zero because the LLM either produces a valid call or gets immediately corrected.

## Hidden States and Probing

Internal representations (residual stream, attention outputs, and MLP outputs) can be extracted from any combination of layers from a frozen transformer as it processes training examples, and these representations can be used to train lightweight probe networks that learn to map internal states to calibrated predictions.

## Tool Response Processing

Tool response processing can be formulated as question-answering on structured tool responses, specifically in the JSON response format which is popular among real-world tools. Including a schema of the structured data in the prompt improves performance (up to +12%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc21e354-fe88-42dc-b5a2-b45988668fe8",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "d3a15b27-f8a5-4f17-8db4-c4b3aef93191",
  "sourceToolAssistantUUID": "fc21e354-fe88-42dc-b5a2-b45988668fe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T14:37:07.413Z_

<details><summary>↩ Tool result · `toolu_01JXJt2Zsu92Aja7h3Je5LQB`</summary>

```text
# Beyond the Black Box: Tool-Use Interpretability in AI Agents

## (1) Models Studied
The research examines two instruction-tuned open-weight models:
- **GPT-OSS 20B**: evaluated with six post-residual layers
- **Gemma 3 27B**: evaluated with four post-block residual layers

Both undergo identical decision-point pipeline processing for comparative analysis.

## (2) Methodology
The framework combines Sparse Autoencoders (SAEs) with linear probes:

- **Data preparation**: Multi-step trajectories converted to per-decision-point rows using NVIDIA Nemotron function-calling dataset
- **Internal state extraction**: Mean-pooled hidden states (last 32 pre-action tokens) encoded via SAE to sparse features
- **Probe training**: Two independent linear classifiers operate on concatenated SAE features across layers
- **Feature analysis**: Top features identified, ranked by predictive importance, then tested through representational ablation (zeroing latents to confirm necessity)

The system reads model activations *before* tool actions execute, preserving a faithful pre-action perspective.

## (3) What They Probe For

**Tool-Need Probe (Probe 1)**: Binary classification—whether external tool invocation is required at current decision step

**Tool-Risk Probe (Probe 2)**: Ternary classification once tool use is warranted:
- Low risk: read-only retrieval/lookup
- Medium risk: bounded write/creation operations
- High risk: authentication, outbound communication, dangerous execution

## (4) Key Findings on Tool-Use Interpretability

**Held-out Nemotron performance:**
- Tool-Need accuracy: 75.3% (GPT-OSS), 71.4% (Gemma)
- Tool-Risk accuracy: 90.3% (GPT-OSS), 88.5% (Gemma) on tool-call steps

**Localization patterns:**
- Strongest signals concentrate in late transformer layers (GPT-OSS layers 19, 23; Gemma layers 31, 40, 53)
- Top features involve numerical data, formal language (Tool-Need), and authentication/credential concepts (Tool-Risk)

**Ablation validation:** Suppressing top-ranked feature sets substantially reduced probe confidence or flipped predictions, confirming causal importance rather than mere correlation.

## (5) Multi-Turn Settings

Yes, extensively addressed. The framework applies "to repeated decision points" across trajectories. An illustrative financial trace (trajectory_id 3344) demonstrates how probe signals evolve across 15+ sequential steps within a single interaction, showing Tool-Need probability rising on retrieval steps and falling on follow-up turns requiring no new delegation.

The paper emphasizes that long-horizon agents particularly benefit: "an early tool mistake can alter the rest of the trajectory, increase token consumption, and create downstream safety and security risk."

## (6) Tool-Use Probing vs. Answer Probing

This work differs fundamentally from output-only evaluation:

> "Prompts reveal correlations, and evaluations score outputs only after the model has already acted"

Internal monitoring provides visibility *before* execution. The method surfaces whether models internally recognized delegation necessity before taking action, distinguishing:
- Correct tool use
- Missed tool calls (tool needed but not invoked)
- Unnecessary calls (no tool needed but invoked anyway)
- High-risk actions

This captures failure modes invisible to behavioral benchmarks alone.

## (7) Accuracy Numbers

**Nemotron held-out test (primary):**
- Tool-Need F1: 0.75 (GPT-OSS), 0.71 (Gemma)
- Tool-Risk macro-F1: 0.64 (GPT-OSS), 0.62 (Gemma)

**Replay performance (GPT-OSS):**
- Step accuracy: 78.6%
- Fully correct episodes: 62.5% (475/760)
- Probe catch rate for missed tools: ~75.5%

**BFCL zero-shot transfer:**
- Expected-internal agreement: 83.6% (GPT-OSS), 87.6% (Gemma)
- Episode success: 49.2% (GPT-OSS), 50.0% (Gemma)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c08b97dd-9e86-46be-9933-dd3caa9084b1",
  "isSidechain": true,
  "promptId": "cc688073-7f21-461f-81a8-bdd0424cb9d7",
  "agentId": "a4f75ce9cd4490ba2",
  "type": "user",
  "uuid": "589c18df-afd5-480a-91c5-e1ce825a7512",
  "sourceToolAssistantUUID": "c08b97dd-9e86-46be-9933-dd3caa9084b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T14:38:28.580Z_

I now have a comprehensive picture. Here is the detailed report.

---

## Detailed Research Report: "Decoding Answers Before CoT" and Related Work on Tool-Call Probing

### 1. What "Decoding Answers Before Chain-of-Thought" (arXiv 2603.01437) Shows

**Authors:** Kyle Cox, Darius Kianersi, Adria Garriga-Alonso (March 2, 2026)

**Core claim:** Instruction-tuned LLMs encode their final answer in residual-stream activations *before* generating any chain-of-thought tokens. CoT is post-hoc rationalization, not genuine deliberation.

**Models:** Gemma 2 (2B-it, 9B-it), Qwen 2.5 (1.5B-it, 3B-it, 7B-it). Limited appendix experiments on GPT-OSS 20B (a reasoning model).

**Tasks:** Four **binary classification** tasks only -- Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry. All formatted as A/B choices with 500 train / 500 test examples and 4 few-shot CoT demonstrations.

**Probe methodology:** Difference-of-means linear probe on residual-stream activations at the **last pre-CoT token** (the colon in "Let's think step by step:"). The probe direction is simply w = mean_yes - mean_no. Scoring is cosine similarity.

**Exact AUC numbers by task:**
- Anachronisms: 0.988 to 1.000 across all models
- Social Chemistry: 0.993 to 0.998
- Sports Understanding: 0.808 to 0.961
- Logical Deduction: 0.688 to 0.878 (the weakest -- notably the task where CoT helps most)

**Steering:** Contrastive activation addition at the best-probe layer flips answers in >50% of cases at alpha=20, significantly exceeding orthogonal baselines. This establishes *causality*, not just correlation.

**Failure modes when steering induces wrong answers:**
1. **Non-entailment:** Correct premises, unsupported conclusion
2. **Confabulation:** Fabricated false premises to justify the steered answer

**Key limitations the paper acknowledges:**
- Only binary classification tasks
- Only instruction-tuned models (not reasoning models trained via RL; their GPT-OSS 20B appendix showed probes work but steering fails)
- Superposition uncertainty -- the "answer direction" might actually encode task-relevant features (plausibility, validity) rather than a discrete committed answer
- No mention whatsoever of tool calling, structured outputs, function calling, or JSON

---

### 2. Critical Finding: Tool-Call Probing Has ALREADY Been Done

Your search reveals that the landscape has shifted dramatically in the last few weeks. Three papers from May 2026 directly probe for tool-call decisions in hidden states:

#### Paper A: "Tool Calling is Linearly Readable and Steerable in Language Models" (arXiv 2605.07990, ~2 weeks old)

This is the single most important paper for your differentiation argument -- and it is **bad news**, because it does almost exactly what your proposal describes. Key details:

- **12 instruction-tuned models** across Gemma 3, Qwen 3/2.5, Llama 3.1 (270M to 27B)
- Probes **tool identity** (which specific tool, not just whether to use a tool) from pre-generation residual stream activations
- Mean-difference steering switches tool selection at **93-100% accuracy for 4B+ models** in single-turn, fixed-menu settings
- Tested on realistic benchmarks: tau-bench (14 airline tools, 16 retail tools), ToolBench (up to 2000 real APIs), BFCL v3
- Discovered a **three-stage circuit**: early tool-specific features -> mid-layer attention heads -> late JSON formatting features
- Key finding: "Flipping the name is enough" -- once tool identity is steered, JSON arguments auto-adapt to the target schema via autoregressive generation
- **However:** argument *values* are NOT steerable (0/30 on redirecting e.g. "Tokyo" to "Paris"), and format steering (JSON vs plain text) also fails (0/10)
- **Critical limitation: multi-turn results are mixed**. In real agentic tau-bench settings, steering shows -30 to +10 percentage points vs. baseline with "no consistent direction." The authors state multi-turn is "fragile" and recommend steering as "an analytical and routing tool, not a standalone method for end-to-end API execution."

#### Paper B: "LLM Agents Already Know When to Call Tools -- Even Without Reasoning" (arXiv 2605.09252, ~1 week old)

- Probes the **binary tool-necessity decision** (use tool vs. don't) rather than tool identity
- **AUROC 0.89-0.96** across Qwen 3 (1.7B-32B) and Llama (8B, 70B) on 18 synthetic environments
- Shows that explicit reasoning about tool necessity is "largely superficial" -- it doesn't improve beyond what's already encoded in pre-generation hidden states
- Their Probe&Prefill method reduces tool calls by 48% with only 1.7% accuracy loss
- Limited to mostly single-turn; multi-hop tasks tested but with minimal analysis of sequential dynamics

#### Paper C: "Beyond the Black Box: Interpretability of Agentic AI Tool Use" (arXiv 2605.06890)

- GPT-OSS 20B and Gemma 3 27B
- Uses SAEs + linear probes on pre-action hidden states
- Probes for **tool-need (binary)** and **tool-risk (ternary: low/medium/high)**
- Tool-Need accuracy: 71-75%; Tool-Risk accuracy: 88-90%
- **Explicitly addresses multi-turn trajectories** with 15+ step financial traces
- Shows probe signals evolve across sequential steps within a single interaction

#### Paper D: "Internal Representations as Indicators of Hallucinations in Agent Tool Selection" (arXiv 2601.05214, January 2026)

- Qwen-7B, GPT-OSS-20B, Llama-3.1-8B
- Probes hidden states to detect **tool-calling hallucinations** (wrong tool name, wrong parameters, missing parameters, tool bypass)
- Extracts features at function name onset + argument region + closing delimiter
- GPT-OSS-20B: 86% accuracy detecting hallucinated tool calls
- Single-turn only; no multi-turn analysis

---

### 3. What Gaps Remain for Your Proposal

Given this landscape, here is an honest assessment of what your proposal could still contribute, and where it is now pre-empted:

**Already covered by existing work:**
- Linear probes on open-source model hidden states for tool identity before reasoning: Done by 2605.07990 with 12 models, multiple benchmarks, and both probing + steering + circuit analysis
- Binary tool-use-vs-no-tool-use probing: Done by 2605.09252 with 0.89-0.96 AUROC
- Pre-CoT answer probing for QA: Done by 2603.01437
- Tool-call hallucination detection from hidden states: Done by 2601.05214

**Gaps that remain genuinely open:**

1. **Multi-turn agentic settings are explicitly flagged as unsolved.** Paper 2605.07990 found steering "fragile" in multi-turn and reported -30 to +10pp with "no consistent direction." Paper 2605.06890 addresses multi-turn trajectories but only for tool-need/tool-risk classification, not tool identity. Nobody has systematically studied how **accumulated conversation context** (prior tool results, error states, user corrections) affects tool-identity encoding in hidden states across turns.

2. **Parameter probing is completely open.** 2605.07990 explicitly showed tool NAME is linearly steerable but argument VALUES are not (0/30). Nobody has probed whether parameter choices (e.g., which database to query, what filter to apply) are encoded pre-generation. This is a fundamentally harder problem because parameters are drawn from the query context, not a fixed menu.

3. **Compositional tool-call structure** -- the joint encoding of (tool_name, param1, param2, ...) as a structured object rather than as independent dimensions -- is unstudied. Existing work treats tool name and parameters separately.

4. **Tool-call sequencing and planning** -- whether the model's hidden state encodes not just the *next* tool call but a *plan* of upcoming tool calls in a multi-step agent workflow -- is unexplored.

5. **Interaction between conversation history and tool-call encoding** -- does the probe direction shift when prior tool calls returned errors? When the user corrects the agent? When the context window grows? Nobody has studied this.

6. **Cross-turn probe transfer** -- whether a probe trained at turn 1 generalizes to turn 5 when the context is rich with prior tool results -- is untested.

---

### 4. Key Methodological Differences: Text Answer Probing vs. Tool-Call Probing

| Dimension | Cox et al. (2603.01437) Text QA | Tool-Call Probing (2605.07990 etc.) |
|---|---|---|
| **Output space** | Binary (A/B, yes/no) | K discrete tool names from fixed menu + unbounded parameter space |
| **Probe target** | Single scalar direction | Per-tool mean vectors in a K-dimensional selection space |
| **Output structure** | Free text answer token | Structured JSON: {"name": ..., "arguments": {...}} |
| **Context dependency** | 4 few-shot examples | System prompt with tool definitions, potentially multi-turn history |
| **Schema constraint** | None | Tool schemas constrain valid outputs; wrong schema = execution failure |
| **Parameter encoding** | N/A | Not linearly readable (confirmed 0/30 by 2605.07990) |
| **Multi-turn** | Not applicable | Critical but poorly understood; steering degrades |
| **Practical stakes** | Getting QA wrong is benign | Wrong tool call can execute irreversible actions (delete data, send money) |

---

### 5. Recommendations for Differentiating Your Proposal

Given this landscape, the strongest differentiation would be to focus on what is explicitly identified as open and hard:

**Strongest angle:** "Pre-reasoning encoding of tool-call decisions in **multi-turn agentic contexts** where prior tool results, error states, and conversation history create dynamic context that fundamentally differs from the static single-turn settings studied so far."

Specific testable hypotheses that no existing paper addresses:
- H1: Tool-identity probe accuracy degrades as conversation depth increases (due to context competition in the residual stream)
- H2: The probe direction for the same tool shifts across turns when prior tool results modify the task state
- H3: Error feedback from prior tool calls creates detectable "replanning" signals in hidden states before the next tool selection
- H4: Joint probing of (tool_name + key_parameters) reveals entangled representations that are not decomposable into independent linear directions

This reframing acknowledges 2603.01437 and the May 2026 tool-probing papers, positions your work as the **multi-turn extension** they all call for, and highlights the unique challenges of probing in conversation-rich, state-dependent settings that no existing work addresses.

Sources:
- [Decoding Answers Before Chain-of-Thought (2603.01437)](https://arxiv.org/abs/2603.01437)
- [Tool Calling is Linearly Readable and Steerable in Language Models (2605.07990)](https://arxiv.org/html/2605.07990)
- [LLM Agents Already Know When to Call Tools (2605.09252)](https://arxiv.org/html/2605.09252v1)
- [Internal Representations as Indicators of Hallucinations in Agent Tool Selection (2601.05214)](https://arxiv.org/html/2601.05214v1)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use (2605.06890)](https://arxiv.org/html/2605.06890)
- [Catching Rationalization in the Act (2603.17199)](https://arxiv.org/pdf/2603.17199)
- [Knowing Before Saying (2505.24362)](https://arxiv.org/abs/2505.24362)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "589c18df-afd5-480a-91c5-e1ce825a7512",
  "isSidechain": true,
  "agentId": "a4f75ce9cd4490ba2",
  "requestId": "req_011CbC6ZukGvApnzT5YL2nF3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69f3b40b-d96a-45a9-a7e8-9840a1c67222",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "826e68f0-f084-4703-baa7-eafff3ec0b55",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPPyPd6tzuuS5pngdiRynP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 642,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 27884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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
