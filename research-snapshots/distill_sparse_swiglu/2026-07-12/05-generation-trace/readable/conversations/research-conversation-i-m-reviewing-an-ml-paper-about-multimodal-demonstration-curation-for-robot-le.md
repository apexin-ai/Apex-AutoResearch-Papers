# Research conversation: I'm reviewing an ML paper about multimodal demonstration curation for robot learning (VLA training). The paper claims to

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a99fa48a1385f86f4.jsonl`
- **Structured JSON:** [`635affa182256643a001.json`](../../sessions/63/635affa182256643a001.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

65 recorded events

### User

_source line 1 · 2026-05-13T19:38:11.690Z_

I'm reviewing an ML paper about multimodal demonstration curation for robot learning (VLA training). The paper claims to be the first to provide task-level diagnostics for when proprioceptive scoring helps demonstration curation. I need to find competing work the authors may have missed.

Please search for ALL of the following (use WebSearch for each):

1. "demonstration curation multimodal scoring 2025 2026" - any recent work on multimodal demo curation
2. "proprioception data quality robot learning 2025 2026" - proprioceptive quality assessment
3. "visual observability robot manipulation scoring 2025 2026" - visual observability metrics
4. "when does multimodal fusion help robot" - modality selection for robotics
5. "data filtering robot imitation learning 2026" - recent data filtering methods
6. "demonstration quality assessment ranking robot 2026" - quality ranking methods
7. "site:arxiv.org multimodal demonstration curation VLA 2026" - arxiv-specific search
8. "site:arxiv.org proprioceptive scoring robot data quality" - proprioceptive scoring
9. "observation modality selection manipulation policy" - modality selection
10. "reward model demonstration quality robot manipulation 2026" - reward models for demo quality

For each search, report the most relevant papers found, especially any that:
- Provide task-level diagnostics for modality selection in curation
- Combine proprioception with vision for scoring demonstrations
- Map observability across large task suites
- Use ranking theory for demonstration curation

Report paper titles, venues, dates, and brief descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "f49d159f-75e0-4753-93ef-2eb8e0ccf893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:38:11.697Z_

```json
{
  "parentUuid": "f49d159f-75e0-4753-93ef-2eb8e0ccf893",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "869371af-346f-460c-8ae5-b41ef5e68ecc",
  "timestamp": "2026-05-13T19:38:11.697Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:38:17.527Z_



I'll run all 10 searches in parallel to find competing work. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "869371af-346f-460c-8ae5-b41ef5e68ecc",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18g7zabRdmKnuoDDWDg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74616273-bec6-4c9c-a106-e2d00da14774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYAmdxT9KPZ9dPJB1zjzGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 912,
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

_source line 4 · 2026-05-13T19:38:17.932Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SrunHK3mBdBJDboc5rEszS`</summary>

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
  "parentUuid": "74616273-bec6-4c9c-a106-e2d00da14774",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18g7zabRdmKnuoDDWDg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7e2f610-9fc6-4cc4-bd98-70a5387d86e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYAmdxT9KPZ9dPJB1zjzGZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 912,
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

_source line 5 · 2026-05-13T19:38:17.936Z_

<details><summary>↩ Tool result · `toolu_01SrunHK3mBdBJDboc5rEszS`</summary>

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
  "parentUuid": "c7e2f610-9fc6-4cc4-bd98-70a5387d86e0",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "d2b4993c-b5ce-45bf-9772-145e8248a5c8",
  "sourceToolAssistantUUID": "c7e2f610-9fc6-4cc4-bd98-70a5387d86e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:38:20.900Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2b4993c-b5ce-45bf-9772-145e8248a5c8",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a081c933-e665-483f-a4d8-097b1cf3100c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 7 · 2026-05-13T19:38:21.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NQ3pZkRWYSU6cZUdhqRwUW`</summary>

```json
{
  "query": "demonstration curation multimodal scoring 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a081c933-e665-483f-a4d8-097b1cf3100c",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12468c9d-6e0c-46c6-b332-7c88c2832add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 8 · 2026-05-13T19:38:22.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MzWVMKkQRU6LgWGDbBQQ16`</summary>

```json
{
  "query": "proprioception data quality robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12468c9d-6e0c-46c6-b332-7c88c2832add",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0044312d-0d3e-48f1-9f08-a341ed7f051f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 9 · 2026-05-13T19:38:22.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VqEUeLuzk65z7vRcoUgHqG`</summary>

```json
{
  "query": "visual observability robot manipulation scoring 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0044312d-0d3e-48f1-9f08-a341ed7f051f",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab3a1e88-4cbe-4cb8-b0c3-5acab8ee93f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 10 · 2026-05-13T19:38:23.870Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UGkHixHs5XeyAF4cM8LWn`</summary>

```json
{
  "query": "when does multimodal fusion help robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab3a1e88-4cbe-4cb8-b0c3-5acab8ee93f7",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31535f48-870c-49f9-91a0-553cf13b91c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 11 · 2026-05-13T19:38:24.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DY3tQsFJSpP3cnxcn5uSdp`</summary>

```json
{
  "query": "data filtering robot imitation learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31535f48-870c-49f9-91a0-553cf13b91c4",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2b26a9a-8156-4ecc-b8db-62bc58fbc3a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 12 · 2026-05-13T19:38:24.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QdQhs99FzoRKvxPkctKLVd`</summary>

```json
{
  "query": "demonstration quality assessment ranking robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2b26a9a-8156-4ecc-b8db-62bc58fbc3a5",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d9ab784-13f1-4a5b-89aa-4b78b0bed397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 13 · 2026-05-13T19:38:25.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GVw1rrsxV1GzCRBZZQ3sPz`</summary>

```json
{
  "query": "multimodal demonstration curation VLA 2026",
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
  "parentUuid": "7d9ab784-13f1-4a5b-89aa-4b78b0bed397",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0429796f-62d7-410d-834a-71d0e88466bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 14 · 2026-05-13T19:38:26.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QPqvBr7E7QxVYGjbd4sTD7`</summary>

```json
{
  "query": "proprioceptive scoring robot data quality",
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
  "parentUuid": "0429796f-62d7-410d-834a-71d0e88466bb",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db7a9146-8a7c-4a6b-9292-03950e451ae4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 15 · 2026-05-13T19:38:26.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ST14BdmrUQAS8F53Krz6jy`</summary>

```json
{
  "query": "observation modality selection manipulation policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db7a9146-8a7c-4a6b-9292-03950e451ae4",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74f0bb74-867d-43e3-b086-e5fe8b8cc28c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 16 · 2026-05-13T19:38:27.090Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QM2uaFjvqDFfrS3KaFTf6j`</summary>

```json
{
  "query": "reward model demonstration quality robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74f0bb74-867d-43e3-b086-e5fe8b8cc28c",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18gUsSmg3NDg4CRx8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b98e4b94-16ba-426b-8cf6-f295378d4213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKyD586rLi8t3VNiip69fQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 9135,
      "output_tokens": 516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 516,
          "cache_read_input_tokens": 9135,
          "cache_creation_input_tokens": 1419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1419,
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

_source line 17 · 2026-05-13T19:38:29.165Z_

<details><summary>↩ Tool result · `toolu_01NQ3pZkRWYSU6cZUdhqRwUW`</summary>

```text
Web search results for query: "demonstration curation multimodal scoring 2025 2026"

Links: [{"title":"Multimodal Data Curation Through Ranked Retrieval","url":"https://arxiv.org/html/2605.01163v1"},{"title":"[2511.21662] Multi-Crit: Benchmarking Multimodal Judges on Pluralistic Criteria-Following","url":"https://arxiv.org/abs/2511.21662"},{"title":"ICLR 2026 Trends: Agentic AI, Multimodal Models & Data Governance","url":"https://encord.com/iclr-2026/"},{"title":"1 Introduction","url":"https://arxiv.org/html/2605.02290v1"},{"title":"Data curation via joint example selection further accelerates multimodal learning | OpenReview","url":"https://openreview.net/forum?id=xqpkzMfmQ5"},{"title":"KnowledgeMR@CVPR26","url":"https://knowledgemr-workshop.github.io/"},{"title":"Multimodal Reward Models","url":"https://www.emergentmind.com/topics/multimodal-reward-models"},{"title":"10 Best Data Curation Tools for Computer Vision [2026]","url":"https://www.lightly.ai/blog/best-data-curation-tools"},{"title":"AI Frontiers 2026-03-04 Phi-4-reasoning-vision-15B Technical Report","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report.pdf"},{"title":"The Second Workshop on Evaluation for Multimodal Generation | EvalMG26 @ SIGIR 2026","url":"https://evalmg.github.io/"}]

Based on the search results, here's what I found about demonstration curation, multimodal scoring, and related topics in 2025-2026:

## Key Research Areas

**Multimodal Data Curation:**
Better-curated multimodal data blends should yield more informative supervision and lower validation perplexity. The Expert Embedding Engine (EEE) approach combines complementary embedding experts and reduces modality-driven separation, collapsing the modality gap by over 90% on average and outperforming traditional curation baselines.

**Demonstration Quality and Selection:**
Recent studies like S1 and LIMO have adopted a curation-based approach, which first generates complete candidate reasoning traces from multiple teacher models and then selects high-quality ones for distillation.

**Multimodal Scoring and Evaluation:**
Multi-Crit is a benchmark for evaluating multimodal judges on their capacity to follow pluralistic criteria, built through a rigorous data curation pipeline that gathers challenging response pairs with multi-criterion human annotations. It introduces three novel metrics for assessing pluralistic adherence, criterion-switching flexibility, and the ability to recognize criterion-level preference conflicts.

**Industry Trends:**
The bottleneck in AI development is now the curation, annotation, and labeling of high-fidelity training distributions. Teams are prioritizing smarter selection, cleaner labels, and tighter feedback loops between data and model performance rather than simply collecting larger datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12468c9d-6e0c-46c6-b332-7c88c2832add",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "f01f80b4-400f-450e-9549-2ccefb2ea941",
  "sourceToolAssistantUUID": "12468c9d-6e0c-46c6-b332-7c88c2832add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T19:38:30.318Z_

<details><summary>↩ Tool result · `toolu_01VqEUeLuzk65z7vRcoUgHqG`</summary>

```text
Web search results for query: "visual observability robot manipulation scoring 2025 2026"

Links: [{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"Robot Manipulation Based on Embodied Visual Perception: A Survey - Wang - 2025 - CAAI Transactions on Intelligence Technology - Wiley Online Library","url":"https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cit2.70022"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Ai et al., Sci. Robot. 10, eadt1497 (2025) 17 September 2025","url":"https://albertboai.com/assets/pdf/2025_scirobotics.adt1497.pdf"},{"title":"GitHub - Psi-Robot/Awesome-VLA-Papers: Paper list in the survey: A Survey on Vision-Language-Action Models: An Action Tokenization Perspective · GitHub","url":"https://github.com/Psi-Robot/Awesome-VLA-Papers"},{"title":"GitHub - HCPLab-SYSU/Embodied_AI_Paper_List: [Embodied-AI-Survey-2025] Paper List and Resource Repository for Embodied AI · GitHub","url":"https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"},{"title":"Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives","url":"https://arxiv.org/html/2512.22983v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Frontiers | Multimodal perception-driven decision-making for human-robot interaction: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1604472/full"}]

Based on the search results, here's what I found regarding visual observability and robot manipulation scoring in 2025-2026:

## Key Research Areas

Visual perception is critical in robotic operations, particularly in collaborative and autonomous robot systems, as through efficient visual systems, robots can acquire and process environmental information in real-time, recognize objects, assess spatial relationships, and make adaptive decisions.

## Recent Developments

There have been 200+ robotics papers from CoRL 2025 with various approaches to robot manipulation and perception. Some recent work uses LLMs to induce probabilistic programs that estimate POMDP dynamics and observations, which relates directly to handling partial observability challenges.

## Benchmark and Scoring Trends

Analysis of 164 Vision-Language-Action (VLA) model submissions at ICLR 2026 shows trends in discrete diffusion VLAs, reasoning models, and benchmarks including LIBERO, CALVIN, and SIMPLER.

Recent work introduces the VLA-FEB benchmark with new metrics for measuring multimodal fusion quality and alignment.

## Technical Approaches

Visual affordance learning focuses on inferring interaction possibilities directly from raw 2D visual observations by predicting pixel-wise affordance maps, with Transporter Networks establishing this paradigm using spatially equivariant feature matching.

The research community is actively developing new metrics and benchmarks for evaluating robot manipulation systems with visual perception in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab3a1e88-4cbe-4cb8-b0c3-5acab8ee93f7",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "b8979f76-dec2-429a-bf88-aaecc1fa07a8",
  "sourceToolAssistantUUID": "ab3a1e88-4cbe-4cb8-b0c3-5acab8ee93f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T19:38:30.425Z_

<details><summary>↩ Tool result · `toolu_01MzWVMKkQRU6LgWGDbBQQ16`</summary>

```text
Web search results for query: "proprioception data quality robot learning 2025 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Proprioceptive Data Annotation for Robot Learning|Labelvisor","url":"https://www.labelvisor.com/proprioceptive-data-annotation-for-robot-learning/"},{"title":"A Terrain Classification Method for Quadruped Robots with Proprioception","url":"https://www.mdpi.com/2079-9292/14/6/1231"},{"title":"Generative Models for Robot Learning","url":"https://iclr.cc/virtual/2025/workshop/23977"},{"title":"Localising under the drape: proprioception in the era of distributed surgical robotic system","url":"https://arxiv.org/html/2510.23512v1"},{"title":"Embodied intelligence for robot manipulation: development and challenges | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-025-00020-1"},{"title":"Real-Time Proprioceptive Sensing Enhanced Switching Model Predictive Control for Quadruped Robot Under Uncertain Environment | MDPI","url":"https://www.mdpi.com/2079-9292/14/13/2681"},{"title":"Learning Object Properties Using Robot Proprioception via ...","url":"https://chaoliu.tech/publication/chen-diff-proprioception-icra-2025/chen-diff-proprioception-icra-2025.pdf"},{"title":"Frontiers | Multimodal perception-driven decision-making for human-robot interaction: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1604472/full"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"}]

I've completed the web search for "proprioception data quality robot learning 2025 2026". Here are the key findings:

## Recent Research Areas

**Proprioceptive Data in Robot Learning:**
For high-quality proprioceptive data annotation, it is important to understand the physical nature of each source to distinguish a useful signal from hardware noise. Proprioceptive data annotation is used to ensure the AI model learns to control the robot and helps to understand exactly how the robot interacts with the physical world.

**Data Types and Quality Metrics:**
Key proprioceptive data includes joint angles (the angle of each robot joint at any given moment), joint velocities (the speed at which joints change position), and joint torques (measuring effort applied to each joint), with high-quality joint torque labeling allowing models to learn how not to overstrain mechanisms.

**2025-2026 Research Trends:**
Recent publications show significant work on proprioception in robot learning. Recent papers from December 2025 include "PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations" and "Learning Agile Striker Skills for Humanoid Soccer Robots from Noisy Sensory Input."

Recent research investigates the relationship between terrain characteristics and quadruped robots based on proprioception sensor data, proposing terrain classification methods by integrating multiple sensor signals.

**Integration with Multi-Modal Learning:**
HPT proposes a heterogeneous pre-training encoder that maps proprioceptive and visual perceptual information from large-scale heterogeneous robot data into a shared latent space, addressing the complexity of collecting environment-specific datasets for individual robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0044312d-0d3e-48f1-9f08-a341ed7f051f",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "0a34aac5-b38a-4f61-a98a-4be1f3409b31",
  "sourceToolAssistantUUID": "0044312d-0d3e-48f1-9f08-a341ed7f051f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T19:38:31.187Z_

<details><summary>↩ Tool result · `toolu_015UGkHixHs5XeyAF4cM8LWn`</summary>

```text
Web search results for query: "when does multimodal fusion help robot"

Links: [{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Frontiers | Multimodal perception-driven decision-making for human-robot interaction: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1604472/full"},{"title":"Effective Techniques for Multimodal Data Fusion: A Comparative Analysis - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10007548/"},{"title":"Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision","url":"https://arxiv.org/html/2504.02477v1"},{"title":"[2504.19002] Deep Learning-Based Multi-Modal Fusion for Robust Robot Perception and Navigation","url":"https://arxiv.org/abs/2504.19002"},{"title":"Multimodal fusion and vision–language models: A survey for robot vision - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1566253525007249"},{"title":"Review of Multimodal Data Fusion for Robotics and Embodied Intelligence","url":"https://www.atlantis-press.com/article/126016751.pdf"},{"title":"Multimodal Sensors and ML‐Based Data Fusion for Advanced Robots - Duan - 2022 - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202200213"},{"title":"Recent advancements in multimodal human–robot interaction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10210148/"},{"title":"Multimodal Fusion and Temporal Reasoning for Intelligent Robot Perception | Happening @ Michigan","url":"https://events.umich.edu/event/148106"}]

Based on the search results, here are the key scenarios where multimodal fusion helps robots:

## Perception and Decision-Making
By integrating multimodal perception techniques with decision-making frameworks, robots can operate in dynamic and complex environments with improved adaptability, reliability, robustness, and efficiency.

## Handling Complex Tasks
Traditional unimodal approaches often encounter perceptual limitations when dealing with complex tasks in real-world environments—such as occlusions, lighting variations, sparse textures, and insufficient semantic information. In contrast, multimodal fusion integrates complementary information from various sensor inputs (e.g., vision, language, depth, LiDAR, and tactile data), thereby enhancing the perception, reasoning, and decision-making capabilities of robot vision systems.

## Robotic Manipulation and Task Generalization
Hierarchical and late fusion architectures achieve the highest manipulation success and generalization, confirming the benefit of multi-level cross-modal integration.

## When Complementary Information Exists
The most significant benefit from exploiting multiple modalities can be noticed within classes, where unimodal models yield close results. On the other hand, categories, where one of the unimodal approaches is undeniably better, do not gain much from multimodality.

## Human-Robot Interaction
Multimodal HRI is a method for individuals to communicate with a robot using various modalities, including voice, image, text, eye movement, and touch, as well as bio-signals like EEG and ECG.

In summary, multimodal fusion helps robots most when they face complex real-world conditions with complementary sensory information that no single modality can capture effectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31535f48-870c-49f9-91a0-553cf13b91c4",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "d4cb0c12-9ef6-448b-b638-523a99601bd2",
  "sourceToolAssistantUUID": "31535f48-870c-49f9-91a0-553cf13b91c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T19:38:31.659Z_

<details><summary>↩ Tool result · `toolu_01DY3tQsFJSpP3cnxcn5uSdp`</summary>

```text
Web search results for query: "data filtering robot imitation learning 2026"

Links: [{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning","url":"https://arxiv.org/html/2408.14037v1"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with ...","url":"https://arxiv.org/pdf/2505.09603"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"A survey on imitation learning for contact-rich tasks in robotics - Toshiaki Tsuji, Yasuhiro Kato, Gokhan Solak, Heng Zhang, Tadej Petrič, Francesco Nori, Arash Ajoudani, 2026","url":"https://journals.sagepub.com/doi/10.1177/02783649261417694"},{"title":"Interventional Data Generation for Robust and Data-Efficient Robot Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=ckFRoOaA3n"},{"title":"Few-Shot Imitation Learning by Querying Unlabeled Datasets","url":"https://www.roboticsproceedings.org/rss19/p011.pdf"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Frontiers | Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/full"}]

Based on the web search results, here are the key findings related to data filtering and robot imitation learning in 2026:

## Recent Research on Data Filtering for Robot Imitation Learning

DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance. This represents a significant advancement over traditional filtering methods.

Unlike standard practices that filter data using human notions of quality (e.g., based on semantic or visual similarity), DataMIL directly optimizes data selection for task success.

## Challenges in Data-Driven Learning

Recently, the robotics community has amassed ever larger and more diverse datasets to train generalist robot policies. However, while these policies achieve strong mean performance across a variety of tasks, they often underperform on individual, specialized tasks and require further tuning on newly acquired task-specific data.

## Alternative Approaches

Re-Mix uses distributionally robust optimization (DRO) to maximize worst-case performance across all possible downstream domains. The method addresses the wide range of challenges that arise when applying DRO to robotics datasets including variability in action spaces and dynamics across different datasets.

## Broader Imitation Learning Trends

Recent surveys indicate that recent advances in multimodal learning and foundation models have significantly enhanced performance in complex contact tasks across industrial, household, and healthcare domains.

The research shows that data filtering remains a critical challenge in robot imitation learning, with new methods focusing on policy-driven approaches rather than heuristic-based filtering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2b26a9a-8156-4ecc-b8db-62bc58fbc3a5",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "aef2632e-ce7a-462a-9233-8b2385370259",
  "sourceToolAssistantUUID": "c2b26a9a-8156-4ecc-b8db-62bc58fbc3a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T19:38:32.008Z_

<details><summary>↩ Tool result · `toolu_01QdQhs99FzoRKvxPkctKLVd`</summary>

```text
Web search results for query: "demonstration quality assessment ranking robot 2026"

Links: [{"title":"Competitions - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/program/competitions/"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Where Autonomy Works: Evaluating Robot Capabilities in 2026 | Epoch AI","url":"https://epoch.ai/blog/where-autonomy-works-evaluating-robot-capabilities-in-2026"},{"title":"Technical Performance | The 2026 AI Index Report","url":"https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance"},{"title":"AI Readiness Assessment: 9 Critical Questions","url":"https://www.progressiverobot.com/2026/05/10/ai-readiness-assessment/"},{"title":"January 2026: New Standard Sets Performance Testing for Household Robots","url":"https://www.standards.iteh.ai/articles/blog/latest-news/household-robot-standards-jan-2026"},{"title":"AI dev tool power rankings & comparison [March 2026] - LogRocket Blog","url":"https://blog.logrocket.com/ai-dev-tool-power-rankings/"},{"title":"Robotics AI Benchmarks 2026: State of the Art | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/robotics"},{"title":"Top 10 robotics developments of January 2026 - The Robot Report","url":"https://www.therobotreport.com/top-10-robotics-developments-of-january-2026/"},{"title":"State of robotics industry report 2026","url":"https://www.therobotreport.com/state-of-robotics-industry-report-2026/"}]

Based on the search results, I found several relevant topics related to demonstration quality assessment and ranking in robotics for 2026:

## Key Findings:

**Demonstration Quality Assessment in Robot Learning:**
WorldEval (Li et al., 2025e) studies whether a world model can serve as a scalable proxy for real-world policy evaluation, ranking different robot policies and even different checkpoints of the same policy entirely in imagination, while also functioning as a safety detector.

**Real-World Robot Capability Evaluation:**
A task that looks solved in a demonstration may be brittle in deployment. A comprehensive assessment from February 2026 evaluated robot performance across industrial, household, and navigation domains, examining reliability, speed, cost, and transfer capabilities.

**Competition Assessments (ICRA 2026):**
In 2026 ICRA competitions, teams are evaluated in terms of their task completion quality, data collection speed, and performance of policy learned using the collected data.

**Performance Standards for Household Robots:**
The publication of EN IEC 62849:2026 ushers in a new era for the performance evaluation of household and similar-use robots. By standardizing evaluation methods for mobility, navigation, and energy use, this document enables clearer benchmarks for industry and regulatory stakeholders.

**Industry Shift:**
The robotics industry found itself at an inflection point in January 2026. After years of innovation, bold claims, and headline-grabbing demonstrations, the conversation is shifting from what robots could do to what they can reliably do in the real world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d9ab784-13f1-4a5b-89aa-4b78b0bed397",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "0bc3fe6a-67f6-4ab0-98f1-b00a4976b245",
  "sourceToolAssistantUUID": "7d9ab784-13f1-4a5b-89aa-4b78b0bed397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T19:38:33.140Z_

<details><summary>↩ Tool result · `toolu_01QPqvBr7E7QxVYGjbd4sTD7`</summary>

```text
Web search results for query: "proprioceptive scoring robot data quality"

Links: [{"title":"Multi-Class Human/Object Detection on Robot Manipulators using Proprioceptive Sensing","url":"https://arxiv.org/html/2508.02425"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation","url":"https://arxiv.org/html/2412.13877"},{"title":"Latent Representations for Visual Proprioception in Inexpensive Robots","url":"https://arxiv.org/html/2504.14634v1"},{"title":"Proprioceptive Image: An Image Representation of Proprioceptive Data from Quadruped Robots for Contact Estimation Learning","url":"https://arxiv.org/html/2510.14612"},{"title":"[2508.02425] Multi-Class Human/Object Detection on Robot Manipulators using Proprioceptive Sensing","url":"https://arxiv.org/abs/2508.02425"},{"title":"Prometheus: Universal, Open-Source Mocap-Based Teleoperation System with Force Feedback for Dataset Collection in Robot Learning","url":"https://arxiv.org/html/2510.01023"},{"title":"Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data","url":"https://arxiv.org/html/2602.04600"},{"title":"Self-Sensing for Proprioception and Contact Detection in Soft Robots Using Shape Memory Alloy Artificial Muscles","url":"https://arxiv.org/html/2409.17111v1"},{"title":"PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations","url":"https://arxiv.org/html/2512.13093v2"},{"title":"Exteroception through Proprioception: Sensing through Improved Contact Modeling for Soft Growing Robots","url":"https://arxiv.org/html/2507.10694"}]

Based on the search results, here's what I found about proprioceptive scoring in robot data quality:

## Proprioceptive Scoring in Robot Data Quality

The search results reveal several approaches to quality assessment and scoring of proprioceptive data in robotics:

### Data Quality Assurance

In the RoboMIND dataset project, researchers define 8 quality assurance criteria in the data collection process. Data preprocessing involves filtering the dataset based on predefined standards, evaluating task execution accuracy, motion trajectory smoothness, and the presence of occlusion or motion blur in the visual data.

### Proprioceptive Scoring Methods

In proprioceptive image representation work, scores are symmetrically clipped to [-3,3], following the three-sigma principle to limit extreme outliers while maintaining contrast for typical values. This adaptive MAD-based construction yields a symmetric, noise-resilient spike matrix that adjusts to local variability while preserving sensitivity to significant temporal transitions.

### Performance Metrics

For online testing of proprioceptive detection systems, precision, recall and F1-score are reported per class, corresponding to confusion matrices. Best-performing models achieved 91.11% accuracy during real-time testing, demonstrating the feasibility of multi-class detection models.

The research demonstrates that proprioceptive data quality is evaluated through multiple metrics including accuracy rates, precision/recall scores, and preprocessing standards that account for signal noise and data integrity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db7a9146-8a7c-4a6b-9292-03950e451ae4",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "b1b8a44c-3896-499d-b22e-cbf0bfad2141",
  "sourceToolAssistantUUID": "db7a9146-8a7c-4a6b-9292-03950e451ae4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T19:38:35.167Z_

<details><summary>↩ Tool result · `toolu_01ST14BdmrUQAS8F53Krz6jy`</summary>

```text
Web search results for query: "observation modality selection manipulation policy"

Links: [{"title":"Any2Policy: Learning Visuomotor Policy with Any-Modality","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f13159aecc416659a3c6cef0aecd0d94-Paper-Conference.pdf"},{"title":"Modality Selection and Skill Segmentation via Cross-Modality Attention","url":"https://arxiv.org/html/2504.14573"},{"title":"Multi-Modal Manipulation via Multi-Modal Policy Consensus","url":"https://arxiv.org/html/2509.23468"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/html/2602.21622"},{"title":"Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation","url":"https://arxiv.org/html/2604.01414"},{"title":"Goal-Guided Prompting With Adaptive Modality Selection for Efficient Assembly Activity Anticipation in Egocentric Videos | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11347530/"},{"title":"[Literature Review] Modality Selection and Skill Segmentation via Cross-Modality Attention","url":"https://www.themoonlight.io/en/review/modality-selection-and-skill-segmentation-via-cross-modality-attention"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://diffusion-policy.cs.columbia.edu/diffusion_policy_ijrr.pdf"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation","url":"https://force-policy.github.io/"}]

Based on the web search results, here's what I found about observation modality selection and manipulation policies:

## Key Research Areas

**Modality Selection for Manipulation Policies**

Recent work addresses the challenge of incorporating multiple sensory modalities through modality selection, proposing a cross-modality attention (CMA) mechanism to identify and selectively utilize the modalities that are most informative for action generation at each timestep. 

A key innovation is the Cross-Modality Attention mechanism that dynamically selects and utilizes the most informative sensory modalities (e.g., vision, tactile, proprioception) at each timestep for action generation.

**Multi-Modal Policy Learning**

Research has developed multi-modal embodied agents capable of processing a wide array of instruction and observation modalities, with methods like the Any-to-Policy Robot Model (Any2Policy). These approaches harness multi-modal encoders to extract relevant features from inputs, which are then transformed into standardized token representations via projection layers.

**Policy-Level Fusion Approaches**

Recent compositional frameworks for multimodal robot manipulation factorize policies at the modality level, where the action distribution conditioned on each input modality is modeled by a separate expert policy, and their outputs are integrated through learned consensus weights from a router network.

**Context-Aware Modality Integration**

Advanced frameworks enable context-aware shifts in modality reliance: tactile experts dominate during contact-rich phases, while vision governs geometric reasoning in free space. This adaptive approach addresses the challenge that simply increasing the number of sensory modalities by stacking inputs often leads to exponentially larger policy search spaces, making learning inefficient and unstable.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74f0bb74-867d-43e3-b086-e5fe8b8cc28c",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "08293fbd-2d96-4a8c-9fbe-7702d60f66a9",
  "sourceToolAssistantUUID": "74f0bb74-867d-43e3-b086-e5fe8b8cc28c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-13T19:38:36.958Z_

<details><summary>↩ Tool result · `toolu_01QM2uaFjvqDFfrS3KaFTf6j`</summary>

```text
Web search results for query: "reward model demonstration quality robot manipulation 2026"

Links: [{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=aemqAxScl9"},{"title":"ICLR Poster SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://iclr.cc/virtual/2026/poster/10008682"},{"title":"[2509.25358] SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://arxiv.org/abs/2509.25358"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://arxiv.org/html/2509.25358"},{"title":"Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/html/2603.16065"},{"title":"New RoboReward dataset and models automate robotic training and evaluation","url":"https://techxplore.com/news/2026-01-roboreward-dataset-automate-robotic.html"},{"title":"(PDF) Multi-Stage Manipulation with Demonstration-Augmented Reward, Policy, and World Model Learning","url":"https://www.researchgate.net/publication/389581071_Multi-Stage_Manipulation_with_Demonstration-Augmented_Reward_Policy_and_World_Model_Learning"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"}]

Based on the web search results, here are some key findings about reward model demonstration quality and robot manipulation in 2026:

## Major Recent Research

**SARM: Stage-Aware Reward Modeling**

A stage-aware, video-based reward modeling framework addresses the challenge that long-horizon, contact-rich problems—especially those involving deformable objects—remain challenging due to inconsistent demonstration quality. The framework jointly predicts task stage and fine-grained progress, using natural-language subtask annotations to derive consistent labels across variable-length demonstrations. Policies trained with this approach achieved an 83% success rate when folding T-shirts from a flattened configuration and 67% when starting from a crumpled state.

**Robometer: General-Purpose Reward Models**

Robometer is a general-purpose, video-language-input, dense reward model trained with a dual reward-prediction objective: a frame-level progress loss on expert data and a preference-prediction loss over trajectory comparisons. The RBM-1M dataset comprises over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

**RoboReward Dataset and Models**

The RoboReward dataset contains many videos showing real robots completing various real-world tasks, coupled with plain-language text descriptions and progress scores, and is designed for training VLMs to judge how well robots completed specific tasks. RoboReward 4B and 8B outperform much larger state-of-the-art VLMs on reward accuracy.

These approaches emphasize that high-quality reward modeling, combined with selective data filtering, is a powerful path forward for building robust and scalable robotic behavior models capable of addressing long-horizon manipulation challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b98e4b94-16ba-426b-8cf6-f295378d4213",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "c49b9d54-d9fd-4a74-ad1f-52159600e12a",
  "sourceToolAssistantUUID": "b98e4b94-16ba-426b-8cf6-f295378d4213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T19:38:43.636Z_

<details><summary>↩ Tool result · `toolu_01GVw1rrsxV1GzCRBZZQ3sPz`</summary>

```text
Web search results for query: "multimodal demonstration curation VLA 2026"

Links: [{"title":"Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation","url":"https://arxiv.org/html/2603.08260"},{"title":"SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture","url":"https://arxiv.org/html/2605.12500"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"HALO: A Unified Vision-Language-Action Model for ...","url":"https://arxiv.org/pdf/2602.21157"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation","url":"https://arxiv.org/html/2603.25406v1"},{"title":"Demonstration-Free Robotic Control via LLM Agents","url":"https://arxiv.org/html/2601.20334v1"},{"title":"Parallels Between VLA Model Post-Training and Human ...","url":"https://arxiv.org/pdf/2506.20966"},{"title":"Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to","url":"https://arxiv.org/pdf/2603.08260"}]

Based on the search results, I found several recent papers from 2026 that address aspects of multimodal demonstration curation and VLA (Vision-Language-Action) models:

## Key Findings

**Seed2Scale Framework**: This work employs a lightweight VLA model called SuperTiny for robust data collection and uses a pretrained VLM as a verifier to filter failed and low-quality trajectories, effectively preventing performance degradation during self-iteration. With only a minimal set of seed data, the target model achieved a 209.15% improvement in success rate, leaping from an initial 22.18% to 68.57%.

**Green-VLA**: This framework employed the DataQA pipeline for robotic dataset curation and quality assessment, enabling focus on high-quality demonstrations to improve both sample efficiency and final policy performance.

**HALO Model**: This work curates a massive, heterogeneous dataset spanning three distinct domains—Visual Question Answering (VQA), Visual Generation (VG), and Action Prediction (AP).

**SenseNova-U1**: Large-scale multimodal instruction data are curated across ten vertical domains through a systematic process consisting of distribution-balanced data curation, prompt augmentation, and multi-criteria quality filtering.

The search results show that demonstration curation for VLA models in 2026 involves sophisticated pipelines combining quality filtering, multimodal evaluation, and data augmentation strategies to improve model performance with minimal seed demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0429796f-62d7-410d-834a-71d0e88466bb",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "1be408f9-187d-484f-8cdd-88d8a2e3faa7",
  "sourceToolAssistantUUID": "0429796f-62d7-410d-834a-71d0e88466bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-13T19:38:48.188Z_

Let me run a few more targeted searches to dig deeper into the most relevant areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be408f9-187d-484f-8cdd-88d8a2e3faa7",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18iNEeJNuZ5bx7PawW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efa96389-63a2-44f8-9474-23b41473be33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrBEtUUEwH9w2f6yXDtmyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2705,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6905,
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

_source line 28 · 2026-05-13T19:38:49.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019frPzdpTpTwvzuKZA6X15U`</summary>

```json
{
  "query": "DataMIL selecting data robot imitation learning datamodels 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efa96389-63a2-44f8-9474-23b41473be33",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18iNEeJNuZ5bx7PawW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40d3acd2-2792-4c64-82ff-db5ce01bedd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrBEtUUEwH9w2f6yXDtmyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2705,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6905,
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

_source line 29 · 2026-05-13T19:38:49.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFqDsHNJB2Dr8UYHdYtiJZ`</summary>

```json
{
  "query": "\"modality selection skill segmentation cross-modality attention\" robot 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40d3acd2-2792-4c64-82ff-db5ce01bedd6",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18iNEeJNuZ5bx7PawW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdf214df-ecd7-41f7-91eb-4ae8bf135fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrBEtUUEwH9w2f6yXDtmyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2705,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6905,
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

_source line 30 · 2026-05-13T19:38:50.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FUUwKgvcKwEDgvD8jXMEVY`</summary>

```json
{
  "query": "Green-VLA DataQA robotic dataset curation quality assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdf214df-ecd7-41f7-91eb-4ae8bf135fe4",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18iNEeJNuZ5bx7PawW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4f4cdcc-00c7-4224-8a2d-26027648a13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrBEtUUEwH9w2f6yXDtmyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2705,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6905,
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

_source line 31 · 2026-05-13T19:38:51.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZnx6nJZcw72MiosEwjz6T`</summary>

```json
{
  "query": "\"learning when to see when to feel\" adaptive vision torque fusion contact manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4f4cdcc-00c7-4224-8a2d-26027648a13e",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18iNEeJNuZ5bx7PawW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d34ddb0-9353-4d66-8065-19b29e026259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrBEtUUEwH9w2f6yXDtmyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2705,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6905,
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

_source line 32 · 2026-05-13T19:38:52.084Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SnyEZ987ZxERhdTWi71LgG`</summary>

```json
{
  "query": "Seed2Scale self-evolving data engine embodied AI VLA quality filtering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d34ddb0-9353-4d66-8065-19b29e026259",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18iNEeJNuZ5bx7PawW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a633ac6-47b4-4796-81f3-a49ccfbd2cf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrBEtUUEwH9w2f6yXDtmyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2705,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6905,
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

_source line 33 · 2026-05-13T19:38:56.321Z_

<details><summary>↩ Tool result · `toolu_01SFqDsHNJB2Dr8UYHdYtiJZ`</summary>

```text
Web search results for query: ""modality selection skill segmentation cross-modality attention" robot 2025"

Links: [{"title":"[2504.14573] Modality Selection and Skill Segmentation via Cross-Modality Attention","url":"https://arxiv.org/abs/2504.14573"},{"title":"Modality Selection and Skill Segmentation via Cross-Modality Attention","url":"https://arxiv.org/pdf/2504.14573"},{"title":"Modality Selection and Skill Segmentation via Cross-Modality Attention | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11175125/;jsessionid=A9DFF542E4FEE2439DA99719042FB907"},{"title":"dblp: Modality Selection and Skill Segmentation via Cross-Modality Attention.","url":"https://dblp.org/rec/journals/corr/abs-2504-14573.html"},{"title":"[Literature Review] Modality Selection and Skill Segmentation via Cross-Modality Attention","url":"https://www.themoonlight.io/en/review/modality-selection-and-skill-segmentation-via-cross-modality-attention"},{"title":"Frontiers | Multimodal perception-driven decision-making for human-robot interaction: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1604472/full"},{"title":"Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision","url":"https://arxiv.org/html/2504.02477v1"},{"title":"Cross-Modality Alignment Perception and Multi-Head Self-Attention Mechanism for Vision-Language-Action of Humanoid Robot - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12787822/"},{"title":"Embodied AI with Foundation Models for Mobile Service ...","url":"https://arxiv.org/pdf/2505.20503"},{"title":"Enhancing robotic skill acquisition with multimodal sensory data: A novel dataset for kitchen tasks | Scientific Data","url":"https://www.nature.com/articles/s41597-025-04798-z"}]

Based on the search results, I found highly relevant research on this topic:

## Key Research Finding

The paper "Modality Selection and Skill Segmentation via Cross-Modality Attention" appears to be the primary work matching your query. The paper addresses the challenge of incorporating additional sensory modalities such as tactile and audio into foundational robotic models through a cross-modality attention (CMA) mechanism that identifies and selectively utilizes the modalities most informative for action generation at each timestep.

## Technical Approach

The core idea revolves around a Cross-Modality Attention (CMA) mechanism that dynamically selects and utilizes the most informative sensory modalities (e.g., vision, tactile, proprioception) at each timestep for action generation. The paper proposes a transformer-based architecture incorporating a CMA module that takes embeddings from different modalities and timesteps as input and learns to dynamically weight and integrate these inputs.

## Application to Skill Segmentation

The CMA mechanism is extended to segment primitive skills from expert demonstrations and leverage this segmentation to train a hierarchical policy capable of solving long-horizon, contact-rich manipulation tasks. Training individual policies for segmented primitive actions improves sample efficiency and accuracy compared to training a single policy for the entire trajectory.

The paper was submitted to arXiv on April 20, 2025, making it a very recent publication in the robotics field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdf214df-ecd7-41f7-91eb-4ae8bf135fe4",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "c4e0f6e2-b6f9-4003-9feb-d93efa7ee3ed",
  "sourceToolAssistantUUID": "bdf214df-ecd7-41f7-91eb-4ae8bf135fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T19:38:58.034Z_

<details><summary>↩ Tool result · `toolu_019frPzdpTpTwvzuKZA6X15U`</summary>

```text
Web search results for query: "DataMIL selecting data robot imitation learning datamodels 2025"

Links: [{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"GitHub - UT-Austin-RobIn/datamil: Code release for -- DataMIL: Selecting Data for Robot Imitation Learning with Datamodels · GitHub","url":"https://github.com/UT-Austin-RobIn/datamil"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://robin-lab.cs.utexas.edu/datamodels4imitation/"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with ...","url":"https://arxiv.org/pdf/2505.09603"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels | OpenReview","url":"https://openreview.net/forum?id=AcTsKglDdh"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://openreview.net/pdf/d1836285b655f13b1f86918922a074b725fa137b.pdf"},{"title":"DATAMIL: SELECTING DATA FOR ROBOT IMITATION ...","url":"https://openreview.net/pdf/82e6c304571ad1e85b44780f29e82e7042b2743f.pdf"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"[Literature Review] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://www.themoonlight.io/en/review/datamil-selecting-data-for-robot-imitation-learning-with-datamodels"}]

I found comprehensive information about DataMIL. Here's what the research reveals:

## DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance.

### Problem and Motivation

The robotics community has amassed ever larger and more diverse datasets to train generalist robot policies; however, while these policies achieve strong mean performance across a variety of tasks, they often underperform on individual, specialized tasks and require further tuning on newly acquired task-specific data. Combining task-specific data with carefully curated subsets of large prior datasets via co-training can produce better specialized policies, but selecting data naively may actually harm downstream performance.

### Key Innovation

Unlike standard practices that filter data using human notions of quality (e.g., based on semantic or visual similarity), DataMIL directly optimizes data selection for task success. DataMIL trains a data-quality estimator using a tractable objective: validation loss, demonstrating empirically that this objective retains sufficient correlations to the true objective (trained policy performance), allowing datamodels to predict data influence without requiring expensive real-world rollouts.

### Experimental Results and Applications

DataMIL was demonstrated on 60+ simulation and real world tasks, most notably selecting relevant data from Open X-Embodiment datasets, showing significant improvements in performance compared to existing data selection methods, even for novel embodiments not present in the prior data. Across the 50 tasks in MetaWorld, a 10% performance boost was shown compared to state-of-the-art baselines.

The paper was posted to arXiv on May 14, 2025, with authors including Shivin Dass, Alaa Khaddaj, Logan Engstrom, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40d3acd2-2792-4c64-82ff-db5ce01bedd6",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "c6cbd5e5-1770-4afe-80b3-943b03fce97a",
  "sourceToolAssistantUUID": "40d3acd2-2792-4c64-82ff-db5ce01bedd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T19:38:58.329Z_

<details><summary>↩ Tool result · `toolu_01XZnx6nJZcw72MiosEwjz6T`</summary>

```text
Web search results for query: ""learning when to see when to feel" adaptive vision torque fusion contact manipulation"

Links: [{"title":"Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation","url":"https://arxiv.org/html/2604.01414"},{"title":"[2604.01414] Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation","url":"https://arxiv.org/abs/2604.01414"},{"title":"Symmetry-Aware Fusion of Vision and Tactile Sensing via Bilateral Force Priors for Robotic Manipulation","url":"https://arxiv.org/html/2602.13689"},{"title":"See, feel, act: Hierarchical learning for complex manipulation skills with multisensory fusion","url":"https://www.researchgate.net/publication/330759920_See_feel_act_Hierarchical_learning_for_complex_manipulation_skills_with_multisensory_fusion"},{"title":"See, feel, act: Hierarchical learning for complex manipulation skills with multisensory fusion | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.aav3123"},{"title":"See, feel, act: Hierarchical learning for complex manipulation skills with multisensory fusion | The Center for Brains, Minds & Machines","url":"https://cbmm.mit.edu/publications/see-feel-act-hierarchical-learning-complex-manipulation-skills-multisensory-fusion"},{"title":"Reactive Diffusion Policy:","url":"https://arxiv.org/pdf/2503.02881"},{"title":"See, Hear, and Feel: Smart Sensory Fusion for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=sygvGP-YLfx"},{"title":"Smart Sensory Fusion for Robotic Manipulation","url":"https://proceedings.mlr.press/v205/li23c/li23c.pdf"},{"title":"Learning to Grasp and Regrasp Using Vision and Touch","url":"https://dspace.mit.edu/bitstream/handle/1721.1/126806/1805.11085.pdf?sequence=2&isAllowed=y"}]

I found the research paper you were searching for! Here's what I found:

## "Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation"

This is a recent paper that addresses vision-based policies in robotic manipulation, published on arXiv in April 2026.

### Key Problem
Purely visual sensing becomes insufficient in contact-rich and force-sensitive tasks where force/torque (F/T) signals provide critical information about contact dynamics, alignment, and interaction quality.

### Main Contribution
The researchers propose an adaptive integration strategy that ignores F/T signals during non-contact phases while adaptively leveraging both vision and torque information during contact.

### Results
Experimental results demonstrate that their method outperforms the strongest baseline by 14% in success rate, highlighting the importance of contact-aware multimodal fusion for robotic manipulation.

### Technical Approach
Two key components are critical for effective fusion: first, a contact-gating strategy filters out the inertia-induced interference on the torque data during free-space motion, and then a CFG-style vision–torque fusion mechanism allows the policy to learn how to adaptively weight modalities.

The paper compares various strategies for integrating vision and force/torque signals within diffusion-based manipulation policies, making it a comprehensive study of multimodal fusion approaches for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d34ddb0-9353-4d66-8065-19b29e026259",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "feb006e8-d668-4811-85c4-1bc7326c08d2",
  "sourceToolAssistantUUID": "5d34ddb0-9353-4d66-8065-19b29e026259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T19:38:58.570Z_

<details><summary>↩ Tool result · `toolu_01FUUwKgvcKwEDgvD8jXMEVY`</summary>

```text
Web search results for query: "Green-VLA DataQA robotic dataset curation quality assessment"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v2"},{"title":"Paper page - Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://huggingface.co/papers/2602.00919"},{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://arxiv.org/pdf/2602.00919"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056v1"},{"title":"Benchmarking Vision, Language, & Action Models on Robotic Learning Tasks","url":"https://arxiv.org/html/2411.05821v1"},{"title":"A Pragmatic VLA Foundation Model","url":"https://arxiv.org/html/2601.18692"},{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001v1"},{"title":"Data Quality Assessment","url":"https://webarchive.gemini.edu/sciops/data/dataQA.html"},{"title":"VLA Models: Why Data-Centric AI Unlocks Next-Gen Robotics","url":"https://voxel51.com/blog/vla-models-data-centric-ai-robotics"}]

Based on the search results, I found relevant information about Green-VLA and its DataQA pipeline:

## Green-VLA and DataQA Pipeline

To ensure high-quality training data, the Green-VLA framework employed the DataQA pipeline for robotic dataset curation and quality assessment. At the data level, the DataQA pipeline filters and smooths heterogeneous demonstrations and aligns temporal dynamics via optical flow–based resampling.

### DataQA Quality Metrics

DataQA Pipeline employs quality filtering using jitter (J), sharpness (S), diversity (D), and variance (σ²) metrics, enabling superior sample efficiency—achieving better results with 3,000 hours than competitors with 10,000+ hours.

### Impact on Training

This pipeline enabled focus on high-quality demonstrations, improving both sample efficiency and final policy performance. Dataset curation plus RL alignment builds on unified pretrain to progressively improve performance on a concrete target embodiment.

### Overall Green-VLA Framework

A scalable data-processing pipeline including DataQA and temporal-alignment filters and synchronizes 3,000 hours of demonstrations; a unified, embodiment-aware action interface enables a single policy to control humanoids, mobile manipulators, and fixed-base arms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4f4cdcc-00c7-4224-8a2d-26027648a13e",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "1549471c-c992-44ba-8795-8517438e5bb2",
  "sourceToolAssistantUUID": "c4f4cdcc-00c7-4224-8a2d-26027648a13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T19:38:59.435Z_

<details><summary>↩ Tool result · `toolu_01SnyEZ987ZxERhdTWi71LgG`</summary>

```text
Web search results for query: "Seed2Scale self-evolving data engine embodied AI VLA quality filtering"

Links: [{"title":"Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to","url":"https://arxiv.org/pdf/2603.08260"},{"title":"Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation","url":"https://arxiv.org/html/2603.08260"},{"title":"[2603.08260] Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation","url":"https://arxiv.org/abs/2603.08260"},{"title":"GigaWorld-0: World Models as Data Engine to Empower Embodied AI","url":"https://arxiv.org/html/2511.19861v1"},{"title":"Why VLA Training Data is the Backbone of Next-Gen Embodied AI","url":"https://macgence.com/blog/vla-training-data/"},{"title":"Image Quality Assessment for Embodied AI","url":"https://arxiv.org/html/2505.16815"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"VLA Model Training Data: Architectures, Needs & Challenges","url":"https://macgence.com/blog/vla-model-training-data"},{"title":"ByteDance Seed","url":"https://seed.bytedance.com/en/seed2"}]

Based on the search results, here's what I found about Seed2Scale:

## Seed2Scale: A Self-Evolving Data Engine for Embodied AI

Seed2Scale is a self-evolving data engine designed to break the data bottleneck in Embodied AI through a heterogeneous synergy architecture of "small-model collection, large-model evaluation, and target-model learning".

### Key Components and Architecture

Starting with as few as four seed demonstrations, the engine employs the lightweight Vision-Language-Action model, SuperTiny, as a dedicated collector, leveraging its strong inductive bias for robust exploration in parallel environments.

A large-scale Vision-Language Model (VLM) serves as a verifier to enable the self-evolution loop by preventing error accumulation through success/failure judgment and quality scoring.

### Quality Filtering Mechanism

The system employs a lightweight VLA model, SuperTiny, for robust data collection and a pretrained VLM as a verifier to filter failed and low-quality trajectories, effectively preventing performance degradation during self-iteration.

### Performance and Benefits

The engine enables large-scale data generation from as few as four initial human demonstrations, significantly mitigating the reliance on manual data acquisition in Embodied AI. Experimental results demonstrate that Seed2Scale exhibits significant scaling potential: as iterations progress, the success rate of the target model shows a robust upward trend, achieving a performance improvement of 131.2%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a633ac6-47b4-4796-81f3-a49ccfbd2cf7",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "2a871eb2-d683-4ccb-9c4e-b13941eb4ef5",
  "sourceToolAssistantUUID": "7a633ac6-47b4-4796-81f3-a49ccfbd2cf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T19:39:02.516Z_

Let me run a few more targeted searches to find the most directly competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a871eb2-d683-4ccb-9c4e-b13941eb4ef5",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18jXqNYtVw3ZtTe1bRa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7b925b3-0525-4141-9551-cf166a81ed89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AanJhD5rwEAYGDAX7eJBuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7552,
      "cache_read_input_tokens": 17459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7552,
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

_source line 39 · 2026-05-13T19:39:03.905Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JtjsfULnfyW9cBozj9Qr5o`</summary>

```json
{
  "query": "\"Quality over Quantity\" demonstration curation influence functions robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7b925b3-0525-4141-9551-cf166a81ed89",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18jXqNYtVw3ZtTe1bRa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f2b21f9-4263-4b2e-9f37-ab597217d0c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AanJhD5rwEAYGDAX7eJBuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7552,
      "cache_read_input_tokens": 17459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7552,
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

_source line 40 · 2026-05-13T19:39:07.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uq8FFBpiWwFFApjh4Fp5T7`</summary>

```json
{
  "query": "demonstration ranking scoring task diagnostics robot policy training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f2b21f9-4263-4b2e-9f37-ab597217d0c9",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18jXqNYtVw3ZtTe1bRa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bafc7c5b-9070-4760-8b11-00ede577f4ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AanJhD5rwEAYGDAX7eJBuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7552,
      "cache_read_input_tokens": 17459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7552,
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

_source line 41 · 2026-05-13T19:39:08.125Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SivMbD7CDUzWKS6US4imb1`</summary>

```json
{
  "query": "\"task-level\" diagnostics modality curation robot demonstrations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bafc7c5b-9070-4760-8b11-00ede577f4ce",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18jXqNYtVw3ZtTe1bRa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49bdcd3f-c398-4d1d-80a2-5bc61cdb0f95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AanJhD5rwEAYGDAX7eJBuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7552,
      "cache_read_input_tokens": 17459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7552,
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

_source line 42 · 2026-05-13T19:39:08.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S92H8kMRnMkujArsC69YQQ`</summary>

```json
{
  "query": "Any2Policy visuomotor policy any modality selection NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49bdcd3f-c398-4d1d-80a2-5bc61cdb0f95",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18jXqNYtVw3ZtTe1bRa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ffff561-5ca0-4f4d-a59c-35f9aa52906d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AanJhD5rwEAYGDAX7eJBuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7552,
      "cache_read_input_tokens": 17459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7552,
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

_source line 43 · 2026-05-13T19:39:08.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3dFkcm7tHdnwirNTwe7Ak`</summary>

```json
{
  "query": "ADM-DP adaptive dynamic modality diffusion policy vision tactile 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ffff561-5ca0-4f4d-a59c-35f9aa52906d",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18jXqNYtVw3ZtTe1bRa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eea01f2-f9e2-4174-99d1-85289176f69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AanJhD5rwEAYGDAX7eJBuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7552,
      "cache_read_input_tokens": 17459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7552,
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

_source line 44 · 2026-05-13T19:39:11.644Z_

<details><summary>↩ Tool result · `toolu_01JtjsfULnfyW9cBozj9Qr5o`</summary>

```text
Web search results for query: ""Quality over Quantity" demonstration curation influence functions robot learning 2025 2026"

Links: [{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[2510.18137] Quality Over Quantity: Curating Contact-Based Robot Datasets Improves Learning","url":"https://arxiv.org/abs/2510.18137"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"Quality Over Quantity: Curating Contact-Based Robot Datasets Improves Learning","url":"https://arxiv.org/html/2510.18137"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"Quantifying Demonstration Quality for Robot Learning and Generalization | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/7083369/7339444/09832744.pdf"},{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://arxiv.org/html/2412.14309v1"},{"title":"Quantifying Demonstration Quality for Robot Learning and Generalization","url":"https://arxiv.org/pdf/2203.13843"},{"title":"[2203.13843] Quantifying Demonstration Quality for Robot Learning and Generalization","url":"https://arxiv.org/abs/2203.13843"}]

Based on the web search results, I found several highly relevant papers on demonstration curation and influence functions for robot learning from 2025-2026:

## Primary Result: "Quality over Quantity: Demonstration Curation via Influence Functions"

The most directly relevant paper is "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning" by Haeone Lee and 6 other authors, published on arXiv on March 10, 2026.

This work proposes Quality over Quantity (QoQ), a systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. The paper addresses the critical issue that the quality of demonstration data from human teleoperation remains a bottleneck, with human errors, operational constraints, and teleoperator variability introducing noise.

## Related Works

**CUPID (2025):** Another influential approach formulates robot data curation as valuating demonstrations according to their downstream impact on policy performance, proposing Cupid based on influence functions. Experiments show that curation with Cupid significantly improves policy performance in mixed-quality regimes, even when using only a fraction of the training data.

**Contact-Based Robot Learning (2025):** Research on contact-based datasets shows that more data is not necessarily advantageous, and rather, less but informative data can accelerate learning.

These papers collectively demonstrate that influence functions are emerging as a powerful technique for data curation in robot learning, enabling systematic selection of high-quality demonstrations over simply collecting larger datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f2b21f9-4263-4b2e-9f37-ab597217d0c9",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "fc80af76-b0f3-43b4-afbc-9005b08011fc",
  "sourceToolAssistantUUID": "7f2b21f9-4263-4b2e-9f37-ab597217d0c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T19:39:15.317Z_

<details><summary>↩ Tool result · `toolu_01S92H8kMRnMkujArsC69YQQ`</summary>

```text
Web search results for query: "Any2Policy visuomotor policy any modality selection NeurIPS 2024"

Links: [{"title":"Any2Policy: Learning Visuomotor Policy with Any-Modality","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f13159aecc416659a3c6cef0aecd0d94-Paper-Conference.pdf"},{"title":"NeurIPS Poster Any2Policy: Learning Visuomotor Policy with Any-Modality","url":"https://neurips.cc/virtual/2024/poster/96353"},{"title":"Any2Policy: Learning Visuomotor Policy with Any-Modality | OpenReview","url":"https://openreview.net/forum?id=8lcW9ltJx9"},{"title":"Any2Policy: learning visuomotor policy with any-modality","url":"https://dl.acm.org/doi/10.5555/3737916.3742160"},{"title":"NeurIPS 2024 Schedule","url":"https://neurips.cc/virtual/2024/calendar"},{"title":"Any2Policy: Learning Visuomotor Policy with Any-Modality | Request PDF","url":"https://www.researchgate.net/publication/397220131_Any2Policy_Learning_Visuomotor_Policy_with_Any-Modality"},{"title":"dblp: Feifei Feng","url":"https://dblp.org/pid/27/4916.html"},{"title":"Downloads 2024","url":"https://neurips.cc/Downloads/2024"},{"title":"Any2Policy: Learning Visuomotor Policy with Any-Modality - proceedings.com","url":"https://www.proceedings.com/079017-4244.html"},{"title":"Any2Policy | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3737916.3742160"}]

Based on the search results, here's what I found about Any2Policy:

Any2Policy was presented at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024).

## Overview

Any2Policy is an end-to-end general-purpose multi-modal system that empowers robots to handle tasks using various modalities, whether in combinations like text-image, audio-image, text-point cloud, or in isolation.

## Framework Architecture

The Any2Policy framework is structured to handle multi-modal inputs, accommodating them either separately or in tandem at the levels of instruction and observation, with embodied alignment modules engineered to synchronize features between different modalities, as well as between instructions and observations.

The Any2Policy architecture is structured in two primary components: first, multi-modal encoders extract relevant features from the input, which are then transformed into standardized token representations via projection layers.

## Dataset and Evaluation

The researchers are releasing a substantial real-world dataset consisting of 30 tasks, where each task includes 30 trajectories, all annotated with multi-modal instructions and observations.

The authors conducted extensive validation using several simulation benchmarks, including Franka Kitchen, Meta-World, and Maniskill2, as well as in real-world settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ffff561-5ca0-4f4d-a59c-35f9aa52906d",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "a3298bc4-5b07-4af9-ab89-7aaf6de5e452",
  "sourceToolAssistantUUID": "8ffff561-5ca0-4f4d-a59c-35f9aa52906d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T19:39:15.847Z_

<details><summary>↩ Tool result · `toolu_01SivMbD7CDUzWKS6US4imb1`</summary>

```text
Web search results for query: ""task-level" diagnostics modality curation robot demonstrations"

Links: [{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"Robot Learning from Demonstration: A Task-level Planning Approach - Staffan Ekvall, Danica Kragic, 2008","url":"https://journals.sagepub.com/doi/10.5772/5611"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v1"},{"title":"Augmenting Robotic Capabilities through Natural Language by Albert Yu","url":"https://www.cs.utexas.edu/~ml/papers/yu.proposal25.pdf"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623"},{"title":"(PDF) Robot Learning from Demonstration: A Task-level Planning Approach","url":"https://www.researchgate.net/publication/221787178_Robot_Learning_from_Demonstration_A_Task-level_Planning_Approach"},{"title":"Deployment-Time Reliability of Learned Robot Policies","url":"https://arxiv.org/html/2603.11400v1"}]

Based on the search results, I found several relevant papers on robot demonstration curation. Here's what the research shows:

## Key Research Areas

Recent work focuses on ranking demonstrations by their estimated performance impact to facilitate curation by filtering existing demonstrations from training sets and selecting high-impact demonstrations from newly collected data, formulating robot data curation as the problem of valuating demonstrations according to their downstream impact on policy performance.

### Trajectory-Level Curation

One approach introduces trajectory-wise curation, which aggregates influence scores of state-action pairs within the same trajectory and then selects high-quality trajectories based on the aggregated scores, significantly reducing noise in the influence signal while ensuring broad state coverage and capturing diverse robot behaviors.

### Multi-Modal Task Specifications

Recent work incorporates tactile and force-torque information from human demonstrations to enhance language models' ability to generate plans for new task scenarios through a bootstrapped reasoning pipeline that sequentially integrates each modality into a comprehensive task plan, demonstrating effectiveness in improving understanding of multi-modal demonstrations.

### Self-Supervised Curation Approaches

A unified framework for data curation filters both suboptimal and redundant state-action pairs in large-scale imitation learning datasets using a suboptimality detector based on self-supervised task progress estimation and a deduplication module, showing on average 15.4% improvement in policy performance across diverse benchmarks.

The research demonstrates that effective demonstration curation considers multiple granularities—from individual state-action pairs to full trajectories—and increasingly leverages multi-modal information for more nuanced task understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49bdcd3f-c398-4d1d-80a2-5bc61cdb0f95",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "6d7e11a0-9e84-4525-9844-1cdafa647162",
  "sourceToolAssistantUUID": "49bdcd3f-c398-4d1d-80a2-5bc61cdb0f95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-13T19:39:15.857Z_

<details><summary>↩ Tool result · `toolu_01H3dFkcm7tHdnwirNTwe7Ak`</summary>

```text
Web search results for query: "ADM-DP adaptive dynamic modality diffusion policy vision tactile 2026"

Links: [{"title":"[2602.21622] ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/abs/2602.21622"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://arxiv.org/html/2602.21622"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.21622v1"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation","url":"https://www.researchgate.net/publication/401229345_ADM-DP_Adaptive_Dynamic_Modality_Diffusion_Policy_through_Vision-Tactile-Graph_Fusion_for_Multi-Agent_Manipulation"},{"title":"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation | Gist.Science","url":"https://gist.science/paper/2602.21622"},{"title":"Robotics Research arXiv on X: \"ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation Enyi Wang, Wen Fan, Dandan Zhang https://t.co/d4lIujkZuG [𝚌𝚜.𝚁𝙾] https://t.co/oyjk9wbVP8\" / X","url":"https://x.com/OWW/status/2027262943662911506"},{"title":"Adaptive Visuo-Tactile Fusion with Predictive Force Attention for Dexterous Manipulation","url":"https://arxiv.org/html/2505.13982"},{"title":"Reactive Diffusion Policy:","url":"https://arxiv.org/pdf/2503.02881"},{"title":"ADM: Accelerated Diffusion Model via Estimated Priors for Robust Motion Prediction under Uncertainties","url":"https://arxiv.org/html/2405.00797v1"},{"title":"VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2604.15938"}]

I found relevant information about ADM-DP. Here's what the search reveals:

## ADM-DP: Adaptive Dynamic Modality Diffusion Policy

ADM-DP is a framework that integrates vision, tactile, and graph-based (multi-agent pose) modalities for coordinated control, addressing challenges in multi-agent robotic manipulation.

### Key Innovations

The framework introduces four main innovations:

1. **Enhanced Visual Encoder**: Merges RGB and point-cloud features via Feature-wise Linear Modulation (FiLM) modulation to enrich perception

2. **Tactile-Guided Grasping**: Uses Force-Sensitive Resistor (FSR) feedback to detect insufficient contact and trigger corrective grasp refinement, improving grasp stability

3. **Graph-Based Collision Encoder**: Leverages shared tool center point (TCP) positions of multiple agents as structured kinematic context to maintain spatial awareness and reduce inter-agent interference

4. **Adaptive Modality Attention Mechanism (AMAM)**: Dynamically re-weights modalities according to task context, enabling flexible fusion

### Performance and Results

Across seven multi-agent tasks, ADM-DP achieves 12-25% performance gains over state-of-the-art baselines. ADM-DP achieved an average success rate of 57.1% with 150 demonstrations, outperforming the best baseline (Flow Policy) by 11.7%, and in low-data settings (50 demos), it showed a 13.3% improvement over baselines.

The paper was published on arXiv in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eea01f2-f9e2-4174-99d1-85289176f69b",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "9fe78759-9ac1-4045-b2f4-f6515da3e538",
  "sourceToolAssistantUUID": "8eea01f2-f9e2-4174-99d1-85289176f69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T19:39:15.961Z_

<details><summary>↩ Tool result · `toolu_01Uq8FFBpiWwFFApjh4Fp5T7`</summary>

```text
Web search results for query: "demonstration ranking scoring task diagnostics robot policy training"

Links: [{"title":"RobotArena ∞ : Scalable Robot Benchmarking via Real-to-Sim Translation","url":"https://arxiv.org/html/2510.23571v1"},{"title":": Where Robotic Manipulation Meets Structured and Scalable Evaluation","url":"https://robo-eval.github.io/media/RoboEval.pdf"},{"title":"Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt","url":"https://arxiv.org/html/2505.20795"},{"title":"WorldEval: World Model as Real-World Robot Policies Evaluator","url":"https://arxiv.org/html/2505.19017v1"},{"title":"GitHub - simpler-env/SimplerEnv: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) (CoRL 2024) · GitHub","url":"https://github.com/simpler-env/SimplerEnv"},{"title":"Evaluating Real-World Robot Manipulation Policies in Simulation","url":"https://simpler-env.github.io/"},{"title":"ROBOTARENA ∞: SCALABLE ROBOT BENCHMARKING VIA REAL-TO-SIM TRANSLATION","url":"https://openreview.net/attachment?id=OutljIofvS&name=pdf"},{"title":"RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies","url":"https://arxiv.org/html/2506.18123v1"},{"title":"Diffusion Policy: How Diffusion Models Are Transforming Robot Learning from Demonstration | by Isaac Kargar | Medium","url":"https://kargarisaac.medium.com/diffusion-policy-how-diffusion-models-are-transforming-robot-learning-from-demonstration-32c27ba829cf"},{"title":"Robotics: Science and Systems 2020 Corvalis, Oregon, USA, July 12-16, 2020","url":"https://www.roboticsproceedings.org/rss16/p082.pdf"}]

I've performed a web search on your query about demonstration ranking, scoring, task diagnostics, robot policy training. Here are the key findings:

## Main Research Areas Found

**1. Robot Policy Evaluation Frameworks:**

ROBOEVAL is a simulation benchmark and evaluation framework for fine-grained analysis of bimanual robotic manipulation, featuring a suite of tiered manipulation tasks decomposed into semantically grounded stages targeting specific skills such as pushing, grasping, holding, rotating, lifting, etc.

**2. Demonstration-Based Ranking and Scoring:**

An approach proposes to crowd-source evaluations across a distributed network of evaluators, where evaluators can freely choose the tasks and environments they evaluate on while performing double-blind evaluations over pairs of policies, and by aggregating preference feedback from pairwise comparisons across diverse tasks and environments, a ranking of policies can be derived.

**3. Task Diagnostics:**

Diagnostic interpretability is enabled via outcome metrics that capture stagewise progress and task success, and behavior metrics that capture spatial and temporal precision, trajectory properties, and bimanual coordination.

**4. Policy Training from Demonstrations:**

A framework utilizes human demonstrations to learn a generalizable robot policy that can directly take human demonstration video as a prompt and perform new tasks without any new teleoperation data and model finetuning.

**5. Policy Ranking Systems:**

Research shows BT rankings of models from human preferences with confidence intervals, where human preferences align with VLM task progress scores.

These search results cover multiple approaches to ranking, scoring, and diagnosing robot policies trained from demonstrations, spanning simulation-based evaluation, real-world testing, and various metrics for assessing policy performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bafc7c5b-9070-4760-8b11-00ede577f4ce",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "0a110759-c954-45e2-82ed-400c512e29de",
  "sourceToolAssistantUUID": "bafc7c5b-9070-4760-8b11-00ede577f4ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-13T19:39:27.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019TkvqgdkPSJDurdYKnatMR`</summary>

```json
{
  "query": "SCIZOR self-supervised data curation imitation learning task progress 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a110759-c954-45e2-82ed-400c512e29de",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18kkSgRjcsoNTrfLp5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21f2bf79-9a1f-455d-aa40-a3ac6c0171e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2AzJfrtQErnz3TrgfEChb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2737,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 25011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 50 · 2026-05-13T19:39:28.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vn1FZKDfFEWEUbBkuxU5tP`</summary>

```json
{
  "query": "CUPID curating data robot influence functions demonstration curation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f2bf79-9a1f-455d-aa40-a3ac6c0171e8",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18kkSgRjcsoNTrfLp5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09e0b8bd-b812-4ed9-b4a5-644cc9e29cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2AzJfrtQErnz3TrgfEChb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2737,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 25011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 51 · 2026-05-13T19:39:29.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LA6BtktfNASsfqKkg1RayB`</summary>

```json
{
  "query": "\"Consistency Matters\" demonstration data quality metrics robot learning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09e0b8bd-b812-4ed9-b4a5-644cc9e29cf3",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18kkSgRjcsoNTrfLp5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e81ad11-14da-413b-8d2d-98adefc55d88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2AzJfrtQErnz3TrgfEChb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2737,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 25011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 52 · 2026-05-13T19:39:29.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GaaTygXXiQFRDUjmB2NW8t`</summary>

```json
{
  "query": "robot data curation mutual information estimators 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e81ad11-14da-413b-8d2d-98adefc55d88",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18kkSgRjcsoNTrfLp5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdc30779-897c-4b08-adcb-93bd9e9ddac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2AzJfrtQErnz3TrgfEChb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2737,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 25011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 53 · 2026-05-13T19:39:30.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LySmy9Mm3WqaXpZzNbVmpY`</summary>

```json
{
  "query": "\"Re-Mix\" optimizing data mixtures large scale imitation learning robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdc30779-897c-4b08-adcb-93bd9e9ddac4",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18kkSgRjcsoNTrfLp5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ee699fe-bb10-4c99-96c1-418b6b1dd505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2AzJfrtQErnz3TrgfEChb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2737,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 25011,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2106
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2737,
          "output_tokens": 262,
          "cache_read_input_tokens": 25011,
          "cache_creation_input_tokens": 2106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2106,
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

_source line 54 · 2026-05-13T19:39:34.234Z_

<details><summary>↩ Tool result · `toolu_01Vn1FZKDfFEWEUbBkuxU5tP`</summary>

```text
Web search results for query: "CUPID curating data robot influence functions demonstration curation 2025"

Links: [{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"GitHub - agiachris/cupid: Official repository for \"CUPID: Curating Data your Robot Loves with Influence Functions,\" accepted to CoRL 2025. · GitHub","url":"https://github.com/agiachris/cupid"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"}]

Based on the search results, I found comprehensive information about CUPID:

## CUPID: Curating Data your Robot Loves with Influence Functions

CUPID (CUrating Performance-Influencing Demonstrations) is a data curation method for robot imitation learning that uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance.

### Core Methodology

CUPID is a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies that estimates the influence of each training demonstration on the policy's expected return. This enables ranking and selection of demonstrations according to their impact on the policy's closed-loop performance.

### Data Curation Applications

CUPID is used to curate data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy.

### Experimental Results

Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Hardware experiments show that our method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.

### Publication Status

CUPID was accepted to Conference on Robot Learning (CoRL) 2025. The official code and resources are available through their GitHub repository and project website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09e0b8bd-b812-4ed9-b4a5-644cc9e29cf3",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "659d2125-e44e-4609-a954-27fb0b8ea422",
  "sourceToolAssistantUUID": "09e0b8bd-b812-4ed9-b4a5-644cc9e29cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-13T19:39:34.542Z_

<details><summary>↩ Tool result · `toolu_019TkvqgdkPSJDurdYKnatMR`</summary>

```text
Web search results for query: "SCIZOR self-supervised data curation imitation learning task progress 2025"

Links: [{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning","url":"https://ut-austin-rpl.github.io/SCIZOR/"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v2"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"[PDF] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SCIZOR:-A-Self-Supervised-Approach-to-Data-Curation-Zhang-Xie/1a601961be1a3facbacc68205b9279216e802c5c"},{"title":"GitHub - UT-Austin-RPL/SCIZOR · GitHub","url":"https://github.com/UT-Austin-RPL/SCIZOR"},{"title":"[Literature Review] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.themoonlight.io/en/review/scizor-a-self-supervised-approach-to-data-curation-for-large-scale-imitation-learning"},{"title":"A self-supervised approach to data curation for large-scale imitation learning","url":"https://repositories.lib.utexas.edu/items/0d6721a9-20a3-48dd-a0c9-f4d6a4d494e1"},{"title":"Copyright by Yuqi Xie 2025 1","url":"https://repositories.lib.utexas.edu/bitstreams/d8256e22-405e-4881-87d8-ca3f8008345e/download"}]

Based on the search results, here's what I found about SCIZOR and its 2025 progress:

## Overview

SCIZOR is a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies. SCIZOR leverages a self-supervised task progress predictor for suboptimal data to remove samples lacking task progression, and a deduplication module operating on joint state-action representation for samples with redundant patterns.

## Key Task Progress Component

The framework includes a progress-prediction model [that] flags and removes frames that fail to make meaningful task progress, without needing reward signals. This self-supervised approach to identifying suboptimal transitions is central to the method's effectiveness.

## 2025 Progress and Results

SCIZOR enables imitation learning policies to achieve higher performance with less data, yielding an average improvement of 15.4% across multiple benchmarks. More specifically, compared to training on the full dataset, SCIZOR delivers absolute gains of 5.4% on RoboMimic, 8.1% on OXE-Magic-Soup, and 32.9% on the Sirius-Fleet real-robot tasks.

The work is scheduled to appear at the IEEE International Conference on Robotics and Automation (ICRA) in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f2bf79-9a1f-455d-aa40-a3ac6c0171e8",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "669426fd-c983-49e9-811d-7feaa3289d6f",
  "sourceToolAssistantUUID": "21f2bf79-9a1f-455d-aa40-a3ac6c0171e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T19:39:37.198Z_

<details><summary>↩ Tool result · `toolu_01LA6BtktfNASsfqKkg1RayB`</summary>

```text
Web search results for query: ""Consistency Matters" demonstration data quality metrics robot learning 2024"

Links: [{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://arxiv.org/html/2412.14309v1"},{"title":"[2412.14309] Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://arxiv.org/abs/2412.14309"},{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration | ACM Transactions on Human-Robot Interaction","url":"https://dl.acm.org/doi/abs/10.1145/3773904"},{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration | Request PDF","url":"https://www.researchgate.net/publication/396997300_Consistency_Matters_Defining_Demonstration_Data_Quality_Metrics_in_Robot_Learning_from_Demonstration"},{"title":"(PDF) Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://www.researchgate.net/publication/387222678_Consistency_Matters_Defining_Demonstration_Data_Quality_Metrics_in_Robot_Learning_from_Demonstration"},{"title":"Maram Sakr's research works","url":"https://www.researchgate.net/scientific-contributions/Maram-Sakr-2329156489"},{"title":"Human-Computer Interaction Dec 2024","url":"https://arxiv.org/list/cs.HC/2024-12?skip=325&show=25"},{"title":"Quantifying Demonstration Quality for Robot Learning and Generalization","url":"https://arxiv.org/pdf/2203.13843"},{"title":"Robotics Dec 2024","url":"https://arxiv.org/list/cs.RO/2024-12?skip=350&show=500"},{"title":"Beyond Success: Quantifying Demonstration Quality in Learning from","url":"https://wafa.johal.org/files/papers/bilal2024.pdf"}]

Based on the search results, I found comprehensive information about "Consistency Matters," a 2024 research paper on demonstration data quality metrics in robot learning.

## Overview

Learning from Demonstration (LfD) empowers robots to acquire new skills through human demonstrations, making it feasible for everyday users to teach robots. However, the success of learning and generalization heavily depends on the quality of these demonstrations.

## Key Research Focus

Consistency is often used to indicate quality in LfD, yet the factors that define this consistency remain underexplored. The paper evaluates a comprehensive set of motion data characteristics to determine which consistency measures best predict learning performance.

## Study Design

The approach was validated with two user studies involving participants with diverse levels of robotics expertise. In the first study (N = 24), users taught a PR2 robot to perform a button-pressing task in a constrained environment, while in the second study (N = 30), participants trained a UR5 robot on a pick-and-place task.

## Key Results

Results show that demonstration consistency significantly impacts success rates in both learning and generalization, with 70% and 89% of task success rates in the two studies predicted using our consistency metrics. Moreover, the metrics estimate generalized performance success rates with 76% and 91% accuracy.

## Significance

The proposed measures provide an intuitive, practical way to assess demonstration data quality before training, without requiring expert data or algorithm-specific modifications. The approach offers a systematic way to evaluate demonstration quality, addressing a critical gap in LfD by formalizing consistency metrics that enhance the reliability of robot learning from human demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e81ad11-14da-413b-8d2d-98adefc55d88",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "830d9aaa-3d59-41d8-9514-804acf8d35e1",
  "sourceToolAssistantUUID": "1e81ad11-14da-413b-8d2d-98adefc55d88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-13T19:39:37.236Z_

<details><summary>↩ Tool result · `toolu_01LySmy9Mm3WqaXpZzNbVmpY`</summary>

```text
Web search results for query: ""Re-Mix" optimizing data mixtures large scale imitation learning robot"

Links: [{"title":"[2408.14037] Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning","url":"https://arxiv.org/abs/2408.14037"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning","url":"https://arxiv.org/html/2408.14037v1"},{"title":"ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning","url":"https://proceedings.mlr.press/v270/hejna25a.html"},{"title":"ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=fIj88Tn3fc"},{"title":"ReMix: Optimizing Data Mixtures for Large Scale Imitation ...","url":"https://hai.stanford.edu/research/remix-optimizing-data-mixtures-for-large-scale-imitation-learning"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240814037H/abstract"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning","url":"https://www.researchgate.net/publication/383428925_Re-Mix_Optimizing_Data_Mixtures_for_Large_Scale_Imitation_Learning"},{"title":"[PDF] Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/de3dfd3075597c5f46d423d2c7f1bb95b456d0f8"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/re-mix-optimizing-data-mixtures-large-scale"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2408.14037"}]

Based on the search results, here's what I found about "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning":

## Overview

Re-Mix is a method for optimizing data mixtures in large imitation learning datasets being collected to train foundation models for robotics. The work investigates how to weigh different subsets or "domains" of robotics datasets for robot foundation model pre-training, using distributionally robust optimization (DRO) to maximize worst-case performance across all possible downstream domains.

## Key Technical Approach

Re-Mix addresses challenges that arise when applying DRO to robotics datasets including variability in action spaces and dynamics across different datasets, employing early stopping, action normalization, and discretization to counteract these issues. The method instantiates the data curation problem as a min-max optimization, where a policy minimizes its excess behavior cloning loss over a reference model subject to learned domain mixture weights that try to maximize it, with the excess loss measuring how much room the policy has to improve on a given domain.

## Results

Through extensive experimentation on the largest open-source robot manipulation dataset, the Open X-Embodiment dataset, the authors demonstrate that domain weights learned by Re-Mix outperform uniform weights by 38% on average and outperform human-selected weights by 32% on datasets used to train existing generalist robot policies, specifically the RT-X models.

The paper was first published on arXiv in August 2024 and has since been accepted to the 8th Conference on Robot Learning (CoRL) in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ee699fe-bb10-4c99-96c1-418b6b1dd505",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "a8d5ff36-1223-426b-bed7-b18ef805791e",
  "sourceToolAssistantUUID": "8ee699fe-bb10-4c99-96c1-418b6b1dd505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-13T19:39:38.117Z_

<details><summary>↩ Tool result · `toolu_01GaaTygXXiQFRDUjmB2NW8t`</summary>

```text
Web search results for query: "robot data curation mutual information estimators 2025"

Links: [{"title":"[2502.08623] Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/abs/2502.08623"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623v2"},{"title":"GitHub - jhejna/demonstration-information: Code for the paper Robot Data Curation with Mutual Information Estimators","url":"https://github.com/jhejna/demonstration-information"},{"title":"[PDF] Robot Data Curation with Mutual Information Estimators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/37cb83dc757f483cfd389c8709b4aee389da8dc6"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"Robot Data Curation with Mutual Information Estimators · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/23/"},{"title":"Robot Data Curation with Mutual Information Estimators | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.08623v3"},{"title":"Suvir Mirchandani's research works | Google Inc. and other places","url":"https://www.researchgate.net/scientific-contributions/Suvir-Mirchandani-2191262582"},{"title":"Robot Data Curation","url":"https://www.roboticsproceedings.org/rss21/p023.pdf"},{"title":"Dorsa SADIGH | University of California, Berkeley, Berkeley | UCB | Department of Electrical Engineering and Computer Sciences | Research profile","url":"https://www.researchgate.net/profile/Dorsa-Sadigh-2"}]

Based on the search results, I found comprehensive information about this research topic. Here's what the search revealed:

## Robot Data Curation with Mutual Information Estimators (2025)

The paper "Robot Data Curation with Mutual Information Estimators" was submitted on February 12, 2025, with the latest version on April 22, 2025, authored by Joey Hejna, Suvir Mirchandani, Ashwin Balakrishna, Annie Xie, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Dhruv Shah, Coline Devin, and Dorsa Sadigh.

### Core Problem and Approach

Despite marked increases in demonstration quantities collected, little work has assessed data quality, despite mounting evidence of its importance in vision and language. The researchers aim to estimate the relative quality of individual demonstrations in terms of both action diversity and predictability.

### Technical Innovation

Rather than using commonly used mutual information estimators that require vast amounts of data, they introduce a novel technique based on k-nearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions. The method is called Demonstration Information Estimation (DemInf), an unsupervised method for curating robot demonstration datasets by using mutual information between states and actions as a proxy for data quality.

### Results

The approach is able to partition demonstration datasets by quality according to human expert scores across diverse benchmarks spanning simulation and real world environments, with training policies based on filtered data leading to 5-10% improvement in RoboMimic and better performance on real ALOHA and Franka setups.

Code accompanying the paper is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdc30779-897c-4b08-adcb-93bd9e9ddac4",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "84042ac1-6956-4b7e-b01f-87359981f821",
  "sourceToolAssistantUUID": "cdc30779-897c-4b08-adcb-93bd9e9ddac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-13T19:39:41.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011fZKNcA1WpbVZQoTfPLgTR`</summary>

```json
{
  "query": "\"curating demonstrations using online experience\" robot imitation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84042ac1-6956-4b7e-b01f-87359981f821",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18nPCnoYhNDQZ8nYU2D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27598e3c-eb62-4424-9da8-2d074a7fd6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gyj2m9pKGMN6n6i2Qc4y9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 6705,
      "cache_read_input_tokens": 27117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6705,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 60 · 2026-05-13T19:39:42.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018cKdW1qEfKTcrueWmyrNvL`</summary>

```json
{
  "query": "proprioception visual modality when helpful robot manipulation task analysis diagnostic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27598e3c-eb62-4424-9da8-2d074a7fd6fd",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18nPCnoYhNDQZ8nYU2D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "111c47fa-5922-4deb-9bda-203f66f4eb8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gyj2m9pKGMN6n6i2Qc4y9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 6705,
      "cache_read_input_tokens": 27117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6705,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 61 · 2026-05-13T19:39:43.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015r1SC77TEExRjLdP19LrG6`</summary>

```json
{
  "query": "Robometer trajectory comparison reward model robot ranking Bradley-Terry 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "111c47fa-5922-4deb-9bda-203f66f4eb8b",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18nPCnoYhNDQZ8nYU2D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f871b3b6-1071-4d2a-99ba-408780afed17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gyj2m9pKGMN6n6i2Qc4y9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 6705,
      "cache_read_input_tokens": 27117,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6705
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 961,
          "output_tokens": 161,
          "cache_read_input_tokens": 27117,
          "cache_creation_input_tokens": 6705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6705,
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

_source line 62 · 2026-05-13T19:39:48.760Z_

<details><summary>↩ Tool result · `toolu_011fZKNcA1WpbVZQoTfPLgTR`</summary>

```text
Web search results for query: ""curating demonstrations using online experience" robot imitation 2025"

Links: [{"title":"[2503.03707] Curating Demonstrations using Online Experience","url":"https://arxiv.org/abs/2503.03707"},{"title":"Curating Demonstrations using Online Experience · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/71/"},{"title":"Curating Demonstrations using Online Experience","url":"https://www.researchgate.net/publication/395366581_Curating_Demonstrations_using_Online_Experience"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"Curating Demonstrations using Online Experience | alphaXiv","url":"https://www.alphaxiv.org/en/overview/2503.03707"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121"},{"title":"[PDF] Curating Demonstrations using Online Experience | Semantic Scholar","url":"https://www.semanticscholar.org/paper/776c9466ece2a34832d4ebef206fa5c2e9855b39"},{"title":"DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration","url":"https://arxiv.org/html/2506.05064v2"},{"title":"[Literature Review] Curating Demonstrations using Online Experience","url":"https://www.themoonlight.io/en/review/curating-demonstrations-using-online-experience"}]

Based on the web search results, here's what I found about "Curating Demonstrations using Online Experience" and robot imitation learning:

## Demo-SCORE Method

The paper "Curating Demonstrations using Online Experience" by Annie S. Chen, Alec M. Lessing, Yuejiang Liu, and Chelsea Finn proposes a method called Demo-SCORE aimed at improving robotic learning from heterogeneous demonstration datasets.

## The Core Problem

Many robot demonstration datasets contain heterogeneous demonstrations of varying quality. This heterogeneity may benefit policy pre-training, but can hinder robot performance when used with a final imitation learning objective. Some strategies in the data may be less reliable than others or may be underrepresented in the data, leading to poor performance when such strategies are sampled at test time. Moreover, such unreliable or underrepresented strategies can be difficult even for people to discern, and sifting through demonstration datasets is time-consuming and costly.

## The Approach

The proposal is for robots to self-curate based on online robot experience (Demo-SCORE). More specifically, they train and cross-validate a classifier to discern successful policy roll-outs from unsuccessful ones and use the classifier to filter heterogeneous demonstration datasets.

## Results

Experiments in simulation and the real world show that Demo-SCORE can effectively identify suboptimal demonstrations without manual curation. Notably, Demo-SCORE achieves over 15-35% higher absolute success rate in the resulting policy compared to the base policy trained with all original demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27598e3c-eb62-4424-9da8-2d074a7fd6fd",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "a820b615-ab0f-4b6d-b288-a924ce3882aa",
  "sourceToolAssistantUUID": "27598e3c-eb62-4424-9da8-2d074a7fd6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-13T19:39:50.901Z_

<details><summary>↩ Tool result · `toolu_018cKdW1qEfKTcrueWmyrNvL`</summary>

```text
Web search results for query: "proprioception visual modality when helpful robot manipulation task analysis diagnostic"

Links: [{"title":"Frontiers | Reinforcement Learning With Vision-Proprioception Model for Robot Planar Pushing","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2022.829437/full"},{"title":"Scaling Proprioceptive-Visual Learning with ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e0f393e7980a24fd12fa6f15adfa25fb-Paper-Conference.pdf"},{"title":"Latent Representations for Visual Proprioception in Inexpensive Robots","url":"https://arxiv.org/html/2504.14634v1"},{"title":"Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing","url":"https://www.touchprocessing.org/2023/camera_ready/camera_ready_7.pdf"},{"title":"General In-Hand Object Rotation with Vision and Touch Haozhi Qi1,2 Brent Yi1","url":"https://proceedings.mlr.press/v229/qi23a/qi23a.pdf"},{"title":"A robot-aided visuo-motor training that improves proprioception and spatial accuracy of untrained movement | Scientific Reports","url":"https://www.nature.com/articles/s41598-017-16704-8"},{"title":"NeuralFeels with neural fields: Visuotactile perception for in-hand manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adl0628"},{"title":"Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing","url":"https://arxiv.org/html/2312.01853v3"},{"title":"spatial AI with vision and touch for robot manipulation ...","url":"https://www.ri.cmu.edu/app/uploads/2024/02/Sudharshan_thesis.pdf"},{"title":"Touch in the Wild: Learning Fine-Grained Manipulation ...","url":"https://openreview.net/pdf?id=WabVVQKTUF"}]

I've completed the web search for your query about proprioception, visual modality, robot manipulation, and task analysis. Here are the key findings:

## Key Research Findings

**Multi-modal Integration for Robot Manipulation:**

Research shows that vision-proprioception models fuse these two modalities and perform planning in the fusion space, inspired by how humans solve tasks through both vision and proprioception.

**When Visual Information is Helpful:**

The search results reveal several scenarios where visual modality provides crucial benefits:

1. **Disambiguation Tasks**: When tactile feedback alone cannot distinguish between objects (such as identical balls), visual information becomes crucial for the robot to locate them.

2. **Global Context vs. Local Precision**: Studies show optimal fusion of multimodal signals where vision gives coarse global context while touch gives precise local information—vision can locate objects on cluttered surfaces while touch singulates fine details for firm grasps.

3. **Handling Occlusion**: Although vision-only baselines may suffice for some scenarios, results validate the utility of rich multimodal sensing for interactive tasks, and when combined with touch, visual estimates are robustified by providing a window into local interactions.

**Diagnostic Insights:**

Results can help identify parts of a robot's configuration that must have internal proprioception and ones that can be left to visual observation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "111c47fa-5922-4deb-9bda-203f66f4eb8b",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "61754865-4b8d-4911-b9b4-2d7fd1404c4d",
  "sourceToolAssistantUUID": "111c47fa-5922-4deb-9bda-203f66f4eb8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T19:39:51.020Z_

<details><summary>↩ Tool result · `toolu_015r1SC77TEExRjLdP19LrG6`</summary>

```text
Web search results for query: "Robometer trajectory comparison reward model robot ranking Bradley-Terry 2026"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Recent advances in the Bradley–Terry Model: theory, algorithms, and applications","url":"https://arxiv.org/html/2601.14727v1"},{"title":"Bradley–Terry model - Wikipedia","url":"https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model"},{"title":"ROBOMETER: Scaling Robotic Reward Models - YouTube","url":"https://www.youtube.com/watch?v=WBBdgLdncG4"}]

## Search Results

I found comprehensive information about Robometer. Here's what the search revealed:

### Robometer Overview

Robometer is a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision, trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task.

### Key Features

Robometer is a general-purpose robotic reward model trained on trajectory comparisons from the RBM-1M dataset that provides dense, video-language-conditioned rewards for robot learning.

### RBM-1M Dataset

RBM-1M is a reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

### Performance

Robometer outperforms state-of-the-art baselines by an average of 14% in reward rank correlation and 32% relative improvement across external benchmarks and out-of-distribution evaluations.

### Publication

Robometer was presented at Robotics: Science and Systems (RSS) 2026, with the paper submitted to arXiv on March 2, 2026.

Regarding the Bradley-Terry model mentioned in your query: while the search results reference the Bradley-Terry model in a separate paper about preference-based ranking, the Robometer paper itself doesn't explicitly mention using Bradley-Terry models, though it does employ pairwise trajectory comparisons which relate to preference-based ranking methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f871b3b6-1071-4d2a-99ba-408780afed17",
  "isSidechain": true,
  "promptId": "0550eaef-cd1f-4c7b-8cd6-2da723f3226e",
  "agentId": "a99fa48a1385f86f4",
  "type": "user",
  "uuid": "424febdf-5c07-4985-a82f-b19ae8c2db8f",
  "sourceToolAssistantUUID": "f871b3b6-1071-4d2a-99ba-408780afed17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-13T19:41:16.877Z_

Here is a comprehensive report of all relevant competing work found across the 10 searches, organized by relevance to the paper's claims.

---

## Most Directly Competing Work (Demonstration Curation Methods)

### 1. CUPID: Curating Data your Robot Loves with Influence Functions
- **Venue:** CoRL 2025
- **Date:** June 2025 (arXiv)
- **Key idea:** Uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop expected return. Ranks demonstrations by their downstream impact on policy performance. Training with <33% curated data can match or beat full-dataset policies.
- **Relevance:** Directly addresses demonstration curation via ranking, but does NOT provide task-level diagnostics for when proprioceptive scoring helps -- it is modality-agnostic.
- [Paper](https://arxiv.org/abs/2506.19121)

### 2. Quality over Quantity (QoQ): Demonstration Curation via Influence Functions for Data-Centric Robot Learning
- **Venue:** arXiv preprint
- **Date:** March 10, 2026
- **Key idea:** Defines data quality as the contribution of each training sample to reducing loss on validation demonstrations. Uses influence functions with trajectory-level aggregation to reduce noise.
- **Relevance:** Very close competitor -- systematic quality ranking of demonstrations. Does NOT examine multimodal scoring or proprioceptive vs. visual modality diagnostics.
- [Paper](https://arxiv.org/abs/2603.09056)

### 3. SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning
- **Venue:** ICRA 2026
- **Date:** May 2025 (arXiv)
- **Key idea:** Unified framework with a self-supervised task-progress predictor that filters suboptimal state-action pairs, plus a deduplication module. Achieves 15.4% average improvement across RoboMimic, OXE-Magic-Soup, and Sirius-Fleet benchmarks.
- **Relevance:** Task-progress-based curation at scale. No multimodal/proprioceptive diagnostics.
- [Paper](https://arxiv.org/abs/2505.22626)

### 4. DataMIL: Selecting Data for Robot Imitation Learning with Datamodels
- **Venue:** arXiv preprint (May 2025), under review
- **Date:** May 14, 2025
- **Key idea:** Policy-driven data selection using the datamodels paradigm. Trains a data-quality estimator using validation loss as a tractable proxy for true policy performance. Tested on 60+ simulation and real tasks including Open X-Embodiment.
- **Relevance:** End-to-end data selection that avoids human heuristics, but is purely policy-performance-driven -- no modality-level analysis.
- [Paper](https://arxiv.org/abs/2505.09603)

### 5. Robot Data Curation with Mutual Information Estimators (DemInf)
- **Venue:** RSS 2025
- **Date:** February 2025 (arXiv)
- **Key idea:** Uses k-nearest-neighbor mutual information estimates on VAE embeddings of states and actions as a proxy for demonstration quality. Unsupervised method that partitions datasets by quality matching human expert scores.
- **Relevance:** Information-theoretic quality scoring. Operates on state-action pairs but does not diagnose which modality (vision vs. proprioception) drives quality differences.
- [Paper](https://arxiv.org/abs/2502.08623)

### 6. Demo-SCORE: Curating Demonstrations using Online Experience
- **Venue:** RSS 2025
- **Date:** March 2025 (arXiv)
- **Key idea:** Robots self-curate demonstrations by training a classifier to distinguish successful from unsuccessful policy rollouts, then filtering demonstrations accordingly. Achieves 15-35% higher success rate vs. uncurated data.
- **Relevance:** Online-experience-driven curation. No modality-level diagnostics.
- [Paper](https://arxiv.org/abs/2503.03707)

### 7. Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning
- **Venue:** CoRL 2025
- **Date:** August 2024 (arXiv)
- **Key idea:** Uses distributionally robust optimization (DRO) to learn domain mixture weights for robot foundation model pre-training. Outperforms uniform weights by 38% and human-selected weights by 32% on Open X-Embodiment.
- **Relevance:** Data mixture optimization at the dataset/domain level rather than per-demonstration curation.
- [Paper](https://arxiv.org/abs/2408.14037)

---

## Most Directly Competing Work (Modality Selection / When Does Proprioception Help)

### 8. Modality Selection and Skill Segmentation via Cross-Modality Attention (CMA)
- **Venue:** IEEE (ICRA 2025 or similar)
- **Date:** April 20, 2025 (arXiv)
- **Key idea:** A Cross-Modality Attention mechanism dynamically selects the most informative sensory modality (vision, tactile, proprioception) at each timestep for action generation. Also segments primitive skills from demonstrations for hierarchical policy learning.
- **Relevance:** **HIGHLY RELEVANT** -- directly addresses modality selection (including proprioception) on a per-timestep basis. However, it operates at the policy-architecture level (dynamic attention weights during inference), not at the demonstration-curation level. Does not provide task-level diagnostics mapping observability across a task suite.
- [Paper](https://arxiv.org/abs/2504.14573)

### 9. Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation
- **Venue:** arXiv preprint
- **Date:** April 2026
- **Key idea:** Proposes contact-gating that filters out inertia-induced interference on torque data during free-space motion, plus CFG-style vision-torque fusion for adaptive modality weighting. 14% success rate improvement over baselines.
- **Relevance:** **HIGHLY RELEVANT** -- directly investigates when vision vs. force/torque is helpful, with an adaptive mechanism. Provides implicit task-phase-level diagnostics (contact vs. non-contact). However, it is about policy architecture, not demonstration curation.
- [Paper](https://arxiv.org/abs/2604.01414)

### 10. ADM-DP: Adaptive Dynamic Modality Diffusion Policy
- **Venue:** arXiv preprint
- **Date:** February 2026
- **Key idea:** Introduces an Adaptive Modality Attention Mechanism (AMAM) that dynamically re-weights vision, tactile, and graph-based modalities according to task context in multi-agent manipulation. 12-25% gains over baselines.
- **Relevance:** Adaptive modality fusion at the policy level with task-context-dependent weighting. Not focused on demonstration curation.
- [Paper](https://arxiv.org/abs/2602.21622)

### 11. Any2Policy: Learning Visuomotor Policy with Any-Modality
- **Venue:** NeurIPS 2024
- **Date:** 2024
- **Key idea:** End-to-end multi-modal system handling any combination of modalities (text-image, audio-image, text-point cloud, etc.) via embodied alignment modules. Validated on 30 real-world tasks.
- **Relevance:** Modality-agnostic policy learning, but does not analyze WHEN specific modalities help or provide task-level diagnostics.
- [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/f13159aecc416659a3c6cef0aecd0d94-Paper-Conference.pdf)

---

## VLA-Specific Data Curation / Quality Pipelines

### 12. Green-VLA: Staged Vision-Language-Action Model (DataQA Pipeline)
- **Venue:** arXiv preprint
- **Date:** February 2026
- **Key idea:** DataQA pipeline for robotic dataset curation using jitter, sharpness, diversity, and variance metrics, plus optical-flow-based temporal resampling. Achieves better results with 3,000 hours than competitors with 10,000+ hours.
- **Relevance:** Multimodal data quality filtering for VLA training, but metrics are primarily visual quality metrics (sharpness, jitter) rather than proprioceptive scoring.
- [Paper](https://arxiv.org/abs/2602.00919)

### 13. Seed2Scale: A Self-Evolving Data Engine for Embodied AI
- **Venue:** arXiv preprint
- **Date:** March 2026
- **Key idea:** Uses a lightweight VLA (SuperTiny) for data collection and a large VLM as a quality verifier/filter. Starting from 4 seed demos, achieves 209% success rate improvement through self-iteration.
- **Relevance:** Quality filtering at the trajectory level via VLM verification, but no proprioceptive scoring or task-level modality diagnostics.
- [Paper](https://arxiv.org/abs/2603.08260)

---

## Reward Models for Demonstration Quality

### 14. Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons
- **Venue:** RSS 2026
- **Date:** March 2026
- **Key idea:** Dense video-language reward model trained with dual objective (frame-level progress + trajectory-comparison preference loss) on the RBM-1M dataset (1M+ trajectories). 14% better reward rank correlation than baselines.
- **Relevance:** Uses ranking theory (trajectory comparisons/preference learning) for quality assessment. The closest work to using ranking theory for demonstration quality, though focused on reward modeling rather than curation.
- [Paper](https://arxiv.org/abs/2603.02115)

### 15. SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation
- **Venue:** ICLR 2026
- **Date:** September 2025 (arXiv)
- **Key idea:** Stage-aware video-based reward model that jointly predicts task stage and fine-grained progress using natural-language subtask annotations. Addresses inconsistent demonstration quality in contact-rich tasks.
- **Relevance:** Stage-level quality assessment that handles variable demonstration quality, but focused on reward modeling for RL rather than demonstration curation.
- [Paper](https://arxiv.org/abs/2509.25358)

### 16. RoboReward
- **Venue:** Published January 2026
- **Key idea:** Dataset of real robot videos with text descriptions and progress scores, used to train VLMs that judge how well robots complete tasks. RoboReward 4B/8B outperform larger VLMs on reward accuracy.
- **Relevance:** VLM-based quality scoring of robot demonstrations.
- [Source](https://techxplore.com/news/2026-01-roboreward-dataset-automate-robotic.html)

---

## Demonstration Quality Metrics (Foundational)

### 17. Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration
- **Venue:** ACM Transactions on Human-Robot Interaction
- **Date:** December 2024 (arXiv)
- **Key idea:** Formalizes consistency metrics (motion characteristics) that predict demonstration quality before training. Achieves 70-91% prediction accuracy for task success rates.
- **Relevance:** Foundational work on pre-training quality metrics for demonstrations, but focused on consistency of human demonstrations rather than modality-specific scoring.
- [Paper](https://arxiv.org/abs/2412.14309)

### 18. Quantifying Demonstration Quality for Robot Learning and Generalization
- **Venue:** IEEE RA-L, 2022
- **Key idea:** Early work on quantifying demonstration quality and its effect on learning and generalization.
- **Relevance:** Precursor work in the demonstration quality space.
- [Paper](https://arxiv.org/abs/2203.13843)

---

## Gap Analysis: Does the Paper's Novelty Claim Hold?

Based on this comprehensive search, the paper's claim of being "the first to provide task-level diagnostics for when proprioceptive scoring helps demonstration curation" appears **largely supported but with important caveats**:

1. **No existing work combines all three elements** (proprioceptive scoring + demonstration curation + task-level diagnostics). Each element exists separately in the literature.

2. **Closest competitors on modality selection** (CMA, Learning When to See/Feel, ADM-DP) operate at the policy-architecture level, not at the curation level. They adaptively weight modalities during inference but do not provide diagnostics about which tasks benefit from proprioceptive scoring during data curation.

3. **Closest competitors on demonstration curation** (CUPID, QoQ, SCIZOR, DataMIL, DemInf, Demo-SCORE) are modality-agnostic -- they score/rank demonstrations without distinguishing whether proprioceptive or visual features drive quality differences.

4. **The Green-VLA DataQA pipeline** does multimodal quality filtering for VLA training, but its metrics are primarily visual (sharpness, jitter, diversity) rather than proprioceptive.

5. **Robometer** uses ranking theory (trajectory comparisons) for quality assessment, which is relevant if the paper under review also uses ranking theory, but Robometer is about reward modeling rather than modality-specific curation diagnostics.

**Potential gaps the authors should acknowledge:**
- The CMA paper (search result #8) does per-timestep modality selection including proprioception and could be seen as providing implicit diagnostics about when proprioception matters, even though it operates at the policy level.
- The "Learning When to See and When to Feel" paper (search result #9, April 2026) directly investigates when vision vs. force/torque helps, with contact-gating providing task-phase-level diagnostics -- this is very recent and may have been concurrent work.
- The DemInf/mutual information approach could theoretically be extended to provide modality-specific quality scores.

Sources:
- [CUPID](https://arxiv.org/abs/2506.19121)
- [Quality over Quantity (QoQ)](https://arxiv.org/abs/2603.09056)
- [SCIZOR](https://arxiv.org/abs/2505.22626)
- [DataMIL](https://arxiv.org/abs/2505.09603)
- [DemInf (Mutual Information)](https://arxiv.org/abs/2502.08623)
- [Demo-SCORE](https://arxiv.org/abs/2503.03707)
- [Re-Mix](https://arxiv.org/abs/2408.14037)
- [Modality Selection via CMA](https://arxiv.org/abs/2504.14573)
- [Learning When to See and When to Feel](https://arxiv.org/abs/2604.01414)
- [ADM-DP](https://arxiv.org/abs/2602.21622)
- [Any2Policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/f13159aecc416659a3c6cef0aecd0d94-Paper-Conference.pdf)
- [Green-VLA](https://arxiv.org/abs/2602.00919)
- [Seed2Scale](https://arxiv.org/abs/2603.08260)
- [Robometer](https://arxiv.org/abs/2603.02115)
- [SARM](https://arxiv.org/abs/2509.25358)
- [RoboReward](https://techxplore.com/news/2026-01-roboreward-dataset-automate-robotic.html)
- [Consistency Matters](https://arxiv.org/abs/2412.14309)
- [Quantifying Demo Quality](https://arxiv.org/abs/2203.13843)
- [Multimodal Fusion VLA Survey](https://www.sciencedirect.com/science/article/pii/S1566253525011248)
- [ICLR 2026 VLA Trends](https://mbreuss.github.io/blog_post_iclr_26_vla.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424febdf-5c07-4985-a82f-b19ae8c2db8f",
  "isSidechain": true,
  "agentId": "a99fa48a1385f86f4",
  "requestId": "req_011Cb18oLJhMWeEhdH9NxD3k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "939e89ab-688d-4daf-ab65-5ca026207047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1142177a-63e5-466d-b204-030ae6acf004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuaZXk5WjGQZzMmSaqATvk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3683,
      "cache_read_input_tokens": 33822,
      "output_tokens": 4017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4017,
          "cache_read_input_tokens": 33822,
          "cache_creation_input_tokens": 3683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3683,
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
