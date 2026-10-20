# Research conversation: Search for concurrent and competing work on cross-lingual calibration transfer in LLMs from 2025-2026. I need to confirm

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a32b0b74a917828b8.jsonl`
- **Structured JSON:** [`bd7be25fb9369b4e6f2d.json`](../../sessions/bd/bd7be25fb9369b4e6f2d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-19T18:24:57.557Z_

Search for concurrent and competing work on cross-lingual calibration transfer in LLMs from 2025-2026. I need to confirm nobody is doing the same thing as: "transferring a calibration direction (linear probe) extracted from English to non-English languages via shared intermediate-layer representations."

Perform these web searches:
1. WebSearch: "cross-lingual calibration transfer LLM 2026"
2. WebSearch: "language-agnostic confidence direction representation space 2026"
3. WebSearch: "cross-lingual calibration transfer multilingual LLM arXiv 2025 2026"
4. WebSearch: "calibration direction transfer multilingual representation engineering"
5. WebSearch: "zero-shot cross-lingual uncertainty calibration 2025 2026"
6. WebSearch: site:openreview.net "cross-lingual calibration" 2026

For each search, report:
- Any papers that directly attempt cross-lingual calibration direction transfer
- Any papers that combine representation-space calibration probes with multilingual alignment
- The closest competing work and how it differs

Be thorough — this determines whether the research idea is novel. Report your findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "18d6fc2d-9994-4d6d-b87c-b5cf67907941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T18:24:57.561Z_

```json
{
  "parentUuid": "18d6fc2d-9994-4d6d-b87c-b5cf67907941",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
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
  "uuid": "3063b241-9d3e-4940-bbb6-59c750a92588",
  "timestamp": "2026-05-19T18:24:57.561Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T18:24:57.563Z_

```json
{
  "parentUuid": "3063b241-9d3e-4940-bbb6-59c750a92588",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f4e62093-d9a6-4ffb-b6d7-1fb85a7f025e",
  "timestamp": "2026-05-19T18:24:57.563Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T18:25:00.280Z_



I'll load the WebSearch tool first, then run all six searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4e62093-d9a6-4ffb-b6d7-1fb85a7f025e",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwbVGAXbqV11QaLcwk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03be18f9-ce82-4526-8ee6-cc506a66e1a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nrCMoZyXWAroJdw4jqXpv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8993,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8993,
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

_source line 5 · 2026-05-19T18:25:00.388Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013HGJmLcscW4fQyFGhUYqoE`</summary>

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
  "parentUuid": "03be18f9-ce82-4526-8ee6-cc506a66e1a3",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwbVGAXbqV11QaLcwk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91d711c-2a77-4c78-b8d4-67c250cf3e97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nrCMoZyXWAroJdw4jqXpv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8993,
      "cache_read_input_tokens": 0,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8993
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8993,
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

_source line 6 · 2026-05-19T18:25:00.391Z_

<details><summary>↩ Tool result · `toolu_013HGJmLcscW4fQyFGhUYqoE`</summary>

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
  "parentUuid": "a91d711c-2a77-4c78-b8d4-67c250cf3e97",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "ae5c72ec-32b0-4e16-afd9-33a59999d524",
  "sourceToolAssistantUUID": "a91d711c-2a77-4c78-b8d4-67c250cf3e97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T18:25:02.934Z_



Now I'll run all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae5c72ec-32b0-4e16-afd9-33a59999d524",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b992b5e-0b2f-452b-85d3-e90054dff3c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 622,
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

_source line 8 · 2026-05-19T18:25:03.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011o68s2ukHxmMLjihTwQ7yD`</summary>

```json
{
  "query": "cross-lingual calibration transfer LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b992b5e-0b2f-452b-85d3-e90054dff3c3",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0db6572-f6d1-478b-95fe-fa3295e77b40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 622,
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

_source line 9 · 2026-05-19T18:25:03.869Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018TQUBAU5dmbdkRygU1T3Bx`</summary>

```json
{
  "query": "language-agnostic confidence direction representation space 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0db6572-f6d1-478b-95fe-fa3295e77b40",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0427e97c-09a3-4e1a-9a80-aaee7663a998",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 622,
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

_source line 10 · 2026-05-19T18:25:03.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JsEuDAMtBD6gDHXTVYFKV4`</summary>

```json
{
  "query": "cross-lingual calibration transfer multilingual LLM arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0427e97c-09a3-4e1a-9a80-aaee7663a998",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08b1f410-36f1-41b5-b698-60820b3b5866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 622,
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

_source line 11 · 2026-05-19T18:25:04.309Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HUAwPJqeUy7P171wJU5aAJ`</summary>

```json
{
  "query": "calibration direction transfer multilingual representation engineering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08b1f410-36f1-41b5-b698-60820b3b5866",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9d5ac02-d027-4f26-936b-cf8b394f9038",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 622,
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

_source line 12 · 2026-05-19T18:25:04.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011DgjskCf4jAZUHnf1Ptnh2`</summary>

```json
{
  "query": "zero-shot cross-lingual uncertainty calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9d5ac02-d027-4f26-936b-cf8b394f9038",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51622f03-def8-4181-aed4-2e94d06ebf2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 8993,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 622,
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

_source line 13 · 2026-05-19T18:25:04.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LbTZVHadkW8f45eBmmizJ6`</summary>

```json
{
  "query": "site:openreview.net \"cross-lingual calibration\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51622f03-def8-4181-aed4-2e94d06ebf2c",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPwonC6SuxtLq7E5znn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "318d8b87-5f1c-41f3-820a-bbca0fb43f48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wvoc6fo7oVJXYAuvWrDqz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8993,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 8993,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 622,
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

_source line 14 · 2026-05-19T18:25:09.314Z_

<details><summary>↩ Tool result · `toolu_011o68s2ukHxmMLjihTwQ7yD`</summary>

```text
Web search results for query: "cross-lingual calibration transfer LLM 2026"

Links: [{"title":"Cross-Lingual Transfer Learning in Large Language Models","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176799777.79169627/v1?onload=true"},{"title":"Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging | OpenReview","url":"https://openreview.net/forum?id=y3CsNQal2l"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource","url":"https://arxiv.org/pdf/2603.21036"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"}]

Based on the search results, here's what I found about cross-lingual calibration transfer in LLMs for 2026:

## Recent Research (2026)

A January 2026 paper on TechRxiv discusses cross-lingual transfer learning in large language models, covering how knowledge is transferred across languages, the evolution of pretrained multilingual models, and zero-shot and few-shot transfer techniques.

Recent research indicates that current LLMs systematically underserve low-resource language communities, and that cross-lingual transfer offers a partial remedy.

## Key Technical Developments

Experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages. Research demonstrates that separately trained alignment modules can be merged with existing task-specific modules, improving cross-lingual capabilities without full re-training.

## Evaluation Challenges

Cross-lingual knowledge transfer is a property where LLMs transfer knowledge acquired in one language to others, but reliably evaluating this ability remains challenging.

The research landscape in 2026 shows active work on improving cross-lingual transfer capabilities while addressing challenges related to low-resource languages and evaluation methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0db6572-f6d1-478b-95fe-fa3295e77b40",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "5cef2194-9bd0-43d0-a6f6-5169951158a0",
  "sourceToolAssistantUUID": "e0db6572-f6d1-478b-95fe-fa3295e77b40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T18:25:10.892Z_

<details><summary>↩ Tool result · `toolu_01HUAwPJqeUy7P171wJU5aAJ`</summary>

```text
Web search results for query: "calibration direction transfer multilingual representation engineering"

Links: [{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Investigating Multilingual NMT Representations at Scale","url":"https://arxiv.org/pdf/1909.02197"}]

Based on the web search results, here are the relevant findings related to your query about calibration, direction transfer, and multilingual representation engineering:

## Multilingual Calibration in Large Language Models

Confidence calibration is the alignment of a model's predicted confidence with its actual accuracy, which is crucial for the reliable deployment of Large Language Models (LLMs). However, non-English languages suffer from systematically worse calibration.

### Key Research Findings

The final layer, biased by English-centric training, provides a poor signal for multilingual confidence, while late-intermediate layers consistently offer a more reliable and better-calibrated signal.

A suite of training-free methods has been introduced, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers for each specific language.

## Representation Transfer Across Languages

Regarding the transfer of representations between languages, transfer of steering vectors is more effective between languages with similar representations, while performance declines as representational distance grows. This research explores how representations and steering vectors can be transferred directionally between different language pairs in multilingual models.

The search results indicate active research in improving multilingual model performance through better understanding of internal representations and developing calibration methods that account for language-specific characteristics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9d5ac02-d027-4f26-936b-cf8b394f9038",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "1a9716ee-331e-499e-8b5b-34c7cba4db39",
  "sourceToolAssistantUUID": "d9d5ac02-d027-4f26-936b-cf8b394f9038",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:25:11.736Z_

<details><summary>↩ Tool result · `toolu_018TQUBAU5dmbdkRygU1T3Bx`</summary>

```text
Web search results for query: "language-agnostic confidence direction representation space 2026"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Published as a conference paper at ICLR 2026 AGNOSTICS:","url":"https://arxiv.org/pdf/2508.04865"},{"title":"Language Models Represent Space and Time","url":"https://arxiv.org/pdf/2310.02207"},{"title":"LANGUAGE-AGNOSTIC REPRESENTATION LEARNING","url":"https://www-cs.stanford.edu/people/jure/pubs/sourcecode-iclr21.pdf"}]

I found several relevant research papers from the web search. Here are the results:

1. **"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models"** - This paper discusses how intermediate layers encode more language-agnostic representations, suggesting the final layer provides a sub-optimal signal for multilingual confidence.

2. **"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models"** - This research characterizes the geometry of correctness representations in transformer activations, finding that the discriminative signal is simple and occupies 3–8 dimensions across 9 models from 5 architecture families. The learned direction produces meaningful changes in error rates through activation steering.

3. **"AGNOSTICS: Published as a conference paper at ICLR 2026"** - This paper presents an approach that works by reformulating language-specific datasets into a uniform language-agnostic format using LLMs.

4. **"Language Models Represent Space and Time"** - This paper discusses how language models encode spatial and temporal representations in a linear fashion within their hidden states.

5. **"Language-Agnostic Representation Learning"** - This work focuses on models that do not rely on language-specific features, facilitating multi-language training through unified representations.

These papers appear to explore different aspects of how language models develop language-agnostic representations and confidence signals in their internal representation spaces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0427e97c-09a3-4e1a-9a80-aaee7663a998",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "eae8eff0-adaa-4698-808c-66fcac44385f",
  "sourceToolAssistantUUID": "0427e97c-09a3-4e1a-9a80-aaee7663a998",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T18:25:11.841Z_

<details><summary>↩ Tool result · `toolu_01LbTZVHadkW8f45eBmmizJ6`</summary>

```text
Web search results for query: "site:openreview.net "cross-lingual calibration" 2026"

Links: [{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=8DBHkEe0sm"},{"title":"Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | OpenReview","url":"https://openreview.net/forum?id=hsMkpzr9Oy"},{"title":"Cross-Lingual Ability of Multilingual BERT: An Empirical Study | OpenReview","url":"https://openreview.net/forum?id=HJeT3yrtDr"},{"title":"Enhancing Cross-Lingual Embedding Alignment with Additive Keywords for International Trade Product Classification | OpenReview","url":"https://openreview.net/forum?id=n1rsWhJf8B"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"On Calibration of Multilingual Question Answering LLMs | OpenReview","url":"https://openreview.net/forum?id=4klghu2PTj"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"},{"title":"$C^3$: Confidence Calibration Model Cascade for Inference-Efficient   Cross-Lingual Natural Language Understanding","url":"https://arxiv.org/pdf/2402.15991"}]

Based on the search results, I found several papers related to cross-lingual calibration from OpenReview and arXiv published in 2026 or recently:

**On OpenReview:**

1. "On Calibration of Multilingual Question Answering LLMs" investigates calibration in in-distribution, out-of-distribution, and cross-lingual transfer settings, including post-hoc methods and regularized fine-tuning.

2. "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" examines cross-lingual alignment, which aims to align multilingual representations, while also analyzing how this pursuit of representational convergence can inadvertently cause "cultural erasure".

3. "Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment" leverages English as a pivot language and computes alignment between English and non-English languages using parallel sentences.

**Also found (from arXiv):**

4. "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" conducts layer-wise investigation of multilingual calibration and introduces training-free calibration methods leveraging intermediate representations.

These papers address various aspects of cross-lingual calibration and alignment in modern language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "318d8b87-5f1c-41f3-820a-bbca0fb43f48",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "fb02ecf6-0b1f-4f3f-bfbd-cde2cb19afee",
  "sourceToolAssistantUUID": "318d8b87-5f1c-41f3-820a-bbca0fb43f48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:25:12.143Z_

<details><summary>↩ Tool result · `toolu_011DgjskCf4jAZUHnf1Ptnh2`</summary>

```text
Web search results for query: "zero-shot cross-lingual uncertainty calibration 2025 2026"

Links: [{"title":"Calibrating Zero-shot Cross-lingual (Un-)structured ...","url":"https://aclanthology.org/2022.emnlp-main.170.pdf"},{"title":"Calibrating Zero-shot Cross-lingual (Un-)structured Predictions","url":"https://openreview.net/pdf?id=xNS4k7_LVzk"},{"title":"Boosting Cross-Lingual Transfer via Self-Learning with Uncertainty   Estimation","url":"https://arxiv.org/pdf/2109.00194"},{"title":"Self-learning framework of zero-shot cross-lingual transfer with uncertainty estimation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12073183"},{"title":"Zero-shot Cross-lingual Transfer is Under-specified Optimization","url":"https://arxiv.org/pdf/2207.05666"},{"title":"Unleashing the Multilingual Encoder Potential: Boosting Zero-Shot   Performance via Probability Calibration","url":"https://arxiv.org/pdf/2310.05069"},{"title":"Zero-Shot Cross-Lingual Transfer using Prefix-Based Adaptation - ACL Anthology","url":"https://aclanthology.org/2025.mrl-main.26/"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"}]

Based on the search results, I found several relevant papers on zero-shot cross-lingual uncertainty calibration:

## Recent Work (2022-2025)

A 2022 paper titled "Calibrating Zero-shot Cross-lingual (Un-)structured Predictions" addresses this topic directly. This work highlights that since zero-shot cross-lingual transfer represents shifts in the data distribution, the point estimates are likely to be miscalibrated.

Another recent approach combines models with various calibration techniques that modify the probabilities of label words predicted by the models, evaluated on both monolingual and multilingual encoders, achieving substantial performance gains through calibration.

## Related Research Areas

One framework adapts three different uncertainties specifically for cross-lingual transfer (Language Heteroscedastic/Homoscedastic Uncertainty and Evidential Uncertainty), evaluated on Named Entity Recognition and Natural Language Inference covering 40 languages.

Recent work from 2025 explores zero-shot cross-lingual transfer with new large language models like Llama and Mistral, noting that while these models enable zero-shot cross-lingual transfer, adapting them to new tasks across languages remains challenging.

The research shows active interest in this area, with papers from 2022 through 2025 focusing on improving calibration and uncertainty estimation in zero-shot cross-lingual settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51622f03-def8-4181-aed4-2e94d06ebf2c",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "cf670e30-ec62-4ed4-9966-bd766167c758",
  "sourceToolAssistantUUID": "51622f03-def8-4181-aed4-2e94d06ebf2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:25:19.089Z_

<details><summary>↩ Tool result · `toolu_01JsEuDAMtBD6gDHXTVYFKV4`</summary>

```text
Web search results for query: "cross-lingual calibration transfer multilingual LLM arXiv 2025 2026"

Links: [{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"[2406.13229] Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/abs/2406.13229"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"},{"title":"A Three-Pronged Approach to Cross-Lingual Adaptation with Multilingual   LLMs","url":"https://arxiv.org/pdf/2406.17377"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/html/2406.13229v1"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/pdf/2406.13229"}]

I found several relevant research papers on arXiv related to cross-lingual transfer in multilingual LLMs:

1. **"On the Calibration of Multilingual Question Answering LLMs"** (arXiv:2311.08669) - This paper shows that pre-trained multilingual LLMs, fine-tuned on English QA, are not well calibrated in languages other than English, specifically low-resource ones like Bengali.

2. **"Probing the Emergence of Cross-lingual Alignment during LLM Training"** (arXiv:2406.13229) - Multilingual Large Language Models (LLMs) achieve remarkable levels of zero-shot cross-lingual transfer performance, which is predicated on their ability to align languages without explicit supervision from parallel sentences. The study uses intrinsic probing techniques to correlate the degree of cross-lingual neuron overlap with the zero-shot cross-lingual transfer performance.

3. **"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs"** (arXiv:2511.14774) - This paper presents an automated generation pipeline to isolate and measure cross-lingual knowledge transfer by identifying self-contained, time-sensitive knowledge entities and verifying them against the model's knowledge, then generating factual questions translated into multiple languages.

4. **"A Three-Pronged Approach to Cross-Lingual Adaptation with Multilingual LLMs"** (arXiv:2406.17377) - This paper explores different methods for cross-lingual adaptation in information extraction tasks for low-resource languages.

These papers address various aspects of cross-lingual transfer and calibration in multilingual language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08b1f410-36f1-41b5-b698-60820b3b5866",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "58b8f0ed-dc2d-4ba3-aa84-63ae517e5ce9",
  "sourceToolAssistantUUID": "08b1f410-36f1-41b5-b698-60820b3b5866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-19T18:25:24.145Z_

Now let me do a few more targeted follow-up searches on the most relevant papers I found, to get more detail on the closest competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b8f0ed-dc2d-4ba3-aa84-63ae517e5ce9",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPyBXRJnz2FE4ksmqnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0ba09af-d03f-4297-88cd-a0707137218a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KG6KXg1p7YVttSNHueUVdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2157,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 9615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2264,
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

_source line 21 · 2026-05-19T18:25:24.633Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E9ucUK3gjevTb4cUngkdNA`</summary>

```json
{
  "query": "\"Beyond the Final Layer\" intermediate representations multilingual calibration arXiv 2510.03136"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0ba09af-d03f-4297-88cd-a0707137218a",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPyBXRJnz2FE4ksmqnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90654fca-4a17-438e-b261-bcd8ad558bef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KG6KXg1p7YVttSNHueUVdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2157,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 9615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2264,
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

_source line 22 · 2026-05-19T18:25:25.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GbCeLeL2cjrNAbdiCLCX8w`</summary>

```json
{
  "query": "\"The Confidence Manifold\" geometric structure correctness representations language models arXiv 2602.08159"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90654fca-4a17-438e-b261-bcd8ad558bef",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPyBXRJnz2FE4ksmqnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94c4c908-8cae-46b2-ab25-c8ca6ed9111c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KG6KXg1p7YVttSNHueUVdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2157,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 9615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2264,
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

_source line 23 · 2026-05-19T18:25:25.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0195hnDaTrfLVgM45k4w4aaH`</summary>

```json
{
  "query": "\"Improving Multilingual Language Models by Aligning Representations through Steering\" arXiv 2505.12584"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94c4c908-8cae-46b2-ab25-c8ca6ed9111c",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPyBXRJnz2FE4ksmqnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f8b5fc6-81e9-4268-afb8-8616d0507b54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KG6KXg1p7YVttSNHueUVdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2157,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 9615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2264,
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

_source line 24 · 2026-05-19T18:25:26.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012wDSyWnh59EKhBTM2CobPE`</summary>

```json
{
  "query": "\"Investigating the Multilingual Calibration Effects\" language model instruction-tuning arXiv 2601.01362"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f8b5fc6-81e9-4268-afb8-8616d0507b54",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPyBXRJnz2FE4ksmqnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "660a7bd3-fece-469c-9ec8-99abaef71db2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KG6KXg1p7YVttSNHueUVdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2157,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 9615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2264,
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

_source line 25 · 2026-05-19T18:25:26.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BSmQGaAyWqUPQBtqbW4jEf`</summary>

```json
{
  "query": "linear probe calibration direction transfer across languages LLM representation engineering 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "660a7bd3-fece-469c-9ec8-99abaef71db2",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPyBXRJnz2FE4ksmqnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c3e18ee-f66e-47aa-933b-1eded80bf6da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KG6KXg1p7YVttSNHueUVdC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2157,
      "cache_creation_input_tokens": 2264,
      "cache_read_input_tokens": 9615,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2157,
          "output_tokens": 336,
          "cache_read_input_tokens": 9615,
          "cache_creation_input_tokens": 2264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2264,
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

_source line 26 · 2026-05-19T18:25:32.218Z_

<details><summary>↩ Tool result · `toolu_01E9ucUK3gjevTb4cUngkdNA`</summary>

```text
Web search results for query: ""Beyond the Final Layer" intermediate representations multilingual calibration arXiv 2510.03136"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=CUS9OTCGdt"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"},{"title":"dblp: Nigel Collier","url":"https://dblp.org/pid/90/2619.html"}]

Based on the search results, I found the paper "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" (arXiv 2510.03136).

**Overview:**

The paper is authored by Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen from the Language Technology Lab at the University of Cambridge.

**Key Findings:**

The work conducts the first large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration.

The authors investigate the model's internal representations and find that the final layer, biased by English-centric training, provides a poor signal for multilingual confidence. In contrast, their layer-wise analysis uncovers that late-intermediate layers consistently offer a more reliable and better-calibrated signal.

**Proposed Method:**

The paper introduces a suite of training-free methods, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers for each specific language.

The study highlights the hidden costs of English-centric alignment and offers a new path toward building more globally equitable and trustworthy LLMs by looking beyond the final layer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90654fca-4a17-438e-b261-bcd8ad558bef",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "25525d08-44ec-4ab9-a6cd-803cd58860e9",
  "sourceToolAssistantUUID": "90654fca-4a17-438e-b261-bcd8ad558bef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T18:25:32.309Z_

<details><summary>↩ Tool result · `toolu_01GbCeLeL2cjrNAbdiCLCX8w`</summary>

```text
Web search results for query: ""The Confidence Manifold" geometric structure correctness representations language models arXiv 2602.08159"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/html/2602.00977"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/pdf/2602.00977"},{"title":"(PDF) The Confidence Manifold: Geometric Structure of ...","url":"https://www.researchgate.net/publication/400604407_The_Confidence_Manifold_Geometric_Structure_of_Correctness_Representations_in_Language_Models"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

**"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models"** (arXiv:2602.08159)

The paper characterizes the geometry of correctness representations across 9 models from 5 architecture families, finding that the structure is simple: the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.

Centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy.

The researchers validate causally through activation steering: the learned direction produces 10.9 percentage point changes in error rates while random directions show no effect. Additionally, internal probes achieve 0.80-0.97 AUC while output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC, indicating that the correctness signal exists internally but is not expressed in outputs.

The paper was published on February 8, 2026, and is authored by Seonglae Cho, Zekun Wu, Kleyton Da Costa, and Adriano Koshiyama.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94c4c908-8cae-46b2-ab25-c8ca6ed9111c",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "c1409932-589d-43c1-b9a6-7c9c99159996",
  "sourceToolAssistantUUID": "94c4c908-8cae-46b2-ab25-c8ca6ed9111c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T18:25:32.455Z_

<details><summary>↩ Tool result · `toolu_012wDSyWnh59EKhBTM2CobPE`</summary>

```text
Web search results for query: ""Investigating the Multilingual Calibration Effects" language model instruction-tuning arXiv 2601.01362"

Links: [{"title":"[2601.01362] Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/abs/2601.01362"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/html/2601.01362"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/pdf/2401.01854"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand   for Multilingual Instructions?","url":"https://arxiv.org/pdf/2402.13703"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/investigating-multilingual-instruction-tuning-do-polyglot-models"}]

I found the paper you're looking for. Here's what I can tell you about it:

The paper "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning" was authored by Jerry Huang, Peng Lu, Qiuhao Zeng, Yusuke Iwasawa, Yutaka Matsuo, Sarath Chandar, Edison Marrese-Taylor, and Irene Li.

The paper addresses how the relationship between large language models (LLMs) and their calibration remains an open area of research. The authors examine a critical gap in the calibration of LLMs within multilingual settings, attempting to understand how data scarcity can lead to different calibration effects.

Key findings include: Their analysis on two multilingual benchmarks covering 29 and 42 languages reveals that even in low-resource languages, model confidence can increase significantly after instruction-tuning on high-resource language SFT datasets, but improvements in accuracy are marginal or non-existent, resulting in mis-calibration. The researchers found that label smoothing is a reasonable method to alleviate this concern without requiring low-resource SFT data, maintaining better calibration across all languages.

The paper was submitted to arXiv on January 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "660a7bd3-fece-469c-9ec8-99abaef71db2",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "96d2af6e-1fcc-4bb6-ab5d-23c9f1e1afc8",
  "sourceToolAssistantUUID": "660a7bd3-fece-469c-9ec8-99abaef71db2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T18:25:32.484Z_

<details><summary>↩ Tool result · `toolu_0195hnDaTrfLVgM45k4w4aaH`</summary>

```text
Web search results for query: ""Improving Multilingual Language Models by Aligning Representations through Steering" arXiv 2505.12584"

Links: [{"title":"[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/abs/2505.12584"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"[Literature Review] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://www.themoonlight.io/en/review/improving-multilingual-language-models-by-aligning-representations-through-steering"},{"title":"Improving Multilingual Language Models by Aligning Representations","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Paper page - Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://huggingface.co/papers/2505.12584"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=625&show=100"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.118/"}]

Here are the search results for the arXiv paper 2505.12584:

## Paper Overview

This paper investigates how Large Language Models (LLMs) represent non-English tokens and proposes a lightweight intervention method using representation steering, where a learned vector is added to the residual stream at a single model layer to enhance multilingual performance.

## Key Contributions

The authors propose and validate a method to enhance the multilingual capabilities of LLMs by steering the representations of a single layer, using a learned alignment with English. They demonstrate that a single steering vector can be shared across structurally similar languages, enabling zero-shot cross-linguistic transfer.

## Core Methodology

The core idea is based on the observation that LLMs often translate non-English prompts internally into English, but this translation is imperfect, leading to inconsistent performance. A "steering vector" is trained that, when added to the hidden state representation of a non-English prompt at a specific layer, shifts its representation closer to that of its English equivalent.

## Results

Through extensive experiments across seven competitive baselines including prompt optimization, supervised fine-tuning (SFT), in-context learning, cross-lingual transfer, and translation-based methods, the approach consistently outperforms most alternatives and achieves performance on par with production-grade translation systems while requiring far fewer resources.

**Authors:** Omar Mahmoud, Buddhika Laknath Semage, Thommen George Karimpanal, Santu Rana

**Submitted:** May 19, 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f8b5fc6-81e9-4268-afb8-8616d0507b54",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "272f3545-ea19-4ad4-9f3f-76119cdb083a",
  "sourceToolAssistantUUID": "3f8b5fc6-81e9-4268-afb8-8616d0507b54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T18:25:34.229Z_

<details><summary>↩ Tool result · `toolu_01BSmQGaAyWqUPQBtqbW4jEf`</summary>

```text
Web search results for query: "linear probe calibration direction transfer across languages LLM representation engineering 2025 2026"

Links: [{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets","url":"https://arxiv.org/pdf/2310.06824"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"How Language Directions Align with Token Geometry in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.16693"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"LLMs Encode How Difficult Problems Are","url":"https://arxiv.org/pdf/2510.18147"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"[2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/abs/2512.22245"}]

I found several relevant papers on this topic. Here are the key results:

## Recent Research on Linear Probes and Representation Engineering (2025-2026)

**Representation Engineering Survey**: A 2025 survey on representation engineering for large language models discusses how probes have been applied to investigate LLM biases, jailbreak formation mechanisms, cross-lingual retrieval, and other linguistic properties.

**Calibrating LLM Judges with Linear Probes**: A recent paper addresses the LLM-as-judge paradigm and the challenge of uncertainty estimation, noting that reasoning-capable models with linear probes for calibration are becoming increasingly prevalent.

**Multilingual LLM Representations**: Research has been conducted on how language directions align with token geometry in multilingual LLMs, focusing on representation learning and linear probing.

**Multilingual Calibration**: A 2025 study presents "the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families".

**Problem Difficulty Encoding**: Linear probes trained across 60 models show that human-derived difficulty ratings are strongly and linearly decodable from model activations, demonstrating the effectiveness of linear probing for discovering interpretable directions.

**Correctness Representation**: Recent work tests the Linear Representation Hypothesis for correctness, using difference-of-means linear probes to verify whether correctness signals are accessible as linear features of the representation space.

These papers collectively demonstrate active research in 2025-2026 on understanding how linear directions encode meaningful features in LLM representations across different languages and contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c3e18ee-f66e-47aa-933b-1eded80bf6da",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "c09c87c2-6f66-48af-a7b4-587d6ef56a81",
  "sourceToolAssistantUUID": "3c3e18ee-f66e-47aa-933b-1eded80bf6da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T18:25:37.268Z_

Let me run a few more targeted searches to ensure thoroughness on the specific intersection of calibration probes and cross-lingual transfer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c09c87c2-6f66-48af-a7b4-587d6ef56a81",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPzJFGCxHsrC71A9XAD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62ac245a-5810-402a-80c0-7bc2826d3bc1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCWmTMysNx1KsN5npsmPHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 11879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6093,
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

_source line 32 · 2026-05-19T18:25:38.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012LzygSoA8BNRDsB7hEKWnT`</summary>

```json
{
  "query": "\"steering vector\" \"cross-lingual\" calibration confidence correctness probe transfer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62ac245a-5810-402a-80c0-7bc2826d3bc1",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPzJFGCxHsrC71A9XAD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60f199c2-80fa-4819-84a0-a7939143d224",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCWmTMysNx1KsN5npsmPHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 11879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6093,
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

_source line 33 · 2026-05-19T18:25:38.681Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E76tULkKvA9aw8afhLLdHV`</summary>

```json
{
  "query": "\"truth direction\" OR \"correctness direction\" multilingual cross-lingual transfer representation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f199c2-80fa-4819-84a0-a7939143d224",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPzJFGCxHsrC71A9XAD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57073de0-7677-49a2-9553-298cd29e8c13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCWmTMysNx1KsN5npsmPHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 11879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6093,
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

_source line 34 · 2026-05-19T18:25:39.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UzJLUsAKfte9EMXoCVzJ3`</summary>

```json
{
  "query": "representation engineering truthfulness direction multilingual language-agnostic probe 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57073de0-7677-49a2-9553-298cd29e8c13",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCPzJFGCxHsrC71A9XAD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6aebd55-0266-424a-b5d4-f5c280027d09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCWmTMysNx1KsN5npsmPHF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 11879,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6093
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 11879,
          "cache_creation_input_tokens": 6093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6093,
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

_source line 35 · 2026-05-19T18:25:49.184Z_

<details><summary>↩ Tool result · `toolu_012LzygSoA8BNRDsB7hEKWnT`</summary>

```text
Web search results for query: ""steering vector" "cross-lingual" calibration confidence correctness probe transfer 2025 2026"

Links: [{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Language-Specific Steering Vectors","url":"https://www.emergentmind.com/topics/language-specific-steering-vectors"},{"title":"CAST: Conditional Activation Steering in LMs","url":"https://www.emergentmind.com/topics/conditional-activation-steering-cast"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/pdf/2602.06022"}]

Here are the search results for your query about steering vectors, cross-lingual approaches, calibration, confidence, correctness, probes, and transfer learning from 2025-2026:

## Key Papers Found:

1. **CORAL (Correctness-Optimized Residual Activation Lens)** - This approach demonstrates gains that transfer to held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements. Recent mechanistic work suggests that confidence and correctness signals fall into the distributed category, and regularized probes extract correctness signals that sparse methods miss, with relevant methods including ITI, SteerConf, and CCPS.

2. **The Confidence Manifold** - Through activation steering, the learned direction produces 10.9 percentage point changes in error rates while random directions show no effect. Internal probes achieve 0.80–0.97 AUC while output-based methods achieve only 0.44–0.64 AUC; the correctness signal exists internally but is not expressed in outputs.

3. **CLaS-Bench (Cross-Lingual Alignment and Steering Benchmark)** - This evaluates cross-lingual steering where prompt and output languages differ, comparing steering approaches including neuron-level interventions, residual-stream vectors, probe-derived directions, and LDA/PCA/SAE vectors, measuring success along forcing (intended language) and relevance (conceptual appropriateness) dimensions.

4. **Language-Specific Steering Vectors** - Results show significant reduction of language confusion in cross-lingual configurations, retention/improvement of task performance, with up to +50 percentage point improvements over baselines for certain language pairs.

5. **CAST (Conditional Activation Steering)** - Cross-lingual accuracy gains range from 44.9–95.2% depending on language, and steering directions extracted from high-resource source tasks are injected during target-task inference to yield zero-shot-like transfer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60f199c2-80fa-4819-84a0-a7939143d224",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "b0f6cbea-4783-4e7b-ae47-6e2d2611dd82",
  "sourceToolAssistantUUID": "60f199c2-80fa-4819-84a0-a7939143d224",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T18:25:49.294Z_

<details><summary>↩ Tool result · `toolu_01E76tULkKvA9aw8afhLLdHV`</summary>

```text
Web search results for query: ""truth direction" OR "correctness direction" multilingual cross-lingual transfer representation 2025 2026"

Links: [{"title":"[2601.04036] Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation","url":"https://arxiv.org/abs/2601.04036"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://aclanthology.org/2025.acl-long.778.pdf"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Cross-Lingual Transfer Learning for Speech Translation","url":"https://aclanthology.org/2025.naacl-short.4.pdf"},{"title":"Unsupervised cross-lingual model transfer for named entity recognition with contextualized word representations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454935/"},{"title":"On cross-lingual retrieval with multilingual text encoders","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9090691/"}]

I found several relevant papers on multilingual cross-lingual transfer and representation from 2025-2026, but none of them specifically mention "truth direction" or "correctness direction." Here's what the search revealed:

## Recent Research on Cross-Lingual Transfer (2025-2026)

Multilingual machine translation systems aim to make knowledge accessible across languages, yet learning effective cross-lingual representations remains challenging, especially pronounced for low-resource languages, where limited parallel data constrains generalization and transfer.

Recent work focuses on middle-layer representation alignment, with alignment objectives operating on middle-layer representations.

Cross-lingual alignment aims to align multilingual representations enabling Large Language Models to seamlessly transfer knowledge across languages, though this pursuit of representational convergence can inadvertently cause "cultural erasure", the functional loss of providing culturally-situated responses that should diverge based on the query language.

The search results don't contain papers specifically about "truth direction" or "correctness direction" in the context of multilingual cross-lingual transfer. These concepts may be from papers that aren't well-indexed in web search results, or they may use different terminology. If you're looking for papers on these specific topics, I'd recommend searching directly on arXiv.org or checking recent conference proceedings (ACL, NAACL, etc.) from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57073de0-7677-49a2-9553-298cd29e8c13",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "ce690ea9-6d30-4bb3-a64d-ea5dd59c6e3c",
  "sourceToolAssistantUUID": "57073de0-7677-49a2-9553-298cd29e8c13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T18:25:51.194Z_

<details><summary>↩ Tool result · `toolu_019UzJLUsAKfte9EMXoCVzJ3`</summary>

```text
Web search results for query: "representation engineering truthfulness direction multilingual language-agnostic probe 2025"

Links: [{"title":"Representation Engineering (RepE)","url":"https://www.emergentmind.com/topics/representation-engineering-repe"},{"title":"Representation Engineering in AI Systems","url":"https://www.emergentmind.com/topics/representation-engineering"},{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.17601v1"},{"title":"[2502.17601] Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/abs/2502.17601"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"}]

Based on the search results, I found relevant information about representation engineering, truthfulness, and probing in language models. Here are the key findings:

## Representation Engineering and Truthfulness

Representation Engineering (RepE) is a paradigm for controlling and analyzing deep neural models by identifying and manipulating high-level conceptual representations directly within the model's hidden activations, treating concepts such as truthfulness as directions or subspaces in a model's high-dimensional internal state.

Models' tendency to produce factual content can be enhanced or controlled via truthfulness or honesty directions.

## Probing for Truthfulness

Several studies have found effective solutions to detect truthfulness representations through different methods of probing. For example, SAPLMA trains a classifier on LLM hidden states to predict the truthfulness of statements, focusing on out-of-distribution generalization and improving over probability-based methods.

## Multilingual and Language-Agnostic Approaches

Cross-lingual transfer has been achieved through sequential injection of "English-reasoning" and target-language anchoring vectors (MRRE) at mid/late layers, enabling LLMs to match or exceed English-level reasoning in low-resource languages.

The search results also reference a comprehensive 2025 survey on representation engineering for large language models that covers various reading and control techniques applicable across different languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6aebd55-0266-424a-b5d4-f5c280027d09",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "41e9c870-e757-4e5a-a951-2b52552ff92a",
  "sourceToolAssistantUUID": "c6aebd55-0266-424a-b5d4-f5c280027d09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T18:25:54.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vztqu6xNL9M5d4Mn7wr1Fy`</summary>

```json
{
  "query": "CORAL \"Correctness-Optimized Residual Activation Lens\" transferable calibration steering arXiv 2602.06022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e9c870-e757-4e5a-a951-2b52552ff92a",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCQ1YpPhtBWMNmJr1me9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65d41035-652d-4cc4-8a99-082a6091ae19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcPKaUvdLHQYv7fgcCbcd1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 17972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T18:25:54.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PEE4J7XMEocDAJiMDk17jo`</summary>

```json
{
  "query": "CLaS-Bench cross-lingual alignment steering benchmark arXiv 2601.08331 probe-derived directions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65d41035-652d-4cc4-8a99-082a6091ae19",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCQ1YpPhtBWMNmJr1me9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45b7cd5d-ad5e-4e7d-9321-45e4533f11a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcPKaUvdLHQYv7fgcCbcd1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 17972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T18:25:55.349Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMSYFcE2L9d94FjaAvw3eZ`</summary>

```json
{
  "query": "\"Middle-Layer Representation Alignment\" cross-lingual transfer fine-tuned LLMs arXiv 2502.14830"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b7cd5d-ad5e-4e7d-9321-45e4533f11a4",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCQ1YpPhtBWMNmJr1me9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cdae768-22bf-41ff-94e9-841bd7a606e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcPKaUvdLHQYv7fgcCbcd1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 17972,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 17972,
          "cache_creation_input_tokens": 2310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2310,
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

_source line 41 · 2026-05-19T18:26:01.071Z_

<details><summary>↩ Tool result · `toolu_01PEE4J7XMEocDAJiMDk17jo`</summary>

```text
Web search results for query: "CLaS-Bench cross-lingual alignment steering benchmark arXiv 2601.08331 probe-derived directions"

Links: [{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/html/2601.08331v1"},{"title":"[2601.08331] CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/abs/2601.08331"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"}]

Based on the search results, I found information about CLaS-Bench and the arXiv paper 2601.08331:

CLaS-Bench is a lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods.

The benchmark evaluates a broad array of steering techniques, including residual-stream DiffMean interventions, probe-derived directions, language-specific neurons, PCA/LDA vectors, Sparse Autoencoders, and prompting baselines.

Steering performance is measured along two axes: language control and semantic relevance, combined into a single harmonic-mean steering score. The results show that across languages the simple residual-based DiffMean method consistently outperforms all other methods.

A layer-wise analysis reveals that language-specific structure emerges predominantly in later layers and steering directions cluster based on language family.

CLaS-Bench is the first standardized benchmark for multilingual steering, enabling both rigorous scientific analysis of language representations and practical evaluation of steering as a low-cost adaptation alternative.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45b7cd5d-ad5e-4e7d-9321-45e4533f11a4",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "7ae1979d-e6d3-4655-84e1-86adf3201d42",
  "sourceToolAssistantUUID": "45b7cd5d-ad5e-4e7d-9321-45e4533f11a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T18:26:04.262Z_

<details><summary>↩ Tool result · `toolu_01Vztqu6xNL9M5d4Mn7wr1Fy`</summary>

```text
Web search results for query: "CORAL "Correctness-Optimized Residual Activation Lens" transferable calibration steering arXiv 2602.06022"

Links: [{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering","url":"http://paperreading.club/page?id=374945"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"}]

I found the paper! Here's what CORAL is about:

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

**Problem it addresses:**
Large language models exhibit persistent miscalibration, especially after instruction tuning and preference alignment, and while modified training objectives can improve calibration, retraining is expensive. Most existing inference-time steering methods optimize proxies for correctness rather than correctness itself.

**Key results:**
CORAL consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. These gains transfer without retraining to held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

**Technical approach:**
The method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time, with joint optimization for the accuracy and calibration components of the Brier score.

The paper was published on February 5, 2026 (arXiv:2602.06022).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65d41035-652d-4cc4-8a99-082a6091ae19",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "78bfa8f9-37e0-4080-822c-01621006ec41",
  "sourceToolAssistantUUID": "65d41035-652d-4cc4-8a99-082a6091ae19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T18:26:04.758Z_

<details><summary>↩ Tool result · `toolu_01SMSYFcE2L9d94FjaAvw3eZ`</summary>

```text
Web search results for query: ""Middle-Layer Representation Alignment" cross-lingual transfer fine-tuned LLMs arXiv 2502.14830"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.14830v1"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - haebom","url":"https://slashpage.com/haebom/y9e1xp2xyyx54m7k35vz?lang=en&tl=en"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://arxiv.org/pdf/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/389207484_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"}]

I found the paper you're looking for! Here's what I found:

## "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs"

**Authors:** Danni Liu and Jan Niehues

**Key Findings:**

Through analysis of LLM internal representations from over 1,000+ language pairs, the authors discover that middle layers exhibit the strongest potential for cross-lingual alignment. They propose a middle-layer alignment objective integrated into task-specific training.

**Problem Addressed:**

While large language models demonstrate remarkable capabilities at task-specific applications through fine-tuning, extending these benefits across diverse languages is essential for broad accessibility. However, effective cross-lingual transfer is hindered by LLM performance gaps across languages and the scarcity of fine-tuning data in many languages.

**Experimental Results:**

Experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages. The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment.

The paper was published in February 2025 and has been accepted to the ACL 2025 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cdae768-22bf-41ff-94e9-841bd7a606e4",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "73c35534-5e44-4856-8f41-c2ed7ddaaa3f",
  "sourceToolAssistantUUID": "2cdae768-22bf-41ff-94e9-841bd7a606e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T18:26:07.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AZTsvkYZdJ7Xus37HrtQMc`</summary>

```json
{
  "query": "\"Cross-Lingual Activation Steering\" multilingual language models arXiv 2601.16390"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73c35534-5e44-4856-8f41-c2ed7ddaaa3f",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCQ2Yque5MroW8ZcKqVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61b2967b-d432-472b-a18e-2212e1b6ee11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPgALjmP5TduVAQzNARpif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2486,
      "cache_read_input_tokens": 20282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2486,
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

_source line 45 · 2026-05-19T18:26:08.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012GPpuBbCpENqeH9EZn9izE`</summary>

```json
{
  "query": "CORAL correctness probe multilingual cross-lingual languages calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61b2967b-d432-472b-a18e-2212e1b6ee11",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCQ2Yque5MroW8ZcKqVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53316836-c19e-415e-960f-a6423fe84e2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPgALjmP5TduVAQzNARpif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2486,
      "cache_read_input_tokens": 20282,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 20282,
          "cache_creation_input_tokens": 2486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2486,
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

_source line 46 · 2026-05-19T18:26:16.058Z_

<details><summary>↩ Tool result · `toolu_01AZTsvkYZdJ7Xus37HrtQMc`</summary>

```text
Web search results for query: ""Cross-Lingual Activation Steering" multilingual language models arXiv 2601.16390"

Links: [{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"}]

I found the paper you're looking for. Here's what I discovered:

Cross-Lingual Activation Steering (CLAS) is a training-free inference-time intervention that selectively modulates neuron activations. 

Large language models exhibit strong multilingual capabilities, yet significant performance gaps persist between dominant and non-dominant languages, with prior work attributing this gap to imbalances between shared and language-specific neurons in multilingual representations.

The paper evaluates CLAS on classification and generation benchmarks, achieving average improvements of 2.3% (Acc.) and 3.4% (F1) respectively, while maintaining high-resource language performance.

The research discovers that effective transfer operates through functional divergence rather than strict alignment; performance gains correlate with increased language cluster separation.

The results demonstrate that targeted activation steering can unlock latent multilingual capacity in existing models without modification to model weights.

The paper was submitted to arXiv on January 23, 2026, by authors Rhitabrat Pokharel, Ameeta Agrawal, and Tanay Nagar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61b2967b-d432-472b-a18e-2212e1b6ee11",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "1621abca-ed60-484f-91c8-bafd9edbf663",
  "sourceToolAssistantUUID": "61b2967b-d432-472b-a18e-2212e1b6ee11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T18:26:21.235Z_

<details><summary>↩ Tool result · `toolu_012GPpuBbCpENqeH9EZn9izE`</summary>

```text
Web search results for query: "CORAL correctness probe multilingual cross-lingual languages calibration 2026"

Links: [{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"[2604.25676] CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG","url":"https://arxiv.org/abs/2604.25676"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"}]

Based on the search results, I found information about CORAL and multilingual/cross-lingual calibration research:

## Main CORAL Method

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. CORAL consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. These gains transfer without retraining to held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

## Multilingual/Cross-lingual Calibration Research

There are also related research efforts on multilingual calibration:

- A systematic evaluation of multilingual calibration was conducted across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families.

- Standard supervised fine-tuning (SFT) for multilingual languages shows improvements in accuracy that are marginal or non-existent, resulting in mis-calibration, though label smoothing appears to alleviate this concern while maintaining better calibration across all languages.

The 2026 research appears to be advancing the understanding of how to improve both correctness and calibration in language models, with emerging work specifically addressing multilingual and cross-lingual considerations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53316836-c19e-415e-960f-a6423fe84e2c",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a32b0b74a917828b8",
  "type": "user",
  "uuid": "44be7e7e-eada-4268-99ca-901aae7bce51",
  "sourceToolAssistantUUID": "53316836-c19e-415e-960f-a6423fe84e2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-19T18:27:20.024Z_

Here is my thorough analysis of the competitive landscape for your proposed research idea -- transferring a calibration direction (linear probe) extracted from English to non-English languages via shared intermediate-layer representations.

---

## Novelty Assessment: Cross-Lingual Calibration Direction Transfer

### Summary Verdict

**No paper found that directly does what you propose.** The specific idea of extracting a linear calibration/correctness probe from English activations and applying it zero-shot to non-English activations at shared intermediate layers is not claimed by any existing work I could find. However, several papers come very close to individual components of the idea, and the gap is narrowing rapidly. Below is the detailed breakdown.

---

### The Closest Competing Papers (Ranked by Threat Level)

#### 1. CORAL (Feb 2026) -- HIGH RELEVANCE
- **Paper:** "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering" ([arXiv:2602.06022](https://arxiv.org/abs/2602.06022))
- **What it does:** Trains a regularized MLP probe on frozen residual-stream activations to predict correctness, then uses this for inference-time steering. Shows transferability across benchmarks (ARC-Challenge, HellaSwag, etc.) with ~14% accuracy and ~49% ECE improvements.
- **How it differs:** CORAL demonstrates transfer across *tasks/benchmarks* (English-to-English), NOT across *languages*. The paper does not appear to evaluate multilingual transfer. Their probe is an MLP (not strictly a linear direction), and they optimize for Brier score rather than extracting a simple linear calibration direction.
- **Threat assessment:** If the CORAL authors extend their work to multilingual settings in a follow-up, it would directly compete. But as of now, the cross-lingual angle is untouched.

#### 2. Beyond the Final Layer (Oct 2025) -- HIGH RELEVANCE
- **Paper:** "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" ([arXiv:2510.03136](https://arxiv.org/abs/2510.03136))
- **What it does:** Systematic study of multilingual calibration across 6 model families and 100+ languages. Discovers that late-intermediate layers provide better multilingual calibration signals than the final layer. Introduces LACE (Language-Aware Confidence Ensemble) which adaptively selects layer ensembles per language.
- **How it differs:** This paper uses the model's own confidence (logit-based) at different layers rather than a *learned calibration probe/direction*. It does NOT train a linear probe on English and transfer it to other languages. It is a training-free method based on layer selection, not on transferring a learned representation.
- **Threat assessment:** This paper establishes the empirical foundation that your idea relies on (intermediate layers are more language-agnostic for calibration). It is highly complementary but does not do the probe-transfer step. You should cite this paper prominently.

#### 3. The Confidence Manifold (Feb 2026) -- MEDIUM-HIGH RELEVANCE
- **Paper:** "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" ([arXiv:2602.08159](https://arxiv.org/abs/2602.08159))
- **What it does:** Shows that correctness signals in LLM activations are geometrically simple (3-8 dimensions, linear separation sufficient). A centroid-distance approach with just 25 labeled examples matches full probe performance (0.90 AUC). Validates causally via activation steering.
- **How it differs:** This paper characterizes the *geometry* of correctness representations across model architectures but does NOT examine cross-lingual transfer. All experiments appear to be English-only. The paper establishes that the calibration direction is simple and low-dimensional (which supports your hypothesis that it might transfer), but never tests it.
- **Threat assessment:** Provides theoretical motivation for why your approach should work. If the authors extend to multilingual settings, this becomes direct competition.

#### 4. Improving Multilingual LLMs via Representation Steering (May 2025) -- MEDIUM RELEVANCE
- **Paper:** "Improving Multilingual Language Models by Aligning Representations through Steering" ([arXiv:2505.12584](https://arxiv.org/abs/2505.12584))
- **What it does:** Trains a steering vector that shifts non-English hidden states closer to English equivalents at a single layer. Shows a single vector can be shared across structurally similar languages (zero-shot cross-linguistic transfer).
- **How it differs:** This paper steers *language representations* toward English for task performance, NOT for calibration/confidence. The steering direction captures language alignment, not correctness/calibration. The goal is to improve task accuracy in non-English languages, not to transfer a calibration signal.
- **Threat assessment:** Demonstrates the mechanism you would use (steering vectors transfer across languages at intermediate layers) but for a completely different purpose. Important related work but not a direct competitor.

#### 5. CLaS-Bench (Jan 2026) -- MEDIUM RELEVANCE
- **Paper:** "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark" ([arXiv:2601.08331](https://arxiv.org/abs/2601.08331))
- **What it does:** Benchmark for evaluating language-forcing behavior across 32 languages. Evaluates probe-derived directions, DiffMean, PCA/LDA vectors, SAE vectors for steering language output.
- **How it differs:** Focuses on *language identity* steering (forcing output language), not on *calibration* or *correctness* probes. The probe directions tested are for language control, not for confidence estimation.
- **Threat assessment:** Provides infrastructure and methodology for evaluating cross-lingual steering, but the calibration/correctness angle is absent.

#### 6. Cross-Lingual Activation Steering (Jan 2026) -- MEDIUM RELEVANCE
- **Paper:** "Cross-Lingual Activation Steering for Multilingual Language Models" ([arXiv:2601.16390](https://arxiv.org/abs/2601.16390))
- **What it does:** Training-free inference-time neuron modulation for improving non-dominant language performance, with 2.3% accuracy and 3.4% F1 improvements.
- **How it differs:** Steers for *task performance*, not for *calibration*. The activation modifications target language-specific neurons, not a calibration/correctness direction.

#### 7. Middle-Layer Representation Alignment (Feb 2025, ACL 2025) -- MEDIUM RELEVANCE
- **Paper:** "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" ([arXiv:2502.14830](https://arxiv.org/abs/2502.14830))
- **What it does:** Shows middle layers have strongest cross-lingual alignment potential. Proposes alignment objective during fine-tuning.
- **How it differs:** Focuses on task transfer via alignment training, not on transferring a calibration probe. Requires training-time intervention.

#### 8. Multilingual Calibration Effects of Instruction-Tuning (Jan 2026) -- LOW-MEDIUM RELEVANCE
- **Paper:** "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning" ([arXiv:2601.01362](https://arxiv.org/abs/2601.01362))
- **What it does:** Shows instruction-tuning on English increases confidence in low-resource languages without corresponding accuracy gains, causing miscalibration. Proposes label smoothing as a fix.
- **How it differs:** Studies calibration as a *side effect* of training, addresses it via training-time interventions (label smoothing), not via representation-space probes.

---

### Papers That Combine Calibration Probes WITH Multilingual Alignment

**None found.** This is the specific gap your work would fill. The literature cleanly separates into two clusters:

- **Cluster A: Calibration via internal representations** (CORAL, Confidence Manifold, "Geometry of Truth") -- all English-only or English-centric, never tested cross-lingually.
- **Cluster B: Cross-lingual representation transfer** (steering vectors, middle-layer alignment, CLaS-Bench, CLAS) -- all focused on task performance or language identity, never on calibration/correctness.

Your proposed work sits precisely at the intersection.

---

### Key Risk Factors

1. **The CORAL team** is the biggest threat. They already have transferable correctness probes; extending to multilingual evaluation is a natural next step. Their Feb 2026 paper is recent.

2. **The "Beyond the Final Layer" team** (Cambridge) already has the multilingual calibration infrastructure and the insight about intermediate layers. If they combine this with learned probes instead of logit-based methods, they arrive at your idea.

3. **The "Confidence Manifold" authors** have shown the geometric simplicity of the correctness signal. Testing cross-lingual invariance of this geometry is an obvious extension.

4. The **representation steering for multilingual LLMs** community (Mahmoud et al., Pokharel et al.) is growing rapidly in early 2026. The machinery for cross-lingual vector transfer is becoming standardized.

---

### Conclusion

The idea appears **novel as of May 2026**, but the novelty window is closing. The individual components (correctness probes in representation space, cross-lingual transfer of steering vectors, intermediate-layer language-agnostic representations for calibration) all exist separately in published work. Nobody has combined them into "train a linear calibration probe on English intermediate-layer activations, apply it zero-shot to non-English languages." This is a clear contribution, but given how close CORAL, Confidence Manifold, and Beyond the Final Layer are converging, executing quickly is advisable.

---

### Sources

- [CORAL: Correctness-Optimized Residual Activation Lens](https://arxiv.org/abs/2602.06022)
- [Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration](https://arxiv.org/abs/2510.03136)
- [The Confidence Manifold: Geometric Structure of Correctness Representations](https://arxiv.org/abs/2602.08159)
- [Improving Multilingual Language Models by Aligning Representations through Steering](https://arxiv.org/abs/2505.12584)
- [CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark](https://arxiv.org/abs/2601.08331)
- [Cross-Lingual Activation Steering for Multilingual Language Models](https://arxiv.org/abs/2601.16390)
- [Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs](https://arxiv.org/abs/2502.14830)
- [Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning](https://arxiv.org/abs/2601.01362)
- [On the Calibration of Multilingual Question Answering LLMs](https://arxiv.org/abs/2311.08669)
- [Calibrating Zero-shot Cross-lingual (Un-)structured Predictions](https://aclanthology.org/2022.emnlp-main.170.pdf)
- [Probing the Emergence of Cross-lingual Alignment during LLM Training](https://arxiv.org/abs/2406.13229)
- [Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation](https://arxiv.org/abs/2512.22245)
- [Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment](https://arxiv.org/abs/2502.15639)
- [Representation Engineering for Large-Language Models: Survey](https://arxiv.org/abs/2502.17601)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44be7e7e-eada-4268-99ca-901aae7bce51",
  "isSidechain": true,
  "agentId": "a32b0b74a917828b8",
  "requestId": "req_011CbCQ3mCpsjVmk5pnFji8h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e7de0d8-1111-4be1-86b6-bfd249ecf175",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9GSUBPAcSg54aRCzVqJ2t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 22768,
      "output_tokens": 2893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1568
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2893,
          "cache_read_input_tokens": 22768,
          "cache_creation_input_tokens": 1568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1568,
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
