# Research conversation: You are investigating a critical discrepancy for a paper on cross-lingual calibration transfer. The issue: Civelli, Bern

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adb09762506495b0b.jsonl`
- **Structured JSON:** [`539aab4705126770c888.json`](../../sessions/53/539aab4705126770c888.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-19T09:13:50.583Z_

You are investigating a critical discrepancy for a paper on cross-lingual calibration transfer.

The issue: Civelli, Bernardelle, Brunello & Demartini (arXiv 2601.12731) found that linear probes for problem difficulty generalize cross-lingually best at SHALLOW layers, while our hypothesis claims INTERMEDIATE layers are optimal for calibration transfer (based on Liu & Niehues ACL 2025 showing cross-lingual alignment peaks at middle layers).

Your tasks:
1. Use WebFetch to read https://arxiv.org/abs/2601.12731 — extract: which layers they found best for cross-lingual generalization of difficulty probes, what models they used, how they define "shallow" vs "intermediate" vs "deep", and any nuance about what transfers at which layer.
2. Use WebFetch to read about Liu & Niehues (ACL 2025) on middle-layer cross-lingual alignment. Search for it first with WebSearch: "Liu Niehues middle layer cross-lingual alignment ACL 2025"
3. Use WebSearch to find: "calibration direction layer depth LLM 2025 2026" — are there papers showing where calibration-specific directions live vs. where difficulty directions live?
4. Use WebSearch for "Joshi calibration across layers EMNLP 2025" to understand which layers have best calibration signals.

Report in detail (500+ words): What is the actual layer discrepancy? Is it possible that difficulty and calibration behave differently across layers? What does the evidence say about the optimal layer for cross-lingual calibration transfer specifically? Can we reconcile these findings or do we need to reframe our hypothesis?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "644b4b72-ba16-4029-aadc-727d884692ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:13:50.589Z_

```json
{
  "parentUuid": "644b4b72-ba16-4029-aadc-727d884692ae",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
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
  "uuid": "ff8a9423-1cac-4d1c-b3dc-d5222f60f822",
  "timestamp": "2026-05-19T09:13:50.589Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:13:50.590Z_

```json
{
  "parentUuid": "ff8a9423-1cac-4d1c-b3dc-d5222f60f822",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d934afb9-44a6-47d6-a8b2-8d8637b93c2d",
  "timestamp": "2026-05-19T09:13:50.590Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:13:53.625Z_



I'll investigate this discrepancy systematically by fetching and searching for all the relevant papers. Let me start with the parallel searches and fetches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d934afb9-44a6-47d6-a8b2-8d8637b93c2d",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfv624ErpiE7su8jk7J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c3afd82-ac55-4d36-8d90-41b60d43c488",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkKnRt1GksBrTYRTJ16kWF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1726,
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

_source line 5 · 2026-05-19T09:13:54.221Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019HeQ5LEbLkH5n1QHYjt4Dh`</summary>

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
  "parentUuid": "7c3afd82-ac55-4d36-8d90-41b60d43c488",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfv624ErpiE7su8jk7J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c76c3960-1efd-45ed-b15a-cafd560dc3ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkKnRt1GksBrTYRTJ16kWF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 7773,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1726,
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

_source line 6 · 2026-05-19T09:13:54.225Z_

<details><summary>↩ Tool result · `toolu_019HeQ5LEbLkH5n1QHYjt4Dh`</summary>

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
  "parentUuid": "c76c3960-1efd-45ed-b15a-cafd560dc3ea",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "c64f6dc9-0726-4ea5-b9ea-c2ce799b4572",
  "sourceToolAssistantUUID": "c76c3960-1efd-45ed-b15a-cafd560dc3ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:13:57.391Z_



Now let me run all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c64f6dc9-0726-4ea5-b9ea-c2ce799b4572",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfvNo7EsZoUS2pLKEX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1101be0e-9e96-42fd-a696-1d1ce893a062",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJYqRZVUMEQEj41tRcrn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9499,
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

_source line 8 · 2026-05-19T09:13:59.697Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SooNLy5yDUUpTbRGxZDUrC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.12731",
  "prompt": "Extract all details about: 1) Which layers they found best for cross-lingual generalization of difficulty probes. 2) What models they used. 3) How they define \"shallow\" vs \"intermediate\" vs \"deep\" layers. 4) Any nuance about what transfers at which layer depth. 5) Their main findings about layer-wise behavior of difficulty probes across languages. Include specific layer numbers and percentages if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1101be0e-9e96-42fd-a696-1d1ce893a062",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfvNo7EsZoUS2pLKEX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53abfb17-fb8d-4f3a-8284-6d83e98da53e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJYqRZVUMEQEj41tRcrn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9499,
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

_source line 9 · 2026-05-19T09:13:59.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nc396998bBEvNumAfrUM4n`</summary>

```json
{
  "query": "Liu Niehues middle layer cross-lingual alignment ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53abfb17-fb8d-4f3a-8284-6d83e98da53e",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfvNo7EsZoUS2pLKEX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9af2788-cd0e-4e8e-ab43-3d89edfc7220",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJYqRZVUMEQEj41tRcrn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9499,
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

_source line 10 · 2026-05-19T09:14:00.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0153TH4X38CGmrcFNd5AAGZM`</summary>

```json
{
  "query": "calibration direction layer depth LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9af2788-cd0e-4e8e-ab43-3d89edfc7220",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfvNo7EsZoUS2pLKEX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c79361e-2e2a-4747-b35a-ceac91354313",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJYqRZVUMEQEj41tRcrn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9499,
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

_source line 11 · 2026-05-19T09:14:00.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAH1tHg2nQGWTyDWiBUL7F`</summary>

```json
{
  "query": "Joshi calibration across layers EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c79361e-2e2a-4747-b35a-ceac91354313",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfvNo7EsZoUS2pLKEX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "747ce263-f0d9-41c9-9929-50ab2196821a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJYqRZVUMEQEj41tRcrn2z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9499,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 9499,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1134,
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

_source line 12 · 2026-05-19T09:14:04.526Z_

<details><summary>↩ Tool result · `toolu_01SooNLy5yDUUpTbRGxZDUrC`</summary>

```text
# Analysis of Layer-wise Difficulty Probes in Multilingual LLMs

Based on the abstract provided, here's what can be extracted:

## Cross-lingual Generalization
"Probes trained on shallow representations generalize substantially better across languages" despite lower single-language performance.

## Models Used
The document does not specify which particular language models were employed in the research.

## Layer Definitions
The paper identifies two representational stages:
- **Shallow**: Early layers of the model
- **Deep**: Later layers of the model

The abstract does not define intermediate layer categories or provide specific layer numbers.

## Layer-wise Behavioral Nuances
The research reveals a functional division: early-layer representations capture language-agnostic difficulty signals that transfer across tongues, while later-layer representations become language-specific but achieve higher accuracy within individual languages.

## Main Findings
The authors discovered that language models employ a two-stage process: they initially form "a language-agnostic representation of problem difficulty, which subsequently becomes language-specific." This progression extends beyond content semantics to metacognitive properties like difficulty estimation.

**Note**: The abstract lacks specific layer numbers, percentages, or model identifications. Fuller details would require accessing the complete paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53abfb17-fb8d-4f3a-8284-6d83e98da53e",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "288ee301-3d4f-4d77-a87a-8ac4d6faa302",
  "sourceToolAssistantUUID": "53abfb17-fb8d-4f3a-8284-6d83e98da53e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T09:14:06.027Z_

<details><summary>↩ Tool result · `toolu_0153TH4X38CGmrcFNd5AAGZM`</summary>

```text
Web search results for query: "calibration direction layer depth LLM 2025 2026"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub","url":"https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"}]

Based on the search results, I found relevant research on calibration in LLMs with a focus on layer depth:

## Key Findings

A 2025 study investigates how calibration evolves throughout the network's depth, uncovering a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.

The researchers identify a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

The findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.

The research was published in the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) by Joshi, Ahmad, and Modi, analyzing multiple open-weight models on the MMLU benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c79361e-2e2a-4747-b35a-ceac91354313",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "15f177cc-76bf-4497-a288-ecc25e10d47a",
  "sourceToolAssistantUUID": "7c79361e-2e2a-4747-b35a-ceac91354313",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T09:14:06.084Z_

<details><summary>↩ Tool result · `toolu_01Nc396998bBEvNumAfrUM4n`</summary>

```text
Web search results for query: "Liu Niehues middle layer cross-lingual alignment ACL 2025"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Knowledge Distillation Adapter for Cross-Lingual Transfer","url":"https://aclanthology.org/2025.inlg-main.8.pdf"},{"title":"Can you map it to English? The Role of Cross-Lingual ...","url":"https://aclanthology.org/2026.eacl-long.225.pdf"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://aclanthology.org/2025.acl-long.778.pdf"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in","url":"https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"}]

Based on the search results, here's what I found about the Liu and Niehues ACL 2025 paper on middle-layer cross-lingual alignment:

## Paper Overview

The paper titled "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" by Danni Liu and Jan Niehues was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.

## Key Findings

While large language models demonstrate remarkable capabilities at task-specific applications through fine-tuning, extending these benefits across diverse languages is essential for broad accessibility. However, effective cross-lingual transfer is hindered by LLM performance gaps across languages and the scarcity of fine-tuning data in many languages.

Through analysis of LLM internal representations from over 1,000+ language pairs, the authors discovered that middle layers exhibit the strongest potential for cross-lingual alignment. They proposed a middle-layer alignment objective integrated into task-specific training.

## Experimental Results

Their experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages. The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9af2788-cd0e-4e8e-ab43-3d89edfc7220",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "59051cb7-5855-4651-8d79-d279725c5859",
  "sourceToolAssistantUUID": "a9af2788-cd0e-4e8e-ab43-3d89edfc7220",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T09:14:06.613Z_

<details><summary>↩ Tool result · `toolu_01QAH1tHg2nQGWTyDWiBUL7F`</summary>

```text
Web search results for query: "Joshi calibration across layers EMNLP 2025"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"}]

Based on the search results, I found the paper you're looking for:

"Calibration Across Layers: Understanding Calibration Evolution in LLMs" by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi was accepted at EMNLP 2025.

The paper investigates an important aspect of Large Language Models: how calibration evolves throughout the network's depth, uncovering a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.

Key findings include:

- The researchers identify a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

- Their findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection.

The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing in Suzhou, China, with page numbers 14697–14725.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "747ce263-f0d9-41c9-9929-50ab2196821a",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "1bf61c96-bf3b-4dd7-bdea-10ad771c4973",
  "sourceToolAssistantUUID": "747ce263-f0d9-41c9-9929-50ab2196821a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T09:14:10.428Z_

Good, I have initial results. Let me now fetch the detailed content from the key papers to get specific layer numbers and nuances.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf61c96-bf3b-4dd7-bdea-10ad771c4973",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfwGrwzqKKw32zmNdXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b33605de-0591-4b69-bab2-1744882a50cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFurbg4HnGTAaEqy24a4QF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
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

_source line 17 · 2026-05-19T09:14:13.278Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WqBzWHfQAUdakC7UgqfPQw`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.14830",
  "prompt": "Extract all details about: 1) Which specific layers (by number or percentage of total depth) show the strongest cross-lingual alignment? 2) How do they define \"middle layers\"? 3) What models did they use and how many layers do those models have? 4) What happens at shallow layers vs middle layers vs deep layers for cross-lingual transfer? 5) Any quantitative results showing alignment scores by layer. 6) Do they discuss why middle layers are optimal?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b33605de-0591-4b69-bab2-1744882a50cf",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfwGrwzqKKw32zmNdXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad3a5602-5896-4b4a-9474-ff46c92db4d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFurbg4HnGTAaEqy24a4QF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
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

_source line 18 · 2026-05-19T09:14:16.543Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GDhJ4Ao4oNiFZzFkNzggcc`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.00280v1",
  "prompt": "Extract all details about: 1) How calibration evolves across layers - which layers show what calibration behavior? 2) Where exactly is the \"confidence correction phase\" - which layer range? 3) The low-dimensional calibration direction - at which layers does it live? 4) What models were studied and how many layers? 5) Any specific layer numbers or percentages where calibration peaks or changes. 6) The distinction between where decisions are made vs where calibration happens. 7) Any discussion of cross-lingual calibration or multilingual aspects."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3a5602-5896-4b4a-9474-ff46c92db4d2",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfwGrwzqKKw32zmNdXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b258b127-a6db-4851-a2da-d5406ba45817",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFurbg4HnGTAaEqy24a4QF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
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

_source line 19 · 2026-05-19T09:14:18.803Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0175HxSxmYSY3MpvQDHe2Z6u`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03136v1",
  "prompt": "Extract all details about: 1) Which intermediate layers are best for multilingual calibration? 2) How do they define intermediate vs final layers? 3) What specific layer numbers or percentages give the best calibration? 4) How does calibration differ across languages at different layers? 5) What models were studied? 6) The relationship between cross-lingual transfer and calibration at different depths. 7) Any comparison with difficulty estimation or confidence estimation at different layers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b258b127-a6db-4851-a2da-d5406ba45817",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfwGrwzqKKw32zmNdXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a42b8aa-9dd7-43e7-b87d-1d07d0bd092e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFurbg4HnGTAaEqy24a4QF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 10633,
      "output_tokens": 569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 569,
          "cache_read_input_tokens": 10633,
          "cache_creation_input_tokens": 2576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2576,
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

_source line 20 · 2026-05-19T09:14:19.404Z_

<details><summary>↩ Tool result · `toolu_01WqBzWHfQAUdakC7UgqfPQw`</summary>

```text
# Cross-Lingual Alignment in LLM Layers

## 1) Strongest Alignment Layers

The research identifies middle layers as demonstrating superior cross-lingual semantic alignment. In their 35-language analysis covering 1,190 language pairs, "the middle layers of both models demonstrate the strongest retrieval performance."

## 2) Definition of "Middle Layers"

For their primary experiments, the authors define middle layers specifically as **layer 16 out of 32 total layers** in Llama 3 (50% depth). They compare this explicitly against bottom (layer 8) and top (layer 32) configurations.

## 3) Models and Layer Counts

The researchers tested two models:
- **Llama 3 8B-Instruct**: 32 layers total
- **Qwen 2.5 7B-Instruct**: Similar architecture with comparable depth

## 4) Layer-Specific Cross-Lingual Transfer Patterns

- **Shallow layers**: Poor alignment and transfer performance; bottom-layer placement caused "particularly strong degradation on the slot filling task"
- **Middle layers**: Optimal transfer improvements; enhanced alignment across multiple preceding layers
- **Deep layers**: Limited improvement propagation; primarily affected only the final layer

## 5) Quantitative Alignment Scores

Translation retrieval accuracy showed these patterns:
- Overall baseline: below 50% across language pairs
- Middle-layer placement improvements substantially enhanced retrieval accuracy from 39.4% to 73.2% on slot filling tasks

## 6) Why Middle Layers Are Optimal

The authors explain that "lower layers are occupied with processing more fundamental text features rather than abstract semantic meanings," suggesting middle layers strike an optimal balance for capturing semantic equivalence across languages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad3a5602-5896-4b4a-9474-ff46c92db4d2",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "74496716-b67c-443c-b1db-b48320f3d620",
  "sourceToolAssistantUUID": "ad3a5602-5896-4b4a-9474-ff46c92db4d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T09:14:25.219Z_

<details><summary>↩ Tool result · `toolu_01GDhJ4Ao4oNiFZzFkNzggcc`</summary>

```text
# Calibration Evolution in LLMs: Key Findings

## 1) Calibration Evolution Across Layers

The research reveals a **three-phase pattern**:

- **Early layers (0-21)**: Accuracy remains near-random (~25% on 4-option MCQA)
- **Mid layers (22-26)**: Accuracy rises sharply and saturates
- **Later layers (26-31)**: Accuracy plateaus while calibration metrics fluctuate significantly

As stated: "accuracy begins to rise significantly from layer 22 and stabilizes by layer 26. However, the calibration behavior follows a different trajectory."

## 2) The Confidence Correction Phase Location

The correction phase occurs in **layers 25-31**, specifically:

- **Layers 25-28**: ECE and MCE scores *increase* (overconfidence emerges)
- **Layers 28-31**: ECE and MCE scores *decline* sharply (calibration improves)

The paper notes that "models become temporarily overconfident before self-adjusting in later layers."

## 3) Low-Dimensional Calibration Direction

The calibration direction emerges from **layers 28-30** and is defined as:

"the mean of the normalized differences between successive layer outputs in the final three layers" (layers 29, 30, 31)

This direction exists in the residual stream and can be perturbed to improve calibration without affecting accuracy.

## 4) Models Studied and Layer Counts

Four models were analyzed:

| Model | Layers |
|-------|--------|
| Phi-2 | 32 |
| LLaMA-3 | 8B (implied full analysis) |
| LLaMA-2 | 7B |
| Mistral-7B | 32 |

## 5) Specific Layer Numbers for Calibration Changes

**Phi-2 specific findings**:
- Layer 22: Accuracy rise begins
- Layer 25-26: Accuracy saturation; calibration peak begins
- Layer 28: Peak ECE/MCE (maximum overconfidence)
- Layer 31: Final calibration improvement

## 6) Decision vs. Calibration Separation

The research demonstrates a critical distinction: "the model's accuracy remains near-random (25%, 4-options) for initial layers and starts to rise from layer 22...However, the ECE and MCE scores first rise (layers 25-28) and then decline (layers 28-31)."

This reveals that **prediction decisions crystallize by layer 26**, but **confidence regulation continues through layer 31**, operating as an independent mechanism.

## 7) Cross-Linguistic or Multilingual Aspects

**None found.** The paper restricts analysis entirely to English-language tasks (MMLU, CoLA, COPA, Rotten Tomatoes, TruthfulQA). No multilingual or cross-linguistic calibration analysis is discussed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b258b127-a6db-4851-a2da-d5406ba45817",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "26739bcb-51a4-43d4-bfcc-93aac154131e",
  "sourceToolAssistantUUID": "b258b127-a6db-4851-a2da-d5406ba45817",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T09:14:32.216Z_

<details><summary>↩ Tool result · `toolu_0175HxSxmYSY3MpvQDHe2Z6u`</summary>

```text
# Multilingual Calibration in LLMs: Key Findings

## 1) Best Intermediate Layers for Multilingual Calibration

Late-intermediate layers consistently outperform final layers for non-English languages. The research identifies "a sweet spot with lower ECE in the late-intermediate layers (between layers 24-end for LLaMA3 and 26-end for Aya, both are 32-layer models)." For LLaMA3, layer 29 achieved the best results, with an average improvement of 8.57 ECE points.

## 2) Definition of Intermediate vs Final Layers

The authors employ a layer-wise probing methodology where they "attach [the modeling head] to each intermediate transformer layer" to extract logits and confidence scores from every depth position. The final layer serves as the baseline reference—it's where standard confidence extraction occurs in conventional practice.

## 3) Specific Layer Numbers and Optimal Performance

- **LLaMA3**: Layer 29 provides optimal multilingual calibration (32 layers total)
- **Aya**: Layer 28 achieves comparable improvements (32 layers total)
- Both models show calibration peaks "between layers 24-end," representing the late-intermediate region

## 4) Cross-Language Calibration Differences Across Depths

A critical dichotomy emerges:
- **English**: Calibration "improves monotonically with layer depth," peaking at the final layer
- **Non-English languages**: Achieve "best calibration in late intermediate layers," with quality degrading toward the final output layer

The authors note that "nearly all non-English languages benefit greatly from moving away from the final layer," with examples like German and Hindi showing reductions exceeding 13-16% in ECE.

## 5) Models Studied

Six major model families were evaluated:
- LLaMA3 (8B-Instruct)
- Qwen2.5 (7B-Instruct)
- Mistral (7B-Instruct)
- Aya (8B)
- DeepSeek (R1-Distill-7B)
- Phi (4)

All experiments used "eight-shot prompting setup in its respective language" across MMMLU (15 languages) and Belebele (122 languages) benchmarks.

## 6) Cross-Lingual Transfer and Calibration Depth

The research reveals that "the final layer, heavily biased by English-dominated training, provides a sub-optimal signal for multilingual confidence." Intermediate layers encode "more language-agnostic representations," enabling better cross-lingual transfer. The authors hypothesize that multilingual inputs are "mapped into shared internal representations that often resemble English-like structures" in middle layers before being decoded in final layers.

## 7) Difficulty/Confidence Estimation Comparison

The study identifies "a latent, more reliable calibration signal hidden deeper within the model's architecture." Notably, "the sweet spot in calibration coincides with the sharp drop in entropy," suggesting that confidence estimation becomes more reliable when entropy reduction stabilizes in intermediate regions. This contrasts with final-layer confidence, which exhibits English-centric bias patterns.

---

**Key Methodological Innovation**: The Language-Aware Confidence Ensemble (LACE) achieves minimal ECE (3.09% for LLaMA3, 3.45% for Aya) by "adaptively selecting an optimal ensemble of layers for each specific language."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a42b8aa-9dd7-43e7-b87d-1d07d0bd092e",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "da92c088-7a92-412e-98ee-8832c543fa3c",
  "sourceToolAssistantUUID": "7a42b8aa-9dd7-43e7-b87d-1d07d0bd092e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T09:14:35.285Z_

Now let me get the full paper details from Civelli et al. to understand their specific layer definitions and model details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da92c088-7a92-412e-98ee-8832c543fa3c",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfy9z1XWt2i9v1mjUAE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2a4d471-abec-49e8-9029-a6bc02103e64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt27hxWpQtWwPF2uULzDdt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 13209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2515,
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

_source line 24 · 2026-05-19T09:14:38.168Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MMUUUPYUTUfXDXaL43RxY2`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2601.12731",
  "prompt": "Extract all details about: 1) Specific layer numbers where cross-lingual difficulty probes work best. 2) Which models were used and how many layers they have. 3) How they define shallow vs deep - any specific layer numbers or percentages. 4) The two-stage process they describe. 5) Any quantitative results comparing probe accuracy at different layers for same-language vs cross-language transfer. 6) Do they test intermediate layers separately from shallow and deep?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a4d471-abec-49e8-9029-a6bc02103e64",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfy9z1XWt2i9v1mjUAE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "444d262c-4de2-49e7-b537-a2ddaa1cd742",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt27hxWpQtWwPF2uULzDdt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 13209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2515,
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

_source line 25 · 2026-05-19T09:14:39.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbuUeApYBme14w8LPT4d7K`</summary>

```json
{
  "query": "Civelli Bernardelle Brunello Demartini \"problem difficulty\" probes layers cross-lingual LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "444d262c-4de2-49e7-b537-a2ddaa1cd742",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfy9z1XWt2i9v1mjUAE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ea2e13a-209c-473b-b018-970467a7c83e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt27hxWpQtWwPF2uULzDdt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 13209,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 13209,
          "cache_creation_input_tokens": 2515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2515,
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

_source line 26 · 2026-05-19T09:14:44.399Z_

<details><summary>↩ Tool result · `toolu_01MMUUUPYUTUfXDXaL43RxY2`</summary>

```text
# Analysis of Cross-Lingual Difficulty Probe Findings

Based on the document, here are the key details requested:

## 1) Optimal Layer Numbers for Cross-Lingual Probes
The document indicates probes work across multiple layers, but specific optimal layer numbers are not clearly stated in the visible content. The research examines layer-wise performance for difficulty detection.

## 2) Models and Layer Counts
The paper tests several multilingual models:
- **Llama 3.1** (specific layer count not detailed in excerpt)
- **Llama 3.2** (1B and 3B variants mentioned)
- **Qwen3** (referenced in citations)
- **GPT models** (OpenAI systems referenced)

## 3) Shallow vs. Deep Definition
The document uses "shallow" and "deep" terminology but does not provide explicit layer number thresholds or percentage cutoffs in the visible sections.

## 4) Two-Stage Process
While the paper is titled "A Shared Geometry of Difficulty in Multilingual Language Models," the specific two-stage methodology is not detailed in the accessible portions of the PDF content provided.

## 5) Quantitative Cross-Language Transfer Results
Specific accuracy comparisons between same-language and cross-language probe transfer at different layers are not clearly presented in the viewable sections.

## 6) Intermediate Layer Testing
Evidence of intermediate layer analysis appears present, but detailed findings are not extracted from the available content.

**Note:** The full research details likely appear in body sections not fully accessible in this PDF excerpt.

[Binary content (application/pdf, 7.3MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/e35f8964-edb8-41bf-9248-b2986ccc4fa6/tool-results/webfetch-1779182078964-z3sint.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "444d262c-4de2-49e7-b537-a2ddaa1cd742",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "1160435e-0bc0-40de-a65c-7e1e913d5d80",
  "sourceToolAssistantUUID": "444d262c-4de2-49e7-b537-a2ddaa1cd742",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T09:14:45.576Z_

<details><summary>↩ Tool result · `toolu_01WbuUeApYBme14w8LPT4d7K`</summary>

```text
Web search results for query: "Civelli Bernardelle Brunello Demartini "problem difficulty" probes layers cross-lingual LLM 2025"

Links: [{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/abs/2601.12731"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/pdf/2601.12731"},{"title":"LLMs Encode How Difficult Problems Are","url":"https://arxiv.org/pdf/2510.18147"},{"title":"(PDF) Political Ideology Shifts in Large Language Models","url":"https://www.researchgate.net/publication/394920825_Political_Ideology_Shifts_in_Large_Language_Models"},{"title":"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models","url":"https://arxiv.org/pdf/2505.18673"}]

I found the research you're looking for! The paper "A Shared Geometry of Difficulty in Multilingual Language Models" by Stefano Civelli, Pietro Bernardelle, Nicolò Brunello, and Gianluca Demartini studies the multilingual geometry of problem-difficulty in LLMs by training linear probes using the AMC subset of the Easy2Hard benchmark, translated into 21 languages.

The key findings are: difficulty-related signals emerge at two distinct stages of the model internals, corresponding to shallow (early-layers) and deep (later-layers) internal representations, that exhibit functionally different behaviors. 

Probes trained on deep representations achieve high accuracy when evaluated on the same language but exhibit poor cross-lingual generalization, while probes trained on shallow representations generalize substantially better across languages, despite achieving lower within-language performance.

The results suggest that LLMs first form a language-agnostic representation of problem difficulty, which subsequently becomes language-specific, and this two-stage representational process extends beyond semantic content to high-level metacognitive properties such as problem-difficulty estimation.

The paper was published on arXiv on January 19, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ea2e13a-209c-473b-b018-970467a7c83e",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "016948a0-51f0-40b8-821b-f7a2c89a0f45",
  "sourceToolAssistantUUID": "4ea2e13a-209c-473b-b018-970467a7c83e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T09:14:50.637Z_

Let me fetch the HTML version of the Civelli et al. paper for more specific layer details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "016948a0-51f0-40b8-821b-f7a2c89a0f45",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfz9osVNo4DD6zX2XyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "286c4281-a9ed-4441-a142-eda2dd858eae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpyanxkfmYa1FAfidVyFvG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 15724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1345,
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

_source line 29 · 2026-05-19T09:14:54.404Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TfjuXvDU36zoNmcfxaztYo`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.12731",
  "prompt": "Extract ALL specific details about layers: 1) Exact layer numbers or layer ranges they tested. 2) Which specific layers are \"shallow\" - give exact numbers or percentages. 3) Which layers are \"deep\" - give exact numbers. 4) Any figures or tables showing probe accuracy by layer, especially cross-lingual transfer accuracy by layer. 5) What models they used and how many layers each model has. 6) Do they test every single layer or just groups? 7) Any mention of \"intermediate\" layers? 8) The AMC/Easy2Hard benchmark details. 9) Any specific numerical accuracy results at different layer depths for cross-lingual vs same-language probes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "286c4281-a9ed-4441-a142-eda2dd858eae",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfz9osVNo4DD6zX2XyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f160945-8b0f-4a74-b22c-c814114f68c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpyanxkfmYa1FAfidVyFvG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 15724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1345,
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

_source line 30 · 2026-05-19T09:14:54.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PXEsctAMou4uf6DKS41vWg`</summary>

```json
{
  "query": "\"beyond the final layer\" intermediate representations multilingual calibration 2025 arxiv layer numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f160945-8b0f-4a74-b22c-c814114f68c3",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBfz9osVNo4DD6zX2XyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da3afcfe-24ce-43d4-a9c4-65bc93afd492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpyanxkfmYa1FAfidVyFvG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 15724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1345,
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

_source line 31 · 2026-05-19T09:15:00.901Z_

<details><summary>↩ Tool result · `toolu_01TfjuXvDU36zoNmcfxaztYo`</summary>

```text
# Layer Details from "A Shared Geometry of Difficulty in Multilingual Language Models"

## Models and Layer Counts
The research evaluated four instruction-tuned models with these layer architectures:
- LLaMA-3.1-8B: 32 layers
- LLaMA-3.2-3B: 28 layers
- LLaMA-3.2-1B: 16 layers
- Qwen3-8B: 36 layers

## Testing Methodology
Researchers "extract residual stream activations from every transformer layer" and "train linear Ridge regression probes to predict continuous difficulty scores" independently at each layer, meaning they tested all layers, not groups.

## Shallow vs. Deep Layer Findings

**Shallow (Early) Layers:**
- Cross-lingual transfer peaks around layer 14-15 for LLaMA-3.1-8B
- These layers maintain "language-agnostic representation of problem difficulty"
- Achieve lower within-language accuracy but "substantially better across languages"

**Deep (Later) Layers:**
- Same-language probes peak around layer 30 for LLaMA-3.1-8B
- Show "poor cross-lingual generalization" despite "high accuracy when evaluated on the same language"

## Intermediate Layers
Figure 1 indicates "performance peaks in the middle layers," suggesting a three-stage structure rather than binary shallow/deep division.

## Accuracy by Layer (LLaMA-3.1-8B)

| Metric | Same-Language | Cross-Lingual |
|--------|---|---|
| Spearman ρ | 0.822±0.019 | 0.783±0.024 |
| Optimal Layer | 30.05 | 15.67 |
| Transfer Drop | 0.177 ρ loss | — |

## Benchmark Details
The AMC subset contains "approximately 4,000 math problems annotated with continuous difficulty scores" from Item Response Theory, "translated into 20 additional languages" (21 total), with "approximately 3,000 problems for training and 1,000 for testing."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f160945-8b0f-4a74-b22c-c814114f68c3",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "24533ffc-8e6f-4f01-9e04-21e34cdc0d5d",
  "sourceToolAssistantUUID": "3f160945-8b0f-4a74-b22c-c814114f68c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T09:15:02.326Z_

<details><summary>↩ Tool result · `toolu_01PXEsctAMou4uf6DKS41vWg`</summary>

```text
Web search results for query: ""beyond the final layer" intermediate representations multilingual calibration 2025 arxiv layer numbers"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Accepted Submissions | MELT Workshop @ COLM 2025","url":"https://melt-workshop.github.io/papers/"},{"title":"Post-Training Quantization Methods","url":"https://www.emergentmind.com/topics/post-training-quantization-methods"}]

I found the paper! Here are the key findings from the search results:

The researchers conducted the first layer-wise investigation of multilingual calibration, discovering that intermediate layers offer a more reliable calibration signal than the final, English-biased layer.

Their layer-wise analysis uncovered that late-intermediate layers consistently offer a more reliable and better-calibrated signal.

The study introduced training-free calibration methods, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers for each specific language, demonstrating their effectiveness in closing the cross-lingual calibration gap.

The work conducted large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration.

The paper is titled "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" and was published on arXiv on October 3, 2025 (arXiv ID: 2510.03136).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da3afcfe-24ce-43d4-a9c4-65bc93afd492",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "d1a2edc3-95b3-4a2c-81ba-3dab011eafa1",
  "sourceToolAssistantUUID": "da3afcfe-24ce-43d4-a9c4-65bc93afd492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-19T09:15:06.885Z_

Now I have comprehensive data from all the key papers. Let me also search for one more piece -- any work that directly connects difficulty probing with calibration to see if the distinction has been explicitly discussed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a2edc3-95b3-4a2c-81ba-3dab011eafa1",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBg1NiXitXs8R5z2SoL9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5713ce92-d140-4814-8ff0-97e76ab9c13d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqtQLhsgvhPojDGPqFBtr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 17069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1435,
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

_source line 34 · 2026-05-19T09:15:07.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BrqaQy2KnKc39tdkT6abmY`</summary>

```json
{
  "query": "difficulty estimation vs calibration confidence layer depth LLM representations difference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5713ce92-d140-4814-8ff0-97e76ab9c13d",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBg1NiXitXs8R5z2SoL9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5020800-2eb8-4220-93cc-bedeafeeef58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqtQLhsgvhPojDGPqFBtr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 17069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1435,
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

_source line 35 · 2026-05-19T09:15:07.829Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HFXQCusN2qDtELL7WuoSaE`</summary>

```json
{
  "query": "\"problem difficulty\" \"calibration\" different layers LLM probing cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5020800-2eb8-4220-93cc-bedeafeeef58",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBg1NiXitXs8R5z2SoL9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1021bd02-5724-4e97-a410-80f43308cc0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxqtQLhsgvhPojDGPqFBtr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1435,
      "cache_read_input_tokens": 17069,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 17069,
          "cache_creation_input_tokens": 1435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1435,
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

_source line 36 · 2026-05-19T09:15:15.171Z_

<details><summary>↩ Tool result · `toolu_01BrqaQy2KnKc39tdkT6abmY`</summary>

```text
Web search results for query: "difficulty estimation vs calibration confidence layer depth LLM representations difference 2025 2026"

Links: [{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Graph-based Confidence Calibration for Large Language Models","url":"https://arxiv.org/pdf/2411.02454"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Benchmarking LLM Uncertainty and Calibration with ...","url":"https://aclanthology.org/2026.eacl-long.106.pdf"},{"title":"Confidence Calibration and Rationalization for LLMs via Multi-Agent   Deliberation","url":"https://arxiv.org/pdf/2404.09127"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"}]

Based on the search results, here's what I found regarding the differences between difficulty estimation and calibration confidence in LLM representations:

## Key Differences in Focus

LLM calibration efforts diverge into two streams: the first targets calibration of next-token predictions and responses to reduce hallucinations, while the second focuses on developing and calibrating explicit confidence estimation mechanisms that assess the correctness of statements generated by LLMs.

## Layer-Depth Analysis

Recent research tests a model's ability to handle different question structures while monitoring its confidence across various layers of the transformer. Prior studies have primarily documented calibration issues at the final output layer, but none have examined confidence behavior in depth or investigated its architectural origins.

One notable finding is that researchers can train auxiliary linear classifiers on hidden layer activations from an LLM to predict the truthfulness of statements, though efficacy depends on identifying the optimal representational layer and may vary across evaluation metrics.

## Confidence Estimation Methods

Existing approaches to LLM confidence estimation include direct self-evaluation, post-hoc adjustments, internal state probing with lightweight classifiers, and model fine-tuning. Self-consistency, semantic entropy, and related approaches achieve strong calibration by aggregating uncertainty across multiple generations.

The recent research (2025-2026) indicates growing interest in understanding how confidence and uncertainty behave across different layers of LLMs, rather than just at the final output layer, with implications for more accurate difficulty estimation and calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5020800-2eb8-4220-93cc-bedeafeeef58",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "a7a0de2c-d332-4580-b97c-1549d7836174",
  "sourceToolAssistantUUID": "a5020800-2eb8-4220-93cc-bedeafeeef58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T09:15:15.204Z_

<details><summary>↩ Tool result · `toolu_01HFXQCusN2qDtELL7WuoSaE`</summary>

```text
Web search results for query: ""problem difficulty" "calibration" different layers LLM probing cross-lingual 2025 2026"

Links: [{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation","url":"https://arxiv.org/html/2605.12515"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/pdf/2601.12731"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"LLMs Encode How Difficult Problems Are","url":"https://arxiv.org/pdf/2510.18147"},{"title":"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models","url":"https://arxiv.org/html/2505.18673v1"},{"title":"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.404/"}]

I found several highly relevant research papers from 2025-2026 that match your query. Here are the key findings:

## Primary Research

The most directly relevant paper is "A Shared Geometry of Difficulty in Multilingual Language Models" which found that problem difficulty is encoded in a depth-dependent manner that trades off cross-lingual generalization and language-specific accuracy. Linear probes show that difficulty is decodable both from shallow and deep layers, with shallow layers supporting strong cross-lingual transfer, while deeper layers yield higher accuracy within the training language but generalize poorly across languages.

Another key work, "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models," conducts a layer-wise investigation of multilingual calibration, discovering that intermediate layers offer a more reliable calibration signal than the final, English-biased layer. This research introduces novel, training-free calibration methods that leverage intermediate representations, demonstrating their effectiveness in closing the cross-lingual calibration gap.

## Related Work

Additionally, research on problem difficulty encoding has been conducted across five major model families—Qwen2.5, Qwen3, LLaMA 3.1, DeepSeek to examine whether difficulty is linearly encoded across different model architectures.

These studies collectively investigate how LLMs encode problem difficulty across different layers and languages, with findings that intermediate and shallow layers better preserve cross-lingual representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1021bd02-5724-4e97-a410-80f43308cc0a",
  "isSidechain": true,
  "promptId": "4fc041ec-397d-49b9-a12a-682409a88b87",
  "agentId": "adb09762506495b0b",
  "type": "user",
  "uuid": "73027887-4214-4eb9-9f95-036c4fa0c801",
  "sourceToolAssistantUUID": "1021bd02-5724-4e97-a410-80f43308cc0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-19T09:15:58.735Z_

I now have comprehensive evidence from all the key papers. Here is my detailed analysis.

---

## Detailed Report: The Layer Discrepancy Between Difficulty Probes and Calibration Transfer

### The Core Discrepancy

The apparent discrepancy involves three distinct layer-depth claims:

**Civelli et al. (arXiv 2601.12731)** found that linear probes for *problem difficulty* generalize cross-lingually best at **shallow layers** -- specifically around layers 14-15 out of 32 in LLaMA-3.1-8B (approximately 44-47% of model depth). Same-language difficulty probes peak much later, around layer 30. The optimal cross-lingual transfer layer averages 15.67 across their experiments, versus 30.05 for same-language accuracy. They tested LLaMA-3.1-8B (32 layers), LLaMA-3.2-3B (28 layers), LLaMA-3.2-1B (16 layers), and Qwen3-8B (36 layers), extracting residual stream activations from every single transformer layer and training Ridge regression probes independently at each.

**Liu & Niehues (ACL 2025, aclanthology.org/2025.acl-long.778)** showed that cross-lingual *semantic* alignment peaks at **middle layers** -- specifically layer 16 out of 32 in LLaMA 3 8B-Instruct (exactly 50% depth). They demonstrated this across 1,190 language pairs from 35 languages. Bottom-layer alignment (layer 8, ~25%) caused severe degradation, while top-layer alignment (layer 32) had limited propagation. Their middle-layer alignment objective improved cross-lingual slot filling from 39.4% to 73.2%.

**The calibration literature** tells a different story. Joshi, Ahmad & Modi (EMNLP 2025, arxiv 2511.00280) found that calibration is a **late-layer phenomenon**: in a 32-layer model, accuracy crystallizes by layer 26, but a distinct "confidence correction phase" operates in layers 28-31. The low-dimensional calibration direction they identify lives in layers 28-30 -- the final ~90-94% of model depth. Meanwhile, the "Beyond the Final Layer" paper (arxiv 2510.03136) found that *multilingual* calibration peaks at **late-intermediate layers**: layer 29 for LLaMA3 and layer 28 for Aya (both 32-layer models, i.e., ~88-91% depth). Crucially, English calibration improves monotonically to the final layer, but non-English languages achieve best calibration at these late-intermediate positions, with the final layer being suboptimal due to English-centric training bias.

### Reconciling the Evidence: Three Distinct Phenomena at Three Distinct Depths

The discrepancy dissolves once we recognize that **difficulty estimation, semantic alignment, and calibration are fundamentally different computational processes** that the model implements at different depths:

1. **Language-agnostic difficulty encoding (shallow, ~44-50% depth)**: Civelli et al. demonstrate that LLMs first form a language-agnostic representation of problem difficulty in early-to-middle layers. This is a *metacognitive* property -- the model encodes "how hard is this problem" before it has fully committed to language-specific processing. At layers 14-16 out of 32, the model has built enough abstract representation to estimate difficulty but has not yet specialized its representations for the specific language. This explains why cross-lingual transfer of difficulty probes works best here.

2. **Cross-lingual semantic alignment (middle, ~50% depth)**: Liu & Niehues show that semantic equivalence across languages peaks at nearly the same depth (layer 16/32). This is consistent -- both difficulty and semantics share language-agnostic properties at approximately the same middle-layer region. The slight difference (Civelli's 15.67 vs. Liu's 16) is negligible and likely within noise.

3. **Calibration and confidence regulation (late, ~88-94% depth)**: Both Joshi et al. and the "Beyond the Final Layer" work show that calibration -- the alignment between model confidence and actual correctness -- is a *post-decisional* process. The model first makes its prediction (by layer 26), then actively recalibrates its confidence in layers 28-31. For multilingual settings, the optimal calibration layer is slightly before the final layer (29 out of 32), because the final layer reintroduces English-centric bias.

### Why This Matters for Cross-Lingual Calibration Transfer

The critical insight is that **"calibration transfer" is not the same thing as "difficulty transfer."** Difficulty estimation asks "how hard is this problem?" -- a property of the input. Calibration asks "how confident should I be in my answer?" -- a property of the model's output distribution. These are related but computationally distinct:

- Difficulty is an **input-side metacognitive property** that can be estimated before the model commits to an answer. It is naturally language-agnostic at shallow layers because it depends on structural/mathematical complexity, not linguistic form.

- Calibration is an **output-side confidence regulation mechanism** that operates after the model has already formed its prediction. It necessarily involves language-specific processing because confidence depends on how well the model handles the specific language.

### Reframing the Hypothesis

The original hypothesis -- that intermediate layers are optimal for cross-lingual calibration transfer -- needs refinement. The evidence suggests a more nuanced picture:

**For transferring difficulty signals cross-lingually**, shallow-to-middle layers (~45-50% depth) are indeed optimal, consistent with both Civelli et al. and Liu & Niehues.

**For transferring calibration signals cross-lingually**, late-intermediate layers (~88-91% depth) are optimal, but this is not the same "middle" that Liu & Niehues identified. The "Beyond the Final Layer" paper's finding that layer 29/32 works best for multilingual calibration is actually a *late* layer, not a middle layer -- it just happens to be slightly before the final layer.

The reconciled hypothesis should be: **Cross-lingual calibration transfer operates at late-intermediate layers (roughly layers 28-30 out of 32), which is the zone where the model's confidence correction mechanism is most active but before English-centric final-layer bias fully takes hold. This is distinct from -- and much deeper than -- the shallow/middle layer zone where difficulty estimation and semantic alignment are most language-agnostic.** The reason the late-intermediate zone works is not because of language-agnostic encoding (which peaks earlier) but because the calibration direction at this depth is low-dimensional and structurally similar across languages, even though the representations themselves have become language-specific.

This reframing preserves the core claim that cross-lingual calibration transfer is possible but shifts the mechanistic explanation: it is not that calibration lives in the language-agnostic zone, but rather that the confidence correction mechanism in layers 28-31 operates on a shared geometric structure (a low-dimensional direction in the residual stream) that is consistent enough across languages to permit transfer, especially when extracting from the late-intermediate position that avoids final-layer English bias.

### Sources

- [A Shared Geometry of Difficulty in Multilingual Language Models -- Civelli et al.](https://arxiv.org/abs/2601.12731)
- [Middle-Layer Representation Alignment for Cross-Lingual Transfer -- Liu & Niehues, ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Calibration Across Layers -- Joshi, Ahmad & Modi, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.742/)
- [Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration](https://arxiv.org/abs/2510.03136)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73027887-4214-4eb9-9f95-036c4fa0c801",
  "isSidechain": true,
  "agentId": "adb09762506495b0b",
  "requestId": "req_011CbBg2KnwwZ65Susgrhuft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f0ba82b-e4fa-4196-a366-1afd7bcaa267",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "e35f8964-edb8-41bf-9248-b2986ccc4fa6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1mMeuKrgCGBeXqZwK4YqB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 18504,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1605
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1882,
          "cache_read_input_tokens": 18504,
          "cache_creation_input_tokens": 1605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1605,
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
