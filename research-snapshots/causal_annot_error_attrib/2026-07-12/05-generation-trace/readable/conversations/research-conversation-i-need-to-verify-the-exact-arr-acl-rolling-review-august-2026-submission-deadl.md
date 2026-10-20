# Research conversation: I need to verify the exact ARR (ACL Rolling Review) August 2026 submission deadline. The reviewer claims it is August 3,

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5efa45deaa3579a4.jsonl`
- **Structured JSON:** [`5df51b04067e3b444422.json`](../../sessions/5d/5df51b04067e3b444422.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-27T17:50:33.623Z_

I need to verify the exact ARR (ACL Rolling Review) August 2026 submission deadline. The reviewer claims it is August 3, 2026 (not ~Aug 15 as we stated).

Please search for:
1. "ACL Rolling Review August 2026 deadline submission"
2. "ARR 2026 submission dates schedule"
3. Check https://aclrollingreview.org for current deadlines

Also search for:
4. "AAAI 2027 deadline submission dates" to confirm the July 21/28 dates
5. "ICLR 2027 submission deadline" to see if dates have been announced

Report the exact confirmed dates for all three venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "1c5caf6a-5510-461d-b3c5-eed9a3a8984e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T17:50:33.626Z_

```json
{
  "parentUuid": "1c5caf6a-5510-461d-b3c5-eed9a3a8984e",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
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
  "uuid": "919e6939-880d-406e-87e5-b9b4b2d9a97c",
  "timestamp": "2026-05-27T17:50:33.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T17:50:33.626Z_

```json
{
  "parentUuid": "919e6939-880d-406e-87e5-b9b4b2d9a97c",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3a7bfd20-3f7f-44cd-ad04-182de377c2b7",
  "timestamp": "2026-05-27T17:50:33.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T17:50:36.320Z_



I'll search for the deadline information across multiple sources. Let me start by fetching the ACL Rolling Review website and running web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7bfd20-3f7f-44cd-ad04-182de377c2b7",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVnnBwqhQqpaJu9C1TL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e9bd0f9-202d-4f6d-9edd-7b7ffe55fc68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187iCsGXWra8YE9MzJRHkrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1508,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 5 · 2026-05-27T17:50:36.621Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014HgPNDxWzoYLhS58n99Wpy`</summary>

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
  "parentUuid": "4e9bd0f9-202d-4f6d-9edd-7b7ffe55fc68",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVnnBwqhQqpaJu9C1TL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe4dd465-dda6-4bf3-ae6a-223af0aaba77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187iCsGXWra8YE9MzJRHkrQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1508,
      "cache_read_input_tokens": 7411,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1508
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1508,
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

_source line 6 · 2026-05-27T17:50:36.624Z_

<details><summary>↩ Tool result · `toolu_014HgPNDxWzoYLhS58n99Wpy`</summary>

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
  "parentUuid": "fe4dd465-dda6-4bf3-ae6a-223af0aaba77",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "dfbce14f-3ede-4418-965f-c40a5a3a10a2",
  "sourceToolAssistantUUID": "fe4dd465-dda6-4bf3-ae6a-223af0aaba77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T17:50:39.106Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfbce14f-3ede-4418-965f-c40a5a3a10a2",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVo1JVTYrJQuqSikCiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72536335-ff21-4d3d-a84b-9d984a158b8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArQaxJswvy6jT2Rw3WrbHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 8 · 2026-05-27T17:50:39.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjNuR5eMbod8kK7yjJisSq`</summary>

```json
{
  "query": "ACL Rolling Review August 2026 deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72536335-ff21-4d3d-a84b-9d984a158b8a",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVo1JVTYrJQuqSikCiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "640c08bc-ceda-4366-82c0-04964779fd21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArQaxJswvy6jT2Rw3WrbHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 9 · 2026-05-27T17:50:40.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXjNxXKzndPecpWwa8dBxB`</summary>

```json
{
  "query": "ARR 2026 submission dates schedule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "640c08bc-ceda-4366-82c0-04964779fd21",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVo1JVTYrJQuqSikCiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5239078a-1c8e-4e11-b57b-aa541ea2cae3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArQaxJswvy6jT2Rw3WrbHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 10 · 2026-05-27T17:50:41.469Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PekTKiZqmocwu8s2jWKiUL`</summary>

```json
{
  "url": "https://aclrollingreview.org",
  "prompt": "Find all submission deadlines for 2026, especially the August 2026 deadline. List every deadline date you can find on this page, including any schedule or calendar of upcoming deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5239078a-1c8e-4e11-b57b-aa541ea2cae3",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVo1JVTYrJQuqSikCiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e12cc5ea-31a3-4a8a-8215-c2b837d7a575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArQaxJswvy6jT2Rw3WrbHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 11 · 2026-05-27T17:50:41.480Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPMgqWrQbFZLQdmtiVX7wV`</summary>

```json
{
  "query": "AAAI 2027 deadline submission dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e12cc5ea-31a3-4a8a-8215-c2b837d7a575",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVo1JVTYrJQuqSikCiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0fc51b2-b355-40d0-89a7-fc498a408e5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArQaxJswvy6jT2Rw3WrbHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 12 · 2026-05-27T17:50:41.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QpB6o2dq6esrUoshzkQ6eL`</summary>

```json
{
  "query": "ICLR 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0fc51b2-b355-40d0-89a7-fc498a408e5f",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVo1JVTYrJQuqSikCiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "383afee7-a540-4c0e-8e01-d5e4b21a5309",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArQaxJswvy6jT2Rw3WrbHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8919,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 306,
          "cache_read_input_tokens": 8919,
          "cache_creation_input_tokens": 1133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1133,
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

_source line 13 · 2026-05-27T17:50:44.492Z_

<details><summary>↩ Tool result · `toolu_01HjNuR5eMbod8kK7yjJisSq`</summary>

```text
Web search results for query: "ACL Rolling Review August 2026 deadline submission"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org//calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here's what I found regarding the ACL Rolling Review August 2026 submission deadline:

For EACL 2027, the final ARR submission date is August 3, 2026, with a commitment date of October 11, 2026.

This appears to be the August 2026 deadline you're asking about. ACL switched to 10-week review cycles starting in May 2025, which means submissions follow a different schedule than before.

If you're looking for submission details for a specific August 2026 cycle or different venue, please note that starting from 2024, all main *ACL conferences used ARR exclusively, including ACL 2026, EACL 2026, NAACL 2025, ACL 2025, EMNLP 2025, AACL 2025, EACL 2026, and ALTA 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "640c08bc-ceda-4366-82c0-04964779fd21",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "83e09f27-f1af-4ed8-8d43-9ed008d1586a",
  "sourceToolAssistantUUID": "640c08bc-ceda-4366-82c0-04964779fd21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T17:50:45.042Z_

<details><summary>↩ Tool result · `toolu_01PekTKiZqmocwu8s2jWKiUL`</summary>

```text
# ARR 2026 Submission Deadlines

Based on the webpage content provided, I found **only one specific deadline date**:

**January 7, 2026** - Registration deadline for authors to serve as reviewers or meta-reviewers (Area Chairs), described as "EoD AoE" (end of day, anywhere on Earth).

## Important Note

The page does not contain an explicit August 2026 deadline or a comprehensive calendar of all 2026 submission deadlines. While the site references "dates and venues" information and mentions that "2024, the ACL, EACL, NAACL, and EMNLP main conferences all used ARR," the actual submission deadlines for these upcoming venues are not detailed on this homepage.

To find the complete 2026 schedule, you would need to visit the "[Dates & Venues](/dates)" section linked in the navigation menu, which is not included in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e12cc5ea-31a3-4a8a-8215-c2b837d7a575",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "5687d56d-b957-44a3-8e76-d9ed28b49ad9",
  "sourceToolAssistantUUID": "e12cc5ea-31a3-4a8a-8215-c2b837d7a575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T17:50:45.179Z_

<details><summary>↩ Tool result · `toolu_01QpB6o2dq6esrUoshzkQ6eL`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, I found limited specific information about the ICLR 2027 submission deadline. ICLR 2027 is scheduled for July 2027 with the deadline listed as "TBA" (To Be Announced), based on a predicted pattern.

The search results show information about ICLR 2026 but not yet detailed deadlines for ICLR 2027. Since ICLR 2027 is still over a year away, the official call for papers and specific submission deadlines have not yet been announced. I recommend checking the official ICLR website (iclr.cc) directly for the most up-to-date information once the 2027 call for papers is released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "383afee7-a540-4c0e-8e01-d5e4b21a5309",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "4f991b55-5f23-431a-b786-4ae60433f62e",
  "sourceToolAssistantUUID": "383afee7-a540-4c0e-8e01-d5e4b21a5309",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T17:50:46.630Z_

<details><summary>↩ Tool result · `toolu_01EXjNxXKzndPecpWwa8dBxB`</summary>

```text
Web search results for query: "ARR 2026 submission dates schedule"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org//calls/papers/"}]

Based on the search results, here's information about ARR 2026 submission dates and schedules:

## ARR Cycle Schedule

The ACL Peer Review Committee recommended switching to 10-week review cycles, with the new schedule starting in May 2025 cycle. This means that instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.

## Key Dates for ARR 2026 Cycles

**March 2026 Cycle:**
The deadline for completing the registration form is January 7th 2026 EoD AoE. The deadline for reviews is February 7th, and for meta-reviews March 3rd.

**May 2026 Cycle:**
Papers must be submitted, at latest, by the ARR 2026 May cycle. After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE. If you receive assignments, your reviews must be completed by July 6, or your meta-reviews - by July 29.

For more detailed information about specific submission deadlines and conference commitments, you may want to check the official ARR website at aclrollingreview.org or the OpenReview pages for each specific cycle.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5239078a-1c8e-4e11-b57b-aa541ea2cae3",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "d082cbb3-6821-48ec-b9af-51738764a6b2",
  "sourceToolAssistantUUID": "5239078a-1c8e-4e11-b57b-aa541ea2cae3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T17:50:47.183Z_

<details><summary>↩ Tool result · `toolu_01HPMgqWrQbFZLQdmtiVX7wV`</summary>

```text
Web search results for query: "AAAI 2027 deadline submission dates"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"}]

Based on the search results, here are the AAAI 2027 submission deadline dates:

## AAAI-27 Main Technical Track Deadlines

The conference will be held February 16 – February 23, 2027 in Montréal, Canada, with the following key deadlines (all in UTC-12):
- June 17, 2026: Open Review submission site opens for author registration
- June 24, 2026: Open Review submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12
- September 24, 2026: Notification of Phase 1 rejections
- October 19-25, 2026: Author feedback window
- November 30, 2026: Notification of final acceptance or rejection
- December 14, 2026: Submission of camera-ready files

Note that deadlines are track-specific and may differ, with track-specific deadlines listed on their respective Call for Papers (CFP).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0fc51b2-b355-40d0-89a7-fc498a408e5f",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "93e7fa33-b61c-41c7-9a6e-6831132cd52c",
  "sourceToolAssistantUUID": "f0fc51b2-b355-40d0-89a7-fc498a408e5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T17:50:50.837Z_

Good, I have initial results. Let me now fetch the ARR dates page directly and the AAAI-27 official page to confirm the exact details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93e7fa33-b61c-41c7-9a6e-6831132cd52c",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVon9VmpJ33X3Cs37nZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce5135ba-f460-48a1-88f3-6abe774fba1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPT1LyEX4wPMC3MU5BLdez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 565,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 10052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
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

_source line 19 · 2026-05-27T17:50:51.781Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JMez2oa1hEwrtBpxvXtYXB`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "List ALL submission deadlines for 2026, especially the August 2026 cycle. I need the exact date for the August 2026 ARR submission deadline. List every cycle and its submission deadline date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce5135ba-f460-48a1-88f3-6abe774fba1b",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVon9VmpJ33X3Cs37nZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69eeb6ec-e061-423b-bfe3-aa89090b6dbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPT1LyEX4wPMC3MU5BLdez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 565,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 10052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
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

_source line 20 · 2026-05-27T17:50:53.192Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011TBuvLEBehdUTLG2epRqBF`</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/",
  "prompt": "List all important dates and submission deadlines for AAAI-27. I need the exact abstract deadline, full paper deadline, and any other key dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69eeb6ec-e061-423b-bfe3-aa89090b6dbf",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVon9VmpJ33X3Cs37nZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d00c784-e64c-4525-9984-f984208d1964",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPT1LyEX4wPMC3MU5BLdez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 565,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 10052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
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

_source line 21 · 2026-05-27T17:50:54.603Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HT3DxSCZv77Csj3ywKa7ss`</summary>

```json
{
  "url": "https://2026.eacl.org/calls/papers/",
  "prompt": "Find the ARR submission deadline for papers to be considered for EACL. What is the final ARR submission date? Is August 3, 2026 mentioned as a deadline?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d00c784-e64c-4525-9984-f984208d1964",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVon9VmpJ33X3Cs37nZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5598612-172d-4344-9100-8383904f3c99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPT1LyEX4wPMC3MU5BLdez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 565,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 10052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
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

_source line 22 · 2026-05-27T17:50:55.271Z_

<details><summary>↩ Tool result · `toolu_01JMez2oa1hEwrtBpxvXtYXB`</summary>

```text
# ARR 2026 Submission Deadlines

Based on the webpage content, here are all the submission deadlines listed for 2026:

| Cycle | Submission Deadline |
|-------|-------------------|
| March 2026 | March 16 |
| May 2026 | May 25 |
| August 2026 | August 3 |
| October 2026 | October 12 |

**August 2026 Cycle Details:**
The exact submission deadline for the August 2026 cycle is **August 3, 2026**. The page notes that "Reviewer registration," "Reviews due," "Author Response," and "Meta-reviews release date" are listed as "TBA" (to be announced) for this cycle, with the cycle ending October 11, 2026.

The document explains that as of May 2025, ARR transitioned from 8-week to 10-week review cycles, "reducing the number of cycles from 6 per year to generally 5," while providing "more reasonable timelines for the review tasks."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69eeb6ec-e061-423b-bfe3-aa89090b6dbf",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "16a5edf6-8257-46e4-bf2d-74638f0f199e",
  "sourceToolAssistantUUID": "69eeb6ec-e061-423b-bfe3-aa89090b6dbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T17:50:55.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NrHpbPVoKJ34YtG4JnJ95x`</summary>

```json
{
  "url": "https://mlciv.com/ai-deadlines/",
  "prompt": "Find any information about ARR August 2026 deadline, AAAI 2027 deadlines, and ICLR 2027 deadlines. List exact dates for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16a5edf6-8257-46e4-bf2d-74638f0f199e",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVon9VmpJ33X3Cs37nZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd5e8a43-c8f0-42ea-b928-f83b66d26316",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPT1LyEX4wPMC3MU5BLdez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 565,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 10052,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 565,
          "output_tokens": 481,
          "cache_read_input_tokens": 10052,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2841,
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

_source line 24 · 2026-05-27T17:50:57.256Z_

<details><summary>↩ Tool result · `toolu_01HT3DxSCZv77Csj3ywKa7ss`</summary>

```text
# EACL 2026 ARR Submission Deadline

The final ARR submission date for papers to be considered for EACL 2026 is **October 6, 2025**. According to the document, this is stated as: "ARR submission deadline: **6 October 2025**"

No, August 3, 2026 is not mentioned as a deadline anywhere in the provided content. The key dates listed relate to the 2025 submission cycle and early 2026 notification period, with the conference itself scheduled for March 24-29, 2026 in Rabat, Morocco.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5598612-172d-4344-9100-8383904f3c99",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "88f53fd6-10e9-4991-8c66-e1178abc5a36",
  "sourceToolAssistantUUID": "f5598612-172d-4344-9100-8383904f3c99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T17:50:57.314Z_

<details><summary>↩ Tool result · `toolu_011TBuvLEBehdUTLG2epRqBF`</summary>

```text
# AAAI-27 Key Submission Deadlines

**Abstract Deadline:** "July 21, 2026 at 11:59 PM UTC-12"

**Full Paper Deadline:** "July 28, 2026" at 11:59 PM UTC-12

**Supplementary Materials & Code:** "July 31, 2026 by 11:59 PM UTC-12"

## Other Important Dates

- **June 17, 2026** – Open Review registration opens
- **June 24, 2026** – Paper submission site opens
- **September 24, 2026** – Phase 1 rejection notifications
- **October 19-25, 2026** – Author feedback period
- **November 30, 2026** – Final acceptance/rejection decisions (Main Technical Track)
- **December 14, 2026** – Camera-ready files due
- **February 16-23, 2027** – Conference in Montréal, Canada

Note: The page indicates all deadlines are "anywhere on earth" (UTC-12) and that track-specific deadlines may vary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d00c784-e64c-4525-9984-f984208d1964",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "2d8e6be7-3430-4e74-bec9-d958e59a6ac9",
  "sourceToolAssistantUUID": "4d00c784-e64c-4525-9984-f984208d1964",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T17:51:01.448Z_

<details><summary>↩ Tool result · `toolu_01NrHpbPVoKJ34YtG4JnJ95x`</summary>

```text
# AI Conference Deadline Information

## ARR August 2026
The webpage lists multiple ARR 2026 entries for August 2026, but the exact dates shown are: **"July 27 - Aug 01, 2027"** (noted as TBA location). This appears to be a data inconsistency on the page, as the year designation seems misaligned with the "August 2026" reference.

## AAAI 2027
The deadline information states: **"February 2027"** for the conference itself. The page notes this is **"Predicted based on historical pattern"** with a mandatory abstract deadline typically occurring one week prior to the paper submission deadline.

## ICLR 2027
The submission window is scheduled for **"Apr 24-28, 2027"** for the conference dates. However, the specific paper deadline date is not explicitly listed on this page; it notes this is **"Predicted based on previous year schedule"** and recommends verifying details on the official conference website.

**Note:** The webpage indicates that predicted deadlines should be verified directly with conference organizers, as these are estimates based on historical patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd5e8a43-c8f0-42ea-b928-f83b66d26316",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "c0a4c513-d42f-4aa5-b0fa-955c062ea7dc",
  "sourceToolAssistantUUID": "dd5e8a43-c8f0-42ea-b928-f83b66d26316",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-27T17:51:04.876Z_

Let me also check the EMNLP 2026 page since it may reference the ARR August cycle, and fetch a conference deadline aggregator for ICLR 2027.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a4c513-d42f-4aa5-b0fa-955c062ea7dc",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVpq9MnYgRNFCTWaeX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ada16b5-253e-44b4-8875-6465f9b9d157",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2AQrPasotpDDrT21coecg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 12893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2152,
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

_source line 28 · 2026-05-27T17:51:06.302Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01462ym6dnzb4KcHGgtUbkqX`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Find all important dates and deadlines for EMNLP 2026, especially any ARR submission deadlines. What ARR cycle is the final one for EMNLP 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ada16b5-253e-44b4-8875-6465f9b9d157",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVpq9MnYgRNFCTWaeX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8036bdc-62bb-414e-8028-eb72fb053739",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2AQrPasotpDDrT21coecg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 12893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2152,
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

_source line 29 · 2026-05-27T17:51:06.593Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VWTASiNRH5jyxq281mneGU`</summary>

```json
{
  "query": "ICLR 2027 call for papers deadline October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8036bdc-62bb-414e-8028-eb72fb053739",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVpq9MnYgRNFCTWaeX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c22fe547-fde5-469d-93f8-25498502979a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2AQrPasotpDDrT21coecg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 12893,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2152
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 12893,
          "cache_creation_input_tokens": 2152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2152,
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

_source line 30 · 2026-05-27T17:51:10.392Z_

<details><summary>↩ Tool result · `toolu_01462ym6dnzb4KcHGgtUbkqX`</summary>

```text
# EMNLP 2026 Key Deadlines

## ARR Submission Deadline

The final ARR cycle for EMNLP 2026 is **ARR 2026 May**. As stated in the submission guidelines: "Papers must be submitted, at latest, by the ARR 2026 May cycle."

The deadline is **May 25, 2026** (11:59 PM UTC-12:00, "anywhere on Earth").

## Other Critical Dates

| Milestone | Date |
|-----------|------|
| Reviewer registration deadline | May 27, 2026 |
| Author response/discussion period | July 7-13, 2026 |
| Meta review release | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notifications | August 20, 2026 |
| Camera-ready papers due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

## Important Note

Papers from earlier ARR cycles may still be committed to EMNLP 2026, but "ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8036bdc-62bb-414e-8028-eb72fb053739",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "a49c5c7e-796d-41fc-a38a-e4f1e7ab83a0",
  "sourceToolAssistantUUID": "e8036bdc-62bb-414e-8028-eb72fb053739",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T17:51:10.878Z_

<details><summary>↩ Tool result · `toolu_01VWTASiNRH5jyxq281mneGU`</summary>

```text
Web search results for query: "ICLR 2027 call for papers deadline October 2026"

Links: [{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Workshops Call for Proposals 2026","url":"https://iclr.cc/Conferences/2026/CallForWorkshops"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"}]

Based on the search results, I found information about ICLR deadlines, but it appears the search returned details about ICLR 2026 rather than ICLR 2027. Here's what I found:

**For ICLR 2026:** The deadline for paper submissions was September 24.

However, the search results did not contain specific information about an ICLR 2027 call for papers deadline in October 2026. The most recent conference information in the results relates to ICLR 2026, which has already taken place (the conference was held in April 2026). 

To find official information about ICLR 2027's call for papers and deadlines, I would recommend checking the official ICLR website at iclr.cc directly, as the official call for papers for ICLR 2027 may not yet be publicly announced or the information may not be widely indexed yet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c22fe547-fde5-469d-93f8-25498502979a",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "51d1e5ac-acda-4434-9957-ad68a39c8bb2",
  "sourceToolAssistantUUID": "c22fe547-fde5-469d-93f8-25498502979a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T17:51:15.181Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DbvM6eunLfhodenHMUoCK3`</summary>

```json
{
  "url": "https://trybibby.com/conference-deadlines",
  "prompt": "Find the ICLR 2027 submission deadline and any other details about ICLR 2027. Also check for AAAI 2027 dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51d1e5ac-acda-4434-9957-ad68a39c8bb2",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVqXZxe6BTWRkAiMELj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f295274-3283-4fe4-8ef7-73471ef4ab60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sp4hdK7gZAia8qgcpWE4Wk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15045,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 15045,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1218,
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

_source line 33 · 2026-05-27T17:51:21.519Z_

<details><summary>↩ Tool result · `toolu_01DbvM6eunLfhodenHMUoCK3`</summary>

```text
# Conference Deadlines Overview

Based on the webpage content, this is a comprehensive deadline tracker for academic conferences across multiple disciplines through 2027.

## Key Upcoming Deadlines

The site lists 78 entries, with Computer Science dominating at 53 conferences. The next major deadline is **CoRL 2026** (Conference on Robot Learning) with a full paper submission due May 29, 2026.

## Major Conferences Featured

Notable venues include:
- **ICLR 2027** with abstract and paper deadlines in September 2026
- **AAAI 2027** with abstract and paper tracks opening in July-August 2026
- **NeurIPS 2027** with a May 2027 deadline
- **CVPR 2027** with abstract registration and paper submissions spanning November 2026-November 2027

## Coverage Areas

The tracker covers research across "ML · AI · CV · NLP · Robotics · Signal · HCI · Data Mining · Neuro · Physics · Math," providing real-time countdown timers for each submission deadline.

## Important Note

The site emphasizes: *"Always verify against the official CFP before submitting — the clock does not stop for mistakes."* Deadlines are rendered in each conference's specified timezone, with many computer science venues using Anywhere-on-Earth (AoE, UTC−12).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f295274-3283-4fe4-8ef7-73471ef4ab60",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "f1dc36fe-c0a4-4116-8804-92201490c212",
  "sourceToolAssistantUUID": "6f295274-3283-4fe4-8ef7-73471ef4ab60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T17:51:23.807Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6XLVv7ggUC7E2EZqPXnwx`</summary>

```json
{
  "query": "ICLR 2027 September 2026 submission deadline abstract paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1dc36fe-c0a4-4116-8804-92201490c212",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVrJszqsEwzpusrShK4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d15a7449-e3e5-49d0-bbc5-325a4f418052",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EFGTJ7S4V8LEGqFDRsDxEH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 16263,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 438
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 16263,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 438,
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

_source line 35 · 2026-05-27T17:51:31.043Z_

<details><summary>↩ Tool result · `toolu_01H6XLVv7ggUC7E2EZqPXnwx`</summary>

```text
Web search results for query: "ICLR 2027 September 2026 submission deadline abstract paper"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"}]

I found information about ICLR 2026, but I need to search specifically for ICLR 2027 submission deadlines. Let me search for that:

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"}]

Based on my search results, I found information about ICLR conferences, but the official ICLR 2027 call for papers with specific submission deadlines does not appear to be announced yet. 

Here's what I found:

The search results show information for ICLR 2026 (the current upcoming conference) and some references to ICLR 2027, but some 2026/2027 CFPs are not yet posted as of early February 2026.

For reference, the pattern from previous years shows that ICLR typically has a mandatory abstract deadline in late September. However, the official call for papers with confirmed submission deadlines for ICLR 2027 has not yet been published.

To get the most accurate and up-to-date information about ICLR 2027 submission deadlines, I recommend:
1. Checking the official ICLR website at iclr.cc
2. Monitoring OpenReview.net for the official ICLR 2027 conference submission system
3. Signing up for updates on the ICLR mailing list


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d15a7449-e3e5-49d0-bbc5-325a4f418052",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "f041525e-e786-4b94-8581-59761fbb6849",
  "sourceToolAssistantUUID": "d15a7449-e3e5-49d0-bbc5-325a4f418052",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-27T17:51:34.174Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013TosRHQ7wvsd35EJMpQU1w`</summary>

```json
{
  "url": "https://iclr.cc/Conferences/2027",
  "prompt": "Find any information about ICLR 2027, including dates, location, submission deadlines, call for papers. List all dates mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f041525e-e786-4b94-8581-59761fbb6849",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVs1gB98Aqi2a8tgRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81e157cf-9340-47ec-87ec-c983b9e4c8eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017X3oncddXw4bS1CyrhSnP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 16701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1105,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 37 · 2026-05-27T17:51:35.214Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y2BDyRqQmykumXx9Sna9us`</summary>

```json
{
  "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac",
  "prompt": "Find the ICLR 2027 submission deadline and AAAI 2027 submission deadline dates. List any exact dates mentioned for these conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e157cf-9340-47ec-87ec-c983b9e4c8eb",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVs1gB98Aqi2a8tgRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7a728c6-7716-47e6-84ce-6533bfb2d988",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017X3oncddXw4bS1CyrhSnP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 16701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1105,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 38 · 2026-05-27T17:51:35.235Z_

<details><summary>↩ Tool result · `toolu_013TosRHQ7wvsd35EJMpQU1w`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81e157cf-9340-47ec-87ec-c983b9e4c8eb",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "e0107bad-0ec2-4834-94ca-3c5ad377e6de",
  "sourceToolAssistantUUID": "81e157cf-9340-47ec-87ec-c983b9e4c8eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-27T17:51:35.511Z_

<details><summary>↩ Tool result · `toolu_01Y2BDyRqQmykumXx9Sna9us`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7a728c6-7716-47e6-84ce-6533bfb2d988",
  "isSidechain": true,
  "promptId": "8d251980-9caf-43e4-a631-55b1b931b61b",
  "agentId": "a5efa45deaa3579a4",
  "type": "user",
  "uuid": "de09b0b0-750c-4e1c-8c02-bddc073b42c2",
  "sourceToolAssistantUUID": "c7a728c6-7716-47e6-84ce-6533bfb2d988",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-27T17:51:54.087Z_

I now have enough information to provide a comprehensive report. Here is a summary of the confirmed deadlines:

---

## Confirmed Deadline Dates

### 1. ACL Rolling Review (ARR) -- August 2026 Cycle

**The reviewer is correct.** The ARR August 2026 submission deadline is **August 3, 2026**, not ~August 15.

This was confirmed directly from the official [ACL Rolling Review Dates & Venues page](https://aclrollingreview.org/dates). The full 2026 ARR cycle schedule is:

| Cycle | Submission Deadline |
|-------|-------------------|
| March 2026 | March 16 |
| May 2026 | May 25 |
| **August 2026** | **August 3** |
| October 2026 | October 12 |

The August cycle ends October 11, 2026. Note that ARR switched from 8-week to 10-week review cycles starting May 2025, reducing from 6 cycles per year to 5, which shifts deadlines earlier than one might expect from historical patterns.

### 2. AAAI 2027

**The July 21/28 dates are confirmed.** From the official [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/):

- **June 17, 2026** -- OpenReview registration opens
- **June 24, 2026** -- Paper submission site opens
- **July 21, 2026** -- Abstracts due (11:59 PM UTC-12)
- **July 28, 2026** -- Full papers due (11:59 PM UTC-12)
- **July 31, 2026** -- Supplementary material and code due
- **September 24, 2026** -- Phase 1 rejection notifications
- **October 19-25, 2026** -- Author feedback window
- **November 30, 2026** -- Final acceptance/rejection
- **December 14, 2026** -- Camera-ready due
- **February 16-23, 2027** -- Conference in Montreal, Canada

### 3. ICLR 2027

**No official dates announced yet.** The ICLR 2027 page (iclr.cc/Conferences/2027) returns a 404, meaning the official call for papers has not been posted. One deadline aggregator ([trybibby.com](https://trybibby.com/conference-deadlines)) predicts abstract and paper deadlines in **September 2026** based on historical patterns (ICLR 2026 had a September 24, 2025 deadline), but these are estimates only and not confirmed by the organizers.

---

## Key Takeaway

The reviewer's correction about the ARR August 2026 deadline is accurate: it is **August 3, 2026**, confirmed on the official ACL Rolling Review website. Your document's "~Aug 15" estimate was off by about 12 days. This is important because the 10-week cycle structure pulls deadlines earlier than the old 8-week cycle pattern might suggest.

Sources:
- [ACL Rolling Review -- Dates and Venues](https://aclrollingreview.org/dates)
- [AAAI-27 Main Technical Track CFP](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [AI & ML Conference Deadlines 2026-2027 (trybibby.com)](https://trybibby.com/conference-deadlines)
- [AI Conference Deadlines (mlciv.com)](https://mlciv.com/ai-deadlines/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de09b0b0-750c-4e1c-8c02-bddc073b42c2",
  "isSidechain": true,
  "agentId": "a5efa45deaa3579a4",
  "requestId": "req_011CbTVsLktFkBhVaJMF3DUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3bbd8b7-d294-40ad-975a-9d212bc83355",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fb084f80-f924-4de3-8655-efd55a5a6caf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126ft9i2P8R9YgHT8WkJYXj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 17806,
      "output_tokens": 935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 401
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 935,
          "cache_read_input_tokens": 17806,
          "cache_creation_input_tokens": 401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 401,
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
