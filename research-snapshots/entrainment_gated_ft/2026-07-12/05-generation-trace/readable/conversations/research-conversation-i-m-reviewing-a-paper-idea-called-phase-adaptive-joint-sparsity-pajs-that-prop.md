# Research conversation: I'm reviewing a paper idea called "Phase-Adaptive Joint Sparsity (PAJS)" that proposes applying different attention-head

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af320cd6db7e1c763.jsonl`
- **Structured JSON:** [`1152e95d0dbc847ec498.json`](../../sessions/11/1152e95d0dbc847ec498.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-11T23:34:18.362Z_

I'm reviewing a paper idea called "Phase-Adaptive Joint Sparsity (PAJS)" that proposes applying different attention-head and MLP activation sparsity levels during different reasoning phases (thinking vs. answer) of reasoning models like DeepSeek-R1. I need to find competing or highly similar work that the authors may have missed.

Please perform the following WebSearches (use WebSearch, not WebFetch) and report findings concisely:

1. Search: "phase-aware sparsity reasoning model inference 2025 2026"
2. Search: "adaptive compute sparsity thinking tokens LLM 2025 2026"
3. Search: "joint attention MLP sparsity reasoning models"
4. Search: "dynamic sparsity budget allocation reasoning model decoding"
5. Search: "compute-aware optimization reasoning model inference efficiency 2026"
6. Search: "site:arxiv.org reasoning model activation sparsity phase 2026"
7. Search: "site:arxiv.org adaptive inference sparsity chain-of-thought 2025"
8. Search: "attention head pruning MLP sparsity reasoning LLM 2025 2026"
9. Search: "DeepSeek-R1 inference optimization sparsity 2026"
10. Search: "site:openreview.net phase adaptive sparsity reasoning 2026"

For each search, report: the search query used, and the top 3-5 most relevant results with titles, venues, and a one-line description. Focus especially on any paper that combines (a) phase/reasoning awareness with (b) compute sparsity (attention + MLP), which is the core claim of PAJS.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "a5cfe51f-d4fd-4c74-a0b4-43900204a497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:34:18.365Z_

```json
{
  "parentUuid": "a5cfe51f-d4fd-4c74-a0b4-43900204a497",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c9d1025a-80d2-487e-b6c9-13ae6c2e455d",
  "timestamp": "2026-05-11T23:34:18.365Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:34:21.403Z_



I'll load the WebSearch tool first, then run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d1025a-80d2-487e-b6c9-13ae6c2e455d",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4U3gAppFnkJRgwUKw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30adda16-24be-4b5b-a7af-f0a4f064860e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cw1wqUHnwVsrPgqkt2kZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:34:21.690Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018nBPQKBv1ukb3tw3zf1vZz`</summary>

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
  "parentUuid": "30adda16-24be-4b5b-a7af-f0a4f064860e",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4U3gAppFnkJRgwUKw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb5211ce-b889-4a50-8a28-620c4320643f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cw1wqUHnwVsrPgqkt2kZT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 8223,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 939,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-11T23:34:21.693Z_

<details><summary>↩ Tool result · `toolu_018nBPQKBv1ukb3tw3zf1vZz`</summary>

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
  "parentUuid": "fb5211ce-b889-4a50-8a28-620c4320643f",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "04fa97c2-545f-4a75-b811-a174302131a8",
  "sourceToolAssistantUUID": "fb5211ce-b889-4a50-8a28-620c4320643f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:34:28.486Z_



Now I'll run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04fa97c2-545f-4a75-b811-a174302131a8",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "447ccf72-eb8b-42ba-99dd-256431879896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-11T23:34:29.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXhXqwBLqU1nuhbdVU7u7d`</summary>

```json
{
  "query": "phase-aware sparsity reasoning model inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "447ccf72-eb8b-42ba-99dd-256431879896",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62bde4e1-484a-4592-9bc5-3c187defd554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-11T23:34:29.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q8w3CCeNhoXXqQgESV2yny`</summary>

```json
{
  "query": "adaptive compute sparsity thinking tokens LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62bde4e1-484a-4592-9bc5-3c187defd554",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "619612c3-646c-47e7-9241-9efca473f038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-11T23:34:30.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011bPx8jHkpBr7dbYiFZQ7NJ`</summary>

```json
{
  "query": "joint attention MLP sparsity reasoning models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "619612c3-646c-47e7-9241-9efca473f038",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffd1e3cd-15ed-4a9a-a9ff-51836d19776e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-11T23:34:31.584Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013N1TS61Q8oFBUsjxwjZ7Sf`</summary>

```json
{
  "query": "dynamic sparsity budget allocation reasoning model decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffd1e3cd-15ed-4a9a-a9ff-51836d19776e",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "016b8e46-e6fe-409c-a9e8-c341844cc822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-11T23:34:31.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bfqmrw29r3kHgt3UapdV6f`</summary>

```json
{
  "query": "compute-aware optimization reasoning model inference efficiency 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "016b8e46-e6fe-409c-a9e8-c341844cc822",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b526888e-9f36-4ce6-86e2-456d17282ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-11T23:34:32.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CGN1evoLAynb3JG86tW26N`</summary>

```json
{
  "query": "site:arxiv.org reasoning model activation sparsity phase 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b526888e-9f36-4ce6-86e2-456d17282ccb",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "663fe488-93a8-46fc-8bbf-a49689597525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-11T23:34:33.787Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NcbMBz9FDwpJnWA5oWcZMe`</summary>

```json
{
  "query": "site:arxiv.org adaptive inference sparsity chain-of-thought 2025",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "663fe488-93a8-46fc-8bbf-a49689597525",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d573d7bf-2d6d-43d0-bb05-3694350bf393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-11T23:34:34.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGf8KARDsY6P23fHkDDArh`</summary>

```json
{
  "query": "attention head pruning MLP sparsity reasoning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d573d7bf-2d6d-43d0-bb05-3694350bf393",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b461e76a-91c3-42da-a51c-a7b6bf8ae1b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-11T23:34:34.732Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Js8NziWgipjpa9KWjQAX23`</summary>

```json
{
  "query": "DeepSeek-R1 inference optimization sparsity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b461e76a-91c3-42da-a51c-a7b6bf8ae1b7",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9b36914-cd7e-4855-9878-4ab6d4a38c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-11T23:34:35.428Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LRc2QxrDsCT55XQhfENPoX`</summary>

```json
{
  "query": "site:openreview.net phase adaptive sparsity reasoning 2026",
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
  "parentUuid": "a9b36914-cd7e-4855-9878-4ab6d4a38c22",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf4iaHrYgbbBb6q6gHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d971ad-8098-405e-ab30-d075b42010cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZrDZkkxmDmoYTwoZ1aGSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9162,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 591,
          "cache_read_input_tokens": 9162,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T23:34:37.252Z_

<details><summary>↩ Tool result · `toolu_01CXhXqwBLqU1nuhbdVU7u7d`</summary>

```text
Web search results for query: "phase-aware sparsity reasoning model inference 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.03152"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"A Survey of Efficient LLM Inference Serving","url":"https://aclanthology.org/2025.inlg-main.32.pdf"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"LARGE LANGUAGE MODEL INFERENCE ACCELERATION:","url":"https://dai.sjtu.edu.cn/my_file/pdf/a43c4dc7-6132-49cb-b737-311eefde646f.pdf"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=1500&show=2000"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"}]

