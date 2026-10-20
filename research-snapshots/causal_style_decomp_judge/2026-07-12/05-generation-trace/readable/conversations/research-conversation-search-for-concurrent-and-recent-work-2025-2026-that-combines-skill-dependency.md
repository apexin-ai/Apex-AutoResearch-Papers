# Research conversation: Search for concurrent and recent work (2025-2026) that combines skill dependency DAGs with compositional generalization 

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad1c78f8837ce5d3d.jsonl`
- **Structured JSON:** [`4669d6cc282c9245c493.json`](../../sessions/46/4669d6cc282c9245c493.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-29T05:54:59.666Z_

Search for concurrent and recent work (2025-2026) that combines skill dependency DAGs with compositional generalization in mathematical reasoning. I need to confirm no one is already doing this exact thing.

Perform these searches:
1. Web search: "skill DAG compositional generalization math reasoning 2026"
2. Web search: "compositional math reasoning skill graph data synthesis 2026 arxiv"
3. Web search: "OMEGA benchmark compositional ceiling targeted data 2026"
4. Web search: "skill taxonomy guided synthesis mathematical reasoning arxiv 2026"
5. Web search: "MASS skill graph STEPS structural entropy math 2026"
6. Web search on OpenReview: "site:openreview.net compositional mathematical reasoning skill graph 2026"

For each search, report what you find. If you find any paper that is doing substantially the same thing (using directed skill DAGs to identify compositional gaps and synthesize targeted multi-skill math training data), flag it prominently.

Report concisely: list any relevant concurrent work with title, venue, date, and a 1-sentence summary of how it relates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "51f315f7-592c-4630-a109-4334eb698dd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:54:59.670Z_

```json
{
  "parentUuid": "51f315f7-592c-4630-a109-4334eb698dd7",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
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
  "uuid": "f6072f1c-38e0-4d69-af14-6e1f374e2a77",
  "timestamp": "2026-05-29T05:54:59.670Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:54:59.671Z_

```json
{
  "parentUuid": "f6072f1c-38e0-4d69-af14-6e1f374e2a77",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "708cc0e9-8d19-436f-b5f3-92b0327d7cbd",
  "timestamp": "2026-05-29T05:54:59.671Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:55:02.014Z_



I'll load the WebSearch tool first, then run all searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "708cc0e9-8d19-436f-b5f3-92b0327d7cbd",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqmFh1ARpsAPA9u7CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "684a1a07-d05e-4edc-a09f-8c549abbe6d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkrZNnbehSN2KigMsbrCty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8996,
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

_source line 5 · 2026-05-29T05:55:02.564Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AitsTejAdSVGJQsGmfBA5p`</summary>

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
  "parentUuid": "684a1a07-d05e-4edc-a09f-8c549abbe6d5",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqmFh1ARpsAPA9u7CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfa46124-153b-48b9-b2e6-cd78252f10b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkrZNnbehSN2KigMsbrCty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8996,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8996,
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

_source line 6 · 2026-05-29T05:55:02.570Z_

<details><summary>↩ Tool result · `toolu_01AitsTejAdSVGJQsGmfBA5p`</summary>

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
  "parentUuid": "bfa46124-153b-48b9-b2e6-cd78252f10b4",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "16c87d15-c78c-4954-ac07-f250cb60fd7a",
  "sourceToolAssistantUUID": "bfa46124-153b-48b9-b2e6-cd78252f10b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:55:04.381Z_



Now I'll run all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c87d15-c78c-4954-ac07-f250cb60fd7a",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b583eaa2-f3cd-48a9-8fcf-4750d6e0911d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 8 · 2026-05-29T05:55:04.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179Rr6SyJ3ZnxdKSGWq2dcW`</summary>

```json
{
  "query": "skill DAG compositional generalization math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b583eaa2-f3cd-48a9-8fcf-4750d6e0911d",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea2c52e2-fc4e-4fbd-850a-070bf0a6cdaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 9 · 2026-05-29T05:55:05.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UJg5xLUVpgnQxNXcNgWFXL`</summary>

```json
{
  "query": "compositional math reasoning skill graph data synthesis 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea2c52e2-fc4e-4fbd-850a-070bf0a6cdaa",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b94f5228-5e1e-446d-a79b-88e994ba8b88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 10 · 2026-05-29T05:55:05.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCBpLcnmrCzTQSuG3VbWc7`</summary>

```json
{
  "query": "OMEGA benchmark compositional ceiling targeted data 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b94f5228-5e1e-446d-a79b-88e994ba8b88",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b285654-a4d7-4f93-871d-164c3267bba7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 11 · 2026-05-29T05:55:05.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L7d1ZYwRc8t6tbsEkunUK2`</summary>

```json
{
  "query": "skill taxonomy guided synthesis mathematical reasoning arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b285654-a4d7-4f93-871d-164c3267bba7",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edb0ae1d-4eb6-43fe-b241-cd3ee0fbb0fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 12 · 2026-05-29T05:55:06.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FqkDAqxMpfYnviVw4LjBk7`</summary>

```json
{
  "query": "MASS skill graph STEPS structural entropy math 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edb0ae1d-4eb6-43fe-b241-cd3ee0fbb0fe",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7ed8956-f3b7-4596-a184-b1defb0f5aa5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 13 · 2026-05-29T05:55:06.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DvwceqsyZTB21jv7ezSkfW`</summary>

```json
{
  "query": "site:openreview.net compositional mathematical reasoning skill graph 2026",
  "allowed_domains": [
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7ed8956-f3b7-4596-a184-b1defb0f5aa5",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLqzKFU6qvN8gNmMcSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "647020df-d35d-4304-9072-0b477792971e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Z6sWK652guP1CzDxLxSk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 8996,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 623
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 8996,
          "cache_creation_input_tokens": 623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 623,
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

_source line 14 · 2026-05-29T05:55:12.003Z_

<details><summary>↩ Tool result · `toolu_0179Rr6SyJ3ZnxdKSGWq2dcW`</summary>

```text
Web search results for query: "skill DAG compositional generalization math reasoning 2026"

Links: [{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang*","url":"https://arxiv.org/pdf/2510.19842"},{"title":"OMEGA: Can LLMs reason outside the box in math? | Ai2","url":"https://allenai.org/blog/omega"},{"title":"On the Interplay of Pre-Training, Mid-Training, and RL on ...","url":"https://arxiv.org/pdf/2512.07783"},{"title":"Compositional Generalization by Learning Analytical Expressions","url":"https://arxiv.org/pdf/2006.10627"},{"title":"Improving Compositional Generalization in Math Word Problem Solving","url":"https://arxiv.org/pdf/2209.01352"},{"title":"Laying the Foundation First? Investigating the Generalization from   Atomic Skills to Complex Reasoning Tasks","url":"https://arxiv.org/pdf/2403.09479"}]

I found several relevant research papers on the intersection of skill DAGs, compositional generalization, and math reasoning. Here are the key findings:

## Recent Research on Skill DAGs and Compositional Generalization

**DAG-Based Mathematical Reasoning:**
Research uses DAG representations (directed acyclic graphs with node and edge sets) for structuring mathematical reasoning in LLMs. DAGs are treated as symbolic reasoning graphs whose structure is shared across different numerical instantiations and linguistic realizations.

**The Compositional Generalization Challenge:**
While models show strong performance on isolated skills, they have limited compositional generalization—for example, when asked to compute the GCD of two numbers and then use that result within a polynomial root-finding subproblem, performance drops sharply, and models fail to integrate skills effectively despite mastering both components individually.

Research investigating whether atomic skills generalize to complex reasoning tasks found that atomic skills cannot spontaneously generalize to compositional tasks, though hierarchical curriculum learning strategies have been proposed to achieve better skill generalization.

**Addressing the Gap:**
Methods propose iterative data augmentation that includes diverse compositional variation into training data to improve compositional generalization in math word problem solving.

These findings indicate that while DAG structures and skill-based approaches show promise for mathematical reasoning, significant challenges remain in achieving true compositional generalization across skill boundaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea2c52e2-fc4e-4fbd-850a-070bf0a6cdaa",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "e398b0cf-027e-4bb0-8af5-750f3b051dac",
  "sourceToolAssistantUUID": "ea2c52e2-fc4e-4fbd-850a-070bf0a6cdaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-29T05:55:12.390Z_

<details><summary>↩ Tool result · `toolu_01DvwceqsyZTB21jv7ezSkfW`</summary>

```text
Web search results for query: "site:openreview.net compositional mathematical reasoning skill graph 2026"

Links: [{"title":"MemoGraph: Augmenting LLMs with Explicit Episodic Memory for Multi-step Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=HaCqQlEjCN"},{"title":"The Power of Power Law: Asymmetry Enables Compositional Reasoning | OpenReview","url":"https://openreview.net/forum?id=70fuQSzSfZ"},{"title":"Not All LLM Reasoners Are Created Equal | OpenReview","url":"https://openreview.net/forum?id=RcqAmkDJfI"},{"title":"Exploring the Compositional Deficiency of Large Language Models in   Mathematical Reasoning","url":"https://arxiv.org/pdf/2405.06680"},{"title":"The Mystery of Compositional Generalization in Graph-based Generative   Commonsense Reasoning","url":"https://arxiv.org/pdf/2410.06272"},{"title":"MODELING COMPLEX MATHEMATICAL REASONING","url":"https://openreview.net/pdf?id=Ge7ZqrKG9t"},{"title":"Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning","url":"https://arxiv.org/pdf/2601.15160"},{"title":"Ineq-Comp: Benchmarking Human-Intuitive Compositional Reasoning in Automated Theorem Proving on Inequalities","url":"https://arxiv.org/pdf/2505.12680"}]

Based on the search results from OpenReview, here are the relevant papers found:

1. **"The Power of Power Law: Asymmetry Enables Compositional Reasoning"** - This paper, published in March 2026 at the LIT Workshop @ ICLR 2026, examines how natural language data follows a power-law distribution, and finds that across compositional reasoning tasks like state tracking and multi-step arithmetic, training under power-law distributions outperforms training under uniform distributions.

2. **"MemoGraph: Augmenting LLMs with Explicit Episodic Memory for Multi-step Mathematical Reasoning"** - Published in March 2026 for ICLR 2026, this paper proposes MemoGraph, a neuro-symbolic framework that augments LLMs with an explicit episodic memory layer. The framework formulates reasoning as the dynamic maintenance of a heterogeneous graph.

These papers address compositional mathematical reasoning using different approaches—one focusing on data distribution effects on skill composition, and another using graph-based episodic memory for multi-step mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "647020df-d35d-4304-9072-0b477792971e",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "c0e11d90-4948-4daf-a9c3-e300b599cb92",
  "sourceToolAssistantUUID": "647020df-d35d-4304-9072-0b477792971e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T05:55:12.828Z_

<details><summary>↩ Tool result · `toolu_01FqkDAqxMpfYnviVw4LjBk7`</summary>

```text
Web search results for query: "MASS skill graph STEPS structural entropy math 2026"

Links: [{"title":"Incremental measurement of structural entropy for dynamic graphs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0004370224001115"},{"title":"Degree-Based Graph Entropy in Structure–Property Modeling","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10379043/"},{"title":"Incremental measurement of structural entropy for dynamic graphs | Artificial Intelligence","url":"https://dl.acm.org/doi/10.1016/j.artint.2024.104175"},{"title":"SE-GSL: A General and Effective Graph Structure Learning Framework   through Structural Entropy Optimization","url":"https://arxiv.org/pdf/2303.09778"},{"title":"Incremental Measurement of Structural Entropy for Dynamic Graphs","url":"https://arxiv.org/html/2207.12653"},{"title":"Structural Entropy of the Stochastic Block Models","url":"https://arxiv.org/pdf/2111.12871"}]

Based on the web search results, I found information related to structural entropy and graph theory, though the specific combination of "MASS skill graph STEPS" didn't return a single unified result. Here's what I found:

The computation of structural entropy consists of three steps: encoding tree construction, node structural entropy calculation, and total structural entropy calculation.

Structural entropy is a metric that measures the amount of information embedded in graph structure data under a strategy of hierarchical abstracting.

The search results primarily contain recent academic papers on structural entropy in dynamic graphs and graph structure learning frameworks. A novel incremental measurement framework called Incre-2dSE dynamically adjusts the community partitioning and efficiently computes the updated structural entropy for each updated graph.

If you're looking for more specific information about a particular paper or concept combining "MASS," "skill graph," and "STEPS" with structural entropy mathematics, you may need to provide additional context, as the search results focused on the structural entropy component but didn't identify the exact specific framework you're referencing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7ed8956-f3b7-4596-a184-b1defb0f5aa5",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "8a44cd20-0e9c-4795-824f-954335211c16",
  "sourceToolAssistantUUID": "c7ed8956-f3b7-4596-a184-b1defb0f5aa5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T05:55:13.004Z_

<details><summary>↩ Tool result · `toolu_01QCBpLcnmrCzTQSuG3VbWc7`</summary>

```text
Web search results for query: "OMEGA benchmark compositional ceiling targeted data 2026"

Links: [{"title":"OMEGA Benchmark","url":"https://www.emergentmind.com/topics/omega-benchmark"},{"title":"OMEGA: Can LLMs Reason Outside the Box in Math? Evaluating Exploratory, Compositional, and Transformative Generalization","url":"https://arxiv.org/pdf/2506.18880"},{"title":"Commonly used compositional data analysis implementations are not advantageous in microbial differential abundance analyses benchmarked against biological ground truth","url":"https://www.biorxiv.org/content/10.1101/2025.02.13.638109.full.pdf"},{"title":"WitChi: Efficient Detection and Pruning of Compositional Bias in Phylogenomic Alignments Using Empirical Chi-Squared Testing","url":"https://www.biorxiv.org/content/10.1101/2025.07.14.663642.full.pdf"},{"title":"Method and system for detecting targets known up to a simplex from multi-spectral and hyper-spectral imagery employing the normal compositional model","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6958466"}]

Based on the search results, I found information about the OMEGA benchmark:

OMEGA delineates three distinct axes of out-of-distribution generalization—exploratory, compositional, and transformative—and offers a unified experimental framework across six core mathematical domains.

Regarding compositional generalization specifically, the benchmark assesses if LLMs can integrate skills learned in isolation, such as solving problems requiring the combined use of previously isolated skills in new mathematical compositions that are absent from the training distribution.

The benchmark exposes persistent limitations of state-of-the-art LLMs in moving beyond mechanical proficiency toward genuinely novel mathematical reasoning, while providing a foundation for targeted model development. OMEGA was created to address the empirical observation that even the highest-performing LLMs display sharp performance drops when encountering problems beyond the scope of their training distribution.

The search results indicate this is recent research on LLM generalization capabilities, though the specific "compositional ceiling targeted data" metrics for 2026 were not detailed in these particular results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b285654-a4d7-4f93-871d-164c3267bba7",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "404b8052-1fa6-4fa3-aaf8-c4d665e9f075",
  "sourceToolAssistantUUID": "9b285654-a4d7-4f93-871d-164c3267bba7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T05:55:15.117Z_

<details><summary>↩ Tool result · `toolu_01L7d1ZYwRc8t6tbsEkunUK2`</summary>

```text
Web search results for query: "skill taxonomy guided synthesis mathematical reasoning arxiv 2026"

Links: [{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676"},{"title":"Under review as a conference paper at ICLR 2026 BASE MODELS KNOW HOW TO REASON,","url":"https://arxiv.org/pdf/2510.07364"},{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/pdf/2602.03279"},{"title":"Key-Point-Driven Data Synthesis with its Enhancement on Mathematical   Reasoning","url":"https://arxiv.org/pdf/2403.02333"}]

Based on the search results, I found a highly relevant paper matching your query:

**"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis"**

The paper proposes STEPS, a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework for generating compositionally challenging data. It addresses the challenge that Large Language Models and agent-based systems often struggle with compositional generalization due to a data bottleneck in which complex skill combinations follow a long-tailed, power-law distribution.

STEPS explicitly targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

Experiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations.

The paper was submitted to arXiv on January 7, 2026 (arXiv ID: 2601.03676).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edb0ae1d-4eb6-43fe-b241-cd3ee0fbb0fe",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "a54bfdcf-7871-4b98-ae33-25e6ec544581",
  "sourceToolAssistantUUID": "edb0ae1d-4eb6-43fe-b241-cd3ee0fbb0fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T05:55:18.426Z_

<details><summary>↩ Tool result · `toolu_01UJg5xLUVpgnQxNXcNgWFXL`</summary>

```text
Web search results for query: "compositional math reasoning skill graph data synthesis 2026 arxiv"

Links: [{"title":"[2602.03279] Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/abs/2602.03279"},{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676"},{"title":"RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis based on Structured Function Library","url":"https://arxiv.org/pdf/2504.20426"},{"title":"[2412.08864] GRIP: A Graph-Based Reasoning Instruction Producer","url":"https://arxiv.org/abs/2412.08864"},{"title":"A Graph-Based Synthetic Data Pipeline for Scaling High-Quality Reasoning Instructions","url":"https://arxiv.org/html/2412.08864v1"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/pdf/2602.03279"}]

Based on the search results, I found several relevant arxiv papers from 2026 related to compositional math reasoning, skill synthesis, and data generation:

## Key Papers Found:

**1. "Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis"** (arXiv:2602.03279, February 3, 2026)

This paper proposes a framework that models problem synthesis as a goal-driven sequential decision process where a specialized agent dynamically selects and composes modular reasoning skills, developing the Agentic-Proposer-4B using Multi-Granularity Policy Optimization (MGPO) to generate high-precision, verifiable training trajectories across mathematics, coding, and science. A 30B solver trained on only 11,000 synthesized trajectories achieves a state-of-the-art 91.6% accuracy on AIME25, rivaling frontier-scale proprietary models such as GPT-5.

**2. "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis"** (arXiv:2601.03676, January 7, 2026)

This paper proposes STEPS, a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework for generating compositionally challenging data that targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

Both papers directly address compositional math reasoning with skill-based approaches and synthetic data generation in early 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b94f5228-5e1e-446d-a79b-88e994ba8b88",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "32e86905-ce69-40fe-bd8c-bfe8bb43ff96",
  "sourceToolAssistantUUID": "b94f5228-5e1e-446d-a79b-88e994ba8b88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-29T05:55:33.554Z_

Let me run a few more targeted searches to dig deeper into the most relevant hit (STEPS/arXiv:2601.03676) and check for any other close matches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e86905-ce69-40fe-bd8c-bfe8bb43ff96",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLs9YAYYG6Fmj3puoC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d247a2a-8583-4058-a197-732f5f5f4023",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MW8Bkk8bkx361hjz5AyB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 9619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 21 · 2026-05-29T05:55:34.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Zjk9Ls364ShyAZYiU6x97`</summary>

```json
{
  "query": "arXiv 2601.03676 STEPS skill taxonomy compositional generalization math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d247a2a-8583-4058-a197-732f5f5f4023",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLs9YAYYG6Fmj3puoC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19ac5cb9-407b-47b3-a87f-28ef36b2c2cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MW8Bkk8bkx361hjz5AyB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 9619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 22 · 2026-05-29T05:55:35.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DzFeatRGT7kZjUP4ZyNfVK`</summary>

```json
{
  "query": "DAG-Math directed acyclic graph mathematical reasoning LLM skill composition training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ac5cb9-407b-47b3-a87f-28ef36b2c2cf",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLs9YAYYG6Fmj3puoC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee002ebb-b635-4606-afc7-2198bdbe0cfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MW8Bkk8bkx361hjz5AyB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 9619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 23 · 2026-05-29T05:55:35.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QA1opJND62aQuLKRDG8Xbt`</summary>

```json
{
  "query": "\"compositional gap\" \"skill dependency\" mathematical reasoning data augmentation arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee002ebb-b635-4606-afc7-2198bdbe0cfc",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLs9YAYYG6Fmj3puoC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1d5861c-0c2c-4642-aa19-68baa03eff82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MW8Bkk8bkx361hjz5AyB3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 9619,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2406,
          "output_tokens": 217,
          "cache_read_input_tokens": 9619,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1761,
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

_source line 24 · 2026-05-29T05:55:42.750Z_

<details><summary>↩ Tool result · `toolu_01DzFeatRGT7kZjUP4ZyNfVK`</summary>

```text
Web search results for query: "DAG-Math directed acyclic graph mathematical reasoning LLM skill composition training data"

Links: [{"title":"DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs | OpenReview","url":"https://openreview.net/forum?id=ylr6WArKQN"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang*","url":"https://arxiv.org/pdf/2510.19842"},{"title":"DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842"},{"title":"[2510.19842] DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2510.19842"},{"title":"NeurIPS DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://neurips.cc/virtual/2025/131173"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang1,","url":"https://openreview.net/pdf?id=Z9V81Q3FH4"},{"title":"S-DAG: A Subject-Based Directed Acyclic Graph for Multi-Agent Heterogeneous","url":"https://arxiv.org/pdf/2511.06727"}]

Based on the search results, here's what I found about DAG-Math:

## Overview

DAG-Math proposes modeling Chain-of-Thought (CoT) as a rule-based stochastic process over directed acyclic graphs (DAGs), where nodes represent intermediate derivation states and edges encode rule applications.

## Key Components

**Purpose**: The approach addresses whether LLMs' strong performance on mathematical problems stems from search, rote procedures, or rule-consistent reasoning.

**Evaluation Metric**: The framework introduces logical closeness, a metric that quantifies how well a model's CoT trajectory adheres to the DAG structure, providing evaluation beyond classical PASS@k metrics.

**Framework Structure**: Phase 1 constructs a task-specific DAG as the search space for generating CoT trajectories, and in Phase 2, the LLM generates CoT trajectories over this DAG under certain stochastic transition rules.

## Benchmark and Training

The DAG-MATH CoT format and a benchmark were constructed to guide LLMs to generate CoT trajectories in this format, thereby enabling the evaluation of their reasoning ability under the framework.

The research appears to be recent, with the work being presented at NeurIPS 2025 and published on arXiv in October 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee002ebb-b635-4606-afc7-2198bdbe0cfc",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "3dd93bed-49c3-4ba2-b765-87bf95291525",
  "sourceToolAssistantUUID": "ee002ebb-b635-4606-afc7-2198bdbe0cfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-29T05:55:43.891Z_

<details><summary>↩ Tool result · `toolu_01QA1opJND62aQuLKRDG8Xbt`</summary>

```text
Web search results for query: ""compositional gap" "skill dependency" mathematical reasoning data augmentation arxiv 2025 2026"

Links: [{"title":"MuggleMath: Assessing the Impact of Query and Response Augmentation on   Math Reasoning","url":"https://arxiv.org/pdf/2310.05506"},{"title":"Exploring the Compositional Deficiency of Large Language Models in   Mathematical Reasoning","url":"https://arxiv.org/pdf/2405.06680"},{"title":"Simple and effective data augmentation for compositional generalization","url":"https://arxiv.org/pdf/2401.09815"},{"title":"[2508.19988] AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios","url":"https://arxiv.org/abs/2508.19988"},{"title":"Learn Beyond The Answer: Training Language Models with Reflection for   Mathematical Reasoning","url":"https://arxiv.org/pdf/2406.12050"},{"title":"Improving Compositional Generalization in Math Word Problem Solving","url":"https://arxiv.org/pdf/2209.01352"},{"title":"Unveiling the Compositional Ability Gap in Vision-Language Reasoning Model","url":"https://arxiv.org/pdf/2505.19406"}]

I found several relevant papers from arXiv related to your search query. Here are the most relevant results:

1. **AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios** (March 2026)
   - LLMs can usually solve both steps in isolation, yet their accuracy drops by ~30% on average when the two are combined, indicating a compositional gap. The work examines neuron patterns, attention maps and membership inference to understand the performance gap, underscoring model brittleness in mixed-type compositional reasoning.

2. **Exploring the Compositional Deficiency of Large Language Models in Mathematical Reasoning** (2024)
   - The work introduces a MATH-TRAP dataset by introducing carefully designed logical traps into original problems, creating 'unseen problems' that cannot be solved by simply following seen reasoning paths.

3. **Improving Compositional Generalization in Math Word Problem Solving** 
   - Proposes an iterative data augmentation method to improve compositional generalization, with the largest increase of 15.6 percentage points.

4. **Unveiling the Compositional Ability Gap in Vision-Language Reasoning Model** (May 2025)
   - Designs diagnostic tasks training models on isolated reasoning skills and evaluates on compositional variants requiring skill integration, finding that models struggle with compositional generalization under cross-modal and cross-task scenarios.

5. **MuggleMath: Assessing the Impact of Query and Response Augmentation on Math Reasoning**
   - Involves augmenting new mathematical problems and answers, followed by supervised fine-tuning on the augmented dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1d5861c-0c2c-4642-aa19-68baa03eff82",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "4f3d8751-fc71-4405-a477-4667c82ec998",
  "sourceToolAssistantUUID": "c1d5861c-0c2c-4642-aa19-68baa03eff82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T05:55:44.659Z_

<details><summary>↩ Tool result · `toolu_011Zjk9Ls364ShyAZYiU6x97`</summary>

```text
Web search results for query: "arXiv 2601.03676 STEPS skill taxonomy compositional generalization math"

Links: [{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"},{"title":"Paper page - Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://huggingface.co/papers/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676v1"},{"title":"GitHub - weiyifan1023/STEPS: Code and Data for Paper \"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis\"","url":"https://github.com/weiyifan1023/STEPS"},{"title":"Improving Compositional Generalization in Math Word Problem Solving","url":"https://arxiv.org/pdf/2209.01352"}]

Based on the search results, here's what I found about arXiv paper 2601.03676:

**Title:** Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis

**Authors:** Yifan Wei, Li Du, Xiaoyan Yu, Yang Feng, and Angsheng Li

**Publication Date:** January 7, 2026

**Overview:** The paper addresses a challenge where Large Language Models and agent-based systems struggle with compositional generalization due to a data bottleneck where complex skill combinations follow a long-tailed, power-law distribution. The authors propose STEPS, a Skill Taxonomy-guided Entropy-based Posttraining data Synthesis framework for generating compositionally challenging data.

**Key Approach:** STEPS targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. It then formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

**Results:** Experiments on challenging instruction-following benchmarks show that STEPS outperforms existing data synthesis baselines, while also yielding improved compositional generalization in downstream agent-based evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ac5cb9-407b-47b3-a87f-28ef36b2c2cf",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "68b1d88f-80bb-4ce4-abac-352fef986553",
  "sourceToolAssistantUUID": "19ac5cb9-407b-47b3-a87f-28ef36b2c2cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T05:55:50.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JYyhToRRabL2odSvpUqYAK`</summary>

```json
{
  "query": "STEPS arXiv 2601.03676 \"skill taxonomy\" \"directed acyclic graph\" OR \"DAG\" math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68b1d88f-80bb-4ce4-abac-352fef986553",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLu5fJr9BH4mC5gKG1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4fcdfc7-b537-4654-9138-2654fe982cb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESAscQogXVDnMYymx2pa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1468,
      "cache_creation_input_tokens": 3276,
      "cache_read_input_tokens": 11380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3276,
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

_source line 28 · 2026-05-29T05:55:51.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013rpmgkSMcnMxssbfyFtVeN`</summary>

```json
{
  "query": "GRIP graph reasoning instruction producer skill dependency math training data synthesis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4fcdfc7-b537-4654-9138-2654fe982cb9",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLu5fJr9BH4mC5gKG1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c3aaae6-7166-460e-a665-f2aeb602753b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESAscQogXVDnMYymx2pa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1468,
      "cache_creation_input_tokens": 3276,
      "cache_read_input_tokens": 11380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3276,
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

_source line 29 · 2026-05-29T05:55:52.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GzSZ1V8YdGT6jE7yCxNHqb`</summary>

```json
{
  "query": "\"Agentic Proposing\" compositional skill synthesis arXiv 2602.03279 math reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3aaae6-7166-460e-a665-f2aeb602753b",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLu5fJr9BH4mC5gKG1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcbfe129-fe05-491d-aacb-ca60d4f290cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESAscQogXVDnMYymx2pa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1468,
      "cache_creation_input_tokens": 3276,
      "cache_read_input_tokens": 11380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3276,
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

### Tool result

_source line 30 · 2026-05-29T05:55:56.484Z_

<details><summary>↩ Tool result · `toolu_01JYyhToRRabL2odSvpUqYAK`</summary>

```text
Web search results for query: "STEPS arXiv 2601.03676 "skill taxonomy" "directed acyclic graph" OR "DAG" math"

Links: [{"title":"[2601.03676] Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/abs/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/pdf/2601.03676"},{"title":"Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis","url":"https://arxiv.org/html/2601.03676"},{"title":"A Knowledge-based Approach for the Automatic Construction of Skill   Graphs for Online Monitoring","url":"https://arxiv.org/pdf/2102.08827"},{"title":"Use of directed acyclic graphs (DAGs) in applied health research: review and recommendations","url":"https://www.medrxiv.org/content/10.1101/2019.12.20.19015511.full.pdf"}]

I found the arXiv paper for you. STEPS is a Skill Taxonomy guided Entropy-based Post-training data Synthesis framework for generating compositionally challenging data. 

STEPS explicitly targets compositional generalization by uncovering latent relationships among skills and organizing them into an interpretable, hierarchical skill taxonomy using structural information theory. The framework formulates data synthesis as a constrained information maximization problem, selecting skill combinations that maximize marginal structural information within the hierarchy while preserving semantic coherence.

While the search results don't explicitly mention a directed acyclic graph (DAG) structure in the abstract or initial description, the paper does discuss a hierarchical skill taxonomy built from skill relationships. You can access the full paper at https://arxiv.org/abs/2601.03676 for more detailed information about the specific mathematical structures used.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fcdfc7-b537-4654-9138-2654fe982cb9",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "a2d6c479-afac-493c-8e04-6671b73d0374",
  "sourceToolAssistantUUID": "e4fcdfc7-b537-4654-9138-2654fe982cb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T05:55:57.443Z_

<details><summary>↩ Tool result · `toolu_013rpmgkSMcnMxssbfyFtVeN`</summary>

```text
Web search results for query: "GRIP graph reasoning instruction producer skill dependency math training data synthesis 2025 2026"

Links: [{"title":"GRIP: A Graph-Based Reasoning Instruction Producer","url":"https://arxiv.org/pdf/2412.08864"},{"title":"[2412.08864v4] GRIP: A Graph-Based Reasoning Instruction Producer","url":"https://arxiv.org/abs/2412.08864v4"},{"title":"[2412.08864] GRIP: A Graph-Based Reasoning Instruction Producer","url":"https://arxiv.org/abs/2412.08864"},{"title":"GRIP: A Graph-Based Reasoning Instruction Producer","url":"https://arxiv.org/pdf/2412.08864v4"},{"title":"GRIP: A Graph-Based Reasoning Instruction Producer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241208864W/abstract"},{"title":"GRIP: A Graph-Based Reasoning Instruction Producer | OpenReview","url":"https://openreview.net/forum?id=36TBVGwzAY"},{"title":"NeurIPS Poster GRIP: A Graph-Based Reasoning Instruction Producer","url":"https://neurips.cc/virtual/2025/poster/120072"}]

Based on the search results, here's what I found about GRIP:

## Overview

GRIP (Graph-based Reasoning Instruction Producer) is a method that efficiently synthesizes high-quality and diverse reasoning instructions by constructing a knowledge graph from seed data and leveraging both explicit and implicit relationships within the graph, while using open-source multi-model supervision to ensure data quality.

## Mathematical Reasoning Application

GRIP was applied to mathematical reasoning, where starting from a seed set of 7.5K math reasoning samples, researchers constructed GRIP-MATH, a dataset containing 2.1 million synthesized question-answer pairs.

## Performance and Advantages

Compared to similar synthetic data methods, GRIP achieves greater scalability and diversity while also significantly reducing costs. On mathematical reasoning benchmarks, models trained with GRIP-MATH demonstrate substantial improvements over their base models and significantly outperform previous data synthesis methods.

## Context

As publicly available Internet data becomes increasingly scarce, synthetic data has emerged as a crucial research direction, though existing data synthesis methods often suffer from limited scalability, insufficient sample diversity, and a tendency to overfit to seed data.

The research appears to have been published around December 2024 with updates through April 2025, and was presented at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c3aaae6-7166-460e-a665-f2aeb602753b",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "c3e8e4a2-445e-4cb1-a9c4-f744c5d83937",
  "sourceToolAssistantUUID": "2c3aaae6-7166-460e-a665-f2aeb602753b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T05:56:02.024Z_

<details><summary>↩ Tool result · `toolu_01GzSZ1V8YdGT6jE7yCxNHqb`</summary>

```text
Web search results for query: ""Agentic Proposing" compositional skill synthesis arXiv 2602.03279 math reasoning"

Links: [{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.03279"},{"title":"[2602.03279] Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/abs/2602.03279"},{"title":"Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://arxiv.org/html/2602.03279"},{"title":"(PDF) Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis","url":"https://www.researchgate.net/publication/400414852_Agentic_Proposing_Enhancing_Large_Language_Model_Reasoning_via_Compositional_Skill_Synthesis"},{"title":"Agentic Proposing: Enhancing Large Language Model ...","url":"https://arxiv.org/pdf/2602.03279"},{"title":"AGENTICMATH: ENHANCING LLM REASONING VIA AGENTIC-BASED MATH DATA GENERATION","url":"https://arxiv.org/pdf/2510.19361"},{"title":"[2508.19988] AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios","url":"https://arxiv.org/abs/2508.19988"}]

Based on the search results, here's information about the paper on arXiv 2602.03279:

## Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis

Agentic Proposing is a novel and fully autonomous framework that transforms problem synthesis into a goal-driven process of compositional logic engineering.

### Key Approach

Problem-construction logic is decomposed into atomic, reasoning modules known as Composable Agent Skills. A specialized proposing agent learns to dynamically select and compose these atomic skills to synthesize complex problems that are both logically sound and precisely calibrated in difficulty.

### Technical Details

The framework uses an iterative workflow of internal reflection and tool-use to develop the Agentic-Proposer-4B using Multi-Granularity Policy Optimization (MGPO) to generate high-precision, verifiable training trajectories across mathematics, coding, and science.

### Results

A 30B solver trained on only 11,000 synthesized trajectories achieves a state-of-the-art 91.6% accuracy on AIME25, rivaling frontier-scale proprietary models such as GPT-5. The specialized 4B proposer, trained via MGPO, outperforms the augmented GPT-5.2 by +1.9 points (and +5.5 points over raw GPT-5.2).

The paper demonstrates that high-quality synthetic training data can effectively substitute for massive human-curated datasets in improving mathematical reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcbfe129-fe05-491d-aacb-ca60d4f290cd",
  "isSidechain": true,
  "promptId": "b3ba186c-0ef7-46c4-8659-4a74240f428f",
  "agentId": "ad1c78f8837ce5d3d",
  "type": "user",
  "uuid": "56e8f89a-7203-4ff6-b78b-bcaaac063e29",
  "sourceToolAssistantUUID": "bcbfe129-fe05-491d-aacb-ca60d4f290cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-29T05:56:46.479Z_

Here is a comprehensive report of the concurrent/recent work landscape.

---

## Concurrent Work Search Results

### HIGHEST RELEVANCE -- Closest match to your proposed idea

**1. STEPS: "Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis"**
- Authors: Yifan Wei, Li Du, Xiaoyan Yu, Yang Feng, Angsheng Li
- Date: January 7, 2026 (arXiv:2601.03676)
- Venue: arXiv preprint (code at github.com/weiyifan1023/STEPS)
- Summary: Builds a **hierarchical skill taxonomy** using structural information theory, then formulates data synthesis as a **constrained information maximization problem** -- selecting skill combinations that maximize marginal structural entropy within the hierarchy. Targets compositional generalization by synthesizing training data for underrepresented skill compositions.
- **Overlap assessment: This is the most concerning hit.** It shares three key elements: (a) organizing skills into a structured hierarchy, (b) using that structure to identify underrepresented skill compositions, and (c) synthesizing targeted training data. However, based on the available details, STEPS uses a **hierarchical taxonomy** (tree-like), not a **directed dependency DAG**; it targets **instruction-following / agent benchmarks**, not specifically mathematical reasoning; and it uses structural entropy to select skill *combinations* rather than modeling prerequisite dependencies between skills. The framing and domain differ, but the conceptual machinery overlaps significantly.

---

### HIGH RELEVANCE -- Shares major components

**2. Agentic Proposing: "Enhancing Large Language Model Reasoning via Compositional Skill Synthesis"**
- Date: February 3, 2026 (arXiv:2602.03279)
- Summary: Decomposes problem-construction logic into atomic "Composable Agent Skills," then trains a proposer agent to dynamically select and compose these skills to synthesize difficult math problems. A 30B solver trained on only 11K synthesized trajectories hits 91.6% on AIME25.
- **Overlap assessment:** Shares the idea of compositional skill-based data synthesis for math. However, it does not model skill *dependencies* as a DAG or use the graph structure to diagnose compositional gaps. The skill composition is agent-driven (RL-based selection), not graph-structure-guided.

**3. GRIP: "A Graph-Based Reasoning Instruction Producer"**
- Date: December 2024, NeurIPS 2025
- Summary: Constructs a **knowledge graph** from seed math data and uses explicit/implicit graph relationships to synthesize 2.1M math QA pairs (GRIP-MATH). Focuses on scalability and diversity of synthetic data.
- **Overlap assessment:** Uses a graph structure for math data synthesis, but the graph represents knowledge/concept relationships for generation diversity, not skill *dependency* DAGs for diagnosing compositional generalization failures.

**4. DAG-Math: "Graph-of-Thought Guided Mathematical Reasoning in LLMs"**
- Date: October 2025 (arXiv:2510.19842), NeurIPS 2025
- Summary: Models Chain-of-Thought reasoning as a stochastic process over DAGs where nodes are derivation states and edges are rule applications. Introduces a "logical closeness" evaluation metric.
- **Overlap assessment:** Uses DAGs in math reasoning but for **evaluating/structuring inference-time CoT**, not for identifying skill gaps or synthesizing training data.

---

### MODERATE RELEVANCE -- Shares some components

**5. OMEGA: "Can LLMs Reason Outside the Box in Math?"**
- Venue: Allen AI (arXiv:2506.18880)
- Summary: Benchmark that delineates three axes of OOD generalization (exploratory, compositional, transformative) across six math domains. Documents sharp performance drops when skills must be composed in unseen ways.
- **Overlap assessment:** Provides the diagnostic/benchmark side of compositional math failure, but does not propose skill DAGs or targeted data synthesis as a remedy.

**6. "Exploring the Compositional Deficiency of Large Language Models in Mathematical Reasoning"**
- Date: May 2024 (arXiv:2405.06680)
- Summary: Introduces MATH-TRAP dataset with logical traps showing LLMs fail on compositional variations of seen problems.
- **Overlap assessment:** Documents the problem you're addressing but doesn't propose the skill-graph-guided synthesis solution.

**7. "Laying the Foundation First? Investigating the Generalization from Atomic Skills to Complex Reasoning Tasks"**
- Date: March 2024 (arXiv:2403.09479)
- Summary: Finds atomic skills do not spontaneously generalize to compositional tasks; proposes hierarchical curriculum learning.
- **Overlap assessment:** Validates the premise of your work (skills don't compose automatically) but uses curriculum learning rather than targeted DAG-guided synthesis.

**8. "The Power of Power Law: Asymmetry Enables Compositional Reasoning"**
- Venue: LIT Workshop @ ICLR 2026 (March 2026)
- Summary: Training under power-law distributions outperforms uniform distributions for compositional reasoning tasks including multi-step arithmetic.
- **Overlap assessment:** Related data distribution insight but no skill graph structure.

**9. AgentCoMa (arXiv:2508.19988)**
- Date: March 2026
- Summary: Compositional benchmark mixing commonsense and math reasoning; documents ~30% accuracy drop when skills are combined.
- **Overlap assessment:** Benchmark only, no synthesis method.

---

### BOTTOM LINE

**No paper found is doing the exact same thing** -- using directed skill *dependency* DAGs to (1) diagnose compositional generalization gaps in mathematical reasoning and (2) synthesize targeted multi-skill math training data to close those gaps.

The closest competitor is **STEPS (arXiv:2601.03676)**, which shares the broad idea of "organize skills into a structure, then use that structure to guide data synthesis for compositional generalization." The key differentiators you would need to articulate clearly are:
- **DAG vs. taxonomy tree**: Your approach uses directed prerequisite dependencies, not just hierarchical clustering.
- **Domain**: STEPS targets instruction-following/agent tasks; your work targets mathematical reasoning specifically.
- **Gap diagnosis**: Your approach uses the DAG to identify specific compositional ceilings, rather than maximizing structural entropy over a taxonomy.

You should cite STEPS prominently as concurrent work and clearly delineate these differences.

Sources:
- [STEPS: Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis](https://arxiv.org/abs/2601.03676)
- [Agentic Proposing: Enhancing LLM Reasoning via Compositional Skill Synthesis](https://arxiv.org/abs/2602.03279)
- [GRIP: A Graph-Based Reasoning Instruction Producer](https://arxiv.org/abs/2412.08864)
- [DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs](https://arxiv.org/abs/2510.19842)
- [OMEGA: Can LLMs Reason Outside the Box in Math?](https://allenai.org/blog/omega)
- [Exploring the Compositional Deficiency of LLMs in Mathematical Reasoning](https://arxiv.org/abs/2405.06680)
- [Laying the Foundation First? Investigating Generalization from Atomic Skills](https://arxiv.org/abs/2403.09479)
- [The Power of Power Law: Asymmetry Enables Compositional Reasoning (OpenReview)](https://openreview.net/forum?id=70fuQSzSfZ)
- [AgentCoMa: A Compositional Benchmark](https://arxiv.org/abs/2508.19988)
- [STEPS GitHub Repository](https://github.com/weiyifan1023/STEPS)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56e8f89a-7203-4ff6-b78b-bcaaac063e29",
  "isSidechain": true,
  "agentId": "ad1c78f8837ce5d3d",
  "requestId": "req_011CbWLvMvddfQaBHsGx8LUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fc5c333-b184-4a05-871a-3b892f673e74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f6c07681-545c-4803-9e33-01c676fbec83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuXD69W7mJ8jww27RLShcd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 14656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3615,
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
