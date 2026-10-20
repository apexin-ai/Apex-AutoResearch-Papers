# Research conversation: I need to find the current best open-source models for theorem proving / formal math as of May 2026. Search the web for:

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0dbd6ab64543c9a6.jsonl`
- **Structured JSON:** [`03cc60c9c73b9a7bbd8c.json`](../../sessions/03/03cc60c9c73b9a7bbd8c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-28T06:15:06.419Z_

I need to find the current best open-source models for theorem proving / formal math as of May 2026. Search the web for:

1. Web search: "best open source LLM theorem proving Lean 2026"
2. Web search: "DeepSeek Prover V2 2026" 
3. Web search: "InternLM Math formal theorem proving 2026"
4. Web search: "Llama 4 math reasoning 2026"
5. Web search: "Qwen 3 math theorem proving 2026"
6. Web search: "open source model Lean 4 proof generation 2026"
7. Web search: "best open source code model 2026 formal math"
8. Web search: "DeepSeek V3 math 2026"

For each model found, report:
- Model name and version
- Parameter count
- Performance on math/theorem proving benchmarks if available
- Whether it's open-source/open-weights
- Release date

I need to know what the current top-performing open-source model is that could serve as a base for fine-tuning a decomposition policy for theorem proving.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "e20212ca-c247-4a59-b983-f1c25273e84f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T06:15:06.423Z_

```json
{
  "parentUuid": "e20212ca-c247-4a59-b983-f1c25273e84f",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
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
  "uuid": "a1e96849-bf52-4039-8b67-8778f3d838ea",
  "timestamp": "2026-05-28T06:15:06.423Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T06:15:06.429Z_

```json
{
  "parentUuid": "a1e96849-bf52-4039-8b67-8778f3d838ea",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "83b7f1f1-a868-48b5-ade6-3e31d05d7a91",
  "timestamp": "2026-05-28T06:15:06.429Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T06:15:08.872Z_



I'll search for all of these topics in parallel to gather comprehensive information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83b7f1f1-a868-48b5-ade6-3e31d05d7a91",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUZokEcmL9UdJh3K7qH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e56c5d9-b6b0-40f9-8781-ef0352b19350",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfHCY1CFHWEGi4HrPDh9ko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1576,
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

_source line 5 · 2026-05-28T06:15:09.357Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V5VCnm1HSg8VtWm84VLpDi`</summary>

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
  "parentUuid": "4e56c5d9-b6b0-40f9-8781-ef0352b19350",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUZokEcmL9UdJh3K7qH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf877fae-cf5e-4ef5-b992-e4865aca85c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfHCY1CFHWEGi4HrPDh9ko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 7411,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1576,
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

_source line 6 · 2026-05-28T06:15:09.359Z_

<details><summary>↩ Tool result · `toolu_01V5VCnm1HSg8VtWm84VLpDi`</summary>

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
  "parentUuid": "bf877fae-cf5e-4ef5-b992-e4865aca85c1",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "c8b70c6d-f188-435e-9168-ed978001b053",
  "sourceToolAssistantUUID": "bf877fae-cf5e-4ef5-b992-e4865aca85c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T06:15:11.432Z_



Now I'll run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8b70c6d-f188-435e-9168-ed978001b053",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d217769-a678-4f61-8cd7-938ad935a0eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 8 · 2026-05-28T06:15:11.979Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FNGdDVLyXJs1kapZSgt62q`</summary>

```json
{
  "query": "best open source LLM theorem proving Lean 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d217769-a678-4f61-8cd7-938ad935a0eb",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7193594-d897-4e66-af30-fe68d73813e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 9 · 2026-05-28T06:15:12.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SSbY6x2tecZvAk3h6JrSGK`</summary>

```json
{
  "query": "DeepSeek Prover V2 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7193594-d897-4e66-af30-fe68d73813e4",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84e6e95e-ac2e-44b6-81b9-377ad3a098ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 10 · 2026-05-28T06:15:12.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTZ1GurSkNyWmmP6dBPv6u`</summary>

```json
{
  "query": "InternLM Math formal theorem proving 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e6e95e-ac2e-44b6-81b9-377ad3a098ce",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a71673b1-e1cb-4b59-9cd6-20fdb8cf4a93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 11 · 2026-05-28T06:15:12.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019iTcnhQXFyZWwcYRr5iNuA`</summary>

```json
{
  "query": "Llama 4 math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a71673b1-e1cb-4b59-9cd6-20fdb8cf4a93",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "980900f5-55f2-42fb-84f9-ef3736df3c5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 12 · 2026-05-28T06:15:13.378Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GrGokjA6sLkoCrfxG9CfKx`</summary>

```json
{
  "query": "Qwen 3 math theorem proving 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "980900f5-55f2-42fb-84f9-ef3736df3c5f",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02bbf536-0135-4b54-b8f7-966ebb8fbe1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 13 · 2026-05-28T06:15:14.007Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xzf5cBg1N695rJQvDYeeu4`</summary>

```json
{
  "query": "open source model Lean 4 proof generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02bbf536-0135-4b54-b8f7-966ebb8fbe1a",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eb35f45-1afc-4b46-a4cf-b28480d1268e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
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

_source line 14 · 2026-05-28T06:15:14.269Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M81ypgMUoKnyf1jHappYb9`</summary>

```json
{
  "query": "best open source code model 2026 formal math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb35f45-1afc-4b46-a4cf-b28480d1268e",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db767d36-5693-49f9-afc6-8db455079d7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
      "output_tokens": 397,
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
          "output_tokens": 397,
          "cache_read_input_tokens": 8987,
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

_source line 15 · 2026-05-28T06:15:14.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012MamNBU5Dom8wpTfMX9Hhv`</summary>

```json
{
  "query": "DeepSeek V3 math 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db767d36-5693-49f9-afc6-8db455079d7c",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUa2Sy4JEtUki4oYUcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd96613a-52a4-4b17-a11c-34e33faacbea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zpUw8AyNNqzDYCGzmepUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 8987,
      "output_tokens": 397,
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
          "output_tokens": 397,
          "cache_read_input_tokens": 8987,
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

_source line 16 · 2026-05-28T06:15:19.853Z_

<details><summary>↩ Tool result · `toolu_01FNGdDVLyXJs1kapZSgt62q`</summary>

```text
Web search results for query: "best open source LLM theorem proving Lean 2026"

Links: [{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning | OpenReview","url":"https://openreview.net/forum?id=fxDCgOruk0"},{"title":"[2306.15626] LeanDojo: Theorem Proving with Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2306.15626"},{"title":"Goedel-Prover: A Frontier Model for Open-Source Automated Theorem   Proving","url":"https://arxiv.org/pdf/2502.07640"},{"title":"Lean Copilot: Large Language Models as Copilots for Theorem Proving in Lean","url":"https://arxiv.org/pdf/2404.12534"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"DeepSeek Launches Prover-V2 Open-Source LLM for Formal Math Proofs - InfoQ","url":"https://www.infoq.com/news/2025/05/deepseek-prover-v2-formal-proof/"},{"title":"[2404.12534] Lean Copilot: Large Language Models as Copilots for Theorem Proving in Lean","url":"https://arxiv.org/abs/2404.12534"},{"title":"AI-Driven Formal Theorem Proving in the Lean Ecosystem","url":"https://leandojo.org/"}]

Based on the search results, here are the best open-source LLM approaches for theorem proving in Lean as of 2026:

## Top Open-Source Models for Lean Theorem Proving

**Goedel-Prover** - The final prover outperforms all existing open-source models in whole-proof generation. On the miniF2F benchmark, it achieves a 57.6% success rate (Pass@32), exceeding the previous best open-source model by 7.6%. On PutnamBench, Goedel-Prover successfully solves 7 problems (Pass@512), ranking first on the leaderboard.

**APOLLO** - On the miniF2F benchmark, we establish a new state‑of‑the‑art accuracy of 84.9% among sub 8B‑parameter models (as of August 2025) while keeping the sampling budget below one hundred. This is particularly notable for smaller models.

**DeepSeek-Prover-V2** - DeepSeek has released DeepSeek-Prover-V2, a new open-source large language model specifically designed for formal theorem proving in Lean 4. The model builds on a recursive theorem proving pipeline powered by the company's DeepSeek-V3 foundation model.

**Lean Copilot** - When automating the theorem proving process, Lean Copilot automates 74.2% proof steps on average, 85% better than aesop (40.1%).

For theorem proving, complex code debugging, scientific analysis, general-purpose models like Qwen 3 235B or DeepSeek R1 are also recommended for their reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7193594-d897-4e66-af30-fe68d73813e4",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "0d38fccd-a3ba-4157-9389-f2aaef4a25b2",
  "sourceToolAssistantUUID": "e7193594-d897-4e66-af30-fe68d73813e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T06:15:19.874Z_

<details><summary>↩ Tool result · `toolu_01SSbY6x2tecZvAk3h6JrSGK`</summary>

```text
Web search results for query: "DeepSeek Prover V2 2026"

Links: [{"title":"DeepSeek Prover V2 - Specs & Pricing [2026]","url":"https://getdeploying.com/llms/deepseek-prover-v2"},{"title":"Run DeepSeek-Prover-V2 7B on Linux: Complete Setup Guide","url":"https://codersera.com/blog/running-deepseek-prover-v2-7b-on-linux-a-complete-guide/"},{"title":"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/pdf/2504.21801"},{"title":"[2504.21801] DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/abs/2504.21801"},{"title":"DeepSeek Prover V2 download | SourceForge.net","url":"https://sourceforge.net/projects/deepseek-prover-v2.mirror/"},{"title":"DeepSeek Prover V2 - API, Providers, Stats | OpenRouter","url":"https://openrouter.ai/deepseek/deepseek-prover-v2:free"}]

Based on the search results, here's what I found about DeepSeek Prover V2 2026:

## Overview

DeepSeek Prover V2 is a family of language models released by DeepSeek AI on April 30, 2025, specialized for formal mathematical reasoning in Lean 4.

## Model Sizes and Architecture

It comes in two sizes: 7B (built on DeepSeek-Prover-V1.5-Base, 32K context) and 671B (built on DeepSeek-V3-Base). The 671B model is a MoE model with 37B active parameters across 256 experts.

## Performance

DeepSeek-Prover-V2-671B achieves state-of-the-art performance in neural theorem proving, reaching 88.9% pass ratio on the MiniF2F-test and solving 49 out of 658 problems from PutnamBench.

## Training and Capabilities

The cold-start training procedure begins by prompting DeepSeek-V3 to decompose complex problems into a series of subgoals, and the proofs of resolved subgoals are synthesized into a chain-of-thought process combined with DeepSeek-V3's step-by-step reasoning for reinforcement learning. Unlike general-purpose LLMs that can describe proofs informally, Prover V2 generates syntactically valid Lean 4 proof terms that can be checked by the Lean 4 kernel.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84e6e95e-ac2e-44b6-81b9-377ad3a098ce",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "19ad7af4-d047-486f-9322-ce265c532bf2",
  "sourceToolAssistantUUID": "84e6e95e-ac2e-44b6-81b9-377ad3a098ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T06:15:20.403Z_

<details><summary>↩ Tool result · `toolu_019iTcnhQXFyZWwcYRr5iNuA`</summary>

```text
Web search results for query: "Llama 4 math reasoning 2026"

Links: [{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Gemma 4 vs. Llama 4: Which “Open” Model Actually Wins in 2026? - MyNextDeveloper","url":"https://mynextdeveloper.com/blogs/gemma-4-vs-llama-4-which-open-model-actually-wins-in-2026/"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Meta Llama 4 Scout and Maverick Production Guide | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai","url":"https://explore.n1n.ai/blog/meta-llama-4-scout-maverick-production-guide-2026-04-27"},{"title":"Best Ollama Models 2026: 15 Ranked (Coding, Reasoning, Chat) | Local AI Master","url":"https://localaimaster.com/blog/best-ollama-models"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"Gemma 4 vs Qwen 3.5 vs Llama 4: Which Open Model Should You Actually Use? (2026) - Botmonster Tech","url":"https://botmonster.com/posts/gemma-4-vs-qwen-3-5-vs-llama-4-open-model-comparison-2026/"},{"title":"Llama 4: Meta's New AI Model - Evolution, Features, and Comparison&lt;!-- --> | GPT-trainer Blog","url":"https://gpt-trainer.com/blog/llama+4+evolution+features+comparison"},{"title":"Unmatched Performance and Efficiency | Llama 4","url":"https://www.llama.com/models/llama-4/"},{"title":"Best Math LLMs (2026): Equations, Proofs, Reasoning | Alignify","url":"https://alignify.co/tools/llm-for-math"}]

Based on the search results, here's what I found about Llama 4 and math reasoning in 2026:

## Llama 4 Math Reasoning Performance

Meta revamped Llama 4's post-training with lightweight supervised fine-tuning, online reinforcement learning, and direct preference optimization, recognizing that balancing these approaches was key to improving performance in reasoning, coding, and math domains.

Meta found that dynamically filtering prompts and constructing training batches with mixed capabilities provided performance improvements on math, reasoning, and coding.

### Model Performance

Llama 4 Maverick (17 billion active parameters) achieves comparable results to DeepSeek v3 on reasoning and coding. However, a gap remains in pure STEM and math reasoning, where OpenAI's o-series maintains a lead, with Maverick scoring 61.2 on the MATH benchmark compared to o1/o3 models.

### Comparison with Other Open Models

When compared to other open models in 2026, on AIME 2026 (a hard math reasoning test), Gemma 4 scores 89.2% against Llama 4 Scout's 88.3%. If applications require heavy mathematical reasoning, Meta suggests using a hybrid approach with Claude 3.5 Sonnet or OpenAI o3 for specific modules until Llama 4 Behemoth is released in late 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "980900f5-55f2-42fb-84f9-ef3736df3c5f",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "f668391b-9397-4c9a-9910-657b8ebd6d0c",
  "sourceToolAssistantUUID": "980900f5-55f2-42fb-84f9-ef3736df3c5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T06:15:20.723Z_

<details><summary>↩ Tool result · `toolu_01Xzf5cBg1N695rJQvDYeeu4`</summary>

```text
Web search results for query: "open source model Lean 4 proof generation 2026"

Links: [{"title":"Chats-llm","url":"https://chats-llm.com/en/blog/leanstral-release"},{"title":"Leanstral: Mistral’s Open-Source Proof Agent for Lean 4","url":"https://rits.shanghai.nyu.edu/ai/leanstral-mistrals-open-source-proof-agent-for-lean-4/"},{"title":"Leanstral: Mistral's Open-Source AI for Trustworthy Coding - Webkul Blog","url":"https://webkul.com/blog/mistrals-leanstral/"},{"title":"Leanstral: Mistral AI's Open-Source Agent for Formal Proofs | AIToolly","url":"https://aitoolly.com/ai-news/article/2026-03-17-leanstral-mistral-ais-open-source-agent-for-trustworthy-coding-and-formal-proof-engineering"},{"title":"Leanstral Review: Mistral Just Shipped the AI That Proves Your Code Is Correct | SaaS Pilot — AI & SaaS Tool Reviews","url":"https://saaspilot.org/ai-coding-assistants/2026-03-20-radar-2-leanstral-review/"},{"title":"Mistral AI Launches Leanstral Open-Source Proof Agent for Lean 4 | MEXC News","url":"https://www.mexc.com/news/941903"},{"title":"Leanstral: the open-source agent for formal code proofs - Viral Methods","url":"https://metodoviral.com/en/news/leanstral-the-open-source-agent-for-formal-code-proofs/"},{"title":"Leanstral Reviews in 2026","url":"https://sourceforge.net/software/product/Leanstral/"},{"title":"Goedel-Prover: Open-Source ATP in Lean 4","url":"https://www.emergentmind.com/topics/goedel-prover"}]

Here are the key findings about open source models for Lean 4 proof generation in 2026:

## Leanstral

Mistral AI introduced Leanstral, the first open-source code agent for Lean 4 formal proof engineering, outperforming Claude Sonnet 4.6 at 15x lower cost. On March 16, 2026, Mistral AI released Leanstral — the first open-source AI agent purpose-built for Lean 4, the formal proof assistant used across mathematical research and verified software development.

**Technical Details:**
With 120 billion total parameters but only 6 billion active per token, Leanstral can formally prove that AI-generated code meets its specifications. The model is released under the Apache 2.0 license.

**Capabilities:**
Leanstral is purpose-built to generate machine-checkable proofs alongside executable code. The model translated Rocq (formerly Coq) definitions into Lean and proved properties about imperative programs, including implementing custom notation and generating theorem proofs from specification statements alone.

**Deployment Options:**
Released under an Apache 2.0 license, Leanstral is accessible via a free API endpoint and Mistral vibe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eb35f45-1afc-4b46-a4cf-b28480d1268e",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "7e6c7125-b0e7-41be-bafc-00e019022df7",
  "sourceToolAssistantUUID": "2eb35f45-1afc-4b46-a4cf-b28480d1268e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T06:15:20.838Z_

<details><summary>↩ Tool result · `toolu_01GrGokjA6sLkoCrfxG9CfKx`</summary>

```text
Web search results for query: "Qwen 3 math theorem proving 2026"

Links: [{"title":"Top 9 Large Language Models as of March 2026 | Shakudo","url":"https://www.shakudo.io/blog/top-9-large-language-models"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Qwen/Qwen3-32B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-32B"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"qwen3","url":"https://ollama.com/library/qwen3"},{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Aristotle: IMO-level Automated Theorem Proving","url":"https://arxiv.org/pdf/2510.01346"}]

Based on the search results, here's what I found about Qwen 3 and math/theorem proving capabilities in 2026:

## Qwen3 Overview

Qwen3 is the latest generation of large language models in the Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models.

## Math and Reasoning Capabilities

Qwen3 uniquely supports seamless switching between thinking mode (for complex logical reasoning, math, and coding) and non-thinking mode (for efficient, general-purpose dialogue) within a single model. It shows significant enhancement in reasoning capabilities, surpassing previous QwQ and Qwen2.5 instruct models on mathematics, code generation, and commonsense logical reasoning.

## Performance on Math Benchmarks

Qwen now supports 119 languages and achieves 92.3% accuracy on AIME25. Additionally, the flagship model, Qwen3-235B-A22B, achieves competitive results in benchmark evaluations of coding, math, and general capabilities when compared to other top-tier models such as DeepSeek-R1, o1, o3-mini, Grok-3, and Gemini-2.5-Pro.

## Automated Theorem Proving

While the search results don't show specific Qwen3 theorem proving capabilities, they do mention that DeepSeek released the DeepSeek-Prover-V2, an open-source model tailored for formal theorem proving in Lean 4. The broader AI landscape in 2026 shows significant advances in automated theorem proving across multiple models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02bbf536-0135-4b54-b8f7-966ebb8fbe1a",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "da7091f6-07e7-45e4-8708-f94505d374b8",
  "sourceToolAssistantUUID": "02bbf536-0135-4b54-b8f7-966ebb8fbe1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T06:15:21.410Z_

<details><summary>↩ Tool result · `toolu_01GTZ1GurSkNyWmmP6dBPv6u`</summary>

```text
Web search results for query: "InternLM Math formal theorem proving 2026"

Links: [{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"InternLM2.5-StepProver: Advancing Automated Theorem Proving via Critic-Guided Search","url":"https://arxiv.org/pdf/2410.15700"},{"title":"GitHub - InternLM/InternLM-Math: State-of-the-art bilingual open-sourced Math reasoning LLMs. · GitHub","url":"https://github.com/InternLM/InternLM-Math"},{"title":"InternLM-Math: Open Math Large Language Models ...","url":"https://www.emergentmind.com/papers/2402.06332"},{"title":"internlm/internlm2-math-plus-1_8b · Hugging Face","url":"https://huggingface.co/internlm/internlm2-math-plus-1_8b"},{"title":"Advancing Mathematics Research with AI-Driven Formal Proof Search","url":"https://arxiv.org/html/2605.22763v1"},{"title":"LLM-Based Theorem Provers","url":"https://www.emergentmind.com/topics/llm-based-theorem-provers"}]

I found several relevant results about InternLM's work in formal theorem proving. Here's what the search revealed:

## InternLM Math and Formal Theorem Proving

InternLM has developed tools for mathematical theorem proving, particularly utilizing formal languages such as LEAN. The project has released several models and datasets:

**Recent Achievements (2024):**
InternLM2.5-StepProver achieves open-source state-of-the-art on multiple benchmarks, including 65.9% pass rate on MiniF2F-test and proving 17.0% of problems in Lean-Workbook-Plus.

**Key Components:**
InternLM-Math integrates formal reasoning through the use of the LEAN theorem prover, enabling it to tackle formal mathematical statements and bridge the gap between informal natural language reasoning and formal mathematical verification.

**Released Resources:**
InternLM has open-sourced their models and searched proofs on GitHub and Hugging Face, including Lean-Workbook with 57K math problems formalized in Lean 4.

**Methodology:**
The major learning paradigm uses expert iteration, where LLMs attempt to prove problems within a dataset and iteratively refine their capabilities through self-training on discovered proofs.

The search results show active development in this area, with the 2026 AI for Math Workshop at ICML specifically highlighting formal theorem proving as a key research theme.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a71673b1-e1cb-4b59-9cd6-20fdb8cf4a93",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "c15b3d80-2210-4baf-b70f-0b1a51057cda",
  "sourceToolAssistantUUID": "a71673b1-e1cb-4b59-9cd6-20fdb8cf4a93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T06:15:22.709Z_

<details><summary>↩ Tool result · `toolu_01M81ypgMUoKnyf1jHappYb9`</summary>

```text
Web search results for query: "best open source code model 2026 formal math"

Links: [{"title":"Best Open Source LLM For Math In 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math"},{"title":"Best Open Source LLMs in 2026: 6 Worth Deploying in Production | Respan","url":"https://www.respan.ai/blog/best-open-source-llms"},{"title":"Best Open-Source & Open-Weight Coding Models (2026)","url":"https://kilo.ai/open-source-models"},{"title":"The Best Open Source LLMs for Coding in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-coding"},{"title":"Best Open Source Models for Coding in 2026 – Free & Powerful","url":"https://www.indianprompt.com/best-open-source-models-for-coding-2026/"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"}]

Based on the search results, here are the best open-source code models in 2026 for formal math and coding:

## Top Recommendations for Formal Math

The top three open-source models for mathematical reasoning in 2026 are DeepSeek-R1 (offering o1-level reasoning), Qwen/QwQ-32B (providing balanced excellence), and THUDM/GLM-Z1-9B-0414 (a lightweight champion).

DeepSeek-R1 offers elite-level performance comparable to OpenAI-o1, QwQ-32B provides the best balance of capability and efficiency, while GLM-Z1-9B-0414 delivers surprising mathematical prowess in a lightweight package.

## Top Recommendations for Coding

The best open-source coding models in 2026 are GLM-5.1, Kimi K2.6, DeepSeek V4-Pro, and Qwen3-Coder-Next for agentic work; MiniMax M2.5 for free hosted use; and Devstral Small 2 or Qwen3.6-27B for local development.

GLM-5.1 is the strongest all-around open-source coding model for long-horizon agentic engineering, with Kimi K2.6 leading on SWE-Bench Pro, DeepSeek V4-Pro leading on LiveCodeBench and 1M-context tasks, and Qwen3-Coder-Next offering the best efficiency per active parameter.

## Additional Notable Models

DeepSeek V3 has achieved scores surpassing GPT-4.5 on evaluation sets related to mathematics and coding.

On the May 12, 2026 LiveBench snapshot, Kimi K2.6 Thinking leads the open-source models with 78.57 Coding Avg and 58.33 Agentic Coding Avg.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db767d36-5693-49f9-afc6-8db455079d7c",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "4c89160a-78ba-4621-8496-6bc8d4fbaec4",
  "sourceToolAssistantUUID": "db767d36-5693-49f9-afc6-8db455079d7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T06:15:23.058Z_

<details><summary>↩ Tool result · `toolu_012MamNBU5Dom8wpTfMX9Hhv`</summary>

```text
Web search results for query: "DeepSeek V3 math 2026"

Links: [{"title":"DeepSeek","url":"https://www.deepseek.com/en/"},{"title":"DeepSeek-V3 Technical Report DeepSeek-AI research@deepseek.com Abstract","url":"https://arxiv.org/pdf/2412.19437"},{"title":"Change Log | DeepSeek API Docs","url":"https://api-docs.deepseek.com/updates"},{"title":"DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models","url":"https://arxiv.org/pdf/2512.02556"},{"title":"DeepSeek-V3 Technical Report","url":"https://arxiv.org/html/2412.19437v1"},{"title":"A Technical Tour of the DeepSeek Models from V3 to V3.2","url":"https://magazine.sebastianraschka.com/p/technical-deepseek"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"Evaluating Mathematical Reasoning Across Large Language Models: A Fine-Grained Approach","url":"https://arxiv.org/pdf/2503.10573"}]

Based on the search results, here's what I found about DeepSeek V3 and its mathematical capabilities:

## DeepSeek V3 Mathematical Performance

DeepSeek-V3 achieves state-of-the-art performance on math-related benchmarks among all non-long-CoT open-source and closed-source models, even outperforming o1-preview on specific benchmarks such as MATH-500.

Compared with DeepSeek-V2, DeepSeek-V3 optimized the pre-training corpus by enhancing the ratio of mathematical and programming samples, while expanding multilingual coverage.

## Model Architecture and Training

V3 is an open-source model with 671B total parameters, activating only 37B per query, excelling in complex reasoning tasks while minimizing resource demands.

## More Recent Developments (2025-2026)

The search results also show more recent versions have been developed. DeepSeek-V3.2-Speciale surpasses GPT-5 and exhibits reasoning proficiency on par with Gemini-3.0-Pro, achieving gold-medal performance in both the 2025 International Mathematical Olympiad (IMO) and the International Olympiad in Informatics (IOI).

Additionally, DeepSeekMath V2 was released on November 27, 2025, based on DeepSeek V3.2-Exp-Base.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd96613a-52a4-4b17-a11c-34e33faacbea",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "2c64948f-f39d-4cff-a764-cd483075333b",
  "sourceToolAssistantUUID": "fd96613a-52a4-4b17-a11c-34e33faacbea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T06:15:26.534Z_

Let me get a few more targeted searches to fill in gaps on specific models mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c64948f-f39d-4cff-a764-cd483075333b",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUb2h8dxv2FKSTsHELN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d96673fc-e1ee-43b7-b067-8ffe38198516",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xs3dGV8iva2hpzkpsWym4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6856,
      "cache_read_input_tokens": 9609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6856,
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

_source line 25 · 2026-05-28T06:15:27.698Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015XEbeL6v2MwzicJDnuK1JW`</summary>

```json
{
  "query": "Leanstral Mistral parameters benchmark performance miniF2F 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d96673fc-e1ee-43b7-b067-8ffe38198516",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUb2h8dxv2FKSTsHELN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32b90a7a-fe65-41d7-8e6f-a6e07b3da834",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xs3dGV8iva2hpzkpsWym4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6856,
      "cache_read_input_tokens": 9609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6856,
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

_source line 26 · 2026-05-28T06:15:28.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SPCiztz9a236AEcdFRiDTM`</summary>

```json
{
  "query": "Goedel-Prover model parameters benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32b90a7a-fe65-41d7-8e6f-a6e07b3da834",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUb2h8dxv2FKSTsHELN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98bb4e7a-be7d-4258-8014-35d463c9611d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xs3dGV8iva2hpzkpsWym4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6856,
      "cache_read_input_tokens": 9609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6856,
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

_source line 27 · 2026-05-28T06:15:28.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FQ221LZfnmZByA6Y6ma4s1`</summary>

```json
{
  "query": "APOLLO theorem proving miniF2F benchmark model size 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98bb4e7a-be7d-4258-8014-35d463c9611d",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUb2h8dxv2FKSTsHELN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b99062f-05e4-4b71-9163-9b18e978f5b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xs3dGV8iva2hpzkpsWym4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6856,
      "cache_read_input_tokens": 9609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6856,
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

_source line 28 · 2026-05-28T06:15:30.054Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RC2jfB7ret23MJVn54zYg7`</summary>

```json
{
  "query": "DeepSeek Prover V2 7B 671B miniF2F PutnamBench results fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b99062f-05e4-4b71-9163-9b18e978f5b2",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUb2h8dxv2FKSTsHELN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f180421a-eb4d-4991-8fa7-316d378b94c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xs3dGV8iva2hpzkpsWym4V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6856,
      "cache_read_input_tokens": 9609,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6856
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 9609,
          "cache_creation_input_tokens": 6856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6856,
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

_source line 29 · 2026-05-28T06:15:35.225Z_

<details><summary>↩ Tool result · `toolu_01SPCiztz9a236AEcdFRiDTM`</summary>

```text
Web search results for query: "Goedel-Prover model parameters benchmark 2025 2026"

Links: [{"title":"Goedel-Prover-V2: Advances in Formal Theorem Proving","url":"https://www.emergentmind.com/topics/goedel-prover-v2"},{"title":"Goedel-Prover: A Frontier Model for Open-Source Automated Theorem   Proving","url":"https://arxiv.org/pdf/2502.07640"},{"title":"Goedel-Prover: Open-Source ATP in Lean 4","url":"https://www.emergentmind.com/topics/goedel-prover"},{"title":"Technical Report GOEDEL-PROVER-V2: SCALING FORMAL THEOREM","url":"https://arxiv.org/pdf/2508.03613"},{"title":"GitHub - Goedel-LM/Goedel-Prover · GitHub","url":"https://github.com/Goedel-LM/Goedel-Prover"},{"title":"Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification","url":"https://arxiv.org/pdf/2603.19329"},{"title":"Goedel-LM/Goedel-Prover-V2-32B · Hugging Face","url":"https://huggingface.co/Goedel-LM/Goedel-Prover-V2-32B"},{"title":"GitHub - Goedel-LM/Goedel-Prover-V2 · GitHub","url":"https://github.com/Goedel-LM/Goedel-Prover-V2"}]

Based on the search results, here's what I found about Goedel-Prover model parameters and benchmarks for 2025-2026:

## Model Parameters

Goedel-Prover-V2 comes in variants at 8B and 32B parameters. The 32B Goedel-Prover-V2 outperforms DeepSeek-Prover-V2-671B with only 1/20th of the parameter count and a greatly reduced compute budget.

## Benchmark Performance

**MiniF2F Benchmark:**
Goedel-Prover-V2-32B achieves 88.0% on MiniF2F at Pass@32 on standard mode and 90.4% on self-correction mode, outperforming prior SOTA DeepSeek-Prover-V2-671B and concurrent work Kimina-Prover-72B.

**PutnamBench:**
On PutnamBench, the Goedel-Prover-V2-32B solves 86 problems at pass@184; the closest competitor, DeepSeek-Prover-V2-671B, solves 47 at pass@1024.

## Additional Benchmarks

The Goedel-Prover-V2 models and new MathOlympiadBench benchmark are released, which comprises human-verified formalizations of Olympiad-level mathematical competition problems, containing 360 problems including 158 IMO problems from 1959 to 2024, 131 IMO shortlist problems covering 2006 to 2023, and 68 regional mathematical Olympiad problems.

Goedel-Prover-V2 is a series of LLMs and an open-source infrastructure that advance the state-of-the-art in automated formal theorem proving, particularly in Lean 4, by introducing scalable data synthesis, verifier-guided self-correction, and model averaging schemes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98bb4e7a-be7d-4258-8014-35d463c9611d",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "2a295fae-64e7-4e5f-8b51-9da3ca860118",
  "sourceToolAssistantUUID": "98bb4e7a-be7d-4258-8014-35d463c9611d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T06:15:36.976Z_

<details><summary>↩ Tool result · `toolu_01RC2jfB7ret23MJVn54zYg7`</summary>

```text
Web search results for query: "DeepSeek Prover V2 7B 671B miniF2F PutnamBench results fine-tuning"

Links: [{"title":"DeepSeek Unveils DeepSeek-Prover-V2: Advancing Neural Theorem Proving with Recursive Proof Search and a New Benchmark | Synced","url":"https://syncedreview.com/2025/04/30/deepseek-unveils-deepseek-prover-v2-advancing-neural-theorem-proving-with-recursive-proof-search-and-a-new-benchmark/"},{"title":"DeepSeek-Prover-V2: Open-Source AI for Lean 4 Formal Theorem Proving | by My Social | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/deepseek-prover-v2-open-source-ai-for-lean-4-formal-theorem-proving-ab7f9910576b"},{"title":"deepseek-ai/DeepSeek-Prover-V2-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-7B"},{"title":"deepseek-ai/DeepSeek-ProverBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/deepseek-ai/DeepSeek-ProverBench"},{"title":"deepseek-ai/DeepSeek-Prover-V2-671B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B"},{"title":"unsloth/DeepSeek-Prover-V2-671B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-Prover-V2-671B"},{"title":"[2504.21801] DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/abs/2504.21801"},{"title":"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/pdf/2504.21801"},{"title":"DeepSeek Prover V2 671B: Features, Benchmarks & Hosting Platforms Compared [2025]","url":"https://www.index.dev/blog/deepseek-prover-v2-features-benchmarks-use-cases"},{"title":"GitHub - deepseek-ai/DeepSeek-Prover-V2 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Prover-V2"}]

Based on the search results, here's what I found about DeepSeek Prover V2 results:

## Performance Results

**DeepSeek-Prover-V2-671B (Large Model):**
- Reached an impressive 88.9% pass ratio on the MiniF2F-test and successfully solved 49 out of 658 problems from PutnamBench
- On MiniF2F-test, it achieves 82.4% accuracy with Pass@32, improving to 88.9% with Pass@8192

**DeepSeek-Prover-V2-7B (Smaller Model):**
- The 7B model added 13 distinct solutions on PutnamBench (in addition to the problems solved by the larger model)
- The 7B variant demonstrated robust capability on the MiniF2F benchmark, outperforming all prior tested open-source provers

## Fine-tuning and Training Approach

DeepSeek-Prover-V2 uses a recursive theorem proving pipeline powered by DeepSeek-V3, where the cold-start training procedure begins by prompting DeepSeek-V3 to decompose complex problems into subgoals, and the proofs of resolved subgoals are synthesized into a chain-of-thought process combined with step-by-step reasoning to create an initial cold start for reinforcement learning.

After the initial training, DeepSeek-Prover V2 undergoes reinforcement learning where the model receives binary feedback—each proof is either correct or incorrect—which helps the model learn to align informal reasoning with Lean's strict proof-checking rules.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f180421a-eb4d-4991-8fa7-316d378b94c9",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "8c5f4e6f-0080-4963-82f3-7205023e961f",
  "sourceToolAssistantUUID": "f180421a-eb4d-4991-8fa7-316d378b94c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T06:15:37.808Z_

<details><summary>↩ Tool result · `toolu_015XEbeL6v2MwzicJDnuK1JW`</summary>

```text
Web search results for query: "Leanstral Mistral parameters benchmark performance miniF2F 2026"

Links: [{"title":"Leanstral Review: Mistral Just Shipped the AI That Proves Your Code Is Correct | SaaS Pilot — AI & SaaS Tool Reviews","url":"https://saaspilot.org/ai-coding-assistants/2026-03-20-radar-2-leanstral-review/"},{"title":"Leanstral Uses 6B Active Parameters to Beat Models 100x Its Size at Formal Proofs – Top AI Product","url":"https://topaiproduct.com/2026/03/16/leanstral-uses-6b-active-parameters-to-beat-models-100x-its-size-at-formal-proofs/"},{"title":"Leanstral by Mistral AI: The AI That Proves Your Code Is Correct","url":"https://emelia.io/hub/leanstral-mistral-ai-formal-verification"},{"title":"Mistral at GTC 2026: Small 4, Forge and Leanstral explained","url":"https://anthemcreation.com/en/artificial-intelligence/mistral-forge-leanstral-small4-gtc-2026-2/"},{"title":"Mistral Leanstral: AI That Proves Its Own Code | AI Automation Global","url":"https://aiautomationglobal.com/blog/mistral-leanstral-formal-code-verification-2026"},{"title":"Leanstral: Mistral’s Open-Source Proof Agent for Lean 4","url":"https://rits.shanghai.nyu.edu/ai/leanstral-mistrals-open-source-proof-agent-for-lean-4/"},{"title":"Leanstral: Open-Source foundation for trustworthy vibe-coding | Mistral AI","url":"https://mistral.ai/news/leanstral"},{"title":"Mistral AI Models 2026: Small 4, Large 3, Voxtral TTS, Forge — Complete Guide | Serenities AI","url":"https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide"},{"title":"Mistral AI Launches Leanstral Open-Source Proof Agent for Lean 4 | MEXC News","url":"https://www.mexc.com/news/941903"},{"title":"Mistral Large 3: An Open-Source MoE LLM Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained"}]

Based on the search results, here's what I found about Leanstral, Mistral parameters, benchmark performance, and miniF2F 2026:

## Leanstral Overview

Leanstral is Mistral AI's open-source AI agent for Lean 4, released March 16, 2026. It generates formal mathematical proofs that verify code correctness, using the Lean 4 proof assistant.

## Model Parameters

Leanstral is a 120-billion-parameter mixture-of-experts model, but it runs on just 6 billion active parameters per forward pass. This is Mistral's signature architecture play: enormous model capacity, fraction of the compute cost.

## Benchmark Performance on MiniF2F

On the MiniF2F benchmark (the standard evaluation set for formal math proofs): Leanstral at pass@2: 26.3% — outperforms Claude Sonnet at $36 total cost vs $549; Leanstral at pass@4: 29.3% — continues scaling linearly; Claude Opus remains ahead at higher pass counts, but at dramatically higher cost.

## Additional Performance Context

It's worth noting that unlike MiniF2F (which targets isolated competition math problems), FLTEval measures the ability to complete formal proofs in a realistic environment with imports, library dependencies, and multi-file proof structures. Leanstral was also benchmarked on FLTEval, where it achieved similar performance advantages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32b90a7a-fe65-41d7-8e6f-a6e07b3da834",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "68a42c34-6f82-487d-be50-2cced3ca0bd7",
  "sourceToolAssistantUUID": "32b90a7a-fe65-41d7-8e6f-a6e07b3da834",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T06:15:45.312Z_

<details><summary>↩ Tool result · `toolu_01FQ221LZfnmZByA6Y6ma4s1`</summary>

```text
Web search results for query: "APOLLO theorem proving miniF2F benchmark model size 2025"

Links: [{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning | OpenReview","url":"https://openreview.net/forum?id=fxDCgOruk0"},{"title":"[2505.05758] APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/abs/2505.05758"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/pdf/2505.05758"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/html/2505.05758v5"},{"title":"MiniF2F Benchmark","url":"https://www.emergentmind.com/topics/minif2f-benchmark"},{"title":"miniF2F Benchmark for Automated Theorem Proving","url":"https://www.emergentmind.com/topics/minif2f-benchmark-86233917-786a-4287-a747-456c2acde59a"},{"title":"kimina-prover preview: towards large formal reasoning ...","url":"https://arxiv.org/pdf/2504.11354"},{"title":"miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification","url":"https://arxiv.org/html/2512.10187v1"}]

Based on the search results, here's what I found about APOLLO and theorem proving on the miniF2F benchmark in 2025:

## APOLLO System Overview

APOLLO (Automated PrOof repair via LLM and Lean cOllaboration) is a modular, model-agnostic agentic framework that combines the strengths of the Lean compiler with an LLM's reasoning abilities to achieve better proof-generation results at a low token and sampling budgets.

## Model Size and Performance

On the miniF2F benchmark, APOLLO establishes a new state-of-the-art accuracy of 84.9% among sub 8B-parameter models (as of August 2025) while keeping the sampling budget below one hundred.

## How APOLLO Works

Apollo directs a fully automated process in which the LLM generates proofs for theorems, a set of agents analyze the proofs, fix the syntax errors, identify the mistakes in the proofs using Lean, isolate failing sub-lemmas, utilize automated solvers, and invoke an LLM on each remaining goal with a low top-K budget. The repaired sub-proofs are recombined and reverified, iterating up to a user-controlled maximum number of attempts.

## Additional Improvements

Moreover, Apollo raises the state-of-the-art accuracy for Goedel-Prover-SFT to 65.6% while cutting sample complexity from 25,600 to a few hundred.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b99062f-05e4-4b71-9163-9b18e978f5b2",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "dc2f2ff4-07e5-4e47-bb7f-5aa6379137c8",
  "sourceToolAssistantUUID": "3b99062f-05e4-4b71-9163-9b18e978f5b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T06:15:48.873Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GXdGwTw845otECLFp1PCsG`</summary>

```json
{
  "query": "Goedel-Prover-V2 32B release date base model open source license 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc2f2ff4-07e5-4e47-bb7f-5aa6379137c8",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUcfp5Wvymip1vmCfQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8a0c78f-f2e4-4abc-afa7-4524dd5a6b85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC1p6GiitAe7eSkdPdA6iE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1164,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 16465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2981,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-28T06:15:49.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Y1jL424MNKozpXoSbqn1N`</summary>

```json
{
  "query": "Kimina-Prover 72B benchmark miniF2F 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8a0c78f-f2e4-4abc-afa7-4524dd5a6b85",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUcfp5Wvymip1vmCfQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86278456-c168-4389-b747-7b1e4395eff9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC1p6GiitAe7eSkdPdA6iE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1164,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 16465,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1164,
          "output_tokens": 130,
          "cache_read_input_tokens": 16465,
          "cache_creation_input_tokens": 2981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2981,
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

_source line 35 · 2026-05-28T06:15:54.310Z_

<details><summary>↩ Tool result · `toolu_01GXdGwTw845otECLFp1PCsG`</summary>

```text
Web search results for query: "Goedel-Prover-V2 32B release date base model open source license 2025"

Links: [{"title":"Goedel-Prover","url":"https://goedel-lm.github.io/"},{"title":"Goedel-LM/Goedel-Prover-V2-32B · Hugging Face","url":"https://huggingface.co/Goedel-LM/Goedel-Prover-V2-32B"},{"title":"[2508.03613] Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://arxiv.org/abs/2508.03613"},{"title":"GitHub - Goedel-LM/Goedel-Prover · GitHub","url":"https://github.com/Goedel-LM/Goedel-Prover"},{"title":"Paper page - Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://huggingface.co/papers/2508.03613"},{"title":"mradermacher/Goedel-Prover-V2-32B-GGUF · Hugging Face","url":"https://huggingface.co/mradermacher/Goedel-Prover-V2-32B-GGUF"},{"title":"Goedel-Prover-V2","url":"https://blog.goedel-prover.com/"},{"title":"(PDF) Goedel-Prover: A Frontier Model for Open-Source Automated Theorem Proving","url":"https://www.researchgate.net/publication/388920388_Goedel-Prover_A_Frontier_Model_for_Open-Source_Automated_Theorem_Proving"},{"title":"mradermacher/Goedel-Prover-V2-32B-i1-GGUF · Hugging Face","url":"https://huggingface.co/mradermacher/Goedel-Prover-V2-32B-i1-GGUF"},{"title":"GitHub - Goedel-LM/Goedel-Prover-V2 · GitHub","url":"https://github.com/Goedel-LM/Goedel-Prover-V2"}]

Based on the search results, here is the information about Goedel-Prover-V2 32B:

## Release Date
At the time of its release (July-August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers.

## Base Model
The model uses Qwen3-8B and 32B as the base model (for the 32B variant).

## Open Source Status
Goedel-Prover-V2 is an open-source language model series that sets a new state-of-the-art in automated formal proof generation. The models, code, and data are released at https://github.com/Goedel-LM/Goedel-Prover-V2.

## License
The license is apache-2.0.

## Performance
The flagship model, Goedel-Prover-V2-32B, achieves 88.0% on MiniF2F at Pass@32 on standard mode and 90.4% on self-correction mode, outperforming prior SOTA DeepSeek-Prover-V2-671B and concurrent work Kimina-Prover-72B by a large margin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8a0c78f-f2e4-4abc-afa7-4524dd5a6b85",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "4aa168c4-17c5-43ff-86f1-0f06f27e2a8f",
  "sourceToolAssistantUUID": "d8a0c78f-f2e4-4abc-afa7-4524dd5a6b85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T06:15:55.484Z_

<details><summary>↩ Tool result · `toolu_018Y1jL424MNKozpXoSbqn1N`</summary>

```text
Web search results for query: "Kimina-Prover 72B benchmark miniF2F 2025 2026"

Links: [{"title":"Kimina-Prover Preview 72B","url":"https://www.emergentmind.com/topics/kimina-prover-preview-72b"},{"title":"AI-MO/Kimina-Prover-72B · Hugging Face","url":"https://huggingface.co/AI-MO/Kimina-Prover-72B"},{"title":"Kimina-Prover: Applying Test-time RL Search on Large Formal Reasoning Models","url":"https://huggingface.co/blog/AI-MO/kimina-prover"},{"title":"Kimina-Prover: An Open-Source Mathematical Theorem Proving Model","url":"https://www.aibase.com/news/17226"},{"title":"GitHub - MoonshotAI/Kimina-Prover-Preview: Technical report of Kimina-Prover Preview.","url":"https://github.com/MoonshotAI/Kimina-Prover-Preview/tree/master"},{"title":"GitHub - MoonshotAI/Kimina-Prover-Preview: Technical report of Kimina-Prover Preview. · GitHub","url":"https://github.com/MoonshotAI/Kimina-Prover-Preview"},{"title":"kimina-prover preview: towards large formal reasoning ...","url":"https://arxiv.org/pdf/2504.11354"},{"title":"Jia Li on X: \"Happy to introduce Kimina-Prover-72B ! Reaching 92.2% on miniF2F using Test time RL. It can solve IMO problems using more than 500 lines of Lean 4 code ! Check our blog post here: https://t.co/QbrmoyYL9i And play with our demo ! https://t.co/u0Wj0Id4vZ https://t.co/2M82V3Arla\" / X","url":"https://x.com/JiaLi52524397/status/1943293969745743907"}]

Here are the search results for Kimina-Prover 72B benchmark miniF2F:

## Overview

Kimina-Prover-Preview-72B is a LLM-based formal theorem prover designed for Lean 4, introduced in April 2025. It employs a 72-billion parameter Qwen2.5 backbone and leverages a multi-stage reinforcement learning pipeline.

## miniF2F Benchmark Performance

The model demonstrates strong performance on the miniF2F benchmark with various metrics:

- At pass@1 (one sample per problem), it solves 52.94% of miniF2F-test
- It achieves 84.0% accuracy with Pass@32 on MiniF2F-test
- With pass@32 it achieves 84.0%, and 86.4% with the addition of a single round of error correction
- Using Test time RL, it reaches 92.2% on miniF2F

## Key Features

Performance scales systematically with model size, a property not previously observed in neural theorem provers for formal mathematics. The model demonstrates strong sample efficiency, outperforming previous stepwise or search-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86278456-c168-4389-b747-7b1e4395eff9",
  "isSidechain": true,
  "promptId": "3f457316-df65-485e-ba63-e9e9420b66e4",
  "agentId": "a0dbd6ab64543c9a6",
  "type": "user",
  "uuid": "0287e892-cc46-48d1-b496-3c73624a8516",
  "sourceToolAssistantUUID": "86278456-c168-4389-b747-7b1e4395eff9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-28T06:16:38.874Z_

Here is a comprehensive summary of the current top open-source models for theorem proving and formal math as of May 2026, ranked by their performance on the key MiniF2F benchmark.

---

## Top Open-Source Models for Theorem Proving (as of May 2026)

### Tier 1: Purpose-Built Theorem Provers (Lean 4)

| Model | Params | MiniF2F-test | PutnamBench | Base Model | License | Release |
|---|---|---|---|---|---|---|
| **Goedel-Prover-V2-32B** | 32B | 90.4% (Pass@32, self-correction) | 86 problems (Pass@184) | Qwen3-32B | Apache 2.0 | Aug 2025 |
| **Kimina-Prover-72B** | 72B | 92.2% (with test-time RL) / 84.0% (Pass@32) | N/A | Qwen2.5-72B | Open-weights | Apr 2025 |
| **DeepSeek-Prover-V2-671B** | 671B total (37B active, MoE) | 88.9% (Pass@8192) / 82.4% (Pass@32) | 49/658 problems | DeepSeek-V3-Base | Open-weights | Apr 2025 |
| **DeepSeek-Prover-V2-7B** | 7B | Strong (outperforms prior open-source) | 13 additional solutions beyond 671B | DeepSeek-Prover-V1.5-Base | Open-weights | Apr 2025 |
| **Leanstral** | 120B total (6B active, MoE) | 29.3% (Pass@4) | N/A | Mistral MoE | Apache 2.0 | Mar 2026 |
| **InternLM2.5-StepProver** | ~7B | 65.9% (Pass@?) | 17.0% of Lean-Workbook-Plus | InternLM2.5 | Open-source | 2024 |

### Tier 2: Agentic Frameworks (model-agnostic wrappers)

| System | Best MiniF2F | Notes |
|---|---|---|
| **APOLLO** | 84.9% (sub-8B models) | Agentic framework that wraps any LLM; uses proof repair, automated solvers, sub-lemma isolation. Not a model itself. |

### Tier 3: Strong General-Purpose Reasoning Models (potential fine-tuning bases)

| Model | Params | Math Benchmarks | Open-source | Release |
|---|---|---|---|---|
| **Qwen3-235B-A22B** | 235B total (22B active, MoE) | AIME25: 92.3% | Yes, open-weights | May 2025 |
| **DeepSeek-R1** | 671B (MoE) | o1-level reasoning, top-tier math | Yes, open-weights | Jan 2025 |
| **DeepSeek-V3 / V3.2** | 671B (37B active, MoE) | Surpasses GPT-4.5 on math/coding | Yes, open-weights | Dec 2024 / Dec 2025 |
| **Qwen3-32B** | 32B (dense) | Strong math/reasoning, thinking mode | Yes, open-weights | May 2025 |
| **GLM-Z1-9B** | 9B | "Lightweight champion" for math | Yes, open-weights | Apr 2025 |

---

## Recommendation for Fine-Tuning a Decomposition Policy

For your specific use case of fine-tuning a decomposition policy for theorem proving, the top candidates are:

**1. Goedel-Prover-V2-32B (Best Overall Choice)**
- Current SOTA among open-source theorem provers
- Beats DeepSeek-Prover-V2-671B with only 1/20th the parameters
- Built on Qwen3-32B, so it inherits strong general reasoning
- Apache 2.0 license -- fully permissive for fine-tuning
- 32B is a practical size for fine-tuning on modern hardware (fits on 2-4 A100s)
- Already trained on formal theorem proving with subgoal decomposition techniques

**2. DeepSeek-Prover-V2-7B (Best Lightweight Option)**
- Only 7B parameters -- very cheap to fine-tune
- Already specialized for Lean 4 theorem proving with subgoal decomposition via RL
- Its training methodology (cold-start decomposition from DeepSeek-V3, then RL with binary proof-checking feedback) is directly relevant to a decomposition policy
- Outperforms all prior open-source provers at its size class

**3. Qwen3-32B (Best General Base for Custom Training)**
- If you want to train a decomposition policy from scratch rather than building on an existing prover, this is the strongest dense 32B base model
- Both Goedel-Prover-V2 and Kimina-Prover chose Qwen as their base, validating it as the go-to foundation for theorem proving fine-tuning

**Key Insight:** DeepSeek-Prover-V2's training pipeline is especially relevant to your goal -- it explicitly uses RL for subgoal decomposition, where DeepSeek-V3 decomposes complex problems into subgoals, synthesizes proofs of those subgoals into chain-of-thought, and then trains via RL with binary correctness feedback from Lean. This is essentially a decomposition policy. Goedel-Prover-V2 builds on similar ideas but achieves better results at a fraction of the parameter count.

---

Sources:
- [Goedel-Prover-V2-32B on Hugging Face](https://huggingface.co/Goedel-LM/Goedel-Prover-V2-32B)
- [Goedel-Prover-V2 Paper](https://arxiv.org/abs/2508.03613)
- [Goedel-Prover-V2 GitHub](https://github.com/Goedel-LM/Goedel-Prover-V2)
- [DeepSeek-Prover-V2 Paper](https://arxiv.org/abs/2504.21801)
- [DeepSeek-Prover-V2-7B on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-7B)
- [DeepSeek-Prover-V2-671B on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B)
- [Kimina-Prover-72B on Hugging Face](https://huggingface.co/AI-MO/Kimina-Prover-72B)
- [Kimina-Prover Blog](https://huggingface.co/blog/AI-MO/kimina-prover)
- [APOLLO Paper](https://arxiv.org/abs/2505.05758)
- [Leanstral by Mistral AI](https://mistral.ai/news/leanstral)
- [Leanstral Review - SaaS Pilot](https://saaspilot.org/ai-coding-assistants/2026-03-20-radar-2-leanstral-review/)
- [Leanstral - Top AI Product](https://topaiproduct.com/2026/03/16/leanstral-uses-6b-active-parameters-to-beat-models-100x-its-size-at-formal-proofs/)
- [InternLM2.5-StepProver Paper](https://arxiv.org/pdf/2410.15700)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- [Qwen3 Blog](https://qwenlm.github.io/blog/qwen3/)
- [DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)
- [Best Open Source LLM for Math - SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)
- [LeanDojo](https://leandojo.org/)
- [Goedel-Prover V1 Paper](https://arxiv.org/pdf/2502.07640)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0287e892-cc46-48d1-b496-3c73624a8516",
  "isSidechain": true,
  "agentId": "a0dbd6ab64543c9a6",
  "requestId": "req_011CbUUdRKxsQ8dZRVk67Suo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa350fdf-c7b8-4be1-af32-169218bf6013",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d31c081-a8b8-4103-b7d3-3a63bc4c67b8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URzSSVZLFqCoWEDJMn3NZE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3089,
      "cache_read_input_tokens": 19446,
      "output_tokens": 2159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2159,
          "cache_read_input_tokens": 19446,
          "cache_creation_input_tokens": 3089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3089,
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