Based on the web search results, I found relevant information about phase-aware sparsity and reasoning model inference from 2025-2026:

## Key Findings

FASA (Frequency-Aware Sparsity for Attention) is rooted in the observation that differential frequencies within RoPE induce functional sparsity among frequency chunks (FCs), where only a sparse subset of dominant FCs contribute significantly to contextual awareness while others construct robust positional patterns. These dominant FCs are sparse, universal, and task-agnostic.

FASA employs a two-stage framework for efficient inference, and has been evaluated across a range of LLMs with varying KV cache budgets, concentrating on three core tasks: long-context benchmark, long-sequence modeling, and long chain-of-thought (LongCoT) reasoning.

### Performance Results

FASA achieves performance comparable to that of full KV cache with reduction of less than 0.7%, while FASA-M provides an 8× compression of the KV cache, and FASA-C delivers 2.6× speedups with 25% of FCs selected.

### Related Sparsity Research

More broadly, optimizing the reasoning path reduces inference time without compromising accuracy, and future architectures may incorporate dynamic reasoning modules that skip unnecessary steps. Additionally, sparsity-based techniques are proving critical not just for improving efficiency but also for enhancing interpretability, modularity, and adaptability in AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62bde4e1-484a-4592-9bc5-3c187defd554",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "68a5af73-fb34-4cc0-aaaf-98b4e25b5712",
  "sourceToolAssistantUUID": "62bde4e1-484a-4592-9bc5-3c187defd554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T23:34:37.846Z_

<details><summary>↩ Tool result · `toolu_01Q8w3CCeNhoXXqQgESV2yny`</summary>

```text
Web search results for query: "adaptive compute sparsity thinking tokens LLM 2025 2026"

Links: [{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"QTALE: Quantization-Robust Token-Adaptive Layer Execution for LLMs","url":"https://arxiv.org/html/2602.10431v1"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Adaptive Thinking: Large Language Models Know When to Think in Latent Space | OpenReview","url":"https://openreview.net/forum?id=2i6Rp0gCq6"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/html/2505.11274v6"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853v1"},{"title":"FAST LLM DECODING BY HIERARCHICAL KEY-VALUE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf"},{"title":"A Survey of Adaptive and Controllable Test-Time Compute ...","url":"https://arxiv.org/pdf/2507.02076"},{"title":"Track: Session 7: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3153"},{"title":"[2503.23798] Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/abs/2503.23798"}]

I found several relevant research papers and resources on this topic. Here's a summary of what's being researched in 2025-2026:

## Key Research Areas

**Adaptive Thinking and Compute Allocation:**
Recent advances in LLM test-time computing have introduced the capability to perform intermediate chain-of-thought reasoning before generating answers, and the relationship between LLM capability, query complexity, and optimal budget allocation is being explored for compute-optimal inference. One approach called Sonata adaptively allocates thinking budgets to optimize the performance-efficiency tradeoff.

**Token Sparsity and Efficiency:**
LLMs exhibit contextual sparsity, where only a subset of computations is required to generate each token. Recent papers cover token reduction techniques including token pruning, merging, clustering, compressing, and adaptive thinking.

**Addressing "Overthinking":**
Recent reasoning models use long chain-of-thought processes learned through reinforcement learning, but tend to use overly long thought processes even for simple questions, leading to wasted computational resources.

**Adaptive Token Routing:**
Adaptive Token Routing employs a routing network to dynamically allocate computational resources to tokens based on their complexity, where critical tokens receive additional processing steps while simpler tokens use fewer resources.

**Test-Time Compute Scaling:**
Leading AI labs are adopting fast-slow thinking where models modulate reasoning depth based on task complexity, with examples like Anthropic's Claude supporting a thinking token budget and OpenAI's o1 variants offering different thinking modes.

The research community is actively publishing on these topics at major 2026 conferences including ICLR, ACL, and ICML.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "619612c3-646c-47e7-9241-9efca473f038",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "9fe31cee-ad88-4fff-9d9e-93671b62e671",
  "sourceToolAssistantUUID": "619612c3-646c-47e7-9241-9efca473f038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:34:37.897Z_

<details><summary>↩ Tool result · `toolu_011bPx8jHkpBr7dbYiFZQ7NJ`</summary>

```text
Web search results for query: "joint attention MLP sparsity reasoning models"

Links: [{"title":"What Matters in Transformers? Not All Attention is Needed","url":"https://arxiv.org/html/2406.15786v6"},{"title":"JoMA: Demystifying Multilayer Transformers via JOint Dynamics of MLP and Attention","url":"https://arxiv.org/html/2310.00535v3"},{"title":"[2310.00535] JoMA: Demystifying Multilayer Transformers via JOint Dynamics of MLP and Attention","url":"https://arxiv.org/abs/2310.00535"},{"title":"LLMs don’t need all the attention layers, study shows","url":"https://bdtechtalks.com/2024/12/09/llm-attention-layer-pruning/"},{"title":"LLaMA-MoE v2: Exploring Sparsity of LLaMA from Perspective of Mixture-of-Experts with Post-Training","url":"https://arxiv.org/html/2411.15708"},{"title":"Emergence of Various Structures via the Lens of Transformer Training Dynamics","url":"https://yuandong-tian.com/talks/llm_sparsity.pdf"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"Overcoming Long-Context Limitations of State-Space Models via Context-Dependent Sparse Attention","url":"https://arxiv.org/html/2507.00449"},{"title":"Demystifying Attention in Multi-layer Transformer and its ...","url":"https://yuandong-tian.com/talks/stanford_nlp_2024.pdf"},{"title":"[2502.11147] RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2502.11147"}]

