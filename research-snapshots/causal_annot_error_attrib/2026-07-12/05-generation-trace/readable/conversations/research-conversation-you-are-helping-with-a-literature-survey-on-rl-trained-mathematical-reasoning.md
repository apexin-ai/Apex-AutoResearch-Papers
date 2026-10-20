# Research conversation: You are helping with a literature survey on RL-trained mathematical reasoning robustness. Search for the most important 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a74cf45dec59802ec.jsonl`
- **Structured JSON:** [`6e6581ae2c3d3627f29a.json`](../../sessions/6e/6e6581ae2c3d3627f29a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-29T05:23:43.344Z_

You are helping with a literature survey on RL-trained mathematical reasoning robustness. Search for the most important papers (2024-2026) on:

1. Mathematical reasoning robustness under perturbation (numerical substitution, variable renaming, distractor insertion)
2. Benchmarks measuring LLM math reasoning fragility (GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, etc.)
3. Training-time interventions for math reasoning robustness

Execute these searches and for EVERY promising paper, fetch its arXiv abstract:

Search 1: "mathematical reasoning robustness perturbation LLM 2025 2026"
Search 2: "GSM-Symbolic GSM-Plus VAR-MATH benchmark math reasoning fragility"
Search 3: "math reasoning LLM accuracy drop perturbation numerical substitution"
Search 4: "MATH-Perturb benchmark mathematical reasoning evaluation robustness"
Search 5: "training robustness mathematical reasoning language model 2025"

For each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:
- Full title
- Authors (first author et al.)
- Venue/year
- URL
- What the paper does (1-2 sentences)
- Why it's important (awards, citations, influence)

Find at least 5-8 distinct papers. Focus on papers that are highly cited or from top venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "295de006-ddc9-48fb-8c22-6ee6895d8ed1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:23:43.349Z_

```json
{
  "parentUuid": "295de006-ddc9-48fb-8c22-6ee6895d8ed1",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
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
  "uuid": "d88dc72d-d9ad-42ae-b8df-5eccb8ec78ee",
  "timestamp": "2026-05-29T05:23:43.349Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:23:43.350Z_

```json
{
  "parentUuid": "d88dc72d-d9ad-42ae-b8df-5eccb8ec78ee",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "347e51c7-ab88-4bce-a4d3-e6dbeeeb1bd0",
  "timestamp": "2026-05-29T05:23:43.350Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:23:46.000Z_



I'll start by loading the WebSearch and WebFetch tools, then execute the searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "347e51c7-ab88-4bce-a4d3-e6dbeeeb1bd0",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTTEPDqAiminnRJfGG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf02f1c5-83ab-45a3-ba85-ea8818bc4d68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9wyxxM3cTsgudPyehLXXT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9088,
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

_source line 5 · 2026-05-29T05:23:46.086Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HHKDEzD5k5c7bQBwQj3v1G`</summary>

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
  "parentUuid": "bf02f1c5-83ab-45a3-ba85-ea8818bc4d68",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTTEPDqAiminnRJfGG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53081cbd-529e-46f1-a8b4-13bfa576d7c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9wyxxM3cTsgudPyehLXXT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9088,
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

_source line 6 · 2026-05-29T05:23:46.090Z_

<details><summary>↩ Tool result · `toolu_01HHKDEzD5k5c7bQBwQj3v1G`</summary>

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
  "parentUuid": "53081cbd-529e-46f1-a8b4-13bfa576d7c7",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "b6e6005f-224e-494e-bc9a-e1b820bee3c9",
  "sourceToolAssistantUUID": "53081cbd-529e-46f1-a8b4-13bfa576d7c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:23:48.418Z_



Now let me execute all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6e6005f-224e-494e-bc9a-e1b820bee3c9",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTf9jScNKWcBXWAu7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4d3adc2-b2a3-4e23-b6eb-69396605083f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tYJSYJtkks62NJTqtzT4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9088,
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

_source line 8 · 2026-05-29T05:23:48.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UKM2H7pbRMfDrU1o6U8BLr`</summary>

```json
{
  "query": "mathematical reasoning robustness perturbation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d3adc2-b2a3-4e23-b6eb-69396605083f",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTf9jScNKWcBXWAu7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50433343-07d8-4a2c-9759-931ab3ff8fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tYJSYJtkks62NJTqtzT4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9088,
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

_source line 9 · 2026-05-29T05:23:49.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XvUfiEpq8Fe6bqjbRxHnAD`</summary>

```json
{
  "query": "GSM-Symbolic GSM-Plus VAR-MATH benchmark math reasoning fragility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50433343-07d8-4a2c-9759-931ab3ff8fbe",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTf9jScNKWcBXWAu7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68945ef0-ebfe-46ac-98b8-da1b8268993e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tYJSYJtkks62NJTqtzT4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9088,
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

_source line 10 · 2026-05-29T05:23:49.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AtxMvagbNtGCFJPcyL3LF9`</summary>

```json
{
  "query": "math reasoning LLM accuracy drop perturbation numerical substitution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68945ef0-ebfe-46ac-98b8-da1b8268993e",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTf9jScNKWcBXWAu7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61be1d8f-fbfa-42cb-9908-27561df0b2d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tYJSYJtkks62NJTqtzT4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9088,
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

_source line 11 · 2026-05-29T05:23:49.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QrT8TQgTVirCqZAEjZyQdo`</summary>

```json
{
  "query": "MATH-Perturb benchmark mathematical reasoning evaluation robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61be1d8f-fbfa-42cb-9908-27561df0b2d3",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTf9jScNKWcBXWAu7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "476f58b0-bad7-43f5-a163-70a4574b2708",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tYJSYJtkks62NJTqtzT4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9088,
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

_source line 12 · 2026-05-29T05:23:50.059Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JQPcQK32vKfow1pPszGNX6`</summary>

```json
{
  "query": "training robustness mathematical reasoning language model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476f58b0-bad7-43f5-a163-70a4574b2708",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJTf9jScNKWcBXWAu7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "087951f0-084e-49dd-a76e-6bc10063e0f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tYJSYJtkks62NJTqtzT4H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 9088,
      "output_tokens": 273,
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
          "output_tokens": 273,
          "cache_read_input_tokens": 9088,
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

_source line 13 · 2026-05-29T05:23:56.781Z_

<details><summary>↩ Tool result · `toolu_01XvUfiEpq8Fe6bqjbRxHnAD`</summary>

```text
Web search results for query: "GSM-Symbolic GSM-Plus VAR-MATH benchmark math reasoning fragility"

Links: [{"title":"GSM-Symbolic: A Rigorous LLM Math Benchmark","url":"https://www.emergentmind.com/topics/gsm-symbolic-benchmark"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=AjXkRZIvjB"},{"title":"Musing 88: GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models","url":"https://aiscientist.substack.com/p/musing-88-gsm-symbolic-understanding"},{"title":"GSM-Symbolic: Evaluating LLM Mathematical Reasoning","url":"https://www.emergentmind.com/topics/gsm-symbolic-approach"},{"title":"GSM-Symbolic: Understanding the limitations of mathematical reasoning in large language models - ~tech - Tildes","url":"https://tildes.net/~tech/1jkc/gsm_symbolic_understanding_the_limitations_of_mathematical_reasoning_in_large_language_models"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/pdf/2507.12885"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/html/2410.05229v1"},{"title":"Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING","url":"https://arxiv.org/pdf/2410.05229"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/gsm-symbolic"},{"title":"[2410.05229] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/abs/2410.05229"}]

Based on the search results, here's what I found about these benchmarks and math reasoning fragility:

## GSM-Symbolic Benchmark

GSM-Symbolic is an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions. It systematically instantiates templates with varied numerical and textual inputs to measure accuracy, variance, and performance drops under subtle problem changes.

## Key Findings on Math Reasoning Fragility

The research reveals significant fragility in LLM mathematical reasoning:

- The performance of all models declines when only the numerical values in the question are altered in the GSM-Symbolic benchmark.

- Adding a single clause that seems relevant to the question causes significant performance drops (up to 65%) across all state-of-the-art models, even though the clause doesn't contribute to the reasoning chain needed for the final answer.

- As the number of clauses increases from baseline through Symbolic to Plus-1 and Plus-2, accuracy declines approximately linearly with an accelerating rate, and variance rises accordingly.

## VAR-MATH Benchmark

VAR-MATH conducts extensive empirical studies on VAR-AMC23, VAR-AIME24, and VAR-AIME25, revealing substantial performance declines in RL-finetuned models and exposing the limitations of current RL strategies in cultivating genuine reasoning.

## Interpretation

The LLMs' high performance variance on different instances of the same question, their significant drop in performance with a slight increase in difficulty, and their sensitivity to inconsequential information indicate that their reasoning is fragile and may be more akin to sophisticated pattern matching rather than true logical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68945ef0-ebfe-46ac-98b8-da1b8268993e",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "0f747270-23f8-4203-ad07-4f77ab214d60",
  "sourceToolAssistantUUID": "68945ef0-ebfe-46ac-98b8-da1b8268993e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T05:23:56.827Z_

<details><summary>↩ Tool result · `toolu_01UKM2H7pbRMfDrU1o6U8BLr`</summary>

```text
Web search results for query: "mathematical reasoning robustness perturbation LLM 2025 2026"

Links: [{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems | OpenReview","url":"https://openreview.net/forum?id=b8GuXlLc1y"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2511.08022"},{"title":"Exploring LLM Reasoning Through Controlled Prompt Variations","url":"https://arxiv.org/pdf/2504.02111"},{"title":"An Investigation of Robustness of LLMs in Mathematical ...","url":"https://arxiv.org/pdf/2508.08833"},{"title":"Evaluating Robustness of Reasoning Models on Parameterized Logical Problems","url":"https://arxiv.org/html/2602.12665"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/pdf/2511.08055"},{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"}]

Based on the web search results, here's what I found regarding mathematical reasoning robustness and perturbations in LLMs for 2025-2026:

## Key Research Findings

**Robust Reasoning Benchmark (RRB)**: A pipeline of 13 deterministic textual perturbations was applied to AIME 2024 and AIME 2025 to evaluate state-of-the-art models. Frontier models are largely resilient, with the notable exception of Claude, which categorically refuses many transformed prompts; open-weights reasoning models exhibit cognitive thrashing and tokenization breakdown.

**PutnamGAP Framework (2026)**: A GAP framework and 6,306-item PutnamGAP benchmark was introduced, showing that even top LLMs suffer large accuracy drops when math-equivalent problems are reworded or reparametrized. OpenAI's flagship reasoning model, O3, scores 51.5% on the originals but drops by 4.7 percentage points on surface-renaming variants, and by 12.9 percentage points on parametric variants.

**MATH-Perturb Study**: Significant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

**Pattern Matching Concerns**: Research shows that the reasoning process of current LLMs essentially relies on complex pattern matching rather than formal mathematical reasoning.

These studies collectively demonstrate vulnerabilities in LLM mathematical reasoning when faced with textual, parametric, or structural perturbations despite strong baseline performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50433343-07d8-4a2c-9759-931ab3ff8fbe",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "70034a4e-1cf4-4b09-a77b-eeab49614a64",
  "sourceToolAssistantUUID": "50433343-07d8-4a2c-9759-931ab3ff8fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-29T05:23:57.416Z_

<details><summary>↩ Tool result · `toolu_01AtxMvagbNtGCFJPcyL3LF9`</summary>

```text
Web search results for query: "math reasoning LLM accuracy drop perturbation numerical substitution"

Links: [{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/html/2511.08022"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/html/2503.04550v1"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2511.08022"},{"title":"MathRobust-LV: Evaluation of Large Language Models’ Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/html/2510.06430v1"},{"title":"MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/pdf/2511.08055"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"Mathematical Reasoning in Large Language Models: Assessing Logical and   Arithmetic Errors across Wide Numerical Ranges","url":"https://arxiv.org/pdf/2502.08680"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"Mathematical Reasoning in Large Language Models: Assessing Logical and Arithmetic Errors across Wide Numerical Ranges","url":"https://arxiv.org/html/2502.08680v1"}]

Based on the search results, I found several relevant studies on how large language models' math reasoning accuracy is affected by perturbations and numerical substitutions:

## Key Findings

**Numerical Perturbations Cause Significant Accuracy Drops:**

When models are disturbed by perturbation sentences with numbers, all models experience a sharp performance drop, with accuracy dropping by up to 51.55% under strong perturbation conditions. In contrast, when disturbed by perturbation sentences without numbers, models initially exhibit strong robustness, with performance remaining at or near original levels.

**Sensitivity to Numerical Information:**

Models are more sensitive to perturbations with numerical information and are more likely to give incorrect answers when disturbed by irrelevant numerical information. LLMs such as GPT-4o exhibit notable fragility when numerical values are perturbed, with replacing numbers leading to a 5% accuracy drop in GPT-4o.

**Performance Across Different Models:**

Open source models with smaller parameters decrease by nearly or more than 10%, with maximum decreases reaching 51.55%, while even the most advanced commercial LLMs have seen a 3%-10% performance drop.

**Logical vs. Arithmetic Errors:**

Logical error rates increase by up to 14 absolute percentage points as perturbation levels rise, even though the logical reasoning process required to solve the problems remains unchanged despite numerical modifications, suggesting that logical reasoning in LLMs tends to exacerbate for out-of-distribution numerical values.

These findings highlight a fundamental vulnerability in LLMs' mathematical reasoning capabilities related to their sensitivity to numerical perturbations and substitutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61be1d8f-fbfa-42cb-9908-27561df0b2d3",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "af452db3-1365-44df-ad9d-83f1718c66a1",
  "sourceToolAssistantUUID": "61be1d8f-fbfa-42cb-9908-27561df0b2d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T05:23:57.547Z_

<details><summary>↩ Tool result · `toolu_01QrT8TQgTVirCqZAEjZyQdo`</summary>

```text
Web search results for query: "MATH-Perturb benchmark mathematical reasoning evaluation robustness"

Links: [{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"},{"title":"T-Math Reasoning Benchmark","url":"https://www.emergentmind.com/topics/t-math-reasoning-benchmark"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities","url":"https://arxiv.org/pdf/2502.06453"},{"title":"[PDF] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MATH-Perturb:-Benchmarking-LLMs'-Math-Reasoning-Huang-Guo/5d2ffdc8a0970642372f6742e191c892e41a6a9b"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"}]

Based on the search results, here's what I found about the MATH-Perturb benchmark:

## Overview

MATH-Perturb is a new benchmark for testing math reasoning in large language models (LLMs) that tests model performance against deliberate perturbations of math problems and evaluates robustness of LLMs' mathematical abilities.

## Purpose and Methodology

The test takes existing math problems and changes how they're worded without altering the core problem to reveal whether AI models genuinely understand mathematics or are just good at recognizing familiar patterns. The benchmark constructs MATH-P-Simple and MATH-P-Hard via simple perturbation and hard perturbation, respectively, consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.

Prior work has constructed mathematical benchmarks when questions undergo simple perturbations—modifications that still preserve the underlying reasoning patterns of the solutions. However, MATH-Perturb explores hard perturbations, which fundamentally change the nature of the problem so that the original solution steps do not apply.

## Key Findings

All models benchmarked, including o1-mini and gemini-2.0-flash-thinking, suffer significant performance drops (10%-25%) on MATH-P-Hard. More specifically, significant performance drops are observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

The research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "476f58b0-bad7-43f5-a163-70a4574b2708",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "ec333636-b7ae-428e-83fb-ea9d7cc53799",
  "sourceToolAssistantUUID": "476f58b0-bad7-43f5-a163-70a4574b2708",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T05:24:00.969Z_

<details><summary>↩ Tool result · `toolu_01JQPcQK32vKfow1pPszGNX6`</summary>

```text
Web search results for query: "training robustness mathematical reasoning language model 2025"

Links: [{"title":"MathRobust-LV: Evaluation of Large Language Models’ Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/html/2510.06430"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v2"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"[2604.08571] Robust Reasoning Benchmark","url":"https://arxiv.org/abs/2604.08571"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/html/2503.04550v1"},{"title":"A Causal Framework to Quantify the Robustness of Mathematical Reasoning   with Language Models","url":"https://arxiv.org/pdf/2210.12023"}]

Based on the web search results, here's what recent research shows about training robustness in mathematical reasoning for language models in 2025:

## Key Research Areas

**Robustness Evaluation Frameworks:**
MathRobust-LV is a new methodology for evaluating linguistic robustness in math reasoning, grounded in minimal but meaning-preserving rewordings. Additionally, Math-RoB is a synthetic benchmark that enables robustness evaluation against data contamination through an instruction-based approach.

**Multiple Robustness Approaches:**
Recent work has examined various aspects of robustness, including non-semantic noise such as punctuation insertions, or numerical perturbations in operands and constants, revealing weaknesses in both arithmetic and reasoning steps. The Robust Reasoning Benchmark (RRB) applies 13 deterministic textual perturbations to AIME 2024 and AIME 2025.

**Training Challenges:**
Synthetic CoT supervision enables scalable instruction tuning but often reproduces the biases and shortcuts of the teacher model generating the traces, reducing diversity in reasoning strategies.

**Out-of-Distribution Generalization:**
Current benchmarks inadequately evaluate out-of-distribution generalization, as many datasets rely on stable problem templates encouraging pattern recognition rather than transferable abstraction, with models frequently solving familiar formats while failing on structurally novel variants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "087951f0-084e-49dd-a76e-6bc10063e0f5",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "dbc7dd2f-b180-48c1-81b3-7c1da414102f",
  "sourceToolAssistantUUID": "087951f0-084e-49dd-a76e-6bc10063e0f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-29T05:24:04.381Z_

I have a solid set of candidate papers. Now let me fetch the arXiv abstracts for each distinct paper I've identified. Let me fetch them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc7dd2f-b180-48c1-81b3-7c1da414102f",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92c997b4-322f-4325-85f4-b54abe91e266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 19 · 2026-05-29T05:24:05.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FZg2JBaeGFmBR23dU6j2qq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.05229",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92c997b4-322f-4325-85f4-b54abe91e266",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01b9179d-e1fd-4703-ac63-e09379511b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 20 · 2026-05-29T05:24:06.241Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gx7Pt6f1DXDEBaG9tvNiBU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06453",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b9179d-e1fd-4703-ac63-e09379511b70",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36f9f2cc-a9b2-4465-837a-483ba61f8d4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 21 · 2026-05-29T05:24:07.213Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0139eBZ7XWhPd5N8hwv7sYwr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08571",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f9f2cc-a9b2-4465-837a-483ba61f8d4c",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f02dfb6-a7bc-4778-aacc-06bfac1dd8b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 22 · 2026-05-29T05:24:07.722Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K28PUUnMXSEVZBnczaBeyv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.08022",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f02dfb6-a7bc-4778-aacc-06bfac1dd8b1",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55da381b-f1ab-4155-8102-f5a64b2b606f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 23 · 2026-05-29T05:24:08.694Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FuuyFXU37MHpHQxymLWLsw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.08833",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55da381b-f1ab-4155-8102-f5a64b2b606f",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cc582f1-bcfa-4719-81a0-7a44e60182a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 24 · 2026-05-29T05:24:09.572Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EWrENtYnjywKDjezUcqP8L`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.04550",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cc582f1-bcfa-4719-81a0-7a44e60182a6",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50762e43-b865-4688-83cb-90c39a60d9e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 25 · 2026-05-29T05:24:10.038Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016vFb5hnpewWmwmFZkAZPdc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.06430",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50762e43-b865-4688-83cb-90c39a60d9e2",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "632b7a5b-b8ca-4d43-962b-adab1759eaa5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 26 · 2026-05-29T05:24:10.244Z_

<details><summary>↩ Tool result · `toolu_01FZg2JBaeGFmBR23dU6j2qq`</summary>

```text
# Paper Information

**Full Title:**
"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models"

**Authors:**
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar

**Submission Date:**
October 7, 2024 (v1); Last revised August 27, 2025 (v2)

**Venue:**
ICLR (International Conference on Learning Representations) - camera ready version

**Abstract Summary:**
The researchers developed GSM-Symbolic, an improved benchmark using symbolic templates to evaluate LLMs' mathematical reasoning on grade-school problems. Their investigation revealed that models show significant performance variance across different instantiations of identical questions. They found that "performance of all models declines when only the numerical values in the question are altered" and that adding seemingly relevant but logically unnecessary clauses causes accuracy drops up to 65%. The authors conclude that current LLMs likely replicate memorized reasoning patterns rather than performing genuine logical reasoning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01b9179d-e1fd-4703-ac63-e09379511b70",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "ee6683bc-3458-4d5b-9123-0e3366913251",
  "sourceToolAssistantUUID": "01b9179d-e1fd-4703-ac63-e09379511b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T05:24:10.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0123pNxK4KDkftswiCXfEz2k`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.12885",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee6683bc-3458-4d5b-9123-0e3366913251",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJUkaC5P9JDoVJ28HSo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7f764dc-e28c-4a6f-8ef7-3f4a8dbdf69c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017T1MTashuzN5xfZtgJ8tWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4543,
      "cache_read_input_tokens": 10212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4543,
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

_source line 28 · 2026-05-29T05:24:11.703Z_

<details><summary>↩ Tool result · `toolu_0139eBZ7XWhPd5N8hwv7sYwr`</summary>

```text
# Robust Reasoning Benchmark - Paper Details

**Full Title:** Robust Reasoning Benchmark

**Authors:**
- Pavel Golikov
- Evgenii Opryshko
- Gennady Pekhimenko
- Mark C. Jeffrey

**Submission Date:** March 26, 2026 (v1); Last revised May 20, 2026 (v2)

**Abstract Summary:**
The researchers introduce a testing pipeline applying textual perturbations to mathematical problems from AIME 2024-2025. Their evaluation of eight advanced models revealed that frontier systems remain relatively stable, though Claude "categorically refuses many transformed prompts." Open-source reasoning models showed significant vulnerabilities, with accuracy dropping up to 54% across perturbations. The study identifies "Intra-Query Attention Dilution," where solving multiple math problems sequentially causes performance degradation on subsequent problems. The authors argue that future architectures require "explicit contextual resets within models' own chain-of-thought" to achieve reliable reasoning.

**Venue/Conference Information:** None specified. This is an arXiv preprint (cs.LG category) with no conference affiliation mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f02dfb6-a7bc-4778-aacc-06bfac1dd8b1",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "61b10da6-8251-4396-a3c2-49acbba574ac",
  "sourceToolAssistantUUID": "9f02dfb6-a7bc-4778-aacc-06bfac1dd8b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-29T05:24:12.238Z_

<details><summary>↩ Tool result · `toolu_01K28PUUnMXSEVZBnczaBeyv`</summary>

```text
# Paper Information

**Full Title:**
"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models"

**Authors:**
- Zhishen Sun
- Guang Dai
- Ivor Tsang
- Haishan Ye

**Submission Date:**
November 11, 2025

**Complete Abstract:**
The researchers propose a perturbation framework to evaluate LLMs' reasoning capabilities by introducing "semantically irrelevant perturbation sentences" and progressively intensifying them. Testing shows models remain stable against non-numerical disruptions but encounter robustness challenges as intensity increases. When facing numerical perturbations, performance degrades significantly—smaller open-source models experience drops exceeding 10%, reaching up to 51.55% at maximum intensity, while advanced commercial models show 3-10% declines. Analysis reveals models are disproportionately sensitive to irrelevant numbers. Additionally, models maintain 20-40% accuracy even without core instructions, suggesting reliance on pattern-matching rather than logical reasoning. The study highlights fundamental limitations in current LLM reasoning capabilities.

**Venue/Conference Information:**
No specific conference or venue is mentioned. The paper is classified as a Computer Science > Artificial Intelligence (cs.AI) submission to arXiv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55da381b-f1ab-4155-8102-f5a64b2b606f",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "3b510ed4-f031-4ce8-83d9-ebc132b0a9d7",
  "sourceToolAssistantUUID": "55da381b-f1ab-4155-8102-f5a64b2b606f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T05:24:12.726Z_

<details><summary>↩ Tool result · `toolu_01Gx7Pt6f1DXDEBaG9tvNiBU`</summary>

```text
# Paper Information

**Full Title:**
"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations"

**Authors:**
Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, and Mengdi Wang

**Submission Date:**
February 10, 2025 (v1); revised February 12, 2025 (v2)

**Abstract:**
The researchers constructed benchmarks with simple and hard perturbations of level-5 MATH problems to investigate whether LLM performance reflects genuine reasoning or memorization. Hard perturbations fundamentally alter problem nature, making original solutions inapplicable. Testing revealed significant performance declines across models, with o1-mini dropping 16.49% and gemini-2.0-flash-thinking dropping 12.9%. The team identified a concerning pattern where models blindly apply learned skills without evaluating applicability to modified contexts, particularly when using original problems for in-context learning.

**Venue Information:**
No specific conference or venue is mentioned. The paper is categorized under arXiv as a Computer Science submission (cs.LG, cs.AI, cs.CL classifications).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36f9f2cc-a9b2-4465-837a-483ba61f8d4c",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "c5807af0-7f95-4bea-85b6-b84823ff82bb",
  "sourceToolAssistantUUID": "36f9f2cc-a9b2-4465-837a-483ba61f8d4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T05:24:13.146Z_

<details><summary>↩ Tool result · `toolu_01FuuyFXU37MHpHQxymLWLsw`</summary>

```text
# Paper Information

**Full Title:**
"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems"

**Authors:**
- Yuren Hao
- Xiang Wan
- ChengXiang Zhai

**Submission Date:**
August 12, 2025 (v1); most recent revision December 4, 2025 (v3)

**Abstract:**
The researchers introduce a framework for evaluating large language models' robustness in mathematical reasoning by testing them on "advanced math problems that are mathematically equivalent but with linguistic and parametric variation." They created PutnamGAP, a benchmark with multiple versions of competition-level math problems. Testing 18 models, they found significant performance drops on variants—for instance, OpenAI's O3 model declined from 51.5% accuracy on originals to 46.8% on surface-renamed versions and 38.6% on parametric variants. The study demonstrates that this evaluation methodology effectively reveals how sensitive LLMs are to non-mathematical perturbations.

**Venue Information:**
No conference or venue is specified. This is a preprint posted on arXiv in the Computation and Language (cs.CL) category.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cc582f1-bcfa-4719-81a0-7a44e60182a6",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "6a6d610d-f20c-4544-a50c-11fe69b319e6",
  "sourceToolAssistantUUID": "5cc582f1-bcfa-4719-81a0-7a44e60182a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T05:24:14.320Z_

<details><summary>↩ Tool result · `toolu_016vFb5hnpewWmwmFZkAZPdc`</summary>

```text
# MathRobust-LV Paper Details

**Full Title:** "MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning"

**Authors:**
- Neeraja Kirtane
- Yuvraj Khanna
- Peter Relan

**Submission Date:** October 7, 2025

**Complete Abstract:**

The researchers developed an evaluation framework examining how well large language models handle mathematical problems when presented with surface-level changes. Their methodology kept numerical structures and answers identical while altering contextual elements like names and variables. Rather than emphasizing competition-level mathematics, the team focused on high school difficulty problems typical of educational tutoring and assessment systems. Testing 34 models revealed performance declines when moving from original problems to variants—with smaller models showing 9-11% drops, though frontier models remained more stable. The work demonstrates that robustness to linguistic variation represents a fundamental challenge for mathematical reasoning in AI systems.

**Venue Information:** No conference or venue is mentioned. The paper is categorized under Computer Science > Computation and Language on arXiv (arXiv:2510.06430).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "632b7a5b-b8ca-4d43-962b-adab1759eaa5",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "129f8a58-7d89-463f-8355-f02228b035c3",
  "sourceToolAssistantUUID": "632b7a5b-b8ca-4d43-962b-adab1759eaa5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-29T05:24:14.431Z_

<details><summary>↩ Tool result · `toolu_01EWrENtYnjywKDjezUcqP8L`</summary>

```text
# Paper Information

**Title:** "Benchmarking Reasoning Robustness in Large Language Models"

**Authors:** Tong Yu, Yongcheng Jing, Xikun Zhang, Wentao Jiang, Wenjie Wu, Yingjie Wang, Wenbin Hu, Bo Du, Dacheng Tao

**Submission Date:** March 6, 2025

**Venue/Conference:** Not mentioned (published on arXiv as cs.AI)

**Abstract Summary:**

The researchers identify significant challenges in how language models handle reasoning tasks. They found that advanced models like DeepSeek and GPT-4o experience performance drops when processing novel or incomplete information, indicating reliance on "memorized patterns rather than systematic reasoning."

The study documents four core vulnerabilities:

1. **Positional bias** – Models favor earlier queries in multi-item inputs
2. **Instruction sensitivity** – Performance declines with auxiliary guidance (5-7.5% drops observed)
3. **Numerical fragility** – Value substitution causes substantial accuracy loss (e.g., GPT-4o dropped from 97.5% to 82.5%)
4. **Memory dependence** – Models resort to guessing when critical data is absent

To investigate these issues comprehensively, the authors introduce Math-RoB, "a novel benchmark" designed to expose reasoning gaps by exploiting hallucinations triggered by missing information through instruction-based dataset generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50762e43-b865-4688-83cb-90c39a60d9e2",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "1afa4f07-3fe4-45f5-967f-bef6a564af46",
  "sourceToolAssistantUUID": "50762e43-b865-4688-83cb-90c39a60d9e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-29T05:24:14.975Z_

<details><summary>↩ Tool result · `toolu_0123pNxK4KDkftswiCXfEz2k`</summary>

```text
# Paper Information

**Full Title:** VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks

**Authors:** Jian Yao, Ran Cheng, Kay Chen Tan

**Submission Date:** July 17, 2025 (v1); last revised January 5, 2026 (v3)

**Venue/Conference:** None specified (published on arXiv as cs.AI preprint)

## Abstract Summary

The paper addresses concerns that improvements in LLM mathematical reasoning from reinforcement learning may reflect "memorization of benchmark-specific patterns" rather than genuine capabilities. The researchers identify two key evaluation problems: benchmark contamination from publicly available test problems and fragility from single-instance assessments.

To counter these issues, they introduce VAR-MATH, which converts numerical problems into parameterized templates requiring models to solve multiple variants. Testing on transformed versions of AMC23, AIME24, and AIME25 reveals substantial performance declines for RL-trained models—averaging 47.9%, 58.8%, and 72.9% respectively—suggesting "some existing RL methods rely on superficial heuristics and fail to generalize beyond specific numerical forms."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f764dc-e28c-4a6f-8ef7-3f4a8dbdf69c",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "f0c8cd39-1837-4a5d-a680-76280a42f716",
  "sourceToolAssistantUUID": "f7f764dc-e28c-4a6f-8ef7-3f4a8dbdf69c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-29T05:24:18.161Z_

Excellent. I have 8 papers already. Let me also search for a couple more relevant papers, particularly on training-time interventions and the GSM-Plus benchmark, and fetch the remaining ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0c8cd39-1837-4a5d-a680-76280a42f716",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJVnR6kP6qDrapdPAzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdb5ee73-2581-466e-978b-b9362fd0f5ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PetdiZKdHe1H5XmSuv77D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3317,
      "cache_read_input_tokens": 14755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3317,
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

_source line 36 · 2026-05-29T05:24:18.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015KBfhfj418vsShDY93nQgd`</summary>

```json
{
  "query": "GSM-Plus benchmark math reasoning LLM arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdb5ee73-2581-466e-978b-b9362fd0f5ae",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJVnR6kP6qDrapdPAzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c204b308-47ee-4a69-9ffe-55108e7aa2dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PetdiZKdHe1H5XmSuv77D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3317,
      "cache_read_input_tokens": 14755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3317,
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

_source line 37 · 2026-05-29T05:24:19.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TkezBPwAo37w5RsR6kdxzv`</summary>

```json
{
  "query": "reinforcement learning math reasoning robustness generalization LLM 2025 arXiv training intervention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c204b308-47ee-4a69-9ffe-55108e7aa2dd",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJVnR6kP6qDrapdPAzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27432826-9fa7-4c7f-ae8d-b2db8d1775c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PetdiZKdHe1H5XmSuv77D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3317,
      "cache_read_input_tokens": 14755,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3317
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 14755,
          "cache_creation_input_tokens": 3317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3317,
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

_source line 38 · 2026-05-29T05:24:26.153Z_

<details><summary>↩ Tool result · `toolu_01TkezBPwAo37w5RsR6kdxzv`</summary>

```text
Web search results for query: "reinforcement learning math reasoning robustness generalization LLM 2025 arXiv training intervention"

Links: [{"title":"LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2506.04821"},{"title":"Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning","url":"https://arxiv.org/html/2506.04723v1"},{"title":"[2504.20571] Reinforcement Learning for Reasoning in Large Language Models with One Training Example","url":"https://arxiv.org/abs/2504.20571"},{"title":"Inverse Reinforcement Learning Meets Large Language ...","url":"https://arxiv.org/pdf/2507.13158"},{"title":"Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning","url":"https://arxiv.org/html/2602.01528v2"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/pdf/2602.08489"}]

I've found several relevant research papers from arXiv on this topic. Here are the key findings:

## Recent Research on Reinforcement Learning for Math Reasoning in LLMs (2025)

**Robust Mathematical Reasoning via RL:**
Using a reinforcement learning setup with verifiable rewards where models receive binary feedback based on puzzle correctness, training approaches significantly improve out-of-distribution performance on mathematical benchmarks, especially for mid-difficulty problems requiring multi-step reasoning.

**Analysis of Reasoning Quality:**
RLVR (reinforcement learning with verifiable reward) optimizes reasoning solely through final-answer correctness, leaving a critical dimension of reasoning quality underexplored: the robustness of the reasoning process itself.

**Generalization Insights:**
Research has identified interesting phenomena during RL training including cross-category generalization, increased frequency of self-reflection, and sustained test performance improvement even after training accuracy has saturated, termed post-saturation generalization.

**Robustness Training Interventions:**
Models trained with epistemic independence training (EIT) on specific bias types generalize to unseen bias types such as authority and distraction, with improvements generalizing across benchmarks, model families, and scales.

**Reward Models for Generalization:**
Systems such as DeepSeek-R1 demonstrate that using rule-based or learned reward models enables LLMs to exhibit behaviors such as deep thinking, long chains of reasoning, and self-correction capabilities.

These papers explore how RL interventions during training can improve the robustness and generalization of mathematical reasoning in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27432826-9fa7-4c7f-ae8d-b2db8d1775c7",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "79f538b6-29a4-4a73-a1de-9fdd8e121381",
  "sourceToolAssistantUUID": "27432826-9fa7-4c7f-ae8d-b2db8d1775c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-29T05:24:26.158Z_

<details><summary>↩ Tool result · `toolu_015KBfhfj418vsShDY93nQgd`</summary>

```text
Web search results for query: "GSM-Plus benchmark math reasoning LLM arXiv 2024"

Links: [{"title":"[2402.19255] GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/abs/2402.19255"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.163/"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/html/2402.19255v1"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038v2"},{"title":"GSM-PLUS: A Comprehensive Benchmark for Evaluating ...","url":"https://aclanthology.org/2024.acl-long.163.pdf"}]

Based on the search results, here's what I found about GSM-Plus:

## Overview

GSM-Plus is an extension of GSM8K augmented with various mathematical perturbations. The paper was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL) in 2024, with the arXiv version uploaded in February 2024 (arXiv:2402.19255).

## Purpose and Findings

The benchmark was created to evaluate the robustness of LLMs' math reasoning capability by testing a wide range of question variations. Experiments on 25 LLMs and 4 prompting techniques showed that while LLMs exhibit different levels of math reasoning abilities, their performances are far from robust, and even for problems that have been solved in GSM8K, LLMs can make mistakes when new statements are added or the question targets are altered.

## Key Results

The benchmark revealed a gap of up to 20% between the accuracy reported by the current model and the accuracy observed in the GSM-Plus setting, while human performance remains unaffected due to the unchanged inherent difficulty level of the questions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c204b308-47ee-4a69-9ffe-55108e7aa2dd",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "ee904a87-0b45-4bc6-9fa3-ebc6adf323d8",
  "sourceToolAssistantUUID": "c204b308-47ee-4a69-9ffe-55108e7aa2dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-29T05:24:29.774Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Tn9hQttLQXG1uxZpGDHXpD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.19255",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee904a87-0b45-4bc6-9fa3-ebc6adf323d8",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJWdGTqKTjRN1dtv171",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf3ae706-8462-4aa6-aa54-9c95d918ce97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tv8T6HXzaretiEV3uZmz7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 18072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 805,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-29T05:24:30.734Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Czkhey5wCnzsvAtDUdo7Lu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.01528",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf3ae706-8462-4aa6-aa54-9c95d918ce97",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJWdGTqKTjRN1dtv171",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fcf7415-3572-43f6-9b91-e94720f4b986",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tv8T6HXzaretiEV3uZmz7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 18072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 805,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-29T05:24:31.692Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BZpXTBRv8mNTiTPnFZXRqv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.04821",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fcf7415-3572-43f6-9b91-e94720f4b986",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJWdGTqKTjRN1dtv171",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c306820c-3772-44bb-8a87-fb2bf8591820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tv8T6HXzaretiEV3uZmz7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 18072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 805,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-29T05:24:32.027Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018aJq5FCmeXLpaxpZ6zAj21`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.04723",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c306820c-3772-44bb-8a87-fb2bf8591820",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJWdGTqKTjRN1dtv171",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58cee3ae-25fe-4731-a4e0-6407b6f07a36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tv8T6HXzaretiEV3uZmz7B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 18072,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 734,
          "output_tokens": 389,
          "cache_read_input_tokens": 18072,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 805,
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

_source line 44 · 2026-05-29T05:24:34.554Z_

<details><summary>↩ Tool result · `toolu_01Tn9hQttLQXG1uxZpGDHXpD`</summary>

```text
# Paper Details

**Full Title:**
"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers"

**Authors:**
- Qintong Li
- Leyang Cui
- Xueliang Zhao
- Lingpeng Kong
- Wei Bi

**Submission Date:**
February 29, 2024 (v1); last revised July 2, 2024 (v2)

**Venue:**
ACL 2024

**Abstract:**
The paper examines whether large language models genuinely understand mathematics or rely on pattern recognition. The researchers created GSM-Plus, an expanded version of the GSM8K dataset with mathematical variations, and tested 25 LLMs using 4 prompting techniques. Key findings indicate that "while LLMs exhibit different levels of math reasoning abilities, their performances are far from robust." The study demonstrates that models frequently fail when problems receive minor alterations or when question objectives change, despite solving the original versions. The team also investigates whether combining existing prompting strategies yields improved robustness through an iterative approach that validates each reasoning step.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf3ae706-8462-4aa6-aa54-9c95d918ce97",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "0e7e1598-69d5-401c-8963-f952ed56b2b1",
  "sourceToolAssistantUUID": "bf3ae706-8462-4aa6-aa54-9c95d918ce97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-29T05:24:36.204Z_

<details><summary>↩ Tool result · `toolu_01Czkhey5wCnzsvAtDUdo7Lu`</summary>

```text
# Paper Information

**Title:** Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning

**Authors:** Qian Wang, Xuandong Zhao, Zirui Zhang, Zhanzhi Lou, Nuo Chen, Dawn Song, Bingsheng He

**Submission Date:** February 2, 2026 (v1); Last revised April 6, 2026 (v2)

**Venue:** Computer Science > Computers and Society (cs.CY); also categorized under Machine Learning (cs.LG)

**Abstract:**
The paper addresses how large language models remain vulnerable to cognitive biases when encountering misleading prompt cues like consensus or authority claims. The researchers propose "Epistemic Independence Training (EIT)," a reinforcement learning approach that "makes bias cues non-predictive of reward." Their method employs "a balanced conflict strategy where bias signals are equally likely to support correct" or incorrect answers. Testing on Qwen3-4B showed improvements in accuracy and robustness against adversarial biases. Notably, models trained on specific bias types "generalize to unseen bias types," suggesting the approach develops broader epistemic independence rather than bias-specific fixes. The work further demonstrates effectiveness "across benchmarks (MedQA, HellaSwag), model families (Llama-3.2-3B), and scales" while outperforming existing distribution-shift methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fcf7415-3572-43f6-9b91-e94720f4b986",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "e9d7ddb4-4e29-438d-a240-5d1f3d16583a",
  "sourceToolAssistantUUID": "2fcf7415-3572-43f6-9b91-e94720f4b986",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-29T05:24:36.531Z_

<details><summary>↩ Tool result · `toolu_018aJq5FCmeXLpaxpZ6zAj21`</summary>

```text
# Paper Details

**Full Title:** "Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning"

**Authors:** Jiayu Wang, Yifei Ming, Zixuan Ke, Caiming Xiong, Shafiq Joty, Aws Albarghouthi, Frederic Sala

**Submission Date:** June 5, 2025 (v1); Last revised October 24, 2025 (v2)

**Venue:** Accepted to NeurIPS 2025

**Abstract Summary:**

This work presents SPARKLE, a framework for understanding how reinforcement learning improves language model performance on mathematical reasoning. The researchers examined three dimensions: plan execution, knowledge integration, and problem-solving chains. Key findings include that "providing models with explicit human-crafted, step-by-step plans can surprisingly degrade performance on the most challenging benchmarks" while RL-trained models show greater robustness. The study also introduces SparkleRL-PSS, a pipeline that reuses difficult problems through partial step scaffolding, enabling effective training without generating additional data. The authors emphasize their work provides insights into building "more adaptive, data-efficient, and interpretable RL pipelines for reasoning tasks."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58cee3ae-25fe-4731-a4e0-6407b6f07a36",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "4b828620-90ec-4a70-b44e-b550c9fbea09",
  "sourceToolAssistantUUID": "58cee3ae-25fe-4731-a4e0-6407b6f07a36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-29T05:24:36.655Z_

<details><summary>↩ Tool result · `toolu_01BZpXTBRv8mNTiTPnFZXRqv`</summary>

```text
# Paper Information

**Full Title:**
"LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning"

**Authors:**
Zhen Hao Wong, Jingwen Deng, Runming He, Zirong Chen, Qijie You, Hejun Dong, Hao Liang, Chengyu Shen, Bin Cui, Wentao Zhang

**Submission Date:**
June 5, 2025

**Complete Abstract:**
The paper addresses how large language models often struggle with structured reasoning in unfamiliar contexts despite excelling at supervised tasks. The researchers propose a framework using reinforcement learning on seven custom logic puzzles designed to develop skills like constraint propagation and symbolic deduction. Models receive binary feedback based on puzzle correctness. The findings indicate this training approach "significantly improves out-of-distribution performance on a range of mathematical benchmarks, especially for mid-difficulty problems that require multi-step reasoning." The work shows that this method strengthens algebraic manipulation, geometric inference, and combinatorial logic while providing limited benefits for rote tasks.

**Venue/Conference Information:**
No conference or venue is mentioned. The paper is categorized as Computer Science > Machine Learning (cs.LG) on arXiv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c306820c-3772-44bb-8a87-fb2bf8591820",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "2b429ed3-31d3-4a0b-ad97-89c497e72d71",
  "sourceToolAssistantUUID": "c306820c-3772-44bb-8a87-fb2bf8591820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-29T05:24:41.241Z_

Now let me do one more targeted search for any training-time intervention papers specifically focused on improving math robustness, and also check for the RIDE paper that appeared earlier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b429ed3-31d3-4a0b-ad97-89c497e72d71",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJXP9BBeykQkaezjQby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2181d251-2ebd-4c69-bdc3-07515ba7cb95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKkj7xVkU68tNfBFbzYyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 18877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2073,
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

_source line 49 · 2026-05-29T05:24:42.187Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LSHy85QwRvorBreKwDcuoZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.04120",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2181d251-2ebd-4c69-bdc3-07515ba7cb95",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJXP9BBeykQkaezjQby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ad490e7-28b7-472c-83c5-bc1c223a340f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKkj7xVkU68tNfBFbzYyG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 18877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2073,
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

_source line 50 · 2026-05-29T05:24:42.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuSFBmgfoWpzhDARQNF1JL`</summary>

```json
{
  "query": "\"math reasoning\" \"RL training\" robustness generalization \"data augmentation\" perturbation LLM 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ad490e7-28b7-472c-83c5-bc1c223a340f",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJXP9BBeykQkaezjQby",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b462327-0fab-449d-a201-c5b52f00627b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKkj7xVkU68tNfBFbzYyG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 2073,
      "cache_read_input_tokens": 18877,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2073
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 314,
          "output_tokens": 216,
          "cache_read_input_tokens": 18877,
          "cache_creation_input_tokens": 2073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2073,
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

_source line 51 · 2026-05-29T05:24:46.620Z_

<details><summary>↩ Tool result · `toolu_01LSHy85QwRvorBreKwDcuoZ`</summary>

```text
# Paper Information

**Full Title:** "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning"

**Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan

**Submission Date:** November 6, 2025 (v1); last revised January 31, 2026 (v2)

**Abstract Summary:** The researchers propose RIDE, a framework using Item Response Theory to create adversarial question variations that assess genuine mathematical reasoning in large language models. By employing 35 LLMs as test subjects, they built a difficulty ranking system and used reinforcement learning to reformulate mathematical problems across difficulty levels. Testing on competition-level benchmarks showed an average 21.73% performance decrease across 26 models, revealing limited robustness in mathematical reasoning capabilities.

**Venue Information:** No specific conference venue is mentioned. The paper is categorized under Computer Science > Computation and Language (cs.CL) on arXiv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ad490e7-28b7-472c-83c5-bc1c223a340f",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "4fadaf51-3ad4-45fc-926e-8e99361b578d",
  "sourceToolAssistantUUID": "1ad490e7-28b7-472c-83c5-bc1c223a340f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-29T05:24:53.379Z_

<details><summary>↩ Tool result · `toolu_01RuSFBmgfoWpzhDARQNF1JL`</summary>

```text
Web search results for query: ""math reasoning" "RL training" robustness generalization "data augmentation" perturbation LLM 2025 2026 arXiv"

Links: [{"title":"Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning","url":"https://arxiv.org/html/2507.00432v1"},{"title":"Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning","url":"https://arxiv.org/html/2506.04723v1"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/pdf/2508.08833"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2511.08022"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038v2"},{"title":"LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2506.04821"}]

I found several highly relevant papers from arXiv (2025-2026) on math reasoning, RL training, robustness, generalization, and data augmentation with perturbation for LLMs:

## Key Papers Found:

1. **"Does Math Reasoning Improve General LLM Capabilities?"** (July 2025)
   - RL-trained models exhibit broader generalization across both reasoning and non-reasoning scenarios, and RL models consistently outperform SFT models, regardless of model size, architecture, or training data, demonstrating superior transferability.

2. **"Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning"** (June 2025)
   - Presents a multi-stage RL training approach with partial solution augmentation that improves the performance of a well-trained RL-tuned model.

3. **"An Investigation of Robustness of LLMs in Mathematical Reasoning"** (August 2025)
   - Introduces the Generalization–and–Perturbation (GAP) framework, instantiated on all 1,051 Putnam Competition questions to produce the 6,306-question PutnamGAP benchmark. A zero-shot evaluation of 18 commercial and open-source LLMs revealed sharp and consistent accuracy drops, exposing a clear robustness gap.

4. **"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking"** (June 2025)
   - The AbstRaL method promotes abstract reasoning in LLMs using RL on granular abstraction data and significantly mitigates performance degradation on recent GSM perturbation benchmarks.

5. **"Toward Automated Robustness Evaluation of Mathematical Reasoning"** (April 2026)
   - Four LLMs obtained 48.04% and 31.35% less averaged accuracy on GSM8K and MATH-500 evaluation variants, respectively.

6. **"LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning"** (June 2025)
   - Focuses on using RL to develop robust mathematical reasoning capabilities in LLMs through logic puzzle training.

These papers comprehensively address the intersection of RL training, robustness, generalization, and data augmentation/perturbation for improving LLM mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b462327-0fab-449d-a201-c5b52f00627b",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "9cada7ec-2a50-403e-bb8d-0b93b127b335",
  "sourceToolAssistantUUID": "2b462327-0fab-449d-a201-c5b52f00627b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-29T05:24:56.484Z_

Let me also fetch the AbstRaL paper, which is directly about a training-time intervention for math reasoning robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cada7ec-2a50-403e-bb8d-0b93b127b335",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJYcgJ9QiBugnephdLt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a29a7ca-a314-41c6-8e7f-1e27c9d9c3e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpzsUMHaAmEFGXVBn7HgvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 20950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 54 · 2026-05-29T05:24:56.798Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JZr8sd9D8bEy2uMCFfABAN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.07751",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue/conference information if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a29a7ca-a314-41c6-8e7f-1e27c9d9c3e5",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJYcgJ9QiBugnephdLt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8dd3530-2b5d-480f-86b7-f3cf2e4042ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpzsUMHaAmEFGXVBn7HgvM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 20950,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1826
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 20950,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1826,
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

_source line 55 · 2026-05-29T05:25:01.108Z_

<details><summary>↩ Tool result · `toolu_01JZr8sd9D8bEy2uMCFfABAN`</summary>

```text
# Paper Information

**Title:** "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking"

**Authors:** Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe

**Submission Date:** June 9, 2025 (v1); Latest revision February 23, 2026 (v4)

**Venue:** ICLR 2026

**Abstract:**

The research addresses robustness issues in smaller language models struggling with grade school math reasoning. Rather than generating synthetic data variations, the authors propose an abstraction-focused strategy. They introduce AbstRaL, a method employing reinforcement learning with granular abstraction data to enhance abstract reasoning. Key findings indicate this approach "significantly mitigates performance degradation on recent GSM perturbation benchmarks" and produces wider generalization benefits across mathematical and general reasoning tasks, suggesting that "abstract thinking broadly enables better generalizability."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8dd3530-2b5d-480f-86b7-f3cf2e4042ec",
  "isSidechain": true,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "agentId": "a74cf45dec59802ec",
  "type": "user",
  "uuid": "6c1874bf-e42f-41ee-b206-5ef02e533d31",
  "sourceToolAssistantUUID": "d8dd3530-2b5d-480f-86b7-f3cf2e4042ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-29T05:26:09.160Z_

I now have a comprehensive collection. Let me compile the final report with all the papers organized by category.

---

Here is the literature survey with 13 distinct papers covering RL-trained mathematical reasoning robustness (2024--2026).

---

## CATEGORY 1: Benchmarks Measuring LLM Math Reasoning Fragility

### 1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

- **Authors:** Iman Mirzadeh et al. (Apple)
- **Venue/Year:** ICLR 2025
- **URL:** https://arxiv.org/abs/2410.05229
- **What it does:** Introduces GSM-Symbolic, a benchmark using symbolic templates to generate diverse instantiations of grade-school math problems. Shows that all models' performance declines when only numerical values change, and adding a single irrelevant-but-plausible clause causes accuracy drops up to 65%, suggesting LLMs replicate memorized reasoning patterns rather than performing genuine logical reasoning.
- **Why it's important:** Published at ICLR 2025 (top venue). One of the most widely cited papers on math reasoning fragility. Originated from Apple ML Research. Established the template-based perturbation methodology that many subsequent papers build upon.

### 2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers

- **Authors:** Qintong Li et al.
- **Venue/Year:** ACL 2024
- **URL:** https://arxiv.org/abs/2402.19255
- **What it does:** Creates an augmented version of GSM8K with systematic mathematical perturbations (numerical variation, question target alteration, added statements). Tests 25 LLMs with 4 prompting techniques and finds up to 20% accuracy gaps between original and perturbed problems, while human performance is unaffected.
- **Why it's important:** Published at ACL 2024 (top NLP venue). One of the earliest systematic robustness benchmarks for math reasoning. Widely referenced as a baseline in subsequent work.

### 3. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations

- **Authors:** Kaixuan Huang et al. (Princeton, Google DeepMind)
- **Venue/Year:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06453
- **What it does:** Constructs perturbations of level-5 (hardest) MATH problems in two categories: "simple" perturbations that preserve solution structure and "hard" perturbations that fundamentally change problem nature. Finds o1-mini drops 16.49% and gemini-2.0-flash-thinking drops 12.9% on hard perturbations. Identifies a novel memorization pattern where models blindly apply learned solution strategies without checking applicability.
- **Why it's important:** First benchmark to distinguish simple vs. hard perturbations at competition-math difficulty. The "blind skill application" finding is a key insight for understanding RL-trained reasoners. Strong author team spanning Princeton and Google DeepMind.

### 4. VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks

- **Authors:** Jian Yao et al.
- **Venue/Year:** arXiv preprint, July 2025 (revised January 2026)
- **URL:** https://arxiv.org/abs/2507.12885
- **What it does:** Converts AMC23, AIME24, and AIME25 problems into parameterized templates and evaluates models on multiple numeric variants. RL-finetuned models show substantial performance declines averaging 47.9%, 58.8%, and 72.9% across those three suites, exposing that RL methods often rely on superficial heuristics rather than generalizable reasoning.
- **Why it's important:** Directly targets the question of whether RL training produces genuine reasoning or benchmark-specific pattern matching. The dramatic drops for RL-trained models (up to 72.9%) are among the largest reported in the literature.

### 5. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning

- **Authors:** Yuren Hao et al.
- **Venue/Year:** arXiv preprint, August 2025
- **URL:** https://arxiv.org/abs/2508.08833
- **What it does:** Introduces the Generalization-and-Perturbation (GAP) framework and the 6,306-item PutnamGAP benchmark derived from all 1,051 Putnam Competition problems. OpenAI's O3 drops from 51.5% to 46.8% on surface-renamed variants and to 38.6% on parametric variants, revealing clear robustness gaps even in frontier models at competition-level difficulty.
- **Why it's important:** Largest-scale perturbation benchmark for competition mathematics. Tests at a much higher difficulty level than GSM-based benchmarks. Demonstrates that even the strongest reasoning models (O3) are not robust to meaning-preserving rewording.

### 6. Robust Reasoning Benchmark (RRB)

- **Authors:** Pavel Golikov et al.
- **Venue/Year:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2604.08571
- **What it does:** Applies a pipeline of 13 deterministic textual perturbations to AIME 2024 and 2025 problems. Finds frontier models are largely resilient, but open-weights reasoning models show accuracy drops up to 54%. Identifies "Intra-Query Attention Dilution" where solving multiple math problems sequentially degrades performance on later problems.
- **Why it's important:** Most recent benchmark (2026). Introduces the attention dilution concept, arguing future architectures need explicit contextual resets within chain-of-thought. Provides the most comprehensive perturbation taxonomy (13 types).

---

## CATEGORY 2: Analysis of Math Reasoning Fragility Mechanisms

### 7. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models

- **Authors:** Zhishen Sun et al.
- **Venue/Year:** arXiv preprint, November 2025
- **URL:** https://arxiv.org/abs/2511.08022
- **What it does:** Proposes a perturbation framework with progressively intensifying "semantically irrelevant perturbation sentences." Models remain stable against non-numerical disruptions but collapse under numerical perturbations -- smaller models drop up to 51.55%, commercial models drop 3--10%. Finds models maintain 20--40% accuracy even without core instructions, confirming pattern-matching behavior.
- **Why it's important:** Key mechanistic finding: models are specifically fragile to irrelevant numerical information, not irrelevant textual information. The 20--40% accuracy-without-instructions result is a striking demonstration that models partially "know the answer pattern" before reading the problem.

### 8. Benchmarking Reasoning Robustness in Large Language Models (Math-RoB)

- **Authors:** Tong Yu et al.
- **Venue/Year:** arXiv preprint, March 2025
- **URL:** https://arxiv.org/abs/2503.04550
- **What it does:** Identifies four core vulnerabilities: positional bias, instruction sensitivity (5--7.5% drops), numerical fragility (GPT-4o drops from 97.5% to 82.5% on value substitution), and memory dependence (guessing when data is absent). Introduces Math-RoB, a benchmark exploiting hallucinations triggered by missing information.
- **Why it's important:** Provides the most systematic taxonomy of reasoning failure modes. The 15-point GPT-4o drop on simple value substitution is a striking result.

### 9. RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning

- **Authors:** Xinyuan Li et al.
- **Venue/Year:** arXiv preprint, November 2025 (revised January 2026)
- **URL:** https://arxiv.org/abs/2511.04120
- **What it does:** Uses Item Response Theory (IRT) with 35 LLMs as "test subjects" to build difficulty rankings, then uses RL to reformulate math problems at controlled difficulty levels. Testing on competition-level benchmarks shows an average 21.73% performance decrease across 26 models.
- **Why it's important:** Novel use of psychometric theory (IRT) to systematically calibrate perturbation difficulty. Bridges educational measurement theory with LLM evaluation.

### 10. MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning

- **Authors:** Neeraja Kirtane et al.
- **Venue/Year:** arXiv preprint, October 2025
- **URL:** https://arxiv.org/abs/2510.06430
- **What it does:** Evaluates 34 models on meaning-preserving linguistic rewording of high-school math problems (changing names, variables, context while keeping numerical structure identical). Smaller models show 9--11% drops; frontier models are more stable.
- **Why it's important:** Focuses specifically on linguistic (not numerical) perturbations, complementing numerical-perturbation studies. The large-scale evaluation (34 models) provides broad coverage.

---

## CATEGORY 3: Training-Time Interventions for Math Reasoning Robustness

### 11. AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking

- **Authors:** Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe
- **Venue/Year:** ICLR 2026
- **URL:** https://arxiv.org/abs/2506.07751
- **What it does:** Proposes reinforcement learning with granular abstraction data to promote abstract reasoning in smaller LLMs. Significantly mitigates performance degradation on GSM perturbation benchmarks and provides wider generalization benefits across mathematical and general reasoning tasks, demonstrating that "abstract thinking broadly enables better generalizability."
- **Why it's important:** Published at ICLR 2026 (top venue). One of the first papers showing a concrete training-time fix that improves robustness on perturbation benchmarks. Co-authored by Samy Bengio (also on GSM-Symbolic). Directly addresses the RL-for-robustness question.

### 12. LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning

- **Authors:** Zhen Hao Wong et al.
- **Venue/Year:** arXiv preprint, June 2025
- **URL:** https://arxiv.org/abs/2506.04821
- **What it does:** Trains models via RL on seven custom logic puzzles (constraint propagation, symbolic deduction) with binary correctness feedback. Significantly improves out-of-distribution performance on mathematical benchmarks, especially for mid-difficulty multi-step reasoning problems, while strengthening algebraic manipulation, geometric inference, and combinatorial logic.
- **Why it's important:** Demonstrates that RL training on non-math logic puzzles transfers to improved math robustness -- an important finding for training-time interventions.

### 13. Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (SPARKLE)

- **Authors:** Jiayu Wang et al.
- **Venue/Year:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2506.04723
- **What it does:** Introduces SPARKLE, a framework analyzing how RL improves LLM math reasoning along three dimensions: plan execution, knowledge integration, and problem-solving chains. Finds that explicit human-crafted step-by-step plans can surprisingly degrade performance on hard benchmarks, while RL-trained models show greater robustness. Introduces SparkleRL-PSS, a training pipeline reusing difficult problems via partial step scaffolding.
- **Why it's important:** Accepted at NeurIPS 2025 (top venue). Provides the deepest mechanistic understanding of why RL training improves reasoning robustness. The counterintuitive finding about explicit plans hurting performance has important implications for training methodology.

---

## Summary Table

| # | Paper | Venue | Category | Key Finding |
|---|-------|-------|----------|-------------|
| 1 | GSM-Symbolic | ICLR 2025 | Benchmark | Up to 65% drop from irrelevant clauses |
| 2 | GSM-Plus | ACL 2024 | Benchmark | Up to 20% gap on perturbations |
| 3 | MATH-Perturb | arXiv 2025 | Benchmark | 16.5% drop on hard perturbations (o1-mini) |
| 4 | VAR-MATH | arXiv 2025 | Benchmark | Up to 72.9% drop for RL-trained models |
| 5 | PutnamGAP | arXiv 2025 | Benchmark | O3 drops 12.9pp on parametric variants |
| 6 | RRB | arXiv 2026 | Benchmark | 13 perturbation types; 54% max drop |
| 7 | Numerical Sensitivity | arXiv 2025 | Analysis | Up to 51.55% drop from numerical distractors |
| 8 | Math-RoB | arXiv 2025 | Analysis | 4 vulnerability types; GPT-4o drops 15pp |
| 9 | RIDE | arXiv 2025 | Analysis | IRT-calibrated perturbations; 21.73% avg drop |
| 10 | MathRobust-LV | arXiv 2025 | Analysis | 9--11% drop from linguistic rewording |
| 11 | AbstRaL | ICLR 2026 | Training fix | RL + abstraction mitigates GSM fragility |
| 12 | LogicPuzzleRL | arXiv 2025 | Training fix | Logic puzzle RL transfers to math robustness |
| 13 | SPARKLE | NeurIPS 2025 | Training fix | Partial-step scaffolding RL improves robustness |

Three papers are from top venues (ICLR 2025, ACL 2024, NeurIPS 2025, ICLR 2026), providing strong publication-quality anchors for the survey. The remaining are recent arXiv preprints that collectively cover the full landscape from benchmarking fragility to training-time interventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c1874bf-e42f-41ee-b206-5ef02e533d31",
  "isSidechain": true,
  "agentId": "a74cf45dec59802ec",
  "requestId": "req_011CbWJZBn7pH2XQWP8aEfrG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f82c2c0c-e558-4202-afda-3f97c3acd5cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcFRW86MfLmHc3yx8HmzfJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 22776,
      "output_tokens": 3562,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3562,
          "cache_read_input_tokens": 22776,
          "cache_creation_input_tokens": 368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 368,
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
