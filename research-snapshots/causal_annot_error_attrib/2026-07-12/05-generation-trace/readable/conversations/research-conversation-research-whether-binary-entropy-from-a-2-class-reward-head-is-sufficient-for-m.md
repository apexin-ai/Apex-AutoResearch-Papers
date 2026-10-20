# Research conversation: Research whether binary entropy from a 2-class reward head is sufficient for multi-tier routing in a process reward mode

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa5982aa090e023fa.jsonl`
- **Structured JSON:** [`ce8b8e8f768fc5307739.json`](../../sessions/ce/ce8b8e8f768fc5307739.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-27T22:00:43.118Z_

Research whether binary entropy from a 2-class reward head is sufficient for multi-tier routing in a process reward model, and what alternatives exist. Context: We have a PRM with a binary (correct/incorrect) reward head. Its predictive entropy has at most log(2)≈0.69 nats of information. We want to use this to route between 3 verification tiers.

I need to find:

1. **Calibration of binary classifiers for routing** - Is binary entropy a reliable signal? What calibration issues arise?
2. **Hidden-state uncertainty methods** - Using the full hidden-state representation rather than just the output logits for uncertainty estimation. Methods like:
   - Spectral-normalized neural Gaussian processes (SNGP)
   - Deep ensembles
   - Deterministic uncertainty quantification (DUQ)
3. **Multi-class uncertainty for PRM** - Could we reformulate the reward head as multi-class (e.g., correct/partially-correct/incorrect/uncertain)?
4. **EDU-PRM entropy usage** (2503.22233) - How does EDU-PRM use entropy? Is it binary entropy or something richer?
5. **Two-tier vs three-tier routing** - Would simplifying to 2 tiers (skip vs. deep-verify) be more robust?

Search queries:
- "binary entropy routing calibration neural network"
- "uncertainty quantification transformer hidden states 2025"
- "EDU-PRM entropy driven uncertainty process reward"
- "adaptive compute allocation uncertainty routing transformer"
- "spectral normalized gaussian process uncertainty estimation 2025 2026"

I need to determine: should we keep 3 tiers with a richer uncertainty signal, or simplify to 2 tiers with binary entropy?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "9269ae7c-c5dc-45c6-879f-1a0afd140033",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T22:00:43.123Z_

```json
{
  "parentUuid": "9269ae7c-c5dc-45c6-879f-1a0afd140033",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
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
  "uuid": "691bd44f-28da-4767-9200-618803215966",
  "timestamp": "2026-05-27T22:00:43.123Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T22:00:43.125Z_

```json
{
  "parentUuid": "691bd44f-28da-4767-9200-618803215966",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "89e8a2c7-5b93-4db5-9fe5-52de2caeb4f8",
  "timestamp": "2026-05-27T22:00:43.125Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T22:00:53.440Z_



I'll research this systematically using web searches to find the latest work on each of these topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89e8a2c7-5b93-4db5-9fe5-52de2caeb4f8",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsCDPfT61HcVrG7Yqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb833814-b9d6-4beb-831c-e2e4f610a44f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016roLdZa7RDYoYnVkzQJVqr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1716,
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

_source line 5 · 2026-05-27T22:00:53.585Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BquUgrNTjbANzvjsPhagek`</summary>

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
  "parentUuid": "bb833814-b9d6-4beb-831c-e2e4f610a44f",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsCDPfT61HcVrG7Yqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fae4c946-c529-4457-845e-a742eda4f787",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016roLdZa7RDYoYnVkzQJVqr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 7411,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1716,
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

_source line 6 · 2026-05-27T22:00:53.588Z_

<details><summary>↩ Tool result · `toolu_01BquUgrNTjbANzvjsPhagek`</summary>

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
  "parentUuid": "fae4c946-c529-4457-845e-a742eda4f787",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "475cb43b-88f5-4730-8c1e-9d6e635065a7",
  "sourceToolAssistantUUID": "fae4c946-c529-4457-845e-a742eda4f787",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T22:00:56.749Z_



Now let me run all the searches in parallel to gather information on each topic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "475cb43b-88f5-4730-8c1e-9d6e635065a7",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsyb9iWxHqF7RYYFMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55c6bc0e-a76f-4135-be58-cfe2356778d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJHAK1RbGi4GKyXo68ie4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 8 · 2026-05-27T22:00:57.369Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015kS7PaWsqQRS3JqzasudkF`</summary>

```json
{
  "query": "EDU-PRM entropy driven uncertainty process reward model 2503.22233"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55c6bc0e-a76f-4135-be58-cfe2356778d1",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsyb9iWxHqF7RYYFMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5c7c844-6f07-4ac1-9175-e22fd6e3e972",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJHAK1RbGi4GKyXo68ie4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 9 · 2026-05-27T22:00:57.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012tR5beE3MZf1yCNCakfjZN`</summary>

```json
{
  "query": "binary entropy calibration routing neural network classifier uncertainty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5c7c844-6f07-4ac1-9175-e22fd6e3e972",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsyb9iWxHqF7RYYFMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93228b19-2dc2-4c88-9ce3-7274b5ca9c12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJHAK1RbGi4GKyXo68ie4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 10 · 2026-05-27T22:00:58.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6bMcvRTQWV2JsC4MjnUsk`</summary>

```json
{
  "query": "spectral normalized gaussian process SNGP uncertainty estimation transformer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93228b19-2dc2-4c88-9ce3-7274b5ca9c12",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsyb9iWxHqF7RYYFMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8006367d-578a-461c-9b7f-4d8017ccae76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJHAK1RbGi4GKyXo68ie4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 11 · 2026-05-27T22:00:58.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PYfWv3GSmDsmKgF9c4D2im`</summary>

```json
{
  "query": "adaptive compute allocation uncertainty routing transformer verification tiers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8006367d-578a-461c-9b7f-4d8017ccae76",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsyb9iWxHqF7RYYFMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e5361bc-baf0-410a-bc4a-328141d1744f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJHAK1RbGi4GKyXo68ie4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 12 · 2026-05-27T22:00:59.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KLKW1KAda7yCMzDCQagNjs`</summary>

```json
{
  "query": "deterministic uncertainty quantification DUQ deep ensemble hidden state uncertainty LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e5361bc-baf0-410a-bc4a-328141d1744f",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpsyb9iWxHqF7RYYFMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59f13e87-1cd7-4f2f-8da6-0f946280459e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZJHAK1RbGi4GKyXo68ie4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 9127,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 9127,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 627,
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

_source line 13 · 2026-05-27T22:01:04.718Z_

<details><summary>↩ Tool result · `toolu_015kS7PaWsqQRS3JqzasudkF`</summary>

```text
Web search results for query: "EDU-PRM entropy driven uncertainty process reward model 2503.22233"

Links: [{"title":"[2503.22233] More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/abs/2503.22233"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/pdf/2503.22233"},{"title":"Paper page - Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://huggingface.co/papers/2503.22233"},{"title":"Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233v1"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty | OpenReview","url":"https://openreview.net/forum?id=nPs3KM1aGG"},{"title":"(PDF) Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://www.researchgate.net/publication/390322275_Process_Reward_Modeling_with_Entropy-Driven_Uncertainty"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"}]

Based on the search results, here's what I found about EDU-PRM:

## Overview

EDU-PRM (Entropy-Driven Uncertainty Process Reward Model) is a novel entropy-driven training framework for process reward modeling that enables dynamic, uncertainty-aligned segmentation of complex reasoning steps, eliminating the need for costly manual step annotations.

## Key Innovation

Unlike previous Process Reward Models (PRMs) that rely on static partitioning and human labeling, EDU-PRM automatically anchors step boundaries at tokens with high predictive entropy, effectively capturing intrinsic logical transitions and facilitating efficient exploration of diverse reasoning paths.

## Performance

On the ProcessBench benchmark, EDU-PRM outperforms strong public PRM baselines, such as Math-Shepherd PRM and Omega PRM, and achieves comparable results with state-of-the-art models while only using 1.5% training data. Additionally, by leveraging the proposed EDU sampling strategy, accuracy improves from 64.7% to 67.3% for generative reasoning tasks, accompanied by a reduction of 32% in token usage.

## Significance

These findings underscore the potential of EDU-PRM as a scalable and annotation-efficient paradigm for process supervision in mathematical reasoning, paving the way for more efficient and robust approaches to complex mathematical problem solving.

The paper was published on arXiv on March 28, 2025, with subsequent versions through March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5c7c844-6f07-4ac1-9175-e22fd6e3e972",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "cefdf430-407c-4063-a7b4-ca3dd7d4cf6c",
  "sourceToolAssistantUUID": "c5c7c844-6f07-4ac1-9175-e22fd6e3e972",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T22:01:05.388Z_

<details><summary>↩ Tool result · `toolu_012tR5beE3MZf1yCNCakfjZN`</summary>

```text
Web search results for query: "binary entropy calibration routing neural network classifier uncertainty"

Links: [{"title":"DBCal: Density Based Calibration of classifier predictions for   uncertainty quantification","url":"https://arxiv.org/pdf/2204.00150"},{"title":"Calibrated and uncertain? Evaluating uncertainty estimates in binary classification models","url":"https://arxiv.org/html/2508.11460v1"},{"title":"Neural Networks Calibration via Learning Uncertainty-Error ...","url":"https://arxiv.org/pdf/2505.22803"},{"title":"Geometric Calibration and Neutral Zones for Uncertainty-Aware Multi-Class Classification","url":"https://arxiv.org/pdf/2511.20960"},{"title":"Classifier Ensemble for Efficient Uncertainty Calibration of Deep Neural   Networks for Image Classification","url":"https://arxiv.org/pdf/2501.10089"},{"title":"Measuring Uncertainty Calibration","url":"https://arxiv.org/pdf/2512.13872"}]

Based on the search results, here are the key findings related to binary entropy calibration, routing, neural network classifier uncertainty:

## Uncertainty Calibration in Neural Networks

With increasingly complex data models such as deep learning techniques, uncertainty quantification has become exceedingly difficult and a plethora of techniques have been proposed. Neural networks often suffer from an "overconfidence" problem, which calibration methods aim to address.

## Calibration Methods and Approaches

Several approaches have been developed to improve classifier calibration:

- Post-hoc calibration methods—temperature scaling and Platt scaling—apply univariate transformations that treat probability vectors as unconstrained Euclidean points, ignoring the simplex constraint.

- CLUE adopts a lightweight and pragmatic approach that leverages the task-specific loss function (e.g., Cross-entropy for classification or Mean Squared Error for regression) as a differentiable proxy for calibration.

- Classifier ensemble techniques for uncertainty calibration investigate different methods for building simple yet efficient classifier ensembles, including majority voting and several metamodel-based approaches.

## Evaluation Metrics

Calibration is often evaluated using metrics like Expected Calibration Error (ECE) and Maximum Calibration Error (MCE).

The search results primarily focus on calibration techniques for uncertainty quantification in neural network classifiers, though they don't specifically address "routing" mechanisms in the context you may have been looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93228b19-2dc2-4c88-9ce3-7274b5ca9c12",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "ab157109-503c-4bc0-928b-0ceaf49bd217",
  "sourceToolAssistantUUID": "93228b19-2dc2-4c88-9ce3-7274b5ca9c12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T22:01:05.571Z_

<details><summary>↩ Tool result · `toolu_01H6bMcvRTQWV2JsC4MjnUsk`</summary>

```text
Web search results for query: "spectral normalized gaussian process SNGP uncertainty estimation transformer 2025 2026"

Links: [{"title":"Enhancing Brain Age Estimation Under Uncertainty: A Spectral-normalized Neural Gaussian Process Approach Utilizing 2.5D Slicing | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2025.02.26.25322983v1.full"},{"title":"GitHub - AIRI-Institute/uncertainty_transformers","url":"https://github.com/airi-institute/uncertainty_transformers"},{"title":"Enhancing Brain Age Estimation Under Uncertainty: A Spectral-normalized Neural Gaussian Process Approach Utilizing 2.5D Slicing","url":"https://www.medrxiv.org/content/10.1101/2025.02.26.25322983.full.pdf"},{"title":"(PDF) Simple and Principled Uncertainty Estimation with Deterministic Deep Learning via Distance Awareness","url":"https://www.researchgate.net/publication/342302060_Simple_and_Principled_Uncertainty_Estimation_with_Deterministic_Deep_Learning_via_Distance_Awareness"},{"title":"Simple and Principled Uncertainty Estimation with Deterministic Deep   Learning via Distance Awareness","url":"https://arxiv.org/pdf/2006.10108"},{"title":"Uncertainty quantification in neural network-based glucose prediction for diabetes","url":"https://arxiv.org/pdf/2603.04955"},{"title":"Uncertainty-Aware Image Classification In Biomedical Imaging Using Spectral-normalized Neural Gaussian Processes","url":"https://arxiv.org/pdf/2602.02370"}]

Based on the search results, I found recent and relevant information about Spectral-normalized Neural Gaussian Process (SNGP) uncertainty estimation with transformers:

## Recent Applications (2025-2026)

SNGP has been applied with a 2.5D slice approach for seamless uncertainty integration in a single network with low computational expenses for brain age estimation, as documented in a February 2025 preprint.

## Transformer Integration

SNGP is implemented as one of the uncertainty estimation methods in a repository for NLP tasks, and these methods were tested with ELECTRA and DeBERTa models on various NLP benchmarks.

## How SNGP Works

SNGP improves the distance-awareness ability of modern DNNs by adding a weight normalization step during training and replacing the output layer with a Gaussian Process. SNGP is a single-network deterministic method which only requires a simple modification of the neural network to enable uncertainty estimation, while keeping training and inference costs low and approaching Deep Ensemble performance.

## Performance Characteristics

On vision and language understanding tasks with modern architectures like Wide-ResNet and BERT, SNGP is competitive with deep ensembles in prediction, calibration and out-of-domain detection, and outperforms other single-model approaches. SNGP has comparable in-distribution performance while significantly improving uncertainty estimation and OOD detection, offering a useful framework for uncertainty-aware classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8006367d-578a-461c-9b7f-4d8017ccae76",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "838b8cda-8ffc-460d-a10c-e87a618cf18a",
  "sourceToolAssistantUUID": "8006367d-578a-461c-9b7f-4d8017ccae76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T22:01:05.789Z_

<details><summary>↩ Tool result · `toolu_01KLKW1KAda7yCMzDCQagNjs`</summary>

```text
Web search results for query: "deterministic uncertainty quantification DUQ deep ensemble hidden state uncertainty LLM"

Links: [{"title":"[2003.02037] Uncertainty Estimation Using a Single Deep Deterministic Neural Network","url":"https://ar5iv.labs.arxiv.org/html/2003.02037"},{"title":"Uncertainty quantification in LLMs","url":"https://bimsa.net/doc/notes/51259.pdf?id=0.9578430985566229"},{"title":"Uncertainty Estimation Using a Single Deep Deterministic Neural Network","url":"http://proceedings.mlr.press/v119/van-amersfoort20a/van-amersfoort20a.pdf"},{"title":"Uncertainty Estimation Using a Single Deep Deterministic Neural Network","url":"https://arxiv.org/pdf/2003.02037"},{"title":"[2102.11582] Deep Deterministic Uncertainty: A Simple Baseline","url":"https://ar5iv.labs.arxiv.org/html/2102.11582"},{"title":"Deep Deterministic Uncertainty: A Simple Baseline","url":"https://arxiv.org/pdf/2102.11582"},{"title":"Black-Box Uncertainty Quantification for Large Language Models via","url":"https://openreview.net/pdf?id=jfq9DUrW90"}]

Based on the search results, here's what I found about these topics:

## Deterministic Uncertainty Quantification (DUQ)

DUQ builds upon ideas of RBF networks and scales training with a novel loss function and centroid updating scheme while matching the accuracy of softmax models. By enforcing detectability of changes in the input using a gradient penalty, DUQ can reliably detect out of distribution data.

DUQ is certain only on the data distribution, and uncertain away from it: the ideal result. Using a single model, DUQ improves upon or matches Deep Ensembles in out of distribution detection on dataset pairs such as Fashion-MNIST vs. MNIST, and CIFAR-10 vs. SVHN.

## Deep Ensembles and Uncertainty

Deep Ensembles are not able to obtain meaningful uncertainty on some datasets because of a lack of diversity in the different models in the ensemble. For Deep Ensembles, both computation and memory cost scale linearly in the number of ensemble components, during both train and test time.

## Uncertainty in Large Language Models

More recent work has adapted UQ to the LLM setting through both white-box and black-box approaches, where the former category exploits internal model signals such as token-level logits or hidden states to estimate semantic uncertainty or detect hallucinations. Black-box methods treat the model as a generator and infer uncertainty from behavioral consistency or learned scoring across sampled outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f13e87-1cd7-4f2f-8da6-0f946280459e",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "68d79d1c-e786-4a67-ad0d-6d802b2a1fb3",
  "sourceToolAssistantUUID": "59f13e87-1cd7-4f2f-8da6-0f946280459e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T22:01:08.747Z_

<details><summary>↩ Tool result · `toolu_01PYfWv3GSmDsmKgF9c4D2im`</summary>

```text
Web search results for query: "adaptive compute allocation uncertainty routing transformer verification tiers"

Links: [{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/html/2602.03975v1"},{"title":"Error-Driven Adaptive Routing: Learning Compute Allocation from Frozen Representations | by Micheal Bee | Nov, 2025 | Medium","url":"https://medium.com/@mbonsign/error-driven-adaptive-routing-learning-compute-allocation-from-frozen-representations-037bbb6196e8"},{"title":"Beyond Single-Dimension AI: Unpacking Jointly’s Meta-ACE Framework","url":"https://www.startuphub.ai/ai-news/ai-video/2025/beyond-single-dimension-ai-unpacking-jointlys-meta-ace-framework/"},{"title":"WHEN TO PONDER: ADAPTIVE COMPUTE ALLOCATION FOR CODE GENERATION VIA TEST-TIME","url":"https://www.arxiv.org/pdf/2601.00894"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"When to Ponder: Adaptive Compute Allocation for Code Generation via Test-Time Training","url":"https://arxiv.org/html/2601.00894"}]

The search results reveal several recent research approaches related to adaptive compute allocation and uncertainty-aware verification in transformers:

## Key Research Findings

**Adaptive Test-Time Compute Allocation:**
Recent work proposes a state-level selective verification framework combining deterministic feasibility gating, pre-verification ranking using hybrid scoring, and adaptive allocation of verifier calls based on local uncertainty. This approach achieves higher accuracy than best-of-N and beam search methods while using 44% fewer verifier calls on the MATH benchmark.

**Error-Driven Adaptive Routing:**
Error-driven adaptive routing dynamically allocates compute based on learned prompt difficulty, learning from error signals to determine whether initial processing achieves acceptable results, needs refinement, or requires contextual warnings.

**Transformer Efficiency Through Test-Time Training:**
Standard transformer models operate on fixed computational graphs where every token processes the same layers and attention heads, creating inefficiency since simple tasks like import statements require far less computation than complex algorithms.

**Meta-ACE Framework:**
One framework evaluates tasks across multiple dimensions: semantic complexity, uncertainty quantification via relative Softmax scoring, verifiability assessment, and resource availability. The approach includes adaptive compute strategies that scale reasoning steps based on task difficulty.

These recent developments (from late 2025 through early 2026) focus on improving efficiency by strategically directing computational resources to where they're most needed, rather than applying uniform computation across all inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e5361bc-baf0-410a-bc4a-328141d1744f",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "80f46706-02b1-4081-b205-220485b93444",
  "sourceToolAssistantUUID": "2e5361bc-baf0-410a-bc4a-328141d1744f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T22:01:15.724Z_

Now let me do more targeted searches to fill in gaps, particularly on EDU-PRM's specific entropy mechanism, multi-class PRM reformulation, and two-tier vs three-tier routing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80f46706-02b1-4081-b205-220485b93444",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpu5nFTx4ZoamNR4mnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0217419-e5a8-49bd-9646-6e589b1d8c7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8vcHF2Tjaz4BaJ3LE2owC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 692,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 9754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 19 · 2026-05-27T22:01:16.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LPFDES6ri3FgakwbetTPN7`</summary>

```json
{
  "query": "EDU-PRM entropy token level segmentation binary logit reward model mechanism details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0217419-e5a8-49bd-9646-6e589b1d8c7b",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpu5nFTx4ZoamNR4mnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0958cd64-92bd-449f-9af4-faf1b1019522",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8vcHF2Tjaz4BaJ3LE2owC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 692,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 9754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 20 · 2026-05-27T22:01:17.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tqw9QZbtguKFFrV3GZCLuB`</summary>

```json
{
  "query": "process reward model multi-class reward head correct partially correct incorrect reformulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0958cd64-92bd-449f-9af4-faf1b1019522",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpu5nFTx4ZoamNR4mnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3346f177-5305-4a22-b786-70966f79d647",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8vcHF2Tjaz4BaJ3LE2owC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 692,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 9754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 21 · 2026-05-27T22:01:18.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzRGiE6msnUuwZZ8qmA7FF`</summary>

```json
{
  "query": "two tier vs three tier routing compute budget verification simplify uncertainty threshold 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3346f177-5305-4a22-b786-70966f79d647",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpu5nFTx4ZoamNR4mnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fa210ee-0b23-4a93-8a89-ae79f29a1439",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8vcHF2Tjaz4BaJ3LE2owC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 692,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 9754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 22 · 2026-05-27T22:01:18.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjnZLpzdrqFuocfN8N9mhA`</summary>

```json
{
  "query": "binary classifier entropy ceiling routing limitations information bottleneck"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fa210ee-0b23-4a93-8a89-ae79f29a1439",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpu5nFTx4ZoamNR4mnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f54cc29-14cd-45e2-87c3-dde42e3dcc5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8vcHF2Tjaz4BaJ3LE2owC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 692,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 9754,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 692,
          "output_tokens": 253,
          "cache_read_input_tokens": 9754,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3101,
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

_source line 23 · 2026-05-27T22:01:24.554Z_

<details><summary>↩ Tool result · `toolu_01Tqw9QZbtguKFFrV3GZCLuB`</summary>

```text
Web search results for query: "process reward model multi-class reward head correct partially correct incorrect reformulation"

Links: [{"title":"Reward Modeling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/05-reward-models"},{"title":"Process Reward Models - Stephen Diehl","url":"https://www.stephendiehl.com/posts/process_reward/"},{"title":"Reward Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/reward-models"},{"title":"Guide to Reward Functions in Reinforcement Fine-Tuning | Rubrik","url":"https://predibase.com/blog/reward-functions-reinforcement-fine-tuning"},{"title":"Process Reward Model with Q-Value Rankings","url":"https://arxiv.org/pdf/2410.11287"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/pdf/2604.02341"},{"title":"Reinforcement Learning from Verifiable Rewards | Label Studio","url":"https://labelstud.io/blog/reinforcement-learning-from-verifiable-rewards/"},{"title":"Rethinking Reward Models for Multi-Domain Test-Time Scaling","url":"https://arxiv.org/pdf/2510.00492"},{"title":"Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning","url":"https://arxiv.org/pdf/2601.18984"}]

Based on the search results, I found relevant information about process reward models and multi-class reward structures. Here's what the research shows:

## Multi-Class Reward Heads in Process Reward Models

Process reward models use a 3-class label system: correct (+1), neutral (0), or incorrect (-1). Traditionally, PRMs are trained with a language modeling head that outputs a token only at the end of a reasoning step, e.g., at the token corresponding to a double new line or other special token.

The search results indicate that existing research typically frames PRM as a classification problem, where each intermediate state is classified as correct or incorrect. However, the results also suggest that moving beyond binary (0 or 1) rewards and assigning partial scores to partially correct outputs can better guide the model's learning.

Notably, these labels do not necessarily tie to whether or not the model is on the right path, but rather to whether the step is correct, which relates to the distinction between complete/incomplete and correct/incorrect processes mentioned in the research.

The standard three-class labeling (correct, neutral/partially correct, and incorrect) appears to be the predominant approach for multi-class reward heads in contemporary process reward model research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3346f177-5305-4a22-b786-70966f79d647",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "0a47bd29-699d-47db-aab9-ac2de93e1ece",
  "sourceToolAssistantUUID": "3346f177-5305-4a22-b786-70966f79d647",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T22:01:24.780Z_

<details><summary>↩ Tool result · `toolu_01LPFDES6ri3FgakwbetTPN7`</summary>

```text
Web search results for query: "EDU-PRM entropy token level segmentation binary logit reward model mechanism details"

Links: [{"title":"Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233v1"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233"},{"title":"Paper page - Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://huggingface.co/papers/2503.22233"},{"title":"(PDF) Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://www.researchgate.net/publication/390322275_Process_Reward_Modeling_with_Entropy-Driven_Uncertainty"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/pdf/2503.22233"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prms"},{"title":"[2503.22233] More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/abs/2503.22233"},{"title":"Process Reward Modeling with Entropy-Driven Uncertainty | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/process-reward-modeling-entropy-driven-uncertainty"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty | OpenReview","url":"https://openreview.net/forum?id=nPs3KM1aGG"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"}]

Based on the search results, here are the key details about EDU-PRM's entropy token level segmentation and binary logit reward model mechanism:

## Core Mechanism

EDU-PRM introduces an entropy-guided dynamic step partitioning mechanism, using logit distribution entropy to pinpoint high-uncertainty regions during token generation dynamically. Unlike previous Process Reward Models (PRMs) that rely on static partitioning or human labeling, EDU-PRM automatically anchors step boundaries at tokens with high predictive entropy, which can effectively capture intrinsic logical transitions and facilitating efficient exploration of diverse reasoning paths.

## Token-Level Segmentation Process

At the separation point (termed the branch point in PRM), rather than conventional high-temperature sampling, the model initiates two decoding branches by selecting the top-1 and top-2 logits. For subsequent decoding, the model exclusively employs greedy sampling to generate content until the next branching event. After performing the EDU sampling, the model generates a binary tree, where each branch is segmented into fragments by uncertainty anchors.

## Binary Reward Labels

To score each fragment, the model assigns a correctness label (0,1) based on the final solution's validity using Monte Carlo Estimation (MCE). EDU-PRM is trained via a classification-oriented cross-entropy loss.

## Performance Results

Experiments on the Qwen2.5-72B model with only 7,500 EDU-PRM-generated training queries demonstrate accuracy closely approximating the full Qwen2.5-72B-PRM (71.1% vs. 71.6%), achieving a 98% reduction in query cost compared to prior methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0958cd64-92bd-449f-9af4-faf1b1019522",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "2c7057e7-c531-4cd9-b52f-dbbe0b996bf3",
  "sourceToolAssistantUUID": "0958cd64-92bd-449f-9af4-faf1b1019522",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T22:01:25.744Z_

<details><summary>↩ Tool result · `toolu_01TjnZLpzdrqFuocfN8N9mhA`</summary>

```text
Web search results for query: "binary classifier entropy ceiling routing limitations information bottleneck"

Links: [{"title":"Stable and Convexified Information Bottleneck: A Smooth Path to Better Representations | Medium","url":"https://lightcapai.medium.com/stable-and-convexified-information-bottleneck-a-smooth-path-to-better-representations-d8c4b463a4f5"},{"title":"1 The Information Bottleneck Problem and Its Applications in Machine Learning","url":"https://arxiv.org/pdf/2004.14941"},{"title":"Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility","url":"https://arxiv.org/html/2509.14386"},{"title":"[2002.05379] The Conditional Entropy Bottleneck","url":"https://ar5iv.labs.arxiv.org/html/2002.05379"},{"title":"Published as a conference paper at ICLR 2019 CAVEATS FOR INFORMATION BOTTLENECK","url":"https://artemyk.github.io/assets/pdf/papers/Kolchinsky%20et%20al_2019_Caveats%20for%20information%20bottleneck%20in%20deterministic%20scenarios.pdf"},{"title":"Published as a conference paper at ICLR 2018 ON THE INFORMATION BOTTLENECK","url":"https://openreview.net/pdf?id=ry_WPG-A-"},{"title":"Information Bottleneck Revisited: Posterior Probability Perspective with   Optimal Transport","url":"https://arxiv.org/pdf/2308.11296"},{"title":"CEB Improves Model Robustness","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7597163/"}]

Here are the search results for your query on binary classifier entropy ceiling, routing limitations, and information bottleneck:

## Key Findings

**Entropy Ceiling in Information Bottleneck**: Standard Information Bottleneck approaches can reach a flat ceiling, particularly in binary channel scenarios, while alternative convexified approaches keep rising smoothly. The mutual information between compressed representations and targets converges to the maximum mutual information available in the channel.

**Binary Classification and Information Bottleneck**: Binary classification tasks using fully connected neural networks can be analyzed through information plane dynamics, where information flow between layers is measured. In binary classification experiments, near-perfect prediction can be achieved while hidden layer activations retain information irrelevant for prediction and fall onto the flat part of the IB curve.

**Information Bottleneck Limitations**: Classical Information Bottleneck algorithms face limitations when the IB curve contains constant-slope segments, which can result in limited numerical results. Binary supervision creates information deficits through information bottleneck constraints.

**Routing and Representation**: Information bottleneck methods address the problem that learning systems may retain too much information about training data by proposing compression-based objectives like the Conditional Entropy Bottleneck.

The search results focus primarily on information-theoretic limitations in deep learning and compression-based approaches rather than specifically on routing limitations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f54cc29-14cd-45e2-87c3-dde42e3dcc5c",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "6e9a4578-609a-420a-9429-3ee0a5a620ff",
  "sourceToolAssistantUUID": "9f54cc29-14cd-45e2-87c3-dde42e3dcc5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T22:01:26.472Z_

<details><summary>↩ Tool result · `toolu_01XzRGiE6msnUuwZZ8qmA7FF`</summary>

```text
Web search results for query: "two tier vs three tier routing compute budget verification simplify uncertainty threshold 2025"

Links: [{"title":"Budget-aware Test-time Scaling via Discriminative Verification","url":"https://arxiv.org/pdf/2510.14913"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"Three-Tier LLM Routing: Fast, Smart, and Power Model Stacks | MindStudio","url":"https://www.mindstudio.ai/blog/set-up-ai-model-router-llm-stack-c2610"},{"title":"Conformal Thinking: Risk Control for Reasoning on a Compute Budget","url":"https://arxiv.org/pdf/2602.03814"},{"title":"UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/html/2605.18796"},{"title":"Comparing Two-Tier and Three-Tier Data Center Networks - WWT","url":"https://www.wwt.com/article/comparing-two-tier-three-tier-data-center-networks"}]

Based on the search results, I found several relevant sources about two-tier vs three-tier systems and compute budget verification:

## LLM Routing and Cascade Systems

The search results reveal recent work on two-tier and three-tier LLM routing architectures for cost-optimal inference. Most systems benefit from having at least three tiers, with the fast tier handling simple, high-volume requests using models like GPT-3.5 Turbo and Claude Instant.

## Compute Budget Verification and Uncertainty Thresholds

On the verification and uncertainty side, a framework introduces an upper threshold that stops reasoning when the model is confident and a lower threshold that stops unsolvable instances, with distribution-free risk control to specify these stopping mechanisms. 

Additionally, setting a threshold could be trickier than setting a token budget since the threshold value often lacks interpretable meaning and could lie in arbitrary ranges.

## Cost-Optimal Routing

Recent work makes the routing score an explicitly calibrated error probability and proves when a threshold on that probability is cost-optimal, building a routing policy by extracting uncertainty scores, calibrating them to error probabilities, and selecting thresholds through constrained cost minimization.

The research indicates these approaches help optimize the tradeoff between model quality, cost, and latency in AI inference systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fa210ee-0b23-4a93-8a89-ae79f29a1439",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "f4cb7e20-95b2-482a-aff7-e23f295629e6",
  "sourceToolAssistantUUID": "4fa210ee-0b23-4a93-8a89-ae79f29a1439",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-27T22:01:30.282Z_

Excellent. Let me get more details on a few critical pieces: the UCCI paper on calibrated cascade routing, the information-theoretic impossibility result, and hidden-state uncertainty methods for LLMs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4cb7e20-95b2-482a-aff7-e23f295629e6",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpvPZ7M3P2BJ1tdzhMn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06684068-2bb1-4cb6-920e-3e64ff3a922a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrnzQesjF1JXvThKKPRCDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 12855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3160,
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

_source line 28 · 2026-05-27T22:01:31.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017SnwzexgAZQ8qz6qSYJVEo`</summary>

```json
{
  "query": "UCCI calibrated uncertainty cost-optimal LLM cascade routing 2605.18796"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06684068-2bb1-4cb6-920e-3e64ff3a922a",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpvPZ7M3P2BJ1tdzhMn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4117fc0-65a6-41ab-835f-92e427560665",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrnzQesjF1JXvThKKPRCDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 12855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3160,
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

_source line 29 · 2026-05-27T22:01:31.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FVADYBRj94Zsmc1iiyVEwu`</summary>

```json
{
  "query": "\"learned confidence calibration\" \"binary supervision\" information-theoretic impossibility 2509.14386"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4117fc0-65a6-41ab-835f-92e427560665",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpvPZ7M3P2BJ1tdzhMn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11285d02-38c8-4782-b1cf-b948d071cb9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrnzQesjF1JXvThKKPRCDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 12855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3160,
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

_source line 30 · 2026-05-27T22:01:32.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPURmRZ44vuWK6v1BbPNzB`</summary>

```json
{
  "query": "hidden state uncertainty estimation large language model probing internal representations epistemic aleatoric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11285d02-38c8-4782-b1cf-b948d071cb9c",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpvPZ7M3P2BJ1tdzhMn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1e2cdd3-5fd1-4b9d-9e93-2df3322d9693",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrnzQesjF1JXvThKKPRCDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 12855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3160,
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

_source line 31 · 2026-05-27T22:01:33.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSgoppt9Tne1JgKFSbriRU`</summary>

```json
{
  "query": "process reward model calibration overconfidence temperature scaling reasoning steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1e2cdd3-5fd1-4b9d-9e93-2df3322d9693",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpvPZ7M3P2BJ1tdzhMn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d34af9e-a4ae-42eb-867b-cbdd78e26243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrnzQesjF1JXvThKKPRCDq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 12855,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 791,
          "output_tokens": 269,
          "cache_read_input_tokens": 12855,
          "cache_creation_input_tokens": 3160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3160,
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

_source line 32 · 2026-05-27T22:01:38.406Z_

<details><summary>↩ Tool result · `toolu_01FVADYBRj94Zsmc1iiyVEwu`</summary>

```text
Web search results for query: ""learned confidence calibration" "binary supervision" information-theoretic impossibility 2509.14386"

Links: [{"title":"[2509.14386] Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility","url":"https://arxiv.org/abs/2509.14386"},{"title":"Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility","url":"https://arxiv.org/pdf/2509.14386"},{"title":"Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility","url":"https://arxiv.org/html/2509.14386v1"},{"title":"Cautious Calibration in Binary Classification","url":"https://arxiv.org/pdf/2408.05120"},{"title":"Confidence Calibration of Classifiers with Many Classes","url":"https://arxiv.org/pdf/2411.02988"},{"title":"Don't Just Blame Over-parametrization for Over-confidence: Theoretical   Analysis of Calibration in Binary Classification","url":"https://arxiv.org/pdf/2102.07856"}]

I found the paper you're looking for. Here's what the search revealed:

## Paper Summary

The paper proves a fundamental impossibility theorem: neural networks cannot simultaneously learn well-calibrated confidence estimates with meaningful diversity when trained using binary correct/incorrect supervision.

**Key Findings:**

The authors formalize this as an underspecified mapping problem where binary signals cannot distinguish between different confidence levels for correct predictions—a 60% confident correct answer receives identical supervision to a 90% confident one.

**Experimental Results:**

Their experiments reveal universal failure patterns: negative rewards produce extreme underconfidence (ECE greater than 0.8) while destroying confidence diversity (std less than 0.05), symmetric losses fail to escape binary signal averaging, and post-hoc methods achieve calibration (ECE less than 0.02) only by compressing the confidence distribution.

**Proposed Solutions:**

The authors propose novel supervision paradigms using ensemble disagreement and adaptive multi-agent learning that could overcome these fundamental limitations without requiring human confidence annotations.

The paper (arXiv:2509.14386) was submitted on September 17, 2025, by Arjun S. Nair and Kristina P. Sinaga.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11285d02-38c8-4782-b1cf-b948d071cb9c",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "a3e58cb8-8711-4a4c-822e-6879d8d8eadb",
  "sourceToolAssistantUUID": "11285d02-38c8-4782-b1cf-b948d071cb9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T22:01:38.935Z_

<details><summary>↩ Tool result · `toolu_017SnwzexgAZQ8qz6qSYJVEo`</summary>

```text
Web search results for query: "UCCI calibrated uncertainty cost-optimal LLM cascade routing 2605.18796"

Links: [{"title":"[2605.18796] UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/abs/2605.18796"},{"title":"UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/html/2605.18796"},{"title":"A Unified Approach to Routing and Cascading for LLMs","url":"https://arxiv.org/pdf/2410.10347"},{"title":"Leveraging Uncertainty Estimation for Efficient LLM Routing","url":"https://arxiv.org/pdf/2502.11021"},{"title":"Leveraging Uncertainty Estimation for Efficient LLM Routing","url":"https://arxiv.org/html/2502.11021v1"},{"title":"[2410.10347] A Unified Approach to Routing and Cascading for LLMs","url":"https://arxiv.org/abs/2410.10347"},{"title":"Quantum-Enhanced LLM Cascade Routing: A QAOA Approach to Cost-Optimal Model Selection in Multi-Agent Systems[v2] | Preprints.org","url":"https://www.preprints.org/manuscript/202604.0413"}]

I found the paper you're searching for! Here's what I found:

UCCI is a calibration-first router that maps token-level margin uncertainty to a per-query error probability via isotonic regression and selects the escalation threshold by constrained cost minimization.

The paper addresses the challenge that LLM cascades and model routing promise lower inference cost by sending easy queries to a small model and escalating hard ones to a large model, but most deployed routers use uncalibrated confidence scores and require per-workload threshold tuning.

Key results from the work include:

- Under three explicit assumptions, threshold policies on the calibrated score are cost-optimal, and isotonic calibration achieves O(n^{-1/3}) sample complexity for expected calibration error (ECE).

- On a production named entity recognition workload of 75,000 queries served by 4B and 12B instruction-tuned LLMs on H100 GPUs, UCCI cuts inference cost by 31% (95% CI: [27%, 35%]) while reducing ECE from 0.12 to 0.03.

- At the same operating point, UCCI beats entropy thresholding, split-conformal routing, and a FrugalGPT-style learned threshold.

The paper was published on arXiv in May 2026 by Varun Kotte.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4117fc0-65a6-41ab-835f-92e427560665",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "da790349-4f20-4515-8981-1a0aec052c9c",
  "sourceToolAssistantUUID": "f4117fc0-65a6-41ab-835f-92e427560665",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T22:01:40.028Z_

<details><summary>↩ Tool result · `toolu_01YPURmRZ44vuWK6v1BbPNzB`</summary>

```text
Web search results for query: "hidden state uncertainty estimation large language model probing internal representations epistemic aleatoric"

Links: [{"title":"Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models","url":"https://arxiv.org/html/2508.08139"},{"title":"Distinguishing the Knowable from the Unknowable with Language Models - Kempner Institute","url":"https://kempnerinstitute.harvard.edu/research/deeper-learning/distinguishing-the-knowable-from-the-unknowable-with-language-models/"},{"title":"[2508.08139] Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models","url":"https://arxiv.org/abs/2508.08139"},{"title":"Distinguishing the Knowable from the Unknowable with Language Models","url":"https://arxiv.org/pdf/2402.03563"},{"title":"Distinguishing the Knowable from the Unknowable with Language Models","url":"https://arxiv.org/html/2402.03563v1"},{"title":"Efficient Knowledge Probing of Large Language Models by Adapting Pre-trained Embeddings","url":"https://arxiv.org/html/2508.06030v1"},{"title":"Distinguishing the knowable from the unknowable with language models | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692092"},{"title":"Fine-Grained Uncertainty Decomposition in Large Language Models: A Spectral Approach","url":"https://arxiv.org/pdf/2509.22272"},{"title":"Mapping Clinical Doubt: Locating Linguistic Uncertainty in LLMs","url":"https://arxiv.org/pdf/2511.22402"}]

Based on the search results, here's what I found on hidden state uncertainty estimation in large language models with focus on probing internal representations and distinguishing epistemic from aleatoric uncertainty:

## Key Research Areas

**Uncertainty Decomposition in LLMs:**

Researchers are studying the feasibility of identifying epistemic uncertainty (reflecting a lack of knowledge), as opposed to aleatoric uncertainty (reflecting entropy in the underlying distribution), in the outputs of large language models over free-form text.

**Probing Internal Representations:**

Supervised linear probes trained on a language model's internal activations can achieve high accuracy at classifying epistemic versus aleatoric uncertainties, even when the probes are evaluated on unseen text domains. Notably, the fact that the linear probe performs well means that notions of epistemic uncertainty are linearly represented in the activations of LLMs.

**Practical Applications:**

Recent work computes aleatoric and epistemic uncertainty from output logits to identify salient tokens and aggregate their hidden states into compact representations for response-level reliability prediction. This approach helps detect when LLMs generate confabulations or unreliable responses.

**Advanced Methods:**

Spectral Uncertainty is a novel approach to quantifying and decomposing uncertainties in LLMs that leverages Von Neumann entropy from quantum information theory to separate total uncertainty into distinct aleatoric and epistemic components.

The research collectively demonstrates that LLMs encode information about epistemic uncertainty in their internal representations, which can be extracted through probing techniques for improved reliability estimation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1e2cdd3-5fd1-4b9d-9e93-2df3322d9693",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "9f990b14-a691-4702-a224-c71479168c10",
  "sourceToolAssistantUUID": "e1e2cdd3-5fd1-4b9d-9e93-2df3322d9693",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T22:01:40.039Z_

<details><summary>↩ Tool result · `toolu_01HSgoppt9Tne1JgKFSbriRU`</summary>

```text
Web search results for query: "process reward model calibration overconfidence temperature scaling reasoning steps"

Links: [{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/know-what-you-dont-know-uncertainty-calibration"},{"title":"Process Reward Models (PRMs): Calibration & Scaling","url":"https://www.emergentmind.com/topics/process-reward-models-prms"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/html/2506.09338v1"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://openreview.net/pdf?id=hzMkfIrdDT"},{"title":"Reward Models Lie When They Sound Certain | by Bhagya Rana | Medium","url":"https://medium.com/@bhagyarana80/reward-models-lie-when-they-sound-certain-dcff69de1a34"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"(PDF) Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://www.researchgate.net/publication/392597872_Know_What_You_Don't_Know_Uncertainty_Calibration_of_Process_Reward_Models"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"Know What You Don't Know | PRM Calibration","url":"https://young-j-park.github.io/know-what-you-dont-know/"}]

Based on the search results, here's what I found about process reward model calibration, overconfidence, temperature scaling, and reasoning steps:

## Process Reward Models and Calibration

Process reward models (PRMs) are specialized models for assigning feedback to each intermediate step in multi-step reasoning tasks performed by LLMs. Even state-of-the-art PRMs can be poorly calibrated.

## The Overconfidence Problem

PRMs tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory. Overconfidence in step-level predictions compounds into catastrophic mistakes at scale.

Early steps in a reasoning trajectory compound: one overconfident prediction leads to a second overconfident prediction, and by the time you reach the final answer, you've accumulated error upon error.

## Temperature Scaling

The simplest calibration method is temperature scaling: divide the PRM's logits by a learned scalar, then recompute probabilities. This uniformly shrinks all confidence scores. However, baseline methods like temperature scaling are effective only when every instance's prediction is consistently overestimated or underestimated.

## Advanced Calibration Approaches

Quantile regression calibration achieves lower calibration errors than standard methods such as temperature scaling, isotonic regression, or histogram binning, especially on out-of-distribution test sets. A calibration approach performed via quantile regression adjusts PRM outputs to better align with true success probabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d34af9e-a4ae-42eb-867b-cbdd78e26243",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "7117c811-879e-4ee7-993b-f9336f0e9f91",
  "sourceToolAssistantUUID": "0d34af9e-a4ae-42eb-867b-cbdd78e26243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-27T22:01:42.604Z_

Let me get one more round of targeted searches on the remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7117c811-879e-4ee7-993b-f9336f0e9f91",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpwPYPcBaZn6EbJhdWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1731f8fb-de87-462f-b4da-6fe2e6353686",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VA2SEcuv4nUJuhUdwSzUmU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 16015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4139,
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

_source line 37 · 2026-05-27T22:01:43.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWfjGqEoa64mTGTdhAgC6c`</summary>

```json
{
  "query": "\"Know What You Don't Know\" uncertainty calibration process reward model details quantile regression 2506.09338"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1731f8fb-de87-462f-b4da-6fe2e6353686",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpwPYPcBaZn6EbJhdWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "291285bf-0f6a-4fdb-bbe6-aa21b583b273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VA2SEcuv4nUJuhUdwSzUmU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 16015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4139,
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

_source line 38 · 2026-05-27T22:01:44.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Hfkrxq549LSd2K54bNn3y`</summary>

```json
{
  "query": "SNGP replace output layer reward model hidden state Gaussian process last layer uncertainty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291285bf-0f6a-4fdb-bbe6-aa21b583b273",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpwPYPcBaZn6EbJhdWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "addbe12e-17ae-40d2-a9ed-38afc1ad1e1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VA2SEcuv4nUJuhUdwSzUmU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 16015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4139,
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

_source line 39 · 2026-05-27T22:01:45.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SXZHdqJWfgYfpurZXrRhs6`</summary>

```json
{
  "query": "multi-class reward model label taxonomy correct neutral incorrect step verification PRM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "addbe12e-17ae-40d2-a9ed-38afc1ad1e1b",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpwPYPcBaZn6EbJhdWp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb3a0bdc-2870-4a7a-bc35-9798630b5d3f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VA2SEcuv4nUJuhUdwSzUmU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 16015,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 16015,
          "cache_creation_input_tokens": 4139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4139,
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

_source line 40 · 2026-05-27T22:01:50.489Z_

<details><summary>↩ Tool result · `toolu_01NWfjGqEoa64mTGTdhAgC6c`</summary>

```text
Web search results for query: ""Know What You Don't Know" uncertainty calibration process reward model details quantile regression 2506.09338"

Links: [{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"Know What You Don't Know | PRM Calibration","url":"https://young-j-park.github.io/know-what-you-dont-know/"},{"title":"(PDF) Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://www.researchgate.net/publication/392597872_Know_What_You_Don't_Know_Uncertainty_Calibration_of_Process_Reward_Models"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116598"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/know-what-you-dont-know-uncertainty-calibration"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"}]

I found the paper! Here are the key details about "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (arXiv:2506.09338):

## Overview
This paper addresses how process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), but even state-of-the-art PRMs can be poorly calibrated.

## The Problem
PRMs tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.

## The Quantile Regression Solution
The paper presents a calibration approach performed via quantile regression that adjusts PRM outputs to better align with true success probabilities. 

More specifically, the method adjusts the output dimension of the prediction head to generate multiple predictions corresponding to different quantiles (e.g., 10%, 50%, and 90%) rather than a single reward value.

Rather than learning a single correction factor, quantile regression learns the full conditional distribution of actual success rates given each PRM prediction, giving not just a corrected point estimate, but confidence bounds.

## Key Application
The calibrated success estimates and their associated confidence bounds enable an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on estimated likelihood.

The paper was authored by Young-Jin Park, Kristjan Greenewald, Kaveh Alim, Hao Wang, and Navid Azizan from MIT and MIT-IBM Watson AI Lab, and was presented at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "291285bf-0f6a-4fdb-bbe6-aa21b583b273",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "d9f9394e-2a3c-4bae-b335-10b11288b840",
  "sourceToolAssistantUUID": "291285bf-0f6a-4fdb-bbe6-aa21b583b273",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-27T22:01:50.527Z_

<details><summary>↩ Tool result · `toolu_018Hfkrxq549LSd2K54bNn3y`</summary>

```text
Web search results for query: "SNGP replace output layer reward model hidden state Gaussian process last layer uncertainty"

Links: [{"title":"uncertainty-baselines/baselines/clinc_intent/sngp.py at main · google/uncertainty-baselines","url":"https://github.com/google/uncertainty-baselines/blob/main/baselines/clinc_intent/sngp.py"},{"title":"Spectral-normalized Neural Gaussian Processes (SNGP)","url":"https://www.emergentmind.com/topics/spectral-normalized-neural-gaussian-processes-sngp"},{"title":"Uncertainty-aware Deep Learning with SNGP | TensorFlow Core","url":"https://www.tensorflow.org/tutorials/understanding/sngp"},{"title":"A Simple Approach to Improve Single-Model Deep Uncertainty via Distance-Awareness","url":"https://research.google/pubs/a-simple-approach-to-improve-single-model-deep-uncertainty-via-distance-awareness/"},{"title":"[2205.00403] A Simple Approach to Improve Single-Model Deep Uncertainty via Distance-Awareness","url":"https://ar5iv.labs.arxiv.org/html/2205.00403"},{"title":"[2205.00403v1] A Simple Approach to Improve Single-Model Deep Uncertainty via Distance-Awareness","url":"https://arxiv.org/abs/2205.00403v1"},{"title":"[2205.00403] A Simple Approach to Improve Single-Model Deep Uncertainty via Distance-Awareness","url":"https://arxiv.org/abs/2205.00403"},{"title":"A Simple Approach to Improve Single-Model Deep Uncertainty via   Distance-Awareness","url":"https://arxiv.org/pdf/2205.00403"},{"title":"GitHub - wshahbaz/uncertainty_aware_dp: Uncertainty-Aware Deep Learning with Spectral-normalized Neural Gaussian Process","url":"https://github.com/wshahbaz/uncertainty_aware_dp"},{"title":"Simple and Principled Uncertainty Estimation with Deterministic Deep   Learning via Distance Awareness","url":"https://arxiv.org/pdf/2006.10108"}]

Based on the search results, here's what I found about SNGP and replacing the output layer with a Gaussian process:

## Overview

SNGP is a method that improves the distance-awareness ability of modern DNNs with two simple changes: (1) applying spectral normalization to hidden weights to enforce bi-Lipschitz smoothness in representations and (2) replacing the last output layer with a Gaussian process layer.

## How It Works

SNGP makes two simple changes to the model: It applies spectral normalization to the hidden residual layers and replaces the Dense output layer with a Gaussian process layer.

## Implementation Details

SNGP requires only two architectural changes: spectral normalization in hidden layers, and replacement of the final layer with a random feature GP with Laplace approximation. Common hyperparameters include spectral norm bound, number of random features (typically 512–2048), and kernel amplitude/length-scale.

## Uncertainty Benefits

SNGP models combine spectral normalization in hidden layers with a Gaussian Process output to deliver distance-aware predictions and calibrated uncertainty, employing a minimax learning framework that ensures predictive uncertainty increases with distance from training data, aiding reliable out-of-distribution detection.

The search results confirm that replacing the output layer with a Gaussian process layer is a core component of SNGP, working in conjunction with spectral normalization of hidden layers to improve uncertainty quantification and distance awareness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "addbe12e-17ae-40d2-a9ed-38afc1ad1e1b",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "3876447c-0ae0-4ea5-909a-64952c7ec6ed",
  "sourceToolAssistantUUID": "addbe12e-17ae-40d2-a9ed-38afc1ad1e1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T22:01:52.726Z_

<details><summary>↩ Tool result · `toolu_01SXZHdqJWfgYfpurZXrRhs6`</summary>

```text
Web search results for query: "multi-class reward model label taxonomy correct neutral incorrect step verification PRM 2025 2026"

Links: [{"title":"Reward Modeling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/05-reward-models"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://arxiv.org/pdf/2602.09305"},{"title":"Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://arxiv.org/html/2503.13551"},{"title":"Rethinking Reward Models for Multi-Domain Test-Time Scaling","url":"https://arxiv.org/pdf/2510.00492"},{"title":"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/pdf/2505.19706"},{"title":"Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models","url":"https://arxiv.org/pdf/2506.09532"}]

Based on the search results, here's what I found about multi-class reward model label taxonomy for process reward models (PRMs):

## Label Taxonomy for PRMs

Process reward models use a 3-class label system where each step receives a label: correct (+1), neutral (0), or incorrect (-1). PRMs provide supervision only at step boundaries (e.g., newline tokens), and all other tokens are masked during training.

## Recent Developments (2025-2026)

The field has evolved significantly with several recent innovations:

**Multi-Level and Probabilistic Scoring**: Most models use a binary label at each step (correct/incorrect), though recent variants allow for multi-level or probabilistic scoring.

**Composite Step-Level Rewards**: ReasonFlux-PRM introduces a composite step-level reward that integrates three signals beyond simple correctness: a quality score from a GPT-4 judge assessing logical soundness, a coherence score for contextual compatibility between adjacent steps, and an alignment score based on semantic similarity with the final response.

**Error-Aware Hierarchical Supervision**: PathFinder-PRM is an error-aware hierarchical PRM that classifies each step to detect the presence of math or consistency errors, and combines these fine-grained error labels to produce a final reward score.

**Dataset Construction**: Supervised datasets are constructed via manual annotation, Monte Carlo completion, LLM-as-judge verifications, or adaptive search to label each reasoning step with correctness, neutrality, or error types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb3a0bdc-2870-4a7a-bc35-9798630b5d3f",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "57fb750c-12a3-40e0-97b8-f944260a425a",
  "sourceToolAssistantUUID": "eb3a0bdc-2870-4a7a-bc35-9798630b5d3f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-27T22:01:55.231Z_

Now let me get details on a couple more relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57fb750c-12a3-40e0-97b8-f944260a425a",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpxKnhTG5kMAi9riiKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "919cd44f-5571-41f7-af38-2d6c1cc0c062",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKVDtNdLqh9NJThcFC3WXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 20154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2771,
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

_source line 44 · 2026-05-27T22:01:55.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SQpmzQLBDT5NmW9XgvWckx`</summary>

```json
{
  "query": "PathFinder-PRM error-aware hierarchical process reward model error typing classification 2505.19706"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919cd44f-5571-41f7-af38-2d6c1cc0c062",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpxKnhTG5kMAi9riiKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a510280c-29ed-4021-827e-4f87982eacc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKVDtNdLqh9NJThcFC3WXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 20154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2771,
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

_source line 45 · 2026-05-27T22:01:56.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fkpw2bMLDL6Us82Ne96gBk`</summary>

```json
{
  "query": "hierarchical multi-step reward model enhanced reasoning 2503.13551 tier routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a510280c-29ed-4021-827e-4f87982eacc5",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpxKnhTG5kMAi9riiKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20eff5e2-af5d-4340-b5c2-efdc5d15ac5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKVDtNdLqh9NJThcFC3WXZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 20154,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 20154,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2771,
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

_source line 46 · 2026-05-27T22:02:02.780Z_

<details><summary>↩ Tool result · `toolu_01Fkpw2bMLDL6Us82Ne96gBk`</summary>

```text
Web search results for query: "hierarchical multi-step reward model enhanced reasoning 2503.13551 tier routing"

Links: [{"title":"[2503.13551v3] Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://arxiv.org/abs/2503.13551v3"},{"title":"[2503.13551] Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://arxiv.org/abs/2503.13551"},{"title":"Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2503.13551"},{"title":"Paper page - Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://huggingface.co/papers/2503.13551"},{"title":"Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://arxiv.org/html/2503.13551v1"},{"title":"GitHub - tengwang0318/hierarchial_reward_model: Offical Code For \"Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models\"","url":"https://github.com/tengwang0318/hierarchial_reward_model"},{"title":"dblp: Yanan Zheng","url":"https://dblp.org/pid/93/7107.html"},{"title":"TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks","url":"https://arxiv.org/pdf/2601.10245"},{"title":"Route-and-Reason: Scaling Large Language Model Reasoning with Reinforced Model Router","url":"https://arxiv.org/pdf/2506.05901"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"}]

Based on the search results, I found information about the paper arxiv 2503.13551:

## Overview

The paper proposes a Hierarchical Reward Model (HRM), which evaluates both individual and consecutive reasoning steps at both fine-grained and coarse-grained levels.

## Problem Statement

The Process Reward Model (PRM) suffers from reward hacking, making it unreliable in identifying the best intermediate step. Additionally, the cost of annotating reasoning processes for reward modeling is high, making large-scale collection of high-quality data challenging.

## Key Contributions

HRM excels at assessing multi-step reasoning coherence, especially when flawed steps are later corrected through self-reflection. 

To further reduce the cost of generating training data, the authors introduce a lightweight and effective data augmentation strategy called Hierarchical Node Compression (HNC), which merges two consecutive reasoning steps (the text was cut off in the search results).

The paper was authored by Teng Wang, Zhangyi Jiang, Zhenqi He, and others, and was submitted to arXiv on March 16, 2025.

Regarding "tier routing" specifically in the query - the search results did not return detailed information about a tier routing component in this particular paper, though they did show related work on routing strategies in other reasoning papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20eff5e2-af5d-4340-b5c2-efdc5d15ac5a",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "68fe39cf-60f9-4a4f-b4dd-fa217547284f",
  "sourceToolAssistantUUID": "20eff5e2-af5d-4340-b5c2-efdc5d15ac5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-27T22:02:04.957Z_

<details><summary>↩ Tool result · `toolu_01SQpmzQLBDT5NmW9XgvWckx`</summary>

```text
Web search results for query: "PathFinder-PRM error-aware hierarchical process reward model error typing classification 2505.19706"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Self-supervised Process Reward Model (SPRM)","url":"https://www.emergentmind.com/topics/self-supervised-process-reward-model-sprm-125c6af6-1a1e-478a-bd22-9e34fc4f589d"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"}]

Based on the search results, I found comprehensive information about PathFinder-PRM (arXiv 2505.19706):

## Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative Process Reward Model (PRM) that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## Motivation and Background

Large Language Models are prone to hallucination, especially during multi-hop and reasoning-intensive tasks such as mathematical problem solving. While Outcome Reward Models verify only final answers, Process Reward Models score each intermediate step to steer generation toward coherent solutions.

## Data and Training

To train PathFinder-PRM, the researchers constructed a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels. The labels include three dimensions: Math, Consistency, and Optimality.

## Performance Results

On PRMBench, PathFinder-PRM achieves a state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward-guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Key Innovation

The model predicts Math and Consistency labels independently in the first forward pass to prevent the Consistency prediction from being influenced by the previously generated Math label, which is a potential issue in autoregressive setups.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a510280c-29ed-4021-827e-4f87982eacc5",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "aa5982aa090e023fa",
  "type": "user",
  "uuid": "97cd7174-d130-45f3-ab8d-7050630c4385",
  "sourceToolAssistantUUID": "a510280c-29ed-4021-827e-4f87982eacc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-27T22:03:30.863Z_

I now have enough information to provide a comprehensive analysis. Here is my research synthesis:

---

## Research Findings: Binary Entropy Sufficiency for Multi-Tier PRM Routing

### 1. Binary Entropy as a Routing Signal: Fundamental Limitations

The core concern is well-founded. A binary reward head produces a single probability p(correct), and its entropy H = -p log p - (1-p) log(1-p) is capped at log(2) ~ 0.69 nats. This creates two distinct problems for 3-tier routing:

**Information-theoretic ceiling.** You are trying to carve a 1-dimensional signal (p) into 3 decision regions via two thresholds. While this is mathematically possible (e.g., p < 0.3 -> deep-verify, 0.3 <= p <= 0.7 -> standard-verify, p > 0.7 -> skip), the signal has no intrinsic structure distinguishing "uncertain because the step is ambiguous" from "uncertain because the model lacks knowledge." Binary entropy conflates epistemic and aleatoric uncertainty.

**Calibration impossibility under binary supervision.** The paper [arXiv:2509.14386](https://arxiv.org/abs/2509.14386) (Nair & Sinaga, 2025) proves that neural networks **cannot** simultaneously learn well-calibrated confidence estimates with meaningful diversity when trained with binary correct/incorrect supervision. Their experiments show that negative rewards produce extreme underconfidence (ECE > 0.8) while destroying confidence diversity (std < 0.05), and that post-hoc calibration methods (temperature scaling, Platt scaling) achieve low ECE only by compressing the confidence distribution into a narrow band -- defeating the purpose of using entropy for routing.

**PRM-specific overconfidence.** The NeurIPS 2025 paper "Know What You Don't Know" ([arXiv:2506.09338](https://arxiv.org/abs/2506.09338), Park et al., MIT/IBM) demonstrates that even state-of-the-art PRMs are poorly calibrated, systematically overestimating the probability that a partial reasoning step leads to a correct final answer. Overconfidence compounds across steps. Temperature scaling provides only uniform correction and fails when miscalibration is heterogeneous across problem difficulty. Their quantile regression approach adjusts the output head to predict multiple quantiles (e.g., 10th, 50th, 90th percentiles), giving calibrated confidence bounds -- but this effectively moves beyond binary entropy.

**Bottom line:** Raw binary entropy from a standard PRM reward head is an unreliable signal for 3-tier routing. The confidence distribution is poorly calibrated, compressed, and unable to distinguish epistemic from aleatoric uncertainty.

### 2. Hidden-State Uncertainty Methods

Several approaches extract richer uncertainty signals from the model's internal representations rather than just output logits:

**SNGP (Spectral-Normalized Neural Gaussian Processes).** Originally from [Liu et al., 2020/2022](https://arxiv.org/abs/2006.10108), SNGP makes two changes: (1) apply spectral normalization to hidden residual layers to enforce bi-Lipschitz smoothness, and (2) replace the final output layer with a random-feature Gaussian Process with Laplace approximation. This gives distance-aware predictions where uncertainty naturally increases for inputs far from training data. On both vision and NLP tasks (Wide-ResNet, BERT), SNGP matches deep ensemble performance for calibration and OOD detection at single-model cost. Typical hyperparameters: spectral norm bound ~0.95, 512-2048 random features. **This is directly applicable to your PRM**: replace the binary reward head with a GP layer, apply spectral norm to the transformer's hidden layers, and you get a continuous uncertainty signal that is richer than binary entropy -- it reflects distance in representation space from the training distribution.

**Deep Ensembles.** Training N independent PRM copies gives disagreement-based uncertainty. However, cost scales linearly (N forward passes), and ensembles can lack diversity on some distributions, limiting their effectiveness. Still, ensemble disagreement is one of the solutions proposed by [arXiv:2509.14386](https://arxiv.org/abs/2509.14386) to overcome the information-theoretic impossibility of binary supervision calibration.

**DUQ (Deterministic Uncertainty Quantification).** [Van Amersfoort et al., 2020](https://arxiv.org/abs/2003.02037) uses RBF-network-style centroid distances with a gradient penalty to ensure the model is certain only on the training distribution. DUQ matches or exceeds deep ensembles for OOD detection with a single forward pass. However, it requires maintaining per-class centroids and is less naturally suited to sequence-level tasks.

**Linear probing of hidden states.** [Kadavath et al., 2022; Chen et al., 2024](https://arxiv.org/abs/2402.03563) show that supervised linear probes on LLM internal activations can classify epistemic vs. aleatoric uncertainty with high accuracy, and this transfers across domains. The key finding is that **epistemic uncertainty is linearly represented in LLM activations**. For your PRM, this means you could train a lightweight probe on the hidden state at step boundaries to get a 2D uncertainty signal (epistemic + aleatoric) rather than 1D binary entropy.

**Recommendation for your setting:** SNGP is the strongest single-model approach. Replace the binary reward head with a GP output layer and add spectral normalization to the transformer backbone. This gives you a continuous uncertainty measure grounded in representation-space distance, providing a much richer signal for 3-tier routing than binary entropy alone.

### 3. Multi-Class Reformulation of the Reward Head

The literature already supports moving beyond binary labels:

**Existing 3-class PRMs.** The standard PRM800K labeling scheme already uses 3 classes: correct (+1), neutral (0), incorrect (-1). Neutral captures steps that are neither clearly right nor wrong. Many PRM implementations collapse this to binary for training, but the annotation infrastructure for 3-class already exists.

**PathFinder-PRM** ([arXiv:2505.19706](https://arxiv.org/abs/2505.19706)) goes further with a hierarchical, multi-dimensional reward head that classifies each step along three axes: Math correctness, Consistency with prior steps, and Optimality. It achieves SOTA PRMScore of 67.7 on PRMBench with 3x less data than prior best. This demonstrates that **richer label taxonomies improve PRM performance**, not just routing.

**ReasonFlux-PRM** uses a composite step-level reward integrating quality (logical soundness), coherence (contextual compatibility), and alignment (semantic similarity) scores.

**Proposed reformulation for your case:** A 4-class reward head {correct, partially-correct, incorrect, uncertain} would naturally map to 3 routing tiers:
- High p(correct) -> Tier 1 (skip/lightweight check)
- High p(partially-correct) or p(uncertain) -> Tier 2 (standard verification)  
- High p(incorrect) -> Tier 3 (deep verification)

The entropy of a 4-class head has a ceiling of log(4) ~ 1.39 nats -- double the binary case -- giving substantially more routing resolution. However, this requires relabeling training data, which is nontrivial. The PathFinder-PRM approach of using LLM-generated multi-dimensional labels is a practical path.

### 4. EDU-PRM Entropy Usage (arXiv:2503.22233)

EDU-PRM uses entropy in a fundamentally different way than what you're considering:

**What EDU-PRM does:** It computes **token-level predictive entropy** from the language model's next-token distribution (not from the reward head) to identify step boundaries. High-entropy tokens mark logical transition points where the reasoning branches. At each such "branch point," it spawns two decoding paths using top-1 and top-2 logits, then continues with greedy decoding until the next high-entropy point.

**What it does NOT do:** EDU-PRM does not use entropy for routing or verification tier selection. It uses entropy purely for step segmentation. The reward labels themselves are **binary** (correct=1, incorrect=0) assigned via Monte Carlo estimation of whether each fragment leads to a correct final answer. The model is trained with standard binary cross-entropy loss.

**Key insight for your work:** EDU-PRM's entropy is the **language model's** next-token entropy (which can be very high -- log(V) for vocabulary V of ~100K tokens), not the reward head's binary entropy. This is a much richer signal. You could adapt this idea: use the LM's token-level entropy at step boundaries as an auxiliary routing signal alongside the reward head's output. Steps where the LM itself is uncertain about what comes next are natural candidates for deeper verification.

### 5. Two-Tier vs. Three-Tier Routing

**The case for 2 tiers with binary entropy:**
- The UCCI paper ([arXiv:2605.18796](https://arxiv.org/abs/2605.18796), Kotte, May 2026) proves that under mild assumptions, threshold policies on a calibrated scalar score are **cost-optimal** for 2-tier cascade routing. Using isotonic regression to calibrate margin uncertainty to error probability, UCCI cuts inference cost by 31% on production workloads while reducing ECE from 0.12 to 0.03. It outperforms entropy thresholding, conformal routing, and learned thresholds.
- Binary entropy naturally supports exactly one threshold -> two tiers.
- Calibrating a single threshold is empirically robust; calibrating two thresholds for 3 tiers compounds calibration error.

**The case for 3 tiers with a richer signal:**
- Adaptive test-time compute work ([arXiv:2602.03975](https://arxiv.org/pdf/2602.03975)) shows that multi-tier allocation with upper and lower thresholds can achieve higher accuracy with 44% fewer verifier calls than best-of-N.
- The quantile regression approach from Park et al. provides calibrated confidence bounds that naturally define three regions: below lower quantile (deep verify), between quantiles (standard verify), above upper quantile (skip).
- PathFinder-PRM's multi-dimensional reward signal gives enough information for fine-grained routing.

### Recommendation

**If you keep the binary reward head as-is:** Simplify to 2 tiers. Use UCCI-style isotonic calibration to map the reward score to a calibrated error probability, set a single cost-optimal threshold, and route to either skip or deep-verify. This is theoretically grounded (provably cost-optimal under stated assumptions), practically robust, and avoids the calibration pathologies documented for binary classifiers.

**If you want 3 tiers (recommended for best performance):** Do not rely on binary entropy alone. Instead:
1. **Minimal change:** Add an SNGP-style GP output layer to the PRM, replacing the binary head. Apply spectral normalization to the transformer backbone. The GP's predictive variance gives a second axis of uncertainty orthogonal to the predicted correctness score, enabling natural 3-way routing: (high confidence correct -> skip), (high variance/uncertain -> standard verify), (high confidence incorrect -> deep verify).
2. **Moderate change:** Train a linear probe on the PRM's hidden state at step boundaries to decompose uncertainty into epistemic and aleatoric components. Route based on both dimensions.
3. **Larger change:** Reformulate as a multi-class head (correct/neutral/incorrect) following PathFinder-PRM's approach with error-type-aware labels. This gives log(3) ~ 1.1 nats of entropy ceiling and a natural 3-way mapping.

The SNGP approach (option 1) offers the best cost-benefit tradeoff: it requires no relabeling, adds negligible inference cost (single forward pass), and provides a principled 2D uncertainty signal (predicted class + distance-based uncertainty) sufficient for 3-tier routing.

---

**Sources:**

- [EDU-PRM: Process Reward Modeling with Entropy-Driven Uncertainty](https://arxiv.org/abs/2503.22233)
- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Disproving Feasibility of Learned Confidence Calibration Under Binary Supervision](https://arxiv.org/abs/2509.14386)
- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)
- [SNGP: Simple and Principled Uncertainty Estimation with Distance Awareness](https://arxiv.org/abs/2006.10108)
- [DUQ: Uncertainty Estimation Using a Single Deep Deterministic Neural Network](https://arxiv.org/abs/2003.02037)
- [PathFinder-PRM: Error Typing for Smarter Rewards](https://arxiv.org/abs/2505.19706)
- [Hierarchical Multi-Step Reward Models for Enhanced Reasoning](https://arxiv.org/abs/2503.13551)
- [Distinguishing the Knowable from the Unknowable with Language Models](https://arxiv.org/abs/2402.03563)
- [Adaptive Test-Time Compute Allocation via Learned Heuristics](https://arxiv.org/abs/2602.03975)
- [AIRI Uncertainty Transformers (SNGP for NLP)](https://github.com/airi-institute/uncertainty_transformers)
- [Leveraging Uncertainty Estimation for Efficient LLM Routing](https://arxiv.org/abs/2502.11021)
- [Conformal Thinking: Risk Control for Reasoning on a Compute Budget](https://arxiv.org/abs/2602.03814)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97cd7174-d130-45f3-ab8d-7050630c4385",
  "isSidechain": true,
  "agentId": "aa5982aa090e023fa",
  "requestId": "req_011CbTpyE4BzwQh6jdLU8JGT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e07f0d77-6c58-4797-a4dc-497c6f32da48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHd3cWPnMrqN7J3USs5mE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 22925,
      "output_tokens": 3349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 837,
          "output_tokens": 3349,
          "cache_read_input_tokens": 22925,
          "cache_creation_input_tokens": 1022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1022,
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