Based on the search results, I found several relevant research papers and findings related to joint attention, MLP sparsity, and reasoning in models:

## Key Research Areas

### 1. Joint Attention and MLP Sparsity in Transformers

Research shows that jointly dropping low-importance Attention and MLP layers yields better performance under high sparsity conditions compared to pruning only one type of layer. A method called "Joint Layer Drop" targets both MLP layers and Attention layers for improved model compression.

### 2. JoMA Framework

The Joint MLP/Attention (JoMA) dynamics framework is a novel mathematical approach to understand the training procedure of multilayer Transformer architectures, achieved by integrating out the self-attention layer in Transformers. JoMA predicts that attention first becomes sparse (to learn salient tokens), then dense (to learn less salient tokens) in the presence of nonlinear activations.

### 3. Sparsity in Reasoning Tasks

Recent work identifies a new attention pattern during the decode stage of reasoning tasks, where milestone tokens (analogous to lemmas in mathematical proofs) emerge and are utilized. To reduce complexities in reasoning, sparsity-based algorithms propose to retain Key-Value (KV) vectors of only the most critical tokens.

### 4. Mixture-of-Experts Approaches

Research investigates the sparsity of dense models by constructing Mixture-of-Experts (MoE) for both the attention and MLP modules in transformer blocks.

These studies demonstrate the growing understanding of how attention and MLP redundancy can be exploited to create more efficient language models while maintaining performance on complex reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffd1e3cd-15ed-4a9a-a9ff-51836d19776e",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "14ae85e3-965f-458e-a95c-4b5a8b84cfbb",
  "sourceToolAssistantUUID": "ffd1e3cd-15ed-4a9a-a9ff-51836d19776e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T23:34:39.039Z_

<details><summary>↩ Tool result · `toolu_013N1TS61Q8oFBUsjxwjZ7Sf`</summary>

```text
Web search results for query: "dynamic sparsity budget allocation reasoning model decoding"

Links: [{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of ...","url":"https://arxiv.org/pdf/2601.07372"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiv.org/html/2601.07372v1"},{"title":"Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks","url":"https://arxiv.org/html/2508.18672v2"},{"title":"GitHub - deepseek-ai/Engram: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models · GitHub","url":"https://github.com/deepseek-ai/Engram"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiviq.substack.com/p/conditional-memory-via-scalable-lookup"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.01278v1"},{"title":"DeepSeek's Engram Separates Memory from Reasoning in LLM Architecture Breakthrough | Introl Blog","url":"https://introl.com/blog/deepseek-engram-conditional-memory-architecture-january-2026"},{"title":"Conditional Memory via Engram in LLMs","url":"https://www.emergentmind.com/papers/2601.07372"}]

Based on the search results, here's what I found about dynamic sparsity budget allocation and reasoning model decoding:

## Key Research Areas

**Sparsity Allocation in Language Models:**

The sparsity allocation problem asks how capacity should be distributed between MoE experts and memory in a fixed parameter budget. Research has uncovered a U-shaped scaling law, revealing that simple lookup mechanisms act as essential complements to neural computation.

**Dynamic Sparse Attention for Reasoning Models:**

PillarAttn is a dynamic sparse attention mechanism designed for self-speculative decoding that reuses attention scores computed during the verification phase to identify critical tokens for subsequent draft phases. The sparsity pattern adapts continuously to the evolving context, crucial for reasoning language model workloads where reasoning chains can shift topics and focus areas.

**Practical Applications:**

Dynamic budget allocation per layer and head can be controlled by a coverage parameter and minimum budget. A U-curve relationship pinpoints a sweet spot where allocating roughly 20-25% of a model's sparse parameter budget to memory yields optimal performance.

**Improved Inference:**

A lossless, training-free framework combining self-speculative decoding with dynamic sparse attention delivers up to 2.13 times higher throughput by reducing attention execution time by 70%.

The research demonstrates that intelligently allocating computational budget between different types of operations—rather than uniform allocation—significantly improves both efficiency and reasoning performance in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "016b8e46-e6fe-409c-a9e8-c341844cc822",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "40ff224c-17ce-484b-a350-99a352c4d24f",
  "sourceToolAssistantUUID": "016b8e46-e6fe-409c-a9e8-c341844cc822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-11T23:34:39.545Z_

<details><summary>↩ Tool result · `toolu_01Bfqmrw29r3kHgt3UapdV6f`</summary>

```text
Web search results for query: "compute-aware optimization reasoning model inference efficiency 2026"

