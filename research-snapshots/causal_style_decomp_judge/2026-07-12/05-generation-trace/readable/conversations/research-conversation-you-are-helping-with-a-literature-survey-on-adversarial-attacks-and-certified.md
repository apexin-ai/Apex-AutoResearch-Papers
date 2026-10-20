# Research conversation: You are helping with a literature survey on adversarial attacks and certified defenses for RAG systems. Search for paper

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af5683602d21c3aad.jsonl`
- **Structured JSON:** [`34466cbd88ade124bec0.json`](../../sessions/34/34466cbd88ade124bec0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

79 recorded events

### User

_source line 1 · 2026-05-30T06:12:58.448Z_

You are helping with a literature survey on adversarial attacks and certified defenses for RAG systems. Search for papers from 2024-2026.

Execute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:

1. Search: "corpus poisoning RAG retrieval augmented generation attack 2024 2025 2026"
2. Search: "PoisonedRAG adversarial retrieval attack 2024 2025"
3. Search: "certified robust RAG retrieval corruption defense 2025 2026"
4. Search: "RobustRAG certifiably robust retrieval augmented generation"
5. Search: "ReliabilityRAG graph-theoretic defense retrieval poisoning Princeton"
6. Search: "adversarial attacks knowledge retrieval LLM 2025 2026"

For each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.

Return a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about attacking or defending RAG systems against corpus/retrieval poisoning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "03484b7c-5f17-4899-b288-5532980a2667",
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

_source line 2 · 2026-05-30T06:12:58.450Z_

```json
{
  "parentUuid": "03484b7c-5f17-4899-b288-5532980a2667",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
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
  "uuid": "21ef3ef3-2d38-4912-af46-61c92d426227",
  "timestamp": "2026-05-30T06:12:58.450Z",
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

_source line 3 · 2026-05-30T06:12:58.451Z_

```json
{
  "parentUuid": "21ef3ef3-2d38-4912-af46-61c92d426227",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2771bf11-0bfc-4889-b892-b3908de2ad81",
  "timestamp": "2026-05-30T06:12:58.451Z",
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

_source line 4 · 2026-05-30T06:13:01.445Z_



I'll start by loading the WebSearch and WebFetch tools, then execute the searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2771bf11-0bfc-4889-b892-b3908de2ad81",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2CgbXbgTE6xbDWgGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76ba5a2e-39fa-45ea-b442-4a8f1fb6a922",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqmrDXR1cv7CB4zfHjPU96",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1610,
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

_source line 5 · 2026-05-30T06:13:02.091Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013p1uux5VQhS1iQ7xqgnf84`</summary>

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
  "parentUuid": "76ba5a2e-39fa-45ea-b442-4a8f1fb6a922",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2CgbXbgTE6xbDWgGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a41c8ca-c78d-41be-bcd4-e5adb1942b15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqmrDXR1cv7CB4zfHjPU96",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 7413,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1610,
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

_source line 6 · 2026-05-30T06:13:02.095Z_

<details><summary>↩ Tool result · `toolu_013p1uux5VQhS1iQ7xqgnf84`</summary>

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
  "parentUuid": "0a41c8ca-c78d-41be-bcd4-e5adb1942b15",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "1acb6b6b-e01c-4e09-9011-798c9d291656",
  "sourceToolAssistantUUID": "0a41c8ca-c78d-41be-bcd4-e5adb1942b15",
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

_source line 7 · 2026-05-30T06:13:04.511Z_



Now let me execute all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1acb6b6b-e01c-4e09-9011-798c9d291656",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdfa652e-317b-4222-84ca-f6f1c45a72df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
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

_source line 8 · 2026-05-30T06:13:05.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SXxZT2ERXrQk3SwhWStANT`</summary>

```json
{
  "query": "corpus poisoning RAG retrieval augmented generation attack 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdfa652e-317b-4222-84ca-f6f1c45a72df",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff5f50a7-9847-4ba9-a268-274f31b882e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
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

_source line 9 · 2026-05-30T06:13:05.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018cgtAL3u2ifJJuNbg15Wtj`</summary>

```json
{
  "query": "PoisonedRAG adversarial retrieval attack 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5f50a7-9847-4ba9-a268-274f31b882e2",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15451cb6-6557-4b7c-9897-fa3ff62b34f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
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

_source line 10 · 2026-05-30T06:13:06.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FMrXFg4fNQbsAQF8NCYxZg`</summary>

```json
{
  "query": "certified robust RAG retrieval corruption defense 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15451cb6-6557-4b7c-9897-fa3ff62b34f7",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35b20a24-9a6b-4b56-8c73-d8d3b77c216c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
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

_source line 11 · 2026-05-30T06:13:06.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E3RmFqi86FR4jXBSwUiNBC`</summary>

```json
{
  "query": "RobustRAG certifiably robust retrieval augmented generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b20a24-9a6b-4b56-8c73-d8d3b77c216c",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7c32f4e-3390-4364-8c1a-c1e3fae11645",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
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

_source line 12 · 2026-05-30T06:13:07.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GpYkVX5jD2Y6RY5Bw2yhT`</summary>

```json
{
  "query": "ReliabilityRAG graph-theoretic defense retrieval poisoning Princeton"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7c32f4e-3390-4364-8c1a-c1e3fae11645",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f6049b9-2306-4fbf-9a07-1a37cbf2f165",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
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

_source line 13 · 2026-05-30T06:13:08.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018xhMuik9NPhTTCJHP7Cf4P`</summary>

```json
{
  "query": "adversarial attacks knowledge retrieval LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f6049b9-2306-4fbf-9a07-1a37cbf2f165",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG2UWMYqmfogiDrTKZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75b22885-f311-450e-9dc9-e82573e74ccf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXt7Ekh9pky89Pzninpky",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9023,
      "output_tokens": 331,
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
          "output_tokens": 331,
          "cache_read_input_tokens": 9023,
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

_source line 14 · 2026-05-30T06:13:12.751Z_

<details><summary>↩ Tool result · `toolu_01SXxZT2ERXrQk3SwhWStANT`</summary>

```text
Web search results for query: "corpus poisoning RAG retrieval augmented generation attack 2024 2025 2026"

Links: [{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=nBta7psl5J"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714756"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"}]

I found several relevant research papers and resources on corpus poisoning attacks against Retrieval-Augmented Generation (RAG) systems from 2024-2026. Here's what the research shows:

## Overview of Corpus Poisoning Attacks on RAG

Corpus poisoning attacks exploit RAG's dependence on extensive, publicly sourced corpora, and attackers can manipulate the retriever to return factually incorrect information by injecting adversarial data into the underlying RAG database.

## Recent Research Developments

**Defense Mechanisms (2025-2026):**
RAGPart leverages the inherent training dynamics of dense retrievers using document partitioning to mitigate poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.

The knowledge expansion defense enhances retrieval robustness by enlarging the set of retrieved top-ranked documents, thus increasing the likelihood of including benign information and diminishing the influence of poisoned content during generation.

**Competitive Poisoning (2025-2026):**
Research shows that RAG poisoning attacks behave differently when multiple attackers compete, and explores how adversaries seed the corpus with manipulated content.

**Practical Attacks (2024-2025):**
PoisonedRAG was the first knowledge database corruption attack against RAG systems, and was accepted to USENIX Security 2025.

The research landscape demonstrates ongoing efforts to both develop and defend against corpus poisoning attacks in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff5f50a7-9847-4ba9-a268-274f31b882e2",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "ee48a4f8-f40d-4f97-82a1-0ae9e06155d5",
  "sourceToolAssistantUUID": "ff5f50a7-9847-4ba9-a268-274f31b882e2",
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

_source line 15 · 2026-05-30T06:13:12.874Z_

<details><summary>↩ Tool result · `toolu_018cgtAL3u2ifJJuNbg15Wtj`</summary>

```text
Web search results for query: "PoisonedRAG adversarial retrieval attack 2024 2025"

Links: [{"title":"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms | OpenReview","url":"https://openreview.net/forum?id=2aL6gcFX7q"},{"title":"Exploring knowledge poisoning attacks to retrieval-augmented generation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1566253525009625"},{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.698.pdf"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"[2402.07867] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/abs/2402.07867"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation","url":"https://arxiv.org/pdf/2405.20485"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...","url":"https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"}]

I found comprehensive information about PoisonedRAG. Here's what the search results reveal:

## PoisonedRAG Overview

PoisonedRAG is a USENIX Security 2025 paper on "Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models." The paper was accepted to USENIX Security 2025 in June 2024.

## The Attack Mechanism

PoisonedRAG is the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. RAG systems are vulnerable to adversarial poisoning attacks, where attackers manipulate retrieval systems by poisoning the data corpus used for retrieval.

## Attack Effectiveness

PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts. Evaluations of several defenses show they are insufficient to defend against PoisonedRAG.

## Research Context

Recent efforts to attack retrieval-augmented generation (RAG) systems mainly focus on manipulating the retrieval corpus to induce malicious responses. Related research has explored defenses against such attacks, including retrieval-stage defenses and knowledge poisoning attacks on knowledge graph-based RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15451cb6-6557-4b7c-9897-fa3ff62b34f7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "6eec6db4-00f1-4973-ab43-9da2b43cb4d0",
  "sourceToolAssistantUUID": "15451cb6-6557-4b7c-9897-fa3ff62b34f7",
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

_source line 16 · 2026-05-30T06:13:13.156Z_

<details><summary>↩ Tool result · `toolu_01E3RmFqi86FR4jXBSwUiNBC`</summary>

```text
Web search results for query: "RobustRAG certifiably robust retrieval augmented generation"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Certifiably Robust RAG against Retrieval Corruption | OpenReview","url":"https://openreview.net/forum?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v1"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"[2405.15556v1] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556v1"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption - DEV Community","url":"https://dev.to/aimodels-fyi/certifiably-robust-rag-against-retrieval-corruption-3a7p"},{"title":"RbFT: Robust Fine-tuning for Retrieval-Augmented Generation against Retrieval Defects","url":"https://arxiv.org/html/2501.18365v1"}]

Based on the search results, here's what I found about RobustRAG:

## Overview

RobustRAG addresses the vulnerability of retrieval-augmented generation (RAG) to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

## Key Approach

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks, using an isolate-then-aggregate strategy where passages are isolated into disjoint groups, LLM responses are generated based on concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output. The framework includes keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.

## Certifiable Robustness

RobustRAG achieves certifiable robustness by formally certifying non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.

## Evaluation

The framework was evaluated on open-domain question-answering and free-form long text generation tasks across three datasets and three LLMs.

The research was authored by Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, and Prateek Mittal, with affiliations at NVIDIA, Princeton University, and UC Berkeley.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7c32f4e-3390-4364-8c1a-c1e3fae11645",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "53558fcc-fb42-4e3f-9c54-2d510ac65bc6",
  "sourceToolAssistantUUID": "f7c32f4e-3390-4364-8c1a-c1e3fae11645",
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

_source line 17 · 2026-05-30T06:13:14.076Z_

<details><summary>↩ Tool result · `toolu_01FMrXFg4fNQbsAQF8NCYxZg`</summary>

```text
Web search results for query: "certified robust RAG retrieval corruption defense 2025 2026"

Links: [{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"}]

Based on the search results, here's what I found regarding certified robust RAG retrieval corruption defense:

## RobustRAG: Certified Defense Against Retrieval Corruption

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) has been shown vulnerable to retrieval corruption attacks where an attacker can inject malicious passages into retrieval results to induce inaccurate responses.

### Core Defense Strategy

The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output. The framework uses keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.

### Certification and Performance

RobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, formal certification provides non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages. 

RobustRAG achieves substantial certifiable robustness while maintaining high clean performance, e.g., 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG. Additionally, RobustRAG demonstrates strong empirical robustness against PoisonedRAG and indirect prompt injection attacks, reducing attack success rates from over 90% to approximately 10%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35b20a24-9a6b-4b56-8c73-d8d3b77c216c",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "32f9e4ff-7669-4e1d-a837-453286c4396c",
  "sourceToolAssistantUUID": "35b20a24-9a6b-4b56-8c73-d8d3b77c216c",
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

_source line 18 · 2026-05-30T06:13:14.944Z_

<details><summary>↩ Tool result · `toolu_014GpYkVX5jD2Y6RY5Bw2yhT`</summary>

```text
Web search results for query: "ReliabilityRAG graph-theoretic defense retrieval poisoning Princeton"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"Chong Xiang's research works | Princeton University and other places","url":"https://www.researchgate.net/scientific-contributions/Chong-Xiang-2175323098"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning","url":"https://arxiv.org/pdf/2508.20083"}]

Based on the search results, I can provide you with information about ReliabilityRAG:

## ReliabilityRAG Overview

ReliabilityRAG is a novel framework designed to make RAG-based systems robust by presenting a strategy of finding a "consistent majority" over a set of retrieved documents by taking a graph-theoretic perspective.

## Key Features

The framework introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, and the MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption.

The approach explicitly incorporates reliability signals from the retriever—whether in the form of document rank or explicit reliability scores—to guide more robust generation.

## Robustness and Scalability

Recognizing the computational cost of exact MIS for large retrieval sets, a scalable weighted sample and aggregate framework was developed that explicitly utilizes reliability information while efficiently handling many documents.

ReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents k grows large, provided certain conditions are met.

## Performance

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f6049b9-2306-4fbf-9a07-1a37cbf2f165",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "87015832-2ef7-47d0-9a94-80aabf8244f3",
  "sourceToolAssistantUUID": "1f6049b9-2306-4fbf-9a07-1a37cbf2f165",
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

_source line 19 · 2026-05-30T06:13:20.118Z_

<details><summary>↩ Tool result · `toolu_018xhMuik9NPhTTCJHP7Cf4P`</summary>

```text
Web search results for query: "adversarial attacks knowledge retrieval LLM 2025 2026"

Links: [{"title":"Memory poisoning attacks on retrieval-augmented Large Language Model agents via deceptive semantic reasoning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197626002496"},{"title":"\"Someone Hid It\": Query-Agnostic Black-Box Attacks on LLM-Based Retrieval","url":"https://arxiv.org/pdf/2602.00364"},{"title":"Injecting Falsehoods: Adversarial Man-in-the-Middle Attacks Undermining Factual Recall in LLMs","url":"https://arxiv.org/pdf/2511.05919"},{"title":"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections | OpenReview","url":"https://openreview.net/forum?id=7B9mTg7z25"},{"title":"Advancing NLP Security by Leveraging LLMs as Adversarial Engines","url":"https://arxiv.org/pdf/2410.18215"},{"title":"Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs","url":"https://arxiv.org/pdf/2603.24511"},{"title":"ACL 2024 Tutorial: Vulnerabilities of Large Language Models to Adversarial Attacks","url":"https://llm-vulnerability.github.io/"},{"title":"Survey of Vulnerabilities in Large Language Models Revealed by   Adversarial Attacks","url":"https://arxiv.org/pdf/2310.10844"}]

Here are the search results for "adversarial attacks knowledge retrieval LLM 2025 2026":

## Key Findings

**Memory Poisoning Attacks on RAG Systems**: A recent attack method called DSRM exposes security vulnerabilities of LLM agents based on RAG when confronted with forged historical knowledge. Despite the strong capabilities of RAG in leveraging knowledge bases and performing complex reasoning, their extensive interaction with knowledge bases introduces significant security risks.

**Query-Agnostic Black-Box Attacks**: Researchers are investigating scenarios where attackers aim to hide victim documents from LLM-based Retrieval systems. As large-language models advance in performance, retrieval methods pose potential security risks in the face of adversarial attacks that could diminish useful information and trigger harmful content by LLMs.

**Factual Integrity Threats**: As LLMs transition to foundational pillars of information retrieval and agentic workflows, the security of their factual integrity has become a primary concern. Models may prioritize adversarial instructions over their own factual recall, and are vulnerable to adversarial attacks that exploit prompt sensitivity.

**Adaptive Defense Evaluation**: Recent research shows that jailbreak and prompt injection defenses must evaluate against adaptive attacks rather than static datasets, with researchers breaking 12 defenses using simple attack techniques.

**Automated Attack Discovery**: An automated approach using LLM agents has discovered adversarial attack algorithms achieving up to 40% attack success rates on certain benchmarks, with attacks optimized on surrogate models transferring directly to held-out models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75b22885-f311-450e-9dc9-e82573e74ccf",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "4481db30-0d95-4e19-8dbd-b16b1d9d08bb",
  "sourceToolAssistantUUID": "75b22885-f311-450e-9dc9-e82573e74ccf",
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

_source line 20 · 2026-05-30T06:13:23.562Z_

Excellent. I've identified many promising papers. Now let me fetch the arxiv abstracts for all the key papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4481db30-0d95-4e19-8dbd-b16b1d9d08bb",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e0699b1-94c8-4600-9a18-4cafe9d65544",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 21 · 2026-05-30T06:13:24.981Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TKvmXmUGs7mosKDVVf2Hax`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.07867",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e0699b1-94c8-4600-9a18-4cafe9d65544",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "494eba6c-670a-4f18-bed1-96aef73e638e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 22 · 2026-05-30T06:13:25.935Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ErabhFiqpobXpdoKEobSNX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.15556",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494eba6c-670a-4f18-bed1-96aef73e638e",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7d729a5-5595-4576-a8e4-80de7dc517e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 23 · 2026-05-30T06:13:26.349Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018d1SwK76eHs35t5uyKuFX6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.23519",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d729a5-5595-4576-a8e4-80de7dc517e4",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87a88f47-9746-42bf-ace4-e7f16e9c2286",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 24 · 2026-05-30T06:13:27.391Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013qM1TAKPimPCD8A16LCcc7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.24268",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87a88f47-9746-42bf-ace4-e7f16e9c2286",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "222b8c00-8aeb-496e-bcde-f96a3a2e53e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 25 · 2026-05-30T06:13:28.270Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015uzTZFUTb753sDyF3Z9RD9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.03957",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "222b8c00-8aeb-496e-bcde-f96a3a2e53e9",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0d11b16-9adc-4681-907e-c31f31662ce7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 26 · 2026-05-30T06:13:28.766Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BQd4UMZjqjLCDAe244vMF1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.16708",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0d11b16-9adc-4681-907e-c31f31662ce7",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d559dada-83f5-4a28-a571-9f18b5fd54cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 27 · 2026-05-30T06:13:29.708Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BkHfa2HR8z1z3TG1PVQVHv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.20485",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d559dada-83f5-4a28-a571-9f18b5fd54cd",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48f55980-df35-4b1b-a607-d3e759305450",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 28 · 2026-05-30T06:13:30.608Z_

<details><summary>↩ Tool result · `toolu_01ErabhFiqpobXpdoKEobSNX`</summary>

```text
# Paper Information

**Title:** "Certifiably Robust RAG against Retrieval Corruption"

**Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal

**Submission Date:** May 24, 2024 (v1); Last Revised: April 1, 2026 (v2)

**Venue:** arXiv (Computer Science - Machine Learning, cs.LG)

**Abstract:**

The authors present RobustRAG, a defense framework addressing vulnerabilities in retrieval-augmented generation systems. The core contribution involves an "isolate-then-aggregate strategy" where passages are partitioned into separate groups, responses are generated from each group independently, and then securely combined. The framework incorporates keyword-based and decoding-based aggregation techniques for text responses.

The work demonstrates formal robustness guarantees, allowing researchers to "formally certify non-trivial lower bounds on response quality -- even against an adaptive attacker" with knowledge of the defense and ability to inject malicious passages. Evaluation spans open-domain question-answering and text generation tasks across three datasets and language models, showing the approach's practical effectiveness against retrieval corruption attacks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7d729a5-5595-4576-a8e4-80de7dc517e4",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "96027fb2-a330-41a1-a0bb-b44c55b69cc7",
  "sourceToolAssistantUUID": "f7d729a5-5595-4576-a8e4-80de7dc517e4",
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

_source line 29 · 2026-05-30T06:13:30.453Z_

<details><summary>↩ Tool result · `toolu_018d1SwK76eHs35t5uyKuFX6`</summary>

```text
# Paper Summary

**Title:** "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search"

**Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova

**Submission/Publication Date:** Submitted September 27, 2025; revised February 15, 2026

**Venue:** NeurIPS 2025

**Abstract:** This work addresses vulnerabilities in retrieval-augmented generation systems by introducing a defense framework that leverages document reliability signals. The researchers propose a graph-theoretic approach using Maximum Independent Set algorithms to identify trustworthy documents while filtering malicious ones. The method incorporates "a scalable weighted sample and aggregate framework" to handle large retrieval sets efficiently while maintaining robustness guarantees. Empirical evaluation demonstrates improved resilience against adversarial attacks compared to existing methods, alongside strong performance on long-form generation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87a88f47-9746-42bf-ace4-e7f16e9c2286",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "5da73fc4-ef7c-4176-a1cb-63f12818b5a3",
  "sourceToolAssistantUUID": "87a88f47-9746-42bf-ace4-e7f16e9c2286",
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

_source line 30 · 2026-05-30T06:13:30.712Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012wFdCv6o4MDK6UXcHJgK8p`</summary>

```json
{
  "url": "https://openreview.net/forum?id=nBta7psl5J",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da73fc4-ef7c-4176-a1cb-63f12818b5a3",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe4e0ecd-34cb-42c1-846d-c54b76e6cf85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 31 · 2026-05-30T06:13:31.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J6tGkfCcb4WHS3zcc5XK3M`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08304",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe4e0ecd-34cb-42c1-846d-c54b76e6cf85",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG3oJUqRLDtvaNjUFHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c14bb3b-5c6d-4ca1-843f-2989d463e2c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMQNUdsWgD3ZLDwvm9pjjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5154,
      "cache_read_input_tokens": 10147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5154,
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

_source line 32 · 2026-05-30T06:13:31.890Z_

<details><summary>↩ Tool result · `toolu_015uzTZFUTb753sDyF3Z9RD9`</summary>

```text
# Paper Summary

**Title:** "Practical Poisoning Attacks against Retrieval-Augmented Generation"

**Authors:** Baolei Zhang, Yuxi Chen, Zhuqing Liu, Lihai Nie, Tong Li, Zheli Liu, Minghong Fang

**Submission Date:** April 4, 2025 (v1); Revised January 8, 2026 (v2)

**Venue:** ACM SACMAT 2026

**Abstract:** The researchers address vulnerabilities in Retrieval-Augmented Generation systems, which enhance large language models but remain susceptible to poisoning attacks. They introduce CorruptRAG, "a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text," making it more feasible and stealthy than previous approaches that required multiple poisoned entries. Testing across large-scale datasets demonstrated that their method "achieves higher attack success rates than existing baselines."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0d11b16-9adc-4681-907e-c31f31662ce7",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "e3ccc81b-2906-4930-b5a4-e77b0a45d3c7",
  "sourceToolAssistantUUID": "d0d11b16-9adc-4681-907e-c31f31662ce7",
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

_source line 33 · 2026-05-30T06:13:33.354Z_

<details><summary>↩ Tool result · `toolu_01BQd4UMZjqjLCDAe244vMF1`</summary>

```text
# Research Paper Summary

**Title:** "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks"

**Authors:** Jinyan Su, Jin Peng Zhou, Zhengxin Zhang, Preslav Nakov, Claire Cardie

**Submission/Publication Date:** 
- Initial submission: December 21, 2024
- Latest revision: July 26, 2025

**Venue:** arXiv (Computer Science > Information Retrieval)

**Abstract:** The paper examines how retrieval-augmented generation systems respond to adversarial poisoning attacks where malicious passages corrupt retrieval corpora. The researchers introduce a structured taxonomy of context types—adversarial, untouched, and guiding—to systematically study their effects on model outputs. They evaluate multiple retrievers and find that "skeptical prompting" can partially protect language models by activating internal reasoning, though effectiveness varies by model capability. The work offers practical recommendations for developing more resilient RAG systems suitable for real-world deployment, with code made available publicly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d559dada-83f5-4a28-a571-9f18b5fd54cd",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "0f0898f7-494f-4935-bc99-5e31c46d809d",
  "sourceToolAssistantUUID": "d559dada-83f5-4a28-a571-9f18b5fd54cd",
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

_source line 34 · 2026-05-30T06:13:33.596Z_

<details><summary>↩ Tool result · `toolu_013qM1TAKPimPCD8A16LCcc7`</summary>

```text
# Paper Summary

**Title:** "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation"

**Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang

**Submission Date:** December 30, 2025

**Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval [Oral presentation]

**Abstract:**

The paper addresses vulnerabilities in Retrieval-Augmented Generation systems where adversaries inject poisoned documents into retrieval corpora. The researchers propose two lightweight retrieval-stage defenses—RAGPart and RAGMask—that operate on retrievers without modifying generation models. RAGPart exploits document partitioning during dense retriever training, while RAGMask detects suspicious tokens through similarity shifts under targeted masking. Testing across multiple benchmarks, poisoning strategies, and state-of-the-art retrievers demonstrates these defenses reduce attack success rates while maintaining performance under normal conditions. The work provides "practical insights for robust RAG deployments" and stresses-tests defenses with an interpretable attack methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "222b8c00-8aeb-496e-bcde-f96a3a2e53e9",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "8d25c96d-3fa3-42b1-9892-352ff026eaf6",
  "sourceToolAssistantUUID": "222b8c00-8aeb-496e-bcde-f96a3a2e53e9",
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

_source line 35 · 2026-05-30T06:13:34.591Z_

<details><summary>↩ Tool result · `toolu_01BkHfa2HR8z1z3TG1PVQVHv`</summary>

```text
# Paper Information

**Title:** "Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation"

**Authors:** Harsh Chaudhari, Giorgio Severi, John Abascal, Anshuman Suri, Matthew Jagielski, Christopher A. Choquette-Choo, Milad Nasr, Cristina Nita-Rotaru, Alina Oprea

**Submission/Publication Date:** Submitted May 30, 2024; last revised October 1, 2025 (version 3)

**Venue:** arXiv (cs.CR - Cryptography and Security)

**Abstract:** This work introduces a poisoning attack targeting RAG systems through injection of a single harmful document. The researchers developed a two-stage optimization technique that crafts a document retrieved only when specific trigger tokens appear in user queries. The poisoned content induces various harmful outcomes including refusal to answer, reputation damage, privacy violations, and harmful behaviors. The team demonstrated their approach on open-source models (Gemma, Vicuna, Llama) and showed transferability to GPT-3.5 Turbo and GPT-4. They also successfully executed the attack on "Chat with RTX," a production RAG system.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48f55980-df35-4b1b-a607-d3e759305450",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "dfba524f-397f-4df1-98c2-7c44f5920716",
  "sourceToolAssistantUUID": "48f55980-df35-4b1b-a607-d3e759305450",
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

_source line 36 · 2026-05-30T06:13:35.247Z_

<details><summary>↩ Tool result · `toolu_012wFdCv6o4MDK6UXcHJgK8p`</summary>

```text
# Paper Information

**Title:** "Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation"

**Authors:** Liuji Chen, Xiaofang Yang, Yuanzhuo Lu, Jinghao Zhang, Xin Sun, Qiang Liu, Shu Wu, Jing Dong, Liang Wang

**Submission Date:** September 19, 2025 (Modified: February 11, 2026)

**Venue:** ICLR 2026 Conference

**Abstract:** The authors investigate poisoning threats against RAG systems when multiple adversaries with conflicting goals target the same query simultaneously. They formalize this competitive attack scenario and introduce "competitive effectiveness" as a metric measuring attacker advantage under such conditions. Their experiments demonstrate that many single-attacker strategies perform poorly when competing with others, revealing performance reversals and metric limitations. They present "PoisonArena," "a standardized framework and benchmark for evaluating poisoning attacks and defenses under realistic, multi-adversary conditions."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe4e0ecd-34cb-42c1-846d-c54b76e6cf85",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "a1d46e6d-6817-40be-ae73-9c733ef89549",
  "sourceToolAssistantUUID": "fe4e0ecd-34cb-42c1-846d-c54b76e6cf85",
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

_source line 37 · 2026-05-30T06:13:35.936Z_

<details><summary>↩ Tool result · `toolu_01J6tGkfCcb4WHS3zcc5XK3M`</summary>

```text
# Paper Details

**Title:** Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions

**Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen

**Submission/Publication Date:** Submitted April 9, 2026; revised May 27, 2026 (v2)

**Venue:** arXiv (cs.CR - Cryptography and Security; cs.AI - Artificial Intelligence)

**Abstract:** The research presents a framework for understanding security threats in retrieval-augmented generation systems. The authors propose "SLOT," a classification scheme examining attack surfaces, defense mechanisms, security objectives aligned with CIA properties, and target categories ranging from individual queries to distributed manipulation patterns. The work maps these elements across a six-stage knowledge pipeline and identifies structural gaps in existing approaches. The authors recommend pursuing more realistic threat models, comprehensive defenses without blind spots, stronger privacy protections, and evaluation methodologies suited for multimodal and autonomous RAG implementations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c14bb3b-5c6d-4ca1-843f-2989d463e2c4",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "386ad921-429f-41db-913f-fee5bffa79bb",
  "sourceToolAssistantUUID": "6c14bb3b-5c6d-4ca1-843f-2989d463e2c4",
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

_source line 38 · 2026-05-30T06:13:36.968Z_

<details><summary>↩ Tool result · `toolu_01TKvmXmUGs7mosKDVVf2Hax`</summary>

```text
# PoisonedRAG Paper Details

**Title:** "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models"

**Authors:** Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia

**Submission Date:** February 12, 2024 (v1); Last revised August 13, 2024 (v3)

**Venue:** USENIX Security Symposium 2025

**Abstract:** The research demonstrates that knowledge databases in RAG systems present a significant security vulnerability. The authors introduce PoisonedRAG, an attack methodology where adversaries inject malicious texts into a knowledge database to manipulate LLM outputs. They formulate this as an optimization problem with solutions for both black-box and white-box attack scenarios. Their findings indicate "a 90% attack success rate when injecting five malicious texts for each target question" into databases containing millions of documents. The study evaluates existing defenses and concludes they are "insufficient to defend against PoisonedRAG," emphasizing the urgency of developing more robust protective measures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "494eba6c-670a-4f18-bed1-96aef73e638e",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "15daaa6e-43bc-4b68-b3d4-82a986b2fce2",
  "sourceToolAssistantUUID": "494eba6c-670a-4f18-bed1-96aef73e638e",
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

_source line 39 · 2026-05-30T06:13:40.396Z_

Good. Now let me fetch the remaining papers I found in the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15daaa6e-43bc-4b68-b3d4-82a986b2fce2",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1898909-1cea-4307-9a7d-ddbc2d0c2acf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 40 · 2026-05-30T06:13:41.597Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XYEMYGvDwFCmwydPJ2a8Jm`</summary>

```json
{
  "url": "https://openreview.net/forum?id=2aL6gcFX7q",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1898909-1cea-4307-9a7d-ddbc2d0c2acf",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c22552dd-7b08-4fa0-8172-989e6b2c67f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 41 · 2026-05-30T06:13:42.603Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014do5qVJ6UneCVs72i9jEkh`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-emnlp.698.pdf",
  "prompt": "Extract the paper title, full author list, venue, and abstract from this PDF."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c22552dd-7b08-4fa0-8172-989e6b2c67f0",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7176adfb-944b-43a5-a9b1-d5d81d0aac3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 42 · 2026-05-30T06:13:43.541Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017BoXeZgZyEXdvj7ZVTg7rs`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.1145/3696410.3714756",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7176adfb-944b-43a5-a9b1-d5d81d0aac3d",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a70e816-0712-485d-8bf4-74a168d82e3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 43 · 2026-05-30T06:13:43.789Z_

<details><summary>↩ Tool result · `toolu_017BoXeZgZyEXdvj7ZVTg7rs`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a70e816-0712-485d-8bf4-74a168d82e3c",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "37444214-a761-41fa-8971-426f63135913",
  "sourceToolAssistantUUID": "4a70e816-0712-485d-8bf4-74a168d82e3c",
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

_source line 44 · 2026-05-30T06:13:44.484Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0175BmWRQdHEUfFSFNNTfiq7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.18365",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37444214-a761-41fa-8971-426f63135913",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c8c0d2b-a8f0-4f49-b9a4-e39cfbe91d7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 45 · 2026-05-30T06:13:44.857Z_

<details><summary>↩ Tool result · `toolu_01XYEMYGvDwFCmwydPJ2a8Jm`</summary>

```text
# Paper Information

**Title:** "Understanding Data Poisoning Attacks for RAG: Insights and Algorithms"

**Authors:** Xun Xian, Tong Wang, Liwen You, Yanjun Qi

**Submission Date:** 28 September 2024 (modified 5 February 2025)

**Venue:** ICLR 2025 Conference

**Abstract:** 

The authors examine vulnerabilities in Retrieval-Augmented Generation systems to adversarial data poisoning. Their key finding shows that "more effective poisoning attacks tend to occur along directions where the clean data distribution exhibits small variances." Based on this observation, they propose two contributions: a defensive method called DRS (Directional Relative Shifts) that identifies suspicious shifts in high-vulnerability directions, and a stealthy attack algorithm that minimizes detectability by regularizing poisoning data's directional shifts. The research includes evaluations across multiple scenarios involving RAG agents and passage retrieval systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c22552dd-7b08-4fa0-8172-989e6b2c67f0",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "6092c693-2362-4d93-8009-f739a07e6cd7",
  "sourceToolAssistantUUID": "c22552dd-7b08-4fa0-8172-989e6b2c67f0",
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

_source line 46 · 2026-05-30T06:13:44.956Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016PjabrfE9q4WctKvqReXii`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.00364",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6092c693-2362-4d93-8009-f739a07e6cd7",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5f58a6a-d71e-463d-8a6c-24e5c82f2a73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 47 · 2026-05-30T06:13:45.590Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qo6apTRk1Nd2eXMwcxbVMf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.20083",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f58a6a-d71e-463d-8a6c-24e5c82f2a73",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG53nPvBjmgKJqbWBiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a8fdf37-7995-4f5d-a992-e216f419a638",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JKdCTF8tXv9EWs4MCCygr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2244,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 15301,
      "output_tokens": 558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1193
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2244,
          "output_tokens": 558,
          "cache_read_input_tokens": 15301,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1193,
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

_source line 48 · 2026-05-30T06:13:48.363Z_

<details><summary>↩ Tool result · `toolu_0175BmWRQdHEUfFSFNNTfiq7`</summary>

```text
# Paper Details

**Title:** "RbFT: Robust Fine-tuning for Retrieval-Augmented Generation against Retrieval Defects"

**Authors:** Yiteng Tu, Weihang Su, Yujia Zhou, Yiqun Liu, Qingyao Ai

**Submission Date:** January 30, 2025

**Venue:** arXiv (Computer Science > Computation and Language)

**Abstract:** The researchers address vulnerabilities in retrieval-augmented generation systems by proposing a fine-tuning method. Their approach tackles the problem that "imperfections in these components often lead to the retrieval of noisy, irrelevant, or misleading counterfactual information." The proposed RbFT technique employs "two targeted fine-tuning tasks" to strengthen language models against retrieval failures. Testing demonstrates the method "significantly improves the robustness of RAG systems across diverse retrieval conditions" while maintaining efficiency and compatibility with other robustness approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c8c0d2b-a8f0-4f49-b9a4-e39cfbe91d7d",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "c8d4f353-0d00-487f-87f6-d1a6adb8f1a2",
  "sourceToolAssistantUUID": "3c8c0d2b-a8f0-4f49-b9a4-e39cfbe91d7d",
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

_source line 49 · 2026-05-30T06:13:48.783Z_

<details><summary>↩ Tool result · `toolu_014do5qVJ6UneCVs72i9jEkh`</summary>

```text
I appreciate you sharing this content, but I need to let you know that what you've provided appears to be raw PDF binary/compressed data rather than readable text. The content shows PDF stream encoding (flate compression) rather than extractable text.

To properly extract the paper title, author list, venue, and abstract, I would need either:

1. **A text-based version** of the PDF content
2. **The actual PDF file** that I could process
3. **Already-extracted metadata** from the paper

The current format makes it impossible to accurately identify these bibliographic elements. If you can provide the document in a more accessible format (plain text, or direct access to a readable PDF), I'd be happy to extract the requested information while respecting the character limits and attribution guidelines you've outlined.

[Binary content (application/pdf, 2.5MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-adversarial/41901ced-6b17-4e52-97f2-1983f67919e2/tool-results/webfetch-1780121624508-qjs84t.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7176adfb-944b-43a5-a9b1-d5d81d0aac3d",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "1936ff11-a7b4-44b4-8d9d-9c9da32b4483",
  "sourceToolAssistantUUID": "7176adfb-944b-43a5-a9b1-d5d81d0aac3d",
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

_source line 50 · 2026-05-30T06:13:49.808Z_

<details><summary>↩ Tool result · `toolu_016PjabrfE9q4WctKvqReXii`</summary>

```text
# Paper Summary

**Title:** "Someone Hid It": Query-Agnostic Black-Box Attacks on LLM-Based Retrieval

**Authors:** Jiate Li, Defu Cao, Li Li, Wei Yang, Yuehan Qin, Chenxiao Yu, Tiannuo Yang, Ryan A. Rossi, Yan Liu, Xiyang Hu, Yue Zhao

**Submission Date:** January 30, 2026 (v1); Last revised May 15, 2026 (v4)

**Venue:** arXiv (Computer Science - Cryptography and Security category)

**Abstract:** The researchers present a practical black-box attack method targeting LLM-based retrieval systems. Their approach "generates transferable injection tokens based on zero-shot surrogate LLMs without need of victim queries or victim models knowledge." The work establishes a theoretical framework for understanding these systems and formulates the transferable attack as a min-max optimization problem. They employ an adversarial learning mechanism to identify optimal adversarial tokens using learnable query samples. The method demonstrates effectiveness across benchmark datasets and popular LLM retrievers, highlighting potential robustness concerns from both malicious and inadvertent document modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5f58a6a-d71e-463d-8a6c-24e5c82f2a73",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "ccf8938b-d262-4b7c-ad70-60b3b85ada7d",
  "sourceToolAssistantUUID": "b5f58a6a-d71e-463d-8a6c-24e5c82f2a73",
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

_source line 51 · 2026-05-30T06:13:50.320Z_

<details><summary>↩ Tool result · `toolu_01Qo6apTRk1Nd2eXMwcxbVMf`</summary>

```text
# Research Paper Summary

**Title:** "Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning"

**Authors:** Yanbo Dai, Zhenlan Ji, Zongjie Li, Kuan Li, Shuai Wang

**Submission Date:** August 27, 2025

**Venue:** arXiv (Computer Science - Cryptography and Security)

**Abstract:**

The paper presents DisarmRAG, a novel attack method targeting retrieval-augmented generation systems. Rather than poisoning knowledge bases directly, the approach "compromises the retriever itself to suppress the SCA and enforce attacker-chosen outputs." The authors employ contrastive learning for model editing, enabling stealthy modifications where retrievers return malicious instructions for specific queries while maintaining normal behavior otherwise. They designed an iterative optimization framework to discover robust prompts bypassing defensive measures. Testing across six language models and three QA benchmarks showed "near-perfect retrieval of malicious instructions, which successfully suppress SCA and achieve attack success rates exceeding 90%" across diverse defensive configurations. The edited retrievers evaded detection methods, underscoring what researchers characterize as an urgent need for retriever-focused defensive strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a8fdf37-7995-4f5d-a992-e216f419a638",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "049b572a-0fb1-4d2f-ba2d-35783645edf8",
  "sourceToolAssistantUUID": "2a8fdf37-7995-4f5d-a992-e216f419a638",
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

_source line 52 · 2026-05-30T06:13:54.051Z_

Now let me fetch the RevPRAG paper and the traceback paper via alternative URLs, plus one more search for any remaining important papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "049b572a-0fb1-4d2f-ba2d-35783645edf8",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG62U3tbkz8RSfbJwdC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e08460fd-c85a-44af-9ca8-e70354a2e86a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHtFajGtKn5YHUYMeuoGFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4267,
      "cache_read_input_tokens": 16494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4267,
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

_source line 53 · 2026-05-30T06:13:55.045Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ht2zj7SvQ5BdGSBVXQdL21`</summary>

```json
{
  "query": "RevPRAG revealing poisoning attacks retrieval augmented generation EMNLP 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e08460fd-c85a-44af-9ca8-e70354a2e86a",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG62U3tbkz8RSfbJwdC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd675abc-cac6-4f81-a28b-0b8d83c2c6b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHtFajGtKn5YHUYMeuoGFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4267,
      "cache_read_input_tokens": 16494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4267,
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

_source line 54 · 2026-05-30T06:13:55.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016oFiZcJ9YAGdWqgaxZnViJ`</summary>

```json
{
  "query": "traceback poisoning attacks retrieval augmented generation WWW 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd675abc-cac6-4f81-a28b-0b8d83c2c6b6",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG62U3tbkz8RSfbJwdC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bce1371f-0f94-4ff3-95a5-c6ecffc2f7c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHtFajGtKn5YHUYMeuoGFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4267,
      "cache_read_input_tokens": 16494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4267,
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

_source line 55 · 2026-05-30T06:13:55.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JYPda4ANKGtFZjAQUhMuYE`</summary>

```json
{
  "query": "TrojanRAG backdoor attack retrieval augmented generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bce1371f-0f94-4ff3-95a5-c6ecffc2f7c5",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG62U3tbkz8RSfbJwdC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e04693f-ec5e-4a16-958e-795e92e1ddda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHtFajGtKn5YHUYMeuoGFA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4267,
      "cache_read_input_tokens": 16494,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4267
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 16494,
          "cache_creation_input_tokens": 4267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4267,
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

_source line 56 · 2026-05-30T06:14:02.170Z_

<details><summary>↩ Tool result · `toolu_016oFiZcJ9YAGdWqgaxZnViJ`</summary>

```text
Web search results for query: "traceback poisoning attacks retrieval augmented generation WWW 2025 arxiv"

Links: [{"title":"(PDF) Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/391018324_Traceback_of_Poisoning_Attacks_to_Retrieval-Augmented_Generation"},{"title":"[2504.21668] Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2504.21668"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.21668v2"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation Baolei Zhang∗","url":"https://www.arxiv.org/pdf/2504.21668v2"},{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714756"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"}]

I found relevant information about the paper you searched for. Here are the results:

The paper "Traceback of Poisoning Attacks to Retrieval-Augmented Generation" was presented at WWW '25 (April 28-May 2, 2025) in Sydney, NSW, Australia.

The paper addresses how Large language models (LLMs) integrated with retrieval-augmented generation (RAG) systems improve accuracy by leveraging external knowledge sources. However, recent research has revealed RAG's susceptibility to poisoning attacks, where the attacker injects poisoned texts into the knowledge database, leading to attacker-desired responses.

The proposed RAGForensics system operates iteratively, first retrieving a subset of texts from the database and then utilizing a specially crafted prompt to guide an LLM in detecting potential poisoning texts, with empirical evaluations across multiple datasets demonstrating effectiveness against state-of-the-art poisoning attacks.

The paper is available on arXiv as arXiv paper 2504.21668, authored by Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, and Zheli Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bce1371f-0f94-4ff3-95a5-c6ecffc2f7c5",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "3c546529-b512-4716-a7cc-6bc03db7959a",
  "sourceToolAssistantUUID": "bce1371f-0f94-4ff3-95a5-c6ecffc2f7c5",
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

_source line 57 · 2026-05-30T06:14:02.930Z_

<details><summary>↩ Tool result · `toolu_01Ht2zj7SvQ5BdGSBVXQdL21`</summary>

```text
Web search results for query: "RevPRAG revealing poisoning attacks retrieval augmented generation EMNLP 2025 arxiv"

Links: [{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.698/"},{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.698.pdf"},{"title":"[Literature Review] RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis","url":"https://www.themoonlight.io/en/review/revprag-revealing-poisoning-attacks-in-retrieval-augmented-generation-through-llm-activation-analysis"},{"title":"[2411.18948] RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis","url":"https://arxiv.org/abs/2411.18948"},{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis","url":"https://www.researchgate.net/publication/397424791_RevPRAG_Revealing_Poisoning_Attacks_in_Retrieval-Augmented_Generation_through_LLM_Activation_Analysis"},{"title":"RIPRAG: Hack a Black-box Retrieval-Augmented ...","url":"https://arxiv.org/pdf/2510.10008"},{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis","url":"https://arxiv.org/html/2411.18948v5"},{"title":"Traceback of Poisoning Attacks to Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.21668v2"}]

I found the research paper you were looking for! Here's what I found:

"RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis" was published in the Findings of the Association for Computational Linguistics: EMNLP 2025.

**Key Details:**

- **Authors:** Xue Tan, Hao Luan, Mingyu Luo, Xiaoyan Sun, Ping Chen, and Jun Dai
- **ArXiv ID:** 2411.18948

**What the Paper Does:**

RevPRAG is a flexible and automated detection pipeline that leverages the activations of LLMs for poisoned response detection. The investigation uncovers distinct patterns in LLMs' activations when generating correct responses versus poisoned responses.

**Performance:**

The approach achieved 98% true positive rate, while maintaining false positive rates close to 1%.

You can access the paper at:
- ACL Anthology: https://aclanthology.org/2025.findings-emnlp.698/
- ArXiv: https://arxiv.org/abs/2411.18948


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd675abc-cac6-4f81-a28b-0b8d83c2c6b6",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "1509fef3-a792-4668-a4f5-773234a82379",
  "sourceToolAssistantUUID": "fd675abc-cac6-4f81-a28b-0b8d83c2c6b6",
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

_source line 58 · 2026-05-30T06:14:07.784Z_

<details><summary>↩ Tool result · `toolu_01JYPda4ANKGtFZjAQUhMuYE`</summary>

```text
Web search results for query: "TrojanRAG backdoor attack retrieval augmented generation 2024 2025"

Links: [{"title":"[PDF] TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/d8d0d704446ffaf09b9722360ed76341934ec3a3"},{"title":"TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RfYD6v829Y"},{"title":"[2405.13401v1] TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models","url":"https://arxiv.org/abs/2405.13401v1"},{"title":"[2405.13401] TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models","url":"https://arxiv.org/abs/2405.13401"},{"title":"TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models","url":"https://arxiv.org/html/2405.13401v1"},{"title":"TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/trojanrag-retrieval-augmented-generation-can-be-backdoor"},{"title":"Awesome-LM-SSP/collection/paper/security/poison_&_backdoor.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/security/poison_&_backdoor.md"},{"title":"RAG Backdoor Attack in Retrieval Systems","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-backdoor-attack"}]

Based on the search results, here's what I found about TrojanRAG:

## Overview

TrojanRAG employs a joint backdoor attack in the Retrieval-Augmented Generation, thereby manipulating LLMs in universal attack scenarios. The paper was initially submitted on May 22, 2024.

## Key Characteristics

TrojanRAG is a joint backdoor attack against the Retrieval-Augmented Generation that can manipulate LLMs robustly. The attack builds multiple purpose-driven backdoors between poisoned knowledge and triggers in the retrieval backdoor injection phase, where retrieval performs well for clean queries but always returns semantic-consistency poisoned content for poisoned queries.

## Threat Model

The research comprehensively exposes the threats of backdoor attacks on LLMs by defining three standardized scenarios from the perspective of attackers, users, and jailbreaking LLMs.

## Results

Extensive experimental results on truthfulness, language understanding, and harmfulness show that TrojanRAG exhibits versatility threats while maintaining retrieval capabilities on normal queries.

## Academic Status

The paper was submitted to ICLR 2025 as a conference withdrawn submission as of November 29, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e04693f-ec5e-4a16-958e-795e92e1ddda",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "f587066c-f989-4ad3-9d1e-c8b3a77a2256",
  "sourceToolAssistantUUID": "1e04693f-ec5e-4a16-958e-795e92e1ddda",
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

_source line 59 · 2026-05-30T06:14:11.360Z_

Let me fetch details for a few more papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f587066c-f989-4ad3-9d1e-c8b3a77a2256",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG7K6x2WtJ7vcKC2Cj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6497e0bf-ca25-4052-83db-ecd082bc6818",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeqdznjyakDb19DyaMriqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 20761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 60 · 2026-05-30T06:14:12.304Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AFQwXx7vNm9gZPGhmunY6q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.18948",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6497e0bf-ca25-4052-83db-ecd082bc6818",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG7K6x2WtJ7vcKC2Cj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69bb123b-2cdc-48db-9402-bf3a2e2967bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeqdznjyakDb19DyaMriqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 20761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 61 · 2026-05-30T06:14:13.493Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BjzDqp3yX79sd6JgUTCK9F`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.21668",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69bb123b-2cdc-48db-9402-bf3a2e2967bf",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG7K6x2WtJ7vcKC2Cj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7021c5db-1158-4369-bb91-b51d34483cfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeqdznjyakDb19DyaMriqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 20761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 62 · 2026-05-30T06:14:13.735Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mqyku3iXFAnoJpsL7QPaPH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.13401",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7021c5db-1158-4369-bb91-b51d34483cfc",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG7K6x2WtJ7vcKC2Cj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79e14ac8-bf56-4328-afca-50cc4094a04a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeqdznjyakDb19DyaMriqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 20761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 63 · 2026-05-30T06:14:14.674Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016j4SLnLHGMYuv6hicWQqMd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.18543",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e14ac8-bf56-4328-afca-50cc4094a04a",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG7K6x2WtJ7vcKC2Cj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4189b2fe-5c56-42af-a11b-ac2c13c3adcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeqdznjyakDb19DyaMriqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 20761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 64 · 2026-05-30T06:14:15.017Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fqu23pSyfEFKnGzGv4Wktd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.10008",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4189b2fe-5c56-42af-a11b-ac2c13c3adcf",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG7K6x2WtJ7vcKC2Cj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bcc9ee9-9a26-40bc-930a-8d4d876bbfe9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeqdznjyakDb19DyaMriqv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 20761,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 20761,
          "cache_creation_input_tokens": 2672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2672,
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

_source line 65 · 2026-05-30T06:14:15.891Z_

<details><summary>↩ Tool result · `toolu_01AFQwXx7vNm9gZPGhmunY6q`</summary>

```text
# Paper Details

**Title:** "RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis"

**Authors:** Xue Tan, Hao Luan, Mingyu Luo, Xiaoyan Sun, Ping Chen, Jun Dai

**Submission Date:** November 28, 2024 (v1); Last revised August 29, 2025 (v5)

**Venue:** Findings of EMNLP 2025

**Abstract:** This work addresses security vulnerabilities in RAG systems where attackers inject harmful content into knowledge databases. The researchers present RevPRAG, a detection pipeline that analyzes LLM activation patterns to identify poisoned responses. The method "could achieve 98% true positive rate, while maintaining false positive rates close to 1%" across multiple datasets and RAG architectures. The research reveals distinct activation signature differences when language models generate legitimate versus compromised outputs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69bb123b-2cdc-48db-9402-bf3a2e2967bf",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "cc55ae2e-bf6e-4412-af22-0e9fae85e464",
  "sourceToolAssistantUUID": "69bb123b-2cdc-48db-9402-bf3a2e2967bf",
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

_source line 66 · 2026-05-30T06:14:17.657Z_

<details><summary>↩ Tool result · `toolu_01Mqyku3iXFAnoJpsL7QPaPH`</summary>

```text
# Paper Summary

**Title:** TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models

**Authors:** Pengzhou Cheng, Yidong Ding, Tianjie Ju, Zongru Wu, Wei Du, Ping Yi, Zhuosheng Zhang, Gongshen Liu

**Submission/Publication Date:** Submitted May 22, 2024; Last revised July 7, 2024 (v4)

**Venue:** arXiv (Computer Science > Cryptography and Security)

**Abstract:** The paper proposes TrojanRAG, a joint backdoor attack targeting the RAG component of LLMs. The approach uses "elaborate target contexts and trigger sets" with "multiple pairs of backdoor shortcuts orthogonally optimized by contrastive learning." The authors employ knowledge graphs for fine-grained matching and evaluate their method across "truthfulness, language understanding, and harmfulness" metrics, demonstrating how the attack maintains functionality on benign queries while enabling adversarial manipulation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79e14ac8-bf56-4328-afca-50cc4094a04a",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "82735de9-747e-44f1-892f-180aef8b042d",
  "sourceToolAssistantUUID": "79e14ac8-bf56-4328-afca-50cc4094a04a",
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

_source line 67 · 2026-05-30T06:14:17.989Z_

<details><summary>↩ Tool result · `toolu_01BjzDqp3yX79sd6JgUTCK9F`</summary>

```text
# Paper Summary

**Title:** "Traceback of Poisoning Attacks to Retrieval-Augmented Generation"

**Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu

**Submission Date:** April 30, 2025 (v1); October 18, 2025 (v2)

**Venue:** The Web Conference 2025

**Abstract:**

The research addresses vulnerabilities in RAG systems where attackers inject poisoned content into knowledge databases to manipulate model outputs. The authors present RAGForensics, described as "the first traceback system for RAG, designed to identify poisoned texts within the knowledge database that are responsible for the attacks." The system operates iteratively by retrieving database texts and using a crafted prompt to guide language models in detecting compromised content. The team validated their approach across multiple datasets against state-of-the-art poisoning attacks. They position this work as pioneering traceback methodology for RAG systems and offer code availability to support implementation and further research in this security domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7021c5db-1158-4369-bb91-b51d34483cfc",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "80e45d32-9100-4229-b8d2-201d8352cd67",
  "sourceToolAssistantUUID": "7021c5db-1158-4369-bb91-b51d34483cfc",
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

_source line 68 · 2026-05-30T06:14:19.599Z_

<details><summary>↩ Tool result · `toolu_016j4SLnLHGMYuv6hicWQqMd`</summary>

```text
# Paper Extraction

**Title:** Benchmarking Poisoning Attacks against Retrieval-Augmented Generation

**Authors:** Baolei Zhang, Haoran Xin, Jiatong Li, Dongzhe Zhang, Minghong Fang, Zhuqing Liu, Lihai Nie, Zheli Liu

**Submission Date:** May 24, 2025

**Venue:** arXiv (Computer Science > Cryptography and Security)

**Abstract:** The researchers present "the first comprehensive benchmark framework for evaluating poisoning attacks on RAG." Their work examines 5 standard question-answering datasets with 10 variants, 13 attack methods, and 7 defense mechanisms. Key findings indicate that while attacks succeed on standard datasets, "their effectiveness drops significantly on the expanded versions." The study demonstrates that advanced RAG architectures—including sequential, branching, conditional, loop, multi-turn conversational, multimodal, and agent-based systems—"remain susceptible to poisoning attacks," and current defenses prove inadequate, highlighting the need for stronger protective strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4189b2fe-5c56-42af-a11b-ac2c13c3adcf",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "b1e966cb-4380-417b-b87b-f9d0a09a91eb",
  "sourceToolAssistantUUID": "4189b2fe-5c56-42af-a11b-ac2c13c3adcf",
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

_source line 69 · 2026-05-30T06:14:20.394Z_

<details><summary>↩ Tool result · `toolu_01Fqu23pSyfEFKnGzGv4Wktd`</summary>

```text
# Paper Details

**Title:** "RIPRAG: Hack a Black-box Retrieval-Augmented Generation Question-Answering System with Reinforcement Learning"

**Authors:** Meng Xi, Sihan Lv, Yechen Jin, Guanjie Cheng, Naibo Wang, Ying Li, Jianwei Yin

**Submission/Publication Date:** Submitted October 11, 2025; revised January 11, 2026

**Venue:** arXiv (Computer Science > Artificial Intelligence)

**Abstract:** 
The paper addresses RAG poisoning attacks by proposing RIPRAG, a framework that treats target systems as black boxes. Using reinforcement learning with black-box feedback, the method optimizes poisoned document generation through similarity and attack rewards. The authors report achieving "an attack success rate (ASR) improvement of up to 0.72 compared to baseline methods," demonstrating vulnerabilities in current defensive strategies and offering insights for LLM security research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bcc9ee9-9a26-40bc-930a-8d4d876bbfe9",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "41006457-d7eb-4780-83f0-ac43da15912e",
  "sourceToolAssistantUUID": "3bcc9ee9-9a26-40bc-930a-8d4d876bbfe9",
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

_source line 70 · 2026-05-30T06:14:23.060Z_

Now let me search for a couple more important areas to ensure completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41006457-d7eb-4780-83f0-ac43da15912e",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG8F2exdNkkJ2vB7vLj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "898051da-62c0-4ff7-8007-5711fb732b9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhqLheEiyohU8ewZw8U34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1765,
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

_source line 71 · 2026-05-30T06:14:23.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UTRWxtHBUSW3XCGkNs2sAB`</summary>

```json
{
  "query": "indirect prompt injection RAG retrieval augmented generation attack defense 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "898051da-62c0-4ff7-8007-5711fb732b9b",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG8F2exdNkkJ2vB7vLj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1273c514-cd40-472d-a60c-7709e0c70a96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhqLheEiyohU8ewZw8U34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1765,
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

_source line 72 · 2026-05-30T06:14:24.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018wNDrP2TJWxkjtWwJJ1kDk`</summary>

```json
{
  "query": "corpus poisoning dense retrieval attack HOTFLIP embedding space 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1273c514-cd40-472d-a60c-7709e0c70a96",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG8F2exdNkkJ2vB7vLj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b84129b-bbc7-439d-8732-ff86e87cfa71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqhqLheEiyohU8ewZw8U34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1765,
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

### Tool result

_source line 73 · 2026-05-30T06:14:31.326Z_

<details><summary>↩ Tool result · `toolu_018wNDrP2TJWxkjtWwJJ1kDk`</summary>

```text
Web search results for query: "corpus poisoning dense retrieval attack HOTFLIP embedding space 2024 2025"

Links: [{"title":"Reproducing HotFlip for Corpus Poisoning Attacks in Dense Retrieval | Advances in Information Retrieval","url":"https://dl.acm.org/doi/10.1007/978-3-031-88717-8_8"},{"title":"Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730110"},{"title":"Reproducing HotFlip for Corpus Poisoning Attacks in Dense Retrieval","url":"https://arxiv.org/html/2501.04802v1"},{"title":"GitHub - liyongkang123/hotflip_corpus_poisoning: This is the code repository for our ECIR 2025 reproducibility paper 《Reproducing HotFlip for Corpus Poisoning Attacks in Dense Retrieval》","url":"https://github.com/liyongkang123/hotflip_corpus_poisoning"},{"title":"Reproducing HotFlip for Corpus Poisoning Attacks in Dense Retrieval | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-88717-8_8"},{"title":"Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval","url":"https://arxiv.org/html/2504.17884"},{"title":"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search","url":"https://arxiv.org/html/2412.20953v1"}]

Based on the search results, here's what I found about corpus poisoning and dense retrieval attacks related to HotFlip and embedding spaces in 2024-2025:

## Key Research Findings

**HotFlip Overview:** HotFlip is a topical gradient-based word substitution method for attacking language models that has been applied to attack retrieval systems by generating malicious passages injected into a corpus (corpus poisoning).

**Recent Applications:** HotFlip-based methods are one of the most widely used gradient-based word substitution approaches and serve as a foundational technique for many other approaches in generating adversarial documents.

**2025 Research:** Multiple recent papers address this topic:
- A paper on "Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval" was published at SIGIR 2025
- A reproducibility paper titled "Reproducing HotFlip for Corpus Poisoning Attacks in Dense Retrieval" was published at ECIR 2025

**Computational Challenges:** HotFlip is known to be computationally inefficient, with the majority of time spent on gradient accumulation for each query-passage pair during the adversarial token generation phase.

**Attack Performance:** HotFlip can effectively attack a variety of dense retrievers, with an observed trend that its attack performance diminishes against more advanced and recent methods.

**Related Methods:** GASLITE is a gradient-based method for crafting optimized adversarial passages that shows superiority in retrieval attacks compared to other approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b84129b-bbc7-439d-8732-ff86e87cfa71",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "fc0a3d91-a68d-464b-98bd-0d0f8f306d76",
  "sourceToolAssistantUUID": "5b84129b-bbc7-439d-8732-ff86e87cfa71",
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

_source line 74 · 2026-05-30T06:14:33.145Z_

<details><summary>↩ Tool result · `toolu_01UTRWxtHBUSW3XCGkNs2sAB`</summary>

```text
Web search results for query: "indirect prompt injection RAG retrieval augmented generation attack defense 2024 2025"

Links: [{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"Defending against Indirect Prompt Injection by Instruction Detection","url":"https://arxiv.org/html/2505.06311v2"},{"title":"Indirect Prompt Injection in RAG Systems and AI Agents: The Attack Nobody Sees Coming | AquilaX","url":"https://aquilax.ai/blog/indirect-prompt-injection-rag-agents"},{"title":"Understanding LLM and RAG attacks: From general threats to targeted prompt injection","url":"https://www.cyberbit.com/campaign/llm-rag-attacks-prompt-injections/"},{"title":"CMC | Free Full-Text | Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies","url":"https://www.techscience.com/cmc/v87n1/66084/html"},{"title":"Securing AI Agents Against Prompt Injection Attacks","url":"https://arxiv.org/pdf/2511.15759"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"[2511.15759] Securing AI Agents Against Prompt Injection Attacks","url":"https://arxiv.org/abs/2511.15759"},{"title":"Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms","url":"https://www.mdpi.com/2078-2489/17/1/54"},{"title":"AI Security - The Hidden Attack Surfaces of RAG and MCP | Deconvolute Labs","url":"https://deconvoluteai.com/blog/attack-surfaces-rag"}]

I've found comprehensive research on indirect prompt injection attacks against RAG systems and defense mechanisms from 2024-2025. Here are the key findings:

## Attack Overview

Indirect prompt injection hides malicious instructions in documents, emails, and web pages that AI agents retrieve and process, and unlike direct injection, the user never types the attack payload. In 2023, indirect injection attacks emerged where attackers began leveraging external data sources (webpages, documents, emails) as attack vectors through Retrieval-Augmented Generation (RAG) systems.

Multiple enterprise deployments of RAG-based internal assistants in 2024-2025 were shown to be vulnerable to injection via uploaded documents, with consequences ranging from data leakage to manipulation of the assistant's recommendations.

## Real-World Impact

Prompt injection, especially in RAG or tool-enabled systems, is the dominant real-world exploit vector in 2024–2025, with OWASP's GenAI Top 10 listing Prompt Injection as LLM01:2025. ChatGPT memory exploitation in September 2024 created persistent 'spAIware' injecting malicious instructions into long-term memory that survived across chat sessions via memory RAG context.

## Defense Approaches

Recent research proposes several defense mechanisms:

- Instruction detection methods can defend against attacks by removing documents containing injected instructions before they are passed to the LLM.

- Defense mechanisms include content filtering with embedding-based anomaly detection, hierarchical system prompt guardrails, and multi-stage response verification.

- RAGPart leverages document partitioning to mitigate poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.

- Addressing corpus knowledge poisoning attacks on RAG using sparse attention is another emerging defense approach.

## Detection Challenges

Detecting indirect injection before it executes is genuinely hard because the injected content looks like text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1273c514-cd40-472d-a60c-7709e0c70a96",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "a183b9ab-d2bc-483f-9725-81eb2d27b55b",
  "sourceToolAssistantUUID": "1273c514-cd40-472d-a60c-7709e0c70a96",
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

_source line 75 · 2026-05-30T06:14:38.642Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015Mk1gzobrH92bzCGkqJ9y4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.20953",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a183b9ab-d2bc-483f-9725-81eb2d27b55b",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG9BYaooHU1UJLrFUAJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69ac083c-3db0-4891-a639-12876518fff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbaJG7QLYHXBV7bSpsRQiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 846,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 25198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-30T06:14:38.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gbc59hajVqXFxmi2hKj74n`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.17884",
  "prompt": "Extract the paper title, full author list, submission/publication date, venue, and complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69ac083c-3db0-4891-a639-12876518fff5",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG9BYaooHU1UJLrFUAJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b5ea866-e6ff-4317-88e6-6d91e3f8c701",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbaJG7QLYHXBV7bSpsRQiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 846,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 25198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 77 · 2026-05-30T06:14:42.999Z_

<details><summary>↩ Tool result · `toolu_015Mk1gzobrH92bzCGkqJ9y4`</summary>

```text
# Paper Details

**Title:** "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search"

**Authors:** Matan Ben-Tov and Mahmood Sharif

**Submission Date:** December 30, 2024 (v1); Last revised September 18, 2025 (v2)

**Venue:** ACM CCS 2025

**Abstract:**

The paper examines security weaknesses in dense embedding-based text retrieval systems. Researchers introduced GASLITE, an attack method that "generate[s] adversarial passages" without modifying models or requiring corpus knowledge, yet achieves high ranking in search results. The study evaluated nine advanced retrieval models across multiple threat scenarios, particularly focusing on targeted attacks against concept-specific queries. Key findings indicate retrievers face severe vulnerability to search-engine optimization attacks even at minimal poisoning levels (≥0.0001% of corpus), with effects generalizing across different datasets and query distributions. Single-query attacks were completely successful, and standard defenses proved ineffective against adaptive attacks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69ac083c-3db0-4891-a639-12876518fff5",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "51808467-f60c-4b53-b0db-c01ea8e30b57",
  "sourceToolAssistantUUID": "69ac083c-3db0-4891-a639-12876518fff5",
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

_source line 78 · 2026-05-30T06:14:43.977Z_

<details><summary>↩ Tool result · `toolu_01Gbc59hajVqXFxmi2hKj74n`</summary>

```text
# Paper Information

**Title:** Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval

**Authors:** Yongkang Li, Panagiotis Eustratiadis, Simon Lupart, Evangelos Kanoulas

**Submission/Publication Date:** Submitted April 24, 2025; revised March 16, 2026

**Venue:** SIGIR 2025 (accepted as full paper, oral presentation)

**Abstract:**

This research examines adversarial attacks against dense retrieval systems through corpus poisoning—injecting malicious documents to degrade search ranking performance. The authors address two key gaps in existing work. First, they develop an optimization approach operating directly in embedding space rather than discrete lexical space, training a perturbation model that maintains geometric proximity while maximizing token-level differences. Second, they tackle the harder unsupervised scenario where attackers have no knowledge of query distributions.

The method generates adversarial examples in under two minutes per document—"four times faster compared to the fastest gradient-based word substitution methods"—while producing more natural text with lower perplexity, making detection more difficult. The approach demonstrates effectiveness across white-box and black-box settings on both in-domain and out-of-domain datasets for top-1 attacks and corpus poisoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b5ea866-e6ff-4317-88e6-6d91e3f8c701",
  "isSidechain": true,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "agentId": "af5683602d21c3aad",
  "type": "user",
  "uuid": "84e10028-5d6a-4b80-90db-ff9ccd638c07",
  "sourceToolAssistantUUID": "2b5ea866-e6ff-4317-88e6-6d91e3f8c701",
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

_source line 79 · 2026-05-30T06:16:23.851Z_

I now have comprehensive data on all the key papers. Here is the structured literature survey:

---

## Literature Survey: Adversarial Attacks and Certified Defenses for RAG Systems (2024--2026)

### ATTACK PAPERS

**1. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models**
- **Authors:** Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia
- **Venue:** USENIX Security 2025
- **URL:** https://arxiv.org/abs/2402.07867
- **Why important:** The foundational paper that introduced knowledge-database poisoning attacks against RAG. Achieves 90% attack success rate by injecting only 5 malicious texts into a database of millions. Showed existing defenses are insufficient.
- **Summary:** Formulates corpus poisoning of RAG as an optimization problem with both black-box and white-box solutions, demonstrating that a small number of injected adversarial passages can reliably steer LLM outputs to attacker-chosen answers.

**2. Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation**
- **Authors:** Harsh Chaudhari, Giorgio Severi, John Abascal, Anshuman Suri, Matthew Jagielski, Christopher A. Choquette-Choo, Milad Nasr, Cristina Nita-Rotaru, Alina Oprea
- **Venue:** arXiv (cs.CR), 2024; validated on GPT-3.5/GPT-4 and production systems
- **URL:** https://arxiv.org/abs/2405.20485
- **Why important:** Demonstrates trigger-activated backdoor attacks on RAG systems that cause refusal, reputation damage, privacy violations, and harmful behaviors. Successfully tested on NVIDIA's "Chat with RTX" production system.
- **Summary:** A two-stage optimization crafts a single poisoned document that is retrieved only when specific trigger tokens appear in queries, enabling targeted harmful outputs while evading detection on clean queries.

**3. TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models**
- **Authors:** Pengzhou Cheng, Yidong Ding, Tianjie Ju, Zongru Wu, Wei Du, Ping Yi, Zhuosheng Zhang, Gongshen Liu
- **Venue:** arXiv (cs.CR), 2024
- **URL:** https://arxiv.org/abs/2405.13401
- **Why important:** Proposes a joint backdoor attack using contrastive learning to build orthogonal backdoor shortcuts between poisoned knowledge and triggers, enabling universal attack scenarios.
- **Summary:** Uses knowledge graphs for fine-grained matching to create multiple purpose-driven backdoors that maintain normal retrieval on clean queries while returning semantically consistent poisoned content for adversarial queries.

**4. CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Yuxi Chen, Zhuqing Liu, Lihai Nie, Tong Li, Zheli Liu, Minghong Fang
- **Venue:** ACM SACMAT 2026
- **URL:** https://arxiv.org/abs/2504.03957
- **Why important:** Advances attack practicality by requiring only a single injected poisoned text (vs. 5 in PoisonedRAG), making attacks more feasible and stealthier.
- **Summary:** A practical single-document poisoning attack against RAG systems that achieves higher attack success rates than existing baselines on large-scale datasets.

**5. DisarmRAG: Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning**
- **Authors:** Yanbo Dai, Zhenlan Ji, Zongjie Li, Kuan Li, Shuai Wang
- **Venue:** arXiv (cs.CR), August 2025
- **URL:** https://arxiv.org/abs/2508.20083
- **Why important:** Uniquely targets the retriever model itself (not the corpus), using contrastive learning to modify retriever behavior so it suppresses self-correction mechanisms in RAG. Over 90% attack success rate.
- **Summary:** Compromises the retriever via model editing so it returns malicious instructions for targeted queries while behaving normally otherwise, defeating self-correction and detection defenses.

**6. RIPRAG: Hack a Black-box RAG Question-Answering System with Reinforcement Learning**
- **Authors:** Meng Xi, Sihan Lv, Yechen Jin, Guanjie Cheng, Naibo Wang, Ying Li, Jianwei Yin
- **Venue:** arXiv (cs.AI), October 2025
- **URL:** https://arxiv.org/abs/2510.10008
- **Why important:** First RL-based black-box attack on RAG, treating the target system as a complete black box. Achieves up to 0.72 ASR improvement over baselines.
- **Summary:** Uses reinforcement learning with black-box feedback (similarity and attack rewards) to optimize poisoned document generation without access to model internals.

**7. "Someone Hid It": Query-Agnostic Black-Box Attacks on LLM-Based Retrieval**
- **Authors:** Jiate Li, Defu Cao, Li Li, Wei Yang, Yuehan Qin, Chenxiao Yu, Tiannuo Yang, Ryan A. Rossi, Yan Liu, Xiyang Hu, Yue Zhao
- **Venue:** arXiv (cs.CR), January 2026
- **URL:** https://arxiv.org/abs/2602.00364
- **Why important:** Query-agnostic attack that works without knowing victim queries or models, using zero-shot surrogate LLMs and adversarial learning for transferable injection tokens.
- **Summary:** Formulates transferable attacks on LLM-based retrieval as a min-max optimization problem, generating adversarial tokens that transfer across different LLM retrievers without query knowledge.

**8. GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search**
- **Authors:** Matan Ben-Tov, Mahmood Sharif
- **Venue:** ACM CCS 2025
- **URL:** https://arxiv.org/abs/2412.20953
- **Why important:** Demonstrates that dense retrieval systems are catastrophically vulnerable even at poisoning levels as low as 0.0001% of the corpus. Published at a top security venue.
- **Summary:** Generates adversarial passages without model or corpus knowledge that achieve high rankings; single-query attacks are 100% successful, and standard defenses fail against adaptive versions.

**9. Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval**
- **Authors:** Yongkang Li, Panagiotis Eustratiadis, Simon Lupart, Evangelos Kanoulas
- **Venue:** SIGIR 2025 (Oral)
- **URL:** https://arxiv.org/abs/2504.17884
- **Why important:** Operates in embedding space rather than discrete token space, generating more natural adversarial texts 4x faster than gradient-based methods while being harder to detect (lower perplexity).
- **Summary:** An unsupervised continuous-space optimization approach for corpus poisoning that generates natural-looking adversarial documents effective in both white-box and black-box settings.

**10. Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation**
- **Authors:** Liuji Chen, Xiaofang Yang, Yuanzhuo Lu, Jinghao Zhang, Xin Sun, Qiang Liu, Shu Wu, Jing Dong, Liang Wang
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=nBta7psl5J
- **Why important:** First paper to study multi-adversary competition in RAG poisoning, revealing that single-attacker strategies degrade under competition. Introduces the PoisonArena benchmark.
- **Summary:** Formalizes competitive poisoning scenarios where multiple attackers with conflicting goals target the same queries, showing performance reversals and metric limitations under realistic multi-adversary conditions.

---

### DEFENSE PAPERS

**11. RobustRAG: Certifiably Robust RAG against Retrieval Corruption**
- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal
- **Venue:** arXiv (cs.LG), 2024; affiliations: Princeton, NVIDIA, UC Berkeley
- **URL:** https://arxiv.org/abs/2405.15556
- **Why important:** The first defense framework with formal certified robustness guarantees against retrieval corruption. Reduces PoisonedRAG attack success from >90% to ~10%.
- **Summary:** Uses an isolate-then-aggregate strategy (partitioning passages into disjoint groups, generating responses per group, securely aggregating) with keyword-based and decoding-based algorithms, providing provable lower bounds on response quality against adaptive attackers.

**12. ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search**
- **Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova
- **Venue:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2509.23519
- **Why important:** Extends certified robustness to web-search RAG using graph theory. Incorporates retriever reliability signals (rank, scores) for more principled defense. Published at NeurIPS.
- **Summary:** Models documents as a graph with contradiction edges, finds a Maximum Independent Set (MIS) to identify consistent majority of trustworthy documents, and provides provable robustness guarantees where malicious document selection probability vanishes as retrieval size grows.

**13. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in RAG**
- **Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang
- **Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral)
- **URL:** https://arxiv.org/abs/2512.24268
- **Why important:** Lightweight retrieval-stage defenses that do not require modifying the generation model, making them practical for deployment.
- **Summary:** RAGPart exploits dense retriever training dynamics via document partitioning; RAGMask detects suspicious tokens by measuring similarity shifts under targeted masking. Both reduce attack success while preserving clean-query performance.

**14. RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis**
- **Authors:** Xue Tan, Hao Luan, Mingyu Luo, Xiaoyan Sun, Ping Chen, Jun Dai
- **Venue:** Findings of EMNLP 2025
- **URL:** https://arxiv.org/abs/2411.18948
- **Why important:** Detection-based defense achieving 98% true positive rate with only 1% false positive rate by analyzing LLM internal activation patterns.
- **Summary:** Discovers distinct activation patterns in LLMs when generating correct vs. poisoned responses, building an automated detection pipeline that identifies compromised outputs without modifying the retrieval or generation pipeline.

**15. RAGForensics: Traceback of Poisoning Attacks to Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu
- **Venue:** The Web Conference (WWW) 2025
- **URL:** https://arxiv.org/abs/2504.21668
- **Why important:** First traceback system for RAG that identifies which poisoned texts in the knowledge database caused an attack, enabling post-hoc forensics.
- **Summary:** Iteratively retrieves database subsets and uses crafted prompts to guide an LLM in detecting poisoned texts responsible for attacks, enabling administrators to locate and remove adversarial content.

**16. Understanding Data Poisoning Attacks for RAG: Insights and Algorithms**
- **Authors:** Xun Xian, Tong Wang, Liwen You, Yanjun Qi
- **Venue:** ICLR 2025
- **URL:** https://openreview.net/forum?id=2aL6gcFX7q
- **Why important:** Provides theoretical understanding of why poisoning attacks work (effective along low-variance directions of clean data), yielding both a principled defense (DRS) and a stealthier attack.
- **Summary:** Shows poisoning attacks exploit low-variance directions in the clean data distribution; proposes DRS (Directional Relative Shifts) for defense and a regularized stealthy attack that minimizes detectability.

**17. RbFT: Robust Fine-tuning for Retrieval-Augmented Generation against Retrieval Defects**
- **Authors:** Yiteng Tu, Weihang Su, Yujia Zhou, Yiqun Liu, Qingyao Ai
- **Venue:** arXiv (cs.CL), January 2025
- **URL:** https://arxiv.org/abs/2501.18365
- **Why important:** Fine-tuning-based defense that trains LLMs to be robust against noisy, irrelevant, or counterfactual retrieved content.
- **Summary:** Two targeted fine-tuning tasks strengthen LLMs against retrieval failures, significantly improving robustness across diverse retrieval conditions while maintaining efficiency and compatibility with other defense methods.

**18. Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks**
- **Authors:** Jinyan Su, Jin Peng Zhou, Zhengxin Zhang, Preslav Nakov, Claire Cardie
- **Venue:** arXiv (cs.IR), December 2024
- **URL:** https://arxiv.org/abs/2412.16708
- **Why important:** Systematic evaluation framework with a taxonomy of context types (adversarial, untouched, guiding) and practical mitigation via "skeptical prompting."
- **Summary:** Evaluates multiple retrievers under poisoning, finding that skeptical prompting activates internal LLM reasoning to partially resist adversarial contexts, with effectiveness varying by model capability.

---

### SURVEY / BENCHMARK PAPERS

**19. Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions**
- **Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen
- **Venue:** arXiv (cs.CR / cs.AI), April 2026
- **URL:** https://arxiv.org/abs/2604.08304
- **Why important:** The most recent and comprehensive survey (2026) proposing the SLOT taxonomy for RAG security across a six-stage knowledge pipeline.
- **Summary:** Classifies attack surfaces, defense mechanisms, security objectives (CIA properties), and targets across the full RAG pipeline; identifies structural gaps and recommends realistic threat models, comprehensive defenses, and multimodal evaluation.

**20. Benchmarking Poisoning Attacks against Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Haoran Xin, Jiatong Li, Dongzhe Zhang, Minghong Fang, Zhuqing Liu, Lihai Nie, Zheli Liu
- **Venue:** arXiv (cs.CR), May 2025
- **URL:** https://arxiv.org/abs/2505.18543
- **Why important:** First comprehensive benchmark: 5 QA datasets with 10 variants, 13 attack methods, 7 defenses. Shows attacks degrade on expanded datasets and advanced RAG architectures remain vulnerable.
- **Summary:** Systematic benchmark revealing that current attack effectiveness drops on harder dataset variants, but advanced RAG architectures (sequential, branching, loop, agent-based, multimodal) all remain susceptible, and existing defenses are inadequate.

---

### Key Themes and Takeaways

**Attack evolution (2024-2026):** Attacks have progressed from multi-document corpus poisoning (PoisonedRAG, 5 docs) to single-document attacks (CorruptRAG), black-box RL-based attacks (RIPRAG), query-agnostic transferable attacks, retriever-model poisoning (DisarmRAG), and competitive multi-adversary scenarios (PoisonArena). The attack surface keeps expanding.

**Defense landscape:** Certified defenses (RobustRAG, ReliabilityRAG) provide formal guarantees via isolate-then-aggregate and graph-theoretic approaches. Detection-based defenses (RevPRAG) analyze LLM activations. Retrieval-stage defenses (RAGPart/RAGMask) are lightweight. Forensic methods (RAGForensics) enable post-hoc traceback. However, benchmarking shows current defenses remain inadequate against the full spectrum of attacks.

**Open problems:** Multimodal RAG security, agent-based RAG robustness, realistic multi-adversary threat models, and privacy-preserving defenses remain underexplored.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e10028-5d6a-4b80-90db-ff9ccd638c07",
  "isSidechain": true,
  "agentId": "af5683602d21c3aad",
  "requestId": "req_011CbYG9yybFQ5BiRGfa8R1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6b806fb-a301-4d1d-868e-21f30725a0ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8KJKfqmBASB5ncBvGCqzr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 26332,
      "output_tokens": 4327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4327,
          "cache_read_input_tokens": 26332,
          "cache_creation_input_tokens": 1730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1730,
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
