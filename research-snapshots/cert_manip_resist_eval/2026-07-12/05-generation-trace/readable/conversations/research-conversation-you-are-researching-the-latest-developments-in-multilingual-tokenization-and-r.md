# Research conversation: You are researching the latest developments in multilingual tokenization and reasoning gaps as of early-mid 2026 to ensu

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a45e407b5da2f3af7.jsonl`
- **Structured JSON:** [`f1c7097b7d421e983c09.json`](../../sessions/f1/f1c7097b7d421e983c09.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

69 recorded events

### User

_source line 1 · 2026-05-19T23:31:44.840Z_

You are researching the latest developments in multilingual tokenization and reasoning gaps as of early-mid 2026 to ensure we have the most current landscape.

Research deeply:
1. Any new papers on causal analysis of tokenization effects (beyond Lesci et al.)
2. New multilingual reasoning benchmarks or evaluations in 2026
3. "What Really Controls Temporal Reasoning in LLMs" (arXiv:2603.19017) - what exactly did they find about tokenization fragmentation?
4. New tokenizer designs or approaches in 2026
5. Any work that has already done causal decomposition of multilingual gaps

Search for:
- "causal decomposition multilingual reasoning gap" 2026
- "tokenization fragmentation causal effect reasoning" 2026
- arXiv:2603.19017 "What Really Controls Temporal Reasoning"
- "multilingual reasoning benchmark" 2026 new
- "tokenizer bias causal" 2026 arXiv
- "fertility tokenization accuracy causal" 2026

Use WebFetch to read key papers found. Report what exists and what gaps remain - specifically whether our proposed contribution is still novel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "e40f09ba-3847-47ec-9f86-6bbc39574d6a",
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

_source line 2 · 2026-05-19T23:31:44.844Z_

```json
{
  "parentUuid": "e40f09ba-3847-47ec-9f86-6bbc39574d6a",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
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
  "uuid": "2d7a6cdd-a9bc-4905-aebe-ba474c53fbd6",
  "timestamp": "2026-05-19T23:31:44.844Z",
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

_source line 3 · 2026-05-19T23:31:44.845Z_

```json
{
  "parentUuid": "2d7a6cdd-a9bc-4905-aebe-ba474c53fbd6",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2fd52213-31e4-4d21-bef3-cd823557c3a8",
  "timestamp": "2026-05-19T23:31:44.845Z",
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

_source line 4 · 2026-05-19T23:31:47.720Z_



I'll research the latest developments in multilingual tokenization and reasoning gaps. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fd52213-31e4-4d21-bef3-cd823557c3a8",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLUa7G32hnKtsJZxGe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dafaed7-f5c2-4efd-9fc7-2c07e38da5d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VL3uqcwxHe55C1hQ7nDXxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T23:31:47.873Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nfj95uC6vEn3wHz3G5H7Bv`</summary>

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
  "parentUuid": "3dafaed7-f5c2-4efd-9fc7-2c07e38da5d4",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLUa7G32hnKtsJZxGe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20ec0fe1-e33e-481a-87c7-038db6039db5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VL3uqcwxHe55C1hQ7nDXxd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 7409,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 7409,
          "cache_creation_input_tokens": 1577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1577,
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

_source line 6 · 2026-05-19T23:31:47.876Z_

<details><summary>↩ Tool result · `toolu_01Nfj95uC6vEn3wHz3G5H7Bv`</summary>

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
  "parentUuid": "20ec0fe1-e33e-481a-87c7-038db6039db5",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "e2e471ee-942f-43cc-9b84-b856dbd3de91",
  "sourceToolAssistantUUID": "20ec0fe1-e33e-481a-87c7-038db6039db5",
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

_source line 7 · 2026-05-19T23:31:50.741Z_



Now let me launch multiple searches in parallel to cover all the research areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e471ee-942f-43cc-9b84-b856dbd3de91",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61d8d0a4-a9da-40fe-b2d3-67854aad60c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 8 · 2026-05-19T23:31:51.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C2e5Kjds6JMPvZjK7wLaMa`</summary>

```json
{
  "query": "causal decomposition multilingual reasoning gap tokenization 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61d8d0a4-a9da-40fe-b2d3-67854aad60c2",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24838fb8-e422-408d-83fc-48e0b0c73f83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 9 · 2026-05-19T23:31:51.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D5ZWqdC7p9GZia8bVArNkH`</summary>

```json
{
  "query": "arXiv:2603.19017 \"What Really Controls Temporal Reasoning\" tokenization fragmentation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24838fb8-e422-408d-83fc-48e0b0c73f83",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a1bd539-e641-4241-a03d-d786391669e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 10 · 2026-05-19T23:31:52.141Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R9sS5L1JqPGzyEyaGXfwRV`</summary>

```json
{
  "query": "tokenization fragmentation causal effect reasoning LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a1bd539-e641-4241-a03d-d786391669e0",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6ff58c5-f596-4df7-859f-b0b8837f97a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 11 · 2026-05-19T23:31:52.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VxsZPP8UcGbQeCQKVC2FNx`</summary>

```json
{
  "query": "multilingual reasoning benchmark 2026 new evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ff58c5-f596-4df7-859f-b0b8837f97a5",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d7a388-ec65-4ee6-b459-ab929cc1cbde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 12 · 2026-05-19T23:31:53.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FTLRBcWCGQYweA2JdrNdmd`</summary>

```json
{
  "query": "tokenizer bias causal analysis 2026 arXiv multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d7a388-ec65-4ee6-b459-ab929cc1cbde",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aabb629f-4184-4cda-8789-be91f7fe9f67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 13 · 2026-05-19T23:31:53.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3R2MEDvceeevsayh5MT9G`</summary>

```json
{
  "query": "fertility tokenization accuracy causal 2026 language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aabb629f-4184-4cda-8789-be91f7fe9f67",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoLhn6oTx6dSE1pfd9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30f7af98-6d87-4c11-99b7-6c32f41e6e5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbKuPdEguVEyTu2qKYPXNE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 8986,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 329,
          "cache_read_input_tokens": 8986,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
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

_source line 14 · 2026-05-19T23:31:58.237Z_

<details><summary>↩ Tool result · `toolu_01D5ZWqdC7p9GZia8bVArNkH`</summary>

```text
Web search results for query: "arXiv:2603.19017 "What Really Controls Temporal Reasoning" tokenization fragmentation"

Links: [{"title":"(PDF) What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?","url":"https://www.researchgate.net/publication/402860933_What_Really_Controls_Temporal_Reasoning_in_Large_Language_Models_Tokenisation_or_Representation_of_Time"},{"title":"[2603.19017] What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?","url":"https://arxiv.org/abs/2603.19017"},{"title":"Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/html/2505.16088v1"},{"title":"Date Fragments: A Hidden Bottleneck of Tokenisation for Temporal Reasoning","url":"https://arxiv.org/html/2505.16088v3"},{"title":"[Quick Review] Date Fragments: A Hidden Bottleneck of Tokenization for Temporal\\n Reasoning","url":"https://liner.com/review/date-fragments-hidden-bottleneck-tokenization-for-temporal-reasoning"},{"title":"A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/pdf/2505.16088"},{"title":"[2505.16088] Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/abs/2505.16088"},{"title":"[2505.16088v3] Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/abs/2505.16088v3"},{"title":"(PDF) Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://www.researchgate.net/publication/391992139_Date_Fragments_A_Hidden_Bottleneck_of_Tokenization_for_Temporal_Reasoning"}]

I found information about arXiv:2603.19017 "What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?"

The paper presents MultiTempBench, a multilingual temporal reasoning benchmark spanning three tasks: date arithmetic, time zone conversion, and temporal relation extraction across five languages (English, German, Chinese, Arabic, and Hausa) and multiple calendar conventions (Gregorian, Hijri, and Chinese Lunar).

Regarding tokenization fragmentation specifically, tokenization fragmentation incurs a "token tax," which increases effective sequence length and can degrade downstream performance. The researchers introduce the multilingual Date Fragmentation Ratio (mDFR), calibrated with human severity ratings, and find that tokenisation quality of temporal artefacts is a resource-dependent bottleneck: in low-resource languages and rarer calendar formats, fragmentation becomes particularly problematic.

The research suggests that multilingual temporal failures may be primarily a tokenisation problem, though the paper also conducts internal representation analyses to understand how temporal reasoning works at a mechanistic level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a1bd539-e641-4241-a03d-d786391669e0",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "1b9d9e41-65bf-44ca-92ea-2aeb6d84c953",
  "sourceToolAssistantUUID": "2a1bd539-e641-4241-a03d-d786391669e0",
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

_source line 15 · 2026-05-19T23:31:59.791Z_

<details><summary>↩ Tool result · `toolu_01FTLRBcWCGQYweA2JdrNdmd`</summary>

```text
Web search results for query: "tokenizer bias causal analysis 2026 arXiv multilingual"

Links: [{"title":"Causal Tokenizer","url":"https://www.emergentmind.com/topics/causal-tokenizer"},{"title":"[2506.03149] Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/abs/2506.03149"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/html/2506.03149v1"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/pdf/2506.03149"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486"},{"title":"Tokenization Disparities as Infrastructure Bias: How Subword Systems Create Inequities in LLM Access and Efficiency","url":"https://arxiv.org/html/2510.12389"},{"title":"Beyond Text Compression: Evaluating Tokenizers Across Scales","url":"https://arxiv.org/pdf/2506.03101"}]

Based on the search results, I found several relevant papers on tokenizer bias and causal analysis in multilingual contexts from 2026 arXiv submissions:

## Key Findings

The paper "Causal Estimation of Tokenisation Bias" (arXiv 2506.03149) addresses tokenization bias as a causal effect using regression discontinuity design. The research notes that the choice of tokeniser should ideally not affect the probability assigned to underlying character-strings, but in practice it does—a mismatch defined as tokenisation bias.

The experimental findings show that tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers. The methodology compares similar subwords around a cutoff point to estimate causal effects, revealing that tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers.

## Multilingual Tokenization Bias

Another relevant paper, "The Token Tax: Systematic Bias in Multilingual Tokenization," demonstrates that tokenization inefficiency imposes systematic disadvantages on low-resource, morphologically complex languages. Research confirms systematic tokenization biases favoring high-resource, Latin-script languages, with low-resource languages consistently demonstrating reduced efficiency across all evaluation metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aabb629f-4184-4cda-8789-be91f7fe9f67",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "4d30d56a-fa5b-4d7f-9153-867f6ce3b511",
  "sourceToolAssistantUUID": "aabb629f-4184-4cda-8789-be91f7fe9f67",
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

_source line 16 · 2026-05-19T23:31:59.793Z_

<details><summary>↩ Tool result · `toolu_01VxsZPP8UcGbQeCQKVC2FNx`</summary>

```text
Web search results for query: "multilingual reasoning benchmark 2026 new evaluation"

Links: [{"title":"(PDF) MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs","url":"https://www.researchgate.net/publication/393966027_MultiNRC_A_Challenging_and_Native_Multilingual_Reasoning_Evaluation_Benchmark_for_LLMs"},{"title":"Multilingual MMLU: Global LLM Benchmarking","url":"https://www.emergentmind.com/topics/multilingual-mmlu"},{"title":"Multilingual Benchmarks 2026: MGSM, MMLU-ProX LLM Scores | BenchLM.ai","url":"https://benchlm.ai/multilingual"},{"title":"The Future is Multilingual: A New Evaluation Benchmark","url":"https://scale.com/blog/multinrc"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://arxiv.org/pdf/2504.18428"},{"title":"Scale Labs Leaderboard: MultiNRC | Scale Labs","url":"https://labs.scale.com/leaderboard/multinrc"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"xSTREET: Multilingual structured reasoning and explanation benchmark - Amazon Science","url":"https://www.amazon.science/code-and-datasets/xstreet-multilingual-structured-reasoning-and-explanation-benchmark"},{"title":"MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs","url":"https://arxiv.org/pdf/2507.17476"}]

Based on the search results, here are the key findings about multilingual reasoning benchmarks in 2026:

## Major New Benchmarks

MultiNRC (Multilingual Native Reasoning Challenge) is a new multilingual evaluation benchmark that contains native and challenging reasoning questions of the targeted language, to assess LLMs' reasoning capability under a natural and native context. MultiNRC is the first benchmark of its kind to be constructed natively by speakers of multiple languages, representing a fundamental shift away from the common practice of simply translating existing English problems.

Current popular multilingual mathematical datasets, such as MGSM and XSVAMP, are too simple to evaluate the reasoning capabilities of advanced LLMs effectively, making that multilingual mathematical reasoning benchmarks have not kept pace with the progress in LLM reasoning abilities, as most advanced and challenging benchmarks are available only in English.

Multilingual MMLU is a comprehensive evaluation framework that adapts MMLU benchmarks to multiple languages while preserving cultural and linguistic nuances.

## Key Findings and Challenges

Current LLMs are still not good at native multilingual reasoning, with none scoring above 50% on MultiNRC, and most models perform substantially better in math reasoning in English compared to in original languages (+10%), indicating persistent challenges with culturally grounded knowledge.

Multilingual reasoning evaluation reveals that reasoning performance varies widely across languages for current LLMs, input-output language consistency is low in reasoning LLMs, and thinking length differs significantly by language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d7a388-ec65-4ee6-b459-ab929cc1cbde",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "f4e3105a-a1a2-4691-8d1d-864ed70f5d1b",
  "sourceToolAssistantUUID": "92d7a388-ec65-4ee6-b459-ab929cc1cbde",
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

_source line 17 · 2026-05-19T23:31:59.797Z_

<details><summary>↩ Tool result · `toolu_01M3R2MEDvceeevsayh5MT9G`</summary>

```text
Web search results for query: "fertility tokenization accuracy causal 2026 language model"

Links: [{"title":"How LLM Tokenization Actually Works Under the Hood | Let's Data Science","url":"https://letsdatascience.com/blog/tokenization-deep-dive-why-it-matters-more-than-you-think"},{"title":"Causal Tokenizer","url":"https://www.emergentmind.com/topics/causal-tokenizer"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"Frontiers | Tokenization efficiency of current foundational large language models for the Ukrainian language","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1538165/full"},{"title":"No Translation Needed: Forecasting Quality from Fertility and Metadata","url":"https://arxiv.org/pdf/2509.05425"},{"title":"No Text Needed: Forecasting MT Quality and Inequity from Fertility and Metadata","url":"https://arxiv.org/html/2509.05425"},{"title":"Understanding Token Fertility: Why It Matters for Multilingual LLMs | by Biswajit | Medium","url":"https://medium.com/@biswanai92/understanding-token-fertility-why-it-matters-for-multilingual-llms-38c0b9f20da2"},{"title":"Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation","url":"https://arxiv.org/pdf/2510.09947"},{"title":"[2509.05425] No Text Needed: Forecasting MT Quality and Inequity from Fertility and Metadata","url":"https://arxiv.org/abs/2509.05425"}]

Based on the search results, here are the key findings regarding fertility, tokenization accuracy, and causal relationships in language models:

## Fertility and Accuracy Relationship

Research shows fertility explains 20-50% of the variance in model accuracy across languages. More specifically, slopes range from −0.08 to −0.18, meaning each additional token per word reduces accuracy by 8-18 percentage points, depending on subject and model.

## Causal Tokenization Approaches

Recent research explores causal methodologies for understanding tokenization impacts. Advances in causal inference methodologies enable the precise estimation of tokenization bias—the effect of a token's inclusion (or exclusion) on model outputs, with methods such as regression discontinuity design. Additionally, empirical studies reveal that varying tokenization strategies can introduce up to a 9% accuracy gap and significantly affect computational cost in large language models.

## Recent 2026 Findings

Translation quality can be predicted using token fertility ratios, token counts, and basic linguistic metadata across 203 languages in the FLORES-200 benchmark, with gradient boosting models achieving favorable performance (R²=0.66 for XX→English and R²=0.72 for English→XX).

## Limitations of Fertility as a Metric

However, despite its wide adoption, fertility has important blind spots as a token-level average, and its link to downstream LLM performance remains unclear.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30f7af98-6d87-4c11-99b7-6c32f41e6e5b",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "ec91b239-50b1-4003-8afa-3ce058af8716",
  "sourceToolAssistantUUID": "30f7af98-6d87-4c11-99b7-6c32f41e6e5b",
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

_source line 18 · 2026-05-19T23:31:59.800Z_

<details><summary>↩ Tool result · `toolu_01R9sS5L1JqPGzyEyaGXfwRV`</summary>

```text
Web search results for query: "tokenization fragmentation causal effect reasoning LLM 2026"

Links: [{"title":"Scaling AI: Solving the Infrastructure Fragmentation of LLM Reasoning • Dev|Journal","url":"https://earezki.com/ai-news/2026-04-24-why-llm-reasoning-is-breaking-ai-infrastructure-and-how-to-fix-it/"},{"title":"Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/html/2505.16088v1"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/html/2601.14658v1"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.14658"},{"title":"Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits","url":"https://arxiv.org/pdf/2505.14178"},{"title":"A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/pdf/2505.16088"}]

Based on the search results, here's what recent research has found about tokenization fragmentation and its causal effects on LLM reasoning:

## Key Findings on Tokenization Fragmentation

The fragmentation ratio generally correlates with temporal reasoning performance, with more fragmented tokenization correlating with worse reasoning performance. Excessive fragmentation correlates with accuracy drops of up to 10 points on uncommon dates like historical and futuristic dates.

Manipulating digit-grouping tokenizations reveal substantial accuracy shifts and altered error distributions in state-of-the-art LLMs, indicating that model "reasoning" frequently adheres to tokenizer-imposed structure rather than learned abstract computational principles.

## How LLMs Handle Fragmented Tokens

LLMs "heal" fragmented date embeddings in their layer stack through an emergent ability termed date abstraction, with larger models quickly compensating for date fragmentation to achieve high accuracy of temporal reasoning at early layers.

## Broader Impact on Reasoning

Token structure dramatically affects reasoning performance, causing failure even with Chain-of-Thought prompting, while atomically-aligned formats unlock strong generalization, allowing small models to outperform larger systems in structured reasoning.

The technical reality of LLM reasoning involves fragmented landscapes where providers use different token budgets and output schemas, leading to unpredictable token usage and billing inconsistencies that prevent effective scaling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6ff58c5-f596-4df7-859f-b0b8837f97a5",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "7771829f-fe2c-42d4-a232-e1083681b52b",
  "sourceToolAssistantUUID": "d6ff58c5-f596-4df7-859f-b0b8837f97a5",
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

_source line 19 · 2026-05-19T23:32:00.509Z_

<details><summary>↩ Tool result · `toolu_01C2e5Kjds6JMPvZjK7wLaMa`</summary>

```text
Web search results for query: "causal decomposition multilingual reasoning gap tokenization 2026 arXiv"

Links: [{"title":"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners","url":"https://arxiv.org/pdf/2505.15257"},{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/html/2510.27269v3"},{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/pdf/2510.27269"},{"title":"[2510.27269] Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/abs/2510.27269"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486v1"},{"title":"Causal Tokenizer","url":"https://www.emergentmind.com/topics/causal-tokenizer"},{"title":"What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features","url":"https://arxiv.org/pdf/2604.04720"},{"title":"Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning","url":"https://arxiv.org/html/2505.16088v1"}]

I found several relevant 2026 arXiv papers related to your search query. Here are the key findings:

## Main Research Papers

**1. "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners"** (arXiv:2505.15257)

This work performs causal intervention by removing language-specific components from hidden representations, evaluated across 10 open-source LLMs and 3 multilingual reasoning benchmarks. Results show consistent performance improvements, supporting the claim that disentangling language and reasoning enhances multilingual generalization.

**2. "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?"** (arXiv:2510.27269, updated April 13, 2026)

This work shows that the multilingual reasoning gap primarily stems from failures in language understanding—specifically, the model's inability to translate multilingual inputs into the language dominating its reasoning traces (typically English). The researchers use token-probability signals and other detection methods, with supervised approaches performing best at detecting understanding failures. They propose Selective Translation, which incorporates an English translation into the initial reasoning trace only when an understanding failure is detected.

**3. "The Token Tax: Systematic Bias in Multilingual Tokenization"** (arXiv:2509.05486)

Tokenization inefficiency imposes structural disadvantages on morphologically complex, low-resource languages, inflating compute resources and depressing accuracy. The research evaluated 10 large language models on multilingual benchmarks and shows that fertility (tokens/word) reliably predicts accuracy, with higher fertility consistently predicting lower accuracy.

These papers collectively address causal analysis, multilingual reasoning gaps, and tokenization's role in performance disparities across languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24838fb8-e422-408d-83fc-48e0b0c73f83",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "629a8ac5-d0b1-4109-ba77-78619633f5c2",
  "sourceToolAssistantUUID": "24838fb8-e422-408d-83fc-48e0b0c73f83",
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

_source line 20 · 2026-05-19T23:32:04.485Z_

Excellent findings. Now let me fetch the key papers in detail to understand exactly what has been done and identify remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629a8ac5-d0b1-4109-ba77-78619633f5c2",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoMdgpNHarmWUNXVspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2637b142-111e-4f45-9bfb-bdd18319ea68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpsYQedaZb2Q9qvaVfWBeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3714,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 10118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 21 · 2026-05-19T23:32:06.755Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018MMkmroSZhXzmCfJNLWwgB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19017",
  "prompt": "Extract the full details of this paper: title, authors, date, abstract, key findings about tokenization fragmentation vs representation of time, the multilingual Date Fragmentation Ratio (mDFR), what they found about causal effects of tokenization on temporal reasoning, their experimental methodology, and their main conclusions. What exactly did they find about tokenization fragmentation's role?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2637b142-111e-4f45-9bfb-bdd18319ea68",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoMdgpNHarmWUNXVspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52838e75-39dd-4c91-b9c1-ab70c1937522",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpsYQedaZb2Q9qvaVfWBeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3714,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 10118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 22 · 2026-05-19T23:32:08.665Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VeLccz3uGEBfDz59X85umG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.03149",
  "prompt": "Extract the full details of this paper: title, authors, date, abstract, methodology (regression discontinuity design), what causal effects of tokenization they measured, which languages/tasks they tested on, key quantitative findings, and conclusions. How does this relate to multilingual reasoning specifically? What gaps remain in their analysis?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52838e75-39dd-4c91-b9c1-ab70c1937522",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoMdgpNHarmWUNXVspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fb28695-cef5-470c-a3ab-2637eebe4d5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpsYQedaZb2Q9qvaVfWBeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3714,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 10118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 23 · 2026-05-19T23:32:10.574Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KkXgxtn4bRpnDnRioVxkDU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27269",
  "prompt": "Extract full details: title, authors, date, abstract, methodology, key findings about why multilingual reasoning gaps emerge, what role tokenization plays in their analysis, what their Selective Translation approach does, and quantitative results. Does this paper do causal decomposition of the gap?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb28695-cef5-470c-a3ab-2637eebe4d5f",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoMdgpNHarmWUNXVspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e34997e7-eda3-4a98-9ed1-f0b448694ff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpsYQedaZb2Q9qvaVfWBeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3714,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 10118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 24 · 2026-05-19T23:32:12.005Z_

<details><summary>↩ Tool result · `toolu_018MMkmroSZhXzmCfJNLWwgB`</summary>

```text
# Research Paper Summary: Temporal Reasoning in LLMs

**Title:** "What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?"

**Authors:** Gagan Bhatia, Ahmad Muhammad Isa, Maxime Peyrard, Wei Zhao

**Submission Date:** March 19, 2026

## Abstract Overview

The researchers introduced MultiTempBench, a benchmark evaluating how well 20 large language models handle temporal reasoning across multiple languages and calendar systems. The study examined three core tasks: date arithmetic, time zone conversion, and temporal relation extraction.

## Key Findings on Tokenization Fragmentation

The research discovered that **tokenization quality acts as a resource-dependent limiting factor**. Specifically:

- In low-resource languages and uncommon calendar formats, fragmentation of date tokens disrupts the separation of Year/Month/Day components, causing accuracy to decline significantly
- High-resource language settings generally remain robust despite digit-level token splitting

## The mDFR Metric

They introduced the **multilingual Date Fragmentation Ratio (mDFR)**, calibrated against human severity assessments, to measure how temporal artifacts break apart during tokenization.

## Causal Mechanism Findings

Through crossed mixed-effects regression analysis, they identified distinct patterns:

- **High-resource languages:** temporal linearity (how models represent time sequentially) emerged as the strongest accuracy predictor
- **Low-resource languages:** fragmentation became the dominant factor determining performance

## Conclusion

The study reveals that **neither tokenization nor representation alone fully explains temporal reasoning**—rather, their relative importance depends on language resources available during model training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52838e75-39dd-4c91-b9c1-ab70c1937522",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "e453ba2f-2a00-4875-95d4-1fe8e88d2932",
  "sourceToolAssistantUUID": "52838e75-39dd-4c91-b9c1-ab70c1937522",
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

_source line 25 · 2026-05-19T23:32:12.344Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G5heLkfuxmNGJTdPTa1hMc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15257",
  "prompt": "Extract full details: title, authors, date, abstract, methodology for language-reasoning disentanglement, what causal interventions they perform, key findings about multilingual reasoning, and how they separate language from reasoning. Does this paper do causal decomposition of the multilingual gap? What is their methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e453ba2f-2a00-4875-95d4-1fe8e88d2932",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoMdgpNHarmWUNXVspH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92447bbe-7a33-4569-96b6-53a8907d5317",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpsYQedaZb2Q9qvaVfWBeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3714,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 10118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 26 · 2026-05-19T23:32:15.593Z_

<details><summary>↩ Tool result · `toolu_01VeLccz3uGEBfDz59X85umG`</summary>

```text
# Paper Analysis: Causal Estimation of Tokenisation Bias

## Core Details
**Title:** Causal Estimation of Tokenisation Bias  
**Authors:** Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, Tiago Pimentel  
**Date:** Submitted June 3, 2025  
**Status:** Published at ACL 2025

## Abstract Summary
The paper addresses how tokenizer choice affects language model probability assignments. The researchers note that while models train on subword sequences, they ultimately assign probabilities to character strings. They define this mismatch as "tokenisation bias" and specifically measure how including or excluding a subword from the vocabulary affects the probability assigned to corresponding characters.

## Methodology
The authors employ **regression discontinuity design (RDD)** as their causal estimation approach. Their key innovation exploits how tokenization algorithms rank subwords and add the top K entries to vocabulary at an arbitrary cutoff point. By comparing similar subwords near this cutoff boundary, they isolate causal effects while working around the constraint that each model trains with only one tokenizer.

## Measured Effects
The research quantifies how tokenizer vocabulary membership causally affects character-level probability assignments, finding that "a subword's presence in a small model's vocabulary may increase its characters' probability by up to 17 times."

## Experimental Scope
**Limitation:** The provided content does not specify which languages, tasks, or datasets the experiments covered. The abstract mentions testing "across scales, vocabularies, and tokenisers" without specifying multilingual evaluation.

## Key Findings
Tokenization "consistently affects models' outputs across scales, vocabularies, and tokenisers," establishing it as "a key design choice in language modelling."

## Gaps for Multilingual Analysis
The content reveals no explicit multilingual testing, cross-lingual transfer effects, or language-specific tokenization bias patterns—significant gaps for understanding how these biases manifest across linguistic diversity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fb28695-cef5-470c-a3ab-2637eebe4d5f",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "8406ccb1-8c15-4f17-b710-b32c9f2aadb8",
  "sourceToolAssistantUUID": "3fb28695-cef5-470c-a3ab-2637eebe4d5f",
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

_source line 27 · 2026-05-19T23:32:16.270Z_

<details><summary>↩ Tool result · `toolu_01KkXgxtn4bRpnDnRioVxkDU`</summary>

```text
# Paper Analysis: Multilingual Reasoning Gaps in Language Models

**Title:** Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?

**Authors:** Deokhyung Kang, Seonjeong Hwang, Daehui Kim, Hyounghun Kim, Gary Geunbae Lee

**Date:** Submitted October 31, 2025; final version April 13, 2026

**Acceptance:** Findings of ACL 2026

## Abstract Summary

The researchers investigate why reasoning language models perform worse in low-resource languages than high-resource ones. They identify that "this gap primarily stems from failures in language understanding" rather than reasoning capability itself.

## Key Findings

**Root Cause:** The models struggle to translate multilingual inputs into English, the language dominating their internal reasoning chains.

**Detection Methods:** The team evaluated multiple approaches to identify understanding failures, finding that "supervised approaches performing best" at meaningful detection rates.

**Selective Translation Approach:** Rather than always translating inputs, their method "incorporates an English translation into the initial reasoning trace only when an understanding failure is detected."

**Quantitative Results:** Using Qwen3-4B, Selective Translation achieved "near full-translation performance while translating only about 20% of inputs."

## Tokenization Role

The document does not explicitly discuss tokenization's role in their analysis.

## Causal Decomposition

The paper does not employ formal causal decomposition methodology—instead, it uses diagnostic detection methods to identify and isolate understanding failures as the primary gap driver.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e34997e7-eda3-4a98-9ed1-f0b448694ff1",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "d0282621-dd2f-42e5-a2dc-c7379aff8cc9",
  "sourceToolAssistantUUID": "e34997e7-eda3-4a98-9ed1-f0b448694ff1",
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

_source line 28 · 2026-05-19T23:32:19.105Z_

<details><summary>↩ Tool result · `toolu_01G5heLkfuxmNGJTdPTa1hMc`</summary>

```text
# Paper Summary: Language-Reasoning Disentanglement in Multilingual LLMs

**Title:** "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners"

**Authors:** Weixiang Zhao, Jiahe Guo, Yang Deng, Tongtong Wu, Wenxuan Zhang, Yulin Hu, Xingyu Sui, Yanyan Zhao, Wanxiang Che, Bing Qin, Tat-Seng Chua, Ting Liu

**Submission Date:** May 21, 2025 (revised December 11, 2025)

**Venue:** NeurIPS 2025

## Core Hypothesis & Methodology

The researchers propose that "reasoning functions largely independently of language processing" in LLMs, similar to cognitive neuroscience findings in humans. Their methodology involves **causal intervention through ablation** of language-specific representations during inference (not training).

## Causal Intervention Approach

Rather than traditional causal decomposition of the multilingual gap, they use **inference-time ablation** to disentangle components. By removing language-specific representations while preserving reasoning mechanisms, they test whether this improves cross-lingual performance.

## Key Findings

- Language-specific ablation "consistently boosts multilingual reasoning performance" across 10 open-weight LLMs and 11 typologically diverse languages
- Layer-wise analysis confirms language and reasoning representations are separable throughout the model
- Preserving top-layer language features remains crucial for linguistic fidelity
- This training-free approach achieves "comparable or superior results" versus supervised fine-tuning and reinforcement learning

**Distinction:** This is intervention-based analysis rather than formal causal decomposition of the multilingual gap itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92447bbe-7a33-4569-96b6-53a8907d5317",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "f8b76f26-c455-44ab-947a-522e379105d8",
  "sourceToolAssistantUUID": "92447bbe-7a33-4569-96b6-53a8907d5317",
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

_source line 29 · 2026-05-19T23:32:21.856Z_

Now let me fetch additional key papers to get the complete picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b76f26-c455-44ab-947a-522e379105d8",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoP12z3xd1rEwWRmXAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9b5a1a4-84d8-4a26-a222-31bfa111eeb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHnNBZMqbZWeLCEWiVerv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5969,
      "cache_read_input_tokens": 11251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5969,
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

_source line 30 · 2026-05-19T23:32:23.499Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012P9Abve7rSSSxLfVFhA6KA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.14658",
  "prompt": "Extract full details: title, authors, date, abstract, key findings about how tokenizers betray reasoning in LLMs. What specific causal mechanisms do they identify? What tasks and languages did they test? What are the key quantitative results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9b5a1a4-84d8-4a26-a222-31bfa111eeb6",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoP12z3xd1rEwWRmXAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e379951f-476a-4f58-82ef-1ae60ad5a14e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHnNBZMqbZWeLCEWiVerv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5969,
      "cache_read_input_tokens": 11251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5969,
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

_source line 31 · 2026-05-19T23:32:25.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WhMiAXpyk4TQJeJ2V1BWN8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04720",
  "prompt": "Extract full details: title, authors, date, abstract, methodology for disentangling reasoning traces with measurable features. What features do they measure? How do they decompose multilingual reasoning? Does this paper do causal decomposition? Key findings and what gaps remain?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e379951f-476a-4f58-82ef-1ae60ad5a14e",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoP12z3xd1rEwWRmXAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a89e0ed5-7e58-4bcd-b1c9-1bdcdd56090e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHnNBZMqbZWeLCEWiVerv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5969,
      "cache_read_input_tokens": 11251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5969,
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

_source line 32 · 2026-05-19T23:32:26.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ojsMh831xT2P53fjfAkv4`</summary>

```json
{
  "query": "\"Say Anything but This\" tokenizer betrays reasoning LLMs 2601.14658 findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a89e0ed5-7e58-4bcd-b1c9-1bdcdd56090e",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoP12z3xd1rEwWRmXAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd337f0e-8bd7-4184-846b-4c751a91e78f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHnNBZMqbZWeLCEWiVerv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5969,
      "cache_read_input_tokens": 11251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5969,
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

_source line 33 · 2026-05-19T23:32:26.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qcs1D8uNRB5swiRUvJPWBo`</summary>

```json
{
  "query": "new tokenizer design 2026 multilingual improved BPE alternative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd337f0e-8bd7-4184-846b-4c751a91e78f",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoP12z3xd1rEwWRmXAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7abcbee1-1136-44ad-8969-c8f07a4aed55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfHnNBZMqbZWeLCEWiVerv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5969,
      "cache_read_input_tokens": 11251,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5969
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 374,
          "cache_read_input_tokens": 11251,
          "cache_creation_input_tokens": 5969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5969,
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

_source line 34 · 2026-05-19T23:32:29.326Z_

<details><summary>↩ Tool result · `toolu_012P9Abve7rSSSxLfVFhA6KA`</summary>

```text
# Research Paper Summary: Tokenizer Betrayal in LLMs

**Title:** "Say Anything but This: When Tokenizer Betrays Reasoning in LLMs"

**Authors:** Navid Ayoobi, Marcus I Armstrong, Arjun Mukherjee

**Date:** Submitted January 21, 2026

---

## Abstract Overview

The researchers investigate how tokenization undermines LLM reasoning. They note that "multiple token ID sequences can detokenize to identical surface strings," creating representational mismatches that cause models to treat semantically identical text as distinct.

---

## Key Causal Mechanisms Identified

The paper identifies eight systematic tokenizer artifacts causing reasoning failures:

1. **One-to-many mappings** – Multiple token sequences produce identical text outputs
2. **Whitespace-boundary shifts** – Tokenizers mishandle spaces between words
3. **Intra-word resegmentation** – Subword boundaries shift incorrectly within terms

The core mechanism involves "phantom edits" where models appear to reason correctly but operate "under the illusion of correct reasoning" due to tokenizer-induced representational defects.

---

## Methodology & Testing

**Task:** A tokenization-consistency probe requiring models to "replace designated target words in context while leaving all other content unchanged"

**Scale:** Over 11,000 replacement trials across state-of-the-art open-source LLMs

**Language:** The content provided doesn't specify which languages were tested.

---

## Key Quantitative Results

The paper reports "a non-trivial rate of outputs exhibit phantom edits," though the specific percentage isn't stated in this excerpt. The researchers found systematic patterns rather than isolated failures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e379951f-476a-4f58-82ef-1ae60ad5a14e",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "70241502-2eb0-41ab-88c9-a640b64475de",
  "sourceToolAssistantUUID": "e379951f-476a-4f58-82ef-1ae60ad5a14e",
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

_source line 35 · 2026-05-19T23:32:31.247Z_

<details><summary>↩ Tool result · `toolu_01WhMiAXpyk4TQJeJ2V1BWN8`</summary>

```text
# Paper Analysis: Multilingual Reasoning Features

## Title & Metadata
**Title:** "What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features"

**Authors:** Dayeon Ki, Kevin Duh, Marine Carpuat

**Submission Date:** April 6, 2026

**arXiv ID:** 2604.04720

---

## Abstract Summary
The authors challenge the assumption that closing English-other language performance gaps requires making all reasoning resemble English patterns. They ask what actually enables effective multilingual reasoning.

---

## Methodology: Three-Pronged Approach

**1. Feature Definition & Statistical Analysis**
The team created "a suite of measurable reasoning features" across three dimensions:
- Multilingual alignment aspects
- Reasoning step components
- Reasoning flow patterns

They applied logistic regression to quantify feature-accuracy associations.

**2. Latent Concept Discovery**
They trained sparse autoencoders on multilingual traces to automatically uncover hidden reasoning concepts that instantiate or extend their defined features.

**3. Test-Time Steering**
Features served as selection policies to guide models toward stronger multilingual reasoning.

---

## Key Findings

The research reveals that while most features show positive accuracy associations, strength varies dramatically across languages and "can even reverse in some." This directly contradicts English-centric approaches.

---

## Causal Decomposition?

The document doesn't explicitly discuss causal decomposition. The methodology appears correlational (using logistic regression) rather than interventional.

---

## Scope & Gaps

**Evaluated on:** Two mathematical reasoning benchmarks, four Large Reasoning Models, ten languages

**Remaining gaps:** The paper suggests need for "adaptive objectives that accommodate language-specific reasoning patterns" rather than universal designs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a89e0ed5-7e58-4bcd-b1c9-1bdcdd56090e",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "50500b62-2a2c-4965-b2b1-1557ffd2b176",
  "sourceToolAssistantUUID": "a89e0ed5-7e58-4bcd-b1c9-1bdcdd56090e",
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

_source line 36 · 2026-05-19T23:32:33.431Z_

<details><summary>↩ Tool result · `toolu_013ojsMh831xT2P53fjfAkv4`</summary>

```text
Web search results for query: ""Say Anything but This" tokenizer betrays reasoning LLMs 2601.14658 findings"

Links: [{"title":"[2601.14658] Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/abs/2601.14658"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/html/2601.14658v1"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.14658"},{"title":"Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits","url":"https://arxiv.org/pdf/2505.14178"},{"title":"Process or Result? Manipulated Ending Tokens Can Mislead Reasoning LLMs   to Ignore the Correct Reasoning Steps","url":"https://arxiv.org/pdf/2503.19326"}]

Based on the search results, here are the key findings from the paper "Say Anything but This: When Tokenizer Betrays Reasoning in LLMs" (arXiv:2601.14658):

## Main Problem

Modern subword tokenizers routinely produce non-unique encodings where multiple token ID sequences can detokenize to identical surface strings. LLMs may treat two internal representations as distinct "words" even when they are semantically identical at the text level.

## Methodology

The researchers introduced a tokenization-consistency probe that requires models to replace designated target words in context while leaving all other content unchanged.

## Key Findings

Through analysis of over 11000 replacement trials across state-of-the-art open-source LLMs, the researchers found a non-trivial rate of outputs exhibiting "phantom edits" - cases where models operate under the illusion of correct reasoning, arising from tokenizer-induced representational defects.

The researchers identified a taxonomy of eight systematic tokenizer artifacts, including whitespace-boundary shifts and intra-word resegmentation.

## Implications

These findings indicate that part of apparent reasoning deficiency originates in the tokenizer layer, motivating tokenizer-level remedies before incurring the cost of training ever-larger models on ever-larger corpora.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd337f0e-8bd7-4184-846b-4c751a91e78f",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "cef6b78e-85c5-4eee-b2be-86e88d3776c2",
  "sourceToolAssistantUUID": "bd337f0e-8bd7-4184-846b-4c751a91e78f",
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

_source line 37 · 2026-05-19T23:32:35.478Z_

<details><summary>↩ Tool result · `toolu_01Qcs1D8uNRB5swiRUvJPWBo`</summary>

```text
Web search results for query: "new tokenizer design 2026 multilingual improved BPE alternative"

Links: [{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design","url":"https://arxiv.org/html/2511.03237"},{"title":"IndicSuperTokenizer: An Optimized Tokenizer for Indic Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=CSrGFB070m"},{"title":"[2511.03237] MUTANT: A Recipe for Multilingual Tokenizer Design","url":"https://arxiv.org/abs/2511.03237"},{"title":"IndicSuperTokenizer: An Optimized Tokenizer for Indic Multilingual LLMs","url":"https://arxiv.org/html/2511.03237v1"},{"title":"Language-Specific Tokenizer Design","url":"https://www.emergentmind.com/topics/language-specific-tokenizer-design"},{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design","url":"https://arxiv.org/pdf/2511.03237"},{"title":"Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models","url":"https://arxiv.org/html/2512.03989v2"}]

I found relevant results about new multilingual tokenizer designs from 2026. Here are the key findings:

## Recent Multilingual Tokenizer Designs

MUTANT is a recipe for building multilingual tokenizers, featuring careful vocabulary and training data design, language-aware pre-tokenization, and subword and multiword aware training. Evaluated across English, 22 Indian languages and code data, the MUTANT tokenizer improves the average fertility score by 39.5% over LLaMA4 and by 18% over Sutra (the current best), translating to 44% improvement in inference throughput over LLaMA4.

## BPE Alternatives and Improvements

While alternate sub-word tokenization algorithms like WordPiece and Unigram LM have been explored, Byte Pair Encoding (BPE) remains the most widely adopted. However, recent improvements to BPE have emerged: PickyBPE discards uninformative merges to improve vocabulary utility, while Scaffold-BPE iteratively prunes low-frequency scaffold tokens to reduce imbalance and enhance downstream performance. SuperBPE expands beyond word boundaries, jointly learning subwords and multi-words yielding improved compression and inference efficiency in a 2-stage curriculum.

## Language-Specific Approaches

Unigram-LM uses EM to prune subword candidates from a seed vocabulary, modeling latent segmentations; it better preserves morphological boundaries and can be tuned for low-resource scenarios. Additionally, LiB (Less-is-Better) merges and prunes according to cognitive cost reduction, facilitating autonomous discovery of subwords, words, and MWEs with balanced token/type counts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7abcbee1-1136-44ad-8969-c8f07a4aed55",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "2b3d1697-ea19-474e-9b69-d515df8f8ef5",
  "sourceToolAssistantUUID": "7abcbee1-1136-44ad-8969-c8f07a4aed55",
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

_source line 38 · 2026-05-19T23:32:37.720Z_

Let me now search for a few more specific items to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b3d1697-ea19-474e-9b69-d515df8f8ef5",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoQD2q1Tzq7fmEySWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5db2c768-d6be-46a3-91e8-fc74fcb4d004",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FprtnuCKqkKpUvdfngG1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 17220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 39 · 2026-05-19T23:32:38.657Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S1WhYuBwm8VorYxXiygXU4`</summary>

```json
{
  "query": "Lesci et al \"Causal Estimation of Tokenisation Bias\" ACL 2025 multilingual reasoning decomposition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5db2c768-d6be-46a3-91e8-fc74fcb4d004",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoQD2q1Tzq7fmEySWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ce5cec9-c4fd-4c2f-b3a2-a7e9c7fc5d63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FprtnuCKqkKpUvdfngG1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 17220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 40 · 2026-05-19T23:32:39.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GmDc8gXW7cDzThxdjejMxn`</summary>

```json
{
  "query": "\"Token Tax\" arXiv 2509.05486 multilingual tokenization systematic bias causal findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ce5cec9-c4fd-4c2f-b3a2-a7e9c7fc5d63",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoQD2q1Tzq7fmEySWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bc774b3-2e05-4b73-b85a-4277dd93543a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FprtnuCKqkKpUvdfngG1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 17220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 41 · 2026-05-19T23:32:40.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UgYwcHMNBbY2FGWXKs4Fv9`</summary>

```json
{
  "query": "MultiNRC multilingual reasoning benchmark 2026 scale labs evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bc774b3-2e05-4b73-b85a-4277dd93543a",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoQD2q1Tzq7fmEySWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7072d51e-3ccc-4013-a4f2-9f9323db29dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FprtnuCKqkKpUvdfngG1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 17220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 42 · 2026-05-19T23:32:40.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014LkuXnw7GvN5gVc8ScUPvA`</summary>

```json
{
  "query": "PolyMath multilingual mathematical reasoning benchmark 2026 arXiv evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7072d51e-3ccc-4013-a4f2-9f9323db29dd",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoQD2q1Tzq7fmEySWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f2d3246-6433-4710-a626-dae1f2222f1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FprtnuCKqkKpUvdfngG1zr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 17220,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2559
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 17220,
          "cache_creation_input_tokens": 2559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2559,
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

_source line 43 · 2026-05-19T23:32:45.618Z_

<details><summary>↩ Tool result · `toolu_01GmDc8gXW7cDzThxdjejMxn`</summary>

```text
Web search results for query: ""Token Tax" arXiv 2509.05486 multilingual tokenization systematic bias causal findings"

Links: [{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/token-tax-systematic-bias-multilingual-tokenization"},{"title":"[2509.05486] The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/abs/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486v1"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://chatpaper.com/ja/chatpaper/paper/186756"},{"title":"(PDF) The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://www.researchgate.net/publication/395355055_The_Token_Tax_Systematic_Bias_in_Multilingual_Tokenization"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization - ACL Anthology","url":"https://aclanthology.org/2026.africanlp-main.10/"},{"title":"Natural Language Processing Papers on X: \"The Token Tax: Systematic Bias in Multilingual Tokenization. https://t.co/XXFdvS3k4T\" / X","url":"https://x.com/HEI/status/1965438941974106394"},{"title":"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models","url":"https://arxiv.org/pdf/2602.11174"}]

I found the paper you're looking for! Here are the key findings from "The Token Tax: Systematic Bias in Multilingual Tokenization" (arXiv:2509.05486):

**Main Findings:**

Tokenization inefficiency imposes structural disadvantages on morphologically complex, low-resource languages, inflating compute resources and depressing accuracy.

**Causal Relationship:**

The researchers evaluated 10 large language models on AfriMMLU and showed that fertility (tokens/word) reliably predicts accuracy, with higher fertility consistently predicting lower accuracy across all models and subjects.

**Economic Impact:**

A doubling in tokens results in quadrupled training cost and time, underscoring the token tax faced by many languages.

**Reasoning Models Performance:**

The first large-scale comparison of tokenization effects for reasoning vs. non-reasoning LLMs showed that reasoning capabilities substantially reduce but do not eliminate tokenization bias.

**Recommendations:**

The results motivate morphologically aware tokenization, fair pricing, and multilingual benchmarks for equitable natural language processing.

The paper was submitted on September 5, 2025, and has also been accepted to the AfricaNLP 2026 workshop proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bc774b3-2e05-4b73-b85a-4277dd93543a",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "f5bc7d55-749d-4260-8da2-4007fa794f09",
  "sourceToolAssistantUUID": "6bc774b3-2e05-4b73-b85a-4277dd93543a",
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

_source line 44 · 2026-05-19T23:32:45.702Z_

<details><summary>↩ Tool result · `toolu_01S1WhYuBwm8VorYxXiygXU4`</summary>

```text
Web search results for query: "Lesci et al "Causal Estimation of Tokenisation Bias" ACL 2025 multilingual reasoning decomposition"

Links: [{"title":"Causal Estimation of Tokenisation Bias - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1374/"},{"title":"GitHub - pietrolesci/tokenisation-bias","url":"https://github.com/pietrolesci/tokenisation-bias"},{"title":"[2506.03149v1] Causal Estimation of Tokenisation Bias","url":"http://arxiv.org/abs/2506.03149v1"},{"title":"[2506.03149] Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/abs/2506.03149"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://aclanthology.org/2025.acl-long.1374.pdf"},{"title":"GitHub - zhijing-jin/CausalNLP_Papers: A reading list for papers on causality for natural language processing (NLP) · GitHub","url":"https://github.com/zhijing-jin/CausalNLP_Papers"},{"title":"Causal Tokenizer","url":"https://www.emergentmind.com/topics/causal-tokenizer"},{"title":"Causal Estimation of Tokenisation Bias","url":"https://arxiv.org/pdf/2506.03149"},{"title":"ACL 2025 on X: \"🏆 ACL Best Paper Award: - Causal Estimation of Memorisation Profiles by Lesci et al. - Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model by Üstün et al. #NLProc #ACL2024NLP\" / X","url":"https://x.com/aclmeeting/status/1823664612207743110?lang=en"}]

I found the paper you're looking for! Here's information about "Causal Estimation of Tokenisation Bias" by Lesci et al. at ACL 2025:

## Overview

The paper "Causal Estimation of Tokenisation Bias" was authored by Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, and Tiago Pimentel, and published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in Vienna, Austria.

## Main Contribution

Modern language models are typically trained over subword sequences, but ultimately define probabilities over character-strings. Ideally, the choice of the tokeniser—which maps character-strings to subwords—should not affect the probability assigned to the underlying character-string; in practice, it does. This mismatch is defined as tokenisation bias.

## Methodology

The authors frame tokenisation bias as a causal effect and estimate it using the regression discontinuity design. They exploit the fact that tokenisation algorithms rank subwords and add the first K to a tokeniser's vocabulary, where K is an arbitrary cutoff point, allowing them to estimate a causal effect by comparing similar subwords around this cutoff.

## Key Findings

The experiments find that tokenisation consistently affects models' outputs across scales, vocabularies, and tokenisers. Notably, a subword's presence in a small model's vocabulary may increase its characters' probability by up to 17 times, highlighting tokenisation as a key design choice in language modelling.

The official implementation is available on GitHub at `pietrolesci/tokenisation-bias`, and the paper is also available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ce5cec9-c4fd-4c2f-b3a2-a7e9c7fc5d63",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "c9ad1224-8c2a-4596-837a-a989c0543456",
  "sourceToolAssistantUUID": "0ce5cec9-c4fd-4c2f-b3a2-a7e9c7fc5d63",
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

_source line 45 · 2026-05-19T23:32:46.590Z_

<details><summary>↩ Tool result · `toolu_014LkuXnw7GvN5gVc8ScUPvA`</summary>

```text
Web search results for query: "PolyMath multilingual mathematical reasoning benchmark 2026 arXiv evaluation"

Links: [{"title":"arXiv/polymath - OpenReward","url":"https://openreward.ai/arXiv/polymath"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts | OpenReview","url":"https://openreview.net/forum?id=B1vCImy6yI"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://arxiv.org/pdf/2504.18428"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://openreview.net/pdf/a485bb803e47f3020ed08d93677e7b9ae140fdf8.pdf"},{"title":"[2504.18428] PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://arxiv.org/abs/2504.18428"},{"title":"[2410.14702] Polymath: A Challenging Multi-modal Mathematical Reasoning Benchmark","url":"https://arxiv.org/abs/2410.14702"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://qwen-polymath.github.io/"},{"title":"PolyMath: Evaluating Mathematical Reasoning in Multilingual Contexts","url":"https://arxiv.org/html/2504.18428v4"}]

Based on the search results, here's what I found about PolyMath:

## Overview

PolyMath is a multilingual mathematical reasoning benchmark covering 18 languages and four easy-to-hard difficulty levels. The benchmark spans from K-12 to Olympiad and advanced frontier mathematics.

## Benchmark Structure

The benchmark partitions difficulty into 4 levels, with each level consisting of 125 problems, and each problem available in 18 language versions.

## Evaluation Results

Comprehensive evaluation shows that even Qwen3-235B-A22B-Thinking and Gemini-2.5-pro achieve only 54.6 and 52.2 benchmark scores, with about 40% accuracy under the highest level.

## Key Findings

The benchmark reveals several key challenges of LLMs in multilingual reasoning: (1) Reasoning performance varies widely across languages; (2) Input-output language consistency is low in reasoning LLMs and may be correlated with performance; (3) The thinking length differs significantly by language.

## Publication Details

The paper was published on September 18, 2025 (with last modification on April 23, 2026) as part of the NeurIPS 2025 Datasets and Benchmarks Track. The arXiv paper identifier is 2504.18428.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f2d3246-6433-4710-a626-dae1f2222f1c",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "0d6a3ef0-3d40-4f1e-8141-418f7ca168d8",
  "sourceToolAssistantUUID": "4f2d3246-6433-4710-a626-dae1f2222f1c",
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

_source line 46 · 2026-05-19T23:32:48.519Z_

<details><summary>↩ Tool result · `toolu_01UgYwcHMNBbY2FGWXKs4Fv9`</summary>

```text
Web search results for query: "MultiNRC multilingual reasoning benchmark 2026 scale labs evaluation"

Links: [{"title":"Scale Labs Leaderboard: MultiNRC | Scale Labs","url":"https://labs.scale.com/leaderboard/multinrc"},{"title":"The Future is Multilingual: A New Evaluation Benchmark","url":"https://scale.com/blog/multinrc"},{"title":"README.md · ScaleAI/MultiNRC at main","url":"https://huggingface.co/datasets/ScaleAI/MultiNRC/blob/main/README.md"},{"title":"MultiNRC","url":"https://scale.com/leaderboard/multinrc"},{"title":"[2507.17476] MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs","url":"https://arxiv.org/abs/2507.17476"},{"title":"MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs - Paper Detail","url":"https://deeplearn.org/arxiv/623059/multinrc:-a-challenging-and-native-multilingual-reasoning-evaluation-benchmark-for-llms"},{"title":"MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs | alphaXiv","url":"https://www.alphaxiv.org/resources/2507.17476v1"},{"title":"(PDF) MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs","url":"https://www.researchgate.net/publication/393966027_MultiNRC_A_Challenging_and_Native_Multilingual_Reasoning_Evaluation_Benchmark_for_LLMs"}]

I found comprehensive information about the MultiNRC benchmark. Here's what I found:

## MultiNRC Overview

MultiNRC is a challenging evaluation benchmark for large language models designed to assess multilingual reasoning ability in French, Spanish, and Chinese, consisting of over 1,000 native-authored reasoning questions crafted by native speakers to capture linguistic and cultural nuances.

## Key Motivation

Existing multilingual reasoning benchmarks are largely created by translating existing English reasoning benchmarks into target languages, which may reflect English's cultural framing and linguistic characteristics rather than being globally representative, resulting in missing reasoning tasks that require native linguistic or cultural understanding.

## Benchmark Design

MultiNRC is the first benchmark constructed natively by speakers of multiple languages and is designed to assess LLMs on more than 1,000 native, linguistic, and culturally grounded reasoning questions written by native speakers of French, Spanish, and Chinese, focusing on four categories: Language-specific Linguistic Reasoning, wordplay & riddles, cultural/tradition reasoning, and math reasoning with cultural relevance.

## Evaluation Methodology

The benchmark only included questions that at least three out of five leading LLMs failed to answer correctly, and was tested against 14 leading LLMs from all major labs. The team used an automated LLM-as-a-judge for evaluation that was validated against human reviewers and found to have an over 95% agreement rate.

## Results

Current LLMs are still not good at native multilingual reasoning, with none scoring above 50% on MultiNRC. The full MultiNRC dataset has been made publicly available on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7072d51e-3ccc-4013-a4f2-9f9323db29dd",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "169ebf32-27d9-4f10-b804-3cf12a0a0be8",
  "sourceToolAssistantUUID": "7072d51e-3ccc-4013-a4f2-9f9323db29dd",
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

_source line 47 · 2026-05-19T23:32:51.189Z_

Let me search for a few more critical items -- specifically whether anyone has done the full causal decomposition of the multilingual reasoning gap we're interested in.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "169ebf32-27d9-4f10-b804-3cf12a0a0be8",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoRAvbzKLHfBeQt2Nof",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64f13d25-9037-43ea-b089-190720acf843",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDPjGqoorN51BTESfHQqQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 729,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 19779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2768,
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

_source line 48 · 2026-05-19T23:32:52.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PyrtwYDR9xRy6JvaZWg16c`</summary>

```json
{
  "query": "causal mediation analysis tokenization multilingual performance gap LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f13d25-9037-43ea-b089-190720acf843",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoRAvbzKLHfBeQt2Nof",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27189f7a-e419-431f-81a6-9f2ccf403408",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDPjGqoorN51BTESfHQqQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 729,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 19779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2768,
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

_source line 49 · 2026-05-19T23:32:52.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011UAvJzsR9NfmL5mVPDWTs9`</summary>

```json
{
  "query": "\"Script Tax\" tokenization efficiency latency disparities multilingual 2602.11174"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27189f7a-e419-431f-81a6-9f2ccf403408",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoRAvbzKLHfBeQt2Nof",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "739f966e-8871-4062-a61b-119e005e9a3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDPjGqoorN51BTESfHQqQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 729,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 19779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2768,
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

_source line 50 · 2026-05-19T23:32:53.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017DokJnRMa3gVJSpcjgMC6W`</summary>

```json
{
  "query": "MUTANT multilingual tokenizer recipe 2511.03237 2026 results BPE improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "739f966e-8871-4062-a61b-119e005e9a3a",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoRAvbzKLHfBeQt2Nof",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ae60f58-8155-45d4-8deb-330ffdf3fcee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDPjGqoorN51BTESfHQqQr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 729,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 19779,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 729,
          "output_tokens": 214,
          "cache_read_input_tokens": 19779,
          "cache_creation_input_tokens": 2768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2768,
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

_source line 51 · 2026-05-19T23:32:59.252Z_

<details><summary>↩ Tool result · `toolu_01PyrtwYDR9xRy6JvaZWg16c`</summary>

```text
Web search results for query: "causal mediation analysis tokenization multilingual performance gap LLM 2025 2026"

Links: [{"title":"Tokenization Disparities as Infrastructure Bias: How Subword Systems Create Inequities in LLM Access and Efficiency","url":"https://arxiv.org/pdf/2510.12389"},{"title":"Tokenization and Representation Biases in Multilingual Models on Dialectal NLP Tasks","url":"https://arxiv.org/pdf/2509.20045"},{"title":"Causal Mediation Analysis for Interpreting Large Language Models","url":"https://ceur-ws.org/Vol-3741/paper39.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf"},{"title":"Tokenization and Representation Biases in Multilingual ...","url":"https://aclanthology.org/2025.emnlp-main.1224.pdf"},{"title":"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners","url":"https://arxiv.org/pdf/2505.15257"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/pdf/2512.21933"},{"title":"Tokenizer Choice For LLM Training: Negligible or Crucial?","url":"https://arxiv.org/pdf/2310.08754"}]

The web search returned several highly relevant results on this topic. Here's what I found:

## Key Research Findings

**Tokenization and Multilingual Performance Gaps:**

Tokenization, the fundamental preprocessing step transforming raw text into subword units, is a critical but underexplored factor, as tokenization algorithms predominantly optimized for high-resource languages may inadequately handle the morphological complexity and structural properties of low-resource languages, thereby exacerbating existing inequalities.

A systematic investigation of tokenization disparities across over 200 languages using the FLORES-200 benchmark quantified variations in cross-lingual efficiency and identified tokenization as a key driver of performance inequities in multilingual NLP.

**Representation Biases in Multilingual Models:**

Tokenization bias has been shown to impact not only the performance, but also the costs of deploying LLMs across languages, and was recently quantified as Tokenization Parity (TP). Small variations in pronunciation and writing lead to significant performance drops known as the dialect gap.

**Causal Analysis Approaches:**

Motivated by cognitive neuroscience, researchers hypothesize that reasoning and language processing in LLMs can be disentangled, performing a causal intervention by removing language-specific components from hidden representations.

**Training Efficiency Impact:**

English-centric tokenizers applied to the training of multilingual LLMs result in severe downstream performance degradation and additional training costs of up to 68%, due to an inefficient tokenization vocabulary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27189f7a-e419-431f-81a6-9f2ccf403408",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "2f82007a-4de0-4c54-a337-ccfca2a3a85c",
  "sourceToolAssistantUUID": "27189f7a-e419-431f-81a6-9f2ccf403408",
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

_source line 52 · 2026-05-19T23:32:59.946Z_

<details><summary>↩ Tool result · `toolu_011UAvJzsR9NfmL5mVPDWTs9`</summary>

```text
Web search results for query: ""Script Tax" tokenization efficiency latency disparities multilingual 2602.11174"

Links: [{"title":"[2602.11174] The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models","url":"https://arxiv.org/abs/2602.11174"},{"title":"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency","url":"https://arxiv.org/pdf/2602.11174"},{"title":"The Script Tax: Measuring Tokenization-Driven Efficiency and Latency Disparities in Multilingual Language Models","url":"https://arxiv.org/html/2602.11174"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/html/2509.05486v1"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization Jessica M. Lundin","url":"https://arxiv.org/pdf/2509.05486"},{"title":"Tokenization Disparities as Infrastructure Bias: How Subword Systems Create Inequities in LLM Access and Efficiency","url":"https://arxiv.org/pdf/2510.12389"},{"title":"(PDF) The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://www.researchgate.net/publication/395355055_The_Token_Tax_Systematic_Bias_in_Multilingual_Tokenization"},{"title":"[2509.05486] The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/abs/2509.05486"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/token-tax-systematic-bias-multilingual-tokenization"}]

I found the paper you searched for! Here's what the research is about:

## The Script Tax: Key Findings

The paper examines how pretrained multilingual language models, often assumed to be script-agnostic, can impose systematic costs on certain writing systems through their tokenizers by comparing two orthographic variants with identical linguistic content.

### Main Results

Across mBERT and XLM-R models, the higher-fragmentation orthography shows approximately a 3.4x increase in fertility (6.73-6.85 vs. 2.10-2.35 tokens/word), leading to a 16.5x inference slowdown (0.23 vs. 3.8 sentences/second) on identical hardware.

Using bits per character (BPC) to avoid measurement issues from subword fragmentation, the researchers found a substantial increase in information cost: +19.7% for mBERT and +47.1% for XLM-R.

### Key Contributions

The research defines the script tax as a joint disparity in fertility, latency, and character-normalized information cost under controlled evaluation, showing that tokenization fragmentation is a first-order driver of both compute overhead (16.5x slowdown) and reduced modeling efficiency.

The results highlight tokenization as a key source of inequity in multilingual NLP and motivate script-aware tokenization and pretraining.

The paper was published on arXiv on January 19, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "739f966e-8871-4062-a61b-119e005e9a3a",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "05ec9784-b010-4f66-acfe-054ad37a1aea",
  "sourceToolAssistantUUID": "739f966e-8871-4062-a61b-119e005e9a3a",
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

_source line 53 · 2026-05-19T23:33:00.370Z_

<details><summary>↩ Tool result · `toolu_017DokJnRMa3gVJSpcjgMC6W`</summary>

```text
Web search results for query: "MUTANT multilingual tokenizer recipe 2511.03237 2026 results BPE improvement"

Links: [{"title":"[2511.03237] MUTANT: A Recipe for Multilingual Tokenizer Design","url":"https://arxiv.org/abs/2511.03237"},{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design","url":"https://arxiv.org/pdf/2511.03237"},{"title":"krutrim-ai-labs/MUTANT · Datasets at Hugging Face","url":"https://huggingface.co/datasets/krutrim-ai-labs/MUTANT"},{"title":"GitHub - ola-krutrim/MUTANT: Code for ACL 2026 work MUTANT · GitHub","url":"https://github.com/ola-krutrim/MUTANT"},{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design | OpenReview","url":"https://openreview.net/forum?id=oEpMYAs10U"},{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mutant-recipe-multilingual-tokenizer-design"},{"title":"Multilingual Tokenizers","url":"https://www.emergentmind.com/topics/multilingual-tokenizers"},{"title":"MUTANT: A Recipe for Multilingual Tokenizer Design Anonymous ACL submission","url":"https://openreview.net/pdf/286d0a3d3ecf557528cf05e466c88f3d9bd9239b.pdf"},{"title":"Mut-BPE: A Modified BPE Strategy Improves Variant Effect Prediction","url":"https://www.biorxiv.org/content/10.1101/2025.12.01.691503.full.pdf"},{"title":"Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization","url":"https://arxiv.org/pdf/2508.04796"}]

Based on the search results, here's what I found about MUTANT:

MUTANT is a recipe for building multilingual tokenizers, with careful vocabulary and training data design, language-aware pre-tokenization, and subword and multiword aware training. The paper was accepted at ACL 2026.

**Key Results:**

Evaluated across English, 22 Indian languages and code data, the tokenizer improves the average fertility score by 39.5% over LLaMA4 and by 18% over Sutra (the current best). This translates to 44% improvement in inference throughput over LLaMA4 while maintaining comparable performance on English and Indic benchmarks.

**Design Approach:**

MUTANT-Indic is a tokenizer for India-specific multilingual LLMs, that produces linguistically coherent tokens and achieves state-of-the-art performance. The work presents detailed ablations across tokenizer training data size, vocabulary size, merging techniques, and pre-tokenization strategies.

The paper (arXiv:2511.03237) addresses the challenge that while subword methods like Byte Pair Encoding (BPE) are widely adopted, their effectiveness in multilingual settings remains underexplored.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ae60f58-8155-45d4-8deb-330ffdf3fcee",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "c197c4f0-a03b-437b-92c9-86dc73856cab",
  "sourceToolAssistantUUID": "4ae60f58-8155-45d4-8deb-330ffdf3fcee",
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

_source line 54 · 2026-05-19T23:33:03.799Z_

Now let me fetch the most critical remaining papers for detailed analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c197c4f0-a03b-437b-92c9-86dc73856cab",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoS3UuxqQdHUxxDhU38",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ecf566a-f43e-452c-9dce-0a675cd94fae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PRnVdXYNaDeyXsw8UCPaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 22547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3396,
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

_source line 55 · 2026-05-19T23:33:07.315Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ThPN7WQzkEMmxs9nGFtvBk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.05486",
  "prompt": "Extract full details: title, authors, date, methodology, key quantitative findings on fertility predicting accuracy, what causal claims they make vs correlational claims. Do they perform causal decomposition of the multilingual gap into tokenization vs other factors? What are the specific regression slopes and R-squared values? What are the limitations they acknowledge?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ecf566a-f43e-452c-9dce-0a675cd94fae",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoS3UuxqQdHUxxDhU38",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1a99173-a6f8-4e6a-8618-026feae81f58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PRnVdXYNaDeyXsw8UCPaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 22547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3396,
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

_source line 56 · 2026-05-19T23:33:09.279Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BmvVwQD3V61penCAUsQ33r`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.16088v3",
  "prompt": "Extract full details about \"Date Fragments\" paper: title, authors, date, methodology, what they found about tokenization fragmentation effects on temporal reasoning, what causal mechanisms they identify, how this relates to the arXiv:2603.19017 paper, key quantitative findings. Does this paper do causal decomposition?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1a99173-a6f8-4e6a-8618-026feae81f58",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoS3UuxqQdHUxxDhU38",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70f58a6d-7130-46ac-a17d-4aa31b3a8094",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PRnVdXYNaDeyXsw8UCPaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 22547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3396,
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

_source line 57 · 2026-05-19T23:33:11.835Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019z536aeCe91ms5HPV48CyC`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.03149v1",
  "prompt": "Extract the full methodology of the regression discontinuity design used in this paper. What exactly do they measure? How do they define tokenization bias causally? Do they examine multilingual reasoning tasks or only English? What are the specific quantitative results about how much tokenization affects model outputs? What are the limitations regarding extending this to multilingual reasoning gaps?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f58a6d-7130-46ac-a17d-4aa31b3a8094",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoS3UuxqQdHUxxDhU38",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8675edcd-f403-474c-8de0-2a0d1c60db4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PRnVdXYNaDeyXsw8UCPaD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 22547,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3396
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 22547,
          "cache_creation_input_tokens": 3396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3396,
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

_source line 58 · 2026-05-19T23:33:13.095Z_

<details><summary>↩ Tool result · `toolu_01ThPN7WQzkEMmxs9nGFtvBk`</summary>

```text
# Paper Summary: The Token Tax

**Title:** "The Token Tax: Systematic Bias in Multilingual Tokenization"

**Authors:** Jessica M. Lundin, Ada Zhang, Nihal Karim, Hamza Louzan, Victor Wei, David Adelani, Cody Carroll

**Date:** Submitted September 5, 2025

## Methodology
The researchers evaluated 10 large language models on AfriMMLU, an assessment containing "9,000 MCQA items; 5 subjects; 16 African languages."

## Key Quantitative Findings
The abstract reports that "fertility (tokens/word) reliably predicts accuracy" and that "higher fertility consistently predicts lower accuracy across all models and subjects." Regarding economic impact, they found that "a doubling in tokens results in quadrupled training cost and time."

## Causal vs. Correlational Claims
The provided content describes correlational relationships ("fertility reliably predicts accuracy") rather than causal decomposition. The abstract does not present regression slopes, R-squared values, or mechanistic decomposition isolating tokenization effects from other factors contributing to multilingual performance gaps.

## Limitations Acknowledged
The webpage extract does not detail specific limitations. The abstract mentions the work "motivates morphologically aware tokenization, fair pricing, and multilingual benchmarks" but does not explicitly discuss study constraints or acknowledge limitations.

**Note:** Full methodological details, statistical coefficients, and limitations likely appear in the complete paper accessible via the PDF link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1a99173-a6f8-4e6a-8618-026feae81f58",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "287c4a6c-4fd6-4241-99f1-763419531741",
  "sourceToolAssistantUUID": "f1a99173-a6f8-4e6a-8618-026feae81f58",
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

_source line 59 · 2026-05-19T23:33:21.093Z_

<details><summary>↩ Tool result · `toolu_019z536aeCe91ms5HPV48CyC`</summary>

```text
# Tokenization Bias: Methodology and Findings

## Causal Definition of Tokenization Bias

The researchers frame tokenization bias using potential outcomes theory. They define it as the causal effect of including a subword in a vocabulary on model predictions. Specifically, they compare performance when a subword is present versus absent, measuring the difference in log-probability assigned to corresponding character sequences.

The formal causal estimand is: "ψ = E[Y₁(v) - Y₀(v)]" where Y₁ represents performance when trained with the subword and Y₀ represents counterfactual performance without it.

## Regression Discontinuity Design

The paper exploits a crucial insight: tokenization algorithms rank subwords sequentially and include the top K in their vocabulary. This arbitrary cutoff point creates a natural experiment.

**The measurement strategy:**
- Compares subwords near the vocabulary cutoff threshold
- Uses subwords just below the cutoff (excluded) as counterfactual estimates
- Uses subwords just above the cutoff (included) as observed values
- Assumes similar subwords near the boundary differ only in treatment assignment

This design avoids confounding because subwords near the threshold have comparable properties despite their inclusion status.

## Scope and Results

**Language coverage:** The experiments focus exclusively on English-language models, with no examination of multilingual tasks or reasoning benchmarks.

**Quantitative findings:**
- Small models (100 parameters): tokenization bias reaches 2.88 nats (BPE) and 2.51 nats (WordPiece)
- Larger models (850 parameters): approximately 1 nat bias
- Practical implication: "a subword's characters would thus be assigned roughly 2.7 times less probability" without vocabulary inclusion

## Key Limitations

The paper acknowledges several constraints:

- **Multilingual gap:** No analysis of how tokenization bias affects cross-linguistic fairness or reasoning across languages
- **Model scale:** Testing limited to relatively small models
- **Task specificity:** Focuses on raw probability assignment rather than downstream task performance
- **Generalization:** Methodology applies primarily to sequentially-constructed tokenizers (BPE, WordPiece)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8675edcd-f403-474c-8de0-2a0d1c60db4f",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "abd8b755-a206-41dc-9ae8-b65dc1d4b410",
  "sourceToolAssistantUUID": "8675edcd-f403-474c-8de0-2a0d1c60db4f",
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

_source line 60 · 2026-05-19T23:33:22.887Z_

<details><summary>↩ Tool result · `toolu_01BmvVwQD3V61penCAUsQ33r`</summary>

```text
# Date Fragments: A Hidden Bottleneck of Tokenisation for Temporal Reasoning

## Bibliographic Details
**Title:** Date Fragments: A Hidden Bottleneck of Tokenisation for Temporal Reasoning

**Authors:** Gagan Bhatia, Maxime Peyrard, Wei Zhao

**Institutions:** University of Aberdeen; Université Grenoble Alpes & CNRS

**Date:** Posted to arXiv as version 3 (2505.16088v3)

---

## Methodology

The researchers introduced three complementary analytical approaches:

1. **Date Fragmentation Ratio (F):** A custom metric quantifying tokenization quality by measuring how faithfully subword tokenizers preserve year, month, and day components. The metric combines penalties for split components, lost delimiters, token count inflation, and distributional divergence (θ).

2. **DateAugBench Dataset:** A benchmark of 6,500 examples across three tasks—context-based resolution, format switching, and date arithmetic—spanning 21 date formats and four temporal periods (Past, Near Past, Present, Future).

3. **Internal Representation Analysis:** Layerwise linear probing to identify the tokenization compensation point (TCP)—"the earliest layer at which...lightweight linear probe...achieves above-chance accuracy" of 80%.

---

## Key Findings on Tokenization Fragmentation

**Quantitative Results:**
- Date fragmentation correlates with accuracy drops up to 10 points on uncommon dates
- Pearson correlation of −0.61 between fragmentation ratio and resolution accuracy across temporal regimes
- OLMo achieved lowest fragmentation (0.15 average ratio); Llama 2 and Phi showed highest (0.63)
- Models achieved ~97% on format switching but only 26-68% on context-based resolution

**Performance Disparities:**
- GPT-4o-mini: 61.7% (Past) → 70.5% (Present) → 58.2% (Future)
- Explicit delimiters (DD/MM/YYYY) yielded 64-71% accuracy versus 34-61% for concatenated formats (DDMMYYYY)

---

## Causal Mechanisms Identified

The authors employed **causal attention-hop analysis** to trace how models "stitch" date fragments:

1. **Emergent Date Abstraction:** Larger models recover calendar-level semantics from fragmented tokens earlier in their layer stack. TCP shifts dramatically with scale: Qwen2.5-0.5B reaches TCP at layer 12 (50% depth); 7B model at layer 4 (14.3%).

2. **Non-Human Reasoning Paths:** LLMs follow flexible, format-dependent ordering (often year → month → day) based on statistical associations with subword fragments, rather than explicit calendar rules humans employ.

3. **Misalignment Finding:** The paper notes that human readers "immediately map each component to a coherent temporal schema," while LLMs "rely on learned statistical associations between digit-patterns." For rare dates outside pretraining distribution, reasoning paths become "obscure."

---

## Relation to arXiv:2603.19017

The provided content does not reference arXiv:2603.19017. No direct comparison or relation is established in this document.

---

## Does This Paper Perform Causal Decomposition?

**Yes, but with important caveats.** The authors employ causal path tracing to identify reasoning paths—sequences showing "in which order date fragments are stitched together." However, this differs from rigorous causal decomposition (e.g., structural causal models or interventional analysis). Their framework combines next-token prediction and token importance (via token replacement) to score paths. The authors acknowledge limitations: "the core idea of our causal framework is inspired by Lindsey et al. (2025); however, our extension to temporal reasoning is not evaluated."

Human evaluation validates the fragmentation metric (Spearman ρ=0.84 vs. human severity ratings), but the causal path analysis lacks independent verification beyond qualitative visualization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70f58a6d-7130-46ac-a17d-4aa31b3a8094",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "1811cd71-dadb-4474-ba3f-473fe2f2131c",
  "sourceToolAssistantUUID": "70f58a6d-7130-46ac-a17d-4aa31b3a8094",
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

_source line 61 · 2026-05-19T23:33:25.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TBmrcheASoQfQA4Hn1xq1c`</summary>

```json
{
  "query": "structural causal model tokenization multilingual reasoning gap decomposition direct indirect effect 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1811cd71-dadb-4474-ba3f-473fe2f2131c",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoThkopfyXFfmjeggYG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b45dd1f8-fd1c-42f2-9a4d-b73e01fcda35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JT5xY4HrXDnWUmURBzzH58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 527,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 25943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1775,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-19T23:33:26.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LhUpH8acmgH3nxaEX5E7Xr`</summary>

```json
{
  "query": "\"Broken Words Broken Performance\" tokenization LLMs arXiv 2512.21933 findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b45dd1f8-fd1c-42f2-9a4d-b73e01fcda35",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoThkopfyXFfmjeggYG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a590923-990b-4bd4-9297-198427860ad2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JT5xY4HrXDnWUmURBzzH58",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 527,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 25943,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 527,
          "output_tokens": 130,
          "cache_read_input_tokens": 25943,
          "cache_creation_input_tokens": 1775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1775,
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

_source line 63 · 2026-05-19T23:33:32.899Z_

<details><summary>↩ Tool result · `toolu_01LhUpH8acmgH3nxaEX5E7Xr`</summary>

```text
Web search results for query: ""Broken Words Broken Performance" tokenization LLMs arXiv 2512.21933 findings"

Links: [{"title":"[2512.21933] Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/abs/2512.21933"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/pdf/2512.21933"},{"title":"(PDF) Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://www.researchgate.net/publication/399135134_Broken_Words_Broken_Performance_Effect_of_Tokenization_on_Performance_of_LLMs"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/html/2512.21933v1"},{"title":"The Text Uncanny Valley: Non-Monotonic Performance Degradation in LLM Information Retrieval","url":"https://arxiv.org/html/2605.07186"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://www.arxiv.org/pdf/2512.21933"},{"title":"[2508.06533] The Art of Breaking Words: Rethinking Multilingual Tokenizer Design","url":"https://arxiv.org/abs/2508.06533"}]

Based on the search results, here are the key findings from the paper "Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs" (arXiv 2512.21933):

## Main Hypothesis and Findings

The paper hypothesizes that natural words broken into multiple tokens due to limited vocabulary size (e.g., Mistral's tokenizer splitting "martial" into "mart" and "ial") negatively impacts LLM performance on various NLP tasks.

## Methodology

To quantify this effect, the authors propose a set of penalty functions that compute a tokenization penalty for a given text for a specific LLM, indicating how "bad" the tokenization is.

## Validation

The researchers established the statistical significance of their hypothesis on seven different NLP tasks across four different LLMs. The evaluation covered 4 different LLMs – Phi, Mistral, Qwen, and Llama – having varying vocabulary sizes.

## Key Example

The paper illustrates the problem using "unhappiness": a human might break it as "un," "happy," and "ness" preserving morphological structure, but the tokenizer of Phi-3.5-mini-instruct breaks it as "unh," "app," "iness."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a590923-990b-4bd4-9297-198427860ad2",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "0ea4c5fa-274a-45b9-bd63-b306b5a620b7",
  "sourceToolAssistantUUID": "8a590923-990b-4bd4-9297-198427860ad2",
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

_source line 64 · 2026-05-19T23:33:32.903Z_

<details><summary>↩ Tool result · `toolu_01TBmrcheASoQfQA4Hn1xq1c`</summary>

```text
Web search results for query: "structural causal model tokenization multilingual reasoning gap decomposition direct indirect effect 2025 2026"

Links: [{"title":"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?","url":"https://arxiv.org/pdf/2510.27269"},{"title":"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners","url":"https://arxiv.org/pdf/2505.15257"},{"title":"The Token Tax: Systematic Bias in Multilingual Tokenization","url":"https://arxiv.org/pdf/2509.05486"},{"title":"Structured Thinking Matters: Improving LLMs Generalization in Causal Inference Tasks","url":"https://arxiv.org/html/2505.18034v1"},{"title":"What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features","url":"https://arxiv.org/pdf/2604.04720"},{"title":"What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?","url":"https://arxiv.org/pdf/2603.19017"}]

Based on the search results, I found several recent research papers (2025-2026) that address aspects of your query related to multilingual reasoning, tokenization, and causal/structural analysis:

## Key Research Findings:

**Multilingual Reasoning Gaps:**
Reasoning language models exhibit a multilingual reasoning gap, performing much better on high-resource languages like English than low-resource languages, and while recent studies have explored various methods to narrow this gap, systematic understanding of why these gaps arise remains under-explored.

**Language-Reasoning Disentanglement:**
Research using causal intervention by removing language-specific components from hidden representations has shown consistent performance improvements across open-source LLMs and multilingual reasoning benchmarks, supporting the claim that disentangling language and reasoning enhances multilingual generalization.

**Tokenization and its Impact:**
Tokenization is established as a source of computational and economic inequality in NLP systems, with impacts ranging from larger token counts to performance degradation for morphologically complex low-resource languages, and these technical disparities translate into economic exclusion through tokenization taxes.

**Reasoning Trace Features:**
Recent work measures multilingual reasoning through features including direct utility (degree to which reasoning steps directly contribute to the final answer) and indirect utility (proportion of steps supporting direct utility steps).

These papers suggest an active research area examining the intersection of multilingual reasoning, tokenization effects, and causal decomposition of model behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b45dd1f8-fd1c-42f2-9a4d-b73e01fcda35",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "58a3619b-5c3d-431c-8bd7-f40156d3306f",
  "sourceToolAssistantUUID": "b45dd1f8-fd1c-42f2-9a4d-b73e01fcda35",
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

_source line 65 · 2026-05-19T23:33:35.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqFBwtSMA5cib7o12WWr9J`</summary>

```json
{
  "query": "\"Tokenization Constraints\" \"Symbolic and Arithmetic Reasoning\" 2505.14178 arXiv findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58a3619b-5c3d-431c-8bd7-f40156d3306f",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoUSZnESm2huCRedm5Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1b4689e-47dc-4feb-80e2-5adabce7bb45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwJKkYv6hnhaNnQos8hpPP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 706,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 27718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1307,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-19T23:33:36.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTF1Z1pMp3dMNUESiZo1Ht`</summary>

```json
{
  "query": "\"Parity-Aware Byte-Pair Encoding\" cross-lingual fairness tokenization 2508.04796 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1b4689e-47dc-4feb-80e2-5adabce7bb45",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoUSZnESm2huCRedm5Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1a9362f-7bc5-4b63-92c2-48e09459eb4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwJKkYv6hnhaNnQos8hpPP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 706,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 27718,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1307
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 706,
          "output_tokens": 144,
          "cache_read_input_tokens": 27718,
          "cache_creation_input_tokens": 1307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1307,
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

_source line 67 · 2026-05-19T23:33:42.076Z_

<details><summary>↩ Tool result · `toolu_01BqFBwtSMA5cib7o12WWr9J`</summary>

```text
Web search results for query: ""Tokenization Constraints" "Symbolic and Arithmetic Reasoning" 2505.14178 arXiv findings"

Links: [{"title":"[2505.14178] Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits","url":"https://arxiv.org/abs/2505.14178"},{"title":"arXiv:2505.14178v1 [cs.CL] 20 May 2025 Tokenization Constraints in LLMs:","url":"https://arxiv.org/pdf/2505.14178"},{"title":"The Lookahead Limitation: Why Multi-Operand Addition is Hard for LLMs","url":"https://arxiv.org/pdf/2502.19981"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.14658"},{"title":"1 Illustrating the dependence of frontier model arithmetic performance on tokenization. We show how using commas can enforce right-to-left (R2L) tokenization for the same addition problem. R2L tokenization leads to improved model performance on both GPT-3.5 and GPT-4 (March 2023 models), which we show is due to tokenization alignment between addends and answer through various controls and error analyses.","url":"https://arxiv.org/html/2402.14903v1"},{"title":"Discrete JEPA: Learning Discrete Token Representations without Reconstruction","url":"https://arxiv.org/pdf/2506.14373"},{"title":"Frugal LMs Trained to Invoke Symbolic Solvers Achieve   Parameter-Efficient Arithmetic Reasoning","url":"https://arxiv.org/pdf/2312.05571"}]

Based on the search results, here are the key findings from the arXiv paper 2505.14178 on "Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits":

## Main Findings

The success of Chain-of-Thought (CoT) prompting reasoning is fundamentally bounded by the structure of tokenized inputs.

The research investigates how tokenization schemes, particularly subword-based methods like byte-pair encoding (BPE), impede symbolic computation by merging or obscuring atomic reasoning units.

## Token Awareness Concept

The paper introduces the notion of Token Awareness to formalize how poor token granularity disrupts logical alignment and prevents models from generalizing symbolic procedures.

## Performance Implications

The research demonstrates that token structure dramatically affects reasoning performance, causing failure even with CoT, while atomically-aligned formats unlock strong generalization.

The paper, published on May 20, 2025, represents a theoretical and empirical investigation into the often-overlooked role of tokenization as the foundational layer of computation in language models, revealing that token structure is a critical constraint on a model's ability to perform symbolic and arithmetic reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1b4689e-47dc-4feb-80e2-5adabce7bb45",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "6491b40c-c52b-410a-bdec-e2721aa5037c",
  "sourceToolAssistantUUID": "d1b4689e-47dc-4feb-80e2-5adabce7bb45",
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

_source line 68 · 2026-05-19T23:33:43.993Z_

<details><summary>↩ Tool result · `toolu_01LTF1Z1pMp3dMNUESiZo1Ht`</summary>

```text
Web search results for query: ""Parity-Aware Byte-Pair Encoding" cross-lingual fairness tokenization 2508.04796 2026"

Links: [{"title":"[2508.04796] Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization","url":"https://arxiv.org/abs/2508.04796"},{"title":"Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization","url":"https://arxiv.org/html/2508.04796v1"},{"title":"Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization | OpenReview","url":"https://openreview.net/forum?id=5410vG60fU"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=29800&show=250"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=10550&show=100"},{"title":"GitHub - swiss-ai/parity-aware-bpe: Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization [ACL 2026] · GitHub","url":"https://github.com/swiss-ai/parity-aware-bpe"},{"title":"Parity-Aware Byte-Pair Encoding:","url":"https://arxiv.org/pdf/2508.04796"},{"title":"Does Visual Rendering Bypass Tokenization? Investigating Script-Tokenizer Misalignment in Pixel-Based Language Models","url":"https://arxiv.org/html/2602.06973v1"},{"title":"Byte-Pair Encoding: Efficient Subword Tokenization","url":"https://www.emergentmind.com/topics/byte-pair-encoding-bpe"}]

Based on the search results, here's information about Parity-Aware Byte-Pair Encoding:

## Overview

Parity-aware Byte Pair Encoding (BPE) is a variant of the widely-used BPE algorithm, introduced to address fairness issues in tokenization across multiple languages.

## The Problem It Addresses

Standard algorithms for learning tokenizers rely on frequency-based objectives, which favor languages dominant in the training data and consequently leave lower-resource languages with tokenizations that are disproportionately longer, morphologically implausible, or even riddled with placeholders. This phenomenon ultimately amplifies computational and financial inequalities between users from different language backgrounds.

## How It Works

At every merge step, Parity-aware BPE maximizes the compression gain of the currently worst-compressed language, trading a small amount of global compression for cross-lingual parity. This modification affects only vocabulary learning; the inference procedure remains the same as in Classical BPE.

## Results

Parity-aware BPE leads to better token-count parity across languages compared to Classical BPE while maintaining comparable global compression rates, and evaluations on 13 multilingual benchmarks show that models trained with a Parity-aware tokenizer match or exceed downstream performance compared to those trained with a Classical BPE tokenizer.

The paper (arXiv:2508.04796) was authored by Foroutan, Meister, Paul, Niklaus, Ahmadi, Bosselut, and Sennrich.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1a9362f-7bc5-4b63-92c2-48e09459eb4a",
  "isSidechain": true,
  "promptId": "9ac1c140-e23a-453c-a122-0f392e101930",
  "agentId": "a45e407b5da2f3af7",
  "type": "user",
  "uuid": "e6f54777-81fd-4cb7-ab3c-a35a6731dadb",
  "sourceToolAssistantUUID": "d1a9362f-7bc5-4b63-92c2-48e09459eb4a",
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

_source line 69 · 2026-05-19T23:34:45.415Z_

Now I have a comprehensive picture. Let me compile the final analysis.

---

## Research Landscape Report: Multilingual Tokenization and Reasoning Gaps (as of mid-2026)

### 1. Causal Analysis of Tokenization Effects (Beyond Lesci et al.)

**Lesci et al. (2025)** -- "Causal Estimation of Tokenisation Bias" (arXiv:2506.03149, ACL 2025 Best Paper) remains the foundational causal work. They use regression discontinuity design (RDD) to show that a subword's vocabulary membership causally increases its characters' probability by up to 17x in small models. However, critical limitations exist: **they test only English-language models, only measure raw probability assignment (not downstream task performance), and do not examine multilingual reasoning at all.** Their methodology applies specifically to sequentially-constructed tokenizers (BPE, WordPiece).

**Bhatia et al. (2025)** -- "Date Fragments: A Hidden Bottleneck of Tokenisation for Temporal Reasoning" (arXiv:2505.16088) employs causal attention-hop analysis to trace how models stitch date fragments together. They report Pearson correlation of -0.61 between fragmentation ratio and resolution accuracy. They use causal path tracing but acknowledge it is not rigorous structural causal modeling -- their causal framework is "inspired by Lindsey et al. (2025)" but its extension to temporal reasoning is not formally validated.

**Ayoobi et al. (2026)** -- "Say Anything but This: When Tokenizer Betrays Reasoning in LLMs" (arXiv:2601.14658, January 2026) identifies eight systematic tokenizer artifacts causing reasoning failures through "phantom edits." Over 11,000 replacement trials. Primarily English-focused, identifies mechanisms but does not perform formal causal decomposition.

**Key gap identified:** No existing work applies formal causal decomposition (e.g., structural causal models with direct/indirect effects, or causal mediation analysis) to decompose the multilingual reasoning gap into tokenization vs. other contributing factors.

---

### 2. New Multilingual Reasoning Benchmarks and Evaluations (2026)

- **MultiNRC** (Scale AI, arXiv:2507.17476): First natively-constructed multilingual reasoning benchmark (French, Spanish, Chinese). 1,000+ questions written by native speakers. No model scores above 50%. Focuses on cultural/linguistic reasoning rather than translation-based evaluation.

- **PolyMath** (arXiv:2504.18428, NeurIPS 2025 D&B Track, updated April 2026): Multilingual mathematical reasoning across 18 languages at 4 difficulty levels (K-12 through Olympiad). Even top models achieve only ~54% overall. Shows reasoning performance varies widely across languages and input-output language consistency is low.

- **MultiTempBench** (from arXiv:2603.19017, March 2026): Multilingual temporal reasoning across 5 languages (English, German, Chinese, Arabic, Hausa), 3 tasks (date arithmetic, time zone conversion, temporal relation extraction), and 3 calendar systems (Gregorian, Hijri, Chinese Lunar).

---

### 3. arXiv:2603.19017 -- "What Really Controls Temporal Reasoning in LLMs" (Bhatia, Isa, Peyrard, Zhao, March 2026)

Key findings:
- Introduced **multilingual Date Fragmentation Ratio (mDFR)**, calibrated with human severity ratings
- Tested 20 LLMs across 5 languages and 3 calendar systems
- Used **crossed mixed-effects regression** (not formal causal decomposition) to analyze factors
- **Critical finding:** The dominant factor depends on resource level:
  - **High-resource languages:** temporal linearity (how models represent time sequentially) is the strongest accuracy predictor
  - **Low-resource languages:** tokenization fragmentation becomes the dominant performance bottleneck
- **Conclusion:** Neither tokenization nor representation alone explains temporal reasoning -- their relative importance is resource-dependent
- This is a **correlational/regression analysis**, not a formal causal decomposition with interventions

---

### 4. New Tokenizer Designs/Approaches (2026)

- **MUTANT** (arXiv:2511.03237, ACL 2026): Recipe for multilingual tokenizers with language-aware pre-tokenization and subword+multiword-aware training. 39.5% fertility improvement over LLaMA4, 44% inference throughput improvement. Evaluated on English + 22 Indian languages.

- **Parity-Aware BPE** (arXiv:2508.04796, ACL 2026): Modified BPE that maximizes compression gain of the worst-compressed language at each merge step. Better cross-lingual parity with comparable global compression. Evaluated on 13 multilingual benchmarks with matching or better downstream performance.

- **PickyBPE, Scaffold-BPE, SuperBPE**: Various BPE improvements focused on vocabulary efficiency, scaffold token pruning, and multi-word boundary expansion.

---

### 5. Existing Work on Causal Decomposition of Multilingual Gaps

**Kang et al. (2025/2026)** -- "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?" (arXiv:2510.27269, Findings of ACL 2026): Identifies "language understanding failure" as the primary driver. They use diagnostic detection methods (not formal causal decomposition). Propose Selective Translation achieving near-full-translation performance while translating only ~20% of inputs. **Does not examine tokenization's role.**

**Zhao et al. (2025)** -- "When Less Language is More" (arXiv:2505.15257, NeurIPS 2025): Performs causal intervention via inference-time ablation of language-specific representations. Shows language-specific ablation consistently boosts multilingual reasoning across 10 LLMs and 11 languages. This is **intervention-based** but targets language vs. reasoning separation, not tokenization specifically.

**Ki et al. (2026)** -- "What Makes Good Multilingual Reasoning?" (arXiv:2604.04720, April 2026): Uses logistic regression and sparse autoencoders to identify measurable features of reasoning traces. Correlational, not causal. Finds feature-accuracy associations vary dramatically and can reverse across languages.

**Lundin et al. (2025)** -- "The Token Tax" (arXiv:2509.05486, AfricaNLP 2026): Shows fertility reliably predicts accuracy on AfriMMLU across 10 LLMs. First comparison of tokenization effects for reasoning vs. non-reasoning LLMs (finding reasoning reduces but does not eliminate the bias). **Correlational only** -- no causal decomposition.

**"The Script Tax"** (arXiv:2602.11174, January 2026): Controlled comparison of two orthographic variants with identical content showing 3.4x fertility increase leads to 16.5x inference slowdown. Strong evidence but focused on efficiency/latency, not reasoning accuracy decomposition.

---

### NOVELTY ASSESSMENT

**What exists:**
1. Causal estimation of tokenization bias on probability assignment (Lesci et al.) -- English only, no reasoning tasks
2. Correlational evidence linking fertility to accuracy (Token Tax, Script Tax)
3. Causal intervention separating language from reasoning representations (Zhao et al.) -- does not isolate tokenization
4. Diagnostic analysis of understanding failures in multilingual reasoning (Kang et al.) -- ignores tokenization
5. Fragmentation analysis for temporal reasoning with regression analysis (Bhatia et al.) -- not formal causal decomposition
6. Taxonomy of tokenizer artifacts causing reasoning failures (Ayoobi et al.) -- descriptive, not decomposing the gap

**What does NOT exist (the gap your proposed contribution fills):**
- **No work performs formal causal decomposition of the multilingual reasoning gap into tokenization-mediated vs. non-tokenization pathways.** Specifically, nobody has built a structural causal model with tokenization properties (fertility, fragmentation) as mediating variables and used causal mediation analysis (natural direct effect vs. natural indirect effect) to quantify what fraction of the multilingual reasoning gap is causally attributable to tokenization.
- Lesci et al.'s causal framework (RDD) is limited to probability assignment in English models. Extending causal methodology to multilingual reasoning tasks is unexplored.
- The Token Tax shows correlation; the Script Tax shows controlled comparison for efficiency; but neither performs causal decomposition of reasoning accuracy gaps.
- The closest work (arXiv:2603.19017) uses mixed-effects regression but explicitly does not claim causal identification.

**Your proposed contribution remains novel** as of mid-2026. The specific gap is: a causal decomposition framework that quantifies how much of the multilingual reasoning gap flows through tokenization (fertility, fragmentation, morphological misalignment) versus other pathways (training data distribution, representation learning, cultural/linguistic knowledge gaps). No published or preprinted work has done this.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6f54777-81fd-4cb7-ab3c-a35a6731dadb",
  "isSidechain": true,
  "agentId": "a45e407b5da2f3af7",
  "requestId": "req_011CbCoVFxq2ueMVFB6aaVtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fc51191-528d-40c3-8ac7-c8511671c3cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ec50337c-efb0-4976-b822-6e64218d6124",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRXHoh59Ca3dqqUXMmM6dv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 29025,
      "output_tokens": 2164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2473
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2164,
          "cache_read_input_tokens": 29025,
          "cache_creation_input_tokens": 2473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2473,
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