Links: [{"title":"2025 AI wrapped","url":"https://lambda.ai/blog/2025-ai-wrapped"},{"title":"Efficient Inference for Edge Large Language Models: A Survey","url":"https://www.sciopen.com/article/10.26599/TST.2025.9010166"},{"title":"More compute for AI, not less","url":"https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"Mastering LLM Techniques: Inference Optimization | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/"},{"title":"Baseten Achieves 225% Better Cost-Performance with NVIDIA","url":"https://businessanalytics.substack.com/p/baseten-achieves-225-better-cost"},{"title":"2026: The Year of AI Inference - VAST Data","url":"https://www.vastdata.com/blog/2026-the-year-of-ai-inference"},{"title":"Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization | OpenReview","url":"https://openreview.net/forum?id=0ERw2196o1"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3754448"}]

Based on the search results, here are key findings about compute-aware optimization for reasoning model inference efficiency in 2026:

## Reasoning Model Efficiency Challenges

Frontier reasoning models demand exponentially more compute than traditional language models. DeepSeek-R1's reasoning process requires massive context windows and extended inference chains, and running these on standard GPU infrastructure meant either accepting intolerable latency or allocating so many GPUs per request that the economics broke.

## Compute-Aware Optimization Approaches

Models can be made aware of inference budgets through Inference Budget-Constrained Policy Optimization (IBPO), where models learn to "understand" the difficulty of queries and allocate inference budgets to harder ones.

Some systems employ hybrid symbolic-neural reasoning strategies that dynamically adjust computational depth depending on task complexity, enabling more efficient inference pipelines and lower average computation without compromising performance.

## 2026 Infrastructure Trends

The differentiation in 2026 won't come from access to capabilities, but more likely from an operations perspective. Model architecture evolved dramatically in 2025, with sparse MoE designs becoming the standard approach for achieving frontier performance efficiently, where tokens are routed to specialized "expert" sub-networks, activating only a fraction of total parameters per request.

Trends shaping LLM inference include mixture-of-experts scheduling, efficient reasoning, and energy-aware inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b526888e-9f36-4ce6-86e2-456d17282ccb",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "ec064e1d-72a7-4359-bbf9-ae1cbb31d720",
  "sourceToolAssistantUUID": "b526888e-9f36-4ce6-86e2-456d17282ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T23:34:40.138Z_

<details><summary>↩ Tool result · `toolu_01CGN1evoLAynb3JG86tW26N`</summary>

```text
Web search results for query: "site:arxiv.org reasoning model activation sparsity phase 2026"

Links: [{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"Base Models Know How to Reason, Thinking Models Learn When","url":"https://arxiv.org/html/2510.07364v3"},{"title":"ActivationReasoning: Logical Reasoning in Latent Activation Spaces","url":"https://arxiv.org/html/2510.18184v1"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/html/2509.00454v2"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for ...","url":"https://arxiv.org/pdf/2508.02128"},{"title":"Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks","url":"https://arxiv.org/html/2508.18672v2"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://arxiv.org/html/2411.02335v2"},{"title":"How does Chain of Thought Think? Mechanistic ...","url":"https://arxiv.org/pdf/2507.22928"}]

I've performed the web search for your query on arxiv.org about reasoning model activation sparsity and phase 2026. Here are the key findings:

## Research on Reasoning Models and Activation Sparsity

The search returned several relevant papers from arxiv.org investigating activation sparsity in reasoning models:

1. **"Universal Properties of Activation Sparsity in Modern Large Language Models"** (February 2026) - This paper examines activation sparsity across different model types including reasoning models, highlighting the universal capacity for activation sparsity in pretrained, instruction-tuned, and reasoning models.

2. **"Base Models Know How to Reason, Thinking Models Learn When"** (October 2025) - This work proposes using Sparse Autoencoders (SAEs) where the dictionary dimension represents distinct reasoning mechanisms and sparsity constraints control how many reasoning mechanisms can be simultaneously active.

3. **"Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks"** (September 2025) - This paper investigates how MoE sparsity influences memorization and reasoning skills, finding that determining optimal sparsity of the MoE during pre-training is crucial for training a reasoning model under a fixed compute budget.

4. **"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction"** (September 2025) - This work demonstrates that a reasoning-aware calibration method (RAC) consistently outperforms baseline methods at higher sparsity levels, achieving 66.4% accuracy at 50% sparsity on the 1.5B parameter model compared to 35.6% with standard calibration.

These papers collectively explore how activation sparsity properties emerge in reasoning models and how to leverage them for improved efficiency and performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "663fe488-93a8-46fc-8bbf-a49689597525",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "7f8f8d2d-7883-419e-889f-3f71222fa556",
  "sourceToolAssistantUUID": "663fe488-93a8-46fc-8bbf-a49689597525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-11T23:34:41.446Z_

<details><summary>↩ Tool result · `toolu_01KGf8KARDsY6P23fHkDDArh`</summary>

```text
Web search results for query: "attention head pruning MLP sparsity reasoning LLM 2025 2026"

Links: [{"title":"Attention Heads and MLP Pruning - Efficient LLMs with AMP","url":"https://arxiv.org/pdf/2504.21174"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/html/2504.21174v1"},{"title":"Efficient self-attention with smart pruning for sustainable large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92586-5"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"[2504.21174] Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/abs/2504.21174"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421174G/abstract"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"Compressing and Deploying Efficient LLMs for ...","url":"https://aclanthology.org/2025.emnlp-industry.119.pdf"},{"title":"SPAttention: Structured Sparse Attention","url":"https://www.emergentmind.com/topics/spattention"}]

I've completed the web search for your query about attention head pruning, MLP sparsity, reasoning, and LLMs from 2025-2026. Here are the key findings:

## Main Research Areas

**Structured Pruning Methods:**

AMP (Attention Heads and MLP Pruning) is a novel structured pruning method that efficiently compresses LLMs by removing less critical structures within Multi-Head Attention (MHA) and Multilayer Perceptron (MLP). AMP surpasses current state-of-the-art on commonsense reasoning tasks by up to 1.49 percentage points, achieving a 30% pruning ratio with minimal impact on zero-shot task performance.

**Sparsity Approaches:**

Recent compression techniques have successfully compressed transformer layers by 99% and linear layers by 70%, resulting in an overall model compression of around 70%, while maintaining nearly the same accuracy. With moderate compression rates of 20% to 40%, model performance not only remained stable but even improved.

**Test-Time Scaling and Reasoning:**

Recent findings challenge the conventional notion that pruning always reduces test-time scaling (TTS) performance and suggest that carefully undertaken pruning can improve TTS effectiveness even further. This is particularly relevant for reasoning LLMs that use chain-of-thought approaches.

**Sparse Attention Techniques:**

Recent methods seek to reduce the computational and memory footprint of self-attention, particularly for large context LLMs, with approaches constraining attention heads by statically partitioning the allowable query-key distances into exclusive, contiguous bands.

The research shows significant progress in efficiently compressing LLMs while maintaining or even improving performance on reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b461e76a-91c3-42da-a51c-a7b6bf8ae1b7",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "e7d3d484-6efd-4b1b-a58c-36bd97c69588",
  "sourceToolAssistantUUID": "b461e76a-91c3-42da-a51c-a7b6bf8ae1b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T23:34:42.763Z_

<details><summary>↩ Tool result · `toolu_01Js8NziWgipjpa9KWjQAX23`</summary>

```text
Web search results for query: "DeepSeek-R1 inference optimization sparsity 2026"

Links: [{"title":"DeepSeek Training and Inference Optimization Research","url":"https://www.aussieai.com/research/deepseek"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"One More Thing: DeepSeek-V3/R1 Inference System ...","url":"https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"Aman's AI Journal • Primers • DeepSeek-R1","url":"https://aman.ai/primers/ai/deepseek-R1/"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via","url":"https://arxiv.org/pdf/2501.12948"},{"title":"deepseek-r1","url":"https://lmstudio.ai/models/deepseek-r1"},{"title":"A new GPT-OSS benchmark and DeepSeek R1 updates for latency-optimized reasoning - MLCommons","url":"https://mlcommons.org/2026/03/mlperf-inference-gpt-oss/"},{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"}]

Based on the search results, here's what I found about DeepSeek-R1 inference optimization and sparsity in 2026:

## Key Inference Optimizations

DeepSeek-R1 uses several inference optimization techniques including single-step reasoning and Multi-head Latent Attention (MLA), an optimization to the attention module that was introduced in their V2 model but improved in R1.

## Sparsity in the Architecture

DeepSeek-V3/R1 features high sparsity with only 8 out of 256 experts per layer activated, which necessitates an extremely large overall batch size. This high sparsity ensures sufficient batch size per expert, enabling higher throughput and lower latency.

## Recent Advances (April 2026)

In April 2026, DeepSeek introduced DeepSeek-V4 with a new hybrid attention system called Compressed Sparse Attention (CSA), where small chunks of tokens are compressed into summary representations, and each new token only attends to the most relevant summaries via top-k selection. In a 1M-token context, DeepSeek-V4-Pro uses only 27% of the inference FLOPs and 10% of the KV cache compared to DeepSeek-V3.2, while DeepSeek-V4-Flash reaches 10% of the FLOPs and 7% of the KV cache.

## Benchmarking Updates (March 2026)

MLPerf Inference v6.0 expands coverage with a new GPT-OSS 120B benchmark and a latency-constrained interactive scenario for DeepSeek-R1, marking the first MLPerf standard for speculative decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9b36914-cd7e-4855-9878-4ab6d4a38c22",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "8b23d221-9dad-42d2-82d9-c3c3ee6a10ed",
  "sourceToolAssistantUUID": "a9b36914-cd7e-4855-9878-4ab6d4a38c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:34:42.827Z_

<details><summary>↩ Tool result · `toolu_01NcbMBz9FDwpJnWA5oWcZMe`</summary>

```text
Web search results for query: "site:arxiv.org adaptive inference sparsity chain-of-thought 2025"

Links: [{"title":"Rethinking Dense Sequential Chains: Reasoning Language Models Can Extract Answers from Sparse, Order-Shuffling Chain-of-Thoughts","url":"https://arxiv.org/html/2605.07307"},{"title":"1 Introduction","url":"https://arxiv.org/html/2512.01278"},{"title":"Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework","url":"https://arxiv.org/html/2509.14093v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"Adaptive Graph of Thoughts: Test-Time Adaptive Reasoning Unifying Chain, Tree, and Graph Structures","url":"https://arxiv.org/html/2502.05078v1"},{"title":"MSAO: Adaptive Modality Sparsity-Aware Offloading with Edge-Cloud Collaboration for Efficient Multimodal LLM Inference","url":"https://arxiv.org/html/2604.02945v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.03152"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v3"},{"title":" Abstract— In order to address the chain of thought in the","url":"https://arxiv.org/pdf/2411.09111"}]

I've successfully performed the web search for "site:arxiv.org adaptive inference sparsity chain-of-thought 2025". Here are the key results:

## Search Results Summary

The search returned several highly relevant papers from arXiv focusing on adaptive inference, sparsity, and chain-of-thought reasoning:

1. **"Rethinking Dense Sequential Chains: Reasoning Language Models Can Extract Answers from Sparse, Order-Shuffling Chain-of-Thoughts"** (4 days ago)
   - Demonstrates that randomly permuting lines of reasoning chains reduces accuracy by less than 0.5 percentage points, and word-level shuffling retains 62%–89% accuracy on AIME 2025

2. **"SparseSpec" - Speculative Decoding with Dynamic Sparse Attention** (December 1, 2025)
   - Introduces PillarAttn, which selectively loads critical tokens with highest attention scores, achieving sparsity that adapts to various contexts

3. **"Reasoning Efficiently Through Adaptive Chain-of-Thought Compression"** (September 17, 2025)
   - Advanced frameworks have reduced CoT lengths by 45%–80% while preserving accuracy and delivering 1.6 to 2 times speedups in inference

4. **"ThinKV: Thought-Adaptive KV Cache Compression"** (October 1, 2025)
   - Decomposes chains of thought into reasoning, execution, and transition segments, enabling thought-aware quantization and eviction

5. **"Adaptive Graph of Thoughts"** (February 7, 2025)
   - Recursively decomposes complex queries into structured subproblems, selectively expanding only those requiring further analysis

These papers collectively explore how sparsity can be exploited in chain-of-thought reasoning to improve inference efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d573d7bf-2d6d-43d0-bb05-3694350bf393",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "42357094-09d9-46e3-801b-236bb67f8cbf",
  "sourceToolAssistantUUID": "d573d7bf-2d6d-43d0-bb05-3694350bf393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:34:43.844Z_

<details><summary>↩ Tool result · `toolu_01LRc2QxrDsCT55XQhfENPoX`</summary>

```text
Web search results for query: "site:openreview.net phase adaptive sparsity reasoning 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/9fc57250e45024249568c5a60d093f2c24f21d52.pdf"},{"title":"How Weight Pruning Destroys Chain-of-Thought Reasoning in ...","url":"https://openreview.net/pdf?id=oSXI5Fk3rP"},{"title":"SparsyFed: SPARSE ADAPTIVE FEDERATED TRAINING","url":"https://openreview.net/pdf?id=OBUQNASaWw"},{"title":"Sparsity-aware distributed learning (Chapter 2) - Big Data over Networks","url":"https://openreview.net/attachment?id=eyMhhU6VSqC&name=pdf"},{"title":"A Fast and Provable Algorithm for Sparse Phase Retrieval | OpenReview","url":"https://openreview.net/forum?id=BlkxbI6vzl"},{"title":"Make Mathematical Reasoning Adaptive | OpenReview","url":"https://openreview.net/forum?id=RUYGpYWVfw"},{"title":"Sparse Reasoning is Enough: Biological-Inspired Framework for Abnormal Event Detection with Large Pre-trained Models | OpenReview","url":"https://openreview.net/forum?id=Cey11tjiSv"},{"title":"Dynamic Sparse Training with Structured Sparsity | OpenReview","url":"https://openreview.net/forum?id=kOBkxFRKTA"},{"title":"Dynamic Sparsity Is Channel-Level Sparsity Learner | OpenReview","url":"https://openreview.net/forum?id=C6IIwFHWkF&noteId=VznqcOglQX"},{"title":"Layer-adaptive Sparsity for the Magnitude-based Pruning | OpenReview","url":"https://openreview.net/forum?id=H6ATjJ0TKdf"}]

I found several results on OpenReview related to sparsity and reasoning. Here are the most relevant papers from your search:

## Most Relevant Results:

**1. Sparse and Universal Sparsity in Language Models (ICLR 2026)**
The design of FASA (Frequency-Adaptive Sparsity Allocation) is rooted in an observation that differential frequencies within RoPE induce functional sparsity among frequency chunks (FCs). FASA excels at long-CoT reasoning, surpasses baseline methods including R-KV (a specialized method for CoT compression), and achieves an impressive 86.4% accuracy on 10% context budget.

**2. How Weight Pruning Destroys Chain-of-Thought Reasoning**
The paper proposes Adaptive Sparsity-Adjusted Normalized Distance (ASAND), designed to robustly correlate weight changes with reasoning fidelity loss. Adaptive, sparsity-aware measures such as ASAND achieve strong correlation with output fidelity by incorporating structural sensitivity and magnitude-aware weighting, emphasizing the importance of designing similarity metrics that account for sparsity for reasoning tasks.

**3. Sparse Reasoning for Abnormal Event Detection (ReCoAED)**
ReCoAED reaches state-of-the-art training-free performance while reasoning on only 28.55%/16.04% of frames used by previous methods, showing that sparse reasoning is sufficient for effective large-model-based anomaly detection.

**4. SparsyFed: Adaptive Sparse Federated Training**
SparsyFed is an adaptive sparse training method for federated learning that prunes activations with an adaptive layer-wise method and model weights using target sparsity.

These papers address various aspects of phase-adaptive and task-adaptive sparsity approaches for efficient reasoning and neural network training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90d971ad-8098-405e-ab30-d075b42010cc",
  "isSidechain": true,
  "promptId": "adb29825-742d-40c1-aacd-587611a850ec",
  "agentId": "af320cd6db7e1c763",
  "type": "user",
  "uuid": "33a6fd2d-1a0b-4689-b25a-210c93fca6b2",
  "sourceToolAssistantUUID": "90d971ad-8098-405e-ab30-d075b42010cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:36:27.441Z_

Here is my consolidated report across all 10 searches.

---

## Literature Search Results for PAJS (Phase-Adaptive Joint Sparsity)

### Search 1: "phase-aware sparsity reasoning model inference 2025 2026"

**Top relevant results:**

1. **FASA: Frequency-Aware Sparsity for Attention** (ICLR 2026) -- Exploits frequency-based functional sparsity in RoPE to compress KV caches. Achieves 8x KV cache compression and 2.6x speedups. Explicitly evaluated on long chain-of-thought reasoning. Very relevant as a competing KV-cache sparsity method, though it does not differentiate between thinking vs. answer phases. [Paper](https://arxiv.org/pdf/2602.03152)

2. **The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs** (2025) -- Broad empirical study of sparse attention trade-offs across transformer LLMs. [Paper](https://arxiv.org/pdf/2504.17768)

3. **ICLR 2025 Workshop on Sparsity in LLMs (SLLM)** -- Covers MoE, quantization, hardware, and inference sparsity. [Link](https://iclr.cc/virtual/2025/workshop/23996)

---

### Search 2: "adaptive compute sparsity thinking tokens LLM 2025 2026"

**Top relevant results:**

1. **SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning** (2025) -- Learns to allocate thinking-token budgets adaptively per query. Directly addresses the "overthinking" problem. Relevant to PAJS's motivation but focuses on token-count budgeting rather than architectural sparsity. [Paper](https://arxiv.org/html/2505.11274v6)

2. **Adaptive Test-Time Compute Allocation via Constrained Policy Optimization** (2026) -- Models learn inference budgets through IBPO (Inference Budget-Constrained Policy Optimization), allocating more compute to harder queries. [Paper](https://arxiv.org/html/2604.14853v1)

3. **Adaptive Thinking: LLMs Know When to Think in Latent Space** (OpenReview) -- Proposes latent-space thinking with adaptive switching. [Link](https://openreview.net/forum?id=2i6Rp0gCq6)

4. **QTALE: Quantization-Robust Token-Adaptive Layer Execution** (2026) -- Adaptive layer execution per token, combining quantization with dynamic compute. [Paper](https://arxiv.org/html/2602.10431v1)

5. **Adaptive Layer-skipping in Pre-trained LLMs** (2025) -- Dynamically skips layers for efficiency. [Paper](https://arxiv.org/abs/2503.23798)

---

### Search 3: "joint attention MLP sparsity reasoning models"

**Top relevant results:**

1. **RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning** (ACL Findings 2025) -- **Highly relevant.** Identifies a new "milestone token" attention pattern during reasoning decoding and proposes reasoning-aware sparse attention. Specifically targets reasoning models. However, focuses on attention-side KV sparsity only, not joint attention+MLP. [Paper](https://arxiv.org/abs/2502.11147)

2. **AMP: Attention Heads and MLP Pruning** (2025) -- **Directly relevant to the "joint" claim of PAJS.** Proposes structured pruning of both attention heads and MLP neurons jointly. Achieves 30% pruning with minimal accuracy loss. However, it is not phase-aware (does not differentiate thinking vs. answer). [Paper](https://arxiv.org/abs/2504.21174)

3. **JoMA: Joint Dynamics of MLP and Attention** (2023) -- Theoretical framework for understanding joint MLP/attention training dynamics. Foundational but not an inference method. [Paper](https://arxiv.org/abs/2310.00535)

4. **"What Matters in Transformers? Not All Attention is Needed"** (ICLR 2025) -- Shows attention layers have high redundancy and can be dropped jointly with MLP layers. [Paper](https://arxiv.org/html/2406.15786v6)

---

### Search 4: "dynamic sparsity budget allocation reasoning model decoding"

**Top relevant results:**

1. **Sparse Self-Speculative Decoding (SparseSpec/PillarAttn)** (Dec 2025) -- **Highly relevant.** Introduces dynamic sparse attention for reasoning model inference via self-speculative decoding. PillarAttn reuses attention scores from the verification phase to identify critical tokens for drafting, with sparsity adapting to context. Achieves 2.13x throughput, 70% attention time reduction. Training-free. [Paper](https://arxiv.org/abs/2512.01278)

2. **Engram: Conditional Memory via Scalable Lookup** (DeepSeek, Jan 2026) -- Introduces a new sparsity axis (memory vs. reasoning) with a U-shaped scaling law showing 20-25% memory allocation is optimal. [Paper](https://arxiv.org/html/2601.07372v1)

3. **Optimal Sparsity of MoE Language Models for Reasoning Tasks** (2025) -- Investigates how MoE sparsity affects reasoning vs. memorization, finding optimal sparsity levels during pre-training. [Paper](https://arxiv.org/html/2508.18672v2)

---

### Search 5: "compute-aware optimization reasoning model inference efficiency 2026"

**Top relevant results:**

1. **Think Smarter not Harder: Adaptive Reasoning with Inference-Aware Optimization** (OpenReview) -- Models learn to modulate reasoning depth based on inference budget constraints. [Link](https://openreview.net/forum?id=0ERw2196o1)

2. **DeepSeek-V4 Compressed Sparse Attention (CSA)** (April 2026) -- DeepSeek's newest architecture uses compressed sparse attention with top-k summary selection. Uses only 27% FLOPs and 10% KV cache vs. V3.2 in 1M-token contexts. Major industry competitor. [Link](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)

3. **Efficient Inference for Edge LLMs Survey** (2025) -- Comprehensive survey of LLM inference efficiency on edge devices. [Paper](https://www.sciopen.com/article/10.26599/TST.2025.9010166)

---

### Search 6: "site:arxiv.org reasoning model activation sparsity phase 2026"

**Top relevant results:**

1. **Universal Properties of Activation Sparsity in Modern LLMs** (Feb 2026) -- **Very relevant.** Characterizes activation sparsity across pretrained, instruction-tuned, and reasoning models. Shows universal capacity for activation sparsity. Could serve as a theoretical foundation or competing empirical study for PAJS. [Paper](https://arxiv.org/html/2509.00454v2)

2. **Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction** (Sep 2025) -- **Directly relevant.** Proposes RAC (Reasoning-Aware Calibration) for pruning reasoning models. Achieves 66.4% accuracy at 50% sparsity vs. 35.6% with standard calibration. Reasoning-aware but not phase-differentiated. [Paper](https://arxiv.org/html/2509.12464v1)

3. **Sparsing Law: Towards LLMs with Greater Activation Sparsity** (2024/2025) -- Establishes scaling laws for activation sparsity in LLMs. [Paper](https://arxiv.org/html/2411.02335v2)

4. **Optimal Sparsity of MoE for Reasoning Tasks** (Sep 2025) -- Studies optimal MoE sparsity for balancing memorization and reasoning. [Paper](https://arxiv.org/html/2508.18672v2)

5. **Amber Pruner: Leveraging N:M Activation Sparsity** (2025) -- Hardware-friendly structured activation sparsity using N:M patterns. [Paper](https://arxiv.org/pdf/2508.02128)

---

### Search 7: "site:arxiv.org adaptive inference sparsity chain-of-thought 2025"

**Top relevant results:**

1. **ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models** (Oct 2025) -- **Most directly competing work.** Decomposes chains of thought into reasoning, execution, and transition segments (i.e., explicit phase decomposition) and applies thought-aware quantization and eviction. This is phase-aware sparsity for reasoning models, though focused on KV cache rather than joint attention+MLP activation sparsity. [Paper](https://arxiv.org/html/2510.01290v1)

2. **Reasoning Efficiently Through Adaptive Chain-of-Thought Compression** (Sep 2025) -- Reduces CoT lengths by 45-80% while preserving accuracy with 1.6-2x speedups. [Paper](https://arxiv.org/html/2509.14093v1)

3. **Rethinking Dense Sequential Chains** (May 2026) -- Shows reasoning models can extract answers from sparse, order-shuffled CoT, suggesting significant redundancy in reasoning chains. [Paper](https://arxiv.org/html/2605.07307)

4. **SparseSpec: Speculative Decoding with Dynamic Sparse Attention** (Dec 2025) -- Already noted above; dynamic sparse attention for reasoning model decoding. [Paper](https://arxiv.org/abs/2512.01278)

---

### Search 8: "attention head pruning MLP sparsity reasoning LLM 2025 2026"

**Top relevant results:**

1. **AMP: Efficient LLMs with Attention Heads and MLP Pruning** (Apr 2025) -- **Key competing work for the "joint" aspect.** Jointly prunes attention heads and MLP structures with up to 30% compression and minimal reasoning accuracy loss (up to +1.49pp on commonsense reasoning). [Paper](https://arxiv.org/abs/2504.21174)

2. **Doing More With Less: Revisiting Effectiveness of LLM Pruning for Test-Time Scaling** (2026) -- **Directly relevant.** Challenges the assumption that pruning always hurts test-time scaling, showing carefully undertaken pruning can improve reasoning effectiveness. [Paper](https://arxiv.org/html/2604.25098)

3. **"What Matters in Transformers?" (ICLR 2025)** -- Shows attention layers are more droppable than MLP layers, providing guidance for where sparsity should be allocated. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf)

---

### Search 9: "DeepSeek-R1 inference optimization sparsity 2026"

**Top relevant results:**

1. **DeepSeek-V4 with Compressed Sparse Attention (CSA)** (April 2026) -- New hybrid attention system where tokens are compressed into summary representations with top-k selection. 27% FLOPs, 10% KV cache vs. V3.2. [Link](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)

2. **MLPerf Inference v6.0 DeepSeek-R1 Benchmark** (March 2026) -- First MLPerf standard for speculative decoding, includes latency-constrained interactive scenario for R1. [Link](https://mlcommons.org/2026/03/mlperf-inference-gpt-oss/)

3. **DeepSeek Inference System Overview** (Feb 2025) -- Official documentation of R1's inference architecture, including MoE sparsity (8/256 experts activated). [Link](https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md)

4. **DeepSeek Engram** (Jan 2026) -- Separates memory from reasoning via conditional memory lookup sparsity. [Paper](https://arxiv.org/html/2601.07372v1)

---

### Search 10: "site:openreview.net phase adaptive sparsity reasoning 2026"

**Top relevant results:**

1. **FASA (ICLR 2026)** -- Already noted; frequency-aware sparsity for attention with strong long-CoT results (86.4% accuracy at 10% context budget). [Link](https://openreview.net/pdf/9fc57250e45024249568c5a60d093f2c24f21d52.pdf)

2. **How Weight Pruning Destroys Chain-of-Thought Reasoning** -- Proposes ASAND (Adaptive Sparsity-Adjusted Normalized Distance), showing that sparsity-aware similarity metrics are needed to predict reasoning fidelity loss from pruning. [Link](https://openreview.net/pdf?id=oSXI5Fk3rP)

3. **Make Mathematical Reasoning Adaptive** (OpenReview) -- Adaptive mathematical reasoning with dynamic compute allocation. [Link](https://openreview.net/forum?id=RUYGpYWVfw)

---

## Summary: Papers Most Threatening to PAJS Novelty

The following papers overlap most with PAJS's core claims. I rank them by relevance:

| Priority | Paper | Why it matters |
|----------|-------|----------------|
| **1 (highest)** | **ThinKV** (Oct 2025) | Explicitly decomposes CoT into reasoning phases (reasoning/execution/transition) and applies phase-specific compression. Closest to PAJS's "phase-aware" claim, though limited to KV cache. |
| **2** | **AMP** (Apr 2025) | Joint attention head + MLP pruning -- exactly the "joint sparsity" axis of PAJS. Not phase-aware, but directly competes on the joint architecture sparsity claim. |
| **3** | **RaaS** (ACL 2025) | Reasoning-aware attention sparsity that identifies milestone tokens during reasoning. Phase-aware on the attention side but not joint with MLP. |
| **4** | **Doing More With Less** (2026) | Shows pruning can actually improve test-time scaling for reasoning models, directly challenging assumptions about sparsity hurting reasoning. |
| **5** | **SparseSpec / PillarAttn** (Dec 2025) | Dynamic sparse attention that adapts to context during reasoning model decoding. Training-free, 2.13x throughput. |
| **6** | **Reasoning Models Can Be Pruned via CoT Reconstruction** (Sep 2025) | Reasoning-aware calibration for pruning. Shows reasoning-specific calibration is critical for maintaining accuracy under sparsity. |
| **7** | **Universal Properties of Activation Sparsity** (Feb 2026) | Empirically characterizes activation sparsity across reasoning models -- could undermine or support PAJS's theoretical motivation. |
| **8** | **FASA** (ICLR 2026) | State-of-the-art KV cache sparsity with strong CoT reasoning results. Competing efficiency method. |
| **9** | **SelfBudgeter** (2025) | Adaptive thinking-token budget allocation. Competes on the "adaptive compute for reasoning" angle but at the token-count level. |

**Key gap analysis for PAJS:** No paper found combines all three of: (a) explicit thinking-vs-answer phase differentiation, (b) joint attention head + MLP activation sparsity, and (c) dynamic budget allocation across those phases. ThinKV comes closest on phase-awareness but only targets KV cache. AMP comes closest on joint attention+MLP but is not phase-aware. PAJS's novelty appears to lie in the intersection of these axes, but the authors must carefully position against ThinKV, AMP, and RaaS, which each cover significant portions of the claimed contribution space.

Sources:
- [FASA (ICLR 2026)](https://arxiv.org/pdf/2602.03152)
- [The Sparse Frontier](https://arxiv.org/pdf/2504.17768)
- [SLLM Workshop ICLR 2025](https://iclr.cc/virtual/2025/workshop/23996)
- [SelfBudgeter](https://arxiv.org/html/2505.11274v6)
- [Adaptive Test-Time Compute Allocation](https://arxiv.org/html/2604.14853v1)
- [Adaptive Thinking (OpenReview)](https://openreview.net/forum?id=2i6Rp0gCq6)
- [QTALE](https://arxiv.org/html/2602.10431v1)
- [Adaptive Layer-skipping](https://arxiv.org/abs/2503.23798)
- [RaaS: Reasoning-Aware Attention Sparsity](https://arxiv.org/abs/2502.11147)
- [AMP: Attention Heads and MLP Pruning](https://arxiv.org/abs/2504.21174)
- [JoMA](https://arxiv.org/abs/2310.00535)
- [What Matters in Transformers](https://arxiv.org/html/2406.15786v6)
- [SparseSpec / PillarAttn](https://arxiv.org/abs/2512.01278)
- [Engram (DeepSeek)](https://arxiv.org/html/2601.07372v1)
- [Optimal Sparsity of MoE for Reasoning](https://arxiv.org/html/2508.18672v2)
- [Think Smarter not Harder (OpenReview)](https://openreview.net/forum?id=0ERw2196o1)
- [DeepSeek-V4 CSA](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [Universal Properties of Activation Sparsity](https://arxiv.org/html/2509.00454v2)
- [Reasoning Models Can Be Pruned via CoT Reconstruction](https://arxiv.org/html/2509.12464v1)
- [Sparsing Law](https://arxiv.org/html/2411.02335v2)
- [Amber Pruner](https://arxiv.org/pdf/2508.02128)
- [ThinKV: Thought-Adaptive KV Cache Compression](https://arxiv.org/html/2510.01290v1)
- [Adaptive CoT Compression](https://arxiv.org/html/2509.14093v1)
- [Rethinking Dense Sequential Chains](https://arxiv.org/html/2605.07307)
- [Doing More With Less: Pruning for Test-Time Scaling](https://arxiv.org/html/2604.25098)
- [What Matters in Transformers (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf)
- [MLPerf Inference v6.0 R1 Benchmark](https://mlcommons.org/2026/03/mlperf-inference-gpt-oss/)
- [DeepSeek Inference System Overview](https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md)
- [How Weight Pruning Destroys CoT Reasoning](https://openreview.net/pdf?id=oSXI5Fk3rP)
- [Make Mathematical Reasoning Adaptive](https://openreview.net/forum?id=RUYGpYWVfw)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a6fd2d-1a0b-4689-b25a-210c93fca6b2",
  "isSidechain": true,
  "agentId": "af320cd6db7e1c763",
  "requestId": "req_011Cawf6LyaQ7YVMHJhumDpp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed3811d5-2ee6-4e15-8949-6974e821bb93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "aebee51c-c868-4321-83fa-0353616d45fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AusisKkUSbiNUpePsgc6DU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9780,
      "cache_read_input_tokens": 10575,
      "output_tokens": 5106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5106,
          "cache_read_input_tokens": 10575,
          "cache_creation_input_tokens": 9780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9780,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
