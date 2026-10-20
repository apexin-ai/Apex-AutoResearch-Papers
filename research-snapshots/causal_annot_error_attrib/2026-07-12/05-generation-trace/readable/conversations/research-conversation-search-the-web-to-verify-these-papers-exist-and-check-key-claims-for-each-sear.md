# Research conversation: Search the web to verify these papers exist and check key claims. For each, search for the title and arXiv ID, and try t

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a553eed3e4789a795.jsonl`
- **Structured JSON:** [`8ebaac61abb62b30e26b.json`](../../sessions/8e/8ebaac61abb62b30e26b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-19T16:39:02.749Z_

Search the web to verify these papers exist and check key claims. For each, search for the title and arXiv ID, and try to access the arXiv page.

1. "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models" - arXiv 2604.01366, April 2026. Claims: linearly separable bias directions, family-dependent mitigation, 26-32% steering reduction.

2. "Predicting Where Steering Vectors Succeed" (Billa) - arXiv 2604.15557, April 2026. Claims: three-regime steerability framework, LAP diagnostic with ρ=0.86-0.91 across 24 concept families.

3. "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering" (Liu) - arXiv 2605.05715, May 2026. Claims: classification-correction gap, specificity ratio ≤0.152, bottleneck MLP achieves Δ=+2.8pp.

4. "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (Patel et al.) - arXiv 2604.19974, April 2026. Claims: pure incorrectness features functionally inert, SAE-based classification-correction gap.

5. "Discovery of Hidden Miscalibration Regimes" (Kobalczyk & van der Schaar) - arXiv 2605.13484, May 2026. Claims: opposing errors cancel when aggregated, worst-calibrated slices average 41% of instances.

Use web search and web fetch. Report concisely what exists vs what doesn't.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "6bd4649a-e029-4163-80ad-873635f9d163",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T16:39:02.753Z_

```json
{
  "parentUuid": "6bd4649a-e029-4163-80ad-873635f9d163",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
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
  "uuid": "63c45a6f-6e03-4526-8ce7-bfc38c2c7b3f",
  "timestamp": "2026-05-19T16:39:02.753Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T16:39:02.754Z_

```json
{
  "parentUuid": "63c45a6f-6e03-4526-8ce7-bfc38c2c7b3f",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "25c7fa4e-2713-4e8a-be4a-c989e4caf51b",
  "timestamp": "2026-05-19T16:39:02.754Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T16:39:05.616Z_



I'll search for each paper systematically. Let me start by loading the WebSearch and WebFetch tools, then search for all papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25c7fa4e-2713-4e8a-be4a-c989e4caf51b",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFs9x51rHgpXoXaCEt1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c2a4cfd-2bfe-45ed-ae50-f9dd3b21bd16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBKCQt3M96rRa4MhCEf8K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1730,
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

_source line 5 · 2026-05-19T16:39:05.978Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Vqmt8o2PS9VQYyPkeTfcBv`</summary>

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
  "parentUuid": "2c2a4cfd-2bfe-45ed-ae50-f9dd3b21bd16",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFs9x51rHgpXoXaCEt1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e54f6ab1-9867-4e71-ab28-91d5b3a23b6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfBKCQt3M96rRa4MhCEf8K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 7773,
      "output_tokens": 112,
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
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 7773,
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

### Tool result

_source line 6 · 2026-05-19T16:39:05.982Z_

<details><summary>↩ Tool result · `toolu_01Vqmt8o2PS9VQYyPkeTfcBv`</summary>

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
  "parentUuid": "e54f6ab1-9867-4e71-ab28-91d5b3a23b6a",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "e3349128-c4a5-448f-9da4-ac02e214966b",
  "sourceToolAssistantUUID": "e54f6ab1-9867-4e71-ab28-91d5b3a23b6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T16:39:09.168Z_



Now let me search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3349128-c4a5-448f-9da4-ac02e214966b",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFsQ1f9mMe72V3LaKvw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82168bf4-5414-4cdb-9b78-094bada21135",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhdD1Z3sjXTNzE55Lw3btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 8 · 2026-05-19T16:39:10.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VvmVTV29V2EPJ3ahpcP2iG`</summary>

```json
{
  "query": "arXiv 2604.01366 \"CogBias\" cognitive bias large language models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82168bf4-5414-4cdb-9b78-094bada21135",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFsQ1f9mMe72V3LaKvw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3117708-9e1f-405a-a36c-c6bb5c8978e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhdD1Z3sjXTNzE55Lw3btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 9 · 2026-05-19T16:39:10.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAxt6kYWSyC2qVAHhuQN1e`</summary>

```json
{
  "query": "arXiv 2604.15557 Billa \"Predicting Where Steering Vectors Succeed\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3117708-9e1f-405a-a36c-c6bb5c8978e5",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFsQ1f9mMe72V3LaKvw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35bc40f3-23aa-4029-90e8-97416e7b245e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhdD1Z3sjXTNzE55Lw3btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 10 · 2026-05-19T16:39:11.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GgTY87eoJwz4hQjqMx8Saw`</summary>

```json
{
  "query": "arXiv 2605.05715 Liu \"Decodable but Not Corrected\" steering residual stream 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35bc40f3-23aa-4029-90e8-97416e7b245e",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFsQ1f9mMe72V3LaKvw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf1e9255-5f72-4dd5-8745-4fe8fa0e9c39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhdD1Z3sjXTNzE55Lw3btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 11 · 2026-05-19T16:39:11.522Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FLBgSgp8eyFkkbuhhzGxK8`</summary>

```json
{
  "query": "arXiv 2604.19974 Patel \"LLM Uncertainty Correctness Same Features\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf1e9255-5f72-4dd5-8745-4fe8fa0e9c39",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFsQ1f9mMe72V3LaKvw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4de2591-84dd-4517-bf2c-2b4890234deb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhdD1Z3sjXTNzE55Lw3btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 12 · 2026-05-19T16:39:11.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XKVsS7hkKXKZqaJMfMPVW6`</summary>

```json
{
  "query": "arXiv 2605.13484 Kobalczyk van der Schaar \"Hidden Miscalibration Regimes\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4de2591-84dd-4517-bf2c-2b4890234deb",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFsQ1f9mMe72V3LaKvw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f10ba255-6d74-4609-b467-684584e45ea9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhdD1Z3sjXTNzE55Lw3btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 13 · 2026-05-19T16:39:18.624Z_

<details><summary>↩ Tool result · `toolu_01NAxt6kYWSyC2qVAHhuQN1e`</summary>

```text
Web search results for query: "arXiv 2604.15557 Billa "Predicting Where Steering Vectors Succeed" 2026"

Links: [{"title":"[2604.15557] Predicting Where Steering Vectors Succeed","url":"https://arxiv.org/abs/2604.15557"},{"title":"Predicting Where Steering Vectors Succeed","url":"https://arxiv.org/html/2604.15557"},{"title":"Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations","url":"https://arxiv.org/pdf/2602.17881"},{"title":"Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment","url":"https://arxiv.org/pdf/2604.03867"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/pdf/2603.24543"},{"title":"[2505.22637] Understanding (Un)Reliability of Steering Vectors in Language Models","url":"https://arxiv.org/abs/2505.22637"},{"title":"On the Non-Identifiability of Steering Vectors in Large Language Models","url":"https://arxiv.org/pdf/2602.06801"},{"title":"[2602.17881] Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations","url":"https://arxiv.org/abs/2602.17881"},{"title":"On the Limitations of Steering in Language Model Alignment","url":"https://arxiv.org/pdf/2505.01162"}]

I found the paper! Here's what I found about arXiv paper 2604.15557:

**Title:** "Predicting Where Steering Vectors Succeed"

**Author:** Jayadev Billa

**Submission Date:** April 16, 2026

**Main Contribution:**

The paper addresses the problem that steering vectors work for some concepts and layers but fail for others, with practitioners having no way to predict which setting applies before running an intervention. 

The authors introduce the Linear Accessibility Profile (LAP), a per-layer diagnostic that repurposes the logit lens as a predictor of steering vector effectiveness.

**Key Results:**

Across 24 controlled binary concept families on five models (Pythia-2.8B to Llama-8B), peak A_lin predicts steering effectiveness at ρ= +0.86 to +0.91 and layer selection at ρ= +0.63 to +0.92. A three-regime framework explains when difference-of-means steering works, when nonlinear methods are needed, and when no method can work.

The paper is available at https://arxiv.org/abs/2604.15557


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35bc40f3-23aa-4029-90e8-97416e7b245e",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "be492a09-8cfc-42f5-81d1-5b746d5393a4",
  "sourceToolAssistantUUID": "35bc40f3-23aa-4029-90e8-97416e7b245e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T16:39:18.740Z_

<details><summary>↩ Tool result · `toolu_01XKVsS7hkKXKZqaJMfMPVW6`</summary>

```text
Web search results for query: "arXiv 2605.13484 Kobalczyk van der Schaar "Hidden Miscalibration Regimes" 2026"

Links: [{"title":"[2605.13484] Discovery of Hidden Miscalibration Regimes","url":"https://arxiv.org/abs/2605.13484"},{"title":"Discovery of Hidden Miscalibration Regimes","url":"https://arxiv.org/html/2605.13484"},{"title":"Decision from Suboptimal Classifiers: Excess Risk Pre- and   Post-Calibration","url":"https://arxiv.org/pdf/2503.18025"},{"title":"Audited calibration under regime shift as a computational test of support-structured broadcast","url":"https://arxiv.org/pdf/2602.23382"},{"title":"Published as a conference paper at ICLR 2025","url":"https://www.arxiv.org/pdf/2503.04570"},{"title":"[2402.17509] Extreme Miscalibration and the Illusion of Adversarial Robustness","url":"https://arxiv.org/abs/2402.17509"},{"title":"Decision-Making under Miscalibration","url":"https://arxiv.org/pdf/2203.09852"}]

I found the paper! Here are the details for arXiv 2605.13484:

**Paper:** Discovery of Hidden Miscalibration Regimes

**Authors:** Katarzyna Kobalczyk and Mihaela van der Schaar from the University of Cambridge

**Submission Date:** 13 May 2026

**Main Contribution:**
The paper addresses how traditional calibration evaluation, which compares model confidence with empirical correctness, can hide substantial structure—models may be systematically overconfident on some kinds of inputs and underconfident on others, causing global reliability diagnostics to obscure localized calibration failures.

**Proposed Solution:**
The authors formulate the problem of discovering hidden miscalibration regimes without assuming access to predefined data slices, define a miscalibration field, and propose a diagnostic framework that learns a calibration-aware representation of the input space and estimates signed local miscalibration by kernel smoothing in the learned geometry.

**Key Findings:**
Across four real-world LLM benchmarks and twelve LLMs, the authors find that input-dependent calibration heterogeneity is prevalent.

You can access the full paper on arXiv at: https://arxiv.org/abs/2605.13484


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f10ba255-6d74-4609-b467-684584e45ea9",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "87dbc881-83ba-41dc-a720-a50877ea47b5",
  "sourceToolAssistantUUID": "f10ba255-6d74-4609-b467-684584e45ea9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T16:39:19.080Z_

<details><summary>↩ Tool result · `toolu_01GgTY87eoJwz4hQjqMx8Saw`</summary>

```text
Web search results for query: "arXiv 2605.05715 Liu "Decodable but Not Corrected" steering residual stream 2026"

Links: [{"title":"[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/abs/2605.05715"},{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/html/2604.02608v1"},{"title":"Exploration quantum steering, nonlocality and entanglement of two-qubit X-state in structured reservoirs","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5286411/"},{"title":"Exploration quantum steering, nonlocality and entanglement of two-qubit   X-state in structured reservoirs","url":"https://arxiv.org/pdf/1705.03194"},{"title":"[2605.01957] LLM-Augmented Semantic Steering of Text Embedding Projection Spaces","url":"https://arxiv.org/abs/2605.01957"}]

I found the paper! Here are the details about arXiv 2605.05715:

**Title:** "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes"

**Author:** Ming Liu from Amazon

**Core Research Question:** Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures?

**Key Findings:**
- The study investigates a classification-correction gap via Overthinking (OT)—a stable behavioral regime in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought
- OT is linearly decodable at 71.6% balanced accuracy
- Yet five families of fixed linear steering (29 configurations) all yield approximately zero change, with identical null results cross-architecture and cross-domain
- Three convergent lines of evidence suggest representational entanglement: the OT direction has 85–88% overlap with task-critical computation

**Submission Date:** 7 May 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf1e9255-5f72-4dd5-8745-4fe8fa0e9c39",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "6ba788bc-5921-4fc8-8735-f6fc8c3098a9",
  "sourceToolAssistantUUID": "bf1e9255-5f72-4dd5-8745-4fe8fa0e9c39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T16:39:20.103Z_

<details><summary>↩ Tool result · `toolu_01FLBgSgp8eyFkkbuhhzGxK8`</summary>

```text
Web search results for query: "arXiv 2604.19974 Patel "LLM Uncertainty Correctness Same Features" 2026"

Links: [{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation","url":"https://arxiv.org/pdf/2502.11620"},{"title":"Uncertainty-Based Abstention in LLMs Improves Safety and Reduces   Hallucinations","url":"https://arxiv.org/pdf/2404.10960"},{"title":"Toward Better Generalisation in Uncertainty Estimators: Leveraging Data-Agnostic Features","url":"https://arxiv.org/pdf/2507.03998"},{"title":"Pretrained LLMs Learn Multiple Types of Uncertainty","url":"https://arxiv.org/pdf/2505.21218"},{"title":"Efficient Uncertainty Estimation for LLM-based Entity Linking in Tabular Data","url":"https://arxiv.org/pdf/2510.01251"}]

I found the paper you're looking for! Here are the details:

**Title:** Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders

**ArXiv ID:** 2604.19974

**Authors:** Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, and Jia Chen

**Submission Date:** April 21, 2026

**Main Research Question:** The paper investigates whether large language models' output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.

**Key Methodology:** The researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.

**Main Findings:** When applied to Llama-3.1-8B and Gemma-2-9B, the study identifies three feature populations with different functional roles. Pure uncertainty features are functionally essential (suppressing them degrades accuracy), while pure incorrectness features are functionally inert (they show statistical differences but produce minimal accuracy changes when suppressed).

The paper is available on arXiv at https://arxiv.org/abs/2604.19974


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4de2591-84dd-4517-bf2c-2b4890234deb",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "8f8e5b77-8da0-4e77-abb1-0be06ea96d0e",
  "sourceToolAssistantUUID": "d4de2591-84dd-4517-bf2c-2b4890234deb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T16:39:22.667Z_

<details><summary>↩ Tool result · `toolu_01VvmVTV29V2EPJ3ahpcP2iG`</summary>

```text
Web search results for query: "arXiv 2604.01366 "CogBias" cognitive bias large language models 2026"

Links: [{"title":"[2604.01366] CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models","url":"https://arxiv.org/abs/2604.01366"},{"title":"CogBias: Measuring and Mitigating Cognitive Bias in Large ...","url":"https://arxiv.org/pdf/2604.01366"},{"title":"Balancing Rigor and Utility: Mitigating Cognitive Biases in Large   Language Models for Multiple-Choice Questions","url":"https://arxiv.org/pdf/2406.10999"},{"title":"Cognitive Effects in Large Language Models","url":"https://arxiv.org/pdf/2308.14337"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/pdf/2309.17012"},{"title":"Predicting Biased Human Decision-Making with Large Language Models in Conversational Settings","url":"https://arxiv.org/pdf/2601.11049"}]

Based on the search results, here's what I found about arXiv 2604.01366:

## CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models

This paper was submitted on April 1, 2026 by authors Fan Huang, Songheng Zhang, Haewoon Kwak, and Jisun An.

**Overview:**
The paper defines LLM cognitive bias as systematic, reproducible deviations from correct answers in tasks with computable ground-truth baselines, and introduces LLM CogBias, a benchmark organized around four families of cognitive biases: Judgment, Information Processing, Social, and Response.

**Key Research Questions:**
While prior work has shown that LLMs exhibit cognitive biases behaviorally, whether these biases correspond to identifiable internal representations and can be mitigated through targeted intervention remains an open question.

**Findings:**
The evaluation of three LLMs found that cognitive biases emerge systematically across all four families, with magnitudes and debiasing responses that are strongly family-dependent, with prompt-level debiasing substantially reducing Response biases.

**Context:**
This research addresses concerns as LLMs are deployed in high-stakes domains such as medical diagnosis, legal analysis, and financial decision-making.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3117708-9e1f-405a-a36c-c6bb5c8978e5",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "cc80a850-2ce5-46f4-b6e5-751dd75362d4",
  "sourceToolAssistantUUID": "e3117708-9e1f-405a-a36c-c6bb5c8978e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T16:39:26.802Z_

All five papers were found via search. Now let me fetch the actual arXiv abstract pages to verify specific claims more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc80a850-2ce5-46f4-b6e5-751dd75362d4",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFtd9TwXb8Q48TXfHyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a12dd3a-b1c7-401d-8e2d-5f8c59e922e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5u3mtetRwP63krqrvoY9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 10637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 19 · 2026-05-19T16:39:28.125Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A9FxnamP58SPCTvdWE2TDc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01366",
  "prompt": "Extract the full title, authors, submission date, and complete abstract. Look for any mention of: linearly separable bias directions, family-dependent mitigation, 26-32% steering reduction. Report exactly what claims are made."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a12dd3a-b1c7-401d-8e2d-5f8c59e922e9",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFtd9TwXb8Q48TXfHyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b40c401-8261-4da7-b951-e1273ca10d2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5u3mtetRwP63krqrvoY9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 10637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 20 · 2026-05-19T16:39:29.629Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DXx7zZQG6WUbn5T7tZYnNp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.15557",
  "prompt": "Extract the full title, authors, submission date, and complete abstract. Look for any mention of: three-regime steerability framework, LAP diagnostic, rho=0.86-0.91, 24 concept families. Report exactly what claims are made."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b40c401-8261-4da7-b951-e1273ca10d2a",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFtd9TwXb8Q48TXfHyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f9a411f-dade-462a-a6a1-d115a3b38bc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5u3mtetRwP63krqrvoY9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 10637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 21 · 2026-05-19T16:39:31.096Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PRxSH1b8kKRxTiGatTuAso`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05715",
  "prompt": "Extract the full title, authors, submission date, and complete abstract. Look for any mention of: classification-correction gap, specificity ratio 0.152, bottleneck MLP, delta +2.8pp. Report exactly what claims are made."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f9a411f-dade-462a-a6a1-d115a3b38bc5",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFtd9TwXb8Q48TXfHyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42bb8b4b-f326-403b-a730-96ae28cc4200",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5u3mtetRwP63krqrvoY9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 10637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 22 · 2026-05-19T16:39:32.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UsEiCa5aU59YiLhPvNgiAp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.19974",
  "prompt": "Extract the full title, authors, submission date, and complete abstract. Look for any mention of: pure incorrectness features functionally inert, SAE-based classification-correction gap. Report exactly what claims are made."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42bb8b4b-f326-403b-a730-96ae28cc4200",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFtd9TwXb8Q48TXfHyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c81479ec-90e8-46f2-a2f4-abd8ce6984bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5u3mtetRwP63krqrvoY9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 10637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 23 · 2026-05-19T16:39:32.410Z_

<details><summary>↩ Tool result · `toolu_01A9FxnamP58SPCTvdWE2TDc`</summary>

```text
# CogBias Paper Summary

**Full Title:** "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models"

**Authors:** Fan Huang, Songheng Zhang, Haewoon Kwak, Jisun An

**Submission Date:** April 1, 2026

**Complete Abstract:**
The paper introduces a benchmark for evaluating cognitive biases in LLMs across four families: Judgment, Information Processing, Social, and Response. Key findings include:

- **Linearly Separable Bias:** Using linear probes, the researchers demonstrated that "these biases are encoded as linearly separable directions in model activation space."

- **Family-Dependent Mitigation:** The abstract specifies that "debiasing responses that are strongly family-dependent: prompt-level debiasing substantially reduces Response biases but backfires for Judgment biases."

- **Steering Reduction:** The study reports "26--32% reduction in bias score (fraction of biased responses) while preserving downstream capability" through activation steering techniques.

- **Cross-Architecture Consistency:** Despite "near-orthogonal bias representations across models (mean cosine similarity 0.01)," steering effects generalize similarly across different architectures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b40c401-8261-4da7-b951-e1273ca10d2a",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "91440c80-b4c1-4576-b9a9-4b13cc6806a8",
  "sourceToolAssistantUUID": "1b40c401-8261-4da7-b951-e1273ca10d2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T16:39:33.317Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GJ7efMrGKpDwW9Mjcb4w5D`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.13484",
  "prompt": "Extract the full title, authors, submission date, and complete abstract. Look for any mention of: opposing errors cancel when aggregated, worst-calibrated slices average 41% of instances. Report exactly what claims are made."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91440c80-b4c1-4576-b9a9-4b13cc6806a8",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFtd9TwXb8Q48TXfHyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb17be01-9f2f-4178-a6f1-3a92b2bba134",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5u3mtetRwP63krqrvoY9a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 10637,
      "output_tokens": 614,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 968
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2702,
          "output_tokens": 614,
          "cache_read_input_tokens": 10637,
          "cache_creation_input_tokens": 968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 968,
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

_source line 25 · 2026-05-19T16:39:34.976Z_

<details><summary>↩ Tool result · `toolu_01DXx7zZQG6WUbn5T7tZYnNp`</summary>

```text
# Paper Summary

**Full Title:** "Predicting Where Steering Vectors Succeed"

**Author:** Jayadev Billa

**Submission Date:** April 16, 2026

**Complete Abstract:**
The research introduces a diagnostic tool called the Linear Accessibility Profile (LAP) that predicts when steering vectors will be effective. The key metric, A_lin, applies the model's unembedding matrix to hidden states without requiring training. Testing across "24 controlled binary concept families on five models (Pythia-2.8B to Llama-8B)" shows that peak A_lin predicts effectiveness with correlations ranging from +0.86 to +0.91 for steering success and +0.63 to +0.92 for layer selection. 

**Key Claims Mentioned:**

- The paper presents "a three-regime framework" explaining when difference-of-means steering succeeds, when nonlinear methods are needed, and when no method works
- An entity-steering demonstration confirms predictions function end-to-end on Gemma-2-2B and OLMo-2-1B-Instruct models
- The LAP-recommended layer redirects completions while "the middle layer (the standard heuristic) has no effect"

The work addresses the practical problem that practitioners lack advance prediction of steering vector effectiveness before running interventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f9a411f-dade-462a-a6a1-d115a3b38bc5",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "a5ad7dba-028a-46b1-9eb5-c13bf49e7fb9",
  "sourceToolAssistantUUID": "3f9a411f-dade-462a-a6a1-d115a3b38bc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T16:39:36.526Z_

<details><summary>↩ Tool result · `toolu_01PRxSH1b8kKRxTiGatTuAso`</summary>

```text
# Paper Summary

**Full Title:** "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes"

**Author:** Ming Liu

**Submission Date:** May 7, 2026

**Abstract:**
The research investigates whether linearly decodable failure signals in LLM hidden states can correct model failures. The study examines "Overthinking" (OT)—a behavioral regime in medical QA where models answer correctly under resampling but fail during extended reasoning.

## Key Findings

**Classification-Correction Gap:** The paper explicitly addresses this concept, showing that while OT is "linearly decodable at 71.6% balanced accuracy (p < 10^{-16})," attempts to correct failures through linear steering yielded "Delta ~= 0" across multiple configurations.

**Specificity Ratio:** The study reports "the OT direction has 85-88% overlap with task-critical computation (specificity ratio <= 0.152)," indicating substantial representational entanglement.

**Delta +2.8pp:** This specific metric does not appear in the document provided.

**Bottleneck MLP:** No mention of this term appears in the content above.

The paper concludes that while decodable failure structure supports reliability estimation through selective abstention (AUROC=0.610), fixed linear steering cannot exploit this for correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42bb8b4b-f326-403b-a730-96ae28cc4200",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "6bc61bdf-394a-48cc-9f2b-34a409907978",
  "sourceToolAssistantUUID": "42bb8b4b-f326-403b-a730-96ae28cc4200",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T16:39:37.304Z_

<details><summary>↩ Tool result · `toolu_01GJ7efMrGKpDwW9Mjcb4w5D`</summary>

```text
# Paper Summary

**Full Title:** Discovery of Hidden Miscalibration Regimes

**Authors:** Katarzyna Kobalczyk, Mihaela van der Schaar

**Submission Date:** May 13, 2026

**Abstract:** The paper addresses how calibration evaluation typically focuses on confidence versus correctness globally, which can mask important patterns. The researchers propose that "models may be systematically overconfident on some kinds of inputs and underconfident on others." Their framework discovers miscalibration without predefined data slices by learning calibration-aware representations and using kernel smoothing. Testing across LLM benchmarks reveals heterogeneous calibration patterns exist widely, and their approach effectively reduces calibration errors in problematic regions where standard methods like temperature scaling underperform.

**Specific Claims Mentioned:**
The webpage content does not contain the specific statistics you referenced (opposing errors canceling when aggregated or worst-calibrated slices averaging 41% of instances). These claims may appear in the full paper text, but they are not present in this abstract or webpage excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb17be01-9f2f-4178-a6f1-3a92b2bba134",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "aed8ced5-c4af-4b98-a2ce-eff868b38e33",
  "sourceToolAssistantUUID": "fb17be01-9f2f-4178-a6f1-3a92b2bba134",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T16:39:37.873Z_

<details><summary>↩ Tool result · `toolu_01UsEiCa5aU59YiLhPvNgiAp`</summary>

```text
# Paper Extraction Summary

**Full Title:** "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders"

**Authors:** Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, Jia Chen

**Submission Date:** April 21, 2026

## Key Claims from Abstract

**Pure Incorrectness Features:** The researchers report that "Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed."

**Additional Major Claims:**
- Pure uncertainty features are functionally essential—suppressing them substantially reduces accuracy
- Confounded features (encoding both signals) are detrimental and their targeted suppression yields 1.1% accuracy improvement and 75% entropy reduction
- Just 3 confounded features from a single mid-network layer can predict model correctness with AUROC ~0.79
- Selective abstention using this approach raises accuracy from 62% to 81% at 53% coverage

The work demonstrates uncertainty and correctness operate through distinct internal mechanisms in large language models, with implications for interpretability and inference-time interventions.

**Note:** No mention of "SAE-based classification-correction gap" terminology appears in the provided abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c81479ec-90e8-46f2-a2f4-abd8ce6984bd",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "693ce213-51ed-4ffb-af28-3bdf0b176506",
  "sourceToolAssistantUUID": "c81479ec-90e8-46f2-a2f4-abd8ce6984bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T16:39:40.990Z_

Now let me try to fetch the HTML versions of papers 3 and 5 to check for the specific claims not found in the abstracts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "693ce213-51ed-4ffb-af28-3bdf0b176506",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFuk9BSFLeqXRgmLXLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9309703-04e2-42dd-aefd-edfadc7efc12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eSVr4SVRdtdhg8PrH4gzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 4630,
      "cache_read_input_tokens": 11605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4630,
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

_source line 30 · 2026-05-19T16:39:42.081Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L3phHq5Xv1XNg4eyE1pJeV`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05715",
  "prompt": "Search for these specific claims: (1) \"bottleneck MLP\" achieving Delta=+2.8pp, (2) any mention of +2.8 percentage points improvement. Report whether these claims appear anywhere in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9309703-04e2-42dd-aefd-edfadc7efc12",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFuk9BSFLeqXRgmLXLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d33d8be-3ec4-44a3-abcb-1ef6d7a93f9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eSVr4SVRdtdhg8PrH4gzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 4630,
      "cache_read_input_tokens": 11605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4630,
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

_source line 31 · 2026-05-19T16:39:43.249Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N6kft46PVTdoYzymWyzBuW`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.13484",
  "prompt": "Search for these specific claims: (1) \"opposing errors cancel when aggregated\", (2) \"worst-calibrated slices average 41% of instances\", (3) any mention of 41%. Report whether these claims appear anywhere in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d33d8be-3ec4-44a3-abcb-1ef6d7a93f9a",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFuk9BSFLeqXRgmLXLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ddfeb3-43a5-429a-863c-dfe2cec8ee25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eSVr4SVRdtdhg8PrH4gzx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 4630,
      "cache_read_input_tokens": 11605,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4630
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 265,
          "output_tokens": 280,
          "cache_read_input_tokens": 11605,
          "cache_creation_input_tokens": 4630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4630,
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

_source line 32 · 2026-05-19T16:39:46.746Z_

<details><summary>↩ Tool result · `toolu_01L3phHq5Xv1XNg4eyE1pJeV`</summary>

```text
# Claims Verification Report

## Finding: Both claims appear in the paper

**(1) "Bottleneck MLP" achieving Delta=+2.8pp**

This claim is confirmed. The paper states: "A learned non-linear residual MLP (4096→64→4096 bottleneck..." in Appendix D, which achieves the specified improvement.

**(2) Any mention of +2.8 percentage points improvement**

This figure appears multiple times throughout the document:

- In the abstract: "a learned non-linear residual MLP...achieves Δ=+2.8pp (p=0.025)"
- In Section 6 Discussion: "Preliminary evidence supports this: a learned non-linear... MLP...achieves Δ=+2.8pp"
- In the Limitations section: "a learned non-linear MLP (4096→64→4096...) achieves Δ=+2.8pp (p=0.025)"

The +2.8pp improvement represents a positive result from a learned non-linear intervention, though the authors note this is "modest relative to the 50.6% centroid-distance reduction" and suggests "only partial disentanglement" of representational entanglement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d33d8be-3ec4-44a3-abcb-1ef6d7a93f9a",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "918432be-957f-4e50-a61c-ef8de10c56bf",
  "sourceToolAssistantUUID": "9d33d8be-3ec4-44a3-abcb-1ef6d7a93f9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T16:39:47.163Z_

<details><summary>↩ Tool result · `toolu_01N6kft46PVTdoYzymWyzBuW`</summary>

```text
I searched the provided paper content for the three specific claims you requested.

**Claim 1: "opposing errors cancel when aggregated"**
✓ **Found.** The paper states: "opposing errors cancel when aggregated by confidence" (in the Hidden Regimes section discussing how global reliability diagrams can hide calibration failures).

**Claim 2: "worst-calibrated slices average 41% of instances"**
✓ **Found.** The validity section reports: "the worst-calibrated slice contains on average 41% of test examples."

**Claim 3: Any mention of 41%**
✓ **Found.** The same passage cited above is the only occurrence of this specific percentage in the paper.

All three claims appear in the document. The 41% figure relates to the size of the worst-calibrated slice among the 18 dataset-model pairs exhibiting significant calibration heterogeneity (those with worst-slice smoothed ECE gaps of at least 0.06).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ddfeb3-43a5-429a-863c-dfe2cec8ee25",
  "isSidechain": true,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "agentId": "a553eed3e4789a795",
  "type": "user",
  "uuid": "7c46d2b2-c063-4595-ab49-e81480bfef89",
  "sourceToolAssistantUUID": "b4ddfeb3-43a5-429a-863c-dfe2cec8ee25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-19T16:40:03.848Z_

All verification is complete. Here is the summary:

---

**Verification Results: All 5 Papers Exist and Are Real**

**Paper 1: "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models" (arXiv 2604.01366)**
- **EXISTS.** Authors: Fan Huang, Songheng Zhang, Haewoon Kwak, Jisun An. Submitted April 1, 2026.
- Claim "linearly separable bias directions": **CONFIRMED** -- abstract states biases are "encoded as linearly separable directions in model activation space."
- Claim "family-dependent mitigation": **CONFIRMED** -- debiasing is "strongly family-dependent."
- Claim "26-32% steering reduction": **CONFIRMED** -- paper reports "26--32% reduction in bias score."

**Paper 2: "Predicting Where Steering Vectors Succeed" (arXiv 2604.15557)**
- **EXISTS.** Author: Jayadev Billa. Submitted April 16, 2026.
- Claim "three-regime steerability framework": **CONFIRMED** -- describes when difference-of-means steering works, when nonlinear methods are needed, and when no method works.
- Claim "LAP diagnostic with rho=0.86-0.91 across 24 concept families": **CONFIRMED** -- peak A_lin predicts steering effectiveness at rho=+0.86 to +0.91 across 24 binary concept families on five models.

**Paper 3: "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering" (arXiv 2605.05715)**
- **EXISTS.** Author: Ming Liu (Amazon). Submitted May 7, 2026.
- Claim "classification-correction gap": **CONFIRMED** -- OT linearly decodable at 71.6% balanced accuracy but steering yields Delta approximately 0.
- Claim "specificity ratio <= 0.152": **CONFIRMED** -- OT direction has 85-88% overlap with task-critical computation, specificity ratio <= 0.152.
- Claim "bottleneck MLP achieves Delta=+2.8pp": **CONFIRMED** -- a learned non-linear residual MLP (4096->64->4096 bottleneck) achieves Delta=+2.8pp (p=0.025).

**Paper 4: "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (arXiv 2604.19974)**
- **EXISTS.** Authors: Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, Jia Chen. Submitted April 21, 2026.
- Claim "pure incorrectness features functionally inert": **CONFIRMED** -- explicitly stated in the abstract: they show statistically significant activation differences but produce "near-zero change in accuracy when suppressed."
- Claim "SAE-based classification-correction gap": **PARTIALLY CONFIRMED** -- the paper uses SAEs and demonstrates a dissociation between decodability and functional impact (i.e., a classification-correction gap), but does not use that exact term. The concept is present; the specific phrase is not.

**Paper 5: "Discovery of Hidden Miscalibration Regimes" (arXiv 2605.13484)**
- **EXISTS.** Authors: Katarzyna Kobalczyk, Mihaela van der Schaar (University of Cambridge). Submitted May 13, 2026.
- Claim "opposing errors cancel when aggregated": **CONFIRMED** -- paper states "opposing errors cancel when aggregated by confidence."
- Claim "worst-calibrated slices average 41% of instances": **CONFIRMED** -- paper reports "the worst-calibrated slice contains on average 41% of test examples."

**Bottom line:** All five papers are real, published on arXiv at the stated IDs and dates. All key claims checked out against the actual paper content, with only one minor nuance: Paper 4 demonstrates the classification-correction gap concept via SAEs but does not use that exact phrase.

Sources:
- [CogBias (2604.01366)](https://arxiv.org/abs/2604.01366)
- [Predicting Where Steering Vectors Succeed (2604.15557)](https://arxiv.org/abs/2604.15557)
- [Decodable but Not Corrected (2605.05715)](https://arxiv.org/abs/2605.05715)
- [LLM Uncertainty and Correctness Features (2604.19974)](https://arxiv.org/abs/2604.19974)
- [Hidden Miscalibration Regimes (2605.13484)](https://arxiv.org/abs/2605.13484)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c46d2b2-c063-4595-ab49-e81480bfef89",
  "isSidechain": true,
  "agentId": "a553eed3e4789a795",
  "requestId": "req_011CbCFvRs7XjtcHhkU1cBKN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "088b3c67-61aa-419f-b74f-fa947cee1608",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJghgVRovCW99CJDk8ww2c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 16235,
      "output_tokens": 1150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1150,
          "cache_read_input_tokens": 16235,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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
