# Research conversation: I'm reviewing a paper proposal about "open-vocabulary affordance reasoning for VLA (Vision-Language-Action) models." I n

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a99e4c4020376a997.jsonl`
- **Structured JSON:** [`dd493851ce295c41294f.json`](../../sessions/dd/dd493851ce295c41294f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-18T19:39:00.475Z_

I'm reviewing a paper proposal about "open-vocabulary affordance reasoning for VLA (Vision-Language-Action) models." I need to find any competing or highly related work that may have been missed. Please search for:

1. "open vocabulary affordance VLA 2025 2026" on web search
2. "affordance reasoning robot manipulation end-to-end 2026" 
3. "chain of thought VLA affordance robustness 2026"
4. "affordance grounding vision language action 2025 2026"
5. "intermediate reasoning tokens robot manipulation 2026"
6. Search specifically for any work comparing different types of chain-of-thought reasoning for robot manipulation
7. Search for "LIBERO-Plus robustness VLA" to find what methods have been evaluated on this benchmark
8. Search for "reasoning content vs reasoning optimization VLA" or similar

For each search, report the most relevant papers found, especially any from 2025-2026 that combine affordance reasoning with VLA models in an end-to-end manner. I'm particularly interested in work that:
- Compares different types of intermediate reasoning for robot manipulation
- Uses affordance-structured reasoning in autoregressive VLAs
- Evaluates VLA robustness under distribution shift

Use WebSearch for all queries. Report titles, arXiv IDs, and brief descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "9bdc16f6-aced-4299-b800-dcee071be537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T19:39:00.477Z_

```json
{
  "parentUuid": "9bdc16f6-aced-4299-b800-dcee071be537",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
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
  "uuid": "82703f51-c8b0-4402-8a58-399bea96eaf3",
  "timestamp": "2026-05-18T19:39:00.477Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T19:39:03.331Z_



I'll start by loading the WebSearch tool schema, then execute all the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82703f51-c8b0-4402-8a58-399bea96eaf3",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnBjefZUpCWr4gshNW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c652857-49bf-45e8-a844-63d634b8aada",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS5m3n67b2g3k6xdx73t7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 854,
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

_source line 4 · 2026-05-18T19:39:03.579Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MQZQ7Mkh7Mjw5Q4zNdRZuJ`</summary>

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
  "parentUuid": "8c652857-49bf-45e8-a844-63d634b8aada",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnBjefZUpCWr4gshNW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d20d64b-2c1b-41f1-b83a-e4d8c3c6f2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS5m3n67b2g3k6xdx73t7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 854,
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

_source line 5 · 2026-05-18T19:39:03.583Z_

<details><summary>↩ Tool result · `toolu_01MQZQ7Mkh7Mjw5Q4zNdRZuJ`</summary>

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
  "parentUuid": "3d20d64b-2c1b-41f1-b83a-e4d8c3c6f2ae",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "3b1425e3-5529-4b50-92c9-fbe7eb749689",
  "sourceToolAssistantUUID": "3d20d64b-2c1b-41f1-b83a-e4d8c3c6f2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T19:39:06.267Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b1425e3-5529-4b50-92c9-fbe7eb749689",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7ee2685-4f33-4c5e-a95c-008429fb82b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 7 · 2026-05-18T19:39:06.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JjfX2u8JdMcTW8nw24joYB`</summary>

```json
{
  "query": "open vocabulary affordance VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7ee2685-4f33-4c5e-a95c-008429fb82b8",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc34c3fb-c6a6-4439-b498-d4004c2136c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 8 · 2026-05-18T19:39:07.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017MTFmLN8131YxK8oe3eeqh`</summary>

```json
{
  "query": "affordance reasoning robot manipulation end-to-end 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc34c3fb-c6a6-4439-b498-d4004c2136c9",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94a90ded-4b6d-4882-9c8d-15ee0f0cecca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 9 · 2026-05-18T19:39:07.758Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HM5Fs2F4mxrEKgSYDY1mX`</summary>

```json
{
  "query": "chain of thought VLA affordance robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a90ded-4b6d-4882-9c8d-15ee0f0cecca",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf4dd73-ad23-497c-9115-26a8d4e4437c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 10 · 2026-05-18T19:39:07.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JoPrpeFexzDdUo7NR8mxW7`</summary>

```json
{
  "query": "affordance grounding vision language action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf4dd73-ad23-497c-9115-26a8d4e4437c",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eceeb38-eb6b-4082-8b70-9228de168549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 11 · 2026-05-18T19:39:08.229Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K3kBC5MMWnnhnxBjuc9YNV`</summary>

```json
{
  "query": "intermediate reasoning tokens robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eceeb38-eb6b-4082-8b70-9228de168549",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e39df5d-4f05-46e9-988b-2ec80ef005bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 12 · 2026-05-18T19:39:08.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SdoZq4wi3oWB69U78HibZP`</summary>

```json
{
  "query": "comparing chain-of-thought reasoning types robot manipulation VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e39df5d-4f05-46e9-988b-2ec80ef005bd",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4e40629-b07b-4d97-98dc-78b0d367c773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 13 · 2026-05-18T19:39:09.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018haRU54JTJqNP76UmUAym3`</summary>

```json
{
  "query": "LIBERO-Plus robustness VLA benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4e40629-b07b-4d97-98dc-78b0d367c773",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd52d152-ae6f-4029-bff5-1f97932c8b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 14 · 2026-05-18T19:39:09.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q7ssnPtY9RH3LgV2HMajfc`</summary>

```json
{
  "query": "reasoning content vs reasoning optimization VLA robot policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd52d152-ae6f-4029-bff5-1f97932c8b1d",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbnSRCNTVQBCcAG4Ncz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "872521f7-b772-416b-9fbe-0cc9c6cbf890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k3LnNKVLSsQ1LjRewMM6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 15 · 2026-05-18T19:39:13.325Z_

<details><summary>↩ Tool result · `toolu_01JoPrpeFexzDdUo7NR8mxW7`</summary>

```text
Web search results for query: "affordance grounding vision language action 2025 2026"

Links: [{"title":"[2504.04744] Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions","url":"https://arxiv.org/abs/2504.04744"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://www.emergentmind.com/papers/2401.06341"},{"title":"[2401.06341] AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/abs/2401.06341"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/pdf/2401.06341"},{"title":"[Quick Review] Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions","url":"https://liner.com/review/grounding-3d-object-affordance-with-language-instructions-visual-observations-and"},{"title":"AffordanceLLM: Grounding affordance from vision language models - Amazon Science","url":"https://www.amazon.science/publications/affordancellm-grounding-affordance-from-vision-language-models"}]

Based on the search results, here's what I found on affordance grounding in vision-language systems for 2025-2026:

## Recent Research on Affordance Grounding

Affordance grounding refers to the task of finding the area of an object with which one can interact. It requires comprehensive understanding of a scene including detection, localization, recognition of objects with their parts, geo-spatial configuration, 3D shapes and physics, and object functionality and potential interaction.

### Key 2025 Development

A notable CVPR 2025 paper introduces a novel task for grounding 3D object affordance using language instructions and visual observations. Researchers proposed LMAffordance3D, the first multi-modal, language-guided 3D affordance grounding network, which applies a vision-language model to fuse 2D and 3D spatial features with semantic features.

### Earlier Foundation Work

Recent work has attempted to improve the generalization capability of affordance grounding by leveraging the rich world, abstract, and human-object-interaction knowledge from pretrained large-scale vision language models. These models can ground affordance for objects from random Internet images, even if both objects and actions are unseen during training.

The field is advancing toward more generalizable, language-guided approaches that integrate multiple modalities to better understand how objects can be interacted with in real-world scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eceeb38-eb6b-4082-8b70-9228de168549",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "102c5865-6e1d-46b8-99ba-907fa08ac704",
  "sourceToolAssistantUUID": "5eceeb38-eb6b-4082-8b70-9228de168549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:39:15.482Z_

<details><summary>↩ Tool result · `toolu_018haRU54JTJqNP76UmUAym3`</summary>

```text
Web search results for query: "LIBERO-Plus robustness VLA benchmark"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, here's what I found about LIBERO-Plus and its robustness evaluation of VLA models:

## Overview

LIBERO-Plus is a diagnostic benchmark for vision-language-action (VLA) models. It comprehensively evaluates VLA models under controlled perturbations across multiple dimensions.

## Benchmark Scale

LIBERO-Plus comprises 10,030 tasks across seven perturbation factors and 21 underlying components.

## Key Findings on VLA Robustness

The benchmark reveals critical vulnerabilities in current VLA models:

- Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations
- Most contemporary VLA models remain brittle, showing particular vulnerability to camera and robot state changes, and almost all models ignore language instructions

## Perturbation Dimensions

The systematic vulnerability analysis introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Purpose

LIBERO-Plus is designed to establish a rigorous leaderboard for evaluating generalization capabilities and enable meaningful cross-model comparisons with a standardized leaderboard for tracking progress in VLA robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd52d152-ae6f-4029-bff5-1f97932c8b1d",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "a2962c66-841f-43a0-8ec9-ce1383d2de19",
  "sourceToolAssistantUUID": "bd52d152-ae6f-4029-bff5-1f97932c8b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T19:39:16.003Z_

<details><summary>↩ Tool result · `toolu_01JjfX2u8JdMcTW8nw24joYB`</summary>

```text
Web search results for query: "open vocabulary affordance VLA 2025 2026"

Links: [{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Open-Vocabulary Affordance Detection in 3D Point Clouds","url":"https://arxiv.org/pdf/2303.02401"},{"title":"Open-Vocabulary 3D Affordance Understanding via ...","url":"https://eprints.gla.ac.uk/360521/2/360521.pdf"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/pdf/2404.11000"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation","url":"https://arxiv.org/pdf/2511.06240"}]

Based on the search results, here's what I found regarding open vocabulary affordance and VLA research in 2025-2026:

## Recent Research Developments

Recent work includes "3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds" (2025), which demonstrates the intersection of these research areas.

## Vision-Language-Action Models and Affordance

Vision-Language-Action (VLA) models are robot foundation models that have garnered significant attention for their ability to enhance robot policy learning. Recent work transforms affordances into visual and textual formats, introducing vision-language co-injection modules that integrate this knowledge into policy networks.

Recent models like CoA-VLA outperform state-of-the-art robot foundation models and exhibit strong generalization capabilities, including recognizing unseen object poses and avoiding obstacles in novel environments.

## Open-Vocabulary Affordance Methods

Open-vocabulary affordance detection enables zero-shot learning with the ability to process new open-language texts as query affordances. Current work addresses affordance localization in the open-vocabulary setting where object categories and affordances are not fixed after training.

## Commercial Timeline

Expert consensus suggests commercial deployment 2025-2026, mass market adoption 2027-2030, and human-level capabilities by early 2030s.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc34c3fb-c6a6-4439-b498-d4004c2136c9",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "9739be23-d370-4294-bf5c-f2fc266c1a69",
  "sourceToolAssistantUUID": "bc34c3fb-c6a6-4439-b498-d4004c2136c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T19:39:16.070Z_

<details><summary>↩ Tool result · `toolu_01K3kBC5MMWnnhnxBjuc9YNV`</summary>

```text
Web search results for query: "intermediate reasoning tokens robot manipulation 2026"

Links: [{"title":"[2505.08548] From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation","url":"https://arxiv.org/abs/2505.08548"},{"title":"From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=yngvAamNQi"},{"title":"[2602.09973] RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation","url":"https://arxiv.org/abs/2602.09973"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/html/2601.01618v1"},{"title":"Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/pdf/2601.01618"},{"title":"From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation","url":"https://arxiv.org/pdf/2505.08548"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"}]

Based on the search results, here are the key findings related to intermediate reasoning tokens and robot manipulation in 2026:

## Recent Research on Reasoning and Robot Manipulation

A novel approach called FSD (From Seeing to Doing) generates intermediate representations through spatial relationship reasoning, providing fine-grained guidance for robotic manipulation. FSD achieves 40.6% success rate in SimplerEnv and 72% success rate across 8 real-world tasks, outperforming the strongest baseline by 30%.

## Intermediate Representation Frameworks

RoboInter comprises a large-scale dataset containing over 230k episodes across 571 diverse scenes, with dense per-frame annotations over more than 10 categories of intermediate representations. RoboInter-VQA introduces 9 spatial and 20 temporal embodied VQA categories to systematically benchmark and enhance the embodied reasoning capabilities of VLMs.

## Challenges with Text-Based Reasoning

Text-based chain-of-thought often requires extensive textual reasoning during inference, with long reasoning traces dramatically increasing token length, resulting in excessive KV-cache usage, high memory consumption, and increased latency.

## Visual Intermediate Representations

Action-Sketcher introduces Visual Sketch as an intermediate representation and operates in a See → Think → Sketch → Act workflow coordinated by adaptive token-gated strategy for reasoning triggers, sketch revision, and action issuance.

These developments show a 2026 trend toward using intermediate representations—both visual and spatial—rather than relying solely on token-based textual reasoning for improved robotic manipulation performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e39df5d-4f05-46e9-988b-2ec80ef005bd",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "844bc447-b359-46cc-917f-605bd3cafcb1",
  "sourceToolAssistantUUID": "0e39df5d-4f05-46e9-988b-2ec80ef005bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T19:39:17.811Z_

<details><summary>↩ Tool result · `toolu_01SdoZq4wi3oWB69U78HibZP`</summary>

```text
Web search results for query: "comparing chain-of-thought reasoning types robot manipulation VLA"

Links: [{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/pdf/2603.12717"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/html/2503.22020v1"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2503.22020v1"},{"title":"GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions","url":"https://arxiv.org/html/2508.07650v1"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action   Models","url":"https://arxiv.org/pdf/2503.22020"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"}]

I found several relevant research papers on chain-of-thought reasoning in Vision-Language-Action (VLA) models for robot manipulation. Here's what the search revealed:

## Key Research Areas

**Visual Chain-of-Thought Approaches:**
CoT-VLA incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks.

**Spatial-Aware Reasoning:**
GraphCoT-VLA designs a structured Chain-of-Thought reasoning module that integrates high-level task understanding and planning, failed task feedback, and low-level imaginative reasoning about future object positions and robot actions, along with a 3D Pose-Object graph that captures spatial configuration of robot joints and topological relationships between objects in 3D space.

**Vulnerabilities in Chain-of-Thought VLAs:**
Recent Vision-Language-Action (VLA) models increasingly adopt chain-of-thought (CoT) reasoning, generating a natural-language plan before decoding motor commands. However, substituting object names in the reasoning trace significantly reduces success rates, while sentence reordering and other corruptions have negligible impact, indicating that the action decoder depends on entity-reference integrity rather than reasoning quality or sequential structure.

These papers represent different approaches to comparing and analyzing chain-of-thought reasoning types in VLA robotic manipulation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4e40629-b07b-4d97-98dc-78b0d367c773",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "3bd580a7-c663-4dbd-82e9-5286c03246c0",
  "sourceToolAssistantUUID": "d4e40629-b07b-4d97-98dc-78b0d367c773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T19:39:18.600Z_

<details><summary>↩ Tool result · `toolu_015HM5Fs2F4mxrEKgSYDY1mX`</summary>

```text
Web search results for query: "chain of thought VLA affordance robustness 2026"

Links: [{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/402148228_Altered_Thoughts_Altered_Actions_Probing_Chain-of-Thought_Vulnerabilities_in_VLA_Robotic_Manipulation"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗","url":"https://arxiv.org/pdf/2510.01623"},{"title":"(PDF) Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://www.researchgate.net/publication/387539786_Improving_Vision-Language-Action_Models_via_Chain-of-Affordance"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"[Literature Review] Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://www.themoonlight.io/en/review/improving-vision-language-action-models-via-chain-of-affordance"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://chain-of-affordance.github.io/"}]

Based on the search results, here's what I found about chain of thought, VLA (Vision-Language-Action) models, affordance, and robustness in 2026:

## Chain-of-Thought in VLA Models

Chain-of-Affordance (CoA-VLA) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion. VLA-R1 develops VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations, simultaneously emphasizing data-level Chain-of-Thought supervision and optimization-level reward alignment.

## Affordance and Robustness

VLA-R1 designs an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. This enables the model to not only provide answers but also explain them, making it robust to challenges like color similarity, repeated instances, and multiple receptacle choices during reasoning.

## Key Recent Work

CoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments. The research also addresses vulnerabilities in chain-of-thought reasoning in VLA systems, with works examining attacks and robustness in this domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cf4dd73-ad23-497c-9115-26a8d4e4437c",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "9e3fbf25-132a-4904-bdf8-2a03f8a26705",
  "sourceToolAssistantUUID": "4cf4dd73-ad23-497c-9115-26a8d4e4437c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T19:39:18.923Z_

<details><summary>↩ Tool result · `toolu_017MTFmLN8131YxK8oe3eeqh`</summary>

```text
Web search results for query: "affordance reasoning robot manipulation end-to-end 2026"

Links: [{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"Afford-X: Generalizable and Slim Affordance Reasoning for Task-oriented Manipulation","url":"https://arxiv.org/pdf/2503.03556"},{"title":"[2209.12941] End-to-End Affordance Learning for Robotic Manipulation","url":"https://arxiv.org/abs/2209.12941"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"End-to-End Affordance Learning for Robotic Manipulation","url":"https://arxiv.org/pdf/2209.12941"}]

Based on the web search results, here are the relevant findings on affordance reasoning for robot manipulation:

## Recent Work in Affordance-Based Robot Manipulation

Afford-X is an end-to-end trainable affordance reasoning model that incorporates Verb Attention and Bi-Fusion modules to improve multi-modal understanding. The model was developed using LVIS-Aff, a large-scale dataset comprising 1,496 tasks and 119k images, designed to enhance the generalizability of affordance reasoning from perception.

In terms of performance, this model achieves up to a 12.1% performance improvement over the best-reported results from non-LLM methods, and it maintains a compact 187M parameter size and infers nearly 50 times faster than the GPT-4V API.

## Broader Context

Recent approaches introduce some form of prior derived from human knowledge as an intermediate stage, including affordances, and unify affordance models with low-level robot policies. This helps to alleviate the sample inefficiency problem of end-to-end learning from scratch.

The results demonstrate that efficient, generalizable affordance reasoning models can be deployed on local devices for task-oriented manipulations and have broad implications for advancing robotics in real-world applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94a90ded-4b6d-4882-9c8d-15ee0f0cecca",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "bd6e332f-759c-429d-809f-de53f6d218fc",
  "sourceToolAssistantUUID": "94a90ded-4b6d-4882-9c8d-15ee0f0cecca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T19:39:21.029Z_

<details><summary>↩ Tool result · `toolu_01Q7ssnPtY9RH3LgV2HMajfc`</summary>

```text
Web search results for query: "reasoning content vs reasoning optimization VLA robot policy"

Links: [{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗","url":"https://arxiv.org/pdf/2510.01623"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/pdf/2505.08243"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2407.08693"},{"title":"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/pdf/2412.03293"},{"title":"Incentivizing Multimodal Reasoning in Large Models for Direct Robot Manipulation","url":"https://arxiv.org/html/2505.12744v1"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15669v2"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"}]

Based on the search results, here's what I found regarding reasoning content vs reasoning optimization in VLA robot policies:

## Reasoning Content (Generating Explanations)

Embodied Chain-of-Thought Reasoning (ECoT) trains VLAs to perform multiple steps of reasoning about plans, sub-tasks, motions, and visually grounded features like object bounding boxes and end effector positions, before predicting the robot action. This approach generates explicit reasoning traces as part of the policy.

Learning to generate reasonings leads to better VLA representations, while attending to the reasonings aids in leveraging these features for improved action prediction.

## Reasoning Optimization (Optimizing for Better Policies)

Rather than just generating reasoning content, some approaches focus on optimizing reasoning to improve policy performance. Reinforcement Learning with Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) systematically optimizes both reasoning and execution, with verifiable rewards for region alignment, trajectory consistency, and output formatting.

Group Relative Policy Optimization (GRPO) applied to supervised fine-tuned models improves spatial and mathematical reasoning abilities, and not only improves task success rates but also encourages emergent reasoning and reflection behaviors.

## Trade-off: Inference Speed vs. Reasoning Quality

An important distinction exists between approaches that generate reasoning at test time versus those that only use reasoning during training. Lightweight alternatives train policies with embodied reasoning data without producing reasonings at test time, boosting performance over non-reasoning VLAs while maintaining fast inference speeds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "872521f7-b772-416b-9fbe-0cc9c6cbf890",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "af522a43-6a38-4986-991c-93dcfe736612",
  "sourceToolAssistantUUID": "872521f7-b772-416b-9fbe-0cc9c6cbf890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T19:39:23.825Z_

Let me run a few more targeted searches to capture additional papers that appeared in the results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af522a43-6a38-4986-991c-93dcfe736612",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca934c71-217d-4862-b0f6-12989c56683b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6377,
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

_source line 24 · 2026-05-18T19:39:24.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0172eVsqU7pKnJyQH4LdwoSK`</summary>

```json
{
  "query": "CoA-VLA chain-of-affordance vision language action model arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca934c71-217d-4862-b0f6-12989c56683b",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2004fa19-4209-4806-8af9-1199117c1650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6377,
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

_source line 25 · 2026-05-18T19:39:25.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011GjGQetDSBw7i7qgmfohLF`</summary>

```json
{
  "query": "VLA-R1 enhancing reasoning vision language action GRPO arXiv 2510.01623"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2004fa19-4209-4806-8af9-1199117c1650",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9562e2e1-740b-4ac6-a00b-e788be359173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6377,
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

_source line 26 · 2026-05-18T19:39:25.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RbTzcj4Lv3pujvuwX8Vmn5`</summary>

```json
{
  "query": "Latent Reasoning VLA latent thinking prediction 2602.01166"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9562e2e1-740b-4ac6-a00b-e788be359173",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fa9deed-e090-45b5-8e25-a8912c4c11fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6377,
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

_source line 27 · 2026-05-18T19:39:26.243Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vb1W5VSgEDFPPRM4eukvLD`</summary>

```json
{
  "query": "DeepThinkVLA reasoning capability vision language action 2511.15669"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fa9deed-e090-45b5-8e25-a8912c4c11fd",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f9c961d-fe2e-4dfc-9347-b50322755a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6377,
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

_source line 28 · 2026-05-18T19:39:27.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012zb7XG98smwrAGXLfsGT41`</summary>

```json
{
  "query": "Diffusion-VLA self-generated reasoning robot foundation model 2412.03293"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f9c961d-fe2e-4dfc-9347-b50322755a8e",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "865cb3e6-40fc-4d61-88da-43baf04da297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6377,
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

_source line 29 · 2026-05-18T19:39:27.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FsDHMkrJYmEpcQSePPB3pg`</summary>

```json
{
  "query": "\"Altered Thoughts Altered Actions\" chain-of-thought vulnerabilities VLA 2603.12717"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "865cb3e6-40fc-4d61-88da-43baf04da297",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbohemAQCfLk1NQDZao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13f33822-4bfb-40db-abc0-a4ccb6b4f951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufw5yN4fu7erkFXHn46Z8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6377,
      "cache_read_input_tokens": 10488,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 10488,
          "cache_creation_input_tokens": 6377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6377,
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

_source line 30 · 2026-05-18T19:39:30.387Z_

<details><summary>↩ Tool result · `toolu_01RbTzcj4Lv3pujvuwX8Vmn5`</summary>

```text
Web search results for query: "Latent Reasoning VLA latent thinking prediction 2602.01166"

Links: [{"title":"[2602.01166] Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.01166"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for","url":"https://www.arxiv.org/pdf/2602.01166"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2602.01166"},{"title":"[2601.05611] LatentVLA: Efficient Vision-Language Models for Autonomous Driving via Latent Action Prediction","url":"https://arxiv.org/abs/2601.05611"}]

Based on the search results, here's what I found about the paper 2602.01166:

## Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models

The paper proposes Latent Reasoning VLA (LaRA-VLA), a unified VLA framework that internalizes multi-modal chain-of-thought (CoT) reasoning into continuous latent representations for embodied action.

**Key Problem:** Vision-Language-Action (VLA) models benefit from chain-of-thought reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception and control.

**Main Approach:** LaRA-VLA performs unified reasoning and prediction in latent space, eliminating explicit CoT generation at inference time and enabling efficient, action-oriented control. To realize latent embodied reasoning, the authors introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and finally adapts latent reasoning dynamics to condition action generation.

**Results:** Experimental results show that LaRA-VLA consistently outperforms state-of-the-art VLA methods while reducing inference latency by up to 90% compared to explicit CoT-based approaches.

The paper was submitted on February 1, 2026, and features authors including Shuanghao Bai, Jing Lyu, and others from multiple institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fa9deed-e090-45b5-8e25-a8912c4c11fd",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "163e5303-e2bf-47b7-b9a9-6a600ec029df",
  "sourceToolAssistantUUID": "3fa9deed-e090-45b5-8e25-a8912c4c11fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T19:39:31.281Z_

<details><summary>↩ Tool result · `toolu_0172eVsqU7pKnJyQH4LdwoSK`</summary>

```text
Web search results for query: "CoA-VLA chain-of-affordance vision language action model arXiv"

Links: [{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241220451L/abstract"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/html/2503.22020v1"}]

Based on the search results, here's what I found about CoA-VLA:

CoA-VLA (Chain-of-Affordance) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion.

**Key Components:**

The model prompts the system to consider four types of affordances before taking action: (1) object affordance — what object to manipulate and where it is; (2) grasp affordance — the specific object part to grasp; (3) spatial affordance — the optimal space to place the object; and (4) movement affordance — the collision-free path for movement.

Each affordance is transformed into two prompting formats: visual affordance and textual affordance, and a novel vision-language co-injection module integrates this knowledge into the policy network.

**Performance:**

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks. The model exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.

The paper was published on arXiv as paper 2412.20451 and is scheduled for presentation at ICCV 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2004fa19-4209-4806-8af9-1199117c1650",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "7fb246f0-b199-4b8e-9336-05240a58eb4e",
  "sourceToolAssistantUUID": "2004fa19-4209-4806-8af9-1199117c1650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T19:39:31.856Z_

<details><summary>↩ Tool result · `toolu_011GjGQetDSBw7i7qgmfohLF`</summary>

```text
Web search results for query: "VLA-R1 enhancing reasoning vision language action GRPO arXiv 2510.01623"

Links: [{"title":"[2510.01623] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.01623"},{"title":"Paper page - VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.01623"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://gigaai-research.github.io/VLA-R1/"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.01623v1"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗","url":"https://arxiv.org/pdf/2510.01623"},{"title":"GitHub - GigaAI-research/VLA-R1","url":"https://github.com/GigaAI-research/VLA-R1"},{"title":"dblp: VLA-R1: Enhancing Reasoning in Vision-Language-Action Models.","url":"https://dblp.org/rec/journals/corr/abs-2510-01623.html"}]

I found the paper you're looking for! Here's what the search returned:

## VLA-R1: Enhancing Reasoning in Vision-Language-Action Models

Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations.

**Key Innovation:**

VLA-R1 integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution.

**Technical Approach:**

The model uses an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Additionally, the researchers developed VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations.

**Authors:** Angen Ye, Zeyu Zhang, Boyuan Wang, Xiaofeng Wang, Dapeng Zhang, Zheng Zhu

The paper was published on arXiv on October 2, 2025, and you can access it at https://arxiv.org/abs/2510.01623.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9562e2e1-740b-4ac6-a00b-e788be359173",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "8758a278-5584-430d-a9e3-c2f54c12b06f",
  "sourceToolAssistantUUID": "9562e2e1-740b-4ac6-a00b-e788be359173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T19:39:32.024Z_

<details><summary>↩ Tool result · `toolu_01FsDHMkrJYmEpcQSePPB3pg`</summary>

```text
Web search results for query: ""Altered Thoughts Altered Actions" chain-of-thought vulnerabilities VLA 2603.12717"

Links: [{"title":"[2603.12717] Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/abs/2603.12717"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/html/2603.12717"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/402148228_Altered_Thoughts_Altered_Actions_Probing_Chain-of-Thought_Vulnerabilities_in_VLA_Robotic_Manipulation"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.12717v1"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/pdf/2603.12717"}]

Based on the search results, here's information about this paper:

**Paper Overview:**
"Altered Thoughts, Altered Actions" examines Vision-Language-Action (VLA) models that increasingly adopt chain-of-thought (CoT) reasoning, generating a natural-language plan before decoding motor commands. The internal text channel between the reasoning module and the action decoder had previously received no adversarial scrutiny.

**Research Methodology:**
The researchers designed a taxonomy of seven text corruptions organized into three attacker tiers (blind noise, mechanical-semantic, and LLM-adaptive) and applied them to a state-of-the-art reasoning VLA across 40 LIBERO tabletop manipulation tasks.

**Key Findings:**
The results reveal a striking asymmetry: substituting object names in the reasoning trace reduces overall success rate by 8.3 percentage points (pp) — reaching -19.3 pp on goal-conditioned tasks and -45 pp on individual tasks — whereas sentence reordering, spatial-direction reversal, token noise, and even a 70B-parameter LLM crafting plausible-but-wrong plans all have negligible impact (within ±4 pp). This asymmetry indicates that the action decoder depends on entity-reference integrity rather than reasoning quality or sequential structure.

The paper was submitted to arXiv on March 13, 2026, with authors Tuan Duong Trinh, Naveed Akhtar, and Basim Azam.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13f33822-4bfb-40db-abc0-a4ccb6b4f951",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "bf9846c6-0427-49fd-99da-ba02d37e506d",
  "sourceToolAssistantUUID": "13f33822-4bfb-40db-abc0-a4ccb6b4f951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T19:39:32.099Z_

<details><summary>↩ Tool result · `toolu_01Vb1W5VSgEDFPPRM4eukvLD`</summary>

```text
Web search results for query: "DeepThinkVLA reasoning capability vision language action 2511.15669"

Links: [{"title":"[2511.15669] DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.15669"},{"title":"Paper page - DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://huggingface.co/papers/2511.15669"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/397780193_DeepThinkVLA_Enhancing_Reasoning_Capability_of_Vision-Language-Action_Models"},{"title":"GitHub - wadeKeith/DeepThinkVLA: DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://github.com/wadeKeith/DeepThinkVLA"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.15669v1"},{"title":"DEEPTHINKVLA: ENHANCING REASONING CAPA- BILITY OF VISION-LANGUAGE-ACTION MODELS","url":"https://arxiv.org/pdf/2511.15669"},{"title":"GitHub - OpenBMB/DeepThinkVLA: DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models · GitHub","url":"https://github.com/OpenBMB/DeepThinkVLA"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15669"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=kCrE9uvxlo"}]

I found detailed information about DeepThinkVLA. Here's what the research presents:

## Overview

DeepThinkVLA enables Vision-Language-Action (VLA) models to "think before acting" via Chain-of-Thought (CoT) as a promising path to overcoming the data-hungry nature of end-to-end robot policies.

## The Core Problem

Existing models use a single autoregressive decoder for both sequential CoT reasoning and high-dimensional, parallelizable robot actions, and this architectural mismatch degrades motor control and fails to forge a strong causal link between thought and action.

## The Solution

The architecture uses a hybrid-attention decoder that generates sequential CoT with causal attention and then switches to bidirectional attention for fast, parallel decoding of action vectors.

The design is complemented by a two-stage training pipeline: first using Supervised Fine-Tuning (SFT) to teach the model foundational reasoning, then applying Reinforcement Learning (RL) with task-success rewards to causally align the full reasoning-action sequence with desired outcomes.

## Implementation Details

The model is a 2.9B parameter hybrid decoder that writes a reasoning trace before emitting action chunks. In inference, DeepThinkVLA preserves accuracy (96.5% average success rate) while running at 0.175x the latency of autoregressive baselines.

The paper (arXiv:2511.15669) was submitted on October 31, 2025, and code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f9c961d-fe2e-4dfc-9347-b50322755a8e",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "f81f65c7-ceff-4cd3-8b9e-de4e681f0659",
  "sourceToolAssistantUUID": "4f9c961d-fe2e-4dfc-9347-b50322755a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T19:39:33.661Z_

<details><summary>↩ Tool result · `toolu_012zb7XG98smwrAGXLfsGT41`</summary>

```text
Web search results for query: "Diffusion-VLA self-generated reasoning robot foundation model 2412.03293"

Links: [{"title":"[2412.03293] Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/abs/2412.03293"},{"title":"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241203293W/abstract"},{"title":"[2412.03293v3] Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/abs/2412.03293v3"},{"title":"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/pdf/2412.03293"},{"title":"[2412.03293v2] Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression","url":"https://arxiv.org/abs/2412.03293v2"},{"title":"(PDF) Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression","url":"https://www.researchgate.net/publication/386454973_Diffusion-VLA_Scaling_Robot_Foundation_Models_via_Unified_Diffusion_and_Autoregression"},{"title":"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/html/2412.03293"}]

Based on the search results, I found detailed information about this research paper:

## Diffusion-VLA Paper Overview

Diffusion-VLA is a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy.

### Key Components

The framework has several key features:

1. **Reasoning Capability**: A next-token prediction objective enables the model to reason effectively over the user's query in the context of current observations.

2. **Action Generation**: A diffusion model is attached to generate robust action outputs.

3. **Reasoning Injection Module**: A novel reasoning injection module integrates reasoning phrases directly into the policy learning process.

### Performance and Results

Extensive experiments were conducted using multiple real robots, including a challenging factory sorting task where Diffusion-VLA successfully categorizes objects, including those not seen during training. Additionally, the model achieved 63.7% accuracy on 102 previously unseen objects in a zero-shot bin-picking task.

The smallest Diffusion-VLA variant (2B parameters) runs at 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for complex tasks.

### Publication Status

The paper was accepted by ICML 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "865cb3e6-40fc-4d61-88da-43baf04da297",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "3be1f589-4fcc-44bb-8c72-c19376372b57",
  "sourceToolAssistantUUID": "865cb3e6-40fc-4d61-88da-43baf04da297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T19:39:36.675Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LP5oyVZV8hiNeux4ssoW1m`</summary>

```json
{
  "query": "RT-Affordance reasoning robotic manipulation affordances arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be1f589-4fcc-44bb-8c72-c19376372b57",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbpdcT86EfSV2a8Moz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30a290c1-4c4a-4ec1-8c22-b72f92d8943b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdQAkwMfqgwsCZSUpPfxnm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 16865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 37 · 2026-05-18T19:39:37.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XAY5t4j6rpQoVbvmtUtnkU`</summary>

```json
{
  "query": "RoboInter holistic intermediate representation robotic manipulation 2602.09973"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a290c1-4c4a-4ec1-8c22-b72f92d8943b",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbpdcT86EfSV2a8Moz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4cc4862-c22e-4f48-9781-ffb4d602753e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdQAkwMfqgwsCZSUpPfxnm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 16865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 38 · 2026-05-18T19:39:38.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012V96b6ahYD9cG8uEcRYEx2`</summary>

```json
{
  "query": "ECoT embodied chain of thought reasoning VLA OpenVLA training 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4cc4862-c22e-4f48-9781-ffb4d602753e",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbpdcT86EfSV2a8Moz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e290840-4e61-476c-a8f4-3515a7532952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdQAkwMfqgwsCZSUpPfxnm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 16865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 39 · 2026-05-18T19:39:39.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PeJNXdqiLKbbZAyHjodrvY`</summary>

```json
{
  "query": "\"world action models\" vs VLA robustness study 2603.22078"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e290840-4e61-476c-a8f4-3515a7532952",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbpdcT86EfSV2a8Moz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b370745-3c2f-4c23-b0d8-e96fff32b767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdQAkwMfqgwsCZSUpPfxnm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 16865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 40 · 2026-05-18T19:39:43.227Z_

<details><summary>↩ Tool result · `toolu_01XAY5t4j6rpQoVbvmtUtnkU`</summary>

```text
Web search results for query: "RoboInter holistic intermediate representation robotic manipulation 2602.09973"

Links: [{"title":"[2602.09973] RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation","url":"https://arxiv.org/abs/2602.09973"},{"title":"RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation","url":"https://arxiv.org/pdf/2602.09973"},{"title":"GitHub - InternRobotics/RoboInter: [ICLR 2026] RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation · GitHub","url":"https://github.com/InternRobotics/RoboInter"},{"title":"RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation","url":"https://arxiv.org/html/2602.09973v1"},{"title":"InternRobotics/RoboInter-Data · Datasets at Hugging Face","url":"https://huggingface.co/datasets/InternRobotics/RoboInter-Data"},{"title":"RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=PGUC3mmMoi"},{"title":"[Literature Review] RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation","url":"https://www.themoonlight.io/en/review/robointer-a-holistic-intermediate-representation-suite-towards-robotic-manipulation"},{"title":"InternRobotics/RoboInter-VQA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/InternRobotics/RoboInter-VQA"},{"title":"ICLR Poster RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation","url":"https://iclr.cc/virtual/2026/poster/10009698"}]

I found comprehensive information about RoboInter. Here's what the search results show:

## Overview

RoboInter is a Manipulation Suite that provides a unified resource including data, benchmarks, and models of intermediate representations for manipulation.

## Key Components

The suite consists of several main components:

1. **RoboInter-Tool**: A lightweight GUI that enables semi-automatic annotation of diverse representations

2. **RoboInter-Data**: A large-scale dataset containing over 230k episodes across 571 diverse scenes, which provides dense per-frame annotations over more than 10 categories of intermediate representations. Annotations include subtasks, primitive skills, segmentation, gripper/object bounding boxes, placement proposals, affordance boxes, grasp poses, traces, contact points, etc.

3. **RoboInter-VQA**: Introduces 9 spatial and 20 temporal embodied VQA categories to systematically benchmark and enhance the embodied reasoning capabilities of VLMs

4. **RoboInter-VLA**: An integrated plan-then-execute framework, supporting modular and end-to-end VLA variants that bridge high-level planning with low-level execution via intermediate supervision

## Purpose

The project addresses limitations where existing manipulation datasets remain costly to curate, highly embodiment-specific, and insufficient in coverage and diversity, and where recent approaches critically rely on extra intermediate supervision, which is largely absent from existing datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4cc4862-c22e-4f48-9781-ffb4d602753e",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "be3117bb-acf8-4f76-9efe-ae1ce124ecaf",
  "sourceToolAssistantUUID": "b4cc4862-c22e-4f48-9781-ffb4d602753e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T19:39:43.838Z_

<details><summary>↩ Tool result · `toolu_01LP5oyVZV8hiNeux4ssoW1m`</summary>

```text
Web search results for query: "RT-Affordance reasoning robotic manipulation affordances arXiv 2024 2025"

Links: [{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/rt-affordance-affordances-are-versatile-intermediate-representations"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances | OpenReview","url":"https://openreview.net/forum?id=s8VMLXKH1X"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot","url":"https://openreview.net/pdf?id=y4KugwU0qU"}]

Based on the search results, here's information about RT-Affordance:

## RT-Affordance Overview

RT-Affordance is a new approach for teaching robots how to manipulate objects, with the core concept being affordances—the possible actions an object allows. The paper was published on November 6, 2024, by Soroush Nasiriany, Sean Kirmani, Tianli Ding, Laura Smith, Yuke Zhu, Danny Driess, Dorsa Sadigh and 1 more author.

## How It Works

RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. The method works by first learning a neural network model that can predict the affordances of objects in a scene, taking in visual observations and outputting affordance heatmaps for each type of affordance (e.g., graspable, liftable, pushable).

## Key Advantages

Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. The model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories, and can be trained on cheap-to-collect in-domain affordance images.

## Performance

RT-Affordance exceeds the performance of existing methods by over 50%, and affordances are robust to novel settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a290c1-4c4a-4ec1-8c22-b72f92d8943b",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "703847c5-d883-483d-a763-2befd01d53de",
  "sourceToolAssistantUUID": "30a290c1-4c4a-4ec1-8c22-b72f92d8943b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T19:39:44.603Z_

<details><summary>↩ Tool result · `toolu_01PeJNXdqiLKbbZAyHjodrvY`</summary>

```text
Web search results for query: ""world action models" vs VLA robustness study 2603.22078"

Links: [{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69d44b615127ff45a9dee58a"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=s1B_PB2r10k"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://huggingface.co/papers/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://www.wispaper.ai/en/user-blog/world-action-models-generalize-better-than-vlas-20260324/eng"}]

Based on the search results, here's what I found about the study with arXiv identifier 2603.22078:

## Study Overview

The paper is titled "Do World Action Models Generalize Better than VLAs? A Robustness Study" (arXiv:2603.22078), with authors from Huawei Technologies and the University of Toronto.

## Key Research Focus

The central topic is a comparative robustness study between Vision-Language-Action (VLA) models and World Action Models (WAMs), specifically examining generalization capabilities and robustness in robotic manipulation tasks.

## What Are WAMs vs VLAs?

World action models (WAMs) are built upon world models trained on large corpora of video data to predict future states, with their latent representation decoded into robot actions. In contrast, VLAs repurpose large-scale vision-language models for robot action generation, but their performance remains constrained by training data scope and they exhibit limited generalization to unseen scenarios and vulnerability to diverse contextual perturbations.

## Main Results

WAMs achieved strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus. WAMs generally generalize better to visual noise and layout changes due to spatiotemporal priors from video pretraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b370745-3c2f-4c23-b0d8-e96fff32b767",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "a668c959-5c44-4f6d-a172-161d33aa13c1",
  "sourceToolAssistantUUID": "0b370745-3c2f-4c23-b0d8-e96fff32b767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T19:39:45.908Z_

<details><summary>↩ Tool result · `toolu_012V96b6ahYD9cG8uEcRYEx2`</summary>

```text
Web search results for query: "ECoT embodied chain of thought reasoning VLA OpenVLA training 2025"

Links: [{"title":"[2407.08693] Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2407.08693"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://ecot-lite.github.io/"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=S70MgnIA0v"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2407.08693"},{"title":"The power of embedded chain-of-thought reasoning for robotics","url":"https://bdtechtalks.substack.com/p/the-power-of-embedded-chain-of-thought"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://embodied-cot.github.io/"},{"title":"Researchers develop technique to give robots “embodied reasoning” abilities | VentureBeat","url":"https://venturebeat.com/ai/researchers-develop-technique-to-give-robots-embodied-reasoning-abilities"},{"title":"Robotic Control via Embodied Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2407.08693"},{"title":"GitHub - MichalZawalski/embodied-CoT: Embodied Chain of Thought: A robotic policy that reason to solve the task. · GitHub","url":"https://github.com/MichalZawalski/embodied-CoT"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/html/2505.08243v2"}]

Based on the search results, here's what I found about ECoT (Embodied Chain-of-Thought Reasoning) and its application to VLAs:

## ECoT Overview

ECoT trains VLAs to perform multiple steps of reasoning about plans, sub-tasks, motions, and visually grounded features like object bounding boxes and end effector positions, before predicting the robot action.

## Performance with OpenVLA

ECoT increases the absolute success rate of OpenVLA, the current strongest open-source VLA policy, by 28% across challenging generalization tasks, without any additional robot training data. After running over 300 real-world evaluation trials per policy, the embodied chain-of-thought policy yields the best performance, especially on tasks that require spatial understanding and semantic generalization.

## Training Data Generation

Researchers solved the challenge of creating training data by creating an automated pipeline that augments existing robot training datasets with ECoT annotations, using VLMs and frontier models such as Gemini to add scene descriptions and reasoning chains to robotic trajectories.

## Recent Developments (2025)

Recent work from 2025 has focused on efficiency improvements. Robot chain-of-thought reasoning provides an effective method for improving generalization and performance of VLAs, and newer ECoT-Lite approaches retain most of the generalization benefits while avoiding drawbacks like needing specialized robot reasoning data and slow inference speeds. ECoT-Lite achieves state-of-the-art performance on the LIBERO simulation benchmark and outperforms conventional VLAs by 10-19% while speeding up inference from 1-1.2 Hz to 3.5+ Hz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e290840-4e61-476c-a8f4-3515a7532952",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "87de06ee-0f98-442d-aba3-1f0dbaf22d3c",
  "sourceToolAssistantUUID": "9e290840-4e61-476c-a8f4-3515a7532952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T19:39:49.204Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y8ccps6e4V4B3aGejxEPQ1`</summary>

```json
{
  "query": "GraphCoT-VLA 3D spatial aware reasoning ambiguous instructions 2508.07650"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87de06ee-0f98-442d-aba3-1f0dbaf22d3c",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbqY2dPEAdoS5Z8S4zM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a81df54a-3aed-4646-9492-07d3b197cd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrFXPzQoDGEqiC7XmG1uSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 20948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 45 · 2026-05-18T19:39:49.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JA9kwpnHgfEefSJ932jhMd`</summary>

```json
{
  "query": "Action-Sketcher visual sketches long-horizon robotic manipulation 2601.01618"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a81df54a-3aed-4646-9492-07d3b197cd96",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbqY2dPEAdoS5Z8S4zM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "146851e3-be35-4385-9151-fdbdd883e529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrFXPzQoDGEqiC7XmG1uSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 20948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 46 · 2026-05-18T19:39:50.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VNKTwJ3aut5Ww86hsGteYn`</summary>

```json
{
  "query": "affordance VLA end-to-end autoregressive robot policy 2025 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "146851e3-be35-4385-9151-fdbdd883e529",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbqY2dPEAdoS5Z8S4zM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e79eeda7-ee39-4a28-978a-f7d2fa0e73d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrFXPzQoDGEqiC7XmG1uSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 20948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 47 · 2026-05-18T19:39:51.177Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015GSZRaV3er9sE8WrMUJjYA`</summary>

```json
{
  "query": "training strategies efficient embodied reasoning ECoT-Lite 2505.08243"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e79eeda7-ee39-4a28-978a-f7d2fa0e73d1",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbqY2dPEAdoS5Z8S4zM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58ad0a07-b5da-4e73-a20e-9c206b6f1999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrFXPzQoDGEqiC7XmG1uSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 20948,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 239,
          "cache_read_input_tokens": 20948,
          "cache_creation_input_tokens": 3516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3516,
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

_source line 48 · 2026-05-18T19:39:55.547Z_

<details><summary>↩ Tool result · `toolu_01Y8ccps6e4V4B3aGejxEPQ1`</summary>

```text
Web search results for query: "GraphCoT-VLA 3D spatial aware reasoning ambiguous instructions 2508.07650"

Links: [{"title":"[2508.07650] GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions","url":"https://arxiv.org/abs/2508.07650"},{"title":"(PDF) GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions","url":"https://www.researchgate.net/publication/394439488_GraphCoT-VLA_A_3D_Spatial-Aware_Reasoning_Vision-Language-Action_Model_for_Robotic_Manipulation_with_Ambiguous_Instructions"},{"title":"GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions","url":"https://arxiv.org/html/2508.07650v1"},{"title":"GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model","url":"https://arxiv.org/pdf/2508.07650"},{"title":"[PDF] GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/d984e849cfa4b39b6d25100695d24e3eaf0c824c"},{"title":"ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2604.09824"}]

Based on the search results, here's what I found about the paper referenced by arXiv ID 2508.07650:

## GraphCoT-VLA Overview

GraphCoT-VLA is an efficient end-to-end model designed to enhance the ability to interpret ambiguous instructions and improve task planning through a structured Chain-of-Thought reasoning module that integrates high-level task understanding and planning, failed task feedback, and low-level imaginative reasoning about future object positions and robot actions.

## Key Innovations

The model constructs a real-time updatable 3D Pose-Object graph, which captures the spatial configuration of robot joints and the topological relationships between objects in 3D space, enabling the model to better understand and manipulate their interactions.

## Problem It Addresses

Existing VLA models exhibit notable limitations in handling ambiguous language instructions and unknown environmental states, with their perception largely constrained to static two-dimensional observations, lacking the capability to model three-dimensional interactions between the robot and its environment.

## Performance

Experimental results across multiple real-world robotic tasks demonstrate that GraphCoT-VLA significantly outperforms existing methods in terms of task success rate and response speed, exhibiting strong generalization and robustness in open environments and under uncertain instructions.

The paper was published on August 11, 2025 on arXiv by authors including Helong Huang, Min Cen, Kai Tan, Xingyue Quan, Guowei Huang, and Hong Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a81df54a-3aed-4646-9492-07d3b197cd96",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "dd716274-dea6-4515-bbfd-fddb77c6b864",
  "sourceToolAssistantUUID": "a81df54a-3aed-4646-9492-07d3b197cd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T19:39:58.419Z_

<details><summary>↩ Tool result · `toolu_01VNKTwJ3aut5Ww86hsGteYn`</summary>

```text
Web search results for query: "affordance VLA end-to-end autoregressive robot policy 2025 2026 site:arxiv.org"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"Affordance Learning for End-to-End Visuomotor Robot Control","url":"https://arxiv.org/pdf/1903.04053"},{"title":"Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring","url":"https://arxiv.org/html/2603.22899v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/pdf/2601.07060"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"}]

Based on the search results, here are some key papers on affordance, VLA (Vision-Language-Action), end-to-end, and autoregressive robot policy from 2025-2026 on arXiv:

1. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** (December 2024/July 2025)
   - Proposes Chain-of-Affordance (CoA-VLA), a novel perspective on generalizing model reasoning at test-time to facilitate policy learning
   - Leverages visual affordance in robot learning, conceptualizing various actions and interactions with objects that a robot can perform based on visual contexts

2. **Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring** (March 2026)
   - Compares five open-source embodied models including Transporter, RT-1, RVT, Octo-Base, and OpenVLA, spanning diffusion-based policies, transformer-based visuomotor architectures, and large VLA models
   - Discusses challenges with autoregressive VLA models in edge deployment

3. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** (2025)
   - Addresses brittleness of VLAs under distribution shifts, where end-to-end design lacks explicit 3D spatial reasoning

4. **PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation** (2025/2026)
   - Notes that a prominent VLA paradigm formulates action generation as autoregressive prediction over tokenized sequences

These papers represent recent advances in combining affordance reasoning with VLA-based robot policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e79eeda7-ee39-4a28-978a-f7d2fa0e73d1",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "351014d4-4ee3-4294-8a54-539a7a8907d2",
  "sourceToolAssistantUUID": "e79eeda7-ee39-4a28-978a-f7d2fa0e73d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T19:39:58.605Z_

<details><summary>↩ Tool result · `toolu_015GSZRaV3er9sE8WrMUJjYA`</summary>

```text
Web search results for query: "training strategies efficient embodied reasoning ECoT-Lite 2505.08243"

Links: [{"title":"Training Strategies for Efficient Embodied Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.08243v2"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://ecot-lite.github.io/"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/html/2505.08243v1"},{"title":"Embodied-CoT/embodied_features_and_demos_libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Embodied-CoT/embodied_features_and_demos_libero"},{"title":"【DL輪読会】 Training Strategies for Efficient Embodied Reasoning | ドクセル","url":"https://www.docswell.com/s/DeepLearning2023/5EX378-2025-05-28-121316"},{"title":"[Literature Review] Training Strategies for Efficient Embodied Reasoning","url":"https://www.themoonlight.io/en/review/training-strategies-for-efficient-embodied-reasoning"},{"title":"(PDF) Training Strategies for Efficient Embodied Reasoning","url":"https://www.researchgate.net/publication/391706892_Training_Strategies_for_Efficient_Embodied_Reasoning"},{"title":"[2505.08243] Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/abs/2505.08243"},{"title":"dblp: Training Strategies for Efficient Embodied Reasoning.","url":"https://dblp.org/rec/journals/corr/abs-2505-08243.html"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/pdf/2505.08243"}]

I found detailed information about this paper. Here's a summary of the research:

## Paper Overview

This paper on "Training Strategies for Efficient Embodied Reasoning" focuses on robot chain-of-thought reasoning (CoT), wherein a model predicts helpful intermediate representations before choosing actions as an effective method for improving the generalization and performance of robot policies, especially vision-language-action models (VLAs).

## Key Problem and Approach

While such approaches improve performance and generalization, they suffer from limitations like needing specialized robot reasoning data and slow inference speeds, making a more complete characterization of why reasoning helps policy performance critical. The researchers hypothesize several mechanisms by which robot reasoning improves policies: (1) better representation learning, (2) improved learning curricularization, and (3) increased expressivity.

## ECoT-Lite Training Strategies

The paper introduces two approaches for learning representations from reasonings without producing them at test time, called ECoT-Lite. The training recipes include: pre-training or co-training VLA models with embodied reasoning data, providing reasoning data as a "scaffolding" in context during training, training with reasoning dropout to remove reasoning during inference, and introducing non-semantic "thinking tokens" to increase effective model expressivity.

## Results

ECoT-Lite achieves state-of-the-art performance on the LIBERO simulation benchmark and outperforms state-of-the-art conventional VLAs on BridgeData V2 evaluations by 10-19%, while speeding up inference from 1-1.2 Hz for conventional embodied chain-of-thought reasoning approaches to 3.5+ Hz of standard VLAs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58ad0a07-b5da-4e73-a20e-9c206b6f1999",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "7f9249a5-6f8e-4a33-b203-8570910f9434",
  "sourceToolAssistantUUID": "58ad0a07-b5da-4e73-a20e-9c206b6f1999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T19:40:00.955Z_

<details><summary>↩ Tool result · `toolu_01JA9kwpnHgfEefSJ932jhMd`</summary>

```text
Web search results for query: "Action-Sketcher visual sketches long-horizon robotic manipulation 2601.01618"

Links: [{"title":"[2601.01618] Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/abs/2601.01618"},{"title":"Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/html/2601.01618"},{"title":"Action-Sketcher: From Reasoning to Action via Visual Sketches for","url":"https://arxiv.org/pdf/2601.01618"},{"title":"Modeling Long-horizon Tasks as Sequential Interaction Landscapes","url":"https://arxiv.org/pdf/2006.04843"},{"title":"Learning Long-Horizon Robot Manipulation Skills via Privileged Action","url":"https://arxiv.org/pdf/2502.15442"},{"title":"From Watch to Imagine: Steering Long-horizon Manipulation via Human Demonstration and Future Envisionment","url":"https://arxiv.org/pdf/2509.22205"},{"title":"ActionSink: Toward Precise Robot Manipulation with Dynamic Integration of Action Flow","url":"https://arxiv.org/pdf/2508.03218"},{"title":"Toward Accurate Long-Horizon Robotic Manipulation: Language-to-Action with Foundation Models via Scene Graphs","url":"https://arxiv.org/pdf/2510.27558"}]

Based on the search results, here's what I found about the paper:

Long-horizon robotic manipulation is increasingly important for real-world deployment, requiring spatial disambiguation in complex layouts and temporal resilience under dynamic interaction. Existing end-to-end and hierarchical Vision-Language-Action (VLA) policies often rely on text-only cues while keeping plan intent latent, which undermines referential grounding in cluttered or underspecified scenes, impedes effective task decomposition of long-horizon goals with close-loop interaction, and limits causal explanation by obscuring the rationale behind action choices.

To address these limitations, the researchers introduce Visual Sketch, an implausible visual intermediate that renders points, boxes, arrows, and typed relations in the robot's current views to externalize spatial intent, connect language to scene geometry. Building on Visual Sketch, they present Action-Sketcher, a VLA framework that operates in a cyclic See→Think→Sketch→Act workflow coordinated by adaptive token-gated strategy for reasoning triggers, sketch revision, and action issuance, thereby supporting reactive corrections and human interaction while preserving real-time action prediction.

The paper was published on January 4, 2026 (arXiv:2601.01618).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "146851e3-be35-4385-9151-fdbdd883e529",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "2e7dc98b-145f-474f-8a2c-721232e68b99",
  "sourceToolAssistantUUID": "146851e3-be35-4385-9151-fdbdd883e529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-18T19:40:03.530Z_

Let me get a few more highly relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e7dc98b-145f-474f-8a2c-721232e68b99",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbreP99uDEWcadpRjCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00578715-5da8-4714-996b-f3d57df44e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApUks7qxqTJhggyE1ygMc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1708,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 24464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

_source line 53 · 2026-05-18T19:40:04.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019eGuG48fqVTAQvgEAjbTEy`</summary>

```json
{
  "query": "PALM progress-aware policy learning affordance reasoning long-horizon 2601.07060"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00578715-5da8-4714-996b-f3d57df44e67",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbreP99uDEWcadpRjCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aa6792d-7794-4db1-b4b4-0ab2aa962383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApUks7qxqTJhggyE1ygMc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1708,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 24464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

_source line 54 · 2026-05-18T19:40:04.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011DqAsV5JR161tfMAuk8eeu`</summary>

```json
{
  "query": "Affordance Field Intervention VLA memory traps robotic manipulation 2512.07472"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aa6792d-7794-4db1-b4b4-0ab2aa962383",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbreP99uDEWcadpRjCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e98a1871-96fc-4cdf-a07e-cc8f1f9ebe9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApUks7qxqTJhggyE1ygMc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1708,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 24464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

_source line 55 · 2026-05-18T19:40:04.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WmhFkxDuThXERDNMNtjMVZ`</summary>

```json
{
  "query": "ProGAL-VLA grounded alignment prospective reasoning 2604.09824"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e98a1871-96fc-4cdf-a07e-cc8f1f9ebe9a",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbreP99uDEWcadpRjCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d70619e4-dcb5-40b6-90b4-91a57c03dfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApUks7qxqTJhggyE1ygMc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1708,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 24464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2520,
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

_source line 56 · 2026-05-18T19:40:05.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EAk6zGFEV3HfBdrWEDvS4d`</summary>

```json
{
  "query": "FSD \"From Seeing to Doing\" bridging reasoning decision robotic manipulation 2505.08548"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d70619e4-dcb5-40b6-90b4-91a57c03dfc7",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbreP99uDEWcadpRjCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6a01ea9-ce6e-48cb-9877-698e9197226a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApUks7qxqTJhggyE1ygMc2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1708,
      "cache_creation_input_tokens": 2520,
      "cache_read_input_tokens": 24464,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2520
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1708,
          "output_tokens": 245,
          "cache_read_input_tokens": 24464,
          "cache_creation_input_tokens": 2520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2520,
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

_source line 57 · 2026-05-18T19:40:10.105Z_

<details><summary>↩ Tool result · `toolu_019eGuG48fqVTAQvgEAjbTEy`</summary>

```text
Web search results for query: "PALM progress-aware policy learning affordance reasoning long-horizon 2601.07060"

Links: [{"title":"(PDF) PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://www.researchgate.net/publication/399707765_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_Manipulation"},{"title":"PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/pdf/2601.07060"},{"title":"[2601.07060] PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/abs/2601.07060"},{"title":"PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/html/2601.07060"},{"title":"Learning from 10 Demos: Generalisable and Sample-Efficient Policy Learning with Oriented Affordance Frames","url":"https://arxiv.org/pdf/2410.12124"}]

Based on the search results, here's what I found about PALM (arXiv:2601.07060):

## Overview

PALM is a VLA (vision-language-action) framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.

## Key Technical Approach

PALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control. To further stabilize long-horizon execution, PALM predicts continuous within-subtask progress, enabling seamless subtask transitions.

A diffusion-based policy jointly decodes the robot's action and a continuous progress value, enabling temporal state tracking and seamless subtask transitions in multistep, long-horizon tasks.

## Performance Results

PALM achieves a 91.8% success rate on LIBERO-LONG, a 12.5% improvement in average length on CALVIN ABC→D, and a 2× improvement over real-world baselines across three long-horizon generalization settings.

The paper addresses a significant challenge in robotic manipulation: existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as repeated actions, missed steps, and premature termination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6aa6792d-7794-4db1-b4b4-0ab2aa962383",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "fc07fa5c-c9a2-490c-b1c2-2adf205373ad",
  "sourceToolAssistantUUID": "6aa6792d-7794-4db1-b4b4-0ab2aa962383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T19:40:12.476Z_

<details><summary>↩ Tool result · `toolu_01WmhFkxDuThXERDNMNtjMVZ`</summary>

```text
Web search results for query: "ProGAL-VLA grounded alignment prospective reasoning 2604.09824"

Links: [{"title":"[2604.09824] ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.09824"},{"title":"ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2604.09824"},{"title":"Progressive Multi-granular Alignments for Grounded Reasoning in Large Vision-Language Models","url":"https://arxiv.org/html/2412.08125v1"},{"title":"Progressive Multi-granular Alignments for Grounded Reasoning in Large   Vision-Language Models","url":"https://arxiv.org/pdf/2412.08125"},{"title":"[2412.08125] Progressive Multi-granular Alignments for Grounded Reasoning in Large Vision-Language Models","url":"https://arxiv.org/abs/2412.08125"},{"title":"Progressive Multi-granular Alignments for Grounded Reasoning in Large Vision-Language Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/32471"}]

Based on the search results, I found information about the paper you're looking for:

ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models is an arXiv paper (2604.09824) submitted on April 10, 2026, authored by Nastaran Darabi and Amit Ranjan Trivedi.

The paper presents Prospective Grounding and Alignment VLA (ProGAL-VLA), which constructs a 3D entity-centric graph (GSM), uses a slow planner to produce symbolic sub-goals, and aligns them with grounded entities via a Grounding Alignment Contrastive (GAC) loss.

Vision language action (VLA) models enable generalist robotic agents but often exhibit language ignorance, relying on visual shortcuts and remaining insensitive to instruction changes. The proposed ProGAL-VLA approach aims to address these issues.

On LIBERO-Plus, ProGAL-VLA increases robustness under robot perturbations from 30.3 to 71.5 percent, reduces language ignorance by 3x-4x, and improves entity retrieval from 0.41 to 0.71 Recall@1. On the Custom Ambiguity Benchmark, it reaches AUROC 0.81 (vs. 0.52), AUPR 0.79, and raises clarification on ambiguous inputs from 0.09 to 0.81 without harming unambiguous success.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d70619e4-dcb5-40b6-90b4-91a57c03dfc7",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "0ecc039e-311e-442a-9635-afcf9b1b5c27",
  "sourceToolAssistantUUID": "d70619e4-dcb5-40b6-90b4-91a57c03dfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T19:40:12.602Z_

<details><summary>↩ Tool result · `toolu_01EAk6zGFEV3HfBdrWEDvS4d`</summary>

```text
Web search results for query: "FSD "From Seeing to Doing" bridging reasoning decision robotic manipulation 2505.08548"

Links: [{"title":"[2505.08548] From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation","url":"https://arxiv.org/abs/2505.08548"},{"title":"From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation","url":"https://arxiv.org/html/2505.08548v2"},{"title":"From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=yngvAamNQi"},{"title":"[Literature Review] From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation","url":"https://www.themoonlight.io/en/review/from-seeing-to-doing-bridging-reasoning-and-decision-for-robotic-manipulation"},{"title":"From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation","url":"https://embodied-fsd.github.io/"},{"title":"GitHub - pickxiguapi/Embodied-FSD: Official code for \"From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation\"","url":"https://github.com/pickxiguapi/Embodied-FSD"},{"title":"Robotics May 2025","url":"https://arxiv.org/list/cs.RO/2025-05?skip=300&show=25"}]

Based on the search results, I found comprehensive information about this paper. Here's what I found:

## FSD: From Seeing to Doing

FSD (From Seeing to Doing) is a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained guidance for robotic manipulation.

### The Problem It Addresses

Achieving generalization in robotic manipulation remains a critical challenge, particularly for unseen scenarios and novel tasks. Current Vision-Language-Action (VLA) models, while building on top of general Vision-Language Models (VLMs), still fall short of achieving robust zero-shot performance due to the scarcity and heterogeneity prevalent in embodied datasets.

### Key Technical Approach

The approach combines a hierarchical data pipeline for training with a self-consistency mechanism that aligns spatial coordinates with visual signals. Instead of directly mapping visual inputs to actions, it uses a multi-step reasoning process anchored by object coordinates and spatial relationships.

### Performance Results

FSD achieves 40.6% success rate in SimplerEnv and 72% success rate across 8 real-world tasks, outperforming the strongest baseline by 30%.

The paper was published on arXiv with ID 2505.08548 and was authored by Yifu Yuan and collaborators. The official code and project homepage are available on GitHub and the project website respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6a01ea9-ce6e-48cb-9877-698e9197226a",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "5b17c925-0d9d-4bf1-b8a2-33c87e24d80c",
  "sourceToolAssistantUUID": "c6a01ea9-ce6e-48cb-9877-698e9197226a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T19:40:15.254Z_

<details><summary>↩ Tool result · `toolu_011DqAsV5JR161tfMAuk8eeu`</summary>

```text
Web search results for query: "Affordance Field Intervention VLA memory traps robotic manipulation 2512.07472"

Links: [{"title":"[2512.07472] Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://www.arxiv.org/abs/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"},{"title":"Robotics Dec 2025","url":"https://arxiv.org/list/cs.RO/2025-12?skip=225&show=25"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"}]

Based on the search results, here's what I found about this paper:

## Overview

Vision-Language-Action (VLA) models have shown great performance in robotic manipulation by mapping visual observations and language instructions directly to actions. However, they remain brittle under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is a failure mode referred to as the "Memory Trap".

## The Proposed Solution

Affordance Field Intervention (AFI) is a lightweight hybrid framework that uses Spatial Affordance Fields (SAFs) as an on-demand plug-in to guide VLA behavior. The system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions, with a SAF-based scorer selecting trajectories with the highest cumulative affordance.

## Results

The method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark.

The paper was published on arXiv on December 8, 2025, by authors Siyu Xu, Zijian Wang, Yunke Wang, Chenghao Xia, Tao Huang, and Chang Xu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e98a1871-96fc-4cdf-a07e-cc8f1f9ebe9a",
  "isSidechain": true,
  "promptId": "3b0ac660-c69c-40e8-a93b-4c0721e7702c",
  "agentId": "a99e4c4020376a997",
  "type": "user",
  "uuid": "bac41cf6-59d5-4096-aabc-6eaaf95bcddf",
  "sourceToolAssistantUUID": "e98a1871-96fc-4cdf-a07e-cc8f1f9ebe9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-18T19:41:39.233Z_

Here is a comprehensive report of the most relevant competing and related work found across all searches. I have organized them by category, with the most directly relevant papers first.

---

## CATEGORY 1: Affordance-Structured Reasoning in VLA Models (Most Directly Related)

### 1. CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance
- **arXiv:** 2412.20451 | **Venue:** ICCV 2025
- Introduces "Chain-of-Affordance" reasoning with four affordance types: object affordance (what/where to manipulate), grasp affordance (which part to grasp), spatial affordance (where to place), and movement affordance (collision-free path). Each affordance is transformed into both visual and textual formats, injected into the policy network via a vision-language co-injection module. Outperforms OpenVLA and Octo. Strong generalization to unseen poses, free space identification, and obstacle avoidance.
- **This is likely the single most relevant competing work** -- it directly combines affordance-structured reasoning with VLA models in an end-to-end manner.

### 2. PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation
- **arXiv:** 2601.07060 | **Date:** January 2026
- A VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues. Distills complementary affordance representations (object relevance, contact geometry, spatial placements, motion dynamics). Uses a diffusion-based policy that jointly decodes actions and continuous progress values. Achieves 91.8% on LIBERO-LONG, +12.5% on CALVIN ABC->D.

### 3. VLA-R1: Enhancing Reasoning in Vision-Language-Action Models
- **arXiv:** 2510.01623 | **Date:** October 2025
- Integrates RLVR (Reinforcement Learning from Verifiable Rewards) with GRPO to optimize both reasoning and execution. Develops VLA-CoT-13K, a dataset with chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Uses verifiable rewards for region alignment, trajectory consistency, and output formatting. Directly addresses reasoning robustness.
- **Highly relevant** -- explicitly combines affordance-aligned CoT with optimization-level reinforcement, comparing data-level vs. optimization-level approaches.

### 4. Affordance Field Intervention (AFI): Enabling VLAs to Escape Memory Traps in Robotic Manipulation
- **arXiv:** 2512.07472 | **Date:** December 2025
- Addresses VLA brittleness under distribution shift via "Spatial Affordance Fields" as a plug-in to guide VLA behavior. Detects memory traps through proprioception, repositions robots to high-affordance regions. +23.5% improvement on real-world OOD scenarios, +20.2% on LIBERO-Pro.

### 5. Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring
- **arXiv:** 2603.22899 | **Date:** March 2026
- Uses implicit affordance anchoring for industrial manipulation tasks. Compares five open-source embodied models (Transporter, RT-1, RVT, Octo-Base, OpenVLA).

---

## CATEGORY 2: Chain-of-Thought / Intermediate Reasoning for VLA Models

### 6. CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models
- **arXiv:** 2503.22020 | **Venue:** CVPR 2025
- Predicts future image frames autoregressively as visual goals before generating action sequences. +17% over state-of-the-art VLA in real-world tasks, +6% in simulation. Uses visual (not textual) reasoning as the intermediate representation.

### 7. DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models
- **arXiv:** 2511.15669 | **Date:** October 2025
- Hybrid-attention decoder with causal attention for sequential CoT generation and bidirectional attention for parallel action decoding. Two-stage training: SFT for foundational reasoning, then RL with task-success rewards. 2.9B parameters, 96.5% average success rate, 0.175x latency of autoregressive baselines.

### 8. Latent Reasoning VLA (LaRA-VLA): Latent Thinking and Prediction for Vision-Language-Action Models
- **arXiv:** 2602.01166 | **Date:** February 2026
- Internalizes multi-modal CoT reasoning into continuous latent representations. Curriculum-based training transitioning from explicit textual/visual CoT to latent reasoning. Reduces inference latency by up to 90% compared to explicit CoT approaches while maintaining performance.

### 9. ECoT / ECoT-Lite: Embodied Chain-of-Thought Reasoning & Training Strategies for Efficient Embodied Reasoning
- **arXiv:** 2407.08693 (ECoT) and 2505.08243 (ECoT-Lite) | **Venues:** CoRL 2024 / 2025
- ECoT trains VLAs on multi-step reasoning (plans, sub-tasks, motions, bounding boxes, end-effector positions). +28% absolute success rate for OpenVLA. ECoT-Lite introduces efficient alternatives: reasoning dropout, thinking tokens, co-training. Achieves SOTA on LIBERO, +10-19% on BridgeData V2, while running at 3.5+ Hz (vs. 1-1.2 Hz for full ECoT).
- **Highly relevant** -- ECoT-Lite directly compares different types of intermediate reasoning (textual CoT, thinking tokens, reasoning dropout) and analyzes WHY reasoning helps (representation learning, curricularization, expressivity).

### 10. GraphCoT-VLA: A 3D Spatial-Aware Reasoning Vision-Language-Action Model for Robotic Manipulation with Ambiguous Instructions
- **arXiv:** 2508.07650 | **Date:** August 2025
- Structured CoT module integrating high-level task planning, failed task feedback, and low-level imaginative reasoning. Constructs real-time updatable 3D Pose-Object graphs capturing spatial configurations and topological relationships.

### 11. ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models
- **arXiv:** 2604.09824 | **Date:** April 2026
- Constructs 3D entity-centric graphs, uses slow planner for symbolic sub-goals, aligns them with grounded entities via Grounding Alignment Contrastive loss. On LIBERO-Plus: robustness under robot perturbations from 30.3% to 71.5%, language ignorance reduced 3-4x. Very recent and directly evaluates on LIBERO-Plus.

---

## CATEGORY 3: Visual / Spatial Intermediate Representations for Manipulation

### 12. Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation
- **arXiv:** 2601.01618 | **Date:** January 2026
- Introduces "Visual Sketch" as an intermediate representation (points, boxes, arrows, typed relations rendered onto current views). See-Think-Sketch-Act workflow with adaptive token-gated strategy.

### 13. FSD (From Seeing to Doing): Bridging Reasoning and Decision for Robotic Manipulation
- **arXiv:** 2505.08548 | **Date:** May 2025
- Generates intermediate representations through spatial relationship reasoning. Uses hierarchical data pipeline with self-consistency mechanism. 40.6% success rate in SimplerEnv, 72% across 8 real-world tasks (+30% over strongest baseline).

### 14. RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation
- **arXiv:** 2411.02704 | **Date:** November 2024
- Hierarchical model: first proposes affordance plan given task language, then conditions policy on affordance plan. Bridges heterogeneous supervision (web datasets + robot trajectories). Exceeds prior methods by 50%+ and shows robustness to novel settings.

### 15. RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation
- **arXiv:** 2602.09973 | **Venue:** ICLR 2026
- Large-scale dataset (230k+ episodes, 571 scenes) with 10+ categories of intermediate representations (subtasks, skills, segmentation, affordance boxes, grasp poses, contact points, etc.). Plan-then-execute VLA framework supporting modular and end-to-end variants.

### 16. Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning
- **arXiv:** 2412.03293 | **Venue:** ICML 2025
- Combines autoregressive reasoning with diffusion-based action generation. Reasoning injection module integrates reasoning directly into policy learning. 2B parameter model runs at 82Hz on a single A6000.

---

## CATEGORY 4: VLA Robustness Analysis and Benchmarks

### 17. LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models
- **arXiv:** 2510.13626 | **Date:** October 2025
- Diagnostic benchmark with 10,030 tasks across 7 perturbation factors and 21 components (object layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise). Reveals VLA models drop from 95% to below 30% under modest perturbations. Most models ignore language instructions.

### 18. Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation
- **arXiv:** 2603.12717 | **Date:** March 2026
- Seven text corruptions across three attacker tiers applied to reasoning VLA on 40 LIBERO tasks. **Key finding:** Object name substitution reduces success by 8.3pp (up to -45pp on individual tasks), but sentence reordering, spatial-direction reversal, token noise, and LLM-crafted wrong plans have negligible impact. Concludes that action decoders depend on entity-reference integrity rather than reasoning quality or sequential structure.
- **Directly relevant** -- this is the most targeted study comparing what aspects of CoT reasoning actually matter for VLA manipulation.

### 19. Do World Action Models Generalize Better than VLAs? A Robustness Study
- **arXiv:** 2603.22078 | **Date:** March 2026
- Compares World Action Models (WAMs) vs VLAs on robustness. WAMs (e.g., LingBot-VA at 74.2% on RoboTwin 2.0-Plus, Cosmos-Policy at 82.2% on LIBERO-Plus) generally generalize better to visual noise and layout changes due to spatiotemporal priors from video pretraining.

---

## CATEGORY 5: Other Affordance-Adjacent Work

### 20. Afford-X: Generalizable and Slim Affordance Reasoning for Task-oriented Manipulation
- **arXiv:** 2503.03556 | **Date:** 2025
- End-to-end trainable affordance reasoning model (187M parameters). +12.1% over best non-LLM methods, 50x faster than GPT-4V API. Trained on LVIS-Aff (1,496 tasks, 119k images). Focuses on affordance perception rather than action generation.

### 21. AffordanceLLM: Grounding Affordance from Vision Language Models
- **arXiv:** 2401.06341 | **Date:** January 2024
- Leverages pretrained VLMs for affordance grounding. Generalizes to unseen objects and actions from random Internet images.

### 22. LMAffordance3D (CVPR 2025): Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions
- **arXiv:** 2504.04744 | **Date:** April 2025
- First multi-modal, language-guided 3D affordance grounding network. Fuses 2D and 3D spatial features with semantic features via a VLM.

---

## Summary of Key Gaps and Overlaps

**Papers most likely to overlap with an "open-vocabulary affordance reasoning for VLA" proposal:**
1. **CoA-VLA** (arXiv:2412.20451) -- The closest competitor: affordance-structured reasoning explicitly integrated into VLA models
2. **VLA-R1** (arXiv:2510.01623) -- CoT supervision aligned with affordance annotations + RLVR optimization
3. **PALM** (arXiv:2601.07060) -- Affordance reasoning for long-horizon VLA with progress tracking
4. **ProGAL-VLA** (arXiv:2604.09824) -- Grounded alignment addressing language ignorance, evaluated on LIBERO-Plus

**Papers most relevant to "comparing different types of intermediate reasoning":**
1. **ECoT-Lite** (arXiv:2505.08243) -- Directly compares reasoning types and analyzes why reasoning helps
2. **Altered Thoughts, Altered Actions** (arXiv:2603.12717) -- Shows entity references matter more than reasoning quality
3. **LaRA-VLA** (arXiv:2602.01166) -- Latent vs. explicit reasoning comparison
4. **DeepThinkVLA** (arXiv:2511.15669) -- Architectural comparison (causal vs. bidirectional attention for reasoning vs. actions)

**Papers most relevant to "VLA robustness under distribution shift":**
1. **LIBERO-Plus** (arXiv:2510.13626) -- The primary robustness benchmark
2. **AFI** (arXiv:2512.07472) -- Affordance-based intervention for OOD robustness
3. **WAMs vs VLAs** (arXiv:2603.22078) -- Comparative robustness study
4. **ProGAL-VLA** (arXiv:2604.09824) -- Robustness on LIBERO-Plus from 30.3% to 71.5%

Sources:
- [CoA-VLA](https://arxiv.org/abs/2412.20451)
- [VLA-R1](https://arxiv.org/abs/2510.01623)
- [PALM](https://arxiv.org/abs/2601.07060)
- [ProGAL-VLA](https://arxiv.org/abs/2604.09824)
- [CoT-VLA](https://arxiv.org/abs/2503.22020)
- [DeepThinkVLA](https://arxiv.org/abs/2511.15669)
- [LaRA-VLA](https://arxiv.org/abs/2602.01166)
- [ECoT](https://arxiv.org/abs/2407.08693)
- [ECoT-Lite](https://arxiv.org/abs/2505.08243)
- [GraphCoT-VLA](https://arxiv.org/abs/2508.07650)
- [Action-Sketcher](https://arxiv.org/abs/2601.01618)
- [FSD](https://arxiv.org/abs/2505.08548)
- [RT-Affordance](https://arxiv.org/abs/2411.02704)
- [RoboInter (ICLR 2026)](https://arxiv.org/abs/2602.09973)
- [Diffusion-VLA](https://arxiv.org/abs/2412.03293)
- [LIBERO-Plus](https://arxiv.org/abs/2510.13626)
- [Altered Thoughts, Altered Actions](https://arxiv.org/abs/2603.12717)
- [WAMs vs VLAs Robustness Study](https://arxiv.org/abs/2603.22078)
- [Affordance Field Intervention](https://arxiv.org/abs/2512.07472)
- [Agile-VLA](https://arxiv.org/abs/2603.22899)
- [Afford-X](https://arxiv.org/abs/2503.03556)
- [AffordanceLLM](https://arxiv.org/abs/2401.06341)
- [LMAffordance3D](https://arxiv.org/abs/2504.04744)
- [Awesome Embodied VLA list](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bac41cf6-59d5-4096-aabc-6eaaf95bcddf",
  "isSidechain": true,
  "agentId": "a99e4c4020376a997",
  "requestId": "req_011CbAbshVh9ocXSyhU3Q5tn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "badc1605-4a30-42e8-8a54-0e360771a693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "667874d5-2882-4ef0-8f21-37f1ca12ff81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5irBY8R7KkkKFof1E6cpe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1475,
      "cache_creation_input_tokens": 3232,
      "cache_read_input_tokens": 26984,
      "output_tokens": 4137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1475,
          "output_tokens": 4137,
          "cache_read_input_tokens": 26984,
          "cache_creation_input_tokens": 3232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3232,
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
